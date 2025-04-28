use std::collections::HashMap;
use std::collections::HashSet;
use std::env;
use std::fs;
use std::path::Path;

type Dict = HashMap<String, HashSet<String>>;

fn serialize_map(map: Dict, filename: &Path) {
    let mut lines: Vec<String> = ["phf_map!(\n".into()].into();
    for (ext, tags) in map.iter() {
        lines.push(format!(r#"    "{ext}" => phf_set!("#));
        for tag in tags {
            lines.push(format!(r#""{tag}", "#));
        }
        lines.push("),\n".into());
    }
    lines.push(")".into());
    fs::write(filename, lines.join("")).unwrap();
}

fn main() {
    // We want to create a series of hashmaps from
    //   identify/{extensions,interpreters}.py
    // and place them in `out_dir/{extensions,interpreters}.rs`
    // (or name each file after the dict, I suppose)

    let mut extensions: Dict = HashMap::new();
    let mut extensions_need_binary_check: Dict = HashMap::new();
    let mut names: Dict = HashMap::new();
    let mut interpreters: Dict = HashMap::new();
    let mut current_dict = String::new();

    // take a python file
    let mut python = fs::read_to_string("identify/extensions.py").unwrap();
    python.push_str(&fs::read_to_string("identify/interpreters.py").unwrap());

    // read the dicts into hashmaps
    for line in python.lines() {
        if let Some((dict_name, _)) = line.split_once('=') {
            current_dict = dict_name.trim().into();
        }
        else if let Some((ext, tags)) = line.split_once(':') {
            let ext = ext.trim().replace('\'', "").to_string();
            let tags: HashSet<String> = tags.trim()
                .split(',')
                .map(|tag|
                    tag.trim().replace(|c| "'{}".contains(c), "")
                )
                .filter(|tag| !tag.is_empty())
                .collect();

            match current_dict.as_str() {
                "EXTENSIONS" => extensions.insert(ext, tags),
                "EXTENSIONS_NEED_BINARY_CHECK" => {
                    extensions_need_binary_check.insert(ext, tags)
                },
                "NAMES" => names.insert(ext, tags),
                "INTERPRETERS" => interpreters.insert(ext, tags),
                _ => panic!("Unexpected dict name: {current_dict}"),
            };
        }
    }

    // write them into a rust file
    let out_dir = env::var_os("OUT_DIR").unwrap();

    let extensions_rs = Path::new(&out_dir).join("extensions.rs");
    let enbc_rs = Path::new(&out_dir).join("extensions_need_binary_check.rs");
    let names_rs = Path::new(&out_dir).join("names.rs");
    let interpreters_rs = Path::new(&out_dir).join("interpreters.rs");
    serialize_map(extensions, &extensions_rs);
    serialize_map(extensions_need_binary_check, &enbc_rs);
    serialize_map(names, &names_rs);
    serialize_map(interpreters, &interpreters_rs);

    println!("cargo:rerun-if-changed=build.rs");
}

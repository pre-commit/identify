use std::collections::HashMap;
use std::collections::HashSet;


fn main() {
    let extensions: HashMap<&str, HashSet<&str>> = include!(
        concat!(env!("OUT_DIR"), "/extensions.rs")
    );
    let extensions_need_binary_check: HashMap<&str, HashSet<&str>> = include!(
        concat!(env!("OUT_DIR"), "/extensions_need_binary_check.rs")
    );
    let names: HashMap<&str, HashSet<&str>> = include!(
        concat!(env!("OUT_DIR"), "/names.rs")
    );
    let interpreters: HashMap<&str, HashSet<&str>> = include!(
        concat!(env!("OUT_DIR"), "/interpreters.rs")
    );

    println!("{:?}", extensions["bash"]);
    println!("{:?}", extensions_need_binary_check["ppm"]);
    println!("{:?}", names[".flake8"]);
    println!("{:?}", interpreters["python3"]);
}

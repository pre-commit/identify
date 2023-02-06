#![allow(dead_code)]
#![allow(unused_imports)]
#![allow(unused_variables)]
#![allow(unused_mut)]

use std::collections::HashMap;
use std::collections::HashSet;
use std::ffi::OsStr;
use std::ffi::OsString;
use std::fs;
use std::os::unix::fs::FileTypeExt; // For `filetype.is_socket()` apparently
// use std::os::unix::fs::PermissionsExt; // fs::Permissions `mode()`
use std::os::unix::fs::MetadataExt; // fs::Permissions `mode()`
use std::path::Path;

use crate::tags;

#[derive(Debug, Eq, Hash, PartialEq)]
pub enum Tags {
    Directory,
    Symlink,
    Socket,
    File,
    Executable,
    NonExecutable,
    Text,
    Binary,
}

pub fn tags_from_path(file_path: &str) -> HashSet<Tags> {
    let file = Path::new(file_path);
    // TODO: Convert to Error
    if !file.exists() {
        panic!("{file_path} does not exist.");
    }

    let metadata = fs::symlink_metadata(&file);

    if let Ok(metadata) = metadata {
        // let perms = metadata.mode() & 0o777;
        // println!("{:o}", perms);
        if metadata.is_symlink() {
            return HashSet::from([Tags::Symlink]);
        }
        if metadata.is_dir() {
            return HashSet::from([Tags::Directory]);
        }
        if metadata.file_type().is_socket() {
            return HashSet::from([Tags::Socket]);
        }
    }

    let tags = HashSet::from([Tags::File]);
    // TODO
    // If executable, add to `tags`

    let t = tags_from_filename(file_path);
    // see if we can get tags_from_filename() and if not,
    //   then... weird parse_shebang stuff?

    // a lil more. reread it when not tired.
    tags
}

pub fn tags_from_filename(filename: &str) -> HashSet<String> {
    let path = Path::new(filename);
    let filename = path.file_name().unwrap().to_str().unwrap().to_string();
    let ext = path.extension().unwrap().to_str().unwrap().to_lowercase();

    let mut ret = HashSet::new();
    /*
    let _: Vec<&str> = filename.split('.').collect();
    let mut parts = Vec::from([filename.clone()]);
    parts.extend(filename.split('.').map(|s| s.to_string()));

    for part in parts {
        if tags::NAMES.contains_key(&part) {
            println!("{:?}", tags::NAMES[&part]);
            // ret.push(tags::NAMES[&part]);
        }
        println!("Boop: {}", part);
    }
    */

    if tags::EXTENSIONS.contains_key(&ext) {
        ret.extend(tags::EXTENSIONS[&ext].iter().map(|s| s.to_string()));
    } else if tags::EXTENSIONS_NEED_BINARY_CHECK.contains_key(&ext) {
        ret.extend(
            tags::EXTENSIONS_NEED_BINARY_CHECK[&ext]
                .iter()
                .map(|s| s.to_string()),
        );
    }
    /*
    for part in Vec::from([
        filename.clone(),
        filename.split('.').map(|s| s.to_string()).collect()
    ]) {
        println!("Boop: {}", part);
    }
    */

    // identify.py creates a set, then,
    //   if filename + filename.split('.') items in extensions.NAMES,
    //   add to set and break
    /*
    let mut map = HashSet::new();
    if filename in extensions::names() {
        map.insert(extension);
    }
    */

    // if there's an extension,
    //   lowercase it,
    //   then if it's in extension.EXTENSIONS, add to set
    //   or if it's in extension.EXTENSIONS_NEED_BINARY_CHECK, add to set
    // return set

    /*
        let mut tags: HashSet<String> = HashSet::new();
        if let Some(name) = path.file_name().and_then(OsStr::to_str) {
            tags.insert(name.to_owned());
        }
        if let Some(ext) = path.extension().and_then(OsStr::to_str) {
            tags.insert(ext.to_owned());
        }
    */
    // Get filename and extension
    // Allow "Dockerfile.xenial" to also match "Dockerfile"
    // If filename in extensions.NAMES, add
    // If extension in EXTENSIONS, add
    // tags
    ret
}

pub fn tags_from_interpreter(interpreter: &str) -> HashSet<String> {
    HashSet::new()
}

pub fn is_text(/* bytes io */) -> bool {
    false
}

pub fn file_is_text(path: &str) -> bool {
    false
}

/*
pub fn parse_shebang( /* bytesio */) -> tuple of unknown size? {
}


pub fn parse_shebang_from_file(path: PathBuf) -> tuple of unknown size? {
}
*/

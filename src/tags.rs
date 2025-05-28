use phf::phf_map;
use phf::phf_set;


pub const NAMES: phf::Map<&str, phf::Set<&str>> =
    include!(concat!(env!("OUT_DIR"), "/names.rs"));

pub const EXTENSIONS: phf::Map<&str, phf::Set<&str>> =
    include!(concat!(env!("OUT_DIR"), "/extensions.rs"));

pub const EXTENSIONS_NEED_BINARY_CHECK: phf::Map<&str, phf::Set<&str>> =
    include!(concat!(env!("OUT_DIR"), "/extensions_need_binary_check.rs"));

pub const INTERPRETERS: phf::Map<&str, phf::Set<&str>> =
    include!(concat!(env!("OUT_DIR"), "/interpreters.rs"));

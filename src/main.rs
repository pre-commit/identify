use std::env;

mod identify;
mod tags;

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    if args.len() < 1 {
        eprintln!("Usage: identify [--filename-only] FILE");
        return;
    }

    if args[0] == "--filename-only" {
        println!("{:?}", identify::tags_from_filename(&args[1]));
    } else {
        println!("{:?}", identify::tags_from_path(&args[0]));
    }
}

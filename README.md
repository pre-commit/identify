identify
========

File identification library for Python.

Given a file (or some information about a file), return a set of standardized
tags identifying what the file is.


## Usage
### With a file on disk

If you have an actual file on disk, you can get the most information possible
(a superset of all other methods):

```python
>>> identify.tags_from_path('/path/to/file.py')
{'file', 'text', 'python', 'non-executable'}
>>> identify.tags_from_path('/path/to/file-with-shebang')
{'file', 'text', 'shell', 'bash', 'executable'}
>>> identify.tags_from_path('/bin/bash')
{'file', 'binary', 'executable'}
>>> identify.tags_from_path('/path/to/directory')
{'directory'}
>>> identify.tags_from_path('/path/to/symlink')
{'symlink'}
```

When using a file on disk, the checks performed are:

* File type (file, symlink, directory)
* Mode (is it executable?)
* File name (mostly based on extension)
* If executable, the shebang is read and the interpreter interpreted


### If you only have the filename

```python
>>> identify.tags_from_filename('file.py')
{'text', 'python'}
```


### If you only have the interpreter

```python
>>> identify.tags_from_interpreter('python3.5')
{'python', 'python3', 'python3.5'}
>>> identify.tags_from_interpreter('bash')
{'shell', 'bash'}
>>> identify.tags_from_interpreter('some-unrecognized-thing')
set()
```


## How it works

A call to `tags_from_path` does this:

1. What is the type: file, symlink, directory? If it's not file, stop here.
2. Is it executable? Add the appropriate tag.
3. Do we recognize the file extension? If so, add the appropriate tags, stop
   here. These tags would include binary/text.
4. Peek at the first X bytes of the file. Use these to determine whether it is
   binary or text, add the appropriate tag.
5. If identified as text above, try to read and interpret the shebang, and add
   appropriate tags.

By design, this means we don't need to partially read files where we recognize
the file extension.

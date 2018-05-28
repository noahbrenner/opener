# Opener

> A simple tool for opening a set of programs

**This project is in initial development. The documentation below describes the intended behavior, but not all of it is implemented yet.**

**Opener** simplifies a workflow that requires opening multiple windows/programs/web pages for a given project. The settings for a given workflow are read from a text file. The text file uses a subset of [INI][] syntax, which allows for some basic syntax highlighting in many text editors.

An example input file:

```ini
[chrome]
https://www.google.com
https://wikipedia.org

[vim]
cwd = /path/to/dir
-o
file.txt
.otherfile

# separate vim window
/path/to/specific/file.ini
```

* The lines in a particular grouping are processed as command line arguments to the program in the containing `[heading]` section.
* `cwd` sets the current working directory.
* Blank lines separate distinct calls to the same program, if they still fall under its heading.
* Comments may be included. They must be on their own line and start with `#`.
* Some heading text (program names) are treated as special cases, and an extension mechanism will likely be added at some point. For example:
    * `chrome` will search for an existing, compatible program. This includes chromium and other variations.
    * The `cwd` for vim is enforced by adding a `-c "cd {your cwd}"` option to the call to enforce the setting even if vim sets it's working directory based on the first input file passed to it.


## Installation and Usage

First, make sure you have [Python 3][] installed. Then, clone or download this repository. There are no external dependencies outside the standard library.

* If you're using Linux or Mac, you may want to run `chmod +x opener.py` so that you can execute the file directly without explicitly calling Python.
* If youre using Windows, you may want to make sure that **Python 3** is set as the default program for `.py` files.

The two main ways to run the **Opener** are:

1. In a terminal, run `$ opener.py your_file.ini` (or `python3 opener.py your_file.ini` if you didn't take one of the steps above).
2. Create a shortcut/alias/etc. to `opener.py` in a convenient location (like your desktop). You can then drag an `.ini` file onto that shortcut to run it. This option does require that you took one of the above steps, allowing you to run a `.py` file directly without explicitly calling the Python interpreter.


## Versioning

A versioning scheme has not been established for this project yet, but it will likely be [Semantic Versioning][semver]. At this point, you can consider the major version number to be `0`.


## Contributing

Since this is a tool very specific to my own needs, I'm not anticipating a lot of contribution, but **contributions are always welcome!** Before you jump in, please read the [Code of Conduct](CODE_OF_CONDUCT.md).


[INI]: https://en.wikipedia.org/wiki/INI_file
[Python 3]: https://www.python.org/downloads/
[semver]: http://semver.org/

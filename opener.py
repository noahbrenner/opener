#!/usr/bin/python3
from subprocess import Popen
from shutil import which
from read_ini import read_ini

# TODO decide if I want to use shlex.quote()
# https://docs.python.org/3/library/shlex.html#shlex.quote


# TODO Create ability to register functions which act on certain program names


PROGRAM_PATH_CACHE = {}

def get_program_path(program):
    if program in PROGRAM_PATH_CACHE:
        return PROGRAM_PATH_CACHE[program]
    else:
        path = which(program)
        PROGRAM_PATH_CACHE[program] = path
        return path



def open_items(items):
    """Open the files/urls from the `items` data structure.

    Arguments:

      items:
        [
            ('program', [
                ('working_directory', ['command', 'line', 'arguments']),
                ... # More instances of opening 'program'.
            ]),
            ... # More programs to open instances of.
        ]
    """
    for program, program_windows in items:
        for directory, args in program_windows:
            print(program, directory, args)
            Popen([program] + args, cwd=directory,
                  close_fds=True, start_new_session=True)


def main(file_path=None):
    """Open the programs and files specified in the .ini file 'file_path'."""
    data = read_ini(file_path)
    open_items(data)
    print(get_program_path('chrome'))


if __name__ == '__main__':
    main()

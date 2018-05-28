# TODO
# - Write a class docstring
class Task:
    # Disallow the addition of non-default attributes
    __slots__ = ['name', 'cwd', 'args']

    def __init__(self, program_name, cwd=None, args=None):
        """Create new Task instance."""
        self.name = program_name
        self.cwd = cwd
        # TODO mayber call this `lines` instead
        # and use `args` for the filtered list, excluding comments?
        self.args = args if args else []

    # TODO save the actual lines from the input file,
    # but also provide a function that returns a list without comments, etc.
    def add_arg(self, arg):
        """Add command line argument(s) to this Task instance."""
        if isinstance(arg, str):
            self.args.append(arg)
        elif isinstance(arg, list):
            self.args.extend(arg)
        else:
            raise TypeError

    # TODO use calculated version of args insted (to remove comments, etc.)
    def __str__(self):
        """Return an approximation of the command line to be run."""
        return ''.join([
            f'cd {self.cwd}; ' if self.cwd else '', # only if cwd is defined
            self.name + ' ',
            ' '.join(repr(arg) for arg in self.args)
        ])

    def __repr__(self):
        """Return a string that could be evaluated to recreate this object."""
        return f'Task({self.name}, cwd={self.cwd}, args={self.args})'

    def source(self):
        """Return an .ini file representation for this object.

        Do not include the program name. This enables a recreation
        of the original source file, which groups multiple instances
        of a single program in a single [program] section.
        """
        cwd = f'cwd = {self.cwd}\n' if self.cwd else ''
        return cwd + '\n'.join(self.args)

    def source_standalone(self):
        """Return a standalone .ini file representation of this object.

        The program name is included in it's own section as [program]
        """
        return f'[{self.name}]\n{self.source()}'


if __name__ == '__main__':
    test = Task('gvim', args=['-o', 'test1.txt'])
    test.add_arg('# a comment')
    test.add_arg(['test2.ini'])
    print('\nstr:\n' + str(test))
    print('\nrepr:\n' + repr(test))
    print('\nsource:\n' + test.source())
    print('\nsource_standalone:\n' + test.source_standalone())

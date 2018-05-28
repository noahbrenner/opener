def read_ini(file_path):
    return [
            ('program1', [
                ('working_directory1', ['command', 'line', 'arguments']),
                ('working_directory2', ['other', 'arguments'])
                ]),
            ('program2', [
                ('working_directory3', ['different', 'arguments']),
                ('working_directory4', ['more', 'things'])
                ])
            ]


if __name__ == '__main__':
    from pprint import pprint
    pprint(read_ini())

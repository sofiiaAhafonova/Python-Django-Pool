import sys
import re
import os
from settings import *

def parse_template(data):
    return data.format_map(globals())

def read_template_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        exit(f'Please, enter correct file path. {e.strerror} "{filename}"')
    except IsADirectoryError as e:
        exit(f'Please, enter correct file path. {e.strerror}: "{filename}"')
    except PermissionError as e:
        exit(f'Please, enter path to file with correct permissions. {e.strerror}: "{filename}"')
    except Exception as e:
        exit(f'Ooops, something went wrong. {str(e)}')


def write_to_html_file(file_title, data):
    with open(file_title + '.html', 'w') as file:
        file.write(data)


def render(filename):
    file_title, extension = os.path.splitext(filename)
    if extension != '.template':
        exit('Please, enter file with extension .template')
    template_data = read_template_file(filename)
    try:
        result = parse_template(template_data)
        write_to_html_file(file_title, result)
    except Exception as e:
        exit(f'Ooops, something went wrong. {str(e)}')


def main():
    if len(sys.argv) == 2:
        render(sys.argv[1])
    else:
        exit('Please, enter the name of template file')

if __name__ == "__main__":
    main()

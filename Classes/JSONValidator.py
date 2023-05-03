from argparse import ArgumentParser
import os
import json


error_found = False

def get_files():
    parser = ArgumentParser()
    parser.add_argument('-p', '--path', help='Path to the JSONs directory', dest='path')
    args = parser.parse_args()
    path = args.path

    jsons = []

    for root, directories, files in os.walk(path):
        for file in files:
            if '.json' in file:
                jsons.append(os.path.join(root, file))

    return jsons


def get_file_content(file):
    with open(file, 'r') as file:
        file_content = file.read()
    
    return file_content


def get_line_number(error):
    error = str(error)

    start_index = error.find("line") + 5
    end_index = error.find(" ", start_index, len(error))
    
    line_number = error[start_index: end_index] if start_index != end_index else error[start_index]

    return line_number


def parse(file):
    file_content = get_file_content(file)

    try:
        json.loads(file_content)
    except ValueError as error:
        global error_found
        
        error_found = True
        line_number = get_line_number(error)
        
        print(f"{file}:{line_number}: error: {error}")


def validate():
    files = get_files()
    
    for file in files:
        parse(file)


validate()
exit(1 if error_found else 0)

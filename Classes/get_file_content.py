def get_file_content(file):
    with open(file, 'r') as file:
        file_content = file.read()
    
    return file_content

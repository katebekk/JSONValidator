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


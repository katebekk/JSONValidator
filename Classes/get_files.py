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

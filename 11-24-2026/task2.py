def read_file(file_name: str) -> str:
    try:
        file = open(file_name, 'rb')
    except:
        print("Could not open file: ", file_name)
        return None

    content = file.read()
    file.close()
    return content

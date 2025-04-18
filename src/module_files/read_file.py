import json

def read_file(path):
    file = open(path, "r") 
    try:
        print("reading from " + str(path))
        contents = file.read()
    except Exception as e:
        print(e)
    finally:
        file.close()
    
    return json.loads(contents)
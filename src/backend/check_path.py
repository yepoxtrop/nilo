import os;

def check_path(path:str):
    if os.path.exists(path):
        return True
    else:
        return False
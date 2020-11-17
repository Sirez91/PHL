from pathlib import Path

def fileExists(path):
    my_file = Path(path)
    if my_file.is_file():
        # file exists
        return True
    else:
        return False

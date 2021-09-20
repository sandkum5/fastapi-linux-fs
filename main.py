from fastapi import FastAPI
import os
from pathlib import Path

app = FastAPI()

# This function
@app.get("/")  # Path Operation Decorator
def read_root():  # Path operation Function
    # return {"Hello": "World"}
    data_dict: dict = {}
    path = Path("/")
    data = os.listdir(path)
    data_dict[path] = data
    return data_dict


# This function list directory files or file contents based on the specified path.
# E.g.
# If the path is a director, it will return the directory files.
# If the path is a file, it will return the contents of the file.
@app.get("/{file_path:path}")
def get_path(file_path):
    path = Path(f"/{file_path}")
    data_dict: dict = {}
    if path.exists():
        if path.is_file():
            with open(path) as f:
                data = f.read()
                data_dict[path] = data
        elif path.is_dir():
            data = os.listdir(path)
            data_dict[path] = data
        return data_dict
    else:
        return "Path doesn't Exist"

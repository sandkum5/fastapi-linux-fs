#!/usr/bin/env python3

from fastapi import FastAPI
import os
from pathlib import Path

app = FastAPI()

#
# This function returns the directories in root directory.
#
@app.get("/")  # Path Operation Decorator
def read_root():  # Path operation Function
    # We are creating a data_dict. We are clearly stating its a dict.
    data_dict: dict = {}
    path = Path("/")
    # data = os.listdir(path)
    data_dict[path] = os.listdir(path)
    return data_dict


#
# This function list directory files or file contents based on the specified path.
# E.g.
# If the path is a directory, it will return the directory files.
# If the path is a file, it will return the contents of the file.
#
@app.get("/{file_path:path}")
def get_path(file_path):
    path = Path(f"/{file_path}")
    data_dict: dict = {}
    if path.exists():
        if path.is_file():
            with open(path) as f:
                # data = f.read()
                data_dict[path] = f.read()
        elif path.is_dir():
            # data = os.listdir(path)
            data_dict[path] = os.listdir(path)
        return data_dict
    else:
        return "Path doesn't Exist"

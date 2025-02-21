import json
import os

json_files = []

column_mappings = {}

for json_file_path in json_files:
    try:
     
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        if isinstance(data, list) and len(data) > 0:
  
            keys = data[0].keys()
            column_mappings[os.path.basename(json_file_path)] = list(keys)
        else:
            column_mappings[os.path.basename(json_file_path)] = "The JSON file does not contain a list of records or is empty."
    except Exception as e:
        column_mappings[os.path.basename(json_file_path)] = f"Error loading file: {e}"

for file, columns in column_mappings.items():
    print(f"File: {file}")
    print("Columns:", columns)
    print()

import os

def write_file(working_directory, file_path, content):
    try:
        abs_wd = os.path.abspath(working_directory)
        abs_filepath = os.path.normpath(os.path.join(abs_wd, file_path))
        if os.path.commonpath([abs_wd, abs_filepath]) != abs_wd:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(abs_filepath):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(abs_filepath), exist_ok=True)
        with open(abs_filepath, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"
import os

def get_files_info(working_directory, directory="."):
    try:
        abs_wd = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_wd, directory))
        if os.path.commonpath([abs_wd, target_dir]) !=abs_wd:
            return f'Error: cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            is_dir = os.path.isdir(filepath)
            filesize = os.path.getsize(filepath)
            files_info.append(f"- {filename}: filesize={filesize} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
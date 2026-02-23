import os
from config import MAX_CHARS
from google import genai
from google.genai import types

def get_file_content(working_directory, directory):

    try:
        abs_wd = os.path.abspath(working_directory)
        abs_filepath = os.path.normpath(os.path.join(abs_wd, directory))
        if os.path.commonpath([abs_wd, abs_filepath])!= abs_wd:
            return f'Error: Cannot read "{directory}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_filepath):
            return f'Error: File not found or is not a regular file: "{directory}"'
        with open(abs_filepath, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{directory}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f'Error reading file "{directory}": {e}'




schema_get_file_content = types.FunctionDeclaration(
name="get_file_content",
description="Lists contents of a file in a specified directory relative to the working directory, maximum of 10000 characters",
parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
        "directory": types.Schema(
            type=types.Type.STRING,
            description="Directory path to get file content from, relative to the working directory (default is the working directory itself)",
        ),
    },
),)
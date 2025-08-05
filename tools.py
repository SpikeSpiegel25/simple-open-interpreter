import os
from langchain.tools import tool

# 工具 1：列出当前目录的文件
@tool
def list_files(directory: str= '.') -> str:
    """
    Lists all files and directors in a specified directory.
    Use this to find out what files are in the current working directory.
    The default directory is the current one ('.').
    :param directory:
    :return:
    """
    try:
        entries = os.listdir(directory)
        if not entries:
            return "The directroy is empty."
        return "\n".join(entries)
    except FileNotFoundError:
        return f"Error: The directory '{directory}' was not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# 工具2：读取制定文件的内容
@tool
def read_file(file_path: str) -> str:
    """
    Reads the content of a specified file.
    Only provide the file name, e.g., example.txt. Do not include quotes or any extra text.
    :param file_path:
    :return:
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

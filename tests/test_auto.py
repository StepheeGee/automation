# tests/test_auto.py
import os
from automation.auto import create_folder, handle_deleted_user, sort_documents, parse_log_file, more_info
from rich.console import Console

console = Console()

def test_create_folder(tmp_path):
    folder_name = "test_folder"
    create_folder(os.path.join(tmp_path, folder_name))
    assert os.path.exists(os.path.join(tmp_path, folder_name))

def test_handle_deleted_user(tmp_path):
    user_folder = os.path.join(tmp_path, "user")
    temp_folder = os.path.join(tmp_path, "temp_user")
    
    # Create a user folder with some content
    os.mkdir(user_folder)
    with open(os.path.join(user_folder, "document.txt"), "w") as file:
        file.write("Sample document content")

    handle_deleted_user(user_folder, temp_folder)
    assert not os.path.exists(user_folder)
    assert os.path.exists(temp_folder)
    assert os.path.exists(os.path.join(temp_folder, "document.txt"))

def test_sort_documents(tmp_path):
    source_folder = os.path.join(tmp_path, "source")
    os.mkdir(source_folder)

    # Create sample files with different extensions
    files = ["file1.txt", "file2.log", "file3.eml", "file4.doc"]
    for file in files:
        with open(os.path.join(source_folder, file), "w") as f:
            f.write("Sample content")

    sort_documents(source_folder)

    assert os.path.exists(os.path.join(source_folder, "logs"))
    assert os.path.exists(os.path.join(source_folder, "mail"))
    assert os.path.exists(os.path.join(source_folder, "logs", "file2.log"))
    assert os.path.exists(os.path.join(source_folder, "mail", "file3.eml"))

def test_parse_log_file(tmp_path):
    log_file = os.path.join(tmp_path, "sample.log")
    target_folder = tmp_path

    # Create a sample log file with errors and warnings
    with open(log_file, "w") as file:
        file.write("ERROR: Something went wrong\nWARNING: This is a warning\nINFO: Just information")

    parse_log_file(log_file, target_folder)

    assert os.path.exists(os.path.join(target_folder, "errors.log"))
    assert os.path.exists(os.path.join(target_folder, "warnings.log"))

def test_more_info(capsys):
    more_info('1')
    captured = capsys.readouterr()
    assert 'Create a new folder with a specified name.' in captured.out

    more_info('6')
    captured = capsys.readouterr()
    assert 'Please choose a valid option.' in captured.out

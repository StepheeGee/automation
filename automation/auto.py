import os
import shutil
import re
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.table import Table

console = Console()

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        console.print(f"[border bold yellow]Folder '[bold yellow]{folder_name}[/bold yellow]' created successfully.[/border bold yellow]")
    except FileExistsError:
        console.print(f"[border bold yellow][bold yellow]Folder '{folder_name}' already exists.[/bold yellow][/border bold yellow]")
    except Exception as e:
        console.print(f"[border bold yellow][bold red]Error creating folder: {e}[/bold red][/border bold yellow]")

def handle_deleted_user(user_folder, temp_folder):
    try:
        shutil.move(user_folder, temp_folder)
        console.print(f"[border bold yellow]User folder '[bold yellow]{user_folder}[/bold yellow]' moved to '[bold yellow]{temp_folder}[/bold yellow]'.[/border bold yellow]")
    except FileNotFoundError:
        console.print("[border bold yellow][bold red]User folder not found.[/bold red][/border bold yellow]")
    except Exception as e:
        console.print(f"[border bold yellow][bold red]Error handling deleted user: {e}[/bold red][/border bold yellow]")

def sort_documents(source_folder):
    try:
        file_types = {"logs": ["log"], "mail": ["txt", "eml"]}
        for filename in os.listdir(source_folder):
            file_extension = filename.split(".")[-1].lower()
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(source_folder, folder)
                    if not os.path.exists(destination_folder):
                        os.mkdir(destination_folder)
                    shutil.move(os.path.join(source_folder, filename), os.path.join(destination_folder, filename))
                    console.print(f"[border bold yellow]Moved '[bold blue]{filename}[/bold blue]' to '[bold yellow]{folder}[/bold yellow]' folder.[/border bold yellow]")
                    break
    except Exception as e:
        console.print(f"[border bold yellow][bold red]Error sorting documents: {e}[/bold red][/border bold yellow]")

def parse_log_file(log_file, target_folder):
    try:
        errors_log = os.path.join(target_folder, "errors.log")
        warnings_log = os.path.join(target_folder, "warnings.log")

        with open(log_file, "r") as file:
            log_content = file.read()

        errors = re.findall(r'\bERROR\b', log_content)
        warnings = re.findall(r'\bWARNING\b', log_content)

        with open(errors_log, "w") as file:
            file.write("\n".join(errors))
            console.print(f"[border bold yellow]Errors logged in '[bold blue]{errors_log}[/bold blue]'.[/border bold yellow]")

        with open(warnings_log, "w") as file:
            file.write("\n".join(warnings))
            console.print(f"[border bold yellow]Warnings logged in '[bold blue]{warnings_log}[/bold blue]'.[/border bold yellow]")
    except FileNotFoundError:
        console.print("[border bold yellow][bold red]Log file not found.[/bold red][/border bold yellow]")
    except Exception as e:
        console.print(f"[border bold yellow][bold red]Error parsing log file: {e}[/bold red][/border bold yellow]")

def more_info(option):
    info_table = Table(title="[bold pink]More Info[/bold pink]")
    if option == '1':
        info_table.add_row("[bold green]Create a folder[/bold green]", "Create a new folder with a specified name.")
    elif option == '2':
        info_table.add_row("[bold green]Handle a deleted user[/bold green]", "Move a user's documents to a temporary folder.")
    elif option == '3':
        info_table.add_row("[bold green]Sort documents into folders[/bold green]", "Sort documents into folders based on their file type.")
    elif option == '4':
        info_table.add_row("[bold green]Parse a log file for errors and warnings[/bold green]", "Parse a log file and create separate logs for errors and warnings.")
    elif option == '5':
        info_table.add_row("[bold green]Exit[/bold green]", "Exit the program.")
    elif option == '6':
        info_table.add_row("[bold green]Invalid option[/bold green]", "Please choose a valid option.")
    console.print(info_table)

def welcome_message():
    try:
        name = Prompt.ask("[bold cyan]Enter your name:[/bold cyan]")
        console.print(f"Hello {name}! Let's get busy...")
    except Exception as e:
        console.print(f"Error in welcome_message: {e}")

def menu_driven_application():
    welcome_message()
    while True:
        console.print("\n[border bold yellow]Automation Tasks Menu:[/border bold yellow]")
        console.print("[border bold pink]1.[/border bold pink] [bold green]Create a folder[/bold green]")
        console.print("[border bold pink]2.[/border bold pink] [bold green]Handle a deleted user[/bold green]")
        console.print("[border bold pink]3.[/border bold pink] [bold green]Sort documents into folders[/bold green]")
        console.print("[border bold pink]4.[/border bold pink] [bold green]Parse a log file for errors and warnings[/bold green]")
        console.print("[border bold pink]5.[/border bold pink] [bold green]Exit[/bold green]")
        console.print("[border bold pink]6.[/border bold pink] [bold green]More Info[/bold green]")

        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3', '4', '5', '6'], default='5')

        if choice == '1':
            folder_name = Prompt.ask("Enter the folder name to create")
            create_folder(folder_name)
        elif choice == '2':
            user_folder = Prompt.ask("Enter the user folder path")
            temp_folder = Prompt.ask("Enter the temporary folder path")
            handle_deleted_user(user_folder, temp_folder)
        elif choice == '3':
            source_folder = Prompt.ask("Enter the source folder path to sort documents")
            sort_documents(source_folder)
        elif choice == '4':
            log_file = Prompt.ask("Enter the path of the log file to parse")
            target_folder = Prompt.ask("Enter the target folder for error and warning logs")
            parse_log_file(log_file, target_folder)
        elif choice == '5':
            console.print("[border bold pink]Exiting the program.[/border bold pink]")
            break
        elif choice == '6':
            more_option = Prompt.ask("Enter the option number to get more info")
            more_info(more_option)
        else:
            console.print("[border bold pink]Invalid option. Please choose a valid option.[/border bold pink]")

if __name__ == "__main__":
    menu_driven_application()

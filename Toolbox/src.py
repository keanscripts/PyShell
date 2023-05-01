import os
import shutil
import datetime
os.system('cls' if os.name == 'nt' else 'clear')

PyShell = ""
while PyShell not in ["end", "stop", "quit"]:
    PyShell = input("PyShell: ")
    if PyShell.lower() == "help":
        print("dir access, dir del, dir create, file ")
    elif PyShell.startswith("dir" + " "):
        dir_var = PyShell[4:]
        if dir_var == "access":
            try:
                os.chdir("/")
                print("Directory access has been permitted.")
            except Exception as e:
                print(f"Failed to grant access to all directories: {str(e)}")
        elif dir_var == "list":
            cwd = os.getcwd()
            contents = os.listdir(cwd)
            print(contents)
        elif dir_var.startswith("create "):
            directory_name = dir_var[7:]
            home_dir = os.path.expanduser("~")
            new_dir_path = os.path.join(home_dir, directory_name)
            os.makedirs(new_dir_path, exist_ok=True)
            print(f"Directory '{directory_name}' created in '{home_dir}'")
        elif dir_var.startswith("del "):
            exclude_dirs = ["Applications", "Downloads"]
            directory_name = dir_var[4:]
            home_dir = os.path.expanduser("~")
            delete_dir_path = os.path.join(home_dir, directory_name)
            if os.path.isdir(delete_dir_path) and directory_name not in exclude_dirs:
                os.system('cls' if os.name == 'nt' else 'clear')
                confirm = input(f"Are you sure you want to delete '{directory_name}'? (y/n)?: ")
                if confirm.lower() == "y":
                    try:
                        os.rmdir(delete_dir_path)
                        print(f"Directory '{directory_name}' deleted from '{home_dir}'.")
                    except Exception as e:
                        print(f"Failed to delete directory: {str(e)}")
                else:
                    print("Deletion cancelled.")
            else:
                print("Directory not found or cannot be deleted.")            
        else:
            print("Invalid syntax.")
    elif PyShell.startswith("file "):
        command_args = PyShell.split()[1:]
        if len(command_args) == 2 and command_args[0] == 'del':
            file_name = command_args[1]
            found_file = False
            print("Searching user-made files in 'Documents' and 'Downloads' directories...")
            home_dir = os.path.expanduser("~")
            ignore_dirs = ['Library', 'Frameworks', 'System', 'bin', 'dev', 'usr']
            ignore_exts = ['.dll', '.exe', '.sys']
            for root, dirs, files in os.walk(home_dir, topdown=True):
                dirs[:] = [d for d in dirs if d not in ignore_dirs]
                if root.endswith(('Documents', 'Downloads', 'Desktop')):
                    print(f"Searching {root}...")
                    for file in files:
                        if file == file_name:
                            found_file = True
                            file_path = os.path.join(root, file_name)
                            if any(file_path.endswith(ext) for ext in ignore_exts):
                                print(f"File '{file_name}' is a system file and cannot be deleted.")
                                break
                            os.system('cls' if os.name == 'nt' else 'clear')
                            confirm = input(f"Are you sure? '{file_path}' will be permanently deleted (y/n)?: ")
                            if confirm.lower() == "y":
                                os.remove(file_path)
                                print(f"'{file_path}' has been deleted.")
                                break
                            else:
                                print("Deletion cancelled.")
                    if found_file:
                        break
            if not found_file:
                print(f"File '{file_name}' does not exist in user-made files.")
        elif len(command_args) == 2 and command_args[0] == 'dupe':
            file_name = command_args[1]
            found_file = False
            print("Searching user-made files in 'Documents' and 'Downloads' directories...")
            home_dir = os.path.expanduser("~")
            ignore_dirs = ['Library', 'Frameworks', 'System', 'bin', 'dev', 'usr']
            for root, dirs, files in os.walk(home_dir, topdown=True):
                dirs[:] = [d for d in dirs if d not in ignore_dirs]
                if root.endswith(('Documents', 'Downloads', 'Desktop')):
                    print(f"Searching {root}...")
                    for file in files:
                        if file == file_name:
                            found_file = True
                            file_path = os.path.join(root, file_name)
                            copy_file_path = os.path.join(root, "copy_" + file_name)
                            if os.path.exists(copy_file_path):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"'{copy_file_path}' already exists.")
                                break
                            shutil.copy2(file_path, copy_file_path)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"'{file_path}' has been duplicated as '{copy_file_path}'.")
                            break
                    if found_file:
                        break
            if not found_file:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"File '{file_name}' does not exist in user-made files.")
        elif PyShell.startswith("file properties"):
            file_name = command_args[1]
            found_file = False
            print("Searching user-made files in 'Documents' and 'Downloads' directories...")
            home_dir = os.path.expanduser("~")
            ignore_dirs = ['Library', 'Frameworks', 'System', 'bin', 'dev', 'usr']
            for root, dirs, files in os.walk(home_dir, topdown=True):
                dirs[:] = [d for d in dirs if d not in ignore_dirs]
                if root.endswith(('Documents', 'Downloads', 'Desktop')):
                    print(f"Searching {root}...")
                    for file in files:
                        if file == file_name:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            found_file = True
                            file_path = os.path.join(root, file_name)
                            file_stat = os.stat(file_path)
                            print(f"File Name: {file_name}")
                            print(f"Type: {os.path.splitext(file_name)[1]}")
                            print(f"Size: {file_stat.st_size} bytes")
                            print(f"Created: {datetime.datetime.fromtimestamp(file_stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')}")
                            print(f"Last Accessed: {datetime.datetime.fromtimestamp(file_stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')}")
                            print(f"Last Modified: {datetime.datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
                            break
                    if found_file:
                        break
            if not found_file:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"File '{file_name}' does not exist in user-made files.")
    else:
        if PyShell not in ["end", "stop", "quit"]:
            print("Invalid input, type 'help' for a list of commands")

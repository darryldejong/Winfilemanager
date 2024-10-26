import os
import shutil
import platform
from colorama import init, Fore, Style

init(autoreset=True)

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Mac/Linux

clear_terminal()

user_home = os.path.expanduser('~')

desktop_path = os.path.join(user_home, 'Desktop')

desktop_exists = os.path.exists(desktop_path)

if not desktop_exists:
    print(f"{Fore.RED}Error: 'Desktop' folder could not be found.")
    input(f"{Fore.CYAN}Press Enter to close the terminal.")
    exit()

downloads_path = os.path.join(user_home, 'Downloads')
documents_path = os.path.join(user_home, 'Documents')
pictures_path = os.path.join(user_home, 'Pictures')
music_path = os.path.join(user_home, 'Music')
videos_path = os.path.join(user_home, 'Videos')

file_mappings = {
    'Pictures': ['.png', '.jpg', '.jpeg', '.gif'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx', '.csv']
}

folder_colors = {
    'Pictures': Fore.MAGENTA,
    'Music': Fore.CYAN,
    'Videos': Fore.BLUE,
    'Documents': Fore.RED
}

files_moved = False

def organize_files(source_path):
    global files_moved
    if source_path is None or not os.path.exists(source_path):
        return
    
    for file_name in os.listdir(source_path):
        file_extension = os.path.splitext(file_name)[1].lower()
        
        for folder, extensions in file_mappings.items():
            if file_extension in extensions:
                target_folder = eval(f"{folder.lower()}_path")
                target_path = os.path.join(target_folder, file_name)
                source_file_path = os.path.join(source_path, file_name)

                if source_file_path == target_path:
                    continue

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(source_file_path, target_path)
                files_moved = True
                color = folder_colors.get(folder, Fore.WHITE)
                print(f"{color}Moved: {file_name}\nFrom: {source_file_path}\nTo: {target_path}\n")

for path in [desktop_path, downloads_path, documents_path, pictures_path, music_path, videos_path]:
    organize_files(path)

if not files_moved:
    print(f"{Fore.GREEN}All files are in the correct place, no files moved.")

print(f"{Fore.YELLOW}File organization completed.")

input(f"{Fore.CYAN}Press Enter to close the terminal.")

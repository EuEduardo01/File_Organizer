import os
import shutil

download_folder_path = r"C:\Users\Eduardo\Downloads" #Substitua pelo endereço da sua pasta downloads.
new_route = r"D:\Eduardo\Documents" #Substitua pelo endereço que deve ser colocada as pastas organizadas.
for file in os.listdir(download_folder_path):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]
    folder_to_organize_file = f"{new_route}/{file_extension}"

    if not os.path.isdir(folder_to_organize_file):
        os.mkdir(folder_to_organize_file)
    shutil.move(f"{download_folder_path}/{file}", f"{folder_to_organize_file}/{file}")
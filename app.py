import os
import shutil

directory = "C:/Users/eduardo.cruz/Downloads/" #Substitua pelo endereço da sua pasta downloads.
files = os.listdir(directory)

filetypes = [
    [[".jpg", ".jpeg", ".png", ".gif"], "Imagens"],
    [[".doc", ".docx", ".txt", "pptx"], "Documentos"],
    [[".xlsx", ".csv"], "Planilhas"],
    [[".pdf"], "PDFs"],
    [[".zip"], "Zip"],
    [[".sql", ".php", ".py", ".html", ".js", ".json"], "Codigos"],
    [[".exe"], "Exe"],
    [[".mp4", ".mp3", ".mpeg", ".mkv", ".mp2", ".m4r", ".avi", ".mpg", ".vob", ".mov", ".wav"], "Audio&Video"]
]

def get_folder_for_file(file, filetypes):
    for extensions, folder in filetypes:
        dir_path = directory+folder
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print(dir_path)
        if file.lower().endswith(tuple(extensions)):
            return folder
        continue

for file in files:
    folder = get_folder_for_file(file, filetypes)
    if isinstance(folder, str):
        shutil.move(os.path.join(directory, file), os.path.join(directory, folder, file))
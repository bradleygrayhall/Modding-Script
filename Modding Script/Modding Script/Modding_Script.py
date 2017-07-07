import os,shutil
from pyunpack import Archive
Archive_list = []
file_list = []
Folder_Name = []
working_folder = os.getcwd()
Check_to_see_if_file_has_archive_extension = [".7z",".ace",".alz",".a",".arc",".arj",".bz2",".cab",".Z",".cpio",".deb",".dms",".gz",".lrz",".lha",".lzh",".lz",".lzma",".lzo",".rpm",".rar",".rz",".tar",".xz",".zip",".jar",".zoo"]
def extract_everything_in_the_folder():
    for file in os.listdir():
        file_list.append(file)
    for file in file_list:
        temp_Lookup_num = file.rfind(".")
        if temp_Lookup_num != -1:
            temp_extension = file[temp_Lookup_num:]
            for type in Check_to_see_if_file_has_archive_extension:
                if type == temp_extension:
                    folder = file[:temp_Lookup_num]
                    os.makedirs(folder,exist_ok=True)
                    Archive(file).extractall(os.getcwd()+"\\"+folder)
                else:
                    continue
        else:
            continue
def Search_Folder_For_BSA_file(File_and_Folder_Name):
    os.chdir(File_and_Folder_Name)
    file_list = os.listdir()
    for contents in file_list:
        if contents == "fomod":
            return True
        if os.path.isdir(str(File_and_Folder_Name+"\\"+contents)) == True:
            os.chdir(File_and_Folder_Name+"\\"+contents)
            temp = os.listdir()
            for new_contents in temp:
                temp_indice = new_contents.rfind(".")
                extension = new_contents[temp_indice:]
                if new_contents == "fomod" or extension == ".bsa":
                    return True
        else:
            temp_indice = contents.find(".")
            extension = contents[temp_indice:]
            if contents == "fomod" or extension == ".bsa":
                return True
    return False
def Delete_Folder(Folder_to_be_Deleted):
    shutil.rmtree(Folder_to_be_Deleted)
def Delete_archive(File_to_be_Deleted):
    os.remove(File_to_be_Deleted)
def main():
    for file in os.listdir():
        temp_indice = file.rfind(".")
        if temp_indice != -1:
            global Archive_list
            Archive_list.append(file)
    extract_everything_in_the_folder()
    for file in Archive_list:
        temp_indice = file.rfind(".")
        for extension in Check_to_see_if_file_has_archive_extension:
            temp_name = file[temp_indice:]
            if temp_name == extension:
                temp = file[:temp_indice]
                BSA_Found = Search_Folder_For_BSA_file(os.getcwd()+"\\"+temp)
                os.chdir(working_folder)
                if BSA_Found == True:
                    Delete_Folder(os.getcwd()+"\\"+temp)
                else:
                    Delete_archive(os.getcwd()+"\\"+file)
main()
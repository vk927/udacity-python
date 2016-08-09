import os
from string import digits
def rename_files():
    file_list=os.listdir(r"C:\....\prank")
    pgm_path=os.getcwd()
    print(pgm_path)
    os.chdir(r"C:\....\prank")
    for file_name in file_list:
        remove_digits=str.maketrans("", "", digits)
        os.rename(file_name,file_name.translate(remove_digits))
    os.chdir(pgm_path)

rename_files()
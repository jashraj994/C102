import os 
import shutil

from_dir = "C:\Users\admin\downloads"
to_dir ="C:\Users\drpsm\OneDrive\Desktop\101"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:

    name,extension=os.path.splitext(file_name)

    print(name)
    print(extension)
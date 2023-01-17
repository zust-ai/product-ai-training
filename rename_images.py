import os
from pathlib import Path

# Get the folder path 
name = 'ramleela'
create_text_file = True
folder_path = f'classes/{name}'

# Get the list of files in the folder
files = os.listdir(folder_path)

supported_ext = ['.png', '.jpg', '.webp']

count = 1

# Iterate over all the files
print(len(files))
for index, file in enumerate(files):
    # Get the file name and its extension
    file_name, file_ext = os.path.splitext(file)
    if file_ext not in supported_ext:
        continue
    new_file_name = f'{name}_{str(count)}'

    print(new_file_name + file_ext)
    # Rename the file
    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_file_name + file_ext))

    # Create a text file
    if create_text_file:
        with open(os.path.join(folder_path, new_file_name + '.txt'), 'w') as f:
            f.write(f'A photo of {name}')

    count = count + 1
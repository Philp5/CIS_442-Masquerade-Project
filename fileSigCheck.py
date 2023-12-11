import os
import magic

def getMasqueradeFiles(folder):
    mime = magic.Magic()

    for root, _, files in os.walk(folder):
        for file_name in files:

            file_path = os.path.join(root, file_name)

            signature = mime.from_file(file_path)
            _, extension = os.path.splitext(file_name)

            extension = extension[1:]
            if(signature.startswith(extension.upper())):
                x=1
            else:
                print(file_name)
                


folder = input("Enter the path for the folder you would like to check: ")
getMasqueradeFiles(folder)


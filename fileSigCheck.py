import os
import magic

def getMasqueradeFiles(folder):
    mime = magic.Magic()

    #Loop through every folder and file in the given root directory
    for root, _, files in os.walk(folder):
        #loop again to check each file
        for file_name in files:

            #get the file path for the file in the root directory
            file_path = os.path.join(root, file_name)

            #using mime get the signature from the file path
            signature = mime.from_file(file_path)
            #using os split the file extension from the end of the file name
            _, extension = os.path.splitext(file_name)
            #remove the leading period form the file extension for comparison
            extension = extension[1:]
            
            #check if the signature and file extension match
            if(signature.startswith(extension.upper())):
                x=1 #do nothing if true
            else:
                print(file_name) #print file name if false
                


folder = input("Enter the path for the folder you would like to check: ")
getMasqueradeFiles(folder)


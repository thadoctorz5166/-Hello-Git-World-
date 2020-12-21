import os 
def main():
    directory = input("Enter the directory that you want to save the file : ") 
    filename = input("Enter the filename : ")
    name = input("Enter your name : ") 
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number : ") 
    #check if the directory exists
    if os.path.isdir(directory):
    #create/open write file
        writeFile = open(os.path.join(directory,filename),'w') 
        #writing the data 
        writeFile.close() 
        print("File contents:")
        #read file
        readFile = open(os.path.join(directory,filename),'r') 
        for line in readFile:
            print(line)

        readFile.close()

    else:
        print("Directory Does Not Exist..")

main()
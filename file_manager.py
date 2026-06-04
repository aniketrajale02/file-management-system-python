from pathlib import Path
import os


def create_folder():
    try:
        name=input("Please tell a folder name:-") 
        p= Path(name)
        p.mkdir()
        print("Folder creted Successfull!!")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

def read_file_folder():
    p=Path("")
    items=list(p.rglob('*'))
    for i ,v in enumerate(items):
        print(f"{i+1}:{v}")

def update_folder():
    try:
        read_file_folder()
        old_name= input("Please tell folder name to update:-")
        p=Path(old_name)
        if p.exists() and p.is_dir():
            new_name=input("please tell your new folder name:-")
            new_p = Path(new_name)
            p.rename(new_p)
            print("Your Folder is updated")
        else:
            print("Sorry no such folder exist")
    except Exception as err:
        print(f"An error occured as {err}")

def delete_folder():
    try:
        read_file_folder()
        name= input("Please tell which folder you want to delete:-")
        p=Path(name)
        if p.exists and p.is_dir():
            p.rmdir()
            print("Folder Deleted Successfully")
        else:
            print("No such folder ids present")

    except Exception as err:
        print(f"An error occured as {err}")

def create_file():
    try:
        read_file_folder()
        name= input("Please tell your file name")
        p=Path(name)
        if not p.exists():
            with open (name,"w") as fs:
                data= input("Write you want these folder:-")
                fs.write(data)
                print("file Create Successfully !!")
        else:
            print("Sorry this file aldready exist")
    except Exception as err:
        print(f" An error occured as {err}")

def read_file():
    try:

        read_file_folder()
        name= input("Please tell your file name")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(name,"r") as fs:
                content = fs.read()
                print("Your file is :-")
                print(content)
        else:
            print(" No such file is exist")
    except Exception as err:
        print(f"An error Occured as {err}")

def update_file():
    read_file_folder()
    name= input("Please tell your file name")
    p=Path(name)
    if p.exists () and p.is_file():
        try:
            print("Optiona:--")
            print("1.For renaming file")
            print("2.For appending Something in file")
            print("3.For overwritting the file content")
            choice=int(input("tell your choice :-"))

            if choice==1:
                new_name= input("Tell you new file name with extension:-")
                new_p=Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("Your file name is changed successfully")
                else:
                    print(" Sorry these name is exist")

            if choice==2:
                with open(name, 'a') as fs:
                    data= input("What you want to apend:-")
                    fs.write(""+data)
                    print("Data appended successfully")
            
            if choice==3:
                with open(name, 'w') as fs:
                    data= input("What you want to overwrite:-")
                    fs.write(data)
                    print("Data changed successfully")
        except Exception as err:
              print(f"An error Occured as {err}")

def delete_file():
    try:
        read_file_folder()
        name= input("Please tell which file with extenstion you want to delete:-")
        p=Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("Deleted successfully")
        else:
            print("No file exist")
    except Exception as err:
              print(f"An error Occured as {err}")

while True:
    print("Choose a option:-")
    print("1.Create a folder")
    print("2.Read files and folder")
    print("3.Update a folder")
    print("4.Delete the folder")
    print("5.Create a File")
    print("6.Read a file")
    print("7.Update a file")
    print("8.Delete a file")
    print("9.EXIT")

    choice= int(input("Please tell your choose:-"))

    if choice==1:
        create_folder()

    elif choice==2:
        read_file_folder()

    elif choice==3:
        update_folder()

    elif choice==4:
        delete_folder()

    elif choice==5:
        create_file()

    elif choice ==6:
        read_file()

    elif choice ==7:
        update_file()

    elif choice ==8:
        delete_file()

    elif choice ==9:
        print("Thank you for using our application")
        break
    else:
        print("Sorry invalid choice")
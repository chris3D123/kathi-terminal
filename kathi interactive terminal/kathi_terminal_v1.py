def display_help():
    print("NF admin  = new file")
    print("TC admin  = terminal check")
    print("h admin   = help")
    print("RF admin  = run a file")
    print("exit      = exit the program")

files = {}

while True:
    command = input("kathi_admin: ")

    if command == "exit":
        print("Exiting KATHI Admin. Goodbye!")
        break
    elif command == "h admin":
        display_help()
    elif command == "NF admin":
        file_name = input("What do you want the name of the file to be: ")
        file_contents = input("What do you want your file to say:\n")
        files[file_name] = file_contents
    elif command == "RF admin":
        file_name = input("What file do you want to run: ")
        if file_name in files:
            print(f"{file_name}:\n {files[file_name]}")
        else:
            print("File not found.")
    elif command == "TC admin":
        print("Checking terminal for bugs...")
        print("Checking KATHI for bugs...")
        print("Checking files for threats...")
        print("Discarding terminal check.")
    else:
        print("Invalid command. Type 'h admin' for help.")

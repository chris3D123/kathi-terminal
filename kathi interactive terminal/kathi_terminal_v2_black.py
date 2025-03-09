import tkinter as tk
from tkinter import scrolledtext

def display_help():
    terminal_output.insert(tk.END, "NF admin  = new file\n")
    terminal_output.insert(tk.END, "TC admin  = terminal check\n")
    terminal_output.insert(tk.END, "h admin   = help\n")
    terminal_output.insert(tk.END, "RF admin  = run a file\n")
    terminal_output.insert(tk.END, "exit      = exit the program\n")
    terminal_output.yview(tk.END)

def execute_command():
    command = command_input.get()
    command_input.delete(0, tk.END)

    if command == "exit":
        root.destroy()
    elif command == "h admin":
        display_help()
    elif command == "NF admin":
        file_name = input_box("What do you want the name of the file to be:")
        file_contents = input_box("What do you want your file to say:")
        files[file_name] = file_contents
        terminal_output.insert(tk.END, f"File '{file_name}' created.\n")
        terminal_output.yview(tk.END)
    elif command == "RF admin":
        file_name = input_box("What file do you want to run:")
        if file_name in files:
            terminal_output.insert(tk.END, f"{file_name}:\n{files[file_name]}\n")
        else:
            terminal_output.insert(tk.END, "File not found.\n")
        terminal_output.yview(tk.END)
    elif command == "TC admin":
        terminal_output.insert(tk.END, "Checking terminal for bugs...\n")
        terminal_output.insert(tk.END, "Checking KATHI for bugs...\n")
        terminal_output.insert(tk.END, "Checking files for threats...\n")
        terminal_output.insert(tk.END, "Discarding terminal check.\n")
        terminal_output.yview(tk.END)
    else:
        terminal_output.insert(tk.END, "Invalid command. Type 'h admin' for help.\n")
        terminal_output.yview(tk.END)

def input_box(prompt):
    temp_window = tk.Toplevel(root)
    temp_window.title("Input")
    tk.Label(temp_window, text=prompt, bg="black", fg="white").pack()
    temp_var = tk.StringVar()
    temp_entry = tk.Entry(temp_window, textvariable=temp_var, bg="black", fg="white", insertbackground="white")
    temp_entry.pack()
    temp_entry.focus()
    tk.Button(temp_window, text="Submit", command=temp_window.destroy, bg="black", fg="white").pack()
    temp_window.configure(bg="black")
    temp_window.grab_set()
    root.wait_window(temp_window)
    return temp_var.get()

# Setting up the tkinter window
root = tk.Tk()
root.title("KATHI Admin Terminal")
root.configure(bg="black")  # Set main window background to black

# Terminal-like output area
terminal_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=60, bg="black", fg="white")
terminal_output.pack(padx=10, pady=10)

# Entry box for commands
command_input = tk.Entry(root, width=60, bg="black", fg="white", insertbackground="white")  # Cursor color is white
command_input.pack(padx=10, pady=5)
command_input.bind("<Return>", lambda event: execute_command())

# Execute button
execute_button = tk.Button(root, text="Execute Command", command=execute_command, bg="black", fg="white")
execute_button.pack(pady=5)

files = {}

terminal_output.insert(tk.END, "Welcome to KATHI Terminal! Type 'h admin' for help.\n")
terminal_output.yview(tk.END)
root.mainloop()

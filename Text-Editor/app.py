import os
import tkinter as tk
from tkinter import ttk, filedialog



def save_file():
    file_path = filedialog.asksaveasfilename()
    try:
        filename = os.path.basename(file_path)
        text_widget = root.nametowidget(notebook.select())
        content = text_widget.get("1.0", "end-1c")

        with open(file_path, "w") as file:
            file.write(content)
    except(AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return

    notebook.tab('current', text=filename)

def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill="both", expand=True)
    notebook.add(text_area, text="Untitled")
    notebook.select(text_area)

def quit():
    root.destroy()

root = tk.Tk()
root.title("Knight Text Editor")
root.option_add('*tearOff', False)
# root.option_add('*tearOff', True)

main = ttk.Frame(root)
main.pack(fill='both', expand=True, padx=1, pady=(4,0))

menubar = tk.Menu()
root.config(menu=menubar, bg='blue')

#Menu option to Create new Notepad
file_menu = tk.Menu(menubar, activebackground='purple')
menubar.add_cascade(menu=file_menu, label='File')
file_menu.add_command(label="New", command=create_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit)






notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)
create_file()
create_file()



root.mainloop()

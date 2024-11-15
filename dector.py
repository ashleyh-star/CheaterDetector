import tkinter
from tkinter import filedialog
import main



mainWindow = tkinter.Tk()

mainWindow.title("Cheating detector")
mainWindow.geometry("550x500")
mainWindow.config(bg="#ffffff")

titleText = tkinter.Label(text="Cheating Detecor", font=("Helvetica", 30),fg="#000000",bg="#ffffff")
titleText.pack(pady=30)

# Reusable function to handle file selection and update the corresponding label
# Function to handle file selection and update the global variable
def select_file1():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as f:
            main.student1work = f.read()  # Update global variable with file content

def select_file2():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as f:
            main.student2work = f.read()  # Update global variable with file content
    main.student2work = file_path

Upload1 = tkinter.Button(text="Upload student 1 work", font=("Helvetica",20), command= select_file1)
Upload1.pack()
Upload1.pack(pady=(30,0))

Upload2 = tkinter.Button(text="Upload student 2 work", font=("Helvetica",20), command= select_file2)
Upload2.pack()
Upload2.pack(pady=(0,30))

text1 = tkinter.Label(text="Threshold:", font=("Times New Roman",20),fg="#000000",bg="#ffffff")
text1.pack()

inputBox1= tkinter.Entry()
inputBox1.pack(pady=(0,20))

def cheatingResult():
    s = f"{main.getSimilarity()}%"
    text2.config(text=s)
    outcome = main.threshold(int(inputBox1.get()))
    text3.config(text=outcome)

result = tkinter.Button(text="Get Result", command = cheatingResult)
result.pack()

text2 = tkinter.Label(text="", font=("Times New Roman",20),fg="#000000",bg="#ffffff")
text2.pack()

text3 = tkinter.Label(text="", font=("Times New Roman",20),fg="#000000",bg="#ffffff")
text3.pack()


mainWindow.mainloop()



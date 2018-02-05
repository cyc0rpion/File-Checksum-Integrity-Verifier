from tkinter import filedialog

def browse_file():
    fname = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    print(fname)
    return(fname)


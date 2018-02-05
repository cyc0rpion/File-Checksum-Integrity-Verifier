import hashlib
from tkinter import *
from tkinter import messagebox
import os
from browse import browse_file
from md import md5s

global x,y,opened,file1Name,file2Name,hash1Text,hash2Text

def reset():
    """Function to reset the state of the program"""
    try:
        fo.close()
        os.remove('savestate.txt')
    except IOError:
        pass
    except NameError:
        pass
    
    python=sys.executable
    os.execl(python,python, * sys.argv)       #RESTART THE SCRIPT
    
def browser1():
    """Function to browse first file and access it"""
    global file1Name
    x = browse_file()
    file1Name=StringVar(window,value=x)
    file1Entry = Entry(window,bd=3,width=50,textvariable=file1Name).grid(row=3,column=5)
    
def browser2():
    """Function to browse and access second file"""
    global file2Name
    y = browse_file()
    file2Name=StringVar(window,value=y)
    file2Entry = Entry(window,bd=3,width=50,textvariable=file2Name).grid(row=5,column=5)
    
def md5_calculator(string):
    """Function to calculate md5sum"""
    ans = (md5s(string))
    return(ans)
    print(ans)
    
##    md5 = hashlib.md5()
##    md5.update(string)
##    md5sum = md5.hexdigest()
##    return(md5sum)

def sha1_calculator(string):
    """Function to calculate sha1sum"""
    sha1 = hashlib.sha1()
    sha1.update(string)
    sha1sum = sha1.hexdigest()
    return(sha1sum)

def checkIntegrity():
    """Function to compare hash sum of both files"""
    global x,y,file1Name,file2Name,hash1Text,hash2Text
    
    def hash1():
        hash1str=("MD5: "+md5hash1+"\n\nSHA1: "+sha1hash1)
        hash1Text = Text(window,height=4,width=50)
        hash1Text.grid(row=4,column=5,columnspan=2)
        hash1Text.insert(INSERT,hash1str)
        

    def hash2():
        hash2str=("MD5: "+md5hash2+"\n\nSHA1: "+sha1hash2)
        hash2Text = Text(window,height=4,width=50)
        hash2Text.grid(row=6,column=5,columnspan=2)
        hash2Text.insert(INSERT,hash2str)

    if(opened==1):
        y=str(file2Name.get())
        
        try:
            file2Content=open(y,'rb').read()
            
            md5hash1 = fo.readline()
            sha1hash1 = fo.readline()
        
            md5hash2 = (md5_calculator(file2Content)+"\n")
            sha1hash2 = (sha1_calculator(file2Content)+"\n")

            if(md5hash1 == md5hash2 and sha1hash1 == sha1hash2):
                messagebox.showinfo('Integrity Check Completed','Data is not Altered')
            else:
                messagebox.showerror('Integrity Check Completed','Data has been Altered')

        except:
            messagebox.showinfo('File not found','Please enter correct file path')

    else:
        x = str(file1Name.get())
        y = str(file2Name.get())

        try:
            file1Content = open(x,'rb').read()
            file2Content = open(y,'rb').read()
        
            
            md5hash1 = md5_calculator(file1Content)
            sha1hash1 = sha1_calculator(file1Content)

            md5hash2 = md5_calculator(file2Content)
            sha1hash2 = sha1_calculator(file2Content)

        
            if(md5hash1 == md5hash2 and sha1hash1 == sha1hash2):
                messagebox.showinfo('Integrity Check Completed','Data is not Altered')
            else:
                messagebox.showerror('Integrity Check Completed','Data has been Altered')

        except:
            messagebox.showinfo('File not found','Please enter correct file path')
            reset()
    try:
        fo.close()
        os.remove('savestate.txt')
    except IOError:
        pass
    except NameError:
        pass

    hashButton = Button(window,text="#",font="Helvetica 10 bold",command=hash1).grid(row=3,column=8)
    hashButton = Button(window,text="#",font="Helvetica 10 bold",command=hash2).grid(row=5,column=8)


def saveState():
     """Function to save state of executing program, if second file is on another system"""
     x=str(file1Name.get())
     file1Content=open(x,'rb').read()
     md5hash1 = md5_calculator(file1Content)
     sha1hash1 = sha1_calculator(file1Content)
     
     so = open('savestate.txt','w')
     so.write(x+"\n")
     so.write(md5hash1+"\n")
     so.write(sha1hash1+"\n")
     so.close()
     messagebox.showinfo("State Saved","Now Execute the program for second file.\nIf you are performing the check on the file on another system execute the program with savestate.txt file")
     window.destroy()



#GUI Part
try:
    try:
        fo = open('savestate.txt','r')
        opened=1
        name = fo.readline()
    except IOError:
        opened=0
    
    window = Tk()
    window.title("Integrity Checker")
    
    rows=11
    columns=11
    
    for i in range(rows):
        for j in range(columns):
            empty=Label(window,text='',height=1,width=2).grid(row=i,column=j)
            
    fciv = Label(window,bg='yellow',fg='blue',text='Integrity Checker',height=1,width=30,font="Helvetica 16 bold italic").grid(row=1,column=0,columnspan=12)
    
    if(opened==1):
        file1Name = StringVar(window,value=name)
    else:
        file1Name = StringVar()
    
    file2Name = StringVar()
    
    file1Label = Label(window,text="File 1",width=5,height=1).grid(row=3,column=3)
    
    if(opened==1):
        file1Entry = Entry(window,bd=3,width=50,textvariable=file1Name,state=DISABLED).grid(row=3,column=5)
        browse1 = Button(window,text="Browse..",relief=RAISED,state=DISABLED).grid(row=3,column=6)
    
    else:
        file1Entry = Entry(window,bd=3,width=50,textvariable=file1Name).grid(row=3,column=5)
        browse1 = Button(window,text="Browse..",relief=RAISED,activebackground='white',command=browser1).grid(row=3,column=6)

    file2Label = Label(window,text="File 2",width=5,height=1).grid(row=5,column=3)
    file2Entry = Entry(window,bd=3,width=50,textvariable=file2Name).grid(row=5,column=5)
    browse2 = Button(window,text="Browse..",relief=RAISED,activebackground='white',command=browser2).grid(row=5,column=6)
    
    if(opened==1):
        saveButton = Button(window,text='Reset State',bg='skyblue',activebackground='lightgreen',relief=RAISED,font="Helvetica 10 bold",command=reset).grid(row=9,column=5)
        message=Label(window,text='a state was saved earlier',bg='yellow',fg='red').grid(row=9,column=6)
    else:
        saveButton = Button(window,text='Save State',bg='skyblue',activebackground='lightgreen',relief=RAISED,command=saveState,font="Helvetica 10 bold").grid(row=9,column=5)
    
    checkButton = Button(window,text='Check Integrity',bg='lightpink',activebackground='lightgreen',relief=RAISED,command=checkIntegrity,font="Helvetica 10 bold").grid(row=7,column=5) 
except:
    messagebox.showinfo("Application Error","Oops! application has ran into a problem")
    window.destroy()

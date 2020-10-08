from tkinter import Tk,StringVar,Label,LEFT,ttk,END
from tkinter import messagebox
import os
from tkinter import filedialog
from PIL import ImageTk, Image
from pdf2image import convert_from_path
import pytesseract

image_counter=1

#Create Directory if Not created
if not os.path.isdir('./detect'):
    os.mkdir('./detect')
if not os.path.isdir('./pdfpic'):
    os.mkdir('./pdfpic')

#open File
def seasame(file):
    os.system("xdg-open "+file)

def design():
    style=ttk.Style()
    style.theme_use('clam')

#Browse File From Directory
def Browse():
    root.filename =  filedialog.askopenfilename(initialdir = "./ImagesPdf",title = "Select file",filetypes = (("All Image files","*.pdf *.png *.jpg *.jpeg"),("jpeg files","*.jpg *.jpeg"),("pdf files","*.pdf"),("png files","*.png")))
    if root.filename:
        if root.filename.endswith('.pdf'):
            print("It is a pdf file")
            pages = convert_from_path(root.filename, 500) 
            # Counter to store images of each page of PDF to image 
            global image_counter
            image_counter=1 
            for page in pages: 
                filename = "page_"+str(image_counter)+".jpg"
                page.save('./pdfpic/'+filename, 'JPEG') 
                image_counter=image_counter+1
            entry.delete(0,END)
            entry.insert(0,root.filename)
            img = Image.open('./ImagesPdf/pdf.png')
            img = img.resize((250, 250), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel.configure(image=img)
            panel.image = img
            panel.grid(row=3,column=1,padx=10,pady=10)
            root.geometry('550x420')
        else:    
            print("It is a image file")
            root.geometry('550x420')
            entry.delete(0,END)
            entry.insert(0,root.filename)
            img = Image.open(root.filename)
            img = img.resize((250, 250), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel.configure(image=img)
            panel.image = img
            panel.grid(row=3,column=1,padx=10,pady=10)

#detect the text
def Detect():
    if not entry.get():
        messagebox.showinfo(title='Error',message='File Not Selected')
    else:
        if(root.filename.endswith('.pdf')):
            #Filename
            outfile = os.path.splitext(os.path.basename(root.filename))[0]+".txt"   
            if os.path.isfile("./detect/"+outfile):
                os.remove("./detect/"+outfile)
            f = open("./detect/"+outfile, "a")
            print("Pages:"+str(image_counter-1))
            for i in range(1,image_counter): 
                filename = "./pdfpic/page_"+str(i)+".jpg"
                # Recognize the text as string in image using pytesserct 
                text = ((pytesseract.image_to_string(Image.open(filename)))) 
                text = text.replace('-\n', '')     
                f.write(text)
                text="\n\n*******************************-Page "+str(i)+"-******************************************\n\n"
                text = text.replace('-\n', '')
                f.write(text)
                os.remove(filename)
                print(str(i)+"/"+str(image_counter-1))
            messagebox.showinfo(title="Done",message="Detection Complete")
            f.close()
            seasame("./detect/"+outfile)
        else:
            outfile = os.path.splitext(os.path.basename(root.filename))[0]+".txt"   
            im=Image.open(entry.get())
            if rtext.get():
                text=pytesseract.image_to_string(im,lang=""+rtext.get() )
                text = text.replace('-\n', '')     
                if text:
                    f = open("./detect/"+outfile, "w")
                    f.write(text)
                    f.close()
                    messagebox.showinfo(title="Done",message="Detection Complete")
                    seasame("./detect/"+outfile)
                else:
                    messagebox.showinfo(title="Error",message="No Text")
            else:
                messagebox.showinfo(title="Warning",message="Select A Language")

#GUI
root=Tk()
root.geometry('550x150')
root.title('Text Recognition')
rtext=StringVar()

design()
Label(root, text="File Location:",padx = 5).grid(row=0,column=0,pady=10)

entry=ttk.Entry(root,width=40)
entry.grid(row=0,column=1,pady=10,padx=5)

button1=ttk.Button(root,text="Browse",command=Browse).grid(row=0,column=2,pady=10,padx=5)

Label(root, text="Choose the language to detect:").grid(row=1,column=1)

rb1=ttk.Radiobutton(root,text="Kannada",variable=rtext,value="kan").grid(row=2,column=0)
rb1=ttk.Radiobutton(root,text="English",variable=rtext,value="eng").grid(row=2,column=1)
rb1=ttk.Radiobutton(root,text="Hindi",variable=rtext,value="hin").grid(row=2,column=2)

button=ttk.Button(root,text="Detect!",command=Detect).grid(padx=10,pady=10,row=4,column=1)

img = Image.open("./ImagesPdf/grey.png")
img = img.resize((250, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(root,image=img)
panel.image=img

root.mainloop()
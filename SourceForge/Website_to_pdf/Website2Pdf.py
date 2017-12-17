#! /usr/bin/env python
#
# Code by Vinay Narayana
#Dec 18, 2017 01:34:53 AM
import sys
import os
import urllib.request as ul
from urllib.request import quote
import webbrowser
import Website2PdfCore as wc

try:
    from Tkinter import *
    import tkinterMessageBox as messagebox
except ImportError:
    from tkinter import *
    from tkinter import messagebox

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import Website2PdfCompact_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Website2Pdf (root)
    Website2PdfCompact_support.init(root, top)
    root.mainloop()

w = None
def create_Website2Pdf(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Website2Pdf (w)
    Website2PdfCompact_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Website2Pdf():
    global w
    w.destroy()
    w = None


class Website2Pdf:
    def urlParse(self):
        #print("here1")
        url = self.txtUrl.get()
        return url
    '''
    def dirParse(self):
        #print("here1")
        direc = self.txtUrl.get()
        if (os.path.exists(direc)):
            print("direc exists")
            messagebox.showinfo("Website2pdf","Directory exists!")
        return direc
    '''
        
    def convertMethod(self):
        url = self.urlParse()
        #direc = self.dirParse()
        direc = None
        if not os.path.exists("./wkhtmltopdf.exe"):
            messagebox.showwarning("Website2pdf", "wkhtmlpdf doesn't exist, keep it in the current folder")
        checkUrl = 404
        try:
            checkUrl = ul.urlopen(url)
        except ValueError:
            messagebox.showerror("Website2pdf","Url isn't valid")
            return;
        flag,fname = None, None
        if(checkUrl.getcode()!=404):
            if direc :
                if (os.path.exists(direc)):
                    try:
                        flag,fname = wc.converter(url,direc)
                    except:
                        messagebox.showwarning("Website2pdf", "Restart the application, UrlError")
                else:
                    messagebox.showinfo("Website2pdf","Directory doesn't exist, using default one")
                    direc= None
                    try: 
                        flag,fname = wc.converter(url,direc)
                    except:
                        messagebox.showwarning("Website2pdf", "Restart the application, UrlError")
            else:
                try:
                    flag,fname = wc.converter(url,direc)
                except:
                        messagebox.showwarning("Website2pdf", "Restart the application, UrlError")

        else:
            messagebox.showerror("Website2Pdf", "Enter the Url")

        print(flag,fname)
        if flag:
            openf = messagebox.askyesno("Website2Pdf","File {} created, want to open it?".format(fname))
            if openf:
                os.system("explorer {}\\Website2Pdf\\{}".format(os.getcwd(),fname))
        else:
            messagebox.showerror("Website2Pdf","Error, occured mail to dev!")

    def mailto(self):
        "recipients: string with comma-separated emails (no spaces!)"
        webbrowser.open("mailto:vinay@programmer.net?subject=Website2Pdf mail &body=")


    def helper(self):
        helpmessage = '''
        ♣♣ View your favorite webpages offline with this application ♣♣
        → Enter the url and click convert button to do it.
        → Files will be in the Website2Pdf folder of current directory.
        → Download wkhtmlpdf to current folder.
        → wkhtmlpdf if shown error, use download button.
            '''
        messagebox.showinfo("Website2Pdf",helpmessage)


    def sourceCode(self):
        webbrowser.open(r"https://github.com/Vinay26k/python/blob/master/Projects/Automate%20with%20Python/GetContent.py")


    def AboutMe(self):
        msg = '''
        https://github.com/Vinay26k/
        Mail : vinay@programmer.net
'''
        messagebox.showinfo("Website2Pdf",msg)


    def download(self):
        webbrowser.open(r"https://www.dropbox.com/s/gaufp6vkathbkk0/wkhtmltopdf.exe?dl=1")
        
                            
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("599x369+486+274")
        top.title("Website2Pdf")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.urlLabel = Label(top)
        self.urlLabel.place(relx=0.02, rely=0.05, height=51, width=124)
        self.urlLabel.configure(activebackground="#f9f9f9")
        self.urlLabel.configure(activeforeground="black")
        self.urlLabel.configure(background="#d9d9d9")
        self.urlLabel.configure(disabledforeground="#a3a3a3")
        self.urlLabel.configure(foreground="#000000")
        self.urlLabel.configure(highlightbackground="#d9d9d9")
        self.urlLabel.configure(highlightcolor="black")
        self.urlLabel.configure(text='''URL''')
        self.urlLabel.configure(width=124)

        self.txtUrl = Entry(top)
        self.txtUrl.place(relx=0.22, rely=0.08, relheight=0.08, relwidth=0.54)
        self.txtUrl.configure(background="white")
        self.txtUrl.configure(disabledforeground="#a3a3a3")
        self.txtUrl.configure(font="TkFixedFont")
        self.txtUrl.configure(foreground="#000000")
        self.txtUrl.configure(highlightbackground="#d9d9d9")
        self.txtUrl.configure(highlightcolor="black")
        self.txtUrl.configure(insertbackground="black")
        self.txtUrl.configure(selectbackground="#c4c4c4")
        self.txtUrl.configure(selectforeground="black")
        self.txtUrl.configure(width=324)

        self.Message1 = Message(top)
        self.Message1.place(relx=0.07, rely=0.16, relheight=0.09, relwidth=0.7)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''example : https://github.com/Vinay26k''')
        self.Message1.configure(width=420)

        self.btnConvert = Button(top)
        self.btnConvert.place(relx=0.27, rely=0.6, height=34, width=107)
        self.btnConvert.configure(activebackground="#d9d9d9")
        self.btnConvert.configure(activeforeground="#000000")
        self.btnConvert.configure(background="#d9d9d9")
        self.btnConvert.configure(disabledforeground="#a3a3a3")
        self.btnConvert.configure(foreground="#000000")
        self.btnConvert.configure(highlightbackground="#d9d9d9")
        self.btnConvert.configure(highlightcolor="black")
        self.btnConvert.configure(pady="0")
        self.btnConvert.configure(text='''Convert to PDF''')
        self.btnConvert.configure(command = self.convertMethod)

        self.btnMail = Button(top)
        self.btnMail.place(relx=0.83, rely=0.46, height=34, width=87)
        self.btnMail.configure(activebackground="#d9d9d9")
        self.btnMail.configure(activeforeground="#000000")
        self.btnMail.configure(background="#d9d9d9")
        self.btnMail.configure(disabledforeground="#a3a3a3")
        self.btnMail.configure(foreground="#000000")
        self.btnMail.configure(highlightbackground="#d9d9d9")
        self.btnMail.configure(highlightcolor="black")
        self.btnMail.configure(pady="0")
        self.btnMail.configure(text='''Mail to Dev!''')
        self.btnMail.configure(command = self.mailto)

        self.Message2 = Message(top)
        self.Message2.place(relx=0.2, rely=0.24, relheight=0.22, relwidth=0.47)
        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''By default, files will stored in Website2Pdf folder. Enter your desired directory here.''')
        self.Message2.configure(width=280)

        self.btnhelp = Button(top)
        self.btnhelp.place(relx=0.52, rely=0.6, height=34, width=97)
        self.btnhelp.configure(activebackground="#d9d9d9")
        self.btnhelp.configure(activeforeground="#000000")
        self.btnhelp.configure(background="#d9d9d9")
        self.btnhelp.configure(disabledforeground="#a3a3a3")
        self.btnhelp.configure(foreground="#000000")
        self.btnhelp.configure(highlightbackground="#d9d9d9")
        self.btnhelp.configure(highlightcolor="black")
        self.btnhelp.configure(pady="0")
        self.btnhelp.configure(text='''help''')
        self.btnhelp.configure(command = self.helper)

        self.btnSource = Button(top)
        self.btnSource.place(relx=0.83, rely=0.33, height=34, width=87)
        self.btnSource.configure(activebackground="#d9d9d9")
        self.btnSource.configure(activeforeground="#000000")
        self.btnSource.configure(background="#d9d9d9")
        self.btnSource.configure(disabledforeground="#a3a3a3")
        self.btnSource.configure(foreground="#000000")
        self.btnSource.configure(highlightbackground="#d9d9d9")
        self.btnSource.configure(highlightcolor="black")
        self.btnSource.configure(pady="0")
        self.btnSource.configure(text='''Source Code''')
        self.btnSource.configure(command = self.sourceCode)

        self.btnAbout = Button(top)
        self.btnAbout.place(relx=0.83, rely=0.6, height=34, width=87)
        self.btnAbout.configure(activebackground="#d9d9d9")
        self.btnAbout.configure(activeforeground="#000000")
        self.btnAbout.configure(background="#d9d9d9")
        self.btnAbout.configure(disabledforeground="#a3a3a3")
        self.btnAbout.configure(foreground="#000000")
        self.btnAbout.configure(highlightbackground="#d9d9d9")
        self.btnAbout.configure(highlightcolor="black")
        self.btnAbout.configure(pady="0")
        self.btnAbout.configure(text='''About Dev''')
        self.btnAbout.configure(command = self.AboutMe)

        self.btnDownload = Button(top)
        self.btnDownload.place(relx=0.62, rely=0.43, height=34, width=87)
        self.btnDownload.configure(activebackground="#d9d9d9")
        self.btnDownload.configure(activeforeground="#000000")
        self.btnDownload.configure(background="#d9d9d9")
        self.btnDownload.configure(disabledforeground="#a3a3a3")
        self.btnDownload.configure(foreground="#000000")
        self.btnDownload.configure(highlightbackground="#d9d9d9")
        self.btnDownload.configure(highlightcolor="black")
        self.btnDownload.configure(pady="0")
        self.btnDownload.configure(text='''Download''')
        self.btnDownload.configure(width=87)
        self.btnDownload.configure(command = self.download)

        self.Message3 = Message(top)
        self.Message3.place(relx=0.15, rely=0.43, relheight=0.09, relwidth=0.47)
        self.Message3.configure(background="#d9d9d9")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''Download wkhtmltopdf from here → ''')
        self.Message3.configure(width=280)

        self.Message4 = Message(top)
        self.Message4.place(relx=0.0, rely=0.89, relheight=0.09, relwidth=1.0)
        self.Message4.configure(background="#d9d9d9")
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(text='''⌂ Note → wkhtmlpdf should be in the same folder along with this application, it's a supporting executable.''')
        self.Message4.configure(width=600)



if __name__ == '__main__':
    vp_start_gui()




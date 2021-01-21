import time
from tkinter import *
import random
import string
import pyperclip


class Generator():
    def __init__(self):
        root = Tk()
        root.iconbitmap('icon.ico')
        root.title('password generator')
        root.geometry('300x200')
        self.pas = StringVar()

        def copy():
            self.pas.set('Text copied')

        def passw():
            self.pas.set('ok generating strong password')
            time.sleep(1)
            s1 = string.ascii_lowercase
            s2 = string.ascii_uppercase
            s3 = string.digits
            s4 = string.punctuation
            try:
                query = int(entry.get())
                s = []
                s.extend(list(s1))
                s.extend(list(s2))
                s.extend(list(s3))
                s.extend(list(s4))
                # self.pas.set(s)
                #  print(s)
                random.shuffle(s)
                # self.pas.set(s)
                # print(s)
                #  print("".join(s[0:query]))
                x = "".join(s[0:query])
                self.pas.set(x)
                pyperclip.copy(x)
            except:
                self.pas.set('Hey man 1st give the length of the password')

        userFrame = LabelFrame(root, text='strong password', font=('Verdana', 10, 'bold'))
        userFrame.pack(fill="both", expand='yes')

        left = Message(userFrame, textvariable=self.pas, bg='Black', fg='white')
        left.config(font=('Helvetica', 10,))
        left.pack(fill='both', expand='yes')

        length = Label(root, text='Please give the length in number', font=('verdana', 10), bg='black', fg='white')
        length.pack(fill='x', expand='no')
        entry = Entry(root, fg='red', font=('verdana', 10))
        entry.pack(fill='x', expand='no')
        btn = Button(root, text='Generate strong password', font=('verdana', 10), bg='deepskyblue', fg='red',
                     command=passw).pack(fill='x', expand='no')
        btn = Button(root, text='copy it', font=('verdana', 10), bg='yellow', fg='red',
                     command=copy).pack(fill='x', expand='no')
        btn = Button(root, text='Close', font=('verdana', 10), bg='deepskyblue', fg='red',
                     command=root
                     .destroy).pack(fill='x', expand='no')
        root.mainloop()


Generator()

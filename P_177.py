from tkinter import *
import random

root = Tk()
root.minsize(800, 600)
root.maxsize(800, 600)
root.title('Private Login')
root.configure(background='Pink')

label_captcha = Label(root, bg='white', fg='black',
                      font=('Bradley Hand ITC', 22, 'bold'))
label_captcha.place(relx=0.5, rely=0.6, anchor=CENTER)

input_name = Entry(root)
input_password = Entry(root, show='*')
input_captcha = Entry(root)

input_name.place(relx=0.4, rely=0.1, anchor=CENTER)
input_password.place(relx=0.4, rely=0.24, anchor=CENTER)
input_captcha.place(relx=0.4, rely=0.38, anchor=CENTER)


def showpass():
    if(input_password['show'] == '*'):
        input_password['show'] = ''
    elif(input_password['show'] == ''):
        input_password['show'] = '*'
    else:
        messagebox.showinfo('error', 'An error occured, please try again')


class captcha:
    def __init__(self):
        self.ucase_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.lcase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.spl_char = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '~']
        self.num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.y = ''

    def generate(self):
        self.C = ''
        for i in range(5):
            self.x = random.randint(1, 4)
            if(self.x == 1):
                self.n1 = random.randint(0, 25)
                self.e = self.ucase_alphabets[self.n1]
                self.C = self.C + str(self.e)
            elif(self.x == 2):
                self.n2 = random.randint(0, 25)
                self.e = self.lcase_alphabets[self.n2]
                self.C = self.C + str(self.e)
            elif(self.x == 3):
                self.n3 = random.randint(0, 9)
                self.e = self.spl_char[self.n3]
                self.C = self.C + str(self.e)
            else:
                self.n4 = random.randint(0, 9)
                self.e = self.num[self.n4]
                self.C = self.C + str(self.e)
        label_captcha['text'] = self.C

    def check_captcha(self, string):
        self.user_captcha = string
        if(len(self.C) > 0):
            if(self.user_captcha == self.C):
                self.y = 'True'
            else:
                self.y = 'False'
        else:
            messagebox.showinfo('error', 'No captcha found!')

    def generate_pass(self):
        self.C = ''
        for i in range(8):
            self.x = random.randint(1, 4)
            if(self.x == 1):
                self.n1 = random.randint(0, 25)
                self.e = self.ucase_alphabets[self.n1]
                self.C = self.C + str(self.e)
            elif(self.x == 2):
                self.n2 = random.randint(0, 25)
                self.e = self.lcase_alphabets[self.n2]
                self.C = self.C + str(self.e)
            elif(self.x == 3):
                self.n3 = random.randint(0, 9)
                self.e = self.spl_char[self.n3]
                self.C = self.C + str(self.e)
            else:
                self.n4 = random.randint(0, 9)
                self.e = self.num[self.n4]
                self.C = self.C + str(self.e)
        input_password.delete(0, END)
        input_password.insert(END, self.C)


b = captcha()
b.generate()


class DB:
    def __init__(self):
        self.d = []
        self.__name = ''
        self.__password = ''
        self.captcha = ''
        self.k = 0

    def update(self):
        self.__name = input_name.get()
        self.__password = input_password.get()
        self.captcha = input_captcha.get()
        if(len(self.__name) > 0 and len(self.__password) > 0 and len(self.captcha) > 0):
            b.check_captcha(self.captcha)
            if(b.y == 'True'):
                self.d.append(self.__name)
                self.d.append(self.__password)
                messagebox.showinfo('Success', 'Successfully updated data')
                input_name.delete(0, END)
                input_password.delete(0, END)
                input_captcha.delete(0, END)
                self.k = 1
                b.generate
            else:
                messagebox.showinfo('error', 'Wrong captcha')
                b.generate()
        else:
            messagebox.showinfo(
                'error', 'Please check the name,password and captcha again!')

    def show(self):
        if(self.k == 1):
            win = Tk()
            win.minsize(600, 400)
            win.maxsize = (600, 400)
            win.title('Profile')
            win.configure(background='navy')

            l1 = Label(win, text='Profile', font=(
                'Comic Sans MS', 24, 'bold'), bg='navy', fg='white')
            l1.place(relx=0.5, rely=0.1, anchor=CENTER)

            l2 = Label(win, text='Name : ' +
                       str(self.d[0]), bg='navy', fg='white', font=('Comic Sans MS', 18, 'bold'))
            l2.place(relx=0.5, rely=0.3, anchor=CENTER)

            l3 = Label(win, text='Password : ' +
                       str(self.d[1]), bg='navy', fg='white', font=('Comic Sans MS', 18, 'bold'))
            l3.place(relx=0.5, rely=0.5, anchor=CENTER)

            def close_win():
                win.destroy()

            bt = Button(win, text='Close', fg='white', bg='red', font=(
                'Comic Sans MS', 14, 'bold'), command=close_win, relief=FLAT)
            bt.place(relx=0.5, rely=0.7, anchor=CENTER)
            win.mainloop()
        else:
            messagebox.showinfo('error', 'No profile created!')


database = DB()

label1 = Label(root, text='Name : ', bg='pink', fg='black',
               font=('Comic Sans MS', 18, 'bold'))
label1.place(relx=0.2, rely=0.1, anchor=CENTER)

label2 = Label(root, text='Password : ', bg='pink', fg='black',
               font=('Comic Sans MS', 18, 'bold'))
label2.place(relx=0.2, rely=0.24, anchor=CENTER)

label3 = Label(root, text='Captcha : ', bg='pink', fg='black',
               font=('Comic Sans MS', 18, 'bold'))
label3.place(relx=0.2, rely=0.38, anchor=CENTER)

btn_update = Button(root, text='Update Login Details',
                    bg='brown', fg='black', font=('Comic Sans MS', 12, 'bold'), relief=FLAT, command=database.update)
btn_update.place(relx=0.78, rely=0.15, anchor=CENTER)

btn_show = Button(root, text='Show Profile',
                  bg='brown', fg='black', font=('Comic Sans MS', 12, 'bold'), relief=FLAT, command=database.show)
btn_show.place(relx=0.78, rely=0.32, anchor=CENTER)

button_refresh = Button(root, text='Refresh', bg='red',
                        fg='white', font=('Comic Sans MS', 12, 'bold'), relief=FLAT, command=b.generate)
button_refresh.place(relx=0.63, rely=0.6, anchor=CENTER)

checkbtn = Checkbutton(root, text='Show', font=(
    'Comic Sans MS', 12, 'bold'), bg='pink', command=showpass)
checkbtn.place(relx=0.38, rely=0.3, anchor=CENTER)

auto_gen = Button(root, text='Auto Generate',
                  font=('Comic Sans MS', 10, 'bold'), bg='brown', fg='black', relief=FLAT, command=b.generate_pass)
auto_gen.place(relx=0.55, rely=0.24, anchor=CENTER)

root.mainloop()

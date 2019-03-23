from tkinter import *
import tkinter.messagebox as tm


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "Bhupindher Kaur" and password == "PYTHON PROJECT":
            def ab():

                inp = str(x.get())
                w = a.get()
                if (w is 1):  # BINARY TO DECIMAL AND THEN TO OTHER SYSTEMS
                    # if __name__ == '__main__':
                    inp = int(inp, 2)
                    bi = bin(inp)
                    oc = oct(inp)
                    dec = inp
                    hexa = hex(inp)
                elif (w is 2):
                    inp = int(inp, 8)
                    bi = bin(inp)
                    oc = oct(inp)
                    dec = inp
                    hexa = hex(inp)

                elif (w is 3):
                    inp = int(inp)
                    bi = bin(inp)
                    oc = oct(inp)
                    dec = inp
                    hexa = hex(inp)



                else:
                    inp = int(inp, 16)
                    bi = bin(inp)
                    oc = oct(inp)
                    dec = inp
                    hexa = hex(inp)

                result = Label(top, text="Result:").place(x=100, y=290)

                l1 = Label(top, text="Binary     :").place(x=130, y=320)
                l2 = Label(top, text="octal      :").place(x=130, y=370)
                l3 = Label(top, text="decimal    :").place(x=130, y=420)
                l4 = Label(top, text="hexadecimal:").place(x=130, y=470)

                e1 = Label(top, text=bi).place(x=250, y=320)
                e2 = Label(top, text=oc).place(x=250, y=370)
                e3 = Label(top, text=dec).place(x=250, y=420)
                e4 = Label(top, text=hexa).place(x=250, y=470)

                explain = Label(top, text="Explanation:").place(x=450, y=290)

            top = Tk()
            top.title("Number Convertor")
            a = IntVar()
            x = IntVar()
            top.resizable(width=False, height=False)

            lab = Label(top, text="Enter a number").place(x=280, y=10)
            num = Entry(top, bd=5, textvariable=x).place(x=380, y=10)

            ti = Label(top, text="Tick the number type you have entered:").place(x=280, y=50)
            C1 = Radiobutton(top, text="Binary", value=1, var=a, height=0, width=10).place(x=350, y=80)
            C2 = Radiobutton(top, text="Octal", value=2, var=a, height=0, width=10).place(x=347, y=110)
            C3 = Radiobutton(top, text="Decimal", value=3, var=a, height=0, width=10).place(x=355, y=140)
            C4 = Radiobutton(top, text="Hexadecimal", value=4, var=a, height=0, width=10).place(x=367, y=170)

            but = Button(top, text="Result", command=ab).place(x=390, y=220)

            top.geometry("1000x700")

        else:
            tm.showerror("Login error", "Incorrect username")


root = Tk()
lf = LoginFrame(root)
root.mainloop()
from builtins import print
from tkinter import *  # Import tkinter
import tkinter.messagebox as box
from tkinter import simpledialog
import tkinter.font as tkFont


class ScoreBoard(Canvas):
    def __init__(self, container, width=800, height=400):
        super().__init__(container, width=width, height=height)
        # container of the canvas
        self.window = container
        self.width = width
        self.height = height

        self.red = 0
        self.blue = 0

        self.config(bg="red")
        self.bind('<Configure>', self.resize)

        self.create_rectangle(0, 0, self.width / 2, self.height, fill="blue")

        #######################
        # set up score label
        # blue one
        self.blue_label = Label(self.window, font=("Helvetica", 240),
                                text=str(self.blue))
        self.blue_label.config(bg='blue', fg='white')
        self.put_blue()
        self.blue_label.bind("<Button-1>", self.blue_1)
        self.blue_label.bind("<Button-3>", self.blue_1_)

        # red one
        self.red_label = Label(self.window, font=("Helvetica", 240),
                               text=str(self.red))
        self.red_label.config(bg='red', fg='white')
        self.put_red()
        self.red_label.bind("<Button-1>", self.red_1)
        self.red_label.bind("<Button-3>", self.red_1_)


        ##################################################
        # setup button
        # USER_INP = simpledialog.askstring(title="Test",
          #                                prompt="What's your Name?:")

        setup_button = Button(self.window, text='Thiết lập',
                              command=self.setupButton)
        setup_button.place(relx=0.47, rely=0.9)
        pass

    def setupButton(self):
        # reset score
        self.red = 0
        self.blue = 0
        self.blue_label.config(text=str(self.blue))
        self.red_label.config(text=str(self.red))

        pass

    def put_blue(self):
        if self.blue >= 10:
            self.blue_label.place(relx=0.1, rely=0.25)
            pass
        else:
            self.blue_label.place(relx=0.15, rely=0.25)
            pass
        self.blue_label.config(text=str(self.blue))
        pass

    def put_red(self):
        if self.red >= 10:
            self.red_label.place(relx=0.60, rely=0.25)
            pass
        else:
            self.red_label.place(relx=0.65, rely=0.25)
            pass
        self.red_label.config(text=str(self.red))
        pass

    def draw_board(self):
        # clean the canvas
        self.delete("all")
        self.create_rectangle(0, 0, self.width / 2, self.height, fill="blue")

        pass

    def resize(self, event):
        w, h = event.width, event.height
        self.config(width=w, height=h)
        self.width = w
        self.height = h
        self.draw_board()

        pass

    def red_1(self, event):
        self.red = self.red + 1
        self.put_red()
        # self.draw_board()
        pass

    def red_1_(self, event):
        self.red = self.red - 1
        self.put_red()
        # self.draw_board()
        pass

    pass

    def blue_1(self, event):
        self.blue = self.blue + 1
        self.put_blue()
        # self.draw_board()
        pass

    def blue_1_(self, event):
        self.blue = self.blue - 1
        self.put_blue()
        # self.draw_board()
        pass

    pass


window = Tk()  # Create a window
window.title('Score Board')  # Set title

view = ScoreBoard(window)
view.pack(fill=BOTH, expand=True)

window.mainloop()  # Create an event loop


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
        ###################################################
        # start button
        start_button = Button(self.window, text='Bắt đầu',
                              command=self.startButton)
        start_button.place(relx=0.44, rely=0.2)

        # pause button
        self.pause_button = Button(self.window, text='Tạm dừng',
                              command=self.pauseButton)
        self.pause_button.place(relx=0.52, rely=0.2)
        self.unpaused = True

        ###################################################
        # count down
        self.remaining = 120
        self.time_range = 120
        self.countdown_label=Label(self, text="0 :00 ", width=8,
                                   font=("Times", 40),)
        self.countdown_label.place(relx=0.4, rely=0.04)

        pass

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining
            pass
        if self.remaining <= 0:
            self.countdown_label.configure(text="Hết giờ")
            pass
        else:
            if self.unpaused is True:
                minute = int(self.remaining / 60)
                seconds = str(self.remaining - minute * 60)
                if int(seconds) < 10:
                    seconds = '0' + seconds
                    pass
                self.countdown_label.configure(text="%s : %s" % (minute, seconds))
                self.remaining = self.remaining - 1
                self.after(1000, self.countdown)
                pass
            pass

        pass

    def pauseButton(self):
        if self.unpaused is True:
            self.unpaused = False
            self.pause_button.config(text="Tiếp tục")
            pass
        else:
            self.unpaused = True
            self.pause_button.config(text="Tạm dừng")
            self.countdown()
            pass
        pass

    def startButton(self):
        self.unpaused = True
        self.countdown(self.time_range)
        pass

    def setupButton(self):
        # reset score
        self.red = 0
        self.blue = 0
        self.blue_label.config(text=str(self.blue))
        self.red_label.config(text=str(self.red))

        self.time_range = simpledialog.askinteger("Thiết lập", "Thêm số giây của trân đấu",
                                        parent=self.window)
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


from tkinter import *  # Import tkinter
#from tkinter.ttk import *

class ScoreBoard(Canvas):
    def __init__(self, container, width=800, height=450):
        super().__init__(container, width=width, height=height)
        # container of the canvas
        self.window = container
        self.width = width
        self.height = height
        self.red = 0
        self.blue = 0


        self.draw_board()
        pass

    def draw_board(self):
        # clean the canvas
        self.delete("all")
        yy = 0.92

        self.create_rectangle(0, 0, self.width / 2, self.height, fill="blue")
        label = label = Label(self.window, text =str(self.blue),
                              font=("Helvetica", 100))
        label.config(bg='black', fg='yellow')
        label.place(relx=0.2, rely=0.3)
        label.bind("<Button>", self.blue_1)



       # self.create_text(self.width / 4, self.height / 2, fill = 'white',
        #                 font = "Times 100 bold", text =str(self.blue))


       #bt_blue_1 = Button(self.window, command=self.blue_1,
                      #     text='+1', width = 8)
       # bt_blue_1.place(relx=0.01, rely= yy - 0.01)
       # bt_blue_2 = Button(self.window, command=self.blue_1,
        #                   text='+2', width = 8)
       # bt_blue_2.place(relx=0.11, rely=yy - 0.01)
        pass

    def blue_1(self, event ):
        self.blue = self.blue + 1
        self.draw_board()
        pass

    pass



window = Tk()  # Create a window
window.title('Score Board')  # Set title


view = ScoreBoard(window)
view.pack()

window.mainloop()  # Create an event loop
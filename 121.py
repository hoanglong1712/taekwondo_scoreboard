from tkinter import *

class testApp2:
    def __init__( self, master ):
        self.ma = master
        self.f = Frame( self.ma )
        self.f.pack(fill=BOTH, expand=YES)
        self.cv = Canvas(self.f, width=25, height=25, bg='red')
        self.cv.pack(fill=BOTH, expand=YES)
        self.b1 = Button( self.f, text='Hello', height=1, width=10,
        padx=0, pady=1)
        self.b1.pack(side=BOTTOM, anchor=E, padx=4, pady=4)

root = Tk()
app = testApp2(root)
root.mainloop()
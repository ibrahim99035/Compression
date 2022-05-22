from CompAlgorithms.LZSS import LZSSclass
from CompAlgorithms.LZW import LZWclass

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Compression Algorithms Program")
root.geometry('700x600')

def displayResults1():
    global entry
    userInput = entry.get()
    LZSScompressed = LZSSclass.compress(userInput)
    LZSSdecompressed = LZSSclass.decompress(LZSScompressed)
    
    ResultLabel1.configure(text="LZSS Compressed: " + LZSScompressed + '\n' + "LZSS Decompressed: " + LZSSdecompressed + '\n' + '---------------------------')

def displayResults2():
    global entry
    userInput = entry.get()
    LZWcompressed = LZWclass.compress(userInput)
    LZWdecompressed = LZWclass.decompress(LZWcompressed)
    
    ResultLabel2.configure(text="LZW Compressed: " + LZWcompressed + '\n' + "LZW Decompressed: " + LZWdecompressed + '\n' + '---------------------------')

    




FirstLabel = Label(root, text="Choose The Algorithm You Want To Use", font=("Helvetica", 20))
FirstLabel.pack()

entry = Entry(root, width=50)
entry.focus_set()
entry.pack()

LZSSButton = Button(root, text="LZSS", font=("Helvetica", 20), height=2, width=5, command=displayResults1)
LZSSButton.pack()

LZWButton = Button(root, text="LZW", font=("Helvetica", 20), height=2, width=5, command=displayResults2)
LZWButton.pack()

ResultLabel1 = Label(root, text="", font=("Helvetica", 15))
ResultLabel1.pack()

ResultLabel2 = Label(root, text="", font=("Helvetica", 15))
ResultLabel2.pack()

root.mainloop()

from tkinter import *
from tkinter import messagebox
import binascii 

global result

#title=title==Genre=C==[C7 F7 LZBb7 Eb7 ]==0=0

def gethex(s):
  r = len(s)
  outputstr = ""
  for i in range(r):
     mystring = s[i]
     x = bytes(mystring,'utf-8')
     x = binascii.hexlify(x)
     y = str(x,'ascii')
     z = '%' + y
     outputstr = outputstr + z
  return outputstr

def createhtml(chordstxt):
    inp = open("irealhead.txt",'r')

    head = inp.read()

    inp = open("irealfoot.txt",'r')

    foot = inp.read()
    musicstr = ""
    
    s = "songname"
    musicstr = gethex(s)
    musicstr = musicstr + '=' + musicstr + "=="
    genre = gethex("Latin")
    musicstr = musicstr + genre + "="
    key = gethex("C")
    musicstr = musicstr + key + "=="
    bar = gethex("[")
    chordsseq = chordstxt
    chordsseq = chordsseq.replace("\n","")
    musicstr = musicstr + chordsseq

    musicstr = musicstr +"%20"
    musicstr = musicstr + gethex(']')

    musicstr = musicstr + "==" + "%20%" + "%30"


    filestr = head + musicstr +foot

    

    h = open("ireal.html", 'w')
    h.write(filestr)
#end of createhtml function


root = None
entryBox = None
label = None
T = NONE




def buttonPushed():
    result = T.get("1.0", "end")
    createhtml(result)


def createTextBox(parent):
    global entryBox
    global label
    label = Label(parent,text="enter song name")
    label.pack()
    entryBox = Entry(parent)
    entryBox.pack()





def main():
    global root
    global result
    global T
    root = Tk()  # Create the root (base) window where all widgets ")


    messagebox.showinfo(title="ireal",message="This app converts text to a irealpro  html file see help text")

    myButton = Button(root, text="convert",command=buttonPushed)
    myButton.pack()
    
    T = Text(root ,height=20, width=80)
    T.pack()
    quote = """Please enter chord sequence following the for format below no leading '|' bar
    delete this text before you start and songname key etc can be edited 
    after import on ireal editor 
    it just gives a generic import in C and songname for simple chord sequences.
    press convert and it will leave a html file to import into ireal.
    This is in early stages of development so keep chords etc simple and edit on irealpro app.
    program by Paul McRae pbmcrae42@yahoo.com
    
    
    BbMaj7 G-7 |C-7 F7 |BbMaj7 G-7 |C-7 F7 |
    BbMaj7 G-7 |C-7 F7 |BbMaj7 G-7 |C-7 F7 |
    D7         |G7     |C7         |F7     |
    BbMaj7 G-7 |C-7 F7 |BbMaj7 G-7 |C-7 F7 
    """
    T.insert(END, quote)

    

    root.mainloop()


main()



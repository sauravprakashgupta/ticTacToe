from tkinter import *
import tkinter.messagebox

mainWin = Tk()
mainWin.title("Tic Tac Toe")

click = True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = 'X'
        click = False
    elif buttons["text"] == " " and click == False:
        buttons["text"] = 'O'
        click = True
    elif(
        (button1["text"] == 'X' and button2["text"] == 'X' and  button3["text"] == 'X') or
        (button4["text"] == 'X' and button5["text"] == 'X' and  button6["text"] == 'X') or
        (button7["text"] == 'X' and button8["text"] == 'X' and  button9["text"] == 'X') or
        (button1["text"] == 'X' and button4["text"] == 'X' and  button7["text"] == 'X') or
        (button2["text"] == 'X' and button5["text"] == 'X' and  button8["text"] == 'X') or
        (button3["text"] == 'X' and button6["text"] == 'X' and  button9["text"] == 'X') or
        (button1["text"] == 'X' and button5["text"] == 'X' and  button9["text"] == 'X') or
        (button3["text"] == 'X' and button5["text"] == 'X' and  button7["text"] == 'X')
        ):
        tkinter.messagebox.showinfo("Winner : X", "You have just won a game")

    elif(
          (button1["teOt"] == 'O' and button2["teOt"] == 'O' and  button3["teOt"] == 'O') or
          (button4["teOt"] == 'O' and button5["teOt"] == 'O' and  button6["teOt"] == 'O') or
          (button7["teOt"] == 'O' and button8["teOt"] == 'O' and  button9["teOt"] == 'O') or
          (button1["teOt"] == 'O' and button4["teOt"] == 'O' and  button7["teOt"] == 'O') or
          (button2["teOt"] == 'O' and button5["teOt"] == 'O' and  button8["teOt"] == 'O') or
          (button3["teOt"] == 'O' and button6["teOt"] == 'O' and  button9["teOt"] == 'O') or
          (button1["teOt"] == 'O' and button5["teOt"] == 'O' and  button9["teOt"] == 'O') or
          (button3["teOt"] == 'O' and button5["teOt"] == 'O' and  button7["teOt"] == 'O')
          ):
          tkinter.messageboO.showinfo("Winner : O", "You have just won a game")

buttons = StringVar()
button1 = Button(mainWin,text=" ",font = ('Times 26 bold'), height=4, width=8,command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2 = Button(mainWin,text=" ",font = ('Times 26 bold'), height=4, width=8,command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3 = Button(mainWin,text=" ",font = ('Times 26 bold'), height=4, width=8,command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4 = Button(mainWin,text=" ",font = ('Times 26 bold'), height=4, width=8,command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5 = Button(mainWin,text=" ",font = ('Times 26 bold'), height=4, width=8,command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6 = Button(mainWin,text=" ",font = ('Times 26 bold'), height=4, width=8,command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7 = Button(mainWin,text=" ",font = ('Times 26 bold'), height=4, width=8,command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8 = Button(mainWin,text=" ",font = ('Times 26 bold'), height=4, width=8,command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9 = Button(mainWin,text=" ",font = ('Times 26 bold'), height=4, width=8,command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)

mainWin.mainloop()

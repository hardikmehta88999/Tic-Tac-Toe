from tkinter import *
import tkinter.messagebox
tk=Tk()
tk.title("TIC TAC TOE")
click=True 
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state =DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
    
def checker(buttons):
    global click,flag#it can be access any part of program 
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        check()
        flag+=1
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        check()
        flag+=1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")
    
def check():
    
    if (button1["text"] =="X" and button2["text"] =="X" and button3["text"] =="X" or
          button4["text"] =="X" and button5["text"] =="X" and button6["text"] =="X" or
          button7["text"] =="X" and button8["text"] =="X" and button9["text"] =="X" or
          button3["text"] =="X" and button5["text"] =="X" and button7["text"] =="X" or
          button1["text"] =="X" and button5["text"] =="X" and button9["text"] =="X" or
          button1["text"] =="X" and button4["text"] =="X" and button7["text"] =="X" or
          button2["text"] =="X" and button5["text"] =="X" and button8["text"] =="X" or
          button3["text"] =="X" and button6["text"] =="X" and button9["text"] =="X"):
          disableButton()
          tkinter.messagebox.showinfo("WINNER X","you won")#to display the message 
          

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")


    elif (button1["text"] =="O" and button2["text"] =="O" and button3["text"] =="O" or
          button4["text"] =="O" and button5["text"] =="O" and button6["text"] =="O" or
          button7["text"] =="O" and button8["text"] =="O" and button9["text"] =="O" or
          button3["text"] =="O" and button5["text"] =="O" and button7["text"] =="O" or
          button1["text"] =="O" and button5["text"] =="O" and button9["text"] =="O" or
          button1["text"] =="O" and button4["text"] =="O" and button7["text"] =="O" or
          button2["text"] =="O" and button5["text"] =="O" and button8["text"] =="O" or
          button3["text"] =="O" and button6["text"] =="O" and button9["text"] =="O"):
          disableButton()
          tkinter.messagebox.showinfo("WINNER O","You won")
          
                  
    
buttons=StringVar()
button1= Button(tk,text=" ",font=('Times 26 bold'), height= 4 , width =8, command=lambda:checker(button1)) 
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2= Button(tk,text=" ",font=('Times 26 bold'), height= 4 , width =8, command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3= Button(tk,text=" ",font=('Times 26 bold'), height= 4 , width =8, command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4= Button(tk,text=" ",font=('Times 26 bold'), height= 4 , width =8, command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5= Button(tk,text=" ",font=('Times 26 bold'), height= 4 , width =8, command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6= Button(tk,text=" ",font=('Times 26 bold'), height= 4 , width =8, command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7= Button(tk,text=" ",font=('Times 26 bold'), height= 4 , width =8, command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8= Button(tk,text=" ",font=('Times 26 bold'), height= 4 , width =8, command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9= Button(tk,text=" ",font=('Times 26 bold'), height= 4 , width =8, command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)

tk.mainloop()
# it will automatically refresh our gui application so that it will look very clean when ever
#we play this game 
#command while click on button which fcuntion  will run so lambda used to call the function
#grid method to place the button tk on window
#sticky which means it will place widget on button means that it will be streched

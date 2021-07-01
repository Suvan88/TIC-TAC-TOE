import tkinter
from tkinter import *
from tkinter import messagebox
root=tkinter.Tk()
root.title("tictactoe")

clicked=True
count=0

def disabalebutton():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)






def ifwon():
    global winner
    winner=False
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner=True
        messagebox.showinfo("tictactoe","Congratulations X wins")
        disabalebutton()
    elif  b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=True
        messagebox.showinfo("tictactoe","Congratulations X wins")
        disabalebutton()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations X wins")
        disabalebutton()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations X wins")
        disabalebutton()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations X wins")
        disabalebutton()


    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations X wins")
        disabalebutton()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations X wins")
        disabalebutton()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations X wins")
        disabalebutton()


    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations X wins")
        disabalebutton()

    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner=True
        messagebox.showinfo("tictactoe","Congratulations O wins")
        disabalebutton()
    elif  b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=True
        messagebox.showinfo("tictactoe","Congratulations O wins")
        disabalebutton()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations O wins")
        disabalebutton()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations O wins")
        disabalebutton()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations O wins")
        disabalebutton()


    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations O wins")
        disabalebutton()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations O wins")
        disabalebutton()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations O wins")
        disabalebutton()


    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tictactoe","Congratulations O wins")
        disabalebutton()









def bclick(b):
    global  clicked,count
    if b["text"]=="" and clicked==True:
                b["text"] = "X"
                clicked=False
                count+=1
                ifwon()
    elif b["text"]=="" and clicked==False:
                b["text"]="O"
                clicked=True
                count+=1
                ifwon()

    else:
        messagebox.showerror("Tictactoe has alrerady been selected\nplease select new box")


    if count==9 and winner==False:
        messagebox.showinfo("tictactoe","it's a tie")
        disabalebutton()








def reset():
        global b1,b2,b3,b4,b5,b6,b7,b8,b9
        global clicked,count
        clicked=True
        count=0

        b1=Button(root,text="",font=("Helvetica",20),height="3",width="6",bg="SystemButtonFace",command=lambda:  bclick(b1))
        b2=Button(root,text="",font=("Helvetica",20),height="3",width="6",bg="SystemButtonFace",command=lambda:  bclick(b2))
        b3=Button(root,text="",font=("Helvetica",20),height="3",width="6",bg="SystemButtonFace",command=lambda:  bclick(b3))

        b4=Button(root,text="",font=("Helvetica",20),height="3",width="6",bg="SystemButtonFace",command=lambda:  bclick(b4))
        b5=Button(root,text="",font=("Helvetica",20),height="3",width="6",bg="SystemButtonFace",command=lambda:  bclick(b5))
        b6=Button(root,text="",font=("Helvetica",20),height="3",width="6",bg="SystemButtonFace",command=lambda:  bclick(b6))

        b7=Button(root,text="",font=("Helvetica",20),height="3",width="6",bg="SystemButtonFace",command=lambda:  bclick(b7))
        b8=Button(root,text="",font=("Helvetica",20),height="3",width="6",bg="SystemButtonFace",command=lambda:  bclick(b8))
        b9=Button(root,text="",font=("Helvetica",20),height="3",width="6",bg="SystemButtonFace",command=lambda:  bclick(b9))


        b1.grid(row=0,column=0)
        b2.grid(row=0,column=1)
        b3.grid(row=0,column=2)

        b4.grid(row=1,column=0)
        b5.grid(row=1,column=1)
        b6.grid(row=1,column=2)

        b7.grid(row=2,column=0)
        b8.grid(row=2,column=1)
        b9.grid(row=2,column=2)



mymenu=Menu(root)
root.config(menu=mymenu)

optionsmenu=Menu(mymenu,tearoff=False)
mymenu.add_cascade(label="Options",menu=optionsmenu)
optionsmenu.add_command(label="Rest Game" , command=reset)
reset()





root.mainloop()

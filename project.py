from tkinter import *
import random
 
mainFrame = Tk()
mainFrame.geometry("300x300")
 
mainFrame.title("Rock-Paper-Scissor")
 
computer_value = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}

def reset_game():
    btn1["state"] = "active"
    btn2["state"] = "active"
    btn3["state"] = "active"
    l1.config(text = "Player              ")
    l3.config(text = "Computer")
    l4.config(text = "")
 
def button_disable():
    btn1["state"] = "disable"
    btn2["state"] = "disable"
    btn3["state"] = "disable"
 

def isrock():
    bot = computer_value[str(random.randint(0,2))]
    if bot == "Rock":
        result = "Match Draw"
    elif bot=="Scissor":
        result = "Player Win"
    else:
        result = "Computer Win"
    l4.config(text = result)
    l1.config(text = "Rock            ")
    l3.config(text = bot)
    button_disable()
 

def ispaper():
    bot = computer_value[str(random.randint(0, 2))]
    if bot == "Paper":
        result = "Match Draw"
    elif bot=="Scissor":
        result = "Computer Win"
    else:
        result = "Player Win"
    l4.config(text = result)
    l1.config(text = "Paper           ")
    l3.config(text = bot)
    button_disable()
 

def isscissor():
    bot = computer_value[str(random.randint(0,2))]
    if bot == "Rock":
        result = "Computer Win"
    elif bot == "Scissor":
        result = "Match Draw"
    else:
        result = "Player Win"
    l4.config(text = result)
    l1.config(text = "Scissor         ")
    l3.config(text = bot)
    button_disable()
 
# Add Labels, Frames and Button
Label(mainFrame,
      text = "Rock Paper Scissor",
      font = "normal 20 bold",
      fg = "blue").pack(pady = 20)
 
frame = Frame(mainFrame)
frame.pack()
 
l1 = Label(frame,
           text = "Player              ",
           font = 10)
 
l2 = Label(frame,
           text = "VS             ",
           font = "normal 10 bold")
 
l3 = Label(frame, text = "Computer", font = 10)
 
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()
 
l4 = Label(mainFrame,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
l4.pack(pady = 20)
 
frame1 = Frame(mainFrame)
frame1.pack()
 
btn1 = Button(frame1, text = "Rock",
            font = 10, width = 7,
            command = isrock)
 
btn2 = Button(frame1, text = "Paper ",
            font = 10, width = 7,
            command = ispaper)
 
btn3 = Button(frame1, text = "Scissor",
            font = 10, width = 7,
            command = isscissor)
 
btn1.pack(side = LEFT, padx = 10)
btn2.pack(side = LEFT,padx = 10)
btn3.pack(padx = 10)
 
Button(mainFrame, text = "Reset Game",
       font = 10, fg = "red",
       bg = "black", command = reset_game).pack(pady = 20)
 
mainFrame.mainloop()
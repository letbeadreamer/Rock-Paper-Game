#steps to build a python Rock Paper Scissors Game
#Import modules
#Initializing the window
#setting images
#function for making rock paper scissors
#Function for making computer rock paper scissor
#function matching 
#exit function
#define buttons and labels widget

#importing modules

import random 
from tkinter import *

#initializing the window
root = Tk()
root.title("ROCK,PAPER,SCISSORS GAME USING PYTHONGEEKS")
width=650
height=580
window_width=root.winfo_screenwidth()
window_height=root.winfo_screenheight()
x=(window_width/2)-(width/2)
y=(window_height/2)-(height/2)
root.geometry("%dx%d+%d+%d" % (width,height,x,y))
root.resizable(0,0)
root.config(bg="#171a19")

#setting images
Blank_img = PhotoImage(file="Resources/blank.png")
Player_Rock=PhotoImage(file="Resources/rock_player.png")
Player_Rock_ado = Player_Rock.subsample(3,3)
Player_Paper=PhotoImage(file="Resources/paper_player.png")
Player_Paper_ado=Player_Paper.subsample(3,3)
Player_Scissor=PhotoImage(file="Resources/scissor_player.png")
Player_Scissor_ado=Player_Scissor.subsample(3,3)
Computer_Rock=PhotoImage(file="Resources/rock_computer.png")
Computer_Paper=PhotoImage(file="Resources/paper_computer.png")
Computer_Scissor=PhotoImage(file="Resources/scissor_computer.png")

#function for making rock paper scissor
def Rock():
    global player_option
    player_option=1
    Image_Player.configure(image=Player_Rock)
    Matching()

def Paper():
    global player_option
    player_option=2
    Image_Player.configure(image=Player_Paper)
    Matching()

def Scissor():
    global player_option
    player_option=3
    Image_Player.configure(image=Player_Scissor)
    Matching()

#Function for making computer rock paper

def Comp_Rock():
    if player_option==1:
        Label_Status.config(text="Game Toe")
    elif player_option == 2:
        Label_Status.config(text="Player Win")
    elif player_option==3:
        Label_Status.config(text="Computer Win")

def Comp_Paper():
    if player_option==1:
        Label_Status.config(text="Computer Win")
    elif player_option==2:
        Label_Status.config(text="Computer Tie")
    elif player_option==3:
        Label_Status.config(text="Player Win")

def Comp_Scissor():
    if player_option==1:
        Label_Status.config(text="Player Win")
    elif player_option==2:
        Label_Status.config(text="Computer Win")
    elif player_option==3:
        Label_Status.config(text="Game Tie")

#function for matching
def Matching():
    computer_option = random.randint(1,3)
    if computer_option==1:
        Image_Computer.configure(image=Computer_Rock)
        Comp_Rock()
    elif computer_option==2:
        Image_Computer.configure(image=Computer_Paper)
        Comp_Paper()
    elif computer_option==3:
        Image_Computer.configure(image=Computer_Scissor)
        Comp_Scissor()

#exit function
def Exit():
    root.destroy()
    exit()

#Define buttons and labels widget

Image_Player=Label(root, image=Blank_img)
Image_Computer=Label(root, image=Blank_img)
Label_Player=Label(root, text="PLAYER")
Label_Player.grid(row=1,column=3)
Label_Player.config(bg="#e8c1c7",fg="black",font=('Times New Roman', 18, 'bold'))
Label_Computer=Label(root, text="COMPUTER")
Label_Computer.grid(row=1,column=3)
Label_Computer.config(bg="#e8c1c7",fg="black",font=('Times New Roman', 18, 'bold'))
Label_Status=Label(root,text="",font=('Times New Roman',12))
Label_Status.config(fg="black", font=('Times New Roman', 20, 'bold', 'italic'))
Image_Player.grid(row=2, column=1, padx=30, pady=20)
Image_Computer.grid(row=2, column=3, pady=20)
Label_Status.grid(row=3, column=2)

rock=Button(root, image=Player_Rock_ado, command=Rock)
paper=Button(root, image=Player_Paper_ado, command=Paper)
scissor=Button(root, image=Player_Scissor_ado, command=Scissor)
button_quit= Button(root,text="Quit",bg="red",fg="white", font=('Times New Roman', 25, 'bold'),command=Exit)
rock.grid(row=4, column=1, pady=30)
paper.grid(row=4, column=2,pady=30)
scissor.grid(row=4,column=3,pady=30)
button_quit.grid(row=5,column=2)

if __name__ == '__main__':
    root.mainloop()



 

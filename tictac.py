#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 11:52:21 2018

@author: deepthisen
"""

import numpy as np
from tkinter import *

def checkTicTac(board,player_code):
    row_check=np.prod(board,axis=1)
    col_check=np.prod(board,axis=0)
    diag1_check=np.prod(np.diag(board))
    diag2_check=np.prod(np.diag(np.flip(board,axis=1)))
    if player_code==1:
        a=np.sum(np.isin(row_check,1))
        b=np.sum(np.isin(col_check,1))
        c=np.sum(np.isin(diag1_check,1))
        d=np.sum(np.isin(diag2_check,1))
    elif player_code==2:
        a=np.sum(np.isin(row_check,8))
        b=np.sum(np.isin(col_check,8))
        c=np.sum(np.isin(diag1_check,8))
        d=np.sum(np.isin(diag2_check,8))
    verdict=a+b+c+d
    return verdict

def disable_allButtons(window):
    for w in window.winfo_children():
        w.configure(state=DISABLED)

global n_click, board
n_click=1
board=np.zeros([3,3])

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200') # 350 pixels and the height to 200 pixels.
lbl = Label(window, text="Hello",font=("Arial Bold", 10))
lbl.grid(column=4, row=4)
# Adding Buttons and specifying events
def clicked(btn,row,col):
    global n_click, board
    if np.mod(n_click,2)==1:
        symb='X'
        board[row,col]=1
        verdict=checkTicTac(board,1)
        lbl.configure(text="Player 1")
        if verdict>0:
            lbl.configure(text="Player 1 wins")
            disable_allButtons(window)

       #     break
    else:
        symb='O' 
        board[row,col]=2
        verdict=checkTicTac(board,2)
        lbl.configure(text="Player 2")
        if verdict>0:
            lbl.configure(text="Player 2 wins")
            disable_allButtons(window)
    #        break

    n_click=n_click+1
    btn.configure(text=str(symb),state=DISABLED)
    
    
btn1 = Button(window, text="-", bg="cyan", fg="red",command= lambda: clicked(btn1,0,0))
btn1.grid(column=0, row=0)
btn2 = Button(window, text="-", bg="cyan", fg="red",command= lambda: clicked(btn2,1,0))
btn2.grid(column=1, row=0)
btn3 = Button(window, text="-", bg="cyan", fg="red",command= lambda: clicked(btn3,2,0))
btn3.grid(column=2, row=0)
btn4 = Button(window, text="-", bg="cyan", fg="red",command= lambda: clicked(btn4,0,1))
btn4.grid(column=0, row=1)
btn5 = Button(window, text="-", bg="cyan", fg="red",command= lambda: clicked(btn5,1,1))
btn5.grid(column=1, row=1)
btn6 = Button(window, text="-", bg="cyan", fg="red",command= lambda: clicked(btn6,2,1))
btn6.grid(column=2, row=1)
btn7 = Button(window, text="-", bg="cyan", fg="red",command= lambda: clicked(btn7,0,2))
btn7.grid(column=0, row=2)
btn8 = Button(window, text="-", bg="cyan", fg="red",command= lambda: clicked(btn8,1,2))
btn8.grid(column=1, row=2)
btn9 = Button(window, text="-", bg="cyan", fg="red",command= lambda: clicked(btn9,2,2))
btn9.grid(column=2, row=2)
### Entering text
#txt = Entry(window,width=10)
#txt.grid(column=1, row=0)
window.mainloop()




#def printTicTac(board):
#    for i in range(len(board)):
#        print('|',end="")
#        for j in range(len(board[i])):
#         if board[i,j]==0:
#          print("  ",end ="|")
#         elif board[i,j]==1:
#          print("X ",end ="|")
#         elif board[i,j]==2:
#          print("O ",end ="|")
#        print()
#        print('----------')


#board=np.zeros([3,3])
#
#n_step=1
#error_code=0;
#
#while n_step>0:
#    row,col    = input("Enter location x\n"), input("Enter location y\n")
#    row=int(row)-1
#    col=int(col)-1
#    
#    if (row>2)|(col>2)|(row<0)|(col<0):
#
#        print('Invalid location')
#        continue
#    elif board[row,col]!=0:
#        print('Location already filled')
#        continue
#        
#        
#    if np.mod(n_step,2)==1:
#        curPlay=1
#        board[row,col]=1
#        print(board)
#        printTicTac(board)
#        verdict=checkTicTac(board,1)
#    else:
#        curPlay=2
#        board[row,col]=2
#        printTicTac(board)
#        verdict=checkTicTac(board,2)
#        
#    if verdict>0:
#        print('Player '+str(curPlay)+' wins')
#        n_step=-1
#    else: 
#        n_step=n_step+1
#    
#    if np.prod(board)!=0:
#        break
    
        

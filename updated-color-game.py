import tkinter as tk
from tkinter import ttk, messagebox
import random, time

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','Purple','Brown']
score,total_try = 0,0
# the game time left, initially 30 seconds. 
timeleft = 30
  
# function that will start the game. 
def startGame(*args): 
    if timeleft == 30: 
        # start the countdown timer. 
        countdown()     
        start_button.config(state= tk.DISABLED)
    # run the function to 
    # choose the next colour. 
    nextColour() 
  
# Function to choose and 
# display the next colour. 
def nextColour(): 
    # use the globally declared 'score' 
    # and 'play' variables above. 
    global score , total_try
    global timeleft 
    # if a game is currently in play 
    if timeleft > 0: 
  
        # make the text entry box active. 
        input_entry.focus_set() 
        # if the colour typed is equal 
        # to the colour of the text 
        total_try+=1
        if input_entry.get().lower() == colours[1].lower(): 
            score += 1
  
        # clear the text entry box. 
        input_entry.delete(0, tk.END)
        random.shuffle(colours) 
          
        # change the colour to type, by changing the 
        # text _and_ the colour to a random colour value 
        color_label.config(fg = str(colours[1]), text = str(colours[0])) 
    else:
        # display score......    
        messagebox.showinfo('Time END',f'Total Try : {total_try} \n The Total Score is : {score} \n Total wrong answers {total_try-score}')
        start_button.config(state=tk.ACTIVE)
  
  
# Countdown timer function  
def countdown():
    global timeleft 
    # if a game is in play 
    if timeleft > 0: 
        # decrement the timer. 
        timeleft -= 1
        # update the time left label 
        time_label.config(text = "Time Left : "
                               + str(timeleft)) 
                                 
        # run the function again after 1 second. 
        time_label.after(1000, countdown)

root = tk.Tk()
root.title("Color Game")
root.geometry("300x400")
root.config(bg='white')

title_label = tk.Label(root,text="Python Color Game",font=('Comic Sans',18,'bold'),fg='royal blue',bg='white')
title_label.place(x=40,y=15)

frame = tk.Frame(root,bd=2,relief=tk.SUNKEN,height=350,width=890,bg='white')
frame.place(x=5,y=60,height=320,width=290)

color_label = tk.Label(frame,text='',font=('Helvetica', 30,'bold'),bg='white')
color_label.pack(fill=tk.X,pady=20)

time_label = tk.Label(frame,text="    ",width=20,font = ('Helvetica', 12),bg='white',bd=4,
relief=tk.GROOVE)
time_label.pack(pady=20,ipady=5,ipadx=5)

input_entry = ttk.Entry(frame,width=20,justify=tk.CENTER,font=("Sitka Small",12))
input_entry.pack(pady=20)
input_entry.focus_set() 
root.bind('<Return>',startGame)

start_button = tk.Button(frame,text='Start',fg='royal blue',font= ('Arial', 13,'bold'),width=10,command=startGame)
start_button.pack(pady=20,ipadx=5,ipady=5)


root.mainloop()

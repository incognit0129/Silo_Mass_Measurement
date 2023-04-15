import tkinter as tk
import random
import Silo_gui as s
import math
import customtkinter as ctk
from tkinter import ttk
import table as table_gui

s1 = s.r1
s2 = s.r2
s3 = s.r3

# Create the window
window = ctk.CTk()
window._set_appearance_mode('dark')


window.title("SILOS")
window.geometry("1000x1000")


#create Table
canvas1 = table_gui.Table(window)

#Create the progress bars
progress_bar1 = tk.Canvas(window, width=100, height=300, bg="white")
progress_bar1.grid(row=1, column=0, padx=100, pady=100)

progress_bar2 = tk.Canvas(window, width=100, height=300, bg="white")
progress_bar2.grid(row=1, column=1, padx=100, pady=100)

progress_bar3 = tk.Canvas(window, width=100, height=300, bg="white")
progress_bar3.grid(row=1, column=2, padx=100, pady=100)

# Create the labels
label1 = tk.Label(window, text="Silo 1", font=('raleway',20, 'bold'), relief='raised')
label1.grid(row=0, column=0 ,padx=3, pady=25)

label2 = tk.Label(window, text="Silo 2", font=('raleway', 20, 'bold'), relief='raised')
label2.grid(row=0, column=1, padx=3, pady=25)

label3 = tk.Label(window, text="Silo 3", font=('raleway', 20, 'bold'), relief='raised')
label3.grid(row=0, column=2, padx=3, pady=25)




#value  mA labels

silo_1_current = tk.Label(window, text="ma", font=('raleway',20, 'bold'), relief='raised')
silo_1_current.grid(row=2, column=0, padx=25, pady=15)

silo_2_current = tk.Label(window, text="ma", font=('raleway', 20, 'bold'), relief='raised')
silo_2_current.grid(row=2, column=1, padx=25, pady=15)


silo_3_current = tk.Label(window, text="ma", font=('raleway', 20, 'bold'), relief='raised')
silo_3_current.grid(row=2, column=2, padx=25, pady=15)


#value lbs labels

silo_1_lbs = tk.Label(window, text="lbs", font=('raleway',20, 'bold'), relief='raised')
silo_1_lbs.grid(row=4, column=0, padx=25, pady=15)

silo_2_lbs = tk.Label(window, text="lbs", font=('raleway',20, 'bold'), relief='raised')
silo_2_lbs.grid(row=4, column=1, padx=25, pady=15)

silo_3_lbs = tk.Label(window, text="lbs", font=('raleway',20, 'bold'), relief='raised')
silo_3_lbs.grid(row=4, column=2, padx=25, pady=15)

#ft labels
silo_1_ft = tk.Label(window, text="ft", font=('raleway',20, 'bold'), relief='raised')
silo_1_ft.grid(row=5, column=0, padx=25, pady=15)

silo_2_ft = tk.Label(window, text="ft", font=('raleway',20, 'bold'), relief='raised')
silo_2_ft.grid(row=5, column=1, padx=25, pady=15)


silo_3_ft = tk.Label(window, text="ft", font=('raleway',20, 'bold'), relief='raised')
silo_3_ft.grid(row=5, column=2, padx=25, pady=15)

# Update the progress bars with a random value every second
def update_progress_bars():
    
    #color warnings
    def change_color1(value):    
        if value1 <= 66:
             progress_bar1.create_rectangle(0, 300-value1*3, 100, 300, fill="yellow")
        
    def change_color2(value):    
        if value2 <= 66:
             progress_bar2.create_rectangle(0, 300-value2*3, 100, 300, fill="yellow")
        
    def change_color3(value):    
        if value3 <= 66:
             progress_bar3.create_rectangle(0, 300-value3*3, 100, 300, fill="yellow")
        
    
    # Generate random values
    value1 = round(((s.r1.get_currentValue()-4)/16)*100, 2)
    value2 = round(((s.r2.get_currentValue()-4)/16)*100, 2)
    value3 = round(((s.r3.get_currentValue()-4)/16)*100, 2)
    
    #Update progress bars
    progress_bar1.delete("all")
    progress_bar1.create_rectangle(0, 300-value1*3, 100, 300, fill="green")
    silo_1_current.config(text=f"{value1} %")
    
    progress_bar2.delete("all")
    progress_bar2.create_rectangle(0, 300-value2*3, 100, 300, fill="green")
    silo_2_current.config(text=f"{value2} %")
    
    progress_bar3.delete("all")
    progress_bar3.create_rectangle(0, 300-value3*3, 100, 300, fill="green")
    silo_3_current.config(text=f"{value3} %")
    
    
    #update labels silo 1 
    silo_1_lbs.config(text =f"{round(((s1.get_currentValue()-4)/16)*84000, 2)} lbs")
    silo_1_ft.config(text =f"{round((((s1.get_currentValue()-4)/(-16))*24)+24, 2)} ft")
    
        #update labels silo 2 
    silo_2_lbs.config(text =f"{round(((s2.get_currentValue()-4)/16)*91747, 2)} lbs")
    silo_2_ft.config(text =f"{round((((s2.get_currentValue()-4)/(-16))*24)+24, 2)} ft")
    
    
    #update labels silo 3 
    silo_3_lbs.config(text =f"{round(((s3.get_currentValue()-4)/16)*99999, 2)} lbs")
    silo_3_ft.config(text =f"{round((((s3.get_currentValue()-4)/(16))*24), 2)}ft")
    
    #conditions
    change_color1(value1)
    change_color2(value2)
    change_color3(value3)
    # if ((((s3.get_currentValue()-4)/(-16))*24)+24 <= 17):
    #         progress_bar1.configure(bg='red')
        
    # Schedule the next update
    window.after(5000, update_progress_bars)

# Start the update loop
update_progress_bars()

# Start the event loop
window.mainloop()

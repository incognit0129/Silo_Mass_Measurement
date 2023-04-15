import tkinter as tk
import random
import Silo_gui as s
import math

s1 = s.r3

# Create the window
window = tk.Tk()
window.title("Progress Bars")
window.geometry("1000x1000")

#Create the progress bars
progress_bar1 = tk.Canvas(window, width=100, height=300, bg="white")
progress_bar1.grid(row=1, column=0, padx=100, pady=100)

progress_bar2 = tk.Canvas(window, width=50, height=300, bg="white")
progress_bar2.grid(row=1, column=1, padx=100, pady=100)

progress_bar3 = tk.Canvas(window, width=50, height=300, bg="white")
progress_bar3.grid(row=1, column=2, padx=100, pady=100)

# Create the labels
label1 = tk.Label(window, text="Silo 1", font=('raleway',20, 'bold'), relief='raised')
label1.grid(row=0, column=0)

label2 = tk.Label(window, text="Silo 2", font=('raleway', 20, 'bold'), relief='raised')
label2.grid(row=0, column=1)

label3 = tk.Label(window, text="Silo 3", font=('raleway', 20, 'bold'), relief='raised')
label3.grid(row=0, column=2)
#value  mA labels

label4 = tk.Label(window, text="ma", font=('raleway',20, 'bold'), relief='raised')
label4.grid(row=2, column=0, padx=25, pady=15)

label5 = tk.Label(window, text="ma", font=('raleway', 20, 'bold'), relief='raised')
label5.grid(row=2, column=1, padx=25, pady=15)


label6 = tk.Label(window, text="ma", font=('raleway', 20, 'bold'), relief='raised')
label6.grid(row=2, column=2, padx=25, pady=15)


#value lbs labels

label7 = tk.Label(window, text="lbs", font=('raleway',20, 'bold'), relief='raised')
label7.grid(row=4, column=0, padx=25, pady=15)
label8 = tk.Label(window, text="lbs", font=('raleway',20, 'bold'), relief='raised')
label8.grid(row=4, column=1, padx=25, pady=15)
label9 = tk.Label(window, text="lbs", font=('raleway',20, 'bold'), relief='raised')
label9.grid(row=4, column=2, padx=25, pady=15)

#ft labels
label10 = tk.Label(window, text="ft", font=('raleway',20, 'bold'), relief='raised')
label10.grid(row=5, column=0, padx=25, pady=15)
label11 = tk.Label(window, text="ft", font=('raleway',20, 'bold'), relief='raised')
label11.grid(row=5, column=1, padx=25, pady=15)
label12 = tk.Label(window, text="ft", font=('raleway',20, 'bold'), relief='raised')
label12.grid(row=5, column=2, padx=25, pady=15)

# Update the progress bars with a random value every second
def update_progress_bars():
    # Generate random values
    value1 = round(((s1.get_currentValue()-4)/16)*100, 2)
    value2 = 50
    value3 = 100
    
    #Update progress bars
    progress_bar1.delete("all")
    progress_bar1.create_rectangle(0, 300-value1*3, 100, 300, fill="green")
    label4.config(text=f"{value1} mA")
    
    progress_bar2.delete("all")
    progress_bar2.create_rectangle(0, 300-value2*3, 100, 300, fill="green")
    label5.config(text=value2)
    
    progress_bar3.delete("all")
    progress_bar3.create_rectangle(0, 300-value3*3, 100, 300, fill="green")
    label6.config(text=value3)
    
    #update labels 
    label7.config(text =f"{round(((s1.get_currentValue()-4)/16)*84000, 2)} lbs")
    label10.config(text =f"{round(((s1.get_currentValue()-4)/16)*24, 2)} ft")
    
    # Schedule the next update
    window.after(1000, update_progress_bars)

# Start the update loop
update_progress_bars()

# Start the event loop
window.mainloop()

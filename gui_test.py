# Python program to create a basic GUI
# application using the customtkinter module

import customtkinter as ctk

import silos
import math
import datetime


window = ctk.CTk()

#window title
window.title('Root 1')
#window size
window.geometry("800x800")
# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("dark")

# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")




   
   
   
#get current value and change to perncentage
silo1 = silos.r1.get_currentValue()
silo2 = silos.r2.get_currentValue()
silo3 = silos.r3.get_currentValue()
#silo4 = silos.r4.get_currentValue()
   
#change current values to percentages
current_weight1 = math.floor(((silo1-4)/16)*84000)
current_weight2 = math.floor(((silos.r1.get_currentValue()-4)/16)*91747)
current_weight3 = math.floor(((silo3-4)/16)*99999)
# current_percent4 = math.floor(((silo4-4)/16)*84000)





# App Class

		#date label
date_label = ctk.CTkLabel(window,font=('Roboto',40,'bold'))
date_label.grid(row=0, column=3,
							padx=10, pady=100,
							)


		# Name Label
silo1_label= ctk.CTkLabel(window,	text="Silo 1",font=('Roboto',40,'bold'))
silo1_label.grid(row=1, column=0,padx=10, pady=00,
							)

	
silo1_weight = ctk.CTkLabel(window,font=( 'Crinsom',50,'bold', ),text_color='yellow')
silo1_weight.grid(row=1, column=3,padx=50, pady=50)
  
  
						
current_label_silo1= ctk.CTkLabel(window,	text=str(silo1)+" ma",font=( 'Crinsom',50,'bold', ),text_color='yellow')
current_label_silo1.grid(row=1, column=4,padx=50, pady=50)
  
  
  
  #-------------------------------------------------
  #silo 2
  
silo2_label = ctk.CTkLabel(window,text="Silo 2",font=('Roboto',40,'bold'))
silo2_label.grid(row=2, column=0,
							padx=10, pady=00,
							)

	
silo2_weight = ctk.CTkLabel(window, text="000000 lbs",font=( 'Crinsom',50,'bold', ),text_color='yellow')
silo2_weight.grid(row=2, column=3,
						padx=50, pady=50)
  
  
						
current_label_silo2 = ctk.CTkLabel(window,text="000000 ft",font=( 'Crinsom',50,'bold', ),text_color='yellow')
current_label_silo2.grid(row=2, column=4,
						padx=50, pady=50)


#--------------------------------------------------------------

		#Silo 3
  
silo3_label = ctk.CTkLabel(window,text="Silo 3",font=('Roboto',40,'bold'))
silo3_label.grid(row=3, column=0,
							padx=10, pady=00,
							)

	
silo3_weight = ctk.CTkLabel(window, text="000000 lbs",font=( 'Crinsom',50,'bold', ),text_color='yellow')
silo3_weight.grid(row=3, column=3,
						padx=50, pady=50)
  
  
						
current_label_silo3 = ctk.CTkLabel(window,text="000000 ft",font=( 'Crinsom',50,'bold', ),text_color='yellow')
current_label_silo3.grid(row=3, column=4,
						padx=50, pady=50)

# 		#date label
# date_label = ctk.CTkLabel(window,font=('Roboto',40,'bold'))
# date_label.grid(row=3, column=0,
# 							padx=10, pady=00,
# 							)
		
#update values gui
def update_clock():
    # get current time as text
    current_weight1 = math.floor(((silos.r1.get_currentValue()-4)/16)*84000)
    current_weight2 = math.floor(((silos.r2.get_currentValue()-4)/16)*91747)
    current_weight3 = math.floor(((silos.r3.get_currentValue()-4)/16)*99999)
    
    #silos Update Current Values	
    silo1 = round(((silos.r1.get_currentValue()-4)/16)*24, 2)
    silo2 =  round(((silos.r2.get_currentValue()-4)/16)*24, 2)
    silo3 =  round(((silos.r3.get_currentValue()-4)/16)*24, 2)
    
    #silo 1
    current_label_silo1.configure(text= str(silo1) +" ft")
    silo1_weight.configure(text= str(current_weight1) +" lbs" )
    
    #silo 2
    current_label_silo2.configure(text= str(silo2) +" ft")
    silo2_weight.configure(text= str(current_weight2) +" lbs" )
    
	
    #silo 3
    current_label_silo3.configure(text= str(silo3) +" ft")
    silo3_weight.configure(text= str(current_weight3) +" lbs" )
    
 
    date_label.configure(text = datetime.datetime.now().strftime("Time  : %H:%M:%S"))
    window.after(1000, update_clock)
   

	
update_clock()
window.mainloop()	

      
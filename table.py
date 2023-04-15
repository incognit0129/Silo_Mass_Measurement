import tkinter as tk
import random
import math
import Silo_gui as s

# import silos as s

silo1_density = 35.2
silo2_density = 37.75
silo3_density = 55.95



#cone volume  pi r squared 1/3 height
silos_full_cone_volume = 427
silo1_full_cone_mass =silos_full_cone_volume * silo1_density
silo2_full_cone_mass =silos_full_cone_volume * silo2_density
silo3_full_cone_mass =silos_full_cone_volume * silo3_density

class Table:
    def __init__(self, master):
        # Create table frame
        self.frame = tk.Frame(master, width=500, height=500)
        self.frame.grid(column=4, row=1)

        # Create header labels
        row_header = tk.Label(self.frame, text='Calculated Values', font=('Arial', 12, 'bold'), relief='ridge', width=15, height=2)
        row_header.grid(row=0, column=2, pady=20)
        
        # row_header = tk.Label(self.frame, text='Volume', font=('Arial', 10, 'bold'),  width=10, height=2)
        # row_header.grid(row=2, column=0, padx=5)
        col_header = tk.Label(self.frame, text='Silo 1 ', font=('Arial', 10, 'bold'), width=10, height=2)
        col_header.grid(row=1, column=1)
        
        # row_header = tk.Label(self.frame, text='Density', font=('Arial', 10, 'bold'), width=10, height=2)
        # row_header.grid(row=3, column=0)

        col_header = tk.Label(self.frame, text='Silo 2', font=('Arial', 10, 'bold'), width=10, height=2)
        col_header.grid(row=1, column=2)
        
        row_header = tk.Label(self.frame, text='Mass', font=('Arial', 12, 'bold'), width=10, height=2)
        row_header.grid(row=4, column=0)
        col_header = tk.Label(self.frame, text='Silo 3', font=('Arial', 10, 'bold'), width=10, height=2)
        col_header.grid(row=1, column=3)

    #    #silo 1
    #     self.cell_1 = tk.Label(self.frame, text='1', font=('Arial', 9, 'bold'), relief='ridge', width=10, height=2)
    #     self.cell_1.grid(row=2, column=1)

    #     self.cell_2 = tk.Label(self.frame, text='2', font=('Arial', 9, 'bold'), relief='ridge', width=10, height=2)
    #     self.cell_2.grid(row=3, column=1)

        self.cell_3 = tk.Label(self.frame, text='3', font=('Arial', 11, 'bold'), relief='ridge', width=10, height=2)
        self.cell_3.grid(row=4, column=1)

        # Silo 2
        # self.cell_4 = tk.Label(self.frame, text='4', font=('Arial', 9, 'bold'), relief='ridge', width=10, height=2)
        # self.cell_4.grid(row=2, column=2)
        
        # self.cell_5 = tk.Label(self.frame, text='5', font=('Arial', 9, 'bold'), relief='ridge', width=10, height=2)
        # self.cell_5.grid(row=3, column=2)
        
      

        self.cell_6= tk.Label(self.frame, text='6', font=('Arial', 11, 'bold'), relief='ridge', width=10, height=2)
        self.cell_6.grid(row=4, column=2)

    # #silo 3

    #     self.cell_7 = tk.Label(self.frame, text='7', font=('Arial',9, 'bold'), relief='ridge', width=10, height=2)
    #     self.cell_7.grid(row=2, column=3)

    #     self.cell_8 = tk.Label(self.frame, text='8', font=('Arial',9, 'bold'), relief='ridge', width=10, height=2)
    #     self.cell_8.grid(row=3, column=3)

        self.cell_9 = tk.Label(self.frame, text='9', font=('Arial',11, 'bold'), relief='ridge', width=10, height=2)
        self.cell_9.grid(row=4, column=3, padx=10, pady=10)

#calculated values
        # row_header = tk.Label(self.frame, text='Linear Values', font=('Arial', 12, 'bold'), relief='ridge', width=15, height=2)
        # row_header.grid(row=5, column=2, pady=20)

        
        
        # row_header = tk.Label(self.frame, text='Volume', font=('Arial', 10, 'bold'),  width=10, height=2)
        # row_header.grid(row=7, column=0, padx=5)

        # col_header = tk.Label(self.frame, text='Silo 1 ', font=('Arial', 10, 'bold'), width=10, height=2)
        # col_header.grid(row=6, column=1)
        
        # row_header = tk.Label(self.frame, text='Density', font=('Arial', 10, 'bold'), width=10, height=2)
        # row_header.grid(row=8, column=0)

        # col_header = tk.Label(self.frame, text='Silo 2', font=('Arial', 10, 'bold'), width=10, height=2)
        # col_header.grid(row=6, column=2)
        
        # row_header = tk.Label(self.frame, text='Mass', font=('Arial', 10, 'bold'), width=10, height=2)
        # row_header.grid(row=9, column=0)

        # col_header = tk.Label(self.frame, text='Silo 3', font=('Arial', 10, 'bold'), width=10, height=2)
        # col_header.grid(row=6, column=3)
#sil 1

        # self.cell_19 = tk.Label(self.frame, text='1', font=('Arial', 8, 'bold'), relief='ridge', width=10, height=2)
        # self.cell_19.grid(row=7, column=1)

        # self.cell_11 = tk.Label(self.frame, text='2', font=('Arial', 8, 'bold'), relief='ridge', width=10, height=2)
        # self.cell_11.grid(row=8, column=1)

        # self.cell_12 = tk.Label(self.frame, text='3', font=('Arial', 8, 'bold'), relief='ridge', width=10, height=2)
        # self.cell_12.grid(row=9, column=1)

        # # Silo 2
        # self.cell_13 = tk.Label(self.frame, text='4', font=('Arial', 8, 'bold'), relief='ridge', width=10, height=2)
        # self.cell_13.grid(row=7, column=2)

        # self.cell_14 = tk.Label(self.frame, text='5', font=('Arial', 8, 'bold'), relief='ridge', width=10, height=2)
        # self.cell_14.grid(row=8, column=2)

        # self.cell_15 = tk.Label(self.frame, text='6', font=('Arial', 8, 'bold'), relief='ridge', width=10, height=2)
        # self.cell_15.grid(row=9, column=2)

        #    # Silo 3

        # self.cell_16 = tk.Label(self.frame, text='7', font=('Arial', 8, 'bold'), relief='ridge', width=10, height=2)
        # self.cell_16.grid(row=7, column=3)

        # self.cell_17 = tk.Label(self.frame, text='8', font=('Arial', 8, 'bold'), relief='ridge', width=10, height=2)
        # self.cell_17.grid(row=8, column=3)

        # self.cell_18 = tk.Label(self.frame, text='9', font=('Arial', 8, 'bold'), relief='ridge', width=10, height=2)
        # self.cell_18.grid(row=9, column=3)

        # Start updating table value every 5 seconds
        self.update_table()

    def update_table(self):
        silo1_height = round((((s.r1.get_currentValue()-4)/(16))*22)-7.33, 2)
        silo2_height = round((((s.r2.get_currentValue()-4)/(16))*22)-7.33, 2)
        silo3_height = round((((s.r3.get_currentValue()-4)/(16))*22)-7.33, 2)
        
        #cylinder volume
        silo1_cylinder_volume = round(math.pi*56.25*silo1_height, 2)
        silo2_cylinder_volume = round(math.pi*56.25*silo2_height, 2)
        silo3_cylinder_volume = round(math.pi*56.25*silo3_height, 2)
        
        #cylinder mass
        silo1_cylinder_mass = round(silo1_cylinder_volume * silo1_density, 2)
        silo2_cylinder_mass = round(silo2_cylinder_volume * silo2_density, 2)
        silo3_cylinder_mass = round(silo3_cylinder_volume * silo3_density, 2)
        
        
        # silo 1 labels
        # self.cell_1['text'] = round(silo1_cylinder_volume + silos_full_cone_volume,2)
        # self.cell_2['text'] = silo1_density
        self.cell_3['text'] = round(silo1_cylinder_mass + silo1_full_cone_mass, 2)
    #silon 2
        # self.cell_4['text'] = round(silo2_cylinder_volume + silos_full_cone_volume,2)
        # self.cell_5['text'] = silo2_density
        self.cell_6['text'] = round(silo2_cylinder_mass + silo2_full_cone_mass, 2)
    #silo 3
        # self.cell_7['text'] = round(silo3_cylinder_volume + silos_full_cone_volume,2)
        # self.cell_8['text'] = silo3_density
        self.cell_9['text'] = round(silo3_cylinder_mass + silo3_full_cone_mass, 2)

    # # linear calculations
    #     self.cell_19['text'] = silo3_height
    #     self.cell_11['text'] = silo1_density
    #     self.cell_12['text'] = str(random.randint(0,9))

    #     self.cell_13['text'] = str(random.randint(0,9))
    #     self.cell_14['text'] = silo2_density
    #     self.cell_15['text'] = str(random.randint(0,9))

    #     self.cell_16['text'] = str(random.randint(0,9))
    #     self.cell_17['text'] = silo3_density
    #     self.cell_18['text'] = str(random.randint(0,9))

        # Schedule next update in 5 seconds
        self.frame.after(5000, self.update_table)

# root = tk.Tk()
# table1 = Table(root)
# # table2 = Table(root)
# root.mainloop()

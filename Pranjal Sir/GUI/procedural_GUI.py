import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import numpy as np



root = tk.Tk() 

root.config(bg="#38e9da")                                              
root.title("GUI to Plot Magnetic Data")   
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

text_box = tk.Text(root, height=50, width=50)
text_box.config(bg="#68743F", fg="#1303F0", font=("Arial", 10, "italic",'bold'))
text_box.grid(row=1,column=1, padx=0, pady=0,sticky='nsew')

def open_file():
    global df, dir,text_box 

    text_box.destroy()  # Destroy the text box to make space for the plot

    text_box = tk.Text(root, height=50, width=50)
    text_box.config(bg="#68743F", fg="#1303F0", font=("Arial", 10, "italic",'bold'))
    text_box.grid(row=1,column=1, padx=0, pady=0,sticky='nsew')

    dir = filedialog.askopenfile() 
    df = pd.read_csv(dir, skiprows=21,header=None,sep =r'\s+')

    df.columns =['DATE','TIME','JULIAN_DAY','H','D','Z','F']

    df['DATETIME'] = df['DATE'] + ':' + df['TIME']
    df = df[['DATETIME','JULIAN_DAY', 'H','D','Z','F']]

    text_box.delete(1.0, tk.END)  # Clear the text box before inserting new content
    text_box.insert(tk.END, df.to_string())  # Insert the DataFrame content


button1 = tk.Button(root,text = 'Open a File',command = open_file)  
button1.config(bg="#000000", fg="#FF0000", font=("Arial", 20, "italic",'bold'))                         
button1.grid(row=0,column=0,padx=0, pady=0,sticky='ns')

scrol_bar1 = tk.Scrollbar(root,orient = tk.VERTICAL, command=text_box.yview)
scrol_bar1.grid(row=1, column=2, sticky='ns')
text_box.config(yscrollcommand=scrol_bar1.set)

scrol_bar2 = tk.Scrollbar(root,orient=tk.HORIZONTAL, command=text_box.xview)
scrol_bar2.grid(row=2, column=1, sticky='we',padx=0, pady=0)

def show_plot():
    text_box.delete(1.0, tk.END)  # Clear the text box before inserting new content
    text_box.destroy()  # Destroy the text box to make space for the plot
    df['DATETIME'] = pd.to_datetime(df['DATETIME'],format= '%Y-%m-%d:%H:%M:%S.%f')


    fig,ax = plt.subplots(4,1,layout='constrained')

    plt.suptitle('Geomagnetic Data for One Day',size= 20)

    fig,ax = plt.subplots(4,1,layout='constrained')

    plt.suptitle('Geomagnetic Data for One Day',size= 20)

    ax[0].plot(df['DATETIME'],df['H'],label= 'H')
    my_fmt = mdates.DateFormatter('%H')
    ax[0].xaxis.set_major_formatter(my_fmt)
    ax[0].set_xlim(np.min(df['DATETIME']), np.max(df['DATETIME']))
    ax[0].legend(loc= 'best')
    ax[0].set_ylabel('H(nT)',size= 10)

    ax[1].plot(df['DATETIME'],df['D'],c='green',label= 'D')
    my_fmt = mdates.DateFormatter('%H')
    ax[1].xaxis.set_major_formatter(my_fmt)
    ax[1].set_xlim(np.min(df['DATETIME']), np.max(df['DATETIME']))
    # ax[1].set_xlabel('UT Time (in Hrs)')
    ax[1].set_ylabel('D(nT)',size= 10)
    ax[1].legend(loc= 'best')

    ax[2].plot(df['DATETIME'],df['Z'],c='red',label= 'Z')
    my_fmt = mdates.DateFormatter('%H')
    ax[2].xaxis.set_major_formatter(my_fmt)
    ax[2].set_xlim(np.min(df['DATETIME']), np.max(df['DATETIME']))
    # ax[2].set_xlabel('UT Time (in Hrs)')
    ax[2].set_ylabel('Z(nT)',size= 10)
    ax[2].legend(loc= 'best')

    ax[3].plot(df['DATETIME'],df['F'],c='orange',label= 'F')
    my_fmt = mdates.DateFormatter('%H')
    ax[3].xaxis.set_major_formatter(my_fmt)
    ax[3].set_xlim(np.min(df['DATETIME']), np.max(df['DATETIME']))
    ax[3].set_xlabel('UT Time (in Hrs)',size= 10)
    ax[3].set_ylabel('F(nT)',size= 10)
    ax[3].legend(loc= 'best')

    canvas = FigureCanvasTkAgg(fig, master = root)  
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=1, padx=0, pady=0, sticky='nsew')


button2 = tk.Button(root,text = 'Show_Plot',command = show_plot)  
button2.config(bg="#000000", fg="#FF0000", font=("Arial", 20, "italic",'bold'))                         
button2.grid(row=0,column=1,padx=0, pady=0,sticky='w') 

root.geometry("900x900")
root.mainloop()                             



 

                                                                                         


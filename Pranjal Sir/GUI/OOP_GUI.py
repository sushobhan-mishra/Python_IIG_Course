from cProfile import label
import os
import tkinter as tk
from tkinter import filedialog

# This is a simple GUI application using tkinter. It creates a main window with two frames, each containing a button. The first button is labeled "Subtraction" and the second button is labeled "Addition". The main window is set to be maximized when the application runs.
class my_first_gui(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.grid(row=0,column=0,sticky='nsew')
        self.config(bg= "#0ee7f7")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # frames in the main window
        self.frame1 = tk.Frame(self,bg="#ffffff")
        self.frame1.grid(row=0,column=0,sticky='nsew')
        self.frame2 = tk.Frame(self,bg="#0ee7f7")
        self.frame2.grid(row=0,column=1,sticky='nsew')

        self.frame1.grid_rowconfigure(2, weight=1)
        self.frame1.grid_columnconfigure(0, weight=1)
        self.frame2.grid_columnconfigure(1, weight=1)

        # buttons in frame1 and frame2
        button1 = tk.Button(self.frame1,text='Select a file',command = self.select_folder)
        button1.grid(row=0,column=0,padx=10,pady=10)

        # label to display selected file info
        self.file_label = tk.Label(self.frame1, text='FILE', bg='#ffffff', fg='black', font=('Arial', 10), wraplength=200, justify=tk.LEFT)
        self.file_label.grid(row=1,column=0,padx=10,pady=10)

        # text widget to display file contents
        self.text_widget = tk.Text(self.frame1, bg='#ffffff', fg='black', font=('Arial', 10), wrap=tk.NONE)
        self.text_widget.grid(row=2,column=0,padx=10,pady=10,sticky='nsew')

        # vertical scrollbar for the text widget
        self.text_scrollbar = tk.Scrollbar(self.frame1, orient=tk.VERTICAL, command=self.text_widget.yview)
        self.text_widget.configure(yscrollcommand=self.text_scrollbar.set)
        self.text_scrollbar.grid(row=2,column=1,sticky='ns',padx=(0,10),pady=10)

        # horizontal scrollbar for the text widget
        self.text_xscrollbar = tk.Scrollbar(self.frame1, orient=tk.HORIZONTAL, command=self.text_widget.xview)
        self.text_widget.configure(xscrollcommand=self.text_xscrollbar.set)
        self.text_xscrollbar.grid(row=3,column=0,columnspan=2,sticky='ew',padx=10,pady=(0,10))

        button2 = tk.Button(self.frame2,text='Addition')
        button2.grid(row=0,column=0,padx=10,pady=10)

    def select_folder(self):
        self.tot_path = filedialog.askopenfilename()
        self.current_folder = os.path.dirname(self.tot_path)
        if self.tot_path:
            try:
                with open(self.tot_path, 'r') as file:
                    file_contents = file.read()
                self.text_widget.config(state='normal')
                self.text_widget.delete('1.0', tk.END)
                self.text_widget.insert('1.0', file_contents)
                self.text_widget.config(state='disabled')
            except Exception as e:
                self.text_widget.config(state='normal')
                self.text_widget.delete('1.0', tk.END)
                self.text_widget.insert('1.0', f"Error reading file: {str(e)}")
                self.text_widget.config(state='disabled')
        text = f"Selected file: {self.tot_path}\nCurrent folder: {self.current_folder}"
        print(text)
        if self.current_folder:
            self.update_folder_types()
            self.update_file_list()
    
        # Update the label to display file info
        self.file_label.config(text=text) 

                     
if __name__ == '__main__':                        # now this source code cannot be used as library
    root = tk.Tk()
    root.title('My First GUI')
    root.state('zoomed')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    app = my_first_gui(root)
    app.mainloop()



# Reviewing the current GUI.py file content before explaining it line by line.

# Line-by-line explanation of GUI.py
# from cProfile import label

# Imports label from the cProfile module.
# In this script, it is not used and can be removed.
# import os

# Imports the standard os module for filesystem path operations.
# import tkinter as tk

# Imports the Tkinter GUI library and gives it the shorthand name tk.
# from tkinter import filedialog

# Imports the filedialog module from Tkinter so the app can open file dialogs.
# # This is a simple GUI application using tkinter...

# A comment describing the purpose of the code.
# class my_first_gui(tk.Frame):

# Defines a new class named my_first_gui that inherits from tk.Frame.
# This class represents the main GUI content inside the Tkinter window.
#  def __init__(self,parent):

# Begins the constructor method for the GUI class.
# parent is the root window that will contain this frame.
#  super().__init__(parent)

# Calls the parent class constructor to initialize the frame.
#  self.grid(row=0,column=0,sticky='nsew')

# Places this frame into the parent window using grid layout at row 0, column 0.
# sticky='nsew' makes it expand in all directions.
#  self.config(bg= "#0ee7f7")

# Sets the background color of the main frame.
#  self.grid_rowconfigure(0, weight=1)

#  self.grid_rowconfigure(0, weight=1)

# Configures row 0 of this frame to expand when the window resizes.
# The second line is redundant because it repeats the same row configuration.
#  self.grid_columnconfigure(0, weight=1)

#  self.grid_columnconfigure(1, weight=1)

# Configures columns 0 and 1 to share available horizontal space.
#  self.frame1 = tk.Frame(self,bg="#ffffff")

# Creates a subframe (frame1) inside the main frame with a white background.
#  self.frame1.grid(row=0,column=0,sticky='nsew')

# Places frame1 into column 0 of the main frame and allows it to expand.
#  self.frame2 = tk.Frame(self,bg="#0ee7f7")

# Creates a second subframe (frame2) with a light blue background.
#  self.frame2.grid(row=0,column=1,sticky='nsew')

# Places frame2 into column 1 of the main frame.
#  self.frame1.grid_rowconfigure(2, weight=1)

# Makes row 2 inside frame1 expand vertically.
#  self.frame1.grid_columnconfigure(0, weight=1)

# Makes column 0 inside frame1 expand horizontally.
#  self.frame1.grid_columnconfigure(1, weight=0)

# Keeps column 1 inside frame1 fixed in size.
#  button1 = tk.Button(self.frame1,text='Select a file',command = self.select_folder)

# Creates a button labeled “Select a file”.
# When clicked, it calls the select_folder method.
#  button1.grid(row=0,column=0,padx=10,pady=10)

# Places the button in frame1 at row 0, column 0 with padding.
#  self.file_label = tk.Label(self.frame1, text='FILE', bg='#ffffff', fg='black', font=('Arial', 10), wraplength=200, justify=tk.LEFT)

# Creates a label to show selected file information.
# It uses Arial font, wraps text at 200 pixels, and left-aligns content.
#  self.file_label.grid(row=1,column=0,padx=10,pady=10)

# Places the label in frame1 below the button.
#  self.text_widget = tk.Text(self.frame1, bg='#ffffff', fg='black', font=('Arial', 10), wrap=tk.WORD)

# Creates a multiline text widget inside frame1.
# wrap=tk.WORD makes text wrap at word boundaries.
#  self.text_widget.grid(row=2,column=0,padx=10,pady=10,sticky='nsew')

# Places the text widget in frame1 at row 2 and allows it to expand.
#  self.text_scrollbar = tk.Scrollbar(self.frame1, orient=tk.VERTICAL, command=self.text_widget.yview)

# Adds a vertical scrollbar widget inside frame1.
# It is linked to the text widget’s vertical view.
#  self.text_widget.configure(yscrollcommand=self.text_scrollbar.set)

# Connects the text widget back to the scrollbar so the scrollbar updates when text scrolls.
#  self.text_scrollbar.grid(row=2,column=1,sticky='ns',padx=(0,10),pady=10)

# Places the scrollbar next to the text widget and stretches it vertically.
#  button2 = tk.Button(self.frame2,text='Addition')

# Creates another button in frame2 labeled “Addition”.
# It has no command assigned yet.
#  button2.grid(row=0,column=0,padx=10,pady=10)

# Places the second button inside frame2.
#  def select_folder(self):

# Defines a method to open a file dialog and load file text.
#  self.tot_path = filedialog.askopenfilename()

# Opens a file selection dialog and stores the selected file path.
#  self.current_folder = os.path.dirname(self.tot_path)

# Extracts the folder path containing the selected file.
#  if self.tot_path:

# Checks whether a file was selected.
#             try:

#  with open(self.tot_path, 'r') as file:

#  file_contents = file.read()

# Attempts to open the selected file and read its contents as text.
#  self.text_widget.config(state='normal')

# Makes the text widget editable temporarily.
#  self.text_widget.delete('1.0', tk.END)

# Clears any existing text from the widget.
#  self.text_widget.insert('1.0', file_contents)

# Inserts the file contents starting at the top of the widget.
#  self.text_widget.config(state='disabled')

# Disables editing again so the user cannot modify the displayed text.
#  except Exception as e:

# Catches any error that happens while reading the file.
#  self.text_widget.config(state='normal')

#  self.text_widget.delete('1.0', tk.END)

#  self.text_widget.insert('1.0', f"Error reading file: {str(e)}")

#  self.text_widget.config(state='disabled')

# Shows an error message in the text widget if file reading fails.
#  if self.current_folder:

#  self.update_folder_types()

#  self.update_file_list()

# Attempts to call two methods for folder handling.
# Note: These methods are not defined in this file, so calling them will raise an error unless defined elsewhere.
#  text = f"Selected file: {self.tot_path}\nCurrent folder: {self.current_folder}"

# Builds a string describing the selected file and folder.
#  print(text)

# Prints that information to the console.
#  self.file_label.config(text=text)

# Updates the label in the GUI to show the selected file path and folder.
# if __name__ == '__main__':

# Checks if this file is being run directly, not imported as a module.
#  root = tk.Tk()

# Creates the main application window.
#  root.title('My First GUI')

# Sets the window title.
#  root.state('zoomed')

# Opens the window maximized.
#  root.grid_rowconfigure(0, weight=1)

#  root.grid_columnconfigure(0, weight=1)

# Allows the main frame to expand with the window.
#  app = my_first_gui(root)

# Creates an instance of the GUI frame inside the root window.
#  app.mainloop()

# Starts the Tkinter event loop so the GUI becomes interactive.
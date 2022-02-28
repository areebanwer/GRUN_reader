"""Code written by Tlanezi Martinez"""

import os
import tkinter as tk  # standard widgets (Label, Button, etc.)
from tkinter import *
from tkinter.messagebox import askokcancel, showinfo  # infoboxes
from tkinter.filedialog import askopenfilename, askdirectory  # select files or folders
from GRUN_reader.points_reader import PointsSet
from GRUN_reader.main import main
import webbrowser
from PIL import Image, ImageTk



class RunoffApp(tk.Frame):
    global img
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title("Runoff App")
        self.master.iconbitmap("graphs/rain.ico")
        ww = 844  # width
        wh = 592  # height


        #screen position
        wx = (self.master.winfo_screenwidth() - ww) / 2
        wy = (self.master.winfo_screenheight() - wh) / 2

        # assign geometry
        self.master.geometry("%dx%d+%d+%d" % (ww, wh, wx, wy))

        self.padx = 5
        self.pady = 5


        ## Wallpaper image
        self.img = ImageTk.PhotoImage(Image.open("rain1.png"))
        self.wallpaper = Label(image = self.img).place(x=0, y=0)

        #Methods that are contained in GRUN folder
        self.coordinates_file = "SELECT"
        self.points = None #creoque nolonecesito era del combobox
        self.out_folder = "SELECT"


        #points file button
        tk.Button(master, text="Select coordinates files.xlsx", width=35, height=3,bg="lemon chiffon",
                  command=lambda: self.set_coordinates()).grid(column=11, row=4,
                                                               padx=self.padx, pady=self.pady,
                                                               sticky=tk.W)


        #Output folder buttom
        tk.Button(master, text="Select output folder for the excel file", width=35, height=3, bg="wheat",
                  command=lambda: self.select_out_directory()).grid(column=11, row=9,
                                                                    padx=self.padx, pady=self.pady,
                                                                    sticky=tk.W)
        self.b_run = tk.Button(master, bg="dark sea green", text="Start",
                                       width=35, height=3, command=lambda: self.run_app())
        self.b_run.grid(sticky=tk.W, row= 14, column=11, padx=self.padx, pady=self.pady)

        #Coordinates file selection
        self.coordinates_label = tk.Label(master, text="Coordinates file (.xlsx): " + self.coordinates_file)
        self.coordinates_label.grid(column=0, columnspan=3, row=4, padx=self.padx, pady=self.pady, sticky=tk.W)
        #Output folder
        self.out_label = tk.Label(master, text="Output folder: " + self.out_folder)
        self.out_label.grid(column=0, columnspan=3, row=9, padx=self.padx, pady=self.pady, sticky=tk.W)
        self.run_label = tk.Label(master, fg="green", text="")
        self.run_label.grid(column=0, columnspan=3, row=11, padx=self.padx, pady=self.pady, sticky=tk.W)



    def run_app(self):
        # ensure that user selected all necessary inputs
        if not self.valid_selections():
            return -1

         #get selected characteristic coordinates
        if askokcancel("Start calculation?",
                       "Click OK to get the results."):
            PointsSet(self.coordinates_file)
            self.b_run.config(fg="forest green")
            self.run_label.config(text="Success: Created %s" % str(
                self.out_folder + "/coordinates_runoff_data.xlsx"))
            (self.out_folder + "/coordinates_runoff_data.xlsx")

    def set_coordinates(self):
        self.coordinates_file = self.select_file("coordinates file", "xlsx")
        try:
            self.points = PointsSet(self.coordinates_file)
        except OSError:
            showinfo("ERROR", "Could not open %s." % self.coordinates_file)
            self.coordinates_file = "SELECT"
            return -1

        # update grain label
        self.coordinates_label.config(text="coordinates file (xlsx): " + self.coordinates_file)


    def select_out_directory(self):
        self.out_folder = askdirectory()
         # update output folder label
        self.out_label.config(text="Output folder: " + self.out_folder)


    def select_file(self, description, file_type):
        return askopenfilename(filetypes=[(description, file_type)],
                           initialdir=os.path.abspath(""),
                           title="Select a %s file" % file_type,
                           parent=self)
    def valid_selections(self):
        if "SELECT" in self.coordinates_file:
            showinfo("ERROR", "Select coordinates file.")
            return False
        if "SELECT" in self.out_folder:
            showinfo("ERROR", "Select output folder.")
            return False
        return True

if __name__ == '__main__':
    RunoffApp().mainloop()


# https://stackoverflow.com/questions/32864610/understanding-parent-and-controller-in-tkinter-init
# https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/?completed=/styling-gui-bit-using-ttk/

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats  as stats
import random
import os
import tkinter as tk



class Distapp(tk.Tk):   # The "Distapp" class is inheriting from the tk.Tk class

    def __init__(self, *args, **kwargs):    # init method always runs when class is invoked. args and kwargs are used to pass unknown amount of args through the method. args= parameters, kwargs= dictionaries
        tk.Tk.__init__(self, *args, **kwargs)   # initializes the inherited tk.Tk tkinter class

        container= tk.Frame(self)   # "container" will be placeholder for window frames used throughout the program
        container.pack(side= "top", fill= "both", expand= True) # fills entire window frame
        container.grid_rowconfigure(0, weight= 1) # 0 sets the initial row and column numbers
        container.grid_columnconfigure(0, weight= 1)

        self.frames= {}     # dictionary to be used for the different window frames to be created throughout the program

        for f in (StartWindow, GraphWindow, ParamUniform, ParamUniformTriangular, ParamUniformTriangularNormal, ParamUniformTriangularNormalExponential, ParamUniformTriangularNormalExponentialErlang, ParamUniformTriangularNormalExponentialErlangGamma, ParamUniformTriangularNormalExponentialErlangGammaWeibull):       # iterates through the different windows the program will contain

            frame= f(container, self)   # defines a frame for each of the window classes in the program (defined below)
            self.frames[f]= frame       # stores each frame in the frames dictionary
            frame.grid(row= 0, column= 0, sticky= "nsew")   # nsew= north south east west: frame stretches to all boundaries of the window

        self.show_frame(StartWindow)        # show_frame defined below, initially for StartWindow, but can be used to pass subsequent window frames needed by the program

    def show_frame(self, controller):       # displays the window frame

        frame= self.frames[controller]  # adds a key to the self.frames dictionary; the key is passed in through the "controller" parameter. the value to the key is the current frame
        frame.tkraise()     # tk.raise brings the frame to the "top" so that the user can see it





class StartWindow(tk.Frame):        # class inherits from tk.Frame method to create a new window frame



    def __init__(self, parent, controller):



        tk.Frame.__init__(self, parent)     # initializes and inherits tk.Frame's __init__ method; parent is the Distapp class




        img_file = tk.PhotoImage(file="nps.png")    # img_file is an "object" instance of the tk.PhotoImage class
        label_txt= tk.Label(self, text= "Choose your distributions:", anchor= "center", justify= "left", pady= 30, font= ("Courier", 44))
        label_img= tk.Label(self, image= img_file)
        label_img.image= img_file   # keeps a reference so that image is not cleared after garbage collection

        label_txt.grid(row= 1, column= 0, padx= 10, pady= 10, sticky= "n")
        label_img.grid(row= 1, column= 1, padx= 10, pady= 10, sticky= "e")

        start_button= tk.Button(self, text= "Start", font= ("Courier", 100), fg= "green", command= lambda: controller.show_frame(ParamUniformTriangularNormalExponentialErlangGammaWeibull))
        quit_button= tk.Button(self, text= "Quit ", font= ("Courier", 100), fg= "red", command= quit)

        check_var0 = tk.IntVar()  # int variables are used to keep track of the state of the checkmark (0= off unchecked, 1= on checked). Each separate option to be checked must have it's own tk.IntVar() variable to keep track of its state
        check_var1 = tk.IntVar()
        check_var2 = tk.IntVar()
        check_var3 = tk.IntVar()
        check_var4 = tk.IntVar()
        check_var5 = tk.IntVar()
        check_var6 = tk.IntVar()

        dist_choice_0 = tk.Checkbutton(self, text="Uniform", justify= "left", padx= 10, pady= 5, font= ("Courier", 24), variable=check_var0)      # add command parameter: a procedure to be called every time the user changes the state of this checkbutton
        dist_choice_1 = tk.Checkbutton(self, text="Triangular", justify= "left", padx= 10, pady= 5, font= ("Courier", 24), variable=check_var1)
        dist_choice_2 = tk.Checkbutton(self, text="Normal", justify= "left", padx= 10, pady= 5, font= ("Courier", 24), variable=check_var2)
        dist_choice_3 = tk.Checkbutton(self, text="Exponential", justify= "left", padx= 10, pady= 5, font= ("Courier", 24), variable=check_var3)
        dist_choice_4 = tk.Checkbutton(self, text="Erlang", justify= "left", padx= 10, pady= 5, font= ("Courier", 24), variable=check_var4)
        dist_choice_5 = tk.Checkbutton(self, text="Gamma", justify= "left", padx= 10, pady= 5, font= ("Courier", 24), variable=check_var5)
        dist_choice_6 = tk.Checkbutton(self, text="Weibull", justify= "left", padx= 10, pady= 5, font= ("Courier", 24), variable=check_var6)

        dist_choice_0.grid(row= 2, column= 0, sticky= "w")
        dist_choice_1.grid(row= 3, column= 0, sticky= "w")
        dist_choice_2.grid(row=4, column=0, sticky="w")
        dist_choice_3.grid(row=5, column=0, sticky="w")
        dist_choice_4.grid(row=6, column=0, sticky="w")
        dist_choice_5.grid(row=7, column=0, sticky="w")
        dist_choice_6.grid(row=8, column=0, sticky="w")

        start_button.grid(row= 10, column= 1, sticky= "w")
        quit_button.grid(row= 11, column= 1, sticky= "w")

        print(type(check_var0))






class ParamUniform(tk.Frame):

    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)


        label_txt = tk.Label(self, text="Enter uniform distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))
        label_txt_default = tk.Label(self, text="(Leave field blank to accept [default] value)", anchor="center", justify="left", pady=0, font=("Courier", 12))

        self.uniform_low = 0
        self.uniform_high = 0
        self.uniform_ssize = 0
        self.uniform_seed = 0

        def uniform_params():
            if uniform_low_field.get() != "":
                self.uniform_low= uniform_low_field.get()
            else:
                self.uniform_low= 0
            if uniform_high_field.get() != "":
                self.uniform_high= uniform_high_field.get()
            else:
                self.uniform_high= 100
            if uniform_ssize_field.get() != "":
                self.uniform_ssize= uniform_ssize_field.get()
            else:
                self.uniform_ssize= 2000
            if uniform_seed_field.get() != "":
                self.uniform_seed= uniform_seed_field.get()
            else:
                self.uniform_seed= 3307


        string_var0= tk.StringVar()     # tkinter requires text entry strings to be converted using the tk.StringVar method for them to be able to be passed to other functions
        string_var1= tk.StringVar()
        string_var2= tk.StringVar()
        string_var3= tk.StringVar()

        uniform_low_field_txt = tk.Label(self, text="Low value [0]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_low_field= tk.Entry(self, textvariable= string_var0, width= 5)     # text entry field for user specified parameters
        uniform_high_field_txt = tk.Label(self, text="High value [100]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_high_field = tk.Entry(self, textvariable=string_var1, width=5)
        uniform_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_ssize_field= tk.Entry(self, textvariable= string_var2, width= 5)
        uniform_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_seed_field= tk.Entry(self, textvariable= string_var3, width= 5)


        label_txt.grid(row= 0, column= 0, padx= 10, pady= 0, sticky= "nw")
        label_txt_default.grid(row= 1, column= 0, padx= 10, pady= 0, sticky= "nw")

        blank_space= tk.Label(self, text="", pady= 15)
        blank_space.grid(row= 2, column= 0)

        uniform_low_field_txt.grid(row= 3, column= 0, sticky= "e")
        uniform_low_field.grid(row= 3, column= 1, sticky= "w")
        uniform_high_field_txt.grid(row= 4, column= 0, sticky= "e")
        uniform_high_field.grid(row= 4, column= 1, sticky= "w")
        uniform_ssize_field_txt.grid(row= 5, column= 0, sticky= "e")
        uniform_ssize_field.grid(row= 5, column= 1, sticky= "w")
        uniform_seed_field_txt.grid(row= 6, column= 0, sticky= "e")
        uniform_seed_field.grid(row= 6, column= 1, sticky= "w")



        go_button = tk.Button(self, text="Go", font= ("Courier", 50), fg="green", command= uniform_params)
        back_button = tk.Button(self, text="Cancel", font=("Courier", 50), command=lambda: controller.show_frame(StartWindow))
        go_button.grid(row= 7, column= 1, sticky= "w")
        back_button.grid(row= 7, column= 2, sticky= "e")





class ParamUniformTriangular(tk.Frame):


    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)


        self.uniform_low = 0
        self.uniform_high = 0
        self.uniform_ssize = 0
        self.uniform_seed = 0

        self.triangular_left = 0
        self.triangular_right = 0
        self.triangular_mode = 0
        self.triangular_ssize = 0
        self.triangular_seed = 0

        def uniform_tri_params():
            if uniform_low_field.get() != "":
                self.uniform_low = uniform_low_field.get()
            else:
                self.uniform_low = 0
            if uniform_high_field.get() != "":
                self.uniform_high = uniform_high_field.get()
            else:
                self.uniform_high = 100
            if uniform_ssize_field.get() != "":
                self.uniform_ssize = uniform_ssize_field.get()
            else:
                self.uniform_ssize = 2000
            if uniform_seed_field.get() != "":
                self.uniform_seed = uniform_seed_field.get()
            else:
                self.uniform_seed = 3307
            if triangular_left_field.get() != "":
                self.triangular_left = triangular_left_field.get()
            else:
                self.triangular_left = 40
            if triangular_right_field.get() != "":
                self.triangular_right = triangular_right_field.get()
            else:
                self.triangular_right = 100
            if triangular_mode_field.get() != "":
                self.triangular_mode = triangular_mode_field.get()
            else:
                self.triangular_mode = 75
            if triangular_ssize_field.get() != "":
                self.triangular_ssize = triangular_ssize_field.get()
            else:
                self.triangular_ssize = 2000
            if triangular_seed_field.get() != "":
                self.triangular_seed= triangular_seed_field.get()
            else:
                self.triangular_seed= 3307

        string_var0 = tk.StringVar()  # tkinter requires text entry strings to be converted using the tk.StringVar method for them to be able to be passed to other functions
        string_var1 = tk.StringVar()
        string_var2 = tk.StringVar()
        string_var3 = tk.StringVar()
        string_var4= tk.StringVar()
        string_var5= tk.StringVar()
        string_var6= tk.StringVar()
        string_var7= tk.StringVar()
        string_var8= tk.StringVar()


        uniform_label_txt = tk.Label(self, text="Enter uniform distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))
        uniform_label_txt_default = tk.Label(self, text="(Leave field blank to accept [default] value)", anchor="center", justify="left", pady=0, font=("Courier", 12))

        uniform_low_field_txt = tk.Label(self, text="Low value [0]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_low_field = tk.Entry(self, textvariable=string_var0, width=5)
        uniform_high_field_txt = tk.Label(self, text="High value [100]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_high_field = tk.Entry(self, textvariable=string_var1, width=5)
        uniform_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_ssize_field = tk.Entry(self, textvariable=string_var2, width=5)
        uniform_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_seed_field = tk.Entry(self, textvariable=string_var3, width=5)


        triangular_label_txt = tk.Label(self, text="Enter triangular distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        triangular_left_field_txt = tk.Label(self, text="Left value [40]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_left_field = tk.Entry(self, textvariable=string_var4, width=5)
        triangular_right_field_txt = tk.Label(self, text="Right value [100]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_right_field = tk.Entry(self, textvariable=string_var5, width=5)
        triangular_mode_field_txt = tk.Label(self, text="Mode [75]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_mode_field = tk.Entry(self, textvariable=string_var6, width=5)
        triangular_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_ssize_field = tk.Entry(self, textvariable=string_var7, width=5)
        triangular_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_seed_field = tk.Entry(self, textvariable=string_var8, width=5)





        uniform_label_txt.grid(row=0, column=0, padx=10, pady=0, sticky="nw")
        uniform_label_txt_default.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        blank_space = tk.Label(self, text="", pady=15)
        blank_space.grid(row=2, column=0)

        uniform_low_field_txt.grid(row= 3, column= 0, sticky= "e")
        uniform_low_field.grid(row= 3, column= 1, sticky= "w")
        uniform_high_field_txt.grid(row= 4, column= 0, sticky= "e")
        uniform_high_field.grid(row= 4, column= 1, sticky= "w")
        uniform_ssize_field_txt.grid(row= 5, column= 0, sticky= "e")
        uniform_ssize_field.grid(row= 5, column= 1, sticky= "w")
        uniform_seed_field_txt.grid(row= 6, column= 0, sticky= "e")
        uniform_seed_field.grid(row= 6, column= 1, sticky= "w")

        blank_space.grid(row= 7, column=0)

        triangular_label_txt.grid(row=8, column=0, padx=10, pady=0, sticky="nw")

        triangular_left_field_txt.grid(row= 9, column= 0, sticky= "e")
        triangular_left_field.grid(row= 9, column= 1, sticky= "w")
        triangular_right_field_txt.grid(row= 10, column= 0, sticky= "e")
        triangular_right_field.grid(row= 10, column= 1, sticky= "w")
        triangular_mode_field_txt.grid(row= 11, column= 0, sticky= "e")
        triangular_mode_field.grid(row= 11, column= 1, sticky= "w")
        triangular_ssize_field_txt.grid(row= 12, column= 0, sticky= "e")
        triangular_ssize_field.grid(row= 12, column= 1, sticky= "w")
        triangular_seed_field_txt.grid(row= 13, column= 0, sticky= "e")
        triangular_seed_field.grid(row= 13, column= 1, sticky= "w")

        go_button = tk.Button(self, text="Go", font= ("Courier", 50), fg="green", command=uniform_tri_params)
        back_button = tk.Button(self, text="Cancel", font=("Courier", 50), command=lambda: controller.show_frame(StartWindow))
        go_button.grid(row=14, column=1, sticky="w")
        back_button.grid(row= 14, column= 2, sticky= "e")






class ParamUniformTriangularNormal(tk.Frame):


    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)


        self.uniform_low = 0
        self.uniform_high = 0
        self.uniform_ssize = 0
        self.uniform_seed = 0

        self.triangular_left = 0
        self.triangular_right = 0
        self.triangular_mode = 0
        self.triangular_ssize = 0
        self.triangular_seed = 0

        self.normal_seed = 0
        self.normal_ssize = 0
        self.normal_stdev = 0

        def uniform_tri_norm_params():
            if uniform_low_field.get() != "":
                self.uniform_low = uniform_low_field.get()
            else:
                self.uniform_low = 0
            if uniform_high_field.get() != "":
                self.uniform_high = uniform_high_field.get()
            else:
                self.uniform_high = 100
            if uniform_ssize_field.get() != "":
                self.uniform_ssize = uniform_ssize_field.get()
            else:
                self.uniform_ssize = 2000
            if uniform_seed_field.get() != "":
                self.uniform_seed = uniform_seed_field.get()
            else:
                self.uniform_seed = 3307
            if triangular_left_field.get() != "":
                self.triangular_left = triangular_left_field.get()
            else:
                self.triangular_left = 40
            if triangular_right_field.get() != "":
                self.triangular_right = triangular_right_field.get()
            else:
                self.triangular_right = 100
            if triangular_mode_field.get() != "":
                self.triangular_mode = triangular_mode_field.get()
            else:
                self.triangular_mode = 75
            if triangular_ssize_field.get() != "":
                self.triangular_ssize = triangular_ssize_field.get()
            else:
                self.triangular_ssize = 2000
            if triangular_seed_field.get() != "":
                self.triangular_seed= triangular_seed_field.get()
            else:
                self.triangular_seed= 3307
            if normal_stdev_field.get() != "":
                self.normal_stdev = normal_stdev_field.get()
            else:
                self.normal_stdev = 25
            if normal_ssize_field.get() != "":
                self.normal_ssize = normal_ssize_field.get()
            else:
                self.normal_ssize = 2000
            if normal_seed_field.get() != "":
                self.normal_seed= normal_seed_field.get()
            else:
                self.normal_seed= 3307

        string_var0 = tk.StringVar()  # tkinter requires text entry strings to be converted using the tk.StringVar method for them to be able to be passed to other functions
        string_var1 = tk.StringVar()
        string_var2 = tk.StringVar()
        string_var3 = tk.StringVar()
        string_var4= tk.StringVar()
        string_var5= tk.StringVar()
        string_var6= tk.StringVar()
        string_var7= tk.StringVar()
        string_var8= tk.StringVar()
        string_var9= tk.StringVar()
        string_var10= tk.StringVar()
        string_var11= tk.StringVar()


        uniform_label_txt = tk.Label(self, text="Enter uniform distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))
        uniform_label_txt_default = tk.Label(self, text="(Leave field blank to accept [default] value)", anchor="center", justify="left", pady=0, font=("Courier", 12))

        uniform_low_field_txt = tk.Label(self, text="Low value [0]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_low_field = tk.Entry(self, textvariable=string_var0, width=5)
        uniform_high_field_txt = tk.Label(self, text="High value [100]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_high_field = tk.Entry(self, textvariable=string_var1, width=5)
        uniform_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_ssize_field = tk.Entry(self, textvariable=string_var2, width=5)
        uniform_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_seed_field = tk.Entry(self, textvariable=string_var3, width=5)


        triangular_label_txt = tk.Label(self, text="Enter triangular distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        triangular_left_field_txt = tk.Label(self, text="Left value [40]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_left_field = tk.Entry(self, textvariable=string_var4, width=5)
        triangular_right_field_txt = tk.Label(self, text="Right value [100]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_right_field = tk.Entry(self, textvariable=string_var5, width=5)
        triangular_mode_field_txt = tk.Label(self, text="Mode [75]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_mode_field = tk.Entry(self, textvariable=string_var6, width=5)
        triangular_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_ssize_field = tk.Entry(self, textvariable=string_var7, width=5)
        triangular_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_seed_field = tk.Entry(self, textvariable=string_var8, width=5)


        normal_label_txt = tk.Label(self, text="Enter normal distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        normal_stdev_field_txt = tk.Label(self, text="Standard deviation [25]: ", justify="left", pady=5, font=("Courier", 12))
        normal_stdev_field = tk.Entry(self, textvariable=string_var9, width=5)
        normal_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        normal_ssize_field = tk.Entry(self, textvariable=string_var10, width=5)
        normal_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        normal_seed_field = tk.Entry(self, textvariable=string_var11, width=5)


        uniform_label_txt.grid(row=0, column=0, padx=10, pady=0, sticky="nw")
        uniform_label_txt_default.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        blank_space = tk.Label(self, text="", pady=15)
        blank_space.grid(row=2, column=0)

        uniform_low_field_txt.grid(row= 3, column= 0, sticky= "e")
        uniform_low_field.grid(row= 3, column= 1, sticky= "w")
        uniform_high_field_txt.grid(row= 4, column= 0, sticky= "e")
        uniform_high_field.grid(row= 4, column= 1, sticky= "w")
        uniform_ssize_field_txt.grid(row= 5, column= 0, sticky= "e")
        uniform_ssize_field.grid(row= 5, column= 1, sticky= "w")
        uniform_seed_field_txt.grid(row= 6, column= 0, sticky= "e")
        uniform_seed_field.grid(row= 6, column= 1, sticky= "w")

        blank_space2 = tk.Label(self, text="", pady=15)
        blank_space2.grid(row= 7, column=0)

        triangular_label_txt.grid(row=8, column=0, padx=10, pady=0, sticky="nw")

        triangular_left_field_txt.grid(row= 9, column= 0, sticky= "e")
        triangular_left_field.grid(row= 9, column= 1, sticky= "w")
        triangular_right_field_txt.grid(row= 10, column= 0, sticky= "e")
        triangular_right_field.grid(row= 10, column= 1, sticky= "w")
        triangular_mode_field_txt.grid(row= 11, column= 0, sticky= "e")
        triangular_mode_field.grid(row= 11, column= 1, sticky= "w")
        triangular_ssize_field_txt.grid(row= 12, column= 0, sticky= "e")
        triangular_ssize_field.grid(row= 12, column= 1, sticky= "w")
        triangular_seed_field_txt.grid(row= 13, column= 0, sticky= "e")
        triangular_seed_field.grid(row= 13, column= 1, sticky= "w")

        blank_space3 = tk.Label(self, text="", pady=15)
        blank_space3.grid(row=14, column=0)

        normal_label_txt.grid(row=15, column=0, padx=10, pady=0, sticky="nw")

        normal_stdev_field_txt.grid(row=16, column=0, sticky="e")
        normal_stdev_field.grid(row=16, column=1, sticky="w")
        normal_ssize_field_txt.grid(row=17, column=0, sticky="e")
        normal_ssize_field.grid(row=17, column=1, sticky="w")
        normal_seed_field_txt.grid(row=18, column=0, sticky="e")
        normal_seed_field.grid(row=18, column=1, sticky="w")


        go_button = tk.Button(self, text="Go", font= ("Courier", 50), fg="green", command=uniform_tri_norm_params)
        back_button = tk.Button(self, text="Cancel", font=("Courier", 50), command=lambda: controller.show_frame(StartWindow))
        go_button.grid(row=19, column=1, sticky="w")
        back_button.grid(row= 19, column= 2, sticky= "e")







class ParamUniformTriangularNormalExponential(tk.Frame):


    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)


        self.uniform_low = 0
        self.uniform_high = 0
        self.uniform_ssize = 0
        self.uniform_seed = 0

        self.triangular_left = 0
        self.triangular_right = 0
        self.triangular_mode = 0
        self.triangular_ssize = 0
        self.triangular_seed = 0

        self.normal_seed = 0
        self.normal_ssize = 0
        self.normal_stdev = 0

        self.exp_rate = 0.0
        self.exp_seed = 0
        self.exp_ssize = 0

        def uniform_tri_norm_exp_params():
            if uniform_low_field.get() != "":
                self.uniform_low = uniform_low_field.get()
            else:
                self.uniform_low = 0
            if uniform_high_field.get() != "":
                self.uniform_high = uniform_high_field.get()
            else:
                self.uniform_high = 100
            if uniform_ssize_field.get() != "":
                self.uniform_ssize = uniform_ssize_field.get()
            else:
                self.uniform_ssize = 2000
            if uniform_seed_field.get() != "":
                self.uniform_seed = uniform_seed_field.get()
            else:
                self.uniform_seed = 3307
            if triangular_left_field.get() != "":
                self.triangular_left = triangular_left_field.get()
            else:
                self.triangular_left = 40
            if triangular_right_field.get() != "":
                self.triangular_right = triangular_right_field.get()
            else:
                self.triangular_right = 100
            if triangular_mode_field.get() != "":
                self.triangular_mode = triangular_mode_field.get()
            else:
                self.triangular_mode = 75
            if triangular_ssize_field.get() != "":
                self.triangular_ssize = triangular_ssize_field.get()
            else:
                self.triangular_ssize = 2000
            if triangular_seed_field.get() != "":
                self.triangular_seed= triangular_seed_field.get()
            else:
                self.triangular_seed= 3307
            if normal_stdev_field.get() != "":
                self.normal_stdev = normal_stdev_field.get()
            else:
                self.normal_stdev = 25
            if normal_ssize_field.get() != "":
                self.normal_ssize = normal_ssize_field.get()
            else:
                self.normal_ssize = 2000
            if normal_seed_field.get() != "":
                self.normal_seed= normal_seed_field.get()
            else:
                self.normal_seed= 3307
            if exp_rate_field.get() != "":
                self.exp_rate = exp_rate_field.get()
            else:
                self.exp_rate = 1/25
            if exp_ssize_field.get() != "":
                self.exp_ssize = exp_ssize_field.get()
            else:
                self.exp_ssize = 2000
            if exp_seed_field.get() != "":
                self.exp_seed= exp_seed_field.get()
            else:
                self.exp_seed= 3307

        string_var0 = tk.StringVar()  # tkinter requires text entry strings to be converted using the tk.StringVar method for them to be able to be passed to other functions
        string_var1 = tk.StringVar()
        string_var2 = tk.StringVar()
        string_var3 = tk.StringVar()
        string_var4= tk.StringVar()
        string_var5= tk.StringVar()
        string_var6= tk.StringVar()
        string_var7= tk.StringVar()
        string_var8= tk.StringVar()
        string_var9= tk.StringVar()
        string_var10= tk.StringVar()
        string_var11= tk.StringVar()
        string_var12= tk.StringVar()
        string_var13= tk.StringVar()
        string_var14= tk.StringVar()


        uniform_label_txt = tk.Label(self, text="Enter uniform distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))
        uniform_label_txt_default = tk.Label(self, text="(Leave field blank to accept [default] value)", anchor="center", justify="left", pady=0, font=("Courier", 12))

        uniform_low_field_txt = tk.Label(self, text="Low value [0]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_low_field = tk.Entry(self, textvariable=string_var0, width=5)
        uniform_high_field_txt = tk.Label(self, text="High value [100]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_high_field = tk.Entry(self, textvariable=string_var1, width=5)
        uniform_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_ssize_field = tk.Entry(self, textvariable=string_var2, width=5)
        uniform_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_seed_field = tk.Entry(self, textvariable=string_var3, width=5)


        triangular_label_txt = tk.Label(self, text="Enter triangular distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        triangular_left_field_txt = tk.Label(self, text="Left value [40]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_left_field = tk.Entry(self, textvariable=string_var4, width=5)
        triangular_right_field_txt = tk.Label(self, text="Right value [100]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_right_field = tk.Entry(self, textvariable=string_var5, width=5)
        triangular_mode_field_txt = tk.Label(self, text="Mode [75]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_mode_field = tk.Entry(self, textvariable=string_var6, width=5)
        triangular_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_ssize_field = tk.Entry(self, textvariable=string_var7, width=5)
        triangular_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_seed_field = tk.Entry(self, textvariable=string_var8, width=5)


        normal_label_txt = tk.Label(self, text="Enter normal distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        normal_stdev_field_txt = tk.Label(self, text="Standard deviation [25]: ", justify="left", pady=5, font=("Courier", 12))
        normal_stdev_field = tk.Entry(self, textvariable=string_var9, width=5)
        normal_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        normal_ssize_field = tk.Entry(self, textvariable=string_var10, width=5)
        normal_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        normal_seed_field = tk.Entry(self, textvariable=string_var11, width=5)


        exp_label_txt = tk.Label(self, text="Enter exponential distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        exp_rate_field_txt = tk.Label(self, text="Rate [1/25]: ", justify="left", pady=5, font=("Courier", 12))
        exp_rate_field = tk.Entry(self, textvariable=string_var12, width=5)
        exp_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        exp_ssize_field = tk.Entry(self, textvariable=string_var13, width=5)
        exp_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        exp_seed_field = tk.Entry(self, textvariable=string_var14, width=5)




        uniform_label_txt.grid(row=0, column=0, padx=10, pady=0, sticky="nw")
        uniform_label_txt_default.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        blank_space = tk.Label(self, text="", pady=15)
        blank_space.grid(row=2, column=0)

        uniform_low_field_txt.grid(row= 3, column= 0, sticky= "e")
        uniform_low_field.grid(row= 3, column= 1, sticky= "w")
        uniform_high_field_txt.grid(row= 4, column= 0, sticky= "e")
        uniform_high_field.grid(row= 4, column= 1, sticky= "w")
        uniform_ssize_field_txt.grid(row= 5, column= 0, sticky= "e")
        uniform_ssize_field.grid(row= 5, column= 1, sticky= "w")
        uniform_seed_field_txt.grid(row= 6, column= 0, sticky= "e")
        uniform_seed_field.grid(row= 6, column= 1, sticky= "w")

        blank_space2 = tk.Label(self, text="", pady=15)
        blank_space2.grid(row= 7, column=0)

        triangular_label_txt.grid(row=8, column=0, padx=10, pady=0, sticky="nw")

        triangular_left_field_txt.grid(row= 9, column= 0, sticky= "e")
        triangular_left_field.grid(row= 9, column= 1, sticky= "w")
        triangular_right_field_txt.grid(row= 10, column= 0, sticky= "e")
        triangular_right_field.grid(row= 10, column= 1, sticky= "w")
        triangular_mode_field_txt.grid(row= 11, column= 0, sticky= "e")
        triangular_mode_field.grid(row= 11, column= 1, sticky= "w")
        triangular_ssize_field_txt.grid(row= 12, column= 0, sticky= "e")
        triangular_ssize_field.grid(row= 12, column= 1, sticky= "w")
        triangular_seed_field_txt.grid(row= 13, column= 0, sticky= "e")
        triangular_seed_field.grid(row= 13, column= 1, sticky= "w")

        blank_space3 = tk.Label(self, text="", pady=15)
        blank_space3.grid(row=14, column=0)

        normal_label_txt.grid(row=15, column=0, padx=10, pady=0, sticky="nw")

        normal_stdev_field_txt.grid(row=16, column=0, sticky="e")
        normal_stdev_field.grid(row=16, column=1, sticky="w")
        normal_ssize_field_txt.grid(row=17, column=0, sticky="e")
        normal_ssize_field.grid(row=17, column=1, sticky="w")
        normal_seed_field_txt.grid(row=18, column=0, sticky="e")
        normal_seed_field.grid(row=18, column=1, sticky="w")

        blank_space4 = tk.Label(self, text="", pady=15)
        blank_space4.grid(row=19, column=0)

        exp_label_txt.grid(row=20, column=0, padx=10, pady=0, sticky="nw")

        exp_rate_field_txt.grid(row=21, column=0, sticky="e")
        exp_rate_field.grid(row=21, column=1, sticky="w")
        exp_ssize_field_txt.grid(row=22, column=0, sticky="e")
        exp_ssize_field.grid(row=22, column=1, sticky="w")
        exp_seed_field_txt.grid(row=23, column=0, sticky="e")
        exp_seed_field.grid(row=23, column=1, sticky="w")


        go_button = tk.Button(self, text="Go", font= ("Courier", 50), fg="green", command=uniform_tri_norm_exp_params)
        back_button = tk.Button(self, text="Cancel", font=("Courier", 50), command=lambda: controller.show_frame(StartWindow))
        go_button.grid(row=24, column=1, sticky="w")
        back_button.grid(row= 24, column= 2, sticky= "e")





class ParamUniformTriangularNormalExponentialErlang(tk.Frame):


    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)


        self.uniform_low = 0
        self.uniform_high = 0
        self.uniform_ssize = 0
        self.uniform_seed = 0

        self.triangular_left = 0
        self.triangular_right = 0
        self.triangular_mode = 0
        self.triangular_ssize = 0
        self.triangular_seed = 0

        self.normal_seed = 0
        self.normal_ssize = 0
        self.normal_stdev = 0

        self.exp_rate = 0.0
        self.exp_seed = 0
        self.exp_ssize = 0

        self.erlang_alpha = 0
        self.erlang_loc = 0
        self.erlang_scale = 0
        self.erlang_ssize = 0
        self.erlang_seed = 0

        def uniform_tri_norm_exp_erlang_params():
            if uniform_low_field.get() != "":
                self.uniform_low = uniform_low_field.get()
            else:
                self.uniform_low = 0
            if uniform_high_field.get() != "":
                self.uniform_high = uniform_high_field.get()
            else:
                self.uniform_high = 100
            if uniform_ssize_field.get() != "":
                self.uniform_ssize = uniform_ssize_field.get()
            else:
                self.uniform_ssize = 2000
            if uniform_seed_field.get() != "":
                self.uniform_seed = uniform_seed_field.get()
            else:
                self.uniform_seed = 3307
            if triangular_left_field.get() != "":
                self.triangular_left = triangular_left_field.get()
            else:
                self.triangular_left = 40
            if triangular_right_field.get() != "":
                self.triangular_right = triangular_right_field.get()
            else:
                self.triangular_right = 100
            if triangular_mode_field.get() != "":
                self.triangular_mode = triangular_mode_field.get()
            else:
                self.triangular_mode = 75
            if triangular_ssize_field.get() != "":
                self.triangular_ssize = triangular_ssize_field.get()
            else:
                self.triangular_ssize = 2000
            if triangular_seed_field.get() != "":
                self.triangular_seed= triangular_seed_field.get()
            else:
                self.triangular_seed= 3307
            if normal_stdev_field.get() != "":
                self.normal_stdev = normal_stdev_field.get()
            else:
                self.normal_stdev = 25
            if normal_ssize_field.get() != "":
                self.normal_ssize = normal_ssize_field.get()
            else:
                self.normal_ssize = 2000
            if normal_seed_field.get() != "":
                self.normal_seed= normal_seed_field.get()
            else:
                self.normal_seed= 3307
            if exp_rate_field.get() != "":
                self.exp_rate = exp_rate_field.get()
            else:
                self.exp_rate = 1/25
            if exp_ssize_field.get() != "":
                self.exp_ssize = exp_ssize_field.get()
            else:
                self.exp_ssize = 2000
            if exp_seed_field.get() != "":
                self.exp_seed= exp_seed_field.get()
            else:
                self.exp_seed= 3307
            if erlang_alpha_field.get() != "":
                self.erlang_alpha = erlang_alpha_field.get()
            else:
                self.erlang_alpha = 3
            if erlang_loc_field.get() != "":
                self.erlang_loc= erlang_loc_field.get()
            else:
                self.erlang_loc= 0
            if erlang_scale_field.get() != "":
                self.erlang_scale = erlang_scale_field.get()
            else:
                self.erlang_scale = 25
            if erlang_ssize_field.get() != "":
                self.erlang_ssize = erlang_ssize_field.get()
            else:
                self.erlang_ssize = 2000
            if erlang_seed_field.get() != "":
                self.erlang_seed= erlang_seed_field.get()
            else:
                self.erlang_seed= 3307

        string_var0 = tk.StringVar()  # tkinter requires text entry strings to be converted using the tk.StringVar method for them to be able to be passed to other functions
        string_var1 = tk.StringVar()
        string_var2 = tk.StringVar()
        string_var3 = tk.StringVar()
        string_var4= tk.StringVar()
        string_var5= tk.StringVar()
        string_var6= tk.StringVar()
        string_var7= tk.StringVar()
        string_var8= tk.StringVar()
        string_var9= tk.StringVar()
        string_var10= tk.StringVar()
        string_var11= tk.StringVar()
        string_var12= tk.StringVar()
        string_var13= tk.StringVar()
        string_var14= tk.StringVar()
        string_var15= tk.StringVar()
        string_var16= tk.StringVar()
        string_var17= tk.StringVar()
        string_var18= tk.StringVar()
        string_var19= tk.StringVar()

        uniform_label_txt = tk.Label(self, text="Enter uniform distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))
        uniform_label_txt_default = tk.Label(self, text="(Leave field blank to accept [default] value)", anchor="center", justify="left", pady=0, font=("Courier", 12))

        uniform_low_field_txt = tk.Label(self, text="Low value [0]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_low_field = tk.Entry(self, textvariable=string_var0, width=5)
        uniform_high_field_txt = tk.Label(self, text="High value [100]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_high_field = tk.Entry(self, textvariable=string_var1, width=5)
        uniform_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_ssize_field = tk.Entry(self, textvariable=string_var2, width=5)
        uniform_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_seed_field = tk.Entry(self, textvariable=string_var3, width=5)


        triangular_label_txt = tk.Label(self, text="Enter triangular distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        triangular_left_field_txt = tk.Label(self, text="Left value [40]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_left_field = tk.Entry(self, textvariable=string_var4, width=5)
        triangular_right_field_txt = tk.Label(self, text="Right value [100]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_right_field = tk.Entry(self, textvariable=string_var5, width=5)
        triangular_mode_field_txt = tk.Label(self, text="Mode [75]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_mode_field = tk.Entry(self, textvariable=string_var6, width=5)
        triangular_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_ssize_field = tk.Entry(self, textvariable=string_var7, width=5)
        triangular_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_seed_field = tk.Entry(self, textvariable=string_var8, width=5)


        normal_label_txt = tk.Label(self, text="Enter normal distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        normal_stdev_field_txt = tk.Label(self, text="Standard deviation [25]: ", justify="left", pady=5, font=("Courier", 12))
        normal_stdev_field = tk.Entry(self, textvariable=string_var9, width=5)
        normal_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        normal_ssize_field = tk.Entry(self, textvariable=string_var10, width=5)
        normal_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        normal_seed_field = tk.Entry(self, textvariable=string_var11, width=5)


        exp_label_txt = tk.Label(self, text="Enter exponential distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        exp_rate_field_txt = tk.Label(self, text="Rate [1/25]: ", justify="left", pady=5, font=("Courier", 12))
        exp_rate_field = tk.Entry(self, textvariable=string_var12, width=5)
        exp_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        exp_ssize_field = tk.Entry(self, textvariable=string_var13, width=5)
        exp_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        exp_seed_field = tk.Entry(self, textvariable=string_var14, width=5)

        erlang_label_txt = tk.Label(self, text="Enter erlang distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        erlang_alpha_field_txt = tk.Label(self, text="Alpha value [3]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_alpha_field = tk.Entry(self, textvariable=string_var15, width=5)
        erlang_loc_field_txt = tk.Label(self, text="Loc value [0]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_loc_field = tk.Entry(self, textvariable=string_var16, width=5)
        erlang_scale_field_txt = tk.Label(self, text="Scale [25]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_scale_field = tk.Entry(self, textvariable=string_var17, width=5)
        erlang_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_ssize_field = tk.Entry(self, textvariable=string_var18, width=5)
        erlang_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_seed_field = tk.Entry(self, textvariable=string_var19, width=5)




        uniform_label_txt.grid(row=0, column=0, padx=10, pady=0, sticky="nw")
        uniform_label_txt_default.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        blank_space = tk.Label(self, text="", pady=15)
        blank_space.grid(row=2, column=0)

        uniform_low_field_txt.grid(row= 3, column= 0, sticky= "e")
        uniform_low_field.grid(row= 3, column= 1, sticky= "w")
        uniform_high_field_txt.grid(row= 4, column= 0, sticky= "e")
        uniform_high_field.grid(row= 4, column= 1, sticky= "w")
        uniform_ssize_field_txt.grid(row= 5, column= 0, sticky= "e")
        uniform_ssize_field.grid(row= 5, column= 1, sticky= "w")
        uniform_seed_field_txt.grid(row= 6, column= 0, sticky= "e")
        uniform_seed_field.grid(row= 6, column= 1, sticky= "w")

        blank_space2 = tk.Label(self, text="", pady=15)
        blank_space2.grid(row= 7, column=0)

        triangular_label_txt.grid(row=8, column=0, padx=10, pady=0, sticky="nw")

        triangular_left_field_txt.grid(row= 9, column= 0, sticky= "e")
        triangular_left_field.grid(row= 9, column= 1, sticky= "w")
        triangular_right_field_txt.grid(row= 10, column= 0, sticky= "e")
        triangular_right_field.grid(row= 10, column= 1, sticky= "w")
        triangular_mode_field_txt.grid(row= 11, column= 0, sticky= "e")
        triangular_mode_field.grid(row= 11, column= 1, sticky= "w")
        triangular_ssize_field_txt.grid(row= 12, column= 0, sticky= "e")
        triangular_ssize_field.grid(row= 12, column= 1, sticky= "w")
        triangular_seed_field_txt.grid(row= 13, column= 0, sticky= "e")
        triangular_seed_field.grid(row= 13, column= 1, sticky= "w")

        blank_space3 = tk.Label(self, text="", pady=15)
        blank_space3.grid(row=14, column=0)

        normal_label_txt.grid(row=15, column=0, padx=10, pady=0, sticky="nw")

        normal_stdev_field_txt.grid(row=16, column=0, sticky="e")
        normal_stdev_field.grid(row=16, column=1, sticky="w")
        normal_ssize_field_txt.grid(row=17, column=0, sticky="e")
        normal_ssize_field.grid(row=17, column=1, sticky="w")
        normal_seed_field_txt.grid(row=18, column=0, sticky="e")
        normal_seed_field.grid(row=18, column=1, sticky="w")

        blank_space4 = tk.Label(self, text="", pady=15)
        blank_space4.grid(row=19, column=0)

        exp_label_txt.grid(row=20, column=0, padx=10, pady=0, sticky="nw")

        exp_rate_field_txt.grid(row=21, column=0, sticky="e")
        exp_rate_field.grid(row=21, column=1, sticky="w")
        exp_ssize_field_txt.grid(row=22, column=0, sticky="e")
        exp_ssize_field.grid(row=22, column=1, sticky="w")
        exp_seed_field_txt.grid(row=23, column=0, sticky="e")
        exp_seed_field.grid(row=23, column=1, sticky="w")

        blank_space5 = tk.Label(self, text="", pady=15)
        blank_space5.grid(row= 24, column=0)

        erlang_label_txt.grid(row=0, column=2, padx=10, pady=0, sticky="nw")

        erlang_alpha_field_txt.grid(row= 1, column= 2, sticky= "e")
        erlang_alpha_field.grid(row= 1, column= 3, sticky= "w")
        erlang_loc_field_txt.grid(row= 2, column= 2, sticky= "e")
        erlang_loc_field.grid(row= 2, column= 3, sticky= "w")
        erlang_scale_field_txt.grid(row= 3, column= 2, sticky= "e")
        erlang_scale_field.grid(row= 3, column= 3, sticky= "w")
        erlang_ssize_field_txt.grid(row= 4, column= 2, sticky= "e")
        erlang_ssize_field.grid(row= 4, column= 3, sticky= "w")
        erlang_seed_field_txt.grid(row= 5, column= 2, sticky= "e")
        erlang_seed_field.grid(row= 5, column= 3, sticky= "w")


        go_button = tk.Button(self, text="Go", font= ("Courier", 50), fg="green", command=uniform_tri_norm_exp_erlang_params)
        back_button = tk.Button(self, text="Cancel", font=("Courier", 50), command=lambda: controller.show_frame(StartWindow))
        go_button.grid(row=25, column=1, sticky="w")
        back_button.grid(row= 25, column= 2, sticky= "e")





class ParamUniformTriangularNormalExponentialErlangGamma(tk.Frame):


    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)


        self.uniform_low = 0
        self.uniform_high = 0
        self.uniform_ssize = 0
        self.uniform_seed = 0

        self.triangular_left = 0
        self.triangular_right = 0
        self.triangular_mode = 0
        self.triangular_ssize = 0
        self.triangular_seed = 0

        self.normal_seed = 0
        self.normal_ssize = 0
        self.normal_stdev = 0

        self.exp_rate = 0.0
        self.exp_seed = 0
        self.exp_ssize = 0

        self.erlang_alpha = 0
        self.erlang_loc = 0
        self.erlang_scale = 0
        self.erlang_ssize = 0
        self.erlang_seed = 0

        self.gamma_alpha = 0.0
        self.gamma_scale = 0.0
        self.gamma_ssize = 0


        def uniform_tri_norm_exp_erlang_gamma_params():
            if uniform_low_field.get() != "":
                self.uniform_low = uniform_low_field.get()
            else:
                self.uniform_low = 0
            if uniform_high_field.get() != "":
                self.uniform_high = uniform_high_field.get()
            else:
                self.uniform_high = 100
            if uniform_ssize_field.get() != "":
                self.uniform_ssize = uniform_ssize_field.get()
            else:
                self.uniform_ssize = 2000
            if uniform_seed_field.get() != "":
                self.uniform_seed = uniform_seed_field.get()
            else:
                self.uniform_seed = 3307
            if triangular_left_field.get() != "":
                self.triangular_left = triangular_left_field.get()
            else:
                self.triangular_left = 40
            if triangular_right_field.get() != "":
                self.triangular_right = triangular_right_field.get()
            else:
                self.triangular_right = 100
            if triangular_mode_field.get() != "":
                self.triangular_mode = triangular_mode_field.get()
            else:
                self.triangular_mode = 75
            if triangular_ssize_field.get() != "":
                self.triangular_ssize = triangular_ssize_field.get()
            else:
                self.triangular_ssize = 2000
            if triangular_seed_field.get() != "":
                self.triangular_seed= triangular_seed_field.get()
            else:
                self.triangular_seed= 3307
            if normal_stdev_field.get() != "":
                self.normal_stdev = normal_stdev_field.get()
            else:
                self.normal_stdev = 25
            if normal_ssize_field.get() != "":
                self.normal_ssize = normal_ssize_field.get()
            else:
                self.normal_ssize = 2000
            if normal_seed_field.get() != "":
                self.normal_seed= normal_seed_field.get()
            else:
                self.normal_seed= 3307
            if exp_rate_field.get() != "":
                self.exp_rate = exp_rate_field.get()
            else:
                self.exp_rate = 1/25
            if exp_ssize_field.get() != "":
                self.exp_ssize = exp_ssize_field.get()
            else:
                self.exp_ssize = 2000
            if exp_seed_field.get() != "":
                self.exp_seed= exp_seed_field.get()
            else:
                self.exp_seed= 3307
            if erlang_alpha_field.get() != "":
                self.erlang_alpha = erlang_alpha_field.get()
            else:
                self.erlang_alpha = 3
            if erlang_loc_field.get() != "":
                self.erlang_loc= erlang_loc_field.get()
            else:
                self.erlang_loc= 0
            if erlang_scale_field.get() != "":
                self.erlang_scale = erlang_scale_field.get()
            else:
                self.erlang_scale = 25
            if erlang_ssize_field.get() != "":
                self.erlang_ssize = erlang_ssize_field.get()
            else:
                self.erlang_ssize = 2000
            if erlang_seed_field.get() != "":
                self.erlang_seed= erlang_seed_field.get()
            else:
                self.erlang_seed= 3307
            if gamma_alpha_field.get() != "":
                self.gamma_alpha = gamma_alpha_field.get()
            else:
                self.gamma_alpha = 3.0
            if gamma_scale_field.get() != "":
                self.gamma_scale = gamma_scale_field.get()
            else:
                self.gamma_scale = 6.0
            if gamma_ssize_field.get() != "":
                self.gamma_ssize= gamma_ssize_field.get()
            else:
                self.gamma_ssize= 2000

        string_var0 = tk.StringVar()  # tkinter requires text entry strings to be converted using the tk.StringVar method for them to be able to be passed to other functions
        string_var1 = tk.StringVar()
        string_var2 = tk.StringVar()
        string_var3 = tk.StringVar()
        string_var4= tk.StringVar()
        string_var5= tk.StringVar()
        string_var6= tk.StringVar()
        string_var7= tk.StringVar()
        string_var8= tk.StringVar()
        string_var9= tk.StringVar()
        string_var10= tk.StringVar()
        string_var11= tk.StringVar()
        string_var12= tk.StringVar()
        string_var13= tk.StringVar()
        string_var14= tk.StringVar()
        string_var15= tk.StringVar()
        string_var16= tk.StringVar()
        string_var17= tk.StringVar()
        string_var18= tk.StringVar()
        string_var19= tk.StringVar()
        string_var20= tk.StringVar()
        string_var21= tk.StringVar()
        string_var22= tk.StringVar()

        uniform_label_txt = tk.Label(self, text="Enter uniform distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))
        uniform_label_txt_default = tk.Label(self, text="(Leave field blank to accept [default] value)", anchor="center", justify="left", pady=0, font=("Courier", 12))

        uniform_low_field_txt = tk.Label(self, text="Low value [0]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_low_field = tk.Entry(self, textvariable=string_var0, width=5)
        uniform_high_field_txt = tk.Label(self, text="High value [100]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_high_field = tk.Entry(self, textvariable=string_var1, width=5)
        uniform_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_ssize_field = tk.Entry(self, textvariable=string_var2, width=5)
        uniform_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_seed_field = tk.Entry(self, textvariable=string_var3, width=5)


        triangular_label_txt = tk.Label(self, text="Enter triangular distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        triangular_left_field_txt = tk.Label(self, text="Left value [40]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_left_field = tk.Entry(self, textvariable=string_var4, width=5)
        triangular_right_field_txt = tk.Label(self, text="Right value [100]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_right_field = tk.Entry(self, textvariable=string_var5, width=5)
        triangular_mode_field_txt = tk.Label(self, text="Mode [75]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_mode_field = tk.Entry(self, textvariable=string_var6, width=5)
        triangular_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_ssize_field = tk.Entry(self, textvariable=string_var7, width=5)
        triangular_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_seed_field = tk.Entry(self, textvariable=string_var8, width=5)


        normal_label_txt = tk.Label(self, text="Enter normal distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        normal_stdev_field_txt = tk.Label(self, text="Standard deviation [25]: ", justify="left", pady=5, font=("Courier", 12))
        normal_stdev_field = tk.Entry(self, textvariable=string_var9, width=5)
        normal_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        normal_ssize_field = tk.Entry(self, textvariable=string_var10, width=5)
        normal_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        normal_seed_field = tk.Entry(self, textvariable=string_var11, width=5)


        exp_label_txt = tk.Label(self, text="Enter exponential distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        exp_rate_field_txt = tk.Label(self, text="Rate [1/25]: ", justify="left", pady=5, font=("Courier", 12))
        exp_rate_field = tk.Entry(self, textvariable=string_var12, width=5)
        exp_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        exp_ssize_field = tk.Entry(self, textvariable=string_var13, width=5)
        exp_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        exp_seed_field = tk.Entry(self, textvariable=string_var14, width=5)

        erlang_label_txt = tk.Label(self, text="Enter erlang distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        erlang_alpha_field_txt = tk.Label(self, text="Alpha value [3]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_alpha_field = tk.Entry(self, textvariable=string_var15, width=5)
        erlang_loc_field_txt = tk.Label(self, text="Loc value [0]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_loc_field = tk.Entry(self, textvariable=string_var16, width=5)
        erlang_scale_field_txt = tk.Label(self, text="Scale [25]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_scale_field = tk.Entry(self, textvariable=string_var17, width=5)
        erlang_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_ssize_field = tk.Entry(self, textvariable=string_var18, width=5)
        erlang_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_seed_field = tk.Entry(self, textvariable=string_var19, width=5)

        gamma_label_txt = tk.Label(self, text="Enter gamma distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        gamma_alpha_field_txt = tk.Label(self, text="Alpha [3.0]: ", justify="left", pady=5, font=("Courier", 12))
        gamma_alpha_field = tk.Entry(self, textvariable=string_var20, width=5)
        gamma_scale_field_txt = tk.Label(self, text="Scale [6.0]: ", justify="left", pady=5, font=("Courier", 12))
        gamma_scale_field = tk.Entry(self, textvariable=string_var21, width=5)
        gamma_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        gamma_ssize_field = tk.Entry(self, textvariable=string_var22, width=5)



        uniform_label_txt.grid(row=0, column=0, padx=10, pady=0, sticky="nw")
        uniform_label_txt_default.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        blank_space = tk.Label(self, text="", pady=15)
        blank_space.grid(row=2, column=0)

        uniform_low_field_txt.grid(row= 3, column= 0, sticky= "e")
        uniform_low_field.grid(row= 3, column= 1, sticky= "w")
        uniform_high_field_txt.grid(row= 4, column= 0, sticky= "e")
        uniform_high_field.grid(row= 4, column= 1, sticky= "w")
        uniform_ssize_field_txt.grid(row= 5, column= 0, sticky= "e")
        uniform_ssize_field.grid(row= 5, column= 1, sticky= "w")
        uniform_seed_field_txt.grid(row= 6, column= 0, sticky= "e")
        uniform_seed_field.grid(row= 6, column= 1, sticky= "w")

        blank_space2 = tk.Label(self, text="", pady=15)
        blank_space2.grid(row= 7, column=0)

        triangular_label_txt.grid(row=8, column=0, padx=10, pady=0, sticky="nw")

        triangular_left_field_txt.grid(row= 9, column= 0, sticky= "e")
        triangular_left_field.grid(row= 9, column= 1, sticky= "w")
        triangular_right_field_txt.grid(row= 10, column= 0, sticky= "e")
        triangular_right_field.grid(row= 10, column= 1, sticky= "w")
        triangular_mode_field_txt.grid(row= 11, column= 0, sticky= "e")
        triangular_mode_field.grid(row= 11, column= 1, sticky= "w")
        triangular_ssize_field_txt.grid(row= 12, column= 0, sticky= "e")
        triangular_ssize_field.grid(row= 12, column= 1, sticky= "w")
        triangular_seed_field_txt.grid(row= 13, column= 0, sticky= "e")
        triangular_seed_field.grid(row= 13, column= 1, sticky= "w")

        blank_space3 = tk.Label(self, text="", pady=15)
        blank_space3.grid(row=14, column=0)

        normal_label_txt.grid(row=15, column=0, padx=10, pady=0, sticky="nw")

        normal_stdev_field_txt.grid(row=16, column=0, sticky="e")
        normal_stdev_field.grid(row=16, column=1, sticky="w")
        normal_ssize_field_txt.grid(row=17, column=0, sticky="e")
        normal_ssize_field.grid(row=17, column=1, sticky="w")
        normal_seed_field_txt.grid(row=18, column=0, sticky="e")
        normal_seed_field.grid(row=18, column=1, sticky="w")

        blank_space4 = tk.Label(self, text="", pady=15)
        blank_space4.grid(row=19, column=0)

        exp_label_txt.grid(row=20, column=0, padx=10, pady=0, sticky="nw")

        exp_rate_field_txt.grid(row=21, column=0, sticky="e")
        exp_rate_field.grid(row=21, column=1, sticky="w")
        exp_ssize_field_txt.grid(row=22, column=0, sticky="e")
        exp_ssize_field.grid(row=22, column=1, sticky="w")
        exp_seed_field_txt.grid(row=23, column=0, sticky="e")
        exp_seed_field.grid(row=23, column=1, sticky="w")

        blank_space5 = tk.Label(self, text="", pady=15)
        blank_space5.grid(row= 24, column=0)

        erlang_label_txt.grid(row=0, column=2, padx=10, pady=0, sticky="nw")

        erlang_alpha_field_txt.grid(row= 1, column= 2, sticky= "e")
        erlang_alpha_field.grid(row= 1, column= 3, sticky= "w")
        erlang_loc_field_txt.grid(row= 2, column= 2, sticky= "e")
        erlang_loc_field.grid(row= 2, column= 3, sticky= "w")
        erlang_scale_field_txt.grid(row= 3, column= 2, sticky= "e")
        erlang_scale_field.grid(row= 3, column= 3, sticky= "w")
        erlang_ssize_field_txt.grid(row= 4, column= 2, sticky= "e")
        erlang_ssize_field.grid(row= 4, column= 3, sticky= "w")
        erlang_seed_field_txt.grid(row= 5, column= 2, sticky= "e")
        erlang_seed_field.grid(row= 5, column= 3, sticky= "w")

        blank_space6 = tk.Label(self, text="", pady=15)
        blank_space6.grid(row=6, column=2)

        gamma_label_txt.grid(row=7, column=2, padx=10, pady=0, sticky="nw")

        gamma_alpha_field_txt.grid(row=8, column=2, sticky="e")
        gamma_alpha_field.grid(row=8, column=3, sticky="w")
        gamma_scale_field_txt.grid(row=9, column=2, sticky="e")
        gamma_scale_field.grid(row=9, column=3, sticky="w")
        gamma_ssize_field_txt.grid(row=10, column=2, sticky="e")
        gamma_ssize_field.grid(row=10, column=3, sticky="w")


        go_button = tk.Button(self, text="Go", font= ("Courier", 50), fg="green", command=uniform_tri_norm_exp_erlang_gamma_params)
        back_button = tk.Button(self, text="Cancel", font=("Courier", 50), command=lambda: controller.show_frame(StartWindow))
        go_button.grid(row=25, column=1, sticky="w")
        back_button.grid(row= 25, column= 2, sticky= "e")






class ParamUniformTriangularNormalExponentialErlangGammaWeibull(tk.Frame):


    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)


        self.uniform_low = 0
        self.uniform_high = 0
        self.uniform_ssize = 0
        self.uniform_seed = 0

        self.triangular_left = 0
        self.triangular_right = 0
        self.triangular_mode = 0
        self.triangular_ssize = 0
        self.triangular_seed = 0

        self.normal_seed = 0
        self.normal_ssize = 0
        self.normal_stdev = 0

        self.exp_rate = 0.0
        self.exp_seed = 0
        self.exp_ssize = 0

        self.erlang_alpha = 0
        self.erlang_loc = 0
        self.erlang_scale = 0
        self.erlang_ssize = 0
        self.erlang_seed = 0

        self.gamma_alpha = 0.0
        self.gamma_scale = 0.0
        self.gamma_ssize = 0

        self.weibull_alpha = 0.0
        self.weibull_ssize = 0


        def uniform_tri_norm_exp_erlang_gamma_weibull_params():
            if uniform_low_field.get() != "":
                self.uniform_low = uniform_low_field.get()
            else:
                self.uniform_low = 0
            if uniform_high_field.get() != "":
                self.uniform_high = uniform_high_field.get()
            else:
                self.uniform_high = 100
            if uniform_ssize_field.get() != "":
                self.uniform_ssize = uniform_ssize_field.get()
            else:
                self.uniform_ssize = 2000
            if uniform_seed_field.get() != "":
                self.uniform_seed = uniform_seed_field.get()
            else:
                self.uniform_seed = 3307
            if triangular_left_field.get() != "":
                self.triangular_left = triangular_left_field.get()
            else:
                self.triangular_left = 40
            if triangular_right_field.get() != "":
                self.triangular_right = triangular_right_field.get()
            else:
                self.triangular_right = 100
            if triangular_mode_field.get() != "":
                self.triangular_mode = triangular_mode_field.get()
            else:
                self.triangular_mode = 75
            if triangular_ssize_field.get() != "":
                self.triangular_ssize = triangular_ssize_field.get()
            else:
                self.triangular_ssize = 2000
            if triangular_seed_field.get() != "":
                self.triangular_seed= triangular_seed_field.get()
            else:
                self.triangular_seed= 3307
            if normal_stdev_field.get() != "":
                self.normal_stdev = normal_stdev_field.get()
            else:
                self.normal_stdev = 25
            if normal_ssize_field.get() != "":
                self.normal_ssize = normal_ssize_field.get()
            else:
                self.normal_ssize = 2000
            if normal_seed_field.get() != "":
                self.normal_seed= normal_seed_field.get()
            else:
                self.normal_seed= 3307
            if exp_rate_field.get() != "":
                self.exp_rate = exp_rate_field.get()
            else:
                self.exp_rate = 1/25
            if exp_ssize_field.get() != "":
                self.exp_ssize = exp_ssize_field.get()
            else:
                self.exp_ssize = 2000
            if exp_seed_field.get() != "":
                self.exp_seed= exp_seed_field.get()
            else:
                self.exp_seed= 3307
            if erlang_alpha_field.get() != "":
                self.erlang_alpha = erlang_alpha_field.get()
            else:
                self.erlang_alpha = 3
            if erlang_loc_field.get() != "":
                self.erlang_loc= erlang_loc_field.get()
            else:
                self.erlang_loc= 0
            if erlang_scale_field.get() != "":
                self.erlang_scale = erlang_scale_field.get()
            else:
                self.erlang_scale = 25
            if erlang_ssize_field.get() != "":
                self.erlang_ssize = erlang_ssize_field.get()
            else:
                self.erlang_ssize = 2000
            if erlang_seed_field.get() != "":
                self.erlang_seed= erlang_seed_field.get()
            else:
                self.erlang_seed= 3307
            if gamma_alpha_field.get() != "":
                self.gamma_alpha = gamma_alpha_field.get()
            else:
                self.gamma_alpha = 3.0
            if gamma_scale_field.get() != "":
                self.gamma_scale = gamma_scale_field.get()
            else:
                self.gamma_scale = 6.0
            if gamma_ssize_field.get() != "":
                self.gamma_ssize= gamma_ssize_field.get()
            else:
                self.gamma_ssize= 2000
            if weibull_alpha_field.get() != "":
                self.weibull_alpha = weibull_alpha_field.get()
            else:
                self.weibull_alpha = 5.0
            if weibull_ssize_field.get() != "":
                self.weibull_ssize= weibull_ssize_field.get()
            else:
                self.weibull_ssize= 2000


        string_var0 = tk.StringVar()  # tkinter requires text entry strings to be converted using the tk.StringVar method for them to be able to be passed to other functions
        string_var1 = tk.StringVar()
        string_var2 = tk.StringVar()
        string_var3 = tk.StringVar()
        string_var4= tk.StringVar()
        string_var5= tk.StringVar()
        string_var6= tk.StringVar()
        string_var7= tk.StringVar()
        string_var8= tk.StringVar()
        string_var9= tk.StringVar()
        string_var10= tk.StringVar()
        string_var11= tk.StringVar()
        string_var12= tk.StringVar()
        string_var13= tk.StringVar()
        string_var14= tk.StringVar()
        string_var15= tk.StringVar()
        string_var16= tk.StringVar()
        string_var17= tk.StringVar()
        string_var18= tk.StringVar()
        string_var19= tk.StringVar()
        string_var20= tk.StringVar()
        string_var21= tk.StringVar()
        string_var22= tk.StringVar()
        string_var23= tk.StringVar()
        string_var24= tk.StringVar()

        uniform_label_txt = tk.Label(self, text="Enter uniform distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))
        uniform_label_txt_default = tk.Label(self, text="(Leave field blank to accept [default] value)", anchor="center", justify="left", pady=0, font=("Courier", 12))

        uniform_low_field_txt = tk.Label(self, text="Low value [0]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_low_field = tk.Entry(self, textvariable=string_var0, width=5)
        uniform_high_field_txt = tk.Label(self, text="High value [100]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_high_field = tk.Entry(self, textvariable=string_var1, width=5)
        uniform_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_ssize_field = tk.Entry(self, textvariable=string_var2, width=5)
        uniform_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        uniform_seed_field = tk.Entry(self, textvariable=string_var3, width=5)


        triangular_label_txt = tk.Label(self, text="Enter triangular distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        triangular_left_field_txt = tk.Label(self, text="Left value [40]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_left_field = tk.Entry(self, textvariable=string_var4, width=5)
        triangular_right_field_txt = tk.Label(self, text="Right value [100]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_right_field = tk.Entry(self, textvariable=string_var5, width=5)
        triangular_mode_field_txt = tk.Label(self, text="Mode [75]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_mode_field = tk.Entry(self, textvariable=string_var6, width=5)
        triangular_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_ssize_field = tk.Entry(self, textvariable=string_var7, width=5)
        triangular_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        triangular_seed_field = tk.Entry(self, textvariable=string_var8, width=5)


        normal_label_txt = tk.Label(self, text="Enter normal distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        normal_stdev_field_txt = tk.Label(self, text="Standard deviation [25]: ", justify="left", pady=5, font=("Courier", 12))
        normal_stdev_field = tk.Entry(self, textvariable=string_var9, width=5)
        normal_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        normal_ssize_field = tk.Entry(self, textvariable=string_var10, width=5)
        normal_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        normal_seed_field = tk.Entry(self, textvariable=string_var11, width=5)


        exp_label_txt = tk.Label(self, text="Enter exponential distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        exp_rate_field_txt = tk.Label(self, text="Rate [1/25]: ", justify="left", pady=5, font=("Courier", 12))
        exp_rate_field = tk.Entry(self, textvariable=string_var12, width=5)
        exp_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        exp_ssize_field = tk.Entry(self, textvariable=string_var13, width=5)
        exp_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        exp_seed_field = tk.Entry(self, textvariable=string_var14, width=5)

        erlang_label_txt = tk.Label(self, text="Enter erlang distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        erlang_alpha_field_txt = tk.Label(self, text="Alpha value [3]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_alpha_field = tk.Entry(self, textvariable=string_var15, width=5)
        erlang_loc_field_txt = tk.Label(self, text="Loc value [0]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_loc_field = tk.Entry(self, textvariable=string_var16, width=5)
        erlang_scale_field_txt = tk.Label(self, text="Scale [25]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_scale_field = tk.Entry(self, textvariable=string_var17, width=5)
        erlang_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_ssize_field = tk.Entry(self, textvariable=string_var18, width=5)
        erlang_seed_field_txt = tk.Label(self, text="Random seed value [3307]: ", justify="left", pady=5, font=("Courier", 12))
        erlang_seed_field = tk.Entry(self, textvariable=string_var19, width=5)

        gamma_label_txt = tk.Label(self, text="Enter gamma distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        gamma_alpha_field_txt = tk.Label(self, text="Alpha [3.0]: ", justify="left", pady=5, font=("Courier", 12))
        gamma_alpha_field = tk.Entry(self, textvariable=string_var20, width=5)
        gamma_scale_field_txt = tk.Label(self, text="Scale [6.0]: ", justify="left", pady=5, font=("Courier", 12))
        gamma_scale_field = tk.Entry(self, textvariable=string_var21, width=5)
        gamma_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        gamma_ssize_field = tk.Entry(self, textvariable=string_var22, width=5)

        weibull_label_txt = tk.Label(self, text="Enter weibull distribution parameters: ", anchor="center", justify="left", pady=0, font=("Courier", 18))

        weibull_alpha_field_txt = tk.Label(self, text="Alpha [5.0]: ", justify="left", pady=5, font=("Courier", 12))
        weibull_alpha_field = tk.Entry(self, textvariable=string_var23, width=5)
        weibull_ssize_field_txt = tk.Label(self, text="Sample size [2000]: ", justify="left", pady=5, font=("Courier", 12))
        weibull_ssize_field = tk.Entry(self, textvariable=string_var24, width=5)



        uniform_label_txt.grid(row=0, column=0, padx=10, pady=0, sticky="nw")
        uniform_label_txt_default.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        blank_space = tk.Label(self, text="", pady=15)
        blank_space.grid(row=2, column=0)

        uniform_low_field_txt.grid(row= 3, column= 0, sticky= "e")
        uniform_low_field.grid(row= 3, column= 1, sticky= "w")
        uniform_high_field_txt.grid(row= 4, column= 0, sticky= "e")
        uniform_high_field.grid(row= 4, column= 1, sticky= "w")
        uniform_ssize_field_txt.grid(row= 5, column= 0, sticky= "e")
        uniform_ssize_field.grid(row= 5, column= 1, sticky= "w")
        uniform_seed_field_txt.grid(row= 6, column= 0, sticky= "e")
        uniform_seed_field.grid(row= 6, column= 1, sticky= "w")

        blank_space2 = tk.Label(self, text="", pady=15)
        blank_space2.grid(row= 7, column=0)

        triangular_label_txt.grid(row=8, column=0, padx=10, pady=0, sticky="nw")

        triangular_left_field_txt.grid(row= 9, column= 0, sticky= "e")
        triangular_left_field.grid(row= 9, column= 1, sticky= "w")
        triangular_right_field_txt.grid(row= 10, column= 0, sticky= "e")
        triangular_right_field.grid(row= 10, column= 1, sticky= "w")
        triangular_mode_field_txt.grid(row= 11, column= 0, sticky= "e")
        triangular_mode_field.grid(row= 11, column= 1, sticky= "w")
        triangular_ssize_field_txt.grid(row= 12, column= 0, sticky= "e")
        triangular_ssize_field.grid(row= 12, column= 1, sticky= "w")
        triangular_seed_field_txt.grid(row= 13, column= 0, sticky= "e")
        triangular_seed_field.grid(row= 13, column= 1, sticky= "w")

        blank_space3 = tk.Label(self, text="", pady=15)
        blank_space3.grid(row=14, column=0)

        normal_label_txt.grid(row=15, column=0, padx=10, pady=0, sticky="nw")

        normal_stdev_field_txt.grid(row=16, column=0, sticky="e")
        normal_stdev_field.grid(row=16, column=1, sticky="w")
        normal_ssize_field_txt.grid(row=17, column=0, sticky="e")
        normal_ssize_field.grid(row=17, column=1, sticky="w")
        normal_seed_field_txt.grid(row=18, column=0, sticky="e")
        normal_seed_field.grid(row=18, column=1, sticky="w")

        blank_space4 = tk.Label(self, text="", pady=15)
        blank_space4.grid(row=19, column=0)

        exp_label_txt.grid(row=20, column=0, padx=10, pady=0, sticky="nw")

        exp_rate_field_txt.grid(row=21, column=0, sticky="e")
        exp_rate_field.grid(row=21, column=1, sticky="w")
        exp_ssize_field_txt.grid(row=22, column=0, sticky="e")
        exp_ssize_field.grid(row=22, column=1, sticky="w")
        exp_seed_field_txt.grid(row=23, column=0, sticky="e")
        exp_seed_field.grid(row=23, column=1, sticky="w")

        blank_space5 = tk.Label(self, text="", pady=15)
        blank_space5.grid(row= 24, column=0)

        erlang_label_txt.grid(row=0, column=2, padx=10, pady=0, sticky="nw")

        erlang_alpha_field_txt.grid(row= 1, column= 2, sticky= "e")
        erlang_alpha_field.grid(row= 1, column= 3, sticky= "w")
        erlang_loc_field_txt.grid(row= 2, column= 2, sticky= "e")
        erlang_loc_field.grid(row= 2, column= 3, sticky= "w")
        erlang_scale_field_txt.grid(row= 3, column= 2, sticky= "e")
        erlang_scale_field.grid(row= 3, column= 3, sticky= "w")
        erlang_ssize_field_txt.grid(row= 4, column= 2, sticky= "e")
        erlang_ssize_field.grid(row= 4, column= 3, sticky= "w")
        erlang_seed_field_txt.grid(row= 5, column= 2, sticky= "e")
        erlang_seed_field.grid(row= 5, column= 3, sticky= "w")

        blank_space6 = tk.Label(self, text="", pady=15)
        blank_space6.grid(row=6, column=2)

        gamma_label_txt.grid(row=7, column=2, padx=10, pady=0, sticky="nw")

        gamma_alpha_field_txt.grid(row=8, column=2, sticky="e")
        gamma_alpha_field.grid(row=8, column=3, sticky="w")
        gamma_scale_field_txt.grid(row=9, column=2, sticky="e")
        gamma_scale_field.grid(row=9, column=3, sticky="w")
        gamma_ssize_field_txt.grid(row=10, column=2, sticky="e")
        gamma_ssize_field.grid(row=10, column=3, sticky="w")

        blank_space7 = tk.Label(self, text="", pady=15)
        blank_space7.grid(row=11, column=2)

        weibull_label_txt.grid(row=12, column=2, padx=10, pady=0, sticky="nw")

        weibull_alpha_field_txt.grid(row=13, column=2, sticky="e")
        weibull_alpha_field.grid(row=13, column=3, sticky="w")
        weibull_ssize_field_txt.grid(row=14, column=2, sticky="e")
        weibull_ssize_field.grid(row=14, column=3, sticky="w")


        go_button = tk.Button(self, text="OK", font= ("Courier", 50), fg="green", command=uniform_tri_norm_exp_erlang_gamma_weibull_params)
        back_button = tk.Button(self, text="Cancel", font=("Courier", 50), command=lambda: controller.show_frame(StartWindow))
        go_button.grid(row=25, column=1, sticky="w")
        back_button.grid(row=25, column=2, sticky="e")


dist_instances= ParamUniformTriangularNormalExponentialErlangGammaWeibull(parent= Distapp, controller= Distapp.show_frame)


class GraphWindow(tk.Frame):

    def __init__(self, parent, controller):



        tk.Frame.__init__(self, parent)

        gamma_ssize2= ParamUniformTriangularNormalExponentialErlangGammaWeibull()

        label_txt= tk.Label(self, text="Histogram", anchor="center", justify="left", pady=30, font=("Courier", 18))
        label_txt.grid(row= 0, column= 0, pady= 10, padx= 10)

        print(dist_instances.gamma_ssize)



app= Distapp()      # "app" is an object instance of the Distapp class

app.mainloop()
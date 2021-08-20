# Dependencies
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import transforms
import os
import nibabel as nib
import glob
import pickle
from cc_excel_readwrite import *
import matplotlib as mpl
from PIL import Image, ImageTk


# Creating the TK window
root = tk.Tk()
root.geometry("")
# Index of path list
global list_index
list_index = 0

# Running variable
global running
running = False

# Customize Popup Window
def customize_vis():
    window = tk.Toplevel()
    
    # Quit/Apply Changes
    def apply_changes():
        # Add custom excel file name for data collection
        try:   
            global custom_excel_file_name
            custom_excel_file_name = excel_file_entry.get()
            excel_name_var.set("Excel sheet: "+ custom_excel_file_name)
            excel_table_string.set(view_excel(custom_excel_file_name))
        except:
            print("Excel file not found")

        # Add custom abnormality buttons
        try:
            global custom_abnormality_list
            custom_abnormality_list = abnormality_entry.get().split(";")
            global num_custom_abnormalities
            print(custom_abnormality_list)
            if custom_abnormality_list[0] == "":
                print("no buttons detected")
            else:
                num_custom_abnormalities = len(custom_abnormality_list)
                for item_index, list_item in enumerate(custom_abnormality_list):
                    button = tk.Button(root, text = list_item, command = lambda list_item=list_item:addData(list_item), fg = "black")
                    button.grid(row = item_index + 12, column = 12, sticky = 'nsew')
        except:
            print("Error in Abnormality Button Addition")

        # Add An Existing Pickle File
        try:
            global cc_list
            with open (base_pickle_entry.get(), 'rb') as filehandle:
                cc_list = pickle.load(filehandle)
            print("Added " + base_pickle_entry.get())
        except:
            print("No Pickle List Found")

        #Add file path to images using Pickle
        try:
            file_counter = 0
            cc_files = []
            for filename in glob.iglob(path_entry.get(), recursive = True):
                cc_files.append(filename)
                cc_files.sort()
                file_counter = file_counter + 1
                print("Adding path: " + filename)
                print("On file # " + str(file_counter))
            with open ('custom.pkl', 'wb') as filehandle:
                pickle.dump(cc_files, filehandle)
        except:
            print("File path invalid")    
        window.destroy()

    # Instructuions, title
    header = tk.Label(window, text = "Customize the program", fg = 'black')

    # Entries
    excel_title_label = tk.Label(window, text = "Excel Sheet Path:", fg = 'black')
    excel_file_entry = tk.Entry(window, width = 20)

    abnormality_label = tk.Label(window, text = "Custom Abnormality Buttons:", fg = 'black')
    abnormality_entry = tk.Entry(window, width = 50)
    
    base_pickle_label = tk.Label(window, text = "Base Image Pickle Path:", fg = 'black')
    base_pickle_entry = tk.Entry(window, width = 50)

    path_entry = tk.Entry(window, width = 50)
    path_title = tk.Label(window, text = "Generate Pickle with Path:", fg = 'black')

    customize_close = tk.Button(window, text = "Apply Changes", command = apply_changes, fg = "black")
    
    #Packing
    header.grid(row = 0, column = 0, sticky = 'nsew')

    excel_title_label.grid(row = 1, column = 0, sticky = 'nsew')
    excel_file_entry.grid(row = 1, column = 1, sticky = 'nsew')

    abnormality_label.grid(row = 2, column = 0, sticky = 'nsew')
    abnormality_entry.grid(row = 2, column = 1, sticky = 'nsew')

    base_pickle_label.grid(row = 3, column = 0, sticky = 'nsew')
    base_pickle_entry.grid(row = 3, column = 1, sticky = 'nsew')

    path_title.grid(row = 5, column = 0, sticky = 'nsew')
    path_entry.grid(row = 5, column = 1, sticky = 'nsew')

    
    customize_close.grid(row = 6, column = 0, sticky = 'nsew')



# Excel Table Preview Labels
excel_table_string = tk.StringVar(root, "Excel Sheet Will Appear Here")
excel_table = tk.Label(root, textvariable = excel_table_string, fg = 'black', wraplength = 200)

excel_name_var = tk.StringVar(root)
excel_name_var.set("Excel Sheet: ")
excel_file_label = tk.Label(root, textvariable = excel_name_var, fg = 'black')


# ------------------------
# Main Console
# ------------------------

# Current File Path Label
path_string = tk.StringVar(root)
current_path_label = tk.Entry(root, textvariable = path_string, fg = 'black', state="readonly")
path_string.set("---------------File Path will appear here---------------")

# Mask Label
mask_path_string = tk.StringVar(root)

# Current Image Index label
index_string = tk.StringVar(root)
current_index = tk.Label(root, textvariable=index_string, fg = 'black')
index_string.set("Current image: "+ str(list_index))



# Sets index of path list from user input
def set_image():
    figplot.cla()
    global list_index
    # Create base image
    list_index = int(set_image_entry.get())
    path_string.set(cc_list[list_index])
    index_string.set("Current image: "+ str(list_index))
    if base_checkbox_var.get() == 1:
        # path_string.set(path_string.get()[:-10] + ".nii.gz")
        extract_slice_tk(alpha_opacity = float(image_opacity.get()), image_path = path_string.get())
    # Add mask string, delete last four letters then add "_cc.nii.gz"
    if mask_checkbox_var.get() == 1:
        mask_path_string.set(path_string.get()[:-7] + "_cc.nii.gz")
        extract_slice_tk(alpha_opacity = float(mask_opacity.get()), image_path = mask_path_string.get())
    canvas.draw()

def go_to_path():
    figplot.cla()
    global list_index
    # Create base image
    path_string.set(set_path_entry.get())
    if base_checkbox_var.get() == 1:
        # path_string.set(path_string.get()[:-10] + ".nii.gz")
        extract_slice_tk(alpha_opacity = float(image_opacity.get()), image_path = path_string.get())
    # Add mask string, delete last four letters then add "_cc.nii.gz"
    if mask_checkbox_var.get() == 1:
        mask_path_string.set(path_string.get()[:-7] + "_cc.nii.gz")
        extract_slice_tk(alpha_opacity = float(mask_opacity.get()), image_path = mask_path_string.get())
    canvas.draw()

# Go to image # button
set_image_button = tk.Button(
    root,
    text="Go To #:",
    width = 5,
    height = 1,
    command = set_image,
    fg = "black")

# Entry for Set Image
set_image_entry = tk.Entry(root, width = 5)

# Go to image path button
set_path_button = tk.Button(
    root,
    text="Go To Path",
    width = 5,
    height = 1,
    command = go_to_path,
    fg = "black")

# Entry for path
set_path_entry = tk.Entry(root, width = 5)


# Running status
running_status = tk.StringVar(root)
running_label = tk.Label(root, textvariable = running_status, fg = 'black')
running_status.set("Running Status: Paused")

# Pause/play functions
def play():
    global running
    running = True
    running_status.set("Running Status: Running")

def pause(event = None):
    global running
    running = False
    running_status.set("Running Status: Paused")

# Pause, play, exit buttons
pause_button = tk.Button(root, text = 'Pause', command = pause, fg = "black")

play_button = tk.Button(root, text = 'Play', command = play, fg = "black")

def window_close():
    root.quit()
    root.destroy()

exit_button = tk.Button(root, text="Quit", width = 5, height = 1, command = window_close, fg = "black")

# Customize button
customize_button = tk.Button(root, text = "Customize", command = customize_vis, fg = "black")

# Image Loading Status
loading_status = tk.StringVar(root)
loading_label = tk.Label(root, textvariable = loading_status, bg = "white", fg = 'green')
loading_status.set("Image Loaded!")


# ---------------
# Plotting
# ---------------

# Create figure, and draw a blank canvas
fig = plt.figure(figsize=(8,6),dpi=100)
canvas = FigureCanvasTkAgg(fig, master = root)
canvas.draw()
figplot = fig.add_subplot(111)

# Plot Midslice
# default -90
# rotate 90 degrees clockwise is 0
# rotate 180 degrees clockwise is 90
# rotate 270 degrees clockwise is 180


def extract_slice_tk(alpha_opacity, image_path):
    global hdr
    global img_data
    # Use Nibabel to load image and get the midslice
    hdr = nib.load(image_path)
    img_data = hdr.get_fdata()
    midslice = img_data[midslice_value.get(),:,:]
    # Rotate the Image
    figplot.set_xlim([0, 250])
    tr = transforms.Affine2D().rotate_deg_around(100, 100, rotation_angle.get(),)
    
    show_fig = figplot.imshow(midslice, transform = tr + figplot.transData, cmap = "Greys_r", alpha = alpha_opacity)
    # Place figure onto canvas

# Duo function used in image opacity buttons mainly used to change opacities
def extract_two_slices():
    loading_status.set("Loading...")
    loading_label.config(fg = "red")
    figplot.cla()
    if base_checkbox_var.get() == 1:
        extract_slice_tk(alpha_opacity = float(image_opacity.get()), image_path = path_string.get())
    if mask_checkbox_var.get() == 1:
        mask_path_string.set(path_string.get()[:-7] + "_cc.nii.gz")
        extract_slice_tk(alpha_opacity = float(mask_opacity.get()), image_path = mask_path_string.get())
    canvas.draw()
    loading_status.set("Image Loaded!")
    loading_label.config(fg = "green")


def update_plot():
    figplot.cla()
    global list_index
    # Create base image
    path_string.set(cc_list[list_index])
    index_string.set("Current image: "+ str(list_index))
    if base_checkbox_var.get() == 1:
        # path_string.set(path_string.get()[:-10] + ".nii.gz")
        extract_slice_tk(alpha_opacity = float(image_opacity.get()), image_path = path_string.get())
   # Add mask string, delete last four letters then add "_cc.nii.gz"
    if mask_checkbox_var.get() == 1:
        mask_path_string.set(path_string.get()[:-7] + "_cc.nii.gz")
        extract_slice_tk(alpha_opacity = float(mask_opacity.get()), image_path = mask_path_string.get())
    canvas.draw()

def loop_images():
    figplot.cla()
    global list_index
    if running:
        loading_status.set("Loading...")
        loading_label.config(fg = "red")
        root.update()
        # Create base image
        list_index = list_index + 1
        path_string.set(cc_list[list_index])
        index_string.set("Current image: "+ str(list_index))
        if base_checkbox_var.get() == 1:
            # path_string.set(path_string.get()[:-10] + ".nii.gz")
            extract_slice_tk(alpha_opacity = float(image_opacity.get()), image_path = path_string.get())
        # Add mask string, delete last four letters then add "_cc.nii.gz"
        if mask_checkbox_var.get() == 1:
            mask_path_string.set(path_string.get()[:-7] + "_cc.nii.gz")
            extract_slice_tk(alpha_opacity = float(mask_opacity.get()), image_path = mask_path_string.get())
        canvas.draw()
        loading_status.set("Image Loaded!")
        loading_label.config(fg = "green")
        root.update()
        root.after(3000, loop_images)

def next_image():
    global list_index
    loading_status.set("Loading...")
    loading_label.config(fg = "red")
    root.update()
    list_index = list_index + 1
    update_plot()
    loading_status.set("Image Loaded!")
    loading_label.config(fg = "green")

    
def previous_image():
    global list_index
    loading_status.set("Loading...")
    loading_label.config(fg = "red")
    root.update()
    list_index = list_index - 1
    update_plot()
    loading_status.set("Image Loaded!")
    loading_label.config(fg = "green")


def plot_midslice():
    figplot.cla()
    global list_index
    # Create base image
    path_string.set(cc_list[list_index])
    index_string.set("Current image: "+ str(list_index))
    # make mask checkbox empty and base checkbox filled
    if mask_checkbox_var.get() == 1:
        mask_checkbox_var.set(0)
        extract_slice_tk(alpha_opacity = float(image_opacity.get()), image_path = path_string.get())
        canvas.draw()
    else:
        base_checkbox_var.set(1)
        midslice = img_data[midslice_value.get(),:,:]
        # Rotate the Image
        figplot.set_xlim([0, 250])
        tr = transforms.Affine2D().rotate_deg_around(100, 100, rotation_angle.get(),)
        show_fig = figplot.imshow(midslice, transform = tr + figplot.transData, cmap = "Greys_r", alpha = image_opacity.get())
    # extract_slice_tk(alpha_opacity = float(image_opacity.get()), image_path = path_string.get())
        canvas.draw()

# Next/Previous image buttons
next_image_button = tk.Button(root, text = "Next Image", command = next_image, fg = "black")
previous_image_button = tk.Button(root, text = "Previous Image", command = previous_image, fg = "black")

# Set Rotation angles
rotation_angle = tk.IntVar(root, -90)

def rotate_right():
    rotation_angle.set(rotation_angle.get()+90)
    update_plot()

def rotate_left():
    rotation_angle.set(rotation_angle.get()-90)
    update_plot()

left_open = Image.open("r_left.png")
right_open = Image.open("r_right.png")

left_image = ImageTk.PhotoImage(left_open)
right_image = ImageTk.PhotoImage(right_open)

rotate_right_button = tk.Button(root, 
    image = right_image,
    command = lambda: rotate_right(),
    fg = "black")

rotate_left_button = tk.Button(root,
    image = left_image,
    command = lambda: rotate_left(),
    fg = "black")

# -----------
# Hotkeys
# -----------

root.bind("<space>", pause)

# Show/hide mask/base image checkboxes
mask_checkbox_var = tk.IntVar(root, 1)
base_checkbox_var = tk.IntVar(root, 1)
mask_checkbox = tk.Checkbutton(root, variable = mask_checkbox_var, command = extract_two_slices)
base_checkbox = tk.Checkbutton(root, variable = base_checkbox_var, command = extract_two_slices)

# Change image 1's opacity
image_opacity = tk.DoubleVar(root, 0.8)
mask_opacity = tk.DoubleVar(root, 0.5)

# Change current image's midslice
change_midslice_label = tk.Label(root, text = "Set midslice:", fg = 'black')
midslice_value = tk.IntVar(root, 89)
change_midslice_spinbox = tk.Spinbox(root, from_ = 0, to = 200, 
    textvariable = midslice_value, 
    width = 3,
    command = lambda: plot_midslice())

# Change opacity spinboxes
change_base_opacity_label = tk.Label(root, text = "Set Base Opacity:", fg = 'black')
change_base_opacity_spinbox = tk.Spinbox(root, from_ = 0, to = 1.0, 
    increment = 0.1,
    textvariable = image_opacity, 
    width = 3,
    command = extract_two_slices)

change_mask_opacity_label = tk.Label(root, text = "Set Mask Opacity:", fg = 'black')
change_mask_opacity_spinbox = tk.Spinbox(root, from_ = 0, to = 1.0, 
    increment = 0.1,
    textvariable = mask_opacity, 
    width = 3,
    command = extract_two_slices)

loop_images_button = tk.Button(
    root, 
    text = "loop images",
    command = loop_images,
    fg = "black"
)

# Show recently added data (into excel) to user
added_data_string = tk.StringVar(root)
added_data_string.set("---Abnormality will appear here---")
added_data_label = tk.Label(root, textvariable = added_data_string, fg = 'black')

# ----------------
# Abnormalities
# ----------------
# Text box to add abnormalities
abnormalities_label = tk.Label(root, text="Describe the abnormality here:", fg = 'black')
abnormalities_entry = tk.Entry(root, width = 50)

# Adds data from current path and abnormality in text box
def addData(ab_text):
    global list_index
    add_row(str(cc_list[list_index]), ab_text, list_index, custom_excel_file_name)
    added_data_string.set(ab_text)
    #Adding Data also refreshes excel preview:
    excel_table_string.set(view_excel(custom_excel_file_name))

# Default add data
add_data_button = tk.Button(
    root, 
    text = "Add Data to Spreadsheet", 
    command = lambda: addData(abnormalities_entry.get()),
    fg = "black"
    )
artifact_preset_button = tk.Button(
    root, 
    text = "Add Artifact Abnormality",
    command = lambda: addData("Artifact error"),
    fg = "black"
)
registration_preset_button = tk.Button(
    root, 
    text = "Add Registration Abnormality",
    command = lambda: addData("Registration error"),
    fg = "black"
)
hypo_preset_button = tk.Button(
    root, 
    text = "Add Hypoplasia Abnormality",
    command = lambda: addData("Hypoplasia"),
    fg = "black"
)
hump_preset_button = tk.Button(
    root, 
    text = "Add Hump-shaped Dysplasia Abnormality",
    command = lambda: addData("Hump-shaped dysplasia"),
    fg = "black"
)
dysplasia_preset_button = tk.Button(
    root, 
    text = "Add Dysplasia Abnormality",
    command = lambda: addData("Dysplasia"),
    fg = "black"
)


#-------------------------------
# GUI Layout
#-------------------------------
#Canvas
canvas.get_tk_widget().grid(row = 0, column = 0, columnspan = 10, rowspan = 40, sticky = 'nsew')

# Excel table name:

# Excel table Packing:
excel_table.grid(row = 1, column = 10, columnspan = 2, rowspan = 40, sticky = 'new')

# File path will appear here:
current_path_label.grid(row = 41, column = 0, columnspan = 15, sticky = "nsew")

# Current Index (image #):
current_index.grid(row = 42, column = 0, sticky = 'nsew')

# Running Status
running_label.grid(row = 42, column = 1, sticky = 'nsew')

# Loading Status
loading_label.grid(row = 42, column = 3, sticky = 'nsew')

# Customize Button
customize_button.grid(row = 43, column = 1, sticky = "nsew")

# Change base image opacity label + Spinbox
change_base_opacity_label.grid(row = 43, column = 2, sticky = 'nse')
change_base_opacity_spinbox.grid(row = 43, column = 3, sticky = 'nsew')

# Excel Sheet Name
excel_file_label.grid(row = 43, column = 0, sticky = 'nsew')

# Change Rotation: column = 7
rotate_left_button.grid(row = 43, column = 7, sticky = "nsew")
rotate_right_button.grid(row = 44, column = 7, sticky = 'nsew')

# Change current midslice label + Spinbox
change_midslice_label.grid(row = 43, column = 8, sticky = 'nse')
change_midslice_spinbox.grid(row = 43, column = 9, sticky = 'nsew')

# Go to image
set_image_button.grid(row = 44, column = 8, sticky = "nsew")
set_image_entry.grid(row = 44, column = 9, sticky = 'nsew')

# Go to path
set_path_button.grid(row = 45, column = 8, sticky = "nsew")
set_path_entry.grid(row = 45, column = 9, sticky = 'nsew')


#loop images
loop_images_button.grid(row = 44, column = 1, sticky = 'nsew')
pause_button.grid(row = 45, column = 1, sticky = "nsew")
play_button.grid(row = 44, column = 0, sticky = 'nsew')

# Change mask opacity label + Spinbox
# Change base image opacity label + Spinbox
change_mask_opacity_label.grid(row = 44, column = 2, sticky = 'nse')
change_mask_opacity_spinbox.grid(row = 44, column = 3, sticky = 'nsew')

# Base/mask checkboxes
mask_checkbox.grid(row = 44, column = 4, sticky = 'nsew')
base_checkbox.grid(row = 43, column = 4, sticky = 'nsew')

# Quit
exit_button.grid(row = 45, column = 0, sticky = 'nsew')

# Previous/Next image buttons
previous_image_button.grid(row = 45, column = 2, sticky = 'nsew')
next_image_button.grid(row = 45, column = 3, sticky = 'nsew')

# Added Abnormality
added_data_label.grid(row = 0, column = 12, columnspan = 2, sticky = "nsew")

#Abnormalities Table
abnormalities_label.grid(row = 1, column = 12, sticky = "nsew")
abnormalities_entry.grid(row = 2, column = 12, sticky = 'nsew')
add_data_button.grid(row = 3, column = 12, sticky = 'nsew')

root.columnconfigure(6, weight = 1)
root.columnconfigure(12, weight = 1)

# Additional Abnormality Presets
artifact_preset_button.grid(row = 6, column = 12, sticky = 'nsew')
registration_preset_button.grid(row = 7, column = 12, sticky = 'nsew')
dysplasia_preset_button.grid(row = 8, column = 12, sticky = 'nsew')
hypo_preset_button.grid(row = 9, column = 12, sticky = 'nsew')
hump_preset_button.grid(row = 10, column = 12, sticky = 'nsew')

root.mainloop()

# Dependencies
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os
import nibabel as nib
import glob


# Creating the TK window
window = tk.Tk()

# Create/pack path entry
enter_label = tk.Label(text="Insert your path here")
enter_text = tk.Entry(width = 100)

# Create figure and draw a blank canvas for later use
fig = plt.figure(figsize=(5,5),dpi=100)
canvas = FigureCanvasTkAgg(fig, master = window)
canvas.get_tk_widget().pack()
canvas.draw()

# Tkinter Plot function
def extract_slice_tk(ms=89):

    # Load image using given path
    hdr = nib.load(enter_text.get())
    img_data = hdr.get_fdata()
    midslice = img_data[ms,:,:]
    
    # Generate figure
    figplot = fig.add_subplot(111)
    figplot.imshow(midslice, cmap = "Greys_r")
    
    # Set current path label
    greeting = tk.Label(text = "Current Path: " + enter_text.get())
    greeting.pack()
    # Place figure onto canvas
    canvas.draw()

# TK Variables
exit_button = tk.Button(
    text="Quit",
    width = 5,
    height = 1,
    command = window.destroy)

plot_button = tk.Button(
    master = window,
    text='plot',
    width = 5,
    height = 1,
    command = extract_slice_tk)

# pack variables
plot_button.pack()
enter_label.pack()
enter_text.pack()
exit_button.pack()

# main loop
window.mainloop()
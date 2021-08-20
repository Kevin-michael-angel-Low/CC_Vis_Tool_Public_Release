# Dependencies
import tkinter as tk
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
from cc_final import *

popup = tk.Toplevel(root)
popup_title = tk.Label(popup, text = "this is a popup!")

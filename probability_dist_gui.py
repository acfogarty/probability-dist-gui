#from Tkinter import *
import Tkinter as tk
import ttk
import binomial
import exponential
import sys
sys.path.insert(1,'/Library/Python/2.7/site-packages')
import test
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class App:

  def __init__(self, master):

    frame = tk.Frame(master)
    frame.pack()

    self.label1 = tk.Label(frame, text="Choose a distribution to explore:")
    self.label1.pack(side=tk.LEFT)

    distributionsList = ['binomial','exponential']
    chosenDistribution = tk.StringVar()
    chosenDistribution.set(distributionsList[0])
    self.combobox = ttk.Combobox(frame, values=distributionsList, textvariable=chosenDistribution)
    self.combobox.pack(side=tk.LEFT)
       
    self.generateButton = tk.Button(frame, text="Go!", command=lambda: self.showFrame(master, chosenDistribution))
    self.generateButton.pack(side=tk.LEFT)

    self.quitButton = tk.Button(frame, text="QUIT", fg="red", command=frame.quit)
    self.quitButton.pack(side=tk.RIGHT,padx=20)

  def showFrame(self, master, chosenDistribution):
    if chosenDistribution.get() == 'binomial':
      frame2 = binomial.BinomialPlot(master)
    elif chosenDistribution.get() == 'exponential':
      frame2 = exponential.ExponentialPlot(master)
    frame2.pack()

root = tk.Tk()

app = App(root)

root.mainloop()
root.destroy() 

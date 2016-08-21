import sys
sys.path.insert(1,'/Library/Python/2.7/site-packages')
import matplotlib.pyplot as plt
import numpy as np
import math
import Tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import auxiliary

class ExponentialPlot(tk.Frame):

  #exponential distribution, simulated and analytical
  #nvalues   - number of simulated values obtained using inverse transform sampling
  #llambda  - rate parameter

  def __init__(self,parent):
    
    plotFrame = tk.Frame.__init__(self, parent, borderwidth = 5)

    titleLabel = tk.Label(self, text="Exponential distribution\nThe exponential probability density function f(x) shows the time we need to wait before an event occurs",relief='groove')
   
    photo = tk.PhotoImage(file="figs/exponential_pdf.gif")
    equationLabel = tk.Label(self, image=photo)
    equationLabel.image = photo

    parametersLabel = tk.Label(self, text="Enter distribution parameters:")

    lambdaLabel = tk.Label(self, text="lambda = ")
    self.lambdaEntry = tk.Entry(self,text="0.5")
    self.lambdaEntry.insert(tk.END,"0.5")
    self.p = 0.5
    lambdaExplanationLabel = tk.Label(self, text="(rate parameter)")

    nvaluesLabel = tk.Label(self, text="# generated values = ")
    self.nvaluesEntry = tk.Entry(self,text="1000")
    self.nvaluesEntry.insert(tk.END,"1000")
    self.nvalues = 1000
    nvaluesExplanationLabel = tk.Label(self, text="(number of values generated from inverse transform sampling)")

    generateButton = tk.Button(self, text="Generate", command = lambda: self.generateDistributions())
 
    self.infoLabel = tk.Label(self, text="")

    #make figure 
    self.fig = Figure(figsize=(7,4), dpi=70)
    self.ax = self.fig.add_subplot(111) 

    #layout
    titleLabel.grid(column=0,row=0,columnspan=3)

    equationLabel.grid(column=0,row=1,columnspan=3)

    parametersLabel.grid(column=0,row=2,columnspan=2)

    lambdaLabel.grid(column=0,row=3)
    self.lambdaEntry.grid(column=1,row=3)
    lambdaExplanationLabel.grid(column=2,row=3)

    nvaluesLabel.grid(column=0,row=4)
    self.nvaluesEntry.grid(column=1,row=4)
    nvaluesExplanationLabel.grid(column=2,row=4)

    generateButton.grid(column=1,row=5)

  def probabilityDensityFunction(self, x):
    #calculates analytical probability of the time between events
    #given rate llambda
    if x<0:
      pdf = 0.0
    else:
      pdf = self.llambda*math.exp(-1*self.llambda*x)
    return pdf
  
  #def performSimulation(self):
  #  draw values U from uniform distribution
  #  generate values E from exponential distribution 
  #  E = -log(U)/lambda

  def generateDistributions(self):

    #get user-input distribution and simulation parameters
    self.llambda = float(self.lambdaEntry.get())
    self.nvalues = int(self.nvaluesEntry.get())

    #update text describing distribution and simulation parameters 
    distributionParametersString = "Distribution parameter: lambda = {0}".format(self.llambda)
    simulationParameterString = "No. of values generated from inverse transform sampling = {0}".format(self.nvalues)   
    self.infoLabel['text'] = distributionParametersString+"\n"+simulationParameterString

    self.ax.clear()

    #plot analytical pdf
    xmax = (math.log(self.llambda)+9.21)/self.llambda #find values of x where pmf(x)=0.0001,ln(0.0001)=9.21
    xvalues = np.linspace(0.0,xmax,dtype=np.float64)
    self.ax.plot(xvalues,np.fromiter([self.probabilityDensityFunction(x) for x in xvalues],float, count=len(xvalues)),label='theory')

    #plot pdf from simulation TODO
    #k_simulation = self.performSimulation()
    #self.ax.hist(k_simulation,bins=10,normed=True,label='simulation')

    self.ax.legend()
    self.ax.set_xlabel('x [?]')
    self.ax.set_ylabel('f(x) [probability density function]')
    self.canvas = FigureCanvasTkAgg(self.fig, self)
    self.canvas.show()

    #layout
    self.infoLabel.grid(column=0,row=6,columnspan=3)
    self.canvas.get_tk_widget().grid(column=0,row=7,columnspan=3)


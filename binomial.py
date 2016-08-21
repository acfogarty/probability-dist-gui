import sys
sys.path.insert(1,'/Library/Python/2.7/site-packages')
import matplotlib.pyplot as plt
import numpy as np
import math
import Tkinter as tk
#import matplotlib
#matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import auxiliary

class BinomialPlot(tk.Frame):

  #binomial distribution, simulated and analytical
  #nruns   - number of simulation runs
  #ntrials - number of Bernoulli trials
  #k       - number of successes
  #p       - probability of success at each trial

  def __init__(self,parent):
    
    plotFrame = tk.Frame.__init__(self, parent, borderwidth = 5)

    titleLabel = tk.Label(self, text="Binomial distribution\nThe binomial probability mass function f(k) shows the probability of having k successes out of n trials,\nwhen p is the probability of success at each trial\nBoth the analytical distribution and a simulated distribution are plotted",relief='groove')#\np = probability of success at each trial\nn = number of trials\nk = number of successes\nns = number of simulation runs")
   
    photo = tk.PhotoImage(file="figs/binomial_pmf.gif")
    equationLabel = tk.Label(self, image=photo)
    equationLabel.image = photo

    parametersLabel = tk.Label(self, text="Enter distribution parameters:")

    pLabel = tk.Label(self, text="p = ")
    self.pEntry = tk.Entry(self,text="0.5")
    self.pEntry.insert(tk.END,"0.5")
    self.p = 0.5
    pExplanationLabel = tk.Label(self, text="(probability of success at each trial)")

    ntrialsLabel = tk.Label(self, text="n = ")
    self.ntrialsEntry = tk.Entry(self,text="500")
    self.ntrialsEntry.insert(tk.END,"500")
    self.ntrials = 500
    ntrialsExplanationLabel = tk.Label(self, text="(number of trials)")

    nrunsLabel = tk.Label(self, text="# simulation runs = ")
    self.nrunsEntry = tk.Entry(self,text="1000")
    self.nrunsEntry.insert(tk.END,"1000")
    self.nruns = 1000
    nrunsExplanationLabel = tk.Label(self, text="(number of simulation runs)")

    generateButton = tk.Button(self, text="Generate", command = lambda: self.generateDistributions())
 
    self.infoLabel = tk.Label(self, text="")

    #make figure 
    self.fig = Figure(figsize=(7,4), dpi=70)
    self.ax = self.fig.add_subplot(111) 

    #layout
    titleLabel.grid(column=0,row=0,columnspan=3)

    equationLabel.grid(column=0,row=1,columnspan=3)

    parametersLabel.grid(column=0,row=2,columnspan=2)

    pLabel.grid(column=0,row=3)
    self.pEntry.grid(column=1,row=3)
    pExplanationLabel.grid(column=2,row=3)

    ntrialsLabel.grid(column=0,row=4)
    self.ntrialsEntry.grid(column=1,row=4)
    ntrialsExplanationLabel.grid(column=2,row=4)

    nrunsLabel.grid(column=0,row=5)
    self.nrunsEntry.grid(column=1,row=5)
    nrunsExplanationLabel.grid(column=2,row=5)

    generateButton.grid(column=1,row=6)

  def probabilityMassFunction(self, k):
    #calculates analytical probability of having k successes
    pmf = pow(self.p,k)*pow(1-self.p,self.ntrials-k)*auxiliary.binomCoeff(self.ntrials,k)
    return pmf
  
  def performSimulation(self):
    #performs nruns simulation runs
    #returns array of length nruns, containing number of successes in each run
    outcomes = np.random.uniform(low=0.0, high=1.0, size=(self.nruns,self.ntrials))
    k_simulation = np.empty(self.nruns)
    i = 0
    for run in outcomes:
      run = np.where(run < self.p, 1, 0)
      k_simulation[i] = sum(run)
      i += 1
    return k_simulation

  def generateDistributions(self):

    #get user-input distribution and simulation parameters
    self.p = float(self.pEntry.get()) #TODO check 0<p<1
    self.ntrials = int(self.ntrialsEntry.get())
    self.nruns = int(self.nrunsEntry.get())

    #update text describing distribution and simulation parameters 
    distributionParametersString = "Distribution parameters: p = {0}, no. of trials = {1}".format(self.p,self.ntrials)
    simulationParameterString = "No. of simulation runs = {0}".format(self.nruns)   
    self.infoLabel['text'] = distributionParametersString+"\n"+simulationParameterString

    self.ax.clear()

    #plot analytical pmf
    kvalues = np.linspace(0,self.ntrials,dtype=np.int)
    self.ax.plot(kvalues,np.fromiter([self.probabilityMassFunction(k) for k in kvalues],float, count=len(kvalues)),label='theory')

    #plot pmf from simulation
    k_simulation = self.performSimulation()
    self.ax.hist(k_simulation,bins=10,normed=True,label='simulation')

    self.ax.legend()
    self.ax.set_xlabel('k [number of successes]')
    self.ax.set_ylabel('f(k) [probability mass function]')
    self.canvas = FigureCanvasTkAgg(self.fig, self)
    self.canvas.show()

    #layout
    self.infoLabel.grid(column=0,row=7,columnspan=3)
    self.canvas.get_tk_widget().grid(column=0,row=8,columnspan=3)


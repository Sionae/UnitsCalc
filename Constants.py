from math import *
import numpy as np
from Classes import *

operators = ["+", "-", "*", "/", "exp", "**"]

# {"kg":0, "m":0, "s":0, "K":0, "A":0, "mol":0, "cd":0, "rad":0, "sr":0}

#Physics constants
G = Var("G", 6.67408 * 10**(-11), {"kg":-1, "m":3, "s":-2, "K":0, "A":0, "mol":0, "cd":0, "rad":0, "sr":0})
h = Var("h", 6.62607 * 10**(-34), {"kg":1, "m":2, "s":-1, "K":0, "A":0, "mol":0, "cd":0, "rad":0, "sr":0})
c = Var("c", 2.99792 * 10**8, {"kg":0, "m":1, "s":-1, "K":0, "A":0, "mol":0, "cd":0, "rad":0, "sr":0})


pi = Var("pi", pi, {"kg":0, "m":0, "s":0, "K":0, "A":0, "mol":0, "cd":0, "rad":0, "sr":0})
e = Var("e", e, {"kg":0, "m":0, "s":0, "K":0, "A":0, "mol":0, "cd":0, "rad":0, "sr":0})

#Defining the constants
#Maths Constants
PConstants = [G, h, c]
MConstants = [pi, e]

totalUnits = PConstants + MConstants


m = Var("m", 5, {"kg":0, "m":1, "s":-1, "K":0, "A":0, "mol":0, "cd":0, "rad":0, "sr":0})
totalUnits.append(m)

#Adding the name of the units, their value and their units in a common array
basicVars = np.array([G.list, h.list, c.list])

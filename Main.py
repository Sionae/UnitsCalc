from Fonctions import *
import panda as pd

file = "Physics.xlsx" #Excel file

dataframes, sheetnames = extract_from_Excel(file)
#Extracting dataframes from each sheet and sheetnames from the file

dataFrames = [] #Array list containing all the data frames
for dt in dataframes:
    array_list.append(pd.DataFrame.as_matrix(dt)) #Converting dataframes into arrays

dataFrames = cut_extra_elt(dataFrames) #We cut elements which do not correspond to all dataframes
dataFrames = flatten_arrays(dataFrames) #Flattening the array






eqList = []

PhysConsts = []
MathsConsts = []

tempList = []
nextTimeList = []

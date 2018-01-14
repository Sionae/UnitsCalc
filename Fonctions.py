from Constants import *
import tqdm
import random


# FILE FUNCTIONS

def extract_from_Excel(file):
    """Extracting Dataframes and sheet names from an excel file"""

    Excel_File = pd.ExcelFile(file)
    df = [] #DataFrames of each slide of the excel file
    sheetnames = []

    for xn in Excel_File.sheet_names:
        df.append(Excel_File.parse(xn))
        sheetnames.append(xn)

    return df, sheetnames


def cut_extra_elt(array_list):
    """Cuts extra elements in a flattened array list in order each array to have the same size"""
    arraylOut = []

    for array in range(0, len(array_list)):
        #Iterate the entire array list to see differences in length
        if array_list[array] is not array_list[-1]: #If not the last element of the array list
            if not check_asize(array_list[array], array_list[array + 1])[0]: #If the sizes are different
                size_diff = np.size(array_list[array]) - np.size(array_list[array + 1])
                #Calculate the difference in size

                while size_diff < 0: #Second array is bigger than first array
                    array_list[array + 1] = np.delete(array_list[array + 1], array_list[array + 1][-1])
                    #Remove last element
                    size_diff = np.size(array_list[array]) - np.size(array_list[array + 1])
                while size_diff > 0: #First array is bigger than second array
                    array_list[array] = np.delete(array_list[array], array_list[array][-1])
                    #Remove last element
                    size_diff = np.size(array_list[array]) - np.size(array_list[array])

        arrayl_out.append(array_list[array])

    return arrayl_out


def rewrite_Excel_elts(array_list, file, sheetnames):
    """Re-model the excel file after the modifications applied to it"""
    writer = pd.ExcelWriter(file, engine='xlsxwriter')
    for array in tqdm(range(0, len(array_list))):
        nar2df(array_list[array]).to_excel(writer, sheetnames[array])

    writer.save()

    print("Modifications completed.")


# ARRAY FUNCTIONS

def check_asize(a1, a2):
    """Checks the size of two arrays"""
    return np.size(a1) == np.size(a2), np.size(a1), np.size(a2)


def flatten_arrays(array_list):
    """Flatten each array in an array list and outputs a flatten array list"""

    arraylOut = [] #Flattened array list
    for array in array_list:
        arraylOut.append(array.flat[:])

    return arraylOut


def a_remove(array_list, obj):
    """Function permitting to remove object from arrays because this is badly done with numpy... """
    l = []
    for array in array_list:
        l.append(array.tolist())

    l.remove(obj)

    return np.array(l)




def append(a1, a2):
    """Function which return a new array after having appended array 2 to array 1"""

    af = []

    for array in a1:
        af.append(array.tolist())

    for array in a2:
        af.append(array.tolist())

    return np.array(af)


# UNITS FUNCTIONS

def UnitsCalc(unitsA, unitsB, op):
    # {"kg":0, "m":0, "s":0, "K":0, "A":0, "mol":0, "cd":0, "rad":0, "sr":0}
    new_units = {}

    if op == "*" or op == "/":
        if op == "*":
            check = 1
        else:
            check = -1

        new_units["kg"] = unitsA["kg"] + unitsB["kg"]*check
        new_units["m"] = unitsA["m"] + unitsB["m"]*check
        new_units["s"] = unitsA["s"] + unitsB["s"]*check
        new_units["K"] = unitsA["K"] + unitsB["K"]*check
        new_units["A"] = unitsA["A"] + unitsB["A"]*check
        new_units["mol"] = unitsA["mol"] + unitsB["mol"]*check
        new_units["cd"] = unitsA["cd"] + unitsB["cd"]*check
        new_units["rad"] = unitsA["rad"] + unitsB["rad"]*check
        new_units["sr"] = unitsA["sr"] + unitsB["sr"]*check


        return True, new_units


    elif op == "+" or op == "-" or op == "**":
        def sameU(A, B, unit):
            return A[unit] == B[unit]

        return sameU(unitsA, unitsB, "kg") and sameU(unitsA, unitsB, "m") and sameU(unitsA, unitsB, "s") and sameU(unitsA, unitsB, "K") and sameU(unitsA, unitsB, "A") and sameU(unitsA, unitsB, "mol") and sameU(unitsA, unitsB, "cd") and sameU(unitsA, unitsB, "rad") and sameU(unitsA, unitsB, "sr"), unitsA



def UnitsDiff(A, B):
    """Calculates the total difference of units between two objects"""
    diff = 0
    for unit in A.keys():
        diff += abs(A[unit] - B[unit])

    return diff


def UnitsInList(l):
    units = {"kg":0, "m":0, "s":0, "K":0, "A":0, "mol":0, "cd":0, "rad":0, "sr":0}
    for x in l:
        for unit in x.units.keys():
            units[unit] += x.units[unit]

    return units


def UnitsOperation(base, n, *units):
    """Gives n number of possible equations due to their units
    *units corresponds to every unit, including the pysics constants and the maths constants"""
    units = units[0] #Converting tuple to list
    try:
        units.remove(base)
    except:
        pass

    UsedP = []
    operators = ["+", "-", "*", "/", "**"]


    count = 0
    pbar = tqdm.tqdm(total=1)
    security = 10000


    while count < n:
        #Main loop
        TotalVar = Var("Total Units", 0, {"kg":0, "m":0, "s":0, "K":0, "A":0, "mol":0, "cd":0, "rad":0, "sr":0})
        UsedU = []
        c = 0
        operators = ["+", "-", "*", "/", "**"]
        while TotalVar.units != base.units and c<security:
            c += 1
            #Pick random unit
            u = random.choice(units)
            op = random.choice(operators)

            if UnitsDiff(TotalVar.units, base.units) > 10:
                count -= 1
                break

            if UnitsCalc(u.units, TotalVar.units, op)[0]:
                if u.name not in UsedU or op!="/":
                    TotalVar.units = UnitsCalc(u.units, TotalVar.units, op)[1]
                    UsedU.append(u.name)
                    UsedU.append(op)

        count += 1
        if UsedU in UsedP:
            continue
        if security == c:
            raise RuntimeError


        UsedP.append(UsedU)

        count += 1

        pbar.update(count/n)


    pbar.close()
    return UsedP


print(UnitsOperation(G, 2, PConstants))

#CALCULUS FUNCTIONS

def give_values(array_list, sheetnames, elements):
    """Gives the values of the extracted Excel file to the passed elements depending on their name"""

    for name in sheetnames:
        for var in elements:
            if name == var.name:
                var.values = var.give_values(array_list[sheetnames.index(name)])

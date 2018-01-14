class Var:
    """Class implementing variables with their names, values and units"""

# Units : {"kg":0, "m":0, "s":0, "K":0, "A":0, "mol":0, "cd":0}



    def __init__(self, name, values, units):
        """The units stand for the different unit values, in this order :
        kg, m, s, K, A, mol, cd, rad, sr"""
        self.name = name
        self.values = values

        self.units = units
        self.NonZeroU = units

        self.list = [self.name, self.values, self.units]



    def getNonZeroU(self):
        usableDict = dict()
        for key, value in self.units.items():
            if value != 0:
                usableDict[key] = value

        self.NonZeroU = usableDict


    def give_values(self, new_values):
        self.values = new_values
        self.list = [self.name, self.values, self.units]
        return self.values

    def update(self):
        self.list = [self.name, self.values, self.units]

    def __str__(self):
        return self.name + " : " + str(self.list[1]) + " " + str(self.NonZeroU)


    def __repr__(self):
        return str(self.NonZeroU)

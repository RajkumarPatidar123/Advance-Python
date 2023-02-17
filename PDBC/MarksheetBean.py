class Marksheet:
    def __init__(self) -> None:
        self.roll_no = 0
        self.name = None
        self.physics = 0
        self.chemistry = 0
        self.maths = 0

    def getRoll_no(self):
        return self.roll_no

    def setRoll_no(self,roll_no):
        self.roll_no = roll_no

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getPhysics(self):
        return self.physics

    def setPhysics(self,physics):
        self.physics = physics

    def getChemistry(self):
        return self.chemistry

    def setChemistry(self,chemistry):
        self.chemistry = chemistry

    def getMaths(self):
        return self.maths

    def setMaths(self,maths):
        self.maths = maths

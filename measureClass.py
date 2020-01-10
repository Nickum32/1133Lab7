class measure:
    def __init__(self, ft=0, inc=0):
        self.feet=ft
        self.inches=inc%12
        self.feet+= inc//12
    def __str__(self):
        if self.feet==0:
            return str(self.inches)+'"'
        elif self.inches==0:
            return str(self.feet)+"'"
        else:
            return str(self.feet)+"'"+str(self.inches)+'"'
    def __add__(self, other):
        newFeet=self.feet+other.feet
        newInches=self.inches+other.inches
        return measure(newFeet, newInches)
    def __sub__(self, other):
        newFeet=self.feet-other.feet
        newInches=self.inches-other.inches
        return measure(newFeet, newInches)



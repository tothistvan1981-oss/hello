# Ez egy proba modul
from tokenize import String

def osszeg():
    egyik = int(input("Kérek egy számot:"))
    masik = int(input("Kérek egy másik számot:"))
    eredmeny = egyik+masik
    print("Az erdemény értéke:".center(50))
    print(str( eredmeny).rjust(50,"_") )
    return



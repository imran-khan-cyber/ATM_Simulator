# Declaring Constants for Dictionary Key Purpose.
NAME = 'name'
PIN = 'pin'

class Accounts:
    """" To maintain and secure User's ID and Pin. """
    # Declaring Static Variables.
    filename = "./data/accounts.csv"
    AC = {}

    def __init__(self): # Using Constructor to load accounts data in Dictionary
        if len(Accounts.AC)== 0: # Load the data if the object creation for the first time only.
            self.acno = ""
            self.LoadData()


    def LoadData(self):
        Accounts.AC.clear()  # First clear the unwanted data present in this dictionary.
        # Open File to load data in Dictionary.
        with open(Accounts.filename,"r") as f:
            lines = f.readlines()
            for line in lines:
                field = line.split(",")
                acno = field[0].strip()
                aname = field[1].strip()
                apin = field[2].strip()
                # Load the separated data in a dictionary.
                Accounts.AC[acno] ={NAME:aname,PIN:apin}
        #print Accounts.AC


    def ValidateAccountNo(self,accno):
        """Validate Account Number entered by user
            is present in Dictionary or not. If present,
            then return UserName that matches the user's
            account number."""
        name = ""
        if Accounts.AC.has_key(accno):
            self.acno = accno
            name = Accounts.AC[accno][NAME]
            return name
        else:
            raise Exception("Invalid! Account Number")


    def ValidatePin(self,pin):
        Pin = Accounts.AC[self.acno][PIN]
        # print Pin,pin
        return(Pin == pin)








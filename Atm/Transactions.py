from datetime import datetime

class Transactions:
    """ To maintain Transaction's Deposit, Withdraw and List Transactions. """
    # static variable
    filename = "./data/transactions.csv"

    def checkBal(self,acc):
        """ This method is used to find each user's closing amount."""
        tot = 0.0
        with open(Transactions.filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                field = line.split(",".strip())
                if len(field) > 3:
                    if (field[0] == acc) and (field[2] == "DEPOSIT"):
                        tot += float(field[3])
                    if (field[0] == acc) and (field[2] == "WITHDRAW"):
                        tot -= float(field[3])
        return tot


    def deposit(self,ano,amount):
        with open(Transactions.filename,"a") as f:
            trandate = datetime.now().strftime("%d/%m/%y %X")
            f.write("{an},{dt},DEPOSIT,{amt}\n".format(an = ano,dt = trandate,amt = amount))
        print "Deposit Successful!"


    def withdraw(self,ano,amount):
        res = 0.0
        res = self.checkBal(ano)
        """ Checking that user closing balance must be greater than 
            or equal to user entered amount. this is for successful
            Withdrawl. """
        if res >= float(amount):
            with open(Transactions.filename,"a") as f:
                trandate = datetime.now().strftime("%d/%m/%y %X")
                f.write("{an},{dt},WITHDRAW,{amt}\n".format(an = ano,dt = trandate,amt = amount))
            print "Withdraw Successful!"
        else:
            print "Sorry! Insuffient Balance..."


    def listtransaction(self,ano):
        trans = []
        closebal = 0.0
        print
        print "{:12s}List Transactions...".format(" ")
        print "{:12s}-------------------".format(" ")
        with open(Transactions.filename,"r")as f:
            lines = f.readlines()
        for line in lines:
            field = line.split(",")
            if field[0] == ano:
                trans.append(line.strip())
        # print trans
        for trn in trans:
            #print trn
            field = trn.split(",")
            accn = field[1]
            Ttype = field[2]
            am = float(field[3])
            if Ttype == "WITHDRAW":
                am = -am
            print "{}  {:15s}${:8.2f}".format(accn, Ttype, am)
            closebal += am
        if closebal > 0:
            print "Closing Balance : $%.2f" %closebal
        else:
            print "Closing Balance : $%.2f" %(0.00)








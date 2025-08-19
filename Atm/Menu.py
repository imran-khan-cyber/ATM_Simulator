from Atm import Account
from Atm import Transactions

# Creating Object instances for Accounts and Transactions
Ac = Account.Accounts()
Tr = Transactions.Transactions()

class Menu:
    """" Integration of Account and Transaction Modules. """
    ano = ''

    def start(self):
        while True:
            print
            print "TamilNadu Bank Ltd..."
            print "Trichy Br."
            print "Welcome to our ATM Banking Service."
            print
            ac = raw_input("Please! Enter your Account Number : ")
            try:
                name = Ac.ValidateAccountNo(ac)
                Menu.ano = ac
                print "Welcome "+ name
                self.startmenu()
            except Exception as e:
                print e.message

    def verifypin(self):
        pin = raw_input("Please! Enter your Pin Number : ")
        return Ac.ValidatePin(pin)


    def startmenu(self):
        while True:
            print
            print " TamilNadu Bank Ltd..."
            print "     Trichy Br."
            print " Welcome to our ATM Banking Service."
            print
            print "Menu Options."
            print "1. Deposit"
            print "2. Withdraw"
            print "3. Transactions List"
            print "4. Exit"
            opt = raw_input("Enter your Options(1-4) : ")
            if opt == '1':
                if self.verifypin():
                    amount = raw_input("Enter amount upto $9999.00 : ")
                    Tr.deposit(Menu.ano,amount)
                else :
                    print "You Entered Invalid Pin! Press Enter to try again"
                    raw_input()
                    break
            elif opt == '2':
                if self.verifypin():
                    amount = raw_input("Enter amount upto $9999.00 : ")
                    Tr.withdraw(Menu.ano, amount)
                else :
                    print "You Entered Invalid Pin! Press Enter to try again"
                    raw_input()
                    break
            elif opt == '3':
                if self.verifypin():
                    Tr.listtransaction(Menu.ano)
                else :
                    print "You Entered Invalid Pin! Press Enter to try again"
                    raw_input()
                    break
            elif opt == '4':
                break
            else:
                print "Invalid! Option"
                raw_input()
                continue








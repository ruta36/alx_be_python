class BankAccount:
    def _init_( self , initial_balance = 0):
        self.__account_balance = initial_balance

    def deposit( self , amount ):
        self.__account_balance += amount

    def withdraw( self , amount ):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False


    def display_balance(self):
        print(f"Current Balance: ${self.__accout_balance:.2f}")


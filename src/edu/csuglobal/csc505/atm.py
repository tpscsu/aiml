class ATM:
    def __init__(self, pin, balance, max_attempts=3):
        self.correct_pin = pin
        self.balance = balance
        self.max_attempts = max_attempts
        self.attempts = 0
        self.state = "Start"

    def insert_card(self):
        print("[STATE] Insert Card: Please enter your PIN.")
        self.state = "Enter_PIN"

    def enter_pin(self, pin):
        if self.state != "Enter_PIN":
            print("[ERROR] Invalid state. Insert card first.")
            return

        print("[STATE] Enter PIN: Validating PIN...")
        self.state = "Validate_PIN"
        self.validate_pin(pin)

    def validate_pin(self, pin):
        if pin == self.correct_pin:
            print("[STATE] Validate PIN: PIN correct. Proceeding to withdrawal.")
            self.state = "Withdraw_Money"
        else:
            self.attempts += 1
            print(f"[STATE] Incorrect PIN: Attempts {self.attempts}/{self.max_attempts}")
            if self.attempts >= self.max_attempts:
                print("[STATE] Exceed PIN Attempts: Too many incorrect attempts. Card blocked.")
                self.state = "Reject_Customer"
            else:
                print("[ACTION] Retry PIN: Asking for PIN again.")
                self.state = "Enter_PIN"

    def withdraw_money(self, amount):
        if self.state != "Withdraw_Money":
            print("[ERROR] Invalid state. Authentication required.")
            return

        print(f"[STATE] Withdraw Money: Requesting withdrawal of ${amount}.")
        self.state = "Check_Balance"
        self.check_balance(amount)

    def check_balance(self, amount):
        if self.balance == 0:
            print("[STATE] Check Balance: Account balance is zero. Closing account.")
            self.state = "Account_Closed"
        elif amount <= self.balance:
            self.balance -= amount
            print(f"[STATE] Transaction Successful: ${amount} dispensed. Remaining balance: ${self.balance}.")
            self.state = "Transaction_Complete"
        else:
            print("[STATE] Insufficient Balance: Transaction denied.")
            self.state = "Transaction_Complete"

    def complete_transaction(self):
        if self.state == "Transaction_Complete":
            print("[STATE] Transaction Complete: Ejecting card. Thank you!")
            self.state = "Start"
        elif self.state == "Reject_Customer":
            print("[STATE] Card Blocked: Contact bank.")
        elif self.state == "Account_Closed":
            print("[STATE] Account Closed: Contact bank.")
        else:
            print("[ERROR] Invalid state to complete transaction.")


# Simulating ATM steps
atm = ATM(pin=1234, balance=500)

atm.insert_card()
atm.enter_pin(1111)  # Incorrect PIN
atm.enter_pin(2222)  # Incorrect PIN
atm.enter_pin(1234)  # Correct PIN
atm.withdraw_money(200)  # Withdraw $200
atm.complete_transaction()

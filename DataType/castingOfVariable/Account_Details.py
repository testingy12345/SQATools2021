class account:
    def __init__(self,account_name,account_email):
        self.name=account_name
        self.email=account_email

    def show_account_name(self):
        print("Account Name :",self.name)

    def show_account_email(self):
        print("Account Email :",self.email)
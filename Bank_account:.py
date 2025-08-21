class Bank_account:
    def __init__(self,name,acc_no,acc_type):
        self.name=name
        self.acc_no=acc_no
        self.acc_type=acc_type
    def __str__(self):
        return f"{self.name}| {self.acc_no} | {self.acc_type} "
Bank_account_list=[]
running= True

#create a loop that makes 
# new objs and puts them in a list until you stop it.
while running:
    try:
        make=input("Make new Account? Y/N :")
        if make=='Y':
            name=input("Enter name: ")
            acc_no=input("Enter account number: ")
            acc_type=input("Enter account type: ")

            new_account=Bank_account(name,acc_no,acc_type)
            Bank_account_list.append(new_account)
            print(f"Account Created :{new_account}") 
        elif make=='N':
            print("Goodbye.")
            running= False
        else:
            raise ValueError("Invalid input. Please type Y or N.")

    except ValueError as v:
        print(v)
                            
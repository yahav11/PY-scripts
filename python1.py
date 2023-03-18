IDarray=[12345,54321]
balance = 0

id = int(input("please enter your id\n"))

if id == IDarray[0]:
    print("hello Yahav gueta,")
    userinput_addTakeBalance = input("would you like to make a deposit/a transference or to check your account balance?\n(enter balance/transfer/deposit)\n\n")

    if userinput_addTakeBalance == "deposit":
        depositAmount = int(input("please enter the amount you would like to deposit\n"))
        balance += depositAmount
        print(f"deposit made successfully, the balance is {balance}\n")

    if userinput_addTakeBalance == "transfer":
        trnswhom = int(input("please enter the account number you would like to transfer to\n"))
        transferenceAmount = int(input("please enter the amount you would like to transfer\n"))
        balance -= transferenceAmount
        print(f"transference successfully made, the balance is {balance}\n")
        
    if userinput_addTakeBalance == "balance":
        print(f"currently your balance is {balance}\n\n")
        answer = input("would you like to make a transfer or a deposit?\n")

        if answer == "yes":
            userinput_addTakeBalance = input("enter transfer/deposit\n\n")
            
            if userinput_addTakeBalance == "deposit":
                depositAmount = int(input("please enter the amount you would like to deposit\n"))
                balance += depositAmount
                print(f"deposit made successfully, the balance is {balance}\n")

            if userinput_addTakeBalance == "transfer":
                trnswhom = int(input("please enter the account number you would like to transfer to\n"))
                transferenceAmount = int(input("please enter the amount you would like to transfer\n"))
                balance -= transferenceAmount
                print(f"transference successfully made, the balance is {balance}\n")

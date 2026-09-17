total_inventory = 0
errors = 0 
total_processed_inventory = 0

#check if stock is integer and negative value 
def check_user_input(user_input):
    #isdigit only returns True for digits 
    #returns false for negative 
    #we should check for whether its digit or negative value
    return user_input.strip().isdigit()



while True: 
    # 1. Initialize the inventory to zero in the start
    user_input = input("Please enter stock value: or type `quit` to kill the program: ")
    if (user_input).lower() == "quit":
        print("Program quit!")
        print("Number of Failed/Rejected Entries: ", errors)
        #need to print total processed
        print("Total Units Processed Inventory: " , total_processed_inventory)
        break
    #logic of my operations
    elif (check_user_input(user_input)):
        stock_value = int(user_input)
        #add valid user input into total_inventory 
        total_inventory+=stock_value
        print("Total inventory: " ,total_inventory)
        #add valid user input into total_processed_inventory
        total_processed_inventory+=stock_value

        # 7. Trigger Overstock Alert: If the total inventory exceeds 500 units, print an
        # alert and break the loop immediately. (keep in mind of the conditional flow we
        # discussed this week: if, elif and else)
        if (total_inventory > 500):
            print("My total inventory has exceeded capacity!!!")
            break

    else: 
        print("Please enter a valid integer. Eg. `1` ")
        errors+=1
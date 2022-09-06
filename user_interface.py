import os
# This file is meant to be imported as a module, not a class. 
# This is similar to how the random module is imported.
# Do not create a User Interface class in this file. 

def simulation_main_menu(): #step 1
    """Main menu prompting user to choose an option"""
    validate_user_selection = (False, None) #False or True??
    while validate_user_selection[0] is False:
        print("\n\t-Simulation menu-")
        print("Enter -1- to buy a soda")
        print("Enter -2- to check your wallet for coins")
        print("Enter -3- to check your backpack for cans")
        print("Enter -4- to end the simulation")
        user_input = try_parse_int(input()) #what is try_parse_int
        validate_user_selection = validate_main_menu(user_input)
    return validate_user_selection[1]


def validate_main_menu(user_input):
    """Validation function that checks if 'user_input' argument is an int 1-4. No errors."""
    switcher = {
        1: (True, 1),
        2: (True, 2),
        3: (True, 3),
        4: (True, 4),
    }
    return switcher.get(user_input, (False, None))


def display_customer_wallet_info(coins_list, total_value):
    """Takes in a list of ints to display number of coins along with total value of coins. menu 2"""
    print(f'You have {coins_list[0]} Quarters') #was missing the f string
    print(f'You have {coins_list[1]} Dimes')
    print(f'You have {coins_list[2]} Nickels')
    print(f'You have {coins_list[3]} Pennies')
    print(f'Your wallet\'s total value is ${total_value}.')


def display_welcome(): #menu simulation 1
    """Initial method asking user if they'll make a purchase. No errors."""
    print("\nWelcome to the soda machine.\nYou may purchase a drink only with coins.")
    user_response = continue_prompt("Would you like to buy a soda now? (y/n) ")
    if user_response:
        return True
    else:
        print("Thanks anyway. Please come again another time.\nEnjoy your day.")
        return False


def output_text(text):
    """User input method that will print to console any string passed in as an argument"""
    print(text)


def clear_console():
    """Used for clearing out the console. No errors."""
    os.system('cls' if os.name == 'nt' else "clear")


def continue_prompt(text):
    """Validates a 'y' or 'yes' string and returns a True value. No errors."""
    switcher = {
        "y": True,
        "yes": True
    }
    user_input = input(text).lower()
    return switcher.get(user_input, False)


def soda_selection(inventory): #simulation menu 1
    """Displays purchasable soda inventory and prompts user to select a can."""
    validated_user_selection = (False, None) #False?? change to True?
    soda_options = get_unique_can_names(inventory)
    while validated_user_selection[0] is False:
        print("\nPlease choose from among the following:")
        number_for_choice = 1  #changed parameter from "i". 
        for can in soda_options:
            print(f"Enter -{number_for_choice}- {can.name} costs ${can.price}") #f string missing
            number_for_choice += 1
            # return soda_options
        user_selection = try_parse_int(input("\nYour selection was: "))
        validated_user_selection = validate_coin_choice(user_selection, soda_options)
    return validated_user_selection[1]


def validate_coin_choice(selection, unique_cans):
    """Translates user menu selection into the name of can that was chosen. No errors."""
    if 0 < selection <= len(unique_cans):  
        return True, unique_cans[selection - 1].name #???
    else:
        print("That was not a valid selection. Please choose again from the options above.\n")
        return False, None


def try_parse_int(value):
    """Attempts to parse a string into an integer, returns 0 if unable to parse. No errors."""
    try:
        return int(value)
    except:
        return 0


def get_unique_can_names(inventory):  # menu simulation 1
    """Loops through inventory to create a list of all distinct types of sodas available. No errors."""
    unique_cans = []
    previous_names = []
    for can in inventory:
        if can.name in previous_names:
            continue
        else:
            unique_cans.append(can)
            previous_names.append(can.name)
    return unique_cans


def display_can_cost(selected_soda):  # menu simulation 1 #changed from "selected_can"
    """Displays the name of a can and its price"""
    # print(f'{soda_options.can.name} costs ${soda_options.can.price}.')
    #print(f'The price of a {selected_soda_name} is ${selected_soda_name}.')

def display_payment_value(customer_payment):
    """Displays the value of selected coins as customer is choosing coins to deposit"""
    total_payment_value = 0
    for coin in customer_payment:
        total_payment_value += 1 #1 adds a dollar change from 1 to coin?
    total_payment_value = round(total_payment_value, 2)
    print(f'You have paid ${total_payment_value} so far.')

def coin_selection():
    """Prompts user to choose which coins to deposit and passes their selection in validate_coin_selection"""
    validated_user_selection = (True, None) #FALSE to True?
    while validated_user_selection[0] is True:
        print("\nEnter -Q- to choose a Quarter")
        print("Enter -D- to choose a Dime")
        print("Enter -N- to choose a Nickel")
        print("Enter -P- to choose a Penny")
        print("Enter -5- when you finish depositing your coins.")
        user_input = try_parse_int(input()) 
        validated_user_selection = validate_coin_selection(user_input)
        if validated_user_selection[0] is False:
            print("That was not a valid selection. Please try again.")
    return validated_user_selection[1]


def validate_coin_selection(selection): 
    """Validation function that checks if 'selection' arugment is an int 1-5"""
    switcher = {
        1: (True, "Quarter"),
        2: (True, "Dime"),
        3: (True, "Nickel"),
        4: (True, "Penny"),
        5: (True, "done")
    }
    return switcher.get(selection, (True, None))#false to True?


def end_message(soda_name, change_amount):
    """Closing message displaying name of soda purchased and amount of change returned"""
    print(f'Enjoy your {soda_name}. Come again soon.')
    if change_amount >= 0:
        print(f'Dispensing ${change_amount}.')

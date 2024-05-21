# Dictionary to store game library with their quantities and rental costs
game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1},
    # Add more games as needed
}

x = 0
# Dictionary to store user accounts with their balances and points
user_accounts = {}

# Admin account details
admin_username = "admin"
admin_password = "adminpass"

# Function to display available games with their numbers and rental costs
def display_available_games():
    list_number = 1
    width = 17
    for title in list(game_library.keys()):                                                                          #set width for alignment
        if width < len(title):
            width = len(title)
    print("Title".center(width) + "\tQuantity\tCost")
    for title in game_library:
        print(f"({list_number}) {title:<{width}}\t{game_library[title]["quantity"]:<{8}}\t${game_library[title]["cost"]:<{4}}")
        list_number+=1

# Function to register a new user
def register_user():
    user_accounts_keys = user_accounts.keys()
    print("Sign Up".center(30, "-"))
    print("Enter a username and password to make your account.(Usernames are unique)")
    username = input("Username: ")
    for account_name in user_accounts.keys():
        if username == account_name:                                                          #checks if username is available
            while x != 1:
              print("Username already exists, enter(1) to retry or (2) to go back to menu")
              option = input("Input here: ")
              try:
                  if option == "1":
                    register_user()
                  elif option == "2":
                      main()
                  else:
                      raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
              except ValueError as e:
                  print(e)
              except TypeError as e:
                  print("Invalid input, input must a number")
    else:
        password = input("Password: ")                                                                             #Saves new key and default values for user_accounts
        user_accounts[username] = {"password": password,"inventory": [],"balance": 0.0,"points": 0}
        print(f"Account made successfully!\nWelcome to our game rental{username}")
        logged_in_menu(username)

# Function to rent a game
def rent_game(username):
    print("Game Rental".center(30, "-"))
    no_of_options = len(game_library.keys())
    while x != 1:
        print("Enter the number of the game you want to rent or (0) to go back to menu")                               #Choose game to rent
        display_available_games()
        print(f"Balance: {user_accounts[username]["balance"]}")
        option = input("Input here: ")
        number = int(option)
        try:
            if option == "0":
                logged_in_menu(username)
            elif 0 > number or number > no_of_options:
                raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
            titles = list(game_library.keys())
            while x != 1:
                print(f"Are you sure you want to rent {titles[number-1]}?\nenter (1) to proceed or (2) to cancel purchase")    #Confirm or cancel transaction
                confirm_purchase = input("Input here: ")
                try:
                    if confirm_purchase == "1":
                        if game_library[titles[number-1]]["cost"] > user_accounts[username]["balance"]:
                            while x != 1:
                                print("Sorry, insufficient balance\n(1)Go back to menu\n(2)Top up your account")
                                choice = input("Input here: ")
                                try:
                                    if choice == "1":
                                        logged_in_menu(username)
                                    elif choice == "2":
                                        top_up_account(username)
                                    else:
                                        raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
                                except ValueError as e:
                                    print(e)
                                except TypeError as e:
                                    print("Invalid input, input must be a number")
                        user_accounts[username]["inventory"].append([titles[number-1]])
                        user_accounts[username]["balance"] -= game_library[titles[number-1]]["cost"]
                        game_library[titles[number-1]]["quantity"] -= 1
                        while x != 1:
                            print("Game added to inventory\n(1)Rent another game\n(2)Go back to menu")
                            choice = input("Input here: ")
                            try:
                                if choice == "1":
                                    rent_game(username)
                                elif choice == "2":
                                    logged_in_menu(username)
                                else:
                                    raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
                            except ValueError as e:
                                print(e)
                            except TypeError as e:
                                print("Invalid input, input must be a number")
                    elif confirm_purchase == "2":
                        rent_game(username)
                    else:
                        raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
                except ValueError as e:
                    print(e)
                except TypeError as e:
                    print("Invalid input, input must be a number")
            if number > no_of_options or number < no_of_options:
                raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print("Invalid input, input must be a number")

# Function to return a game
def return_game(username):
    print("Return Game".center(30, "-"))
    while x != 1:
      print("Enter the number of the game you want to return or (0) to go back to menu")
      display_game_inventory(username)
      option = input("Input here: ")
      number = int(option)
      no_of_options = len(user_accounts[username]["inventory"])
      try:
          if option == "0":
              logged_in_menu(username)
          elif 0 > number or no_of_options < number:
              raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
          print(f"Are you sure you want to return {user_accounts[username]["inventory"][number-1]}?\nenter (1) to proceed or (2) to cancel purchase")
          confirm_return = input("Input here: ")
          if confirm_return == "1":
              game_library[user_accounts[username]["inventory"][number-1][0]]["quantity"] += 1
              user_accounts[username]["inventory"].remove(user_accounts[username]["inventory"][number-1])
              print("Game returned successfully!")
              return_game(username)
          elif confirm_return == "2":
              return_game(username)
          else:
              raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
      except ValueError as e:
          print(e)
      except TypeError as e:
          print("Invalid input, input must be a number")

# Function to top-up user account
def top_up_account(username):
    print("Top up".center(30, "-"))
    while x != 1:
      print("(1)Increase balance\n(2)Return to menu")
      option = input("Input here: ")
      try:
          if option == "1":
              print(f"Current balance is ${user_accounts[username]["balance"]} how much do you want to add")
              amount = input("amount: ")
              print(f"Are you sure you want to add ${amount} to your balance?\nenter (1) to proceed or leave it blank to cancel transaction")
              choice = input("Input here: ")
              if choice == "1":
                  if int(amount) < 0:
                      raise ValueError("Cannot add negative amount to balance")
                  user_accounts[username]["balance"] += float(amount)
                  print(f"Balance increased! New balance is ${user_accounts[username]["balance"]}")
                  logged_in_menu(username)
              elif choice is False:
                  print("transaction cancelled")
                  top_up_account(username)
              else:
                  raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
          elif option == "2":
              logged_in_menu(username)
          else:
              raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
      except ValueError as e:
          print(e)
      except TypeError as e:
          print("Invalid input, input must be a number")

# Function to display user's inventory
def display_inventory(username):
    print("Inventory".center(30, "-"))
    print(f"Rented games".center(20) + f"balance = {user_accounts[username]["balance"]}\tpoints = {user_accounts[username]["points"]}")
    game_number = 1
    for game in user_accounts[username]["inventory"]:
        print(f"({game_number}) {game}\t")
        game_number += 1
    while x != 1:
        print("Enter (1) to go back to menu")
        option = input ("Input here: ")
        try:
            if option == "1":
                logged_in_menu(username)
            else:
                raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print("Invalid input, input must be a number")

# Function for admin to update game details
def admin_update_game():
    while x != 1:
        print("(1)Add Game\n(2)Edit Detail\n(3)Go back to menu")
        option = input("Input here: ")
        try:
            if option == "1":
                print("Add game".center(30, "-"))
                title = input("Input title: ")
                quantity = input("Input Quantity: ")
                cost = input("Input cost: ")
                game_library[title] = {"quantity": quantity, "cost": cost}
                print("Game added Successfully!\nEnter (1) to Continue editing or (2) to Go back to menu")
                choice = input("Input here: ")
                if choice == "1":
                    admin_update_game()
                elif choice == "2": 
                    admin_menu()
            elif option == "2":
                display_available_games()
                print("Enter the number of the game you want to edit")
                title = input ("Input here: ")
                quantity = input("New quantity: ")
                cost = input("New cost: ")
                game_library_keys = list(game_library.keys())
                game_library[game_library_keys[int(title)-1]] = {"quantity": quantity, "cost": cost}
                while x != 1:
                    print("Game successfully edited!\nEnter (1) to Continue editing\n or (2) to Go back to menu")
                    choice = input("Input here: ")
                    try:
                        if choice == "1":
                            admin_update_game()
                        elif choice == "2": 
                            admin_menu()
                        else:
                            raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
                    except ValueError as e:
                        print(e)
                    except TypeError as e:
                        print("Invalid input, input must be one of the numbers enclosed in paranthesis")
            elif option == "3":
                admin_menu()
            else:
                raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print("Invalid input, input must be a number")

# Function for admin login
def admin_login():
    print("Admin login".center(30, "-"))
    username = input("Username: ")
    x = 0
    if username == admin_username:
        password = input("Password: ")
        if password == admin_password:
            admin_menu()
        else:
            while x != 1:
                print("Incorrect password, input (1) to try again or (2) to go back to menu")
                option = input("Input here: ")
                try:
                    if option == "1":
                        admin_login()
                    elif option == "2":
                        main()
                    else:
                        raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
                except ValueError as e:
                    print(e)
                except TypeError as e:
                    print("Invalid input, input must be a number")
    else:
        while x!= 1:
            print("Incorrect username for admin, input (1) to try again or (2) to go back to menu")
            option = input("Input here: ")
            try:
                if option == "1":
                    admin_login()
                elif option == "2":
                    main()
                else:
                    raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
            except ValueError as e:
                print(e)
            except TypeError as e:
                print("Invalid input, input must be a number")

# Admin menu
def admin_menu():
    print("Admin".center(30, "-"))
    while x != 1:
        print("Welcome admin!, Input the number of your chosen action\n(1)View game library\n(2)Update game library\n(3)Logout")
        option = input("Input here: ")
        try:
            if option == "1":
                display_available_games()
                while x != 1:
                  print("Enter (1) to go back to menu")
                  choice = input("Input here: ")
                  try:
                    if choice == "1":
                        admin_menu()
                    else:
                      raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
                  except ValueError as e:
                    print(e)
                  except TypeError as e:
                    print("Invalid input, input must be a number")
            elif option == "2":
                admin_update_game()
            elif option == "3":
                main()
            else:
                raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print("Invalid input, input must be a number")

# Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    print("Free points".center(30, "-"))
    user_accounts[username]["points"] += 1
    while x != 1:
        print(f"Congratulations, you have claimed your daily free point\nYou now have {user_accounts[username]["points"]} points.\n(1)go back to menu\n(2)Convert to balance\n(3)Rent a game")
        option = input("Input here: ")
        try:
            if option == "1":
                logged_in_menu(username)
            elif option == "2":
                while x != 1:
                    print("How much would you like to convert?")
                    amount = input("Input here: ")
                    try:
                        if int(amount) > user_accounts[username]["points"]:
                            raise ValueError("Input must be less than or equal to your current points")
                        elif int(amount) < 0:
                            raise ValueError("Input must be less than or equal to your current points")
                        else:
                            user_accounts[username]["points"] - int(amount)
                            user_accounts[username]["balance"] += int(amount)*3
                            print(f"Points added to balance, you new balance is {user_accounts[username]["balance"]}\n(1)go back to menu\n(2)Rent a game")
                            while x != 1:
                                choice = input("Input here: ")
                                try:
                                    if choice == "1":
                                        logged_in_menu(username)
                                    elif choice == "2":
                                        rent_game(username)
                                    else:
                                        raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
                                except ValueError as e:
                                    print(e)
                                except TypeError as e:
                                    print("Invalid input, input must be a number")
                    except ValueError as e:
                        print(e)
                    except TypeError as e:
                        print("Invalid input, input must be a number")
            elif option == "3":
                rent_game(username)
            else:
                raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print("Invalid input, input must be a number")

def display_game_inventory(username):
    print(f"Rented games".center(20) + f"balance = {user_accounts[username]["balance"]}\tpoints = {user_accounts[username]["points"]}")
    game_number = 1
    for game in user_accounts[username]["inventory"]:
        print(f"({game_number}) {game}\t")
        game_number += 1

# Function to handle user's logged-in menu
def logged_in_menu(username):
    print(f"Welcome {username}".center(30, "-"))
    while x != 1:
        print("Input the number of your chosen action\n(1)Rent a game\n(2)Return a game\n(3)Top up your account\n(4)Claim free point\n(5)View inventory\n(6)Check credentials\n(7)Logout")
        option = input("Input here: ")
        try:
            if option == "1":
                rent_game(username)
            elif option == "2":
                return_game(username)
            elif option == "3":
                top_up_account(username)
            elif option == "4":
                redeem_free_rental(username)
            elif option == "5":
                display_inventory(username)
            elif option == "6":
                check_credentials(username)
            elif option == "7":
                main()
            else:
                raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print("Invalid input, input must be a number")

# Function to check user credentials
def check_credentials(username):
    print("Credentials".center(30, "-"))
    print(f"Username: {username}\nPassword: {user_accounts[username]["password"]}")
    while x != 1:
        print("Input (1) to go back to menu")
        option = input("Input here: ")
        try:
            if option == "1":
                logged_in_menu(username)
            else:
                raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print("Invalid input, input must be a number")

def log_in():
    print("Login".center(30,"-"))
    username = input("Username: ")
    for account_name in user_accounts.keys():
        if username == account_name:
            password = input("Password: ")
            if user_accounts[username]["password"] == password:
                    logged_in_menu(username)
            else:
                while x != 1:
                    print("Incorrect password, input (1) to try again or (2) to go back to menu")
                    option = input("Input here: ")
                    try:
                        if option == "1":
                            log_in()
                        elif option == "2":
                            main()
                        else:
                            raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
                    except ValueError as e:
                        print(e)
                    except TypeError as e:
                        print("Invalid input, input must be a number")
    while x!= 1:
        print("Username does not exist, input (1) to try again or (2) to go back to menu")
        option = input("Input here: ")
        try:
            if option == "1":
                log_in()
            elif option == "2":
                main()
            else:
                raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print("Invalid input, input must be a number")

    
# Main function to run the program
def main():
    print("Main menu".center(30, "-"))
    while x != 1:
        print("Enter the number for your chosen action\n(1)User Login\n(2)Admin login\n(3)Sign up")
        option = input("Input here: ")
        try:
            if option == "1":
                log_in()
            elif option == "2":
                admin_login()
            elif option == "3":
                register_user()
            else:
                raise ValueError("Invalid input, input must be one of the numbers enclosed in paranthesis")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print("Invalid input, input must be a number")

if __name__ == "__main__":
    main()
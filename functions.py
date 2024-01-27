
def list_helper(list_menu, restaurant_menu_list, spicy_scale_map):
    if len(restaurant_menu_list) == 0:
        print("WARNING: There is nothing to display!")
        # Pause before going back to the main menu
        input("::: Press Enter to continue")
    else:
        subopt = get_selection("List", list_menu)
        if subopt == 'A':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1)
        elif subopt == 'V':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1, vegetarian_only=True)

######## LIST OPTION ########

def get_selection(action, suboptions, to_upper=True, go_back=False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu
    The function displays a submenu for the user to choose from.
    Asks the user to select an option using the input() function.
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.
    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What field would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper()  # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=False, show_idx=True, start_idx=0, vegetarian_only=False):
    """
    param: restaurant_menu (list) - a list object that holds the dictionaries for each dish
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
    param: name_only (Boolean)
            If False, then only the name of the dish is printed.
            Otherwise, displays the formatted dish information.
    param: show_idx (Boolean)
            If False, then the index of the menu is not displayed.
            Otherwise, displays the "{idx + start_idx}." before the
            dish name, where idx is the 0-based index in the list.
    param: start_idx (int)
            an expected starting value for idx that
            gets displayed for the first dish, if show_idx is True.
    param:  vegetarian_only (Boolean)
            If set to False, prints all dishes, regardless of their
            is_vegetarian status ("yes/no" field status).
             If set to True , display only the dishes with
            "is_vegetarian" status set to "yes".
    returns: None; only prints the restaurant menu
    """
    print('------------------------------------------')
    for i, dish in enumerate(restaurant_menu_list):
        
        # if vegetarian_only is True and the dish is not vegetarian, skip
        if vegetarian_only == True and dish['is_vegetarian'] == 'no':
            continue
        # if the index of the task needs to be displayed (show_idx is True), print dish index only
        if show_idx == True:
            print(start_idx, end='. ')
            start_idx += 1
        print(dish["name"].upper())
            
        #if name_only is False
        if not name_only:
            
            print(f"* Calories: {dish['calories']}")
            print(f"* Price: {dish['price']:.1f}")
            print(f"* Is it vegetarian: {dish['is_vegetarian']}")
            print(f"* Spicy level: {spicy_scale_map[dish['spicy_level']]}")
            print()

    print('------------------------------------------')
            
def is_num(s):
    """
    Takes in a string s and returns True if it represents a number (either an integer or a decimal).
    """
    try:
        int(float(s))
        return True
    except ValueError:
        return False

def is_valid_name(name):
    """
    Takes in the name of a dish and checks whether it is the right length - between 3 and 25 characters, inclusive of both.
    """
    if isinstance(name, str) and 3 <= len(name) <= 25:
        return True
    else:
        return False

def is_valid_spicy_level(spicy_level, spicy_scale_map):
    """
    Takes in a string representing level of spiciness as an int, as well as a dictionary that maps levels of spiciness to their english description, and checks whether the string is a valid level of spiciness according to the dict.
    """
    if isinstance(spicy_level, str) and spicy_level.isdigit():
        spicy_level = int(spicy_level)
        if spicy_level in spicy_scale_map.keys():
            return True
    return False

def is_valid_is_vegetarian(is_vegetarian):
    """
    Takes in a string representing whether a dish is vegetarian and checks whether it is either "yes" or "no".
    """
    if isinstance(is_vegetarian, str) and is_vegetarian.lower() in ['yes', 'no']:
        return True
    else:
        return False

def is_valid_calories(calories):
    """
    Takes in a string representing a dish's calories, checks that it corresponds to an integer.
    """
    if isinstance(calories, str) and calories.isdigit():
        return True
    else:
        return False

def is_valid_price(price):
    """
    Takes in a string representing a dish's price, checks whether its a numerical value or not by calling is_num function inside it.
    """
    if isinstance(price, str) and is_num(price):
        return True
    else:
        return False

def get_new_menu_dish(menu_dish_list, spicy_scale_map):
    """
    Takes in a list of strings representing dish attributes and a dictionary that maps levels of spiciness to their english description.
    Validates the input list one element at a time before transforming it into a dictionary.
    Returns the dictionary object if validation is successful, otherwise returns a tuple with the name of the invalid parameter and the value it had.
    """
    if len(menu_dish_list) != 5:
        return len(menu_dish_list)

    name = menu_dish_list[0]
    calories = menu_dish_list[1]
    price = menu_dish_list[2]
    is_vegetarian = menu_dish_list[3]
    spicy_level = menu_dish_list[4]

    if not is_valid_name(name):
        return ("name", name)

    if not is_valid_calories(calories):
        return ("calories", calories)

    if not is_valid_price(price):
        return ("price", price)

    if not is_valid_is_vegetarian(is_vegetarian):
        return ("is_vegetarian", is_vegetarian)

    if not is_valid_spicy_level(spicy_level, spicy_scale_map):
        return ("spicy_level", spicy_level)

    return {
        "name": name,
        "calories": int(calories),
        "price": float(price),
        "is_vegetarian": is_vegetarian.lower(),
        "spicy_level": int(spicy_level)
    }
def print_dish(dish, spicy_scale_map, name_only=False):
    """
    param: dish (dict) - a dictionary object that is expected to contain the following keys:
            - "name": dish's name
            - "calories": calories for this dish
            - "price": price of this dish
            - "is_vegetarian": boolean whether this dish is for vegetarian
            - "spicy_level": integer that represents the level of spiciness
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
            values for each corresponding key are string description of the
            level of spiciness
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the dish is printed.
            Otherwise, displays the formatted restaurant menues.
    returns: None; only prints the restaurant menu item
    """
    
    
    if name_only == True:
        print(dish["name"].upper())
    else:
        print(dish["name"].upper())
        print(f"* Calories: {dish['calories']}")
        print(f"* Price: {dish['price']:.1f}")
        print(f"* Is it vegetarian: {dish['is_vegetarian']}")
        print(f"* Spicy level: {spicy_scale_map[dish['spicy_level']]}")
        print()
    return None
    
def add_helper(restaurant_menu_list, spicy_scale_map):
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter each required field, separated by commas.")
        # * `name` : name of the dish
        #     * `calories`: number of calories per serving
        #     * 'is_vegetarian' : if the item is vegetarian
        #     * `price` : price of the item
        #     * 'spicy_level' : 1 - 4
        print("::: name of the dish, calories, price, is it vegetarian ( yes | no ), spicy_level ( 1-4 )")
        dish_data = input("> ")  # get the data 
        dish_values = dish_data.split(",") # process the data into a list
        result_dict = get_new_menu_dish(..., spicy_scale_map)  # TODO: attempt to create a new dish for the menu
        if type(result_dict) == dict:
            restaurant_menu_list.append(...)  # TODO: add a new dish to the list of dish menus
            print(f"Successfully added a new dish!")
            print_dish(result_dict, spicy_scale_map)
        elif type(result_dict) == int:
            print(f"WARNING: invalid number of fields!")
            print(f"You provided {result_dict}, instead of the expected 5.\n")
        else:
            print(f"WARNING: invalid dish field: {result_dict}\n")

        print("::: Would you like to add another dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()
def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    print("==========================")
    print("What would you like to do?")
    for key, value in menu.items():
        print(f"{key} - {value}")
    print("==========================")
    
def delete_item(in_list, idx, start_idx=0):
    """
    param: in_list - a list from which to remove an item
    param: idx (str) - a string that is expected to
            contain a representation of an integer index
            of an item in the provided list
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing
    The function first checks if the input list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from info_list.
    On success, the function saves the item from info_list
    and returns it after it is deleted from in_list.
    returns:
    If the input list is empty, return 0.
    If idx is not of type string, return None.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from the input list.
    Helper functions:
    - is_valid_index()
    """
    if in_list == []:
        return 0
    if type(idx) != str:
        return None
    if not(is_valid_index(idx, in_list, start_idx)):
        return -1

    deleted = in_list[int(idx) - start_idx]
    in_list.pop(int(idx) - start_idx)
    return deleted

def delete_helper(restaurant_menu_list, spicy_scale_map):
    continue_action = 'y'
    while continue_action == 'y':
        if not restaurant_menu_list:
            print("WARNING: There is nothing to delete!")
            break
        print("Which dish would you like to delete?")
        print("Press A to delete the entire menu for this restaurant, M to cancel this operation")
        print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=True, show_idx=True, start_idx=1)
        user_option = input("> ")
        if user_option == "A" or user_option == "a":
            print(f"::: WARNING! Are you sure you want to delete the entire menu ?")
            print("::: Type Yes to continue the deletion.")
            user_option = input("> ")
            if user_option == "Yes" or user_option == "yes" :
                restaurant_menu_list = ...
                print(f"Deleted the entire menu.")
            else:
                print(f"You entered '{No}' instead of Yes.")
                print("Canceling the deletion of the entire menu.")
            break
        elif user_option == 'M' or user_option == 'm':
            break
        result = delete_dish(restaurant_menu_list, user_option, 1)
        if type(result) == dict:
            print("Success!")
            print(f"Deleted the dish |{result['name']}|")
        elif result == 0:  # delete_item() returned an error
            print("WARNING: There is nothing to delete.")
        elif result == -1:  # is_valid_index() returned False
            print(f"WARNING: |{user_option}| is an invalid dish number!")

        print("::: Would you like to delete another dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()
    return restaurant_menu_list

def save_menu_to_csv(restaurant_menu_list, filename):
    """
    param: restaurant_menu_list(list of dict) - The list shore dictionary of dishes 
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the menu items. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every dishes dictionary in the dictionaries list and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:
    * name
    * calories
    * price
    * is_vegetarian
    * spicy_level
    
    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        csv_writer.writerow(['name', 'calories', 'price', 'is_vegetarian', 'spicy_level'])
        
        for item in restaurant_menu_list:
            string_list = [item['name'], item['calories'], item['price'], item['is_vegetarian'], item['spicy_level']]
            csv_writer.writerow(string_list)
            
    import csv
    import os
    
def save_helper(restaurant_menu_list):
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = save_menu_to_csv(restaurant_menu_list, filename)  # TODO: Call the function with appropriate inputs and capture the output
        if result == 'n':  # TODO
            print(f"WARNING: |{file_name}| is an invalid file name!")  # TODO
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully saved restaurant menu to |{saved_menu.csv}|")
            break

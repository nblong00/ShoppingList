import datetime
import csv
import utils
import logging

logging.basicConfig(filename="script.log", level=logging.DEBUG)

def welcome(name):
    dt = datetime.datetime.now()
    print("\nHello {},".format(name))
    print(f"Today's date is: {dt.strftime("%B %d, %Y")}")
    print("Welcome to the shopping list simulator!\n")
    print("What do you need to pick up at the store?")

    
def add_to_list(item, shopping_list):
    print(("* If the item was added by mistake or incorrectly, enter DELETE, otherwise, provide the item's price"))
    user_response = input("> ")
    if user_response.title() == "Delete":
        pass
    else: 
        item_cost = float(user_response)
        shopping_list_altered = utils.write_item(item, item_cost, shopping_list) 

        print(f"{item} has been added to the list")
        print(f"Shopping list currently contains {len(shopping_list)} item(s).")
        return shopping_list_altered


def del_row(shopping_list):
    del_item = input("Enter name of item to delete:\n> ").title()
    initial_length = len(shopping_list)
    shopping_list_altered = [entry for entry in shopping_list if entry['item'] != del_item]

    if len(shopping_list_altered) < initial_length:
        with open('data.csv', 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', lineterminator='')
            writer.writerow(['item', 'cost'])  
            for entry in shopping_list_altered:
                utils.csv_new_line(csvfile)
                writer.writerow([entry['item'], entry['cost']])
        print(f"{del_item} has been removed from the list.")
        logging.debug(f"deleted item: {del_item}")
        show_list(shopping_list)
        return shopping_list_altered
    else:
        print(f"{del_item} not found in the list.")
        print("Use the LIST command to see items currently in list.")
        return shopping_list

    
def show_list(shopping_list): 
    print()
    print("Here is your current list:\n")
    for index, item in enumerate(shopping_list, 1):
        print(f"{index}. {item['item']} - ${item['cost']}")
    print()

    
def main():
    shopping_list = []
    human_name = input("Enter your name: ").title()

    welcome(human_name)
    utils.show_help()
    shopping_list = utils.read_items(shopping_list)

    while True:
        new_item = input("> ")
        if new_item.upper() == "DONE":
            break
        elif new_item.lower() == "help":
            print("\n    Help Menu:")
            utils.show_help()
            continue
        elif new_item.lower() == "list":
            show_list(shopping_list)
            continue
        elif new_item.lower() == "delete":
            shopping_list = del_row(shopping_list)
            continue
        else:
            shopping_list = add_to_list(new_item.title(), shopping_list)  


main()   
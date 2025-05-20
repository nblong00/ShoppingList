import datetime
import csv

shopping_list = []


def welcome(name):

    dt = datetime.datetime.now()

    print()
    print("Hello {},".format(name))
    print(f"Today's date is: {dt.strftime("%B %d, %Y")}")
    print("Welcome to the shopping list simulator!")
    print()

def show_help(loop_runs):
    if loop_runs < 1:
        print("What do you need to pick up at the store?")
        print("""
    Enter 'DONE' to stop adding items. 
    Enter 'HELP' for this help.
    Enter 'LIST' to list current items added.
    Enter 'DELETE' to remove item from list.
    """)
    else: 
        print("""
    Help Menu:         

    Enter 'DONE' to stop adding items. 
    Enter 'HELP' for this help.
    Enter 'LIST' to list current items added.
    Enter 'DELETE' to remove item from list.
    """)

def load_data():

    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            shopping_list.append({
                'item': row['item'],
                'cost': row['cost'],
            })    
    
def add_to_list(item):
    
    print(("* If the item was added by mistake or incorrectly, enter DELETE, otherwise, provide the item's price"))
    user_response = input("> ")
    if user_response.title() == "Delete":
        pass
    else: 
        item_cost = float(user_response)
        with open('data.csv', 'a+', newline='') as csvfile:
            lastchar = csvfile.read(1)
            if lastchar != '\n':
                csvfile.write('\n')
            writer = csv.writer(csvfile, delimiter=',', lineterminator='')
            writer.writerow([item, item_cost])

            shopping_list.append({
                'item': item,
                'cost': item_cost,
            })    

            print(f"{item} has been added to the list")
            print(f"Shopping list currently contains {len(shopping_list)} item(s).")

def del_row():
    global shopping_list
    del_item = input("Enter name of item to delete:\n> ")

    initial_length = len(shopping_list)
    shopping_list[:] = [entry for entry in shopping_list if entry['item'] != del_item]

    if len(shopping_list) < initial_length:
        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', lineterminator='')
            writer.writerow(['item', 'cost'])  
            for entry in shopping_list:
                writer.writerow([entry['item'], entry['cost']])
        print(f"{del_item} has been removed from the list.")
    else:
        print(f"{del_item} not found in the list.")
        print("Use the LIST command to see items currently in list.")

def show_list():
    
    print()
    print("Here is your current list:\n")
    for index, item in enumerate(shopping_list, 1):
        print(f"{index}. {item['item']} - ${item['cost']}")
    print()
    
def main():

    human_name = input("Enter your name: ").title()
    loop_passes = 0

    welcome(human_name)
    show_help(loop_passes)
    load_data()
    while True:
        if loop_passes < 1:
            loop_passes += 1
        new_item = input("> ")
        if new_item.upper() == "DONE":
            break
        elif new_item.lower() == "help":
            show_help(loop_passes)
            continue
        elif new_item.lower() == "list":
            show_list()
            continue
        elif new_item.lower() == "delete":
            del_row()
            continue
        add_to_list(new_item.title())  

main()   
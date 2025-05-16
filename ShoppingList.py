import datetime
import csv

shopping_list = []


def welcome(name):

    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            shopping_list.append({
                'item': row['item'],
                'cost': row['cost'],
            })

    dt = datetime.datetime.now()

    print()
    print("Hello {},".format(name))
    print(f"Today's date is: {dt.strftime("%B %d, %Y")}")
    print("Welcome to the shopping list simulator!")
    print()
    print(shopping_list)

def show_help(loop_runs):
    if loop_runs < 1:
        print("What do you need to pick up at the store?")
        print("""
    Enter 'DONE' to stop adding items. 
    Enter 'HELP' for this help.
    Enter 'LIST' to list current items added.
    """)
    else: 
        print("""
    Help Menu:         

    Enter 'DONE' to stop adding items. 
    Enter 'HELP' for this help.
    Enter 'LIST' to list current items added.
    """)
    
    
def add_to_list(item):
    
    shopping_list.append(item) 
    print(("* If the item was added by mistake or incorrectly, enter DELETE, otherwise, provide the item's price"))
    user_response = input("> ")
    if user_response.title() == "Delete":
        del(shopping_list[shopping_list.index(item)])
    else: 
        item_cost = float(user_response)
        item_prices.append(item_cost)
        print(f"{item} has been added to the list")
        print(f"Shopping list currently contains {len(shopping_list)} item(s).")
    
    
def show_list():
    
    print("Here is your current list:")
    for index, item in enumerate(shopping_list, 1):
        item_index = shopping_list.index(item)
        print(f"{index}. {item} - ${item_prices[item_index]}")

def save_list():
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([shopping_list, item_prices])
    
def main():

    human_name = input("Enter your name: ").title()
    loop_passes = 0

    welcome(human_name)
    show_help(loop_passes)
    while True:
        if loop_passes < 1:
            loop_passes += 1
        new_item = input("> ")
        if new_item.upper() == "DONE":
            save_list()
            break
        elif new_item.lower() == "help":
            show_help(loop_passes)
            continue
        elif new_item.lower() == "list":
            show_list()
            continue
        add_to_list(new_item.title())  

main()   

shopping_list = []
item_prices = []

def welcome(name):
    print()
    print("Hello {},".format(name))
    print("Welcome to the shopping list simulator!")
    print()

def show_help():
    print("What do you need to pick up at the store?")
    print("""
Enter 'DONE' to stop adding items. 
Enter 'HELP' for this help.
Enter 'LIST' to list current items added.
""")
    
    
def add_to_list(item):
    item_cost = float(input("How much does this item cost?\n> "))
    item_prices.append(item_cost)
    shopping_list.append(item) 
    print("{} has been added to the list".format(item))
    print("Shopping list currently contains {} item(s).".format(len(shopping_list)))
    
    
def show_list():
    
    item_number = 1
    print("Here is your current list:")
    for item in shopping_list:
        item_index = shopping_list.index(item)
        print("{}. {} - ${}".format(item_number, item, item_prices[item_index]))
        item_number += 1
    

human_name = input("Enter your name: ").title()

welcome(human_name)
show_help()
while True:
    new_item = input("> ")
    if new_item.upper() == "DONE":
        break
    elif new_item.lower() == "help":
        show_help()
        continue
    elif new_item.lower() == "list":
        show_list()
        continue  
    add_to_list(new_item.title())     
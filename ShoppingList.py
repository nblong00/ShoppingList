
shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items. 
Enter 'HELP' for this help.
Enter 'LIST' to list current items added.
""")
    
    
def add_to_list(item):
    shopping_list.append(item) 
    print("{} has been added to the list".format(item))
    print("Shopping list currently contains {} item(s).".format(len(shopping_list)))
    
    
def show_list():
    
    item_number = 1
    print("Here is your current list:")
    for item in shopping_list:
        print("{}. {}".format(item_number, item))
        item_number += 1
    
    
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
        
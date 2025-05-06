# Create a new empty list named shopping_list

shopping_list = []

# Create function named add_to_list that declares a parameter named item
    # Add item to list
def add_to_list(item):
    shopping_list.append(item) 
    print("{} has been added to the list".format(item))
    print("Shopping list currently contains {} item(s).".format(len(shopping_list)))
    #notify user item was added
    #state number of items in list
    
def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items. 
Enter 'HELP' for this help.
""")
    
show_help()

while True:
    new_item = input("> ")
    
    if new_item.upper() == "DONE":
        break
    elif new_item.lower() == "help":
        show_help()
        continue
          
    add_to_list(new_item.title())
        
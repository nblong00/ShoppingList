import csv

def write_item(item, item_cost, shopping_list):
    with open('data.csv', 'a+', newline='') as csvfile:
        csv_new_line(csvfile)
        writer = csv.writer(csvfile, delimiter=',', lineterminator='')
        writer.writerow([item, item_cost])
        shopping_list.append({
            'item': item,
            'cost': item_cost,
        })
    return shopping_list

def read_items():
    pass

def csv_new_line(csvfile):
    lastchar = csvfile.read(1)
    if lastchar != '\n':
        csvfile.write('\n')

def show_help():
    print("""
    Enter 'DONE' to stop adding items. 
    Enter 'HELP' for this help.
    Enter 'LIST' to list current items added.
    Enter 'DELETE' to remove item from list.
    """)
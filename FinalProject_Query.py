"""
Anthony Martinez
ID - 2187242

This Project will deal with the whole query system that will output results depending
on the inputs from the User. It will ignore inputs that are not found in our table/list.
Will be using functions found on my last project.


"""

# Importing this so that I can get the full inventory.
import manageInv as mInv




class Inventory:
    def __init__(self, file) -> None:
        # This is the full inventory of the ID, company, laptop, cost, date, if Damage.
        self._fullInv = mInv.run(file)


    # This will go ahead and find the item we are looking for.
    def query_items(self, manufacturer, item_type):
        found_items = []
        # Iterate through the keys and values in _fullInv
        for key, value in self._fullInv.items():
            # Check if the manufacturer, item type, and status are correct
            if value[0] == manufacturer and value[1] == item_type and value[-1] != 'damaged':
                found_items.append([key] + value)  # Append the key and value as a list
            
        if not found_items:
            print("No such item in inventory")
            return
        
        # Sort found_items by cost (index 3) in descending order
        found_items.sort(key=lambda x: x[3], reverse=True)
        output_item = found_items.pop(0)

        print(f"Your item is: {output_item[0]} {output_item[1]} {output_item[2]} ${output_item[3]}")
        if len(found_items) > 1:
            print("Your may also consider:")
            for items in found_items:
                print(items[0], items[1], items[2], items[3])


    def extract_keywords(self, user_input):
        # Extract manufacturers and item types from _fullInv
        manufacturers = set([self._fullInv[key][0] for key in self._fullInv])
        item_types = set([self._fullInv[key][1] for key in self._fullInv])

        # Initialize variables to store extracted manufacturer and item type
        manufacturer = None
        item_type = None

        # Split the user input into words
        words = user_input.split()

        # Iterate through the words in the user input
        for word in words:
            # Check if the word matches a known manufacturer
            if word.capitalize() in manufacturers:
                manufacturer = word.capitalize()
            # Check if the word matches a known item type
            elif word.lower() in item_types:
                item_type = word.lower()

        return manufacturer, item_type



def main():




    files = ['ManufacturerList.txt', 'PriceList.txt', 'ServiceDatesList.txt']
    inv = Inventory(files)

    while True:
        user_input = input("Please input what kind of system you are looking for. Input 'q' to quit. \n")
        if user_input.lower() == "q":
            break
        manufacturer, item_type = inv.extract_keywords(user_input)
        print("===========================")
        print("Manufacturer:", manufacturer)
        print("Item type:", item_type)
        print("===========================")
        inv.query_items(manufacturer, item_type)
        print("===========================")

if __name__ == "__main__":
    main()
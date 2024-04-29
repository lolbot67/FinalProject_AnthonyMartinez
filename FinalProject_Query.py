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
        self._fullInv = mInv.run()
    # This will go ahead and find the item we are looking for.
    def query_items(self, manufacturer, item_type):
        found_items = []
        # Will be listing the keys
        for key in self._fullInv.keys():
            # My statement to find the correct manufacturer and type that the user is finding
            if self._fullInv[key][0] == manufacturer and self._fullInv[key][1] == item_type and self._fullInv[key][-1] != 'damaged':
                found_items.append([[key] + self._fullInv[key]])
        if not found_items:
            print("No such item in inventory")
            return
        # Order it by the cost so that the highest cost will be first one and be recommended for User.
        found_items.sort(key=lambda x: x[3], reverse=True)
        output_item = found_items[0]

        print(f"Your item is: {output_item[0]} {output_item[1]} {output_item[2]} ${output_item[3]}")
        print("Your may also consider:")
        for items in found_items:
            print(items[0], items[1], items[2], items[3])





def main():
    files = ['ManufacturerList.txt', 'PriceList.txt', 'ServiceDatesList.txt']
    inv = Inventory(files)
    userInp = ""

    while userInp != "q":
        userInp = input("Please input what kind of system you are looking for. input 'q' to quit.")
        print("yes")
    print(inv._fullInv)



if __name__ == "__main__":
    main()
"""
ManageInv.py
Anthony Martinez
UH ID - 2187242

This program will take input from ManufacturerList, PriceList, and ServiceDatesList which are all txt files and output them with ordered and proper
table onto 3 different output txt. The output txt files should be named FullInventory, LaptopInventory, PastServiceDateInventory, and DamagedInventory
which each output will have their own respective formats.

FullInventory.txt
contain item ID, manufacturer name, item type, price, service date, and list if it is damaged.

LaptopInventory.txt
contain item ID, manufacturer name, price, service date, and list if it is damaged.

PastServiceDateInventory.txt
contain:  item ID, manufacturer name, item type, price, service date, and list if it is damaged.

DamagedInventory.txt
contain:  item ID, manufacturer name, item type, price, and service date. 
"""
# since I am working with date for PasServiceDateInv I would need import datetime
from datetime import datetime, timedelta

# This program will go ahead and seperate all information from the input files to dictionary lists.
def fileToDict(lst):
    # mem is my list memory which I will place all my result in order
    mem = {}
    # Creating a list to 
    for fileTxt in lst:
        with open(fileTxt, 'r') as file:
            # Reading line by line to seperate them in list to place them in my mem dict.
            for line in file:
                # striping any spaces and spliting per lines by a comma
                txt = line.strip().split(',')
                # seperating my key from my 
                key = txt[0]
                values = txt[1:]
                if key in mem:
                    mem[key] += values
                else: 
                    mem[key] = values
    # Checking if it's damage to place at the end to have the same format.
    keys = mem.keys()
    for key in keys:
        if 'damaged' in mem[key]:
            mem[key].remove('damaged')
            mem[key].append('damaged')
    return mem




# This program will create my first output which is FullInventory which will help me create the other 3.
def fullInventory(dict):
    # Now that I have my dictionary from my function filesToDict will now sort them with the proper format.
    # dict = dictionary

    # sorting my dictionary 
    sortedDict = {key: value for key, value in sorted(dict.items(), key=lambda item: item[1])}
    with open('MySolution/FullInventory.txt', 'w') as fullInv:
        for key in sortedDict.keys():
            string = f"{key}"
            for lst in sortedDict[key]:
                # String will contain ID, manufacturer name, item type, price, service date, and list if it is damaged.
                string += ',' +lst
            fullInv.writelines(string + '\n')
    return sortedDict



# Now going to do ManufacturerList txt file item ID, manufacturer name, price, service date, and list if it is damaged.
def laptopInventory(dict):
    # Sorting by key ID as requested
    sortedDict = {k: dict[k] for k in sorted(dict)}
    # opening manufacturingLst file to write
    with open('MySolution/LaptopInventory.txt', 'w') as laptInv:
        for key in sortedDict.keys():
            # checking if it's a laptop or not
            if 'laptop' in sortedDict[key]:
                # Since we already formated the dictionary list we could just pull from these 3 spots to always have the same solution
                string = f'{key},{sortedDict[key][0]},{sortedDict[key][2]},{sortedDict[key][3]}'
                # If damaged in the list we just added onto the end.
                if 'damaged' in sortedDict[key]:
                    string += ',damaged'
                # writing my string info with format as item ID, manufacturer name, price, service date, and list if it is damaged.
                laptInv.write(string +'\n')


# Now working for PastServiceDateInventory to output any system that has been expired. 
def pastServiceDateInv(dict):
    # Sorting the dict by the date now instead of later. 
    sortedDict = {key: value for key, value in sorted(dict.items(), key=lambda item: datetime.strptime(item[1][3], "%m/%d/%Y"))}
    # Getting current date when application is run.
    currentDate = datetime.now()
    with open('MySolution/PastServiceDateInventory.txt', 'w') as pastServiceFile:
        # Now will iterate, format, and check if date is expired.
  
        for key in sortedDict.keys():
            serviceDate = sortedDict[key][3]
            # Now will format ServiceDate so that I can compare with Today date. Month/Day/Year
            serviceDate = datetime.strptime(serviceDate, "%m/%d/%Y")
            # Checking if date is passed the date and write if it's past the service date.
            if currentDate > serviceDate:
                # creating string with format 
                string = f'{key}'
                for txt in sortedDict[key]:
                    string += f',{txt}'
                pastServiceFile.write(string + '\n')
            # Since most of the date are from 2020 all of them is writable however, I did check that it does work if I change the year

# Now creating a function to output a file items that are damaged or not.
def damagedInv(dict):
    # Sorting the list by the price
    sortedDict = {key: value for key, value in sorted(dict.items(), key=lambda item: item[1][2])}
    with open('MySolution/DamagedInventory.txt','w') as damageFile:

        # Now iterating the dict by keys
        for key in sortedDict.keys():
            # Checking if damage
            if sortedDict[key][-1] == 'damaged':
                string = f'{key}'
                for txt in sortedDict[key][:4]:
                    string += f',{txt}'
                damageFile.write(string + '\n')
# Did check that Damage Inv work if you add damage at the end.






# This will run my main program which I test and run my code
def run(files):
    # Testing Variable To test out different outputs and more examples
    test = {
    '1': ['Apple', 'laptop', '999', '7/3/2020'],
    '2': ['Apple', 'phone', '534', '2/1/2021'],
    '3': ['Dell', 'laptop', '799', '7/2/2020'],
    '4': ['Dell', 'tower', '345', '5/27/2020'],
    '5': ['Lenovo', 'laptop', '239', '9/1/2020', 'damaged'],
    '6': ['Lenovo', 'tower', '599', '10/1/2020'],
    '7': ['Samsung', 'phone', '1200', '12/1/2023'],
    '8': ['Apple', 'tablet', '399', '6/15/2022'],
    '9': ['Dell', 'desktop', '899', '3/8/2021'],
    '10': ['HP', 'laptop', '649', '8/20/2021'],
    '11': ['Lenovo', 'desktop', '449', '11/5/2020'],
    '12': ['Samsung', 'tablet', '299', '4/30/2022'],
    '13': ['Apple', 'watch', '199', '9/12/2022'],
    '14': ['Google', 'phone', '799', '1/7/2022'],
    '15': ['Microsoft', 'laptop', '1199', '10/25/2021'],
    '16': ['Sony', 'headphones', '149', '5/3/2023'],
    '17': ['LG', 'TV', '799', '12/19/2021'],
    '18': ['Amazon', 'Echo', '99', '2/14/2022'],
    '19': ['Fitbit', 'fitness tracker', '129', '7/9/2023'],
    '20': ['GoPro', 'action camera', '299', '11/21/2022'],
    '21': ['Apple', 'laptop', '1099', '6/3/2021'],
    '22': ['Apple', 'laptop', '1299', '9/2/2020'],
    '23': ['Apple', 'tablet', '499', '3/14/2023'],
    '24': ['Dell', 'laptop', '899', '5/5/2022'],
    '25': ['Dell', 'laptop', '999', '8/17/2021'],
    '26': ['Dell', 'desktop', '699', '10/30/2022'],
    '27': ['Lenovo', 'desktop', '499', '4/1/2023'],
    '28': ['Lenovo', 'desktop', '599', '6/6/2022'],
    '29': ['Lenovo', 'laptop', '349', '2/8/2023'],
    '30': ['Lenovo', 'laptop', '449', '12/12/2022']
}




    # Pulling the dictionary from fullInventory since it would be under the fullInv format and sort.
    fullInv = fullInventory(fileToDict(files))

    # Would not be needing a return value so just calling the function with the dictionary from FullInv.
    laptopInventory(fullInv)
    pastServiceDateInv(fullInv)
    damagedInv(fullInv)
    # Change this with test to test with other stuff
    return test

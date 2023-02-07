
#dictionary global varible
dict = {
    
    "key1": "val1",
    
    "key2": "val2", 
    
    "key3": "val3"

}

#main menu function
def MainMenu(dict):
    while True:
        
        #welcome menu 
        print("\n\nWelcome To MyPyDictionary\n")
        print("Here is your current dictionary:\n")
        print("-----------------------------------------------------")
        print(dict)
        print("-----------------------------------------------------")
        
        
        #options list - options selected by number
        print("\n1.     |Make a New Entry|      ")
        print("\n2.     |Add A New Item Into the Dictionary|    ")
        print("\n3.     |Create a New Dictionary|")

        #selection options
        
        sel = input("\nPlease input a number from the choice list: ")
        
        if sel == ("1"):
                NewEntry(dict)
        elif sel == ("2"):
                RemoveKey(dict)
        elif sel == ("3"):
                CreateNewDict(dict)
                
        else:
                print ("end")
                break

#enter a new key and value into the dict
def NewEntry(dict):
    print (dict)
    newkey = input("\nEnter a New Key: ")
    newval = input("\nEnter a Value: ")
    dict[newkey] = newval
    print ("\nPrinting New Entry: \n")
    print (dict)
    print ("\n")
    MainMenu(dict)

#Remove a dict item

def RemoveKey(dict):
    key = input("\nPlease Enter the key entry u would like to remove: ")
    if key in dict:
        del dict[key]
        print ("\nKey Sucessfully Deleted.")
        MainMenu(dict)
    else:
        print("key does not exist.")

#Create new dictionary function

def CreateNewDict(dict):
    dict = {}  #This dict local variable replaces the global variable which is stored in each function. 
               #Hence when this is used it pushes this empty dict into the main menu function and overrides the global varible.
    MainMenu(dict)


MainMenu(dict)

#I may add something in future that copies your final dictionary into a txt file or parses a txt file for dictionary entries.
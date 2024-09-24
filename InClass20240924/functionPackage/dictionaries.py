# dictionaries.py

def demo():
    """
    Demostrate basic dictionary stuff
    """
    
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)

    #Iterate over the dictionary by key 
    for key in myDictionary.keys():
        print(key)

    #iterate by value /key
    for item in myDictionary.items():
        print(item)

    #iterate by value 
    for value in myDictionary.values():
        print(value)

    #add a key/value pair to the dictionary 
    myDictionary["Michigan State"] = "Spartans"

    print(len(myDictionary))

    #Cause an exception 
    try:
        print(myDictionary["Ohio State"])
    except:
        print ("Ohio state is an invalid key")

    #remove xavier by key and print the entire dictionary 
    myDictionary.pop("Xavier")
    print(myDictionary)

    #Create another dictionary called newTeams. 
    #add several key/value pairs 
    #combine that myDictionary and print the results 
    newTeams = {"Dayton":"Flyers", 
                "Notre Dame":"Fighting Irish",
                "Ohio":"Bobcats"}
    myDictionary.update(newTeams)
    print(myDictionary)


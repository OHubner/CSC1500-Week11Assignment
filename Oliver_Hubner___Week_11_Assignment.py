

def main():
    #1
    #Create the initial list
    badData = [1121, "Jackie Grainger", 22.22,
             1122, "Jignesh Thrakkar", 25.25,
             1127, "Dion Green", 28.75, False,
             24.32, 1132, "Jacob Gerber",
             "Sarah Sanderson", 23.45, 1137, True,
             "Brandon Heck", 1138, 25.84, True,
             1152, "David Toma", 22.65,
             23.75, 1157, "Charles King", False,
             "Jackie Grainger", 1121, 22.22, False,
             22.65, 1152, "David Toma"]

    #Remove the bool values that serve an unknown purpose
    for i in badData:
        if i == False:
            badData.remove(False)
        elif i == True:
            badData.remove(True)

    
    overallCounter = 1
    goodData = []
    #2 and 3
    #loop to go through the initial list, assign values into dictionaries, and then store those dictionaries into a new list
    while overallCounter <= len(badData):
        #Base dictionary for storing data into
        tempDict = {"EmployeeID": 0, "Employee Name" : "", "Hourly Wage" : 0.0}
        #Loop to store each employees info into the dictionary
        for i in range(0, 3):
            index = overallCounter - 1
            item = badData[index]
            if type(item) == int:
                tempDict["EmployeeID"] = item
            elif type(item) == str:
                tempDict["Employee Name"] = item
            elif type(item) == float:
                tempDict["Hourly Wage"] = item
            overallCounter += 1
        #Stores the dictionary into the new list if that employee's data doesnt already exist in the list
        if tempDict not in goodData:
            goodData.append(tempDict)

    #7.1
    print("Data sorted and stored in dictionaries")
    for i in goodData:
        print(i)
    
    #4
    print("\nAdding total hourly rate with the benefit amount added")
    for i in goodData:
        i["total_hourly_rate"] = round(i["Hourly Wage"] * 1.3, 2)
    for i in goodData:
        print(i)

    #5
    underpaid_salaries = []
    for i in goodData:
        if (i["total_hourly_rate"] > 28.15 and i["total_hourly_rate"] < 30.65):
            underpaid_salaries.append(i)
    #7.2
    print("\nList of people with underpaid salaries")
    for i in underpaid_salaries:
        print(i)

    #6
    company_raises = []
    for i in goodData:
        tempDict2 = {"Employee Name" : i["Employee Name"], "Raise Amount" : 0.0}
        currentHourly = i["Hourly Wage"]
        raiseperc = 0.0
        if currentHourly > 22 and currentHourly < 24:
            raiseperc = .05
        elif currentHourly >= 24 and currentHourly < 26:
            raiseperc = .04
        elif currentHourly >= 26 and currentHourly < 28:
            raiseperc = .03
        else:
            raiseperc = .02
        tempDict2["Raise Amount"] = round(currentHourly * raiseperc, 2)
        company_raises.append(tempDict2)
    #7.3
    print("\nRaise Amounts")
    for i in company_raises:
        print(i)



main()

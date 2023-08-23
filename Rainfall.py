'''
Data and data1 are two strings with rainfall records of a few cities for months from
January to December. The records of towns are separated by \n. The name of each
town is followed by :.

Data and towns can be seen in "Your Test Cases:".

Task:
FUNCTION: mean(town, strng) should return the average of rainfall for the city town
and the strng data or data1 (In R and Julia this function is called avg).
FUNCTION: variance(town, strng) should return the variance of rainfall for the city
town and the strng data or data1.

Examples:
mean("London", data), 51.19(9999999999996) 
variance("London", data), 57.42(833333333374)

Notes:
**If functions mean or variance have as parameter town a city
   which has no records return -1 or -1.0 (depending on the language)
**Don't truncate or round: the tests will pass if abs(your_result - test_result) <= 1e-2
   or abs((your_result - test_result) / test_result) <= 1e-6 depending on the language.
**Shell tests only variance
**A ref: http://www.mathsisfun.com/data/standard-deviation.html
**Data and data1 (can be named d0 and d1 depending on the language; see "Sample Tests:")
   are adapted from: http://www.worldclimate.com

'''

#Nuaiman's Solution
def mean(town, string):
    TownData = string.split("\n")
    New = ""
    DataArr = []
    Flag = False
    towns = ["Rome", "London", "Paris", "NY", "Vancouver", "Sydney", "Bangkok", "Tokyo",
         "Beijing", "Lima", "Montevideo", "Caracas", "Madrid", "Berlin"]
    for c in range(len(TownData)):
        if town in towns and town in TownData[c]:
            Flag = True
            New = TownData[c].strip(town)
            DataArr = New.split(",")
            for n in range(len(DataArr)):
                DataArr[n] = float(DataArr[n].strip(DataArr[n][:4]))
    if DataArr is None or Flag == False:
        return -1
    total = 0      
    for r in range(len(DataArr)):
        total += DataArr[r]
    if len(DataArr) == 0 or total == 0:
        return None
    else:
        avg = total/ len(DataArr)  
        return avg
            
def variance(town, string):
    TownData = string.split("\n")
    New = ""
    DataArr = []
    Flag = False
    towns = ["Rome", "London", "Paris", "NY", "Vancouver", "Sydney", "Bangkok", "Tokyo",
         "Beijing", "Lima", "Montevideo", "Caracas", "Madrid", "Berlin"]
    for c in range(len(TownData)):
        if town in towns and town in TownData[c]:
            Flag = True
            New = TownData[c].strip(town+":")       
            DataArr = New.split(",")
            for n in range(len(DataArr)):
                DataArr[n] = float(DataArr[n].strip(DataArr[n][:4]))
    if DataArr is None or Flag == False:
        return -1
    total = 0      
    for r in range(len(DataArr)):
        total += DataArr[r]
    if len(DataArr) == 0:
        return None
    else:
        avg = total/ len(DataArr)
    total2 = 0
    for r in range(len(DataArr)):
        total2 += DataArr[r]*DataArr[r]
    if total2 is not None or avg is not None or len(DataArr) is not None:
        var = (total2/len(DataArr)) - (avg*avg)    
        return var
    else:
        return None

#Solution 2
def get_towndata(town, strng):
    for line in strng.split('\n'):
        s_town, s_data = line.split(':')
        if s_town == town:
            return [s.split(' ') for s in s_data.split(',')]
    return None

def mean(town, strng):
    data = get_towndata(town, strng)
    if data is not None:
        return sum([float(x) for m,x in data]) / len(data)
    else:
        return -1.
    
def variance(town, strng):
    data = get_towndata(town, strng)
    if data is not None:
        mean = sum([float(x) for m,x in data]) / len(data)
        return sum([(float(x)-mean)**2 for m,x in data]) / len(data)
    else:
        return -1.



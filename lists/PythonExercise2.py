#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
minValue = min(ages)
maxValue = max(ages)
print(ages)
print(minValue)
print(maxValue)

#Add the min age and the max age again to the list
ages.append(minValue)
ages.append(maxValue)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
def medianAge(ages: list[int]):
    ages.sort()
    listLength = len(ages)
    middle = listLength // 2 #floor division(rounds to nearest whole number)

    if listLength % 2 == 0:
        #one middle number
        median = ages[middle]
    else:
         #two middle numbers
        median = (ages[middle-1] + ages[middle]) / 2
    return median

print(medianAge(ages=ages))

#Find the average age (sum of all items divided by their number )
def averageAge(ages: list[int]):
    ages.sort()
    ageSum = 0
    listLength = len(ages)

    for num in ages:
        ageSum += num

    average = ageSum / listLength
    print(average)

averageAge(ages=ages)

#Find the range of the ages (max minus min)
def rangeOfAges(ages: list[int]):
    ages.sort()
    minValue = min(ages)
    maxValue = max(ages)

    rangeAge = maxValue - minValue
    print(rangeAge)

rangeOfAges(ages=ages)

#Compare the value of (min - average) and (max - average), use abs() method
def compareValue(ages: list[int]):
    ages.sort()
    minValue = min(ages)
    maxValue = max(ages)

    average = sum(ages)/len(ages)

    minNumber = abs(minValue-average)
    maxNumber = abs(maxValue-average)

    if minNumber > maxNumber:
        print(minNumber)
    else:
        print(maxNumber)

compareValue(ages=ages)

#Find the middle country(ies) in the countries list
from countries import *

def findMiddleCountries(countries: list[int]):
    listLength = len(countries)
    middle = listLength // 2

    if listLength % 2 == 0:
        print(countries[middle])
    else:
       print(countries[middle-1], countries[middle])

findMiddleCountries(countries=countries)

#Divide the countries list into two equal lists if it is even if not one more country for the first half.

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

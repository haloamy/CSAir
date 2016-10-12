# coding=utf-8
'''
Created by Amy Chen on 9/25/2016
'''
import CSAirParsing
from _collections import defaultdict
from itertools import chain
import webbrowser
import CSAirMetro
import CSAirRoute
import json



#A list of all possible main category, user can choose by enter the
#corresponding number.

def listOfMainCategory():
    print("1. Get a list of all the cities that CSAir flies to.")
    print("2. Get specific information about a specific city in the CSAir route network.")
    print("3. Statistical information about CSAir's route network.")
    print("4. Get the route map url")
    print("5. Information about a route.")
    
#A list of options that the user can get access and explore
# the corresponding information
def specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary):
    print("Would you like to add a new city? ")
    yesOrNo = raw_input()
    if (yesOrNo == "yes"):
        addCity(metroCodeDictionary, matchNameToCityCode, routeCodeDictionary)
        refSpecificCity(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(yesOrNo == "no"):
        print("Would you like to remove a city?")
        removeYesOrNo = raw_input()
        if(removeYesOrNo == "yes"):
            removeCIty(metroCodeDictionary, routeCodeDictionary)
            refSpecificCity(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
        else:
            refSpecificCity(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
#A list of options for user to explore different statistics information
# about a specific flight.
def statsInfo(metroCodeDictionary, routeCodeDictionary):
    print("would you like to add a route?")
    userInput = raw_input()
    if(userInput == "yes"):
        addRoute(metroCodeDictionary,routeCodeDictionary)
        refStatsInfo(metroCodeDictionary, routeCodeDictionary)
    elif(userInput == "no"):
        print("Would you like to remove a route?")
        userInputR = raw_input()
        if(userInputR == "yes"):
            removeRoute(metroCodeDictionary, routeCodeDictionary)
            refStatsInfo(metroCodeDictionary,routeCodeDictionary)
        else:
            refStatsInfo(metroCodeDictionary,routeCodeDictionary)
            
#This function will compare all the distance of single flight and return
#the longest distance.
def singleLongestDistance(routeCodeDictionary):
    longestDistance = 0
    currentPorts = None
    currentArrival = None
    for ports in routeCodeDictionary:
        for arrival in routeCodeDictionary[ports].flightRoute:
            currentAirFlight = routeCodeDictionary[ports].flightRoute[arrival]
            if (longestDistance < currentAirFlight):
                longestDistance = currentAirFlight
                currentPorts = ports
                currentArrival = arrival
    getPrint = ("From " + currentPorts + " to " + currentArrival + " is the longest distance single flight." + "\n")
    return getPrint

#This function will compare all the distance of single flight and return
#the shortest distance flight.
def singleShotestDistance(routeCodeDictionary):
    shortestDistance = 99999
    currentPorts = None
    currentArrival = None
    for ports in routeCodeDictionary:
        for arrival in routeCodeDictionary[ports].flightRoute:
            currentAirFlight = routeCodeDictionary[ports].flightRoute[arrival]
            if(shortestDistance > currentAirFlight):
                shortestDistance = currentAirFlight
                currentPorts = ports
                currentArrival = arrival
    getPrint = ("From " + currentPorts + " to " +currentArrival + " is the shortest distance single flight." + "\n")
    return getPrint

#This function will calculate the average distance of a single flight
def singleAverageDistance(routeCodeDictionary):
    totalDistance = 0
    temp = 0
    for ports in routeCodeDictionary:
        for arrival in routeCodeDictionary[ports].flightRoute:
            totalDistance = totalDistance + routeCodeDictionary[ports].flightRoute[arrival]
            temp = temp+1
    averageDistance =  float(totalDistance / temp)
    getPrint = ("The average distance for a single flight is  " + str(averageDistance) + "\n")
    return getPrint

#This function will compare all the cities' population and return the city that 
#has the biggest population.
def  largestPopulation( metroDictionary):
    biggestCity = 0
    currentCity = None
    for cityName in metroDictionary:
        currentPopulation = metroDictionary[cityName].population
        if(biggestCity < currentPopulation):
            biggestCity = currentPopulation
            currentCity = metroDictionary[cityName].name
    getPrint =  ("The biggest city by population by CSAir is " + currentCity)
    return getPrint

#This function will compare all the cities' population and return the city that
#has the smallest population.
def smallestPopulation(metroDictionary):
    smallestCity = 9999999
    currentCity = None
    for cityName in metroDictionary:
        currentPopulation = metroDictionary[cityName].population
        if(smallestCity > currentPopulation):
            smallestCity = currentPopulation
            currentCity = metroDictionary[cityName].name
    getPrint = ("The smallest city by population by CSAir is " + currentCity)
    return getPrint

#This function will calculate all the population of all city and return
#the average size of population.
def averageSizePopulation(metroDictionary):
    totalPopulation = 0
    temp = 0
    for nameCity in metroDictionary:
        totalPopulation = totalPopulation + metroDictionary[nameCity].population
        temp = temp + 1
    averagePopulation = float(totalPopulation / temp)
    getPrint = ("The average population throughout all cities is" + str(averagePopulation) + "\n")
    return getPrint

#This function will provide a list of all continent that served by CSAir and 
#which cities are in them
def allContinentAndCityList(metroCodeDictionary, routeCodeDictionary):
    allContinents = {}
    for cityName in metroCodeDictionary:
        if (metroCodeDictionary[cityName].continent in allContinents):
            allContinents[metroCodeDictionary[cityName].continent].append(cityName)
        else:
            allContinents[metroCodeDictionary[cityName].continent] = [cityName]
    print("There are the list of the continent with its included cities: ")
    for continent in allContinents:
        temp = continent + ": "
        for cityName in allContinents[continent]:
            temp += cityName + ","
        print(  temp[:-1])
    return statsInfo(metroCodeDictionary,routeCodeDictionary)

#This function will check all the connection and return the
#city that has the most
def hubCity(metroCodeDictionary, routeCodeDictionary):
    tempS = defaultdict(int)
    tempE = defaultdict(int)
    tempT = defaultdict(lambda: (0, 0))
    print("The city that has the most connection is/are : ")
    for ports in routeCodeDictionary:
        for arrival in routeCodeDictionary[ports].flightRoute:
            if ports in routeCodeDictionary:
                tempS[ports] += 1
            if arrival in routeCodeDictionary:
                tempE[arrival] += 1
    for tempS, tempE in chain(tempS.items(), tempE.items()):
        tempT[tempS] = tempT[tempS][0] + tempE, tempT[tempS][1]  
    for key, val in tempT.iteritems():
        if(val == max(tempT.values())):
            print( key)
    return refStatsInfo(routeCodeDictionary, metroCodeDictionary)

#This function will show the user all the possible cities' name
#when they press 1 at the main category
def allCityList(metroCodeDictionary, routeCodeDictionary, matchNameToCityCode):
    for name in metroCodeDictionary:
        print(metroCodeDictionary[name].name)
    specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
#This function will query out the code for specific city name when
#user click a.                
def cityQueryCodeInfo(cityName, metroCodeDictionary):
    getPrint = metroCodeDictionary[cityName].code
    return getPrint
                                   
#This function will query out the county the city belongs to
def cityQueryCountryInfo(cityName, metroCodeDictionary):
    getPrint = metroCodeDictionary[cityName].country
    return getPrint

#This function will query out the continent of the city belongs to
def cityQueryContinentInfo(cityName, metroCodeDictionary):
    getPrint = metroCodeDictionary[cityName].continent
    return getPrint

#This function will query out the timezone of the city
def cityQueryTimezoneInfo(cityName, metroCodeDictionary):
    getPrint = metroCodeDictionary[cityName].timezone
    return getPrint

#This function will query out the coordinates of the city which is the longitude and latitude
def cityQueryCoordinatesInfo(cityName, metroCodeDictionary):
    getPrint = metroCodeDictionary[cityName].coordinates
    return getPrint

# This function will query out the population of the city
def cityQueryPopulationInfo(cityName, metroCodeDictionary):
    getPrint = metroCodeDictionary[cityName].population
    return getPrint

#This function will query out the region of the city
def cityQueryRegionInfo(cityName, metroCodeDictionary):
    getPrint = metroCodeDictionary[cityName].region
    return getPrint

#This function will convert the name of a city into code representation
def convertNameToCode(cityName, metroCodeDictionary):
    return metroCodeDictionary[cityName].code

#This function will remove a city from the city list
def removeCIty(metroCodeDictionary, routeCodeDictionary):
    print("What city you would like to remove?")
    userInput = raw_input()
    print("The city you have entered has been successfully removed!")
    convertToPorts = convertNameToCode(userInput, metroCodeDictionary)
    for city in metroCodeDictionary.keys():
        if (city == userInput):
            del metroCodeDictionary[city]
    for ports in routeCodeDictionary.keys():
        for arrival in routeCodeDictionary[ports].flightRoute.keys():
            if(ports == convertToPorts):
                del routeCodeDictionary[ports]
            if(arrival == convertToPorts):
                del routeCodeDictionary[ports]
    
#This function will remove a route from the route dictionary
def removeRoute(metroCodeDictionary,routeCodeDictionary):
    print("Departure you want to delete is: ")
    input_depart = raw_input()
    print("Destination you want to delete is: ")
    input_dest = raw_input()
    for ports in routeCodeDictionary.keys():
        for arrival in routeCodeDictionary[ports].flightRoute.keys():
            if((ports == input_depart) and (arrival == input_dest)):
                del routeCodeDictionary[ports]
#Print all of the route helper function
def routeList(routeCodeDictionary):
    for ports in routeCodeDictionary:
        for arrival in routeCodeDictionary[ports].flightRoute:
            print(ports + " - " + arrival)
#PartIV get the url string for the route map
def getRouteMapString(routeCodeDictionary):
    firstPart = "http://www.gcmap.com/mapui?P="
    entireUrl =  firstPart
    for ports in routeCodeDictionary:
        for arrival in routeCodeDictionary[ports].flightRoute:
            entireUrl += ports + "-" + arrival + ",+"
    print(entireUrl[:-2])
    webbrowser.open(entireUrl)
    print("\n")
    main()
#Function for when the user want to add a city 
def addCity(metroCodeDictionary,matchNameToCityCode,routeCodeDictionary):
    metroCodeDictionary = metroCodeDictionary
    airName = raw_input("Please enter the city name:")
    airCode = raw_input("Please enter the city code:")
    airCountry = raw_input("Please enter the country of city:")
    airContinent = raw_input("Please enter the continent of the city:")
    airTimezone = input("please enter the timezone:")
    airCoordinates = input("please enter the coordinate:")
    airPopulation = input("please enter the population of the city:")
    airRegion = input("please enter the region code of the city:")
    
    metroCodeDictionary[airName] = CSAirMetro.CSAirMetro(airCode, airName, airCountry, airContinent, airTimezone, airCoordinates, airPopulation, airRegion)
    print("Now you have successfully added the city.")
 
#Function for when user want to add a route
def addRoute(metroCodeDictionary, routeCodeDictionary):
    airPortStartingPoint = raw_input("Please enter the starting point.")
    airPortEndingPoint = raw_input("Please enter the ending point.")
    airDistance = raw_input("Please enter the distance between the two points.")
    routeCodeDictionary[airPortStartingPoint] = CSAirRoute.CSAirRoute()
    routeCodeDictionary[airPortStartingPoint].flightRoute[airPortEndingPoint]= airDistance
    print("The route you have entered has been successfully added")
  
#Function in order to edit existing cities.
def editCity(cityName, matchNameToCityCode, routeCodeDictionary, metroCodeDictionary):
    print("Which part you want to change?")
    userInput = raw_input()
    if(userInput == "country"):
        print("Switch it to what country?")
        userInputCountry = raw_input()
        metroCodeDictionary[cityName].country = userInputCountry
        specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(userInput == "continent"):
        print("Switch it to what continent?")
        userInputContinent = raw_input()
        metroCodeDictionary[cityName].continent = userInputContinent
        specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(userInput == "timezone"):
        print("Switch it to what timezone?")
        userInputTimezone = raw_input()
        metroCodeDictionary[cityName].timezone = userInputTimezone
        specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(userInput == "coordinate"):
        print("Switch it to what coordinate?")
        userInputCoordinate = raw_input()
        metroCodeDictionary[cityName].coordinates = userInputCoordinate
        specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(userInput == "population"):
        print("New population number is? ")
        userInputPopulation = raw_input()
        metroCodeDictionary[cityName].population = userInputPopulation
        specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(userInput == "region"):
        print ("Switch it to what region?")
        userInputRegion = raw_input()
        metroCodeDictionary[cityName].region = userInputRegion
        specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    else:
        print("Invalid input, please try again!")
        editCity(cityName, matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
#refracto function for specific cityinfo
def refSpecificCity(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary):
    print("Please enter the city name you desire to know more!")  
    cityName = raw_input()
    if (cityName not in matchNameToCityCode):
        print("Invalid city name.\n")
        return main()
    else:
        print("\n")
    print("Choose one of the letter below please.")
    print("a. Its code.")
    print("b. Its name.")
    print("c. Its country.")
    print("d. Its continent.")
    print("e. Its timezone.")
    print("f. Its longitude and latitude.")
    print("g. Its population.")
    print("h. Its region.")
    print("i. A list of all of the other cities that are accessible via a single non-stop flight from that source city.")
    print("j. I want to go go back to the main category")
    print("k. Edit the city")
    print("s. Save the change to a new json file!")
    #possible choice for user to click
    letterChose = raw_input()
    if (letterChose == "a"):
        print cityQueryCodeInfo(cityName, metroCodeDictionary)
        print("\n")  
        return specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(letterChose == "b"):
        print(cityName + "\n")
        print("\n")
        return specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(letterChose == "c"):
        print cityQueryCountryInfo(cityName, metroCodeDictionary)
        print("\n")
        return specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
        return specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(letterChose == "d"):
        print cityQueryContinentInfo(cityName, metroCodeDictionary)
        print("\n")
        return specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(letterChose == "e"):
        print cityQueryTimezoneInfo(cityName, metroCodeDictionary)
        print("\n")
        return specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(letterChose == "f"):
        print cityQueryCoordinatesInfo(cityName, metroCodeDictionary)
        print("\n")
        return specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(letterChose == "g"):
        print cityQueryPopulationInfo(cityName, metroCodeDictionary)
        print("\n")
        return specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(letterChose == "h"):
        print cityQueryRegionInfo(cityName, metroCodeDictionary)
        print("\n")
        return specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(letterChose == "i"):
        cityList = []
        convertInput = convertNameToCode(cityName, metroCodeDictionary)
        for arrival in routeCodeDictionary[convertInput].flightRoute:
            cityList.append(str(arrival))
        print("The accessible non stop flight from " + str(cityName) + " is/are: ")
        print(cityList)
        return specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    elif(letterChose == "j"):
        return main()
    elif(letterChose == "k"):
        editCity(cityName, matchNameToCityCode,routeCodeDictionary, metroCodeDictionary)
    elif(letterChose == "s"):
        getNewJson(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)
    else:
        print("Your input is invalid!")
        return main()
        print("/n")
#refractor function for statsinfo
def refStatsInfo(metroCodeDictionary, routeCodeDictionary):
    print("Choose one of the letter below please.")
    print("a. The longest single flight in the network.")
    print("b. The shortest single flight in the network.")
    print("c. The average distance of all the flights in the network.")
    print("d. The biggest city (by population) served by CSAir.")
    print("e. The smallest city (by population) served by CSAir.")
    print("f. The average size (by population) of all the cities served by CSAir.")
    print("g. I list of the continents served by CSAir and which cities are in them.")
    print("h. Identifying CSAir's hub cities – the cities that have the most direct connections.")
    print("i. I want to go back to the main category.")
    print("j. Check the route list.")
    letterCode = raw_input()
    if(letterCode == "a"):
        print singleLongestDistance(routeCodeDictionary)
        return statsInfo(metroCodeDictionary,routeCodeDictionary)
    elif(letterCode == "b"):
        print singleShotestDistance(routeCodeDictionary)
        return statsInfo(metroCodeDictionary,routeCodeDictionary)
    elif(letterCode == "c"):
        print singleAverageDistance(routeCodeDictionary)
        return statsInfo(metroCodeDictionary,routeCodeDictionary)
    elif(letterCode == "d"):
        print largestPopulation(metroCodeDictionary)
        return statsInfo(metroCodeDictionary,routeCodeDictionary)
    elif(letterCode == "e"):
        print smallestPopulation(metroCodeDictionary)
        return statsInfo(metroCodeDictionary,routeCodeDictionary)
    elif(letterCode == "f"):
        print averageSizePopulation(metroCodeDictionary)
        return statsInfo(metroCodeDictionary,routeCodeDictionary)
    elif(letterCode == "g"):
        return allContinentAndCityList(metroCodeDictionary,routeCodeDictionary)
    elif(letterCode == "h"):
        return hubCity(metroCodeDictionary,routeCodeDictionary)
    elif(letterCode == "i"):
        return main()
    elif(letterCode == "j"):
        routeList(routeCodeDictionary)
        return main()
    else:
        print("Invalid input, please choose something else")
        return statsInfo(metroCodeDictionary,routeCodeDictionary)

#Save the changed information into new json file
def getNewJson(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary):
    newDict = {}
    newDict['data sources'] =  [
            "http://www.gcmap.com/" ,
            "http://www.theodora.com/country_digraphs.html" ,
            "http://www.citypopulation.de/world/Agglomerations.html" ,
            "http://www.mongabay.com/cities_urban_01.htm" ,
            "http://en.wikipedia.org/wiki/Urban_agglomeration" ,
            "http://www.worldtimezone.com/standard.html"
        ] 
    newDict['metros'] = []
    newDict['routes'] = []
    for metro in metroCodeDictionary:
        temp = {}
        temp['code'] = metroCodeDictionary[metro].code
        temp['name'] = metroCodeDictionary[metro].name
        temp['country'] = metroCodeDictionary[metro].country
        temp['continent'] = metroCodeDictionary[metro].continent
        temp['timezone'] = metroCodeDictionary[metro].timezone
        temp['coordinates'] = metroCodeDictionary[metro].coordinates
        temp['population'] = metroCodeDictionary[metro].population
        temp['region'] = metroCodeDictionary[metro].region
        newDict['metros'].append(temp)  
    for route1 in routeCodeDictionary:
        for route2 in routeCodeDictionary[route1].flightRoute:
            temp = {}
            temp['ports'] = []
            temp['ports'].append(route1)
            temp['ports'].append(route2)
            temp['distance'] = routeCodeDictionary[route1].flightRoute[route2]
            newDict['routes'].append(temp)
    with open('NewAir.json', 'w') as outfile:
        json.dump(newDict, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
        outfile.close()
    print("You now can open the NewAir.json to check the new json file.")
    specificCityInfo(matchNameToCityCode, routeCodeDictionary, metroCodeDictionary)


#Function that will provide all the information about a route, such as total distance o the route
#the cost to fly the route and the time it will take to travel the route.
def routeInfo(routeCodeDictionary):
    print("Please enter the route.")
    inputRoute = raw_input()
    newList = inputRoute.split("-")
    total = 0.0
    firstCostPerK = 0.35
    for i in range(len(newList) - 1):
        cost = routeCodeDictionary[newList[i]].flightRoute[newList[i+1]] * firstCostPerK
        total = total + routeCodeDictionary[newList[i]].flightRoute[newList[i+1]]      
        firstCostPerK -= 0.05
    print ("The total distance is " +str(total) + " and the total cost is " + str(cost) +"$.")
    timeforfirstandlast = 1.06667
    if(total < 400.0):
        temp = total / 2.0
        time = 4 + (temp / 375.0) * 2.0
        print("The total time is " + str(time) + "hours")
    else:
        temp = total - 400.0
        time = 4 + timeforfirstandlast + (temp / 750.0)
        print("The total time is " + str(time))
     
        
def main():
        listOfMainCategory()
        userInput = raw_input()
        parsing_File = CSAirParsing.CSAirParsing()
        if (userInput == "1"):
            allCityList(parsing_File.metroCodeDictionary, parsing_File.routeCodeDictionary, parsing_File.matchNameToCityCode)
        elif(userInput == "2"):
            specificCityInfo(parsing_File.metroCodeDictionary, parsing_File.routeCodeDictionary, parsing_File.metroCodeDictionary)
        elif (userInput == "3"):
            statsInfo(parsing_File.metroCodeDictionary, parsing_File.routeCodeDictionary)
        elif(userInput == "4"):
            getRouteMapString(parsing_File.routeCodeDictionary)
        elif(userInput == "5"):
            routeInfo(parsing_File.routeCodeDictionary)

if __name__ == '__main__':
    main()

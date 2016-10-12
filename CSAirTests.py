# coding=utf-8
'''
Created by Amy Chen on 9/25/2016
'''
import unittest
import CSAirMainUI
import CSAirMetro
import CSAirRoute
#Test cases for CSAir project

class CSAirTest(unittest.TestCase):
        
    #This will test the function about cityQueryCodeInfo function and see if it come out 
    #with the proper outcome
    def test_cityQueryCodeInfo(self):
        metroCodeDictionary = {}
        metroCodeDictionary["Beijing"] = CSAirMetro.CSAirMetro("PEK" , "Beijing", "CH", "Asia", 8, {"N" : 40, "E" : 117}, 13600000, 4)
        cityName = "Beijing"
        self.assertEqual(CSAirMainUI.cityQueryCodeInfo(cityName, metroCodeDictionary) ,  "PEK")
    
    #This will test the function about cityQueryCountryIndo function and see if it come out 
    #with the proper outcome
    def test_cityQueryCountryInfo(self):
        metroCodeDictionary = {}
        metroCodeDictionary["Beijing"] = CSAirMetro.CSAirMetro("PEK" , "Beijing", "CH", "Asia", 8, {"N" : 40, "E" : 117}, 13600000, 4)
        cityName = "Beijing"
        self.assertEqual(CSAirMainUI.cityQueryCountryInfo(cityName, metroCodeDictionary), "CH")
    
    #This will test the function about cityQueryContinentInfo function and see if it come out 
    #with the proper outcome
    def test_cityQueryContinentInfo(self):
        metroCodeDictionary = {}
        metroCodeDictionary["Beijing"] = CSAirMetro.CSAirMetro("PEK" , "Beijing", "CH", "Asia", 8, {"N" : 40, "E" : 117}, 13600000, 4)
        cityName = "Beijing"
        self.assertEqual(CSAirMainUI.cityQueryContinentInfo(cityName, metroCodeDictionary), "Asia")
    
    #This will test the function about cityQueryTimezoneInfo function and see if it come out 
    #with the proper outcome
    def test_cityQueryTimezoneInfo(self):
        metroCodeDictionary = {}
        metroCodeDictionary["Beijing"] = CSAirMetro.CSAirMetro("PEK" , "Beijing", "CH", "Asia", 8, {"N" : 40, "E" : 117}, 13600000, 4)
        cityName = "Beijing"
        self.assertEqual(CSAirMainUI.cityQueryTimezoneInfo(cityName, metroCodeDictionary), 8)
    
    #This will test the function about cityQueryCoordinatesInfo function and see if it come out 
    #with the proper outcome
    def test_cityQueryCoordinatesInfo(self):
        metroCodeDictionary = {}
        metroCodeDictionary["Beijing"] = CSAirMetro.CSAirMetro("PEK" , "Beijing", "CH", "Asia", 8, {"N" : 40, "E" : 117}, 13600000, 4)
        cityName = "Beijing"
        self.assertEqual(CSAirMainUI.cityQueryCoordinatesInfo(cityName, metroCodeDictionary), {'E': 117, 'N': 40})
        
    #This will test the function about cityQueryPopulationInfo function and see if it come out 
    #with the proper outcome  
    def test_cityQueryPopulationInfo(self):
        metroCodeDictionary = {}
        metroCodeDictionary["Beijing"] = CSAirMetro.CSAirMetro("PEK" , "Beijing", "CH", "Asia", 8, {"N" : 40, "E" : 117}, 13600000, 4)
        cityName = "Beijing"
        self.assertEqual(CSAirMainUI.cityQueryPopulationInfo(cityName, metroCodeDictionary), 13600000 )
        
    #This will test the function about cityQueryPopulationInfo function and see if it come out 
    #with the proper outcome  
    def test_cityQueryRegionInfo(self):
        metroCodeDictionary = {}
        metroCodeDictionary["Beijing"] = CSAirMetro.CSAirMetro("PEK" , "Beijing", "CH", "Asia", 8, {"N" : 40, "E" : 117}, 13600000, 4)
        cityName = "Beijing"
        self.assertEqual(CSAirMainUI.cityQueryRegionInfo(cityName, metroCodeDictionary), 4 )
    
    #This will test the function about convertNameToCode function and see if it come out 
    #with the proper outcome 
    def test_convertNameToCode(self):
        metroCodeDictionary = {}
        metroCodeDictionary["Beijing"] = CSAirMetro.CSAirMetro("PEK" , "Beijing", "CH", "Asia", 8, {"N" : 40, "E" : 117}, 13600000, 4)
        cityName = "Beijing"
        self.assertEqual(CSAirMainUI.convertNameToCode(cityName, metroCodeDictionary), "PEK" )
        
        

    #This will test and see if singleLongestDistance will return the longest distance flight
    def test_singleLongestDistance(self):
        routeCodeDictionary = {}
        routeCodeDictionary["SCL"] = CSAirRoute.CSAirRoute()
        routeCodeDictionary["LIM"] = CSAirRoute.CSAirRoute()
        routeCodeDictionary["MEX"] = CSAirRoute.CSAirRoute()
        routeCodeDictionary["SCL"].flightRoute["LIM"] = 2453
        routeCodeDictionary["LIM"].flightRoute["MEX"] = 4231
        routeCodeDictionary["LIM"].flightRoute["BOG"] = 1879
        routeCodeDictionary["MEX"].flightRoute["LAX"] = 2499
        routeCodeDictionary["MEX"].flightRoute["CHI"] = 2714
        routeCodeDictionary["MEX"].flightRoute["MIA"] = 2053
        routeCodeDictionary["MEX"].flightRoute["BOG"] = 3158
        self.assertEqual(CSAirMainUI.singleLongestDistance(routeCodeDictionary), "From LIM to MEX is the longest distance single flight.\n")
        
    #This will test and see if singleShotestDistance will return the shorest distance flight
    def test_singleShotestDistance(self):
        routeCodeDictionary = {}
        routeCodeDictionary["SCL"] = CSAirRoute.CSAirRoute()
        routeCodeDictionary["LIM"] = CSAirRoute.CSAirRoute()
        routeCodeDictionary["MEX"] = CSAirRoute.CSAirRoute()
        routeCodeDictionary["SCL"].flightRoute["LIM"] = 2453
        routeCodeDictionary["LIM"].flightRoute["MEX"] = 4231
        routeCodeDictionary["LIM"].flightRoute["BOG"] = 1879
        routeCodeDictionary["MEX"].flightRoute["LAX"] = 2499
        routeCodeDictionary["MEX"].flightRoute["CHI"] = 2714
        routeCodeDictionary["MEX"].flightRoute["MIA"] = 2053
        routeCodeDictionary["MEX"].flightRoute["BOG"] = 3158
        self.assertEqual(CSAirMainUI.singleShotestDistance(routeCodeDictionary), "From LIM to BOG is the shortest distance single flight.\n")
    
    #This will test and see if it will return the average distance of all flight
    def test_singleAverageDistance(self):
        routeCodeDictionary = {}
        routeCodeDictionary["SCL"] = CSAirRoute.CSAirRoute()
        routeCodeDictionary["LIM"] = CSAirRoute.CSAirRoute()
        routeCodeDictionary["MEX"] = CSAirRoute.CSAirRoute()
        routeCodeDictionary["SCL"].flightRoute["LIM"] = 2453
        routeCodeDictionary["LIM"].flightRoute["MEX"] = 4231
        routeCodeDictionary["LIM"].flightRoute["BOG"] = 1879
        routeCodeDictionary["MEX"].flightRoute["LAX"] = 2499
        routeCodeDictionary["MEX"].flightRoute["CHI"] = 2714
        routeCodeDictionary["MEX"].flightRoute["MIA"] = 2053
        routeCodeDictionary["MEX"].flightRoute["BOG"] = 3158
        self.assertEqual(CSAirMainUI.singleAverageDistance(routeCodeDictionary), "The average distance for a single flight is  2712.0\n")
    
    #This will test and see if largestPopulation will return the largest population among 
    #all cities.
    def test_largestPopulation(self):
        metroCodeDictionary = {}
        metroCodeDictionary["Beijing"] = CSAirMetro.CSAirMetro("PEK" , "Beijing", "CH", "Asia", 8, {"N" : 40, "E" : 117}, 13600000, 4)
        metroCodeDictionary["Paris"] = CSAirMetro.CSAirMetro("PAR", "Paris", "FR", "Europe", 0, {"N" : 49, "E" : 2}, 10400000, 3)
        self.assertEqual(CSAirMainUI.largestPopulation(metroCodeDictionary), "The biggest city by population by CSAir is Beijing")
    
    #This will test and see if averageSizePopulation will return the smallest population among
    #all cities
    def test_averageSizePopulation(self):
        metroCodeDictionary = {}
        metroCodeDictionary["Beijing"] = CSAirMetro.CSAirMetro("PEK" , "Beijing", "CH", "Asia", 8, {"N" : 40, "E" : 117}, 13600000, 4)
        metroCodeDictionary["Paris"] = CSAirMetro.CSAirMetro("PAR", "Paris", "FR", "Europe", 0, {"N" : 49, "E" : 2}, 10400000, 3)
        self.assertEqual(CSAirMainUI.averageSizePopulation(metroCodeDictionary), "The average population throughout all cities is12000000.0\n")
    #This will test and see the routeinfo function works properly.
    
    
    
    
    
    
    
    
    
    
    
    

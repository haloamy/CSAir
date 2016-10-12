# coding=utf-8
'''
Created by Amy Chen on 9/25/2016
'''
import json
import CSAirMetro
import CSAirRoute



class CSAirParsing:
    def __init__(self):
        
        with open('CSAirJSON.json') as json_data:
            data = json.load(json_data)
            #create dictionaries to store different key values
            self.metroCodeDictionary = {}
            self.matchNameToCityCode = {}
            self.routeCodeDictionary = {}
                  
            #Parsing all the data using the key value name
            for metro_info in data['metros']:
                airCode = metro_info['code']
                airName = metro_info['name']
                airCountry = metro_info['country']
                airContinent = metro_info['continent']
                airTimezone = metro_info['timezone']
                airCoordinates = metro_info['coordinates']
                airPopulation = metro_info['population']
                airRegion = metro_info['region']
                self.metroCodeDictionary[airName] = CSAirMetro.CSAirMetro(airCode, airName, airCountry, airContinent, airTimezone, airCoordinates, airPopulation, airRegion)
                self.matchNameToCityCode[airName] = airCode
                self.routeCodeDictionary[airCode] = CSAirRoute.CSAirRoute()
                
            for route_info in data['routes']:
                airPortStartingPoint = route_info['ports'][0]
                airPortEndingPoint = route_info['ports'][1]
                airDistance = route_info['distance']
                self.routeCodeDictionary[airPortStartingPoint].flightRoute[airPortEndingPoint] = airDistance
                
            CSAirParsing.addChampaign(self, self.metroCodeDictionary, self.metroCodeDictionary, self.routeCodeDictionary)
        
    def addChampaign(self,matchNameToCityCode,metroCodeDictionary, routeCodeDictionary):
        with open('cmi_hub.json') as jsonFile:
            jsonData = json.load(jsonFile)
            for metro_info in jsonData['metros']:
                airCode = metro_info['code']
                airName = metro_info['name']
                airCountry = metro_info['country']
                airContinent = metro_info['continent']
                airTimezone = metro_info['timezone']
                airCoordinates = metro_info['coordinates']
                airPopulation = metro_info['population']
                airRegion = metro_info['region']
                self.metroCodeDictionary[airName] = CSAirMetro.CSAirMetro(airCode, airName, airCountry, airContinent, airTimezone, airCoordinates, airPopulation, airRegion)
                self.matchNameToCityCode[airName] = airCode
                self.routeCodeDictionary[airCode] = CSAirRoute.CSAirRoute()
                
            for route_info in jsonData['routes']:
                airPortStartingPoint = route_info['ports'][0]
                airPortEndingPoint = route_info['ports'][1]
                airDistance = route_info['distance']
                self.routeCodeDictionary[airPortStartingPoint].flightRoute[airPortEndingPoint] = airDistance


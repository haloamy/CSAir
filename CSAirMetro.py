# coding=utf-8
'''
Created by Amy Chen on 9/25/2016
'''

class CSAirMetro():
    #This function will initiate all the information under the city specific
    #inorder to save the data from the json file
    def __init__(self, code, name, country, continent, timezone, coordinates, population, region):
        self.code = code
        self.name = name
        self.country = country
        self.continent = continent
        self.timezone = timezone
        self.coordinates = coordinates
        self.population = population
        self.region = region
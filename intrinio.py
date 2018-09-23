import requests

class intrinio :
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def getDataPoint(self, identifier, item):
        if type(identifier) == tuple:
            valuesDict = {}
            for co in identifier:
                if type(item) == tuple:
                    valuesDict[co] = {}
                    for i in item:
                        got =  requests.get('https://api.intrinio.com/data_point?identifier=' + co + '&item=' + i,
                            auth=(self.username, self.password))
                        valuesDict[co][i] = got.json()['value']
                else:
                    got = requests.get('https://api.intrinio.com/data_point?identifier=' + co + '&item=' + item,
                        auth=(self.username, self.password))
                    valuesDict[co] = got.json()['value']
            return valuesDict
                


        if type(item) == tuple:
            valuesDict = {}
            for i in item:
                got =  requests.get('https://api.intrinio.com/data_point?identifier=' + identifier + '&item=' + i,
                                    auth=(self.username, self.password))
                valuesDict[i] = got.json()['value']
            return valuesDict
            
        got = requests.get('https://api.intrinio.com/data_point?identifier=' + identifier + '&item=' + item,
                           auth=(self.username, self.password))
        return got.json()['value']
    
    
    def getIndustryInfo(self, identifier, item):
        sicCode = self.getDataPoint(identifier, 'sic')
        if type(item) == tuple:
            valuesDict = {}
            for i in item:
                got =  requests.get('https://api.intrinio.com/data_point?identifier=$SIC.' + str(sicCode) + '&item=' + i,
                                    auth=(self.username, self.password))
                valuesDict[i] = got.json()['value']
            return valuesDict
            
        got = requests.get('https://api.intrinio.com/data_point?identifier=$SIC.' + str(sicCode) + '&item=' + item,
                           auth=(self.username, self.password))
        return got.json()['value']
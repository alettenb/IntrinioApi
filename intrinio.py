import requests

class intrinio :
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def getDataPoint(self, identifier, item):
        if type(identifier) == tuple:
            valuesDict = {}
            
            if type(item) == tuple:
                for company in identifier:
                    valuesDict[company] = {}
                got =  requests.get('https://api.intrinio.com/data_point?identifier=' + ','.join(str(i) for i in identifier) + '&item=' + ','.join(str(i) for i in item),
                    auth=(self.username, self.password))
                for obj in got.json()['data']:
                    co = str(obj['identifier'])
                    item = obj['item']
                    valuesDict[co][item] = obj['value']
            else:
                got = requests.get('https://api.intrinio.com/data_point?identifier=' + ','.join(str(i) for i in identifier) + '&item=' + item,
                    auth=(self.username, self.password))
                for obj in got.json()['data']:
                    co = str(obj['identifier'])
                    valuesDict[co] = obj['value']
            return valuesDict
                


        if type(item) == tuple:
            valuesDict = {}
            got =  requests.get('https://api.intrinio.com/data_point?identifier=' + identifier + '&item=' + ','.join(str(i) for i in item),
                                auth=(self.username, self.password))
            for obj in got.json()['data']:
                item = obj['item']
                valuesDict[item] = obj['value']
            return valuesDict
            
        got = requests.get('https://api.intrinio.com/data_point?identifier=' + identifier + '&item=' + item,
                           auth=(self.username, self.password))
        return got.json()['value']
    

    def getIndustryInfo(self, identifier, item):
        sicCode = self.getDataPoint(identifier, 'sic')
        if type(item) == tuple:
            valuesDict = {}
            got =  requests.get('https://api.intrinio.com/data_point?identifier=$SIC.' + str(sicCode) + '&item=' + ','.join(str(i) for i in item),
                                auth=(self.username, self.password))
            for obj in got.json()['data']:
                item = obj['item']
                valuesDict[item] = obj['value']
            return valuesDict
            
        got = requests.get('https://api.intrinio.com/data_point?identifier=$SIC.' + str(sicCode) + '&item=' + item,
                           auth=(self.username, self.password))
        return got.json()['value']
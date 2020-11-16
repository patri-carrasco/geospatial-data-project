from functools import reduce
import operator

def getFromDict(dict_n,maps):
    return reduce(operator.getitem,maps,dict_n)

def mapData(data):
  return map(lambda x: {
    'name': x['name'],
    'longitude': x['offices'][0]['longitude'],
    'latitude': x['offices'][0]['latitude']
  }, data)
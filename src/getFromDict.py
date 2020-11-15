from functools import reduce
import operator

def getFromDict(dict_n,maps):
    return reduce(operator.getitem,maps,dict_n)
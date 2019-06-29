import pandas as pd
import numpy as np


#############################################################################################	
def preprocessing(data):

	"""
		Most important ******
	"""
	data = handleNanValues(data)

	return data

#############################################################################################	
def handleNanValues(data):
	"""
		Handle NaN values ....
	"""

	for i in data.columns:
		if data[i].dtype == "object":
			if data[i].isnull().sum() >= 1:
				data.fillna(method='ffill',inplace=True)
				data.fillna(method='bfill',inplace=True)

		else:
			if data[i].isnull().sum() >= 1:
				data.fillna(data[i].mean(),inplace=True)

	return data


	pass

#############################################################################################	
def meanEncodings(data,colName,target):
    """
        This function encodes the value in colName corresponding to the target value ......
    """
    
    # count all the target values correspondig to unique values in columns ....
    uniqueValues = data[colName].unique()
    arr = []
    
    for i in uniqueValues:
        
        dataI = data[data[colName]==i] # total columns corresspoding to i'th value ...
        totalIValues = dataI.shape[0] # total number of rows corressponding to the i'th value ...
        total1TargetValues = len(dataI[dataI[target] == 1]) # total number of target values that are 1 ...
        valToPut = total1TargetValues / totalIValues
        
        for i in range(totalIValues):
            # append this value the number of times this value has occured in the dataframe ....
            arr.append(valToPut)
            pass
        
        pass
    return arr
    pass
	
#############################################################################################	

def func(u,l,k):
    
    return (l*l*k)/(u*np.exp(u))

def isCategorical(data):
    """
        Tells whether a particular column is categorical or not .....
    """

    categorical = []
    totalLength = data.shape[0]

    for i in data.columns:
        uniqueVals = len(data[i].unique())
        if(func(uniqueVals,totalLength,3) > 1):
            categorical.append(i)
    print("Possible categorical columns : ",len(categorical),categorical)
    print("\n\n")
    return categorical
    pass

#############################################################################################	
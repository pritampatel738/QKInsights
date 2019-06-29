import pandas as pd
import numpy as np

#######################################################################################

def logScale(data,column):
	"""
		Improves the scaling of your data.
	"""
	data[column] = np.log(data[column]+1)
	return data[column]
	
########################################################################################

def normalizeDataColumn(data,column):
	
	"""
		Min-Max + Mean Normalization of column of the data.
	"""
	data[column] = (data[column] - data[column].mean()) / (data[column].max() - data[column].min + 1)
	return data[column]
	pass
	
########################################################################################

	
def groupByTwoColumns(data,col1,col2):
    """
        Corresponding to every training how many rows are there ....
		Col1 is any column and col2 is the target column ....
    """
    unique = data[col1].unique()
    
    for i in unique:
        
        data1 = data[data[col1] == i]
        data2 = data1[data1[col2]==1]
        totalNo = len(data2)
        print("The {} {} has {} {}.".format(col1,i,totalNo,col2))
        
        pass
    
    #groupByTwoColumns(train,'no_of_trainings','is_promoted')
    pass
	
######################################################################################
	
def countByTwoColumns(data,col1,col2,width=10,height=7):
    """
        Corresponding to every training how many rows are there ....
        col2 is the target variable ....
    """
    unique = data[col1].unique()
    arr = []
    for i in range(len(data[col1])):
        arr.append(0)
        
    for i in unique:
        
        data1 = data[data[col1] == i]
        data2 = data1[data1[col2]==1]
        totalNo = len(data2)
        print("The {} {} has {} {}.".format(col1,i,totalNo,col2))
        arr[i] = totalNo
        
        pass
    arr1 = [] # contains count values ....
    for i in arr:
        if i != 0 :
            arr1.append(i)
        pass

    x_ticks = [] # contains x values ...
    for i in range(len(arr)):
        if arr[i] != 0:
            x_ticks.append(i)
        pass
    
    fig = plt.figure(figsize=(width,height))
    plt.xticks(x_ticks,rotation=90)
    
    print(len(x_ticks))
    print(len(arr1))
    a = plt.plot(x_ticks,arr1)
    #a = plt.hist(arr,bins=len(arr))
    return arr
	#countIsPromotedByAge = countByTwoColumns(train,'age','is_promoted')
	#countIsPromotedByNoOfTrainings = countByTwoColumns(train,'no_of_trainings','is_promoted')

    pass
	
#############################################################################################

def labelEncodeAll(data):


    """
    Sorts the unique value in each columns and then encodes to get consistent results.
    """

    for i in data.columns:
        print(i)
        if data[i].dtype == "object":
            uniqueValues = data[i].sort_values().unique()
            replaceValues = np.arange(1,len(uniqueValues)+1,1)
            data[i].replace(uniqueValues,replaceValues,inplace=True)
    return data
#############################################################################################

def covariance(column1,column2):
    try:
        column1 = np.array(column1)
        column2 = np.array(column2)

        if(column1.shape[0] < 1 or column2.shape[0] < 1):
            print("Please provide correct input.")
            return


        if(column1.shape[0] != column2.shape[0] and column1.shape[1] != column2.shape[1]):
            print("Please provide correct input with same shape")
            return

        #print("The means are {} {}".format(column1.mean(),column2.mean()))
        sumVal = 0
        col1 = (column1 - column1.mean())
        col2 = (column2-column2.mean())
        #print(col1,col2)
        #print(col1*col2)
        sumVal = sum(col1*col2)
        #sumVal = sum((column1 - column1.mean()) * (column2-column2.mean()))
        
        #print("The sumval in covariance is : {}".format(sumVal))
        sumVal = sumVal / (column1.shape[0]) 
        
        #print("The covariance value is : {}.".format(sumVal))
        return sumVal
    
        pass
    except:
        print("Something went wrong !")
        pass

def correlation(column1,column2):
    try:
        column1 = np.array(column1)
        column2 = np.array(column2)

        if(column1.shape[0] < 1 or column2.shape[0] < 1):
            print("Please provide correct input.")
            return

        stdColumn1 = column1.std()
        stdColumn2 = column2.std()
        #print(stdColumn1)
        #print(stdColumn2)
        
        covarianceValue = covariance(column1,column2)
        correlationValue = (covarianceValue) / (stdColumn1*stdColumn2)
        
        #print("The correlation value is : {}".format(correlationValue))
        return correlationValue
        pass
    
    except:
        print("Something went wrong !")
        pass


#############################################################################################

def FPSkewness(data,column):
    # fischer-pearson skewness .....

    # find out the skewness of the data .....
    try:
        #print("inside")
        column1 = np.array(data[column])
        n = column1.shape[0]
        if column1.shape[0] < 1:
            print("Please provide valid input.")
            return -8888
        #print("outside")
        retVal =  sum(pow(column1 - column1.mean(),3)) / (column1.shape[0])
        #print(retVal)
        stdDev = column1.std()
        #print(retVal,stdDev)
        #print(retVal,stdDev)
        retVal = retVal / pow(stdDev,3)
        #retVal = (retVal * n) / ((n-1)*(n-2))
        #print(retVal,stdDev)
        #print("The skewness value is : {}.".format(retVal))
        return retVal
        
    except:
        print("Something went wrong !")
        return -8888
        
    
def GOBSkewness(data,column):

    try:
        if data[column].shape[0] < 1:
            print("Please provide valid input.")
            return -8888

        dVal = data[column].describe()
        #print(dVal)
        q1 = dVal['25%']
        q2 = dVal['50%']
        q3 = dVal['75%']

        retVal = (q1 + q3 - 2*q2) / (q3 - q1)

        return retVal
    except:
        print("Something went wrong !")

#############################################################################################

def kurtosis(data,column):

    column1 = np.array(data[column])
    n = column1.shape[0]
    if column1.shape[0] < 1:
        print("Please provide valid input.")
        return -8888
    stdDev = column1.std()
    retVal =  sum(pow(column1 - column1.mean(),4)) / (column1.shape[0])
    retVal = retVal / pow(stdDev,4)
    retVal -= 3 # to make normal distribution have 0 kurtosis ...
    return retVal

#############################################################################################








































































































































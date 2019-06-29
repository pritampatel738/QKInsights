import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import preprocessing
import usefulFunctions

##################################################################################################	

def dataImbalanceCategorical(data,target):

	dataDict = {}
	uniqueVals = data[target].unique()
	
	for i in uniqueVals:
		cnt = len(data[data[target] == i])
		#print(cnt)
		dataDict[i] = cnt
	print(end="\n\n")
	print("The distribution of classess are : ",dataDict)
	#print(dataDict)
	
	# set min and max to the very first sample point in target ...
	minVal = len(data[data[target] == data[target][0]])
	minString = data[target][0]
	
	maxVal = len(data[data[target] == data[target][0]])
	maxString = data[target][0]
	
	for i in dataDict.keys():
		# check for maximum value ...
		if(dataDict[i] > maxVal):
			maxVal = dataDict[i]
			maxString = i
		if(dataDict[i] <= minVal):
			minVal = dataDict[i]
			minString = i
		# endfor
		
	print("{} class has most occurence {}.".format(maxString,maxVal))
	print("{} class has minimum occurence {}.".format(minString,minVal))
	
	fig = plt.figure(figsize=(5,5))
	plt.title("Class distribution")
	plt.xticks(np.arange(len(uniqueVals)),uniqueVals,rotation=90)
	plt.bar(np.arange(len(dataDict.values())),data[target].value_counts())
	plt.show()

	if(maxVal/(minVal+1) > 4):
		print("There is a possibility of class imbalance.")
	
	print("\n\n")
	
##################################################################################################	
	
def checkNormalDistribution(data,column):
	"""
		Check which of the columns are mean distributed.
	"""
	
	# stores the names of the column whose distribution is somewhat normalized ...
	meanDistributedData  = []
	mean = data[column].mean()
	std = data[column].std()

	if(abs(mean) <= 0.1 and 1.3 >=abs(std) >= 0.5):
		return 1
	else:
		return 0

	

##################################################################################################	

def nonCategoricalDistributionAnalysis(data,target,categorical):

	try:
		for i in data.columns:
			#print(i)
			if i not in categorical:
				print("\n\n")
				if data[i].dtype == "object":
					continue

				print("Here's the information about {} column.\n".format(i))
				# do calculations .....
				#print(i)
				mean = data[i].mean()
				std = data[i].std()
				median = data[i].median()

				if(checkNormalDistribution(data,i)):
					print("Column {} is normally distributed.\n\n".format(i))
					continue
				else:
					#print(i)
					# check for the potential outliers and quartile distribution values .....
					print("\n\n\nChecking for  outliers")
					dVal = data[i].describe()
					#interQuartileRange = description
					q1 = dVal['25%']
					median = dVal['50%']
					q3 = dVal['75%']
					interQuartileRange = q3 - q1


					## inner fences and checking for minor outlier .. ....
					lowerBoundInner = q1 - (1.5 * interQuartileRange)
					upperBoundInner = q3 + (1.5 * interQuartileRange)
					#print("The inner fence is bounded by ({},{}).\n".format(lowerBoundInner,upperBoundInner))
					#print("Checking for MINOR OUTLIERS\n")
					count = 0
					for j in data[i]:
						if j<lowerBoundInner or j>upperBoundInner:
							count += 1

						
					if count:
						print("There are {} possible sample points  that can be potential for MINOR OUTLIER.".format(count))
					else:
						print("No potential minor outliers.")


					# outer fences and checking for major outliers .....
					lowerBoundOuter = q1 - (3 * interQuartileRange)
					upperBoundOuter = q3 + (3 * interQuartileRange)
					#print("The outer fence is bounded by ({},{}).\n".format(lowerBoundOuter,upperBoundOuter))
					#print("Checking for MAJOR OUTLIERS")
					count1 = 0
					for j in data[i]:
						if j<lowerBoundOuter or j>upperBoundOuter:
							count1 += 1
					

					if count1:
						print("There are {} possible sample points  that can be potential MAJOR OUTLIER.".format(count1))
					else:
						print("No potential major outliers.")
					


					# if the data is not normally distributed .... (Just an Indicator comment) ...
					print("\n\n\nChecking for skewness")
					skewnessVal = usefulFunctions.FPSkewness(data,i)
					if skewnessVal == 0:
						print("{} is symmetrically distributed.".format(i))
					elif skewnessVal < 0:
						print("{} is distributed more towards right side with a skewness value of {}.".format(i,skewnessVal))
					else:
						print("{} is distributed more towards left side with a skewness value of {}.".format(i,skewnessVal))
					#print("\n\n")


					print("\n\n\nChecking for kurtosis.")
					kurtosis = usefulFunctions.kurtosis(data,i)
					if kurtosis > 0:
						print("{} is leptokurtic i.e, it has high peak value.".format(i))

					elif kurtosis == 0:
						print("{} is mesokurtic i.e, it is normally distributed.".format(i))
					else:
						print("{} is platykurtic i.e, it has less peak value.".format(i))

	except:
		print("Something went wrong !")

		


			


	

def CategoricalDistributionAnalysis(data,target,categorical):

	return 


	



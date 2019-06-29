#import imp



import sys
import histogram
import pandas as pd
import numpy as np
import preprocessing
import mildIntro
import usefulFunctions

def main():
	#print("Hello World")
	path = input("Please input the full path of your dataset : \n")
	target = input("Please input the target name : Put -1 if data doesn't contain target \n")
	
	#path = 'C:\Users\prita\Desktop\Pritam_2304\PythonFiles\HR_Analytics\train.csv'
	data = pd.read_csv(path)
	#print(data.head(),end="\n\n")


	mildIntro.mildIntro(data)
	
	# just handling NaN values .....
	data = preprocessing.preprocessing(data)


	histogram.dataImbalanceCategorical(data,target)
	#correlation.findCorrelation(data,target)
	
	categoricalColumns = preprocessing.isCategorical(data)
	#print(categoricalColumns)

	histogram.nonCategoricalDistributionAnalysis(data,target,categoricalColumns)


	# Combine categorical and nonCategorical columns to find who has most avg value for non-categorical column ....











































































	pass
	
	
if __name__ == "__main__":
	main()
import pandas as pd
import numpy as np

def mildIntro(data):

	print("Let's get some basic information about the data.\n")
	print("The shape of the data is  {}.\n\n".format(data.shape))

	#print("Let's see top 5 rows from the data.")
	#print(data.head())

	objectCount = 0 # stores the number of column having object type ...
	intCount = 0 # stores the number of column having int type ...
	floatCount = 0 # stores the number of column having int type ...
	objectCols = []
	intCols = []
	floatCols = []
	for i in data.columns:
		if data[i].dtype == "object":
			objectCols.append(i)
			objectCount += 1

		elif data[i].dtype == "int64":
			intCols.append(i)
			intCount += 1

		elif data[i].dtype == "float64":
			floatCols.append(i)
			floatCount += 1

	print("Dataset contains {} object columns and they are : {}\n".format(objectCount,objectCols))
	print("Dataset contains {} int64 columns and they are : {}\n".format(intCount,intCols))
	print("Dataset contains {} float64 columns and they are : {}\n\n".format(floatCount,floatCols))

	# null values have been removed .....
	for i in data.columns:
		if data[i].isnull().sum():
			print("Column {} contains {} NaN values.".format(i,data[i].isnull().sum()))

	print("\n\n")
import fileinput
import math 

def main():
	testFileProvided = True; # Change this to False to test on the same train data
	trainDataFile = 'traindata.txt'
	trainLabelFile = 'trainlabels.txt'
	testDataFile = 'testdata.txt'
	testLabelFile = 'testlabels.txt'


	######################################
	# train file processing
	######################################

	# Read training data and store them
	trainData = []
	with open( trainDataFile ) as f:
		trainData = f.read().splitlines()

	# Read training label and store them
	trainLabel = []
	with open( trainLabelFile ) as f:
		trainLabel = f.read().splitlines()

	if 	len(trainLabel) != len (trainData ):
		print ( 'The train label and train data should have the same length' )
		exit()

	######################################
	# test file processing
	######################################
	if testFileProvided:
		# Read test data and store them
		testData = []
		with open( testDataFile ) as f:
			testData = f.read().splitlines()

		# Read test label and store them
		testLabel = []
		with open( testLabelFile ) as f:
			testLabel = f.read().splitlines()

		if 	len(testLabel) != len (testData ):
			print ( 'The test label and test data should have the same length' )
			exit()
	else:
		testData = trainData
		testLabel = trainLabel

	######################################
	# Split keywords in each entry and store their count
	######################################
	yesTable = {}
	noTable = {}
	numOfYesWords = 0
	numOfNoWords = 0
	yesCount = 0
	noCount = 0
	numOfTerms = 0

	for i in range( len(trainLabel) ):
		words = trainData[i].split()
		if trainLabel[i] == '1' :
			yesCount +=1
			for word in words:
				numOfYesWords +=1
				if word in yesTable:
					yesTable[word] +=1
				else: 
					yesTable[word] = 1
					if word not in noTable:
						numOfTerms +=1
		elif  trainLabel[i] == '0' :
			noCount +=1
			for word in words:
				numOfNoWords +=1
				if word in noTable:
					noTable[word] +=1
				else: 
					noTable[word] = 1
					if word not in yesTable:
						numOfTerms +=1



	#####################################################
	# Start testing
	####################################################
	successCount = 0;
	failCount = 0;
	testCasesCount = 0
	for testString in testData:
		######################################
		# Split keywords and store them in test table
		######################################
		testcase = testString.split()
		testTable = {}
		for word in testcase:
			if word in testTable:
				testTable[word] +=1
			else: 
				testTable[word] = 1

		#print ( testTable )


		######################################
		# processing calculation
		######################################
		yesPercentage = float (yesCount) / (yesCount + noCount) 
		noPercentage = float (noCount) / (yesCount + noCount) 
		yesNumerator = float ( numOfYesWords + numOfTerms )
		noNumerator = float ( numOfNoWords + numOfTerms )

		for key in testTable:
			if key in yesTable:
				rep = yesTable[key]
			else:
				rep = 0 
			yesVal = (rep+1) / yesNumerator
			yesPercentage *= math.pow( yesVal, testTable[key] )

		for key in testTable:
			if key in noTable:
				rep = noTable[key]
			else:
				rep = 0 
			noVal = (rep+1) / noNumerator
			noPercentage *= math.pow( noVal, testTable[key] )


		if  yesPercentage > noPercentage:
			ans = '1'
		else:
			ans = '0'

		if ans == testLabel[testCasesCount]:
			successCount +=1
		else:
			failCount +=1

		testCasesCount+=1

	print ( "Success count: %d"% successCount )
	print ( "Fail count: %d"% failCount )
	percentage = successCount*100.0/testCasesCount
	print ( "Success Rate: %f" % percentage )

main()
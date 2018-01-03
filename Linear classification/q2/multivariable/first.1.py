#from bokeh.plotting import figure, output_file, show
from random import choice
from bokeh.io import output_file, show, vplot
from bokeh.plotting import figure, output_file, show
import os
import os.path
import math
import sys
import numpy
import random
output_file("error.html")
errorGraph = figure(plot_width=800, plot_height=800, title=None, toolbar_location='below', toolbar_sticky=False)

counter = 0;

def getw(Scailedmatrix,cls,w):
	array = []
	kappa = 1.0
	n = len(Scailedmatrix)
	for k in xrange(1000):
		i = 0
		initw = w
		sum1 = []
		array.append(error(Scailedmatrix, cls, w))
		count = 0
	
		for x in Scailedmatrix:
		
			w = w + kappa/n*(numpy.sum(numpy.multiply((cls[i]-x.dot(w.transpose())), x).transpose()))
			i += 1
		if ((w == initw[0]) - 0).all():
			break
	
	print(array)
	errorGraph.line ( xrange(len(array)) , array, line_width=2 )

	print(w)
	k+=1
	print(" %d times"% k)

	return w
	
def error (Scailedmatrix,cls,w):
	array =[] 
	L = len(Scailedmatrix)
	i = 0
	values =0
	for m in Scailedmatrix:
		
		values += ((cls[i] - float(m.dot(w.T)))**2)
		i += 1
		
	values = values/(2*L)
	return values
	
if os.path.exists('regdata.csv'):
	f = open('regdata.csv')
	md = f.readline()
	md = f.readlines()	
	data =(list(map(lambda l: list(map(float, l.split(',')[:2])), md)))
	cls= (list(map(lambda l: int(l.strip().split(',')[2]), md)))
	data = numpy.matrix(data)
	q = len(data)
	table = []
	for i in range(q):
		table.append ( 1 )
	
	Scailedmatrix = []
	Scailedmatrix.append(table)
	for row in data.T:
		row = row.tolist()
		newcol = []
		avgval = numpy.mean(row)
		maxval = numpy.max(row)
		minval = numpy.min(row)
		range = maxval - minval
		for val in row[0]:
			newcol.append( (val-avgval)/(range) ) # scailing 
		Scailedmatrix.append(newcol)
	
	Scailedmatrix = numpy.matrix(Scailedmatrix).T

	print(Scailedmatrix)

	
	#Compute the error at each iteration and save the error values in vector
	length = len(Scailedmatrix.transpose())
	w = [random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)]
	
	w = numpy.matrix(w)
	
	kappa = 1
	w = getw(Scailedmatrix,cls,w)

else:
	print("File doesn't exist")
	sys.exit(-1)



 

show(errorGraph)

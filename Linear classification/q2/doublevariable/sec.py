from bokeh.plotting import figure, output_file, show
from bokeh.io import output_file, show, vplot
import math


def evaluate(w, x):
		return w[0] + x*w[1]
		
def main():
		
	data =  [[1, 1]]
	data += [[2, 3]]
	data += [[4, 3]]
	data += [[3, 2]] 
	data += [[5, 5]] 
	
	
	
	output_file("test.html")
	lineGraph = figure(plot_width=800, plot_height=800,title=None, toolbar_location='below', toolbar_sticky=False)
	           

	
	# plotting data 
	xcord = [item[0] for item in data]
	ycord = [item[1] for item in data]
	lineGraph.square(xcord, ycord , size=10)
	
	w = [0,0]
	learningRate = 0.001
	
	errorArray = []
	for test in range(100):
		errorSum = 0
		for point in data:
			error =  point[1] - evaluate(w, point[0]) 
			w[0] = w[0] + ( error * learningRate ) 
			w[1] = w[1] +  (error * learningRate * point[0] )
			errorSum += ( error*error )
		errorArray.append(  (1.0/5) * errorSum  )
	
		print ( w )



	lineGraph.line ([ 0, 10 ], [ w[0] , evaluate(w, 10) ], line_width=2 )
	
	
	
	
	
	
	
	errorGraph = figure(plot_width=800, plot_height=800, title=None, toolbar_location='below', toolbar_sticky=False)
	
	errorGraph.line ( range(len(errorArray)) , errorArray, line_width=2 )

	graphs = vplot(lineGraph,errorGraph )
	show(graphs)

main()
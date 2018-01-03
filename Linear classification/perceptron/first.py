from bokeh.plotting import figure, output_file, show
from random import choice
import math

output_file("toolbar.html")

# create a new plot with the toolbar below
p = figure(plot_width=800, plot_height=800,
           title=None, toolbar_location='below',
           toolbar_sticky=False)

below =  [[1, 3, 0.2, -1]]
below += [[1, 1, 0.3, -1]]
below += [[1, 4, 0.5, -1]]
below += [[1, 2, 0.7, -1]] 
below += [[1, 0, 1  , -1]] 
below += [[1, 1, 1.2, -1]]
below += [[1, 1, 1.7, -1]]
 
above =  [[1, 6, 0.2, 1]] 
above += [[1, 7, 0.3, 1]]
above += [[1, 6, 0.7, 1]]
above += [[1, 3, 1.1, 1]]
above += [[1, 2, 1.5, 1]] 
above += [[1, 4, 1.7, 1]]
above += [[1, 2, 1.9, 1]]




# plotting data that should be below the line
xcord = [item[1] for item in below]
ycord = [item[2] for item in below]
p.square(xcord, ycord , size=5)

# plotting data that should be above the line
xcord = [item[1] for item in above]
ycord = [item[2] for item in above]
p.circle(xcord, ycord , size=5, color="#FF0000")

# plotting data that should be above the line
def sign(m):
	if m >= 0:
		return 1
	else:
		return -1

w = [0,0,0]
n = 0.1


total = below + above

for test in range(500):
	item = choice (total)  #randomly choose a point
	result = w[0]*item[0] + w[1]*item[1] + w[2]*item[2]
	expected = item[3]
	if expected != sign(result):
		w[0] = w[0] + expected * n * item[0]
		w[1] = w[1] + expected * n * item[1]
		w[2] = w[2] + expected * n * item[2] 


	
y =  -w[0]/w[2] 
slope = -w[1]  / w[2]
ang = math.atan ( slope )

print( w )


p.line ([0, y*(w[2]/w[1]) ], [y, 0], line_width=2 )


show(p)

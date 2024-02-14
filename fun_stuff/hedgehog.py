
import matplotlib.pyplot as plt
import math
import numpy as np
from math import sin, cos, pi

# This code was adapted from Matlab code posted on LinkedIn
# By MathWorks: https://www.linkedin.com/posts/the-mathworks_2_nationalhedgehogday-activity-7159218684543045632-Cia0?utm_source=share&utm_medium=member_desktop 

# feet - Using segments from three parabolas
x = np.arange(1.0, 8, .01)
y1 = [-1*(i-2)*(i-1) for i in x]
y2 = [ -1*(i-6)*(i-7) for i in x]
y3 = [ -1*(i-7)*(i-8) for i in x]
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

# face - using segments from circles shifted to create
# the outline of the face
theta1 = np.arange(1.5*pi, 1.785*math.pi, .01)
xf1 = [4*math.cos(t1)+6.5 for t1 in theta1]
yf1 = [4*math.sin(t1)+4.25 for t1 in theta1]
plt.plot(xf1, yf1,)
theta2 = np.arange(1.25*math.pi+.02,1.5*math.pi,.01)
xf2 = [3*math.cos(t2)+9.5 for t2 in theta2]
yf2 = [3*math.sin(t2)+5 for t2 in theta2]
plt.plot(xf2,yf2,)
theta3 = np.arange(.77*math.pi+.02, 1*math.pi, .01)
xf3 = [4*math.cos(t3)+10.5 for t3 in theta3]
yf3 = [4*math.sin(t3) + 0.25 for t3 in theta3]
plt.plot(xf3, yf3)

# nose - using a circle of radius 0.25 centered (9.25,2)
theta4 = np.arange(0, 2*math.pi, .01)
xn1 = [0.25*math.cos(t4)+9.75 for t4 in theta4]
yn1 = [0.25*math.sin(t4)+ 2 for t4 in theta4]
plt.plot(xn1, yn1)

# eye - This is a circle of radius 0.15 centered at (7.5, 2.1)
theta5 = np.arange(0, 2*math.pi, .01)
xe1 = [.15*math.cos(t5)+7.5 for t5 in theta5]
ye1 = [.15*math.sin(t5)+2.1 for t5 in theta5]
plt.plot(xe1,ye1,)

# back curve - the main curve of the back comes from an
# ellipse with major axis in horizontal direction with r = 4
# and minor axis in the vertical direction with r = 3
theta6 = np.arange(0.37*math.pi-.15, 1*math.pi , 0.15)
xPoints = [4*math.cos(t6)+5 for t6 in theta6]
yPoints = [3*math.sin(t6) for t6 in theta6]

# The hair emanates from the curve of the back and is a segment 
# from a circle of r=0.5
for idx in range(1,len(theta6)):
    thetai = theta6[idx]
    alpha = np.arange(-.5*math.pi + thetai, thetai , .01)
    xb = [.5*math.cos(a)+xPoints[idx] for a in alpha]
    yb = [.5*math.sin(a)+yPoints[idx] for a in alpha]
    plt.plot(xb, yb, )
plt.axis([0,10,0,5])

plt.show()
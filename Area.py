import numpy as np
import scipy as scp
import scipy.integrate as scint
import matplotlib.pyplot as plt

#defining variables...

a=8
b=5
c=2
m=1.5

xstart=float(raw_input('Left Bound:'))
xend=float(raw_input('Right Bound:'))
xstep=float(raw_input('Rectangle Width:'))

#generating a list of x values stored in rect:
#these x values are the left sides of each rectangle

def setup(xstart,xend,stepper):

    count=xstart
    rect=[]

    while count <= xend:
        rect.append(count)
        count=stepper+count

    #shifting these x values to the midpoint of every rectangle (midpoint reimann sum)...

    mid=[]
    for x in rect:
        tmp=x+(stepper/2)
        if tmp <= xend: mid.append(tmp)

    #creating a list of y values based on mid values for the linear function...

    count=0
    global ylin
    ylin=[]
    while count <= len(mid)-1:
        ytemp=(m*mid[count])+b
        ylin.append(ytemp)
        count=count+1

    #creating a list of y values based on mid values for the quadratic function...

    count=0
    global yquad
    yquad=[]
    while count <= len(mid)-1:
        ytemp=a*(mid[count]**2)+b*mid[count]+c
        yquad.append(ytemp)
        count=count+1

    #creating a list of y values based on mid values for the third function...

    count=0
    global y3
    y3=[]
    while count <= len(mid)-1:
        ytemp=(a*mid[count]+b)*(scp.e**(-1*c*mid[count]))
        y3.append(ytemp)
        count=count+1

#defining an area function that multiplies the all y values in

def midsum(function,stepper):
    blocklist=[]
    global atotal
    #print 'yeet',function
    for x in function:
        block=x*stepper
        blocklist.append(block)
    atotal=sum(blocklist)

def error(function):
    if function == 1: areaactual=scint.quad(lambda x: 1.5*x+5, xstart, xend)
    if function == 2: areaactual=scint.quad(lambda x: 8*(x**2)+5*x+2, xstart, xend)
    if function == 3: areaactual=scint.quad(lambda x: (8*x+5)*(scp.e**(-1*2*x)), xstart, xend)
    global err
    err=abs((atotal-areaactual[0])/areaactual[0])*100

def errorspread(f1,f2):
    countnew=1.0
    x=[]
    y=[]
    while countnew <= (xend-xstart):
        x.append(countnew)
        curve1=0
        curve2=0
        curve3=0
        if f1 == ylin: curve1=1
        if f1 == yquad: curve2=1
        if f1 == y3: curve3=1
        setup(xstart,xend,countnew)
        if curve1 == 1: f1=ylin
        if curve2 == 1: f1=yquad
        if curve3 == 1: f1=y3
        #print f1
        midsum(f1,countnew)
        #print atotal
        error(f2)
        y.append(err)
        countnew=countnew+1
    plt.scatter(x,y)
    if f2 == 1: plt.title('Percent Error vs. Step Size for Linear Equation')
    if f2 == 2: plt.title('Percent Error vs. Step Size for Quadratic Equation')
    if f2 == 3: plt.title('Percent Error vs. Step Size for Complicated Equation')
    plt.xlabel('Step Size')
    plt.ylabel('Percent Error')
    plt.show()


setup(xstart,xend,xstep)
print ''
midsum(ylin,xstep)
print 'Linear Equation Area:', atotal
error(1)
print 'Percent Error:', err
print ''
print ''
midsum(yquad,xstep)
print 'Quadratic Equation Area:', atotal
error(2)
print 'Percent Error:', err
print ''
print ''
midsum(y3,xstep)
print 'Complicated Equation Area:', atotal
error(3)
print 'Percent Error:', err
print ''

errorspread(ylin,1)
errorspread(yquad,2)
errorspread(y3,3)

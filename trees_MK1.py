#drawing trees

import math
import turtle

shape = [[0,0],[0,100],[0,0],[100,100],[0,0],[-100,100],[0,0]] #the branch shape
proportion = 0.7 #the ratio of the new branch relative to the previous branch
sparsity = 100 #how distance between branches

def part(TreeTurtle,proportion, shape, sparsity, startingCords): #building an individual part
    runningSparsity = sparsity
    for pointIndex in range(len(shape[1:])):
        point = shape[pointIndex+1]
        nextPoint = (startingCords[0] + point[0]*proportion, startingCords[1] + point[1]*proportion)
        prevPoint = (startingCords[0] + shape[pointIndex][0]*proportion, startingCords[1] + shape[pointIndex][1]*proportion)
        distance = calculate_distance(nextPoint[0], nextPoint[1], prevPoint[0], prevPoint[1])
        heading = findheading(nextPoint[0], nextPoint[1], prevPoint[0], prevPoint[1])
        TreeTurtle.setheading(heading)
        while runningSparsity < distance:
            TreeTurtle.forward(runningSparsity)
            distance -= runningSparsity
            runningSparsity = sparsity
            part(TreeTurtle.clone(),proportion*proportion, shape, sparsity, [turtle.xcor(), turtle.ycor()])
        TreeTurtle.forward(distance)
        runningSparsity -= distance
    TreeTurtle.ht()
    
def distance_to_next_point(shape, pointCounter):
    if pointCounter != len(shape):
        x0 = turtle.xcor() #finding the points of the current and next point
        y0 = turtle.ycor()
        x1 = shape[pointCounter + 1][0]
        y1 = shape[pointCounter + 1][1]
        return calculate_distance(x0, y0, x1, y1) #getting the distance from the next point
         

def calculate_distance(x0, y0, x1, y1): #calculates the distance to the next point
    distance = ((x0 - x1)**2 + (y0 - y1)**2)**0.5
    return distance

def findheading(x0, y0, x1, y1): #finding the degrees to point to a particular point
    xDistance = x0-x1 #getting distances
    yDistance = y0-y1
    if xDistance == 0: #ensuring no division by 0
        if yDistance > 0:
            angle = 90
        else:
            angle = 270
    else:
        angle = math.degrees(math.atan(yDistance/xDistance))#finding the number of degrees that the thing needs to turn
    if xDistance < 0: #flipping to get other half of circle
        angle = 180 + angle
    return angle

t1 = turtle.Turtle()


t1.speed(0)
part(t1, proportion, shape, sparsity, [0,0])
t1.ht()

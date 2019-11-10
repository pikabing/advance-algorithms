import matplotlib.pyplot as plt
import random
from bresenham import bresenham
import array

# Author - Pratik Gupta (referenced from others)
# q1 is upto class Node and q2 is the whole file

def createPGMFile(filename, width, height, points):
  buff = array.array('B')

  for _ in range(width*height):
    buff.append(255)

  for point in points:
    y,x = point
    row = height - x - 1
    col = y

    pgm_index = row * width + col  # index for 1D array
    buff[pgm_index] = 0

  with open(filename, 'wb') as pgmFile:
    # define PGM Header
    pgmHeader = 'P5' + '\n' + str(width) + '  ' + \
        str(height) + '  ' + str(255) + '\n'

    # write the header to the file
    pgmFile.write(pgmHeader.encode())

    # # write the data to the file
    buff.tofile(pgmFile)

    pgmFile.close()


def bresenhams(p1, p2):  
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    points = []
    m_new = 2 * (y2 - y1)  
    slope_error_new = m_new - (x2 - x1) 
  
    y=y1 
    for x in range(x1,x2+1):  
        points.append((x,y))
        # print("(",x ,",",y ,")")  
        slope_error_new =slope_error_new + m_new    
        if (slope_error_new >= 0):  
            y=y+1
            slope_error_new =slope_error_new - 2 * (x2 - x1)
    return points

k = int(input("Enter value of k: "))
y0 = int(input("Enter value of y0: "))
yk = int(input("Enter value of yk: "))
width = k * 40 + 100
height = yk + 100
i = 0
j = 5
segments = []
pointsToPlot = []
while(i < k*40):
    x1 = random.randint(i+1,i+40)
    x2 = random.randint(j+1,j+40)
    
    p1 = (x1,y0)
    p2 = (x2,yk)
    # print(p1,p2)
    segments.append([p1,p2])
    points = list(bresenham(x1,y0,x2,yk))
    for point in points:
        pointsToPlot.append(point)
    # points.append(p2)
    # print(points)

    x = [] 
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])

    plt.plot(x,y)
    i += 40
    j = i + 5


# plt.show()
# print("Segments are:",segments)


regions = []
for i in range(len(segments)-1):
    region = []
    region.append(segments[i][0])
    region.append(segments[i][1])
    region.append(segments[i+1][0])
    region.append(segments[i+1][1])
    regions.append(region)

print("Regions are:", regions)

#_____________________________________________________________________
#p1 = leftbottom, p2 = lefttop, p3 = rightbottom, p4 = righttop

class Node: 
    def __init__(self, p1,p2,p3,p4): 
        self.left = None
        self.right = None
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4 

    def centroid(self):
        xCentroid = (self.p1[0]+ self.p2[0]+ self.p3[0]+ self.p4[0])/4
        yCentroid = (self.p1[1]+ self.p2[1]+ self.p3[1]+ self.p4[1])/4
        return (xCentroid, yCentroid)

    
    def checkPointInRegion(self,query):
        prod1 = ((self.p2[0] - self.p1[0]) * (query[1] - self.p1[1])) - ((self.p2[1] - self.p1[1]) * (query[0] - self.p1[0]))
        prod2 = ((self.p4[0] - self.p3[0]) * (query[1] - self.p3[1])) - ((self.p4[1] - self.p3[1]) * (query[0] - self.p3[0]))
        if prod1 <= 0 and prod2 > 0:
            return 1
        elif prod1 > 0:
            return 2
        else:
            return 3



def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.centroid() < node.centroid(): 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.centroid()) 
        inorder(root.right)

def search(root,query):
    if root == None:
        return root
    v = root.checkPointInRegion(query)
    if v == 1:
        return root
    elif v == 2:
        return search(root.left,query)
    return search(root.right,query)
    

    

n = len(regions)
root = Node(regions[n//2][0],regions[n//2][1],regions[n//2][2],regions[n//2][3])
for i in range(len(regions)):
    if i != n//2:
        insert(root,Node(regions[i][0],regions[i][1],regions[i][2],regions[i][3]))



querypoint = (250,300)

reg = search(root, querypoint)

if querypoint[0] > regions[n-1][2][0] or querypoint[0] > regions[n-1][3][0]:
    print("QueryPoint lies to the Right of Segment:",regions[n-1][2],regions[n-1][3] )

elif querypoint[0] < regions[0][0][0] or querypoint[0] < regions[0][1][0]:
    print("QueryPoint lies to the Left of Segment:",regions[0][0],regions[0][1] )
else:
    print("The QueryPoint lies in the region:") 
    print(reg.p1,reg.p2,reg.p3,reg.p4)


plt.scatter(querypoint[0],querypoint[1])
plt.show()

createPGMFile('out1.pgm',width,height, pointsToPlot)
# print(segments)

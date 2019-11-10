from matplotlib import pyplot

def getCrossProd(p, q, r):
    value = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if value == 0:
        return 0
    elif value >0:
        return 1
    return 2


def getRightMost(points):
    Rightmost = 0
    for i in range(1,len(points)):
        if points[i][0] > points[Rightmost][0]:
            Rightmost = i
    return Rightmost


def convexHull(points):
    RightMostIndex = getRightMost(points)
    p = RightMostIndex

    hull = []

    while(1):
        hull.append(points[p])

        q = (p + 1) % len(points)

        for i in range(len(points)):
            if getCrossProd(points[p], points[i], points[q]) == 1:
                q = i
        
        p = q

        if p == RightMostIndex:
            break

    return hull
#__________________________________________________________
def calcDotProd(p,q):
    ans = p[0]*q[0] + p[1]*q[1]
    return ans

def findIntersection(polygon, line):
    intersectionPoints = []
    polygon.append(polygon[0])
    p0 = line[0]
    p1 = line[1]

    Dx = p1[0] - p0[0]
    Dy = p1[1] - p0[1]
    D = (Dx, Dy)

    n = len(polygon)

    pointsOfEntering = []
    pointsOfLeaving = []

    i = 0

    while(i < n-1):
        pe = polygon[i]
        dy = polygon[i+1][1] - polygon[i][1]
        dx = polygon[i+1][0] - polygon[i][0] 
        normal = (-dy, dx)
        
        nd = calcDotProd(normal, D)
        if nd:
            t = -1 * (calcDotProd(normal,(p0[0]-pe[0], p0[1]- pe[1])) / nd)
            if nd < 0 and t >= 0:
                xte = p0[0] + ((p1[0]- p0[0])* t)
                yte = p0[1] + ((p1[1]- p0[1])* t)
                pprime = (xte, yte)
                
                if ((pprime[0] > polygon[i][0] and  pprime[0] < polygon[i+1][0]) or (pprime[0] < polygon[i][0] and  pprime[0] > polygon[i+1][0])) and ((pprime[1] > polygon[i][1] and  pprime[1] < polygon[i+1][1]) or (pprime[1] < polygon[i][1] and  pprime[1] > polygon[i+1][1])):
                    print(pprime)
                    finalPoints.append(polygon[i])
                    finalPoints.append(pprime)
                    finalPoints.append(p1)
                    pointsOfEntering.append(t)
                    intersectionPoints.append(pprime)
                
            elif nd > 0 and t <= 1:
                xtl = p0[0] + ((p1[0]- p0[0])* t)
                ytl = p0[1] + ((p1[1]- p0[1])* t)
                qprime = (xtl, ytl)
                if ((qprime[0] > polygon[i][0] and  qprime[0] < polygon[i+1][0]) or (qprime[0] < polygon[i][0] and  qprime[0] > polygon[i+1][0])) and ((qprime[1] > polygon[i][1] and  qprime[1] < polygon[i+1][1]) or (qprime[1] < polygon[i][1] and  qprime[1] > polygon[i+1][1])):
                    print(qprime)
                    finalPoints.append(p0)
                    finalPoints.append(qprime)
                    finalPoints.append(polygon[i+1])
                    pointsOfLeaving.append(t)
                    intersectionPoints.append(qprime)
        i += 1
    
    return intersectionPoints


#_________________________________________________________________________________

polygon1 = [(0,6), (1,7), (3,7), (5,6), (5,4), (4,2), (2,2), (0,3)]
polygon2 = [(5,2), (3,4), (3,6), (5,7), (7,7), (8,6), (8,4), (7,2)]


polygon = polygon2
polygon.append(polygon2[0])

allIntersectionPoints = []
finalPoints = []

for i in range(len(polygon)-1):
    line = [polygon[i],polygon[i+1]]
    intersectionPoints = findIntersection(polygon1,line)

    for points in intersectionPoints:
        allIntersectionPoints.append(points)

print(finalPoints)


x = [] 
y = []
for i in range(len(polygon1)):    
    x.append(polygon1[i][0])
    y.append(polygon1[i][1])
pyplot.fill(x,y,edgecolor = 'r',fill = False)

x = [] 
y = []
for i in range(len(polygon2)):    
    x.append(polygon2[i][0])
    y.append(polygon2[i][1])
pyplot.fill(x,y,edgecolor = 'b',fill = False)

x = [] 
y = []
for i in range(len(finalPoints)):    
    x.append(finalPoints[i][0])
    y.append(finalPoints[i][1])
pyplot.fill(x,y,edgecolor = 'g',fill = True)

pyplot.show()
        

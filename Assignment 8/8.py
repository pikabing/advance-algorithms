import matplotlib.pyplot as plt
import math, random, time

def make_circle(points):
    # Convert to float and randomize order
    shuffled = [(float(x), float(y)) for (x, y) in points]
    random.shuffle(shuffled)
    
    # Progressively add points to circle or recompute circle
    c = None
    for (i, p) in enumerate(shuffled):
        if c is None or not is_in_circle(c, p):
            c = _make_circle_one_point(shuffled[ : i + 1], p)
    return c


# One boundary point known
def _make_circle_one_point(points, p):
    c = (p[0], p[1], 0.0)
    for (i, q) in enumerate(points):
        if not is_in_circle(c, q):
            if c[2] == 0.0:
                c = make_diameter(p, q)
            else:
                c = _make_circle_two_points(points[ : i + 1], p, q)
    return c


# Two boundary points known
def _make_circle_two_points(points, p, q):
    circ = make_diameter(p, q)
    left  = None
    right = None
    px, py = p
    qx, qy = q
    
    # For each point not in the two-point circle
    for r in points:
        if is_in_circle(circ, r):
            continue
        
        # Form a circumcircle and classify it on left or right side
        cross = _cross_product(px, py, qx, qy, r[0], r[1])
        c = make_circumcircle(p, q, r)
        if c is None:
            continue
        elif cross > 0.0 and (left is None or _cross_product(px, py, qx, qy, c[0], c[1]) > _cross_product(px, py, qx, qy, left[0], left[1])):
            left = c
        elif cross < 0.0 and (right is None or _cross_product(px, py, qx, qy, c[0], c[1]) < _cross_product(px, py, qx, qy, right[0], right[1])):
            right = c
    
    # Select which circle to return
    if left is None and right is None:
        return circ
    elif left is None:
        return right
    elif right is None:
        return left
    else:
        return left if (left[2] <= right[2]) else right


def make_diameter(a, b):
    cx = (a[0] + b[0]) / 2.0
    cy = (a[1] + b[1]) / 2.0
    r0 = math.hypot(cx - a[0], cy - a[1])
    r1 = math.hypot(cx - b[0], cy - b[1])
    return (cx, cy, max(r0, r1))


def make_circumcircle(a, b, c):
    ox = (min(a[0], b[0], c[0]) + max(a[0], b[0], c[0])) / 2.0
    oy = (min(a[1], b[1], c[1]) + max(a[1], b[1], c[1])) / 2.0
    ax = a[0] - ox;  ay = a[1] - oy
    bx = b[0] - ox;  by = b[1] - oy
    cx = c[0] - ox;  cy = c[1] - oy
    d = (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) * 2.0
    if d == 0.0:
        return None
    x = ox + ((ax*ax + ay*ay) * (by - cy) + (bx*bx + by*by) * (cy - ay) + (cx*cx + cy*cy) * (ay - by)) / d
    y = oy + ((ax*ax + ay*ay) * (cx - bx) + (bx*bx + by*by) * (ax - cx) + (cx*cx + cy*cy) * (bx - ax)) / d
    ra = math.hypot(x - a[0], y - a[1])
    rb = math.hypot(x - b[0], y - b[1])
    rc = math.hypot(x - c[0], y - c[1])
    return (x, y, max(ra, rb, rc))


_MULTIPLICATIVE_EPSILON = 1 + 1e-14

def is_in_circle(c, p):
    return c is not None and math.hypot(p[0] - c[0], p[1] - c[1]) <= c[2] * _MULTIPLICATIVE_EPSILON


# Returns twice the signed area of the triangle defined by (x0, y0), (x1, y1), (x2, y2).
def _cross_product(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)

def draw_fig(circle, points): 
    xlist = []
    yList = []

    for p in points:
        xlist.append(p[0])
        yList.append(p[1])
    

    h = circle[0]
    k = circle[1]
    r = circle[2]
    circle = plt.Circle((h,k), r, color='g', fill = False, clip_on=False)
    
    fig, ax = plt.subplots()
    ax.axis("equal")
    ax.set_xlim((-150, 150))
    ax.set_ylim((-150, 150))
    ax.add_artist(circle)
    point = plt.plot(xlist,yList, 'bo')
    plt.show()
    # time.sleep(5)
    # plt.close('all')

def findDistance(p1, p2):
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    return distance

def isPointInsdieCircle(point, circle):
    centre = (circle[0], circle[1])
    radius = circle[2]

    dist = findDistance(centre, point)

    return dist <= radius



def generatePoints():
    size = random.randint(20, 100)
    print("No. of points: ", size)
    points = []
    for i in range(0,size):
        x = random.randint(1,100)
        y = random.randint(1,100)
        points.append((x,y))
    
    # print(points)
    return points

def selectRandomPoints(points):
    randomPoints = random.sample(points, 20)
    # print(randomPoints)
    return randomPoints


def findCircleForRandomPoints(randomPoints):
    circle = make_circle(randomPoints)
    return circle

def areAllPointsInsideCircle(points, circle):
    for point in points:
        if not isPointInsdieCircle(point, circle):
            return False
    return True

def driver(points):
    while(True):
        randomPoints = selectRandomPoints(points)
        circle = findCircleForRandomPoints(randomPoints)
        if areAllPointsInsideCircle(points, circle):
            print("Centre: ({}, {})".format(circle[0],circle[1]))
            print("Radius: {}".format(circle[2]))
            draw_fig(circle, points)
            break
        else:
            # draw_fig(circle,points)
            pass


points = generatePoints()
driver(points)

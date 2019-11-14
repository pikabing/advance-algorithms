import heapq
import matplotlib.pyplot as plt

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    try:
        div = det(xdiff, ydiff)
        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div

        a = x >= line1[0][0] and x >= line2[0][0]
        b = x <= line1[1][0] and x <= line2[1][0]

        if (a and b):
            return x, y
        else:
            return -1, -1
    except:
        return -1, -1



class Segment():
    def __init__(self,leftPoint, rightPoint, name):
        self.leftX = leftPoint[0]
        self.leftY = leftPoint[1]
        self.rightX = rightPoint[0]
        self.rightY = rightPoint[1]
        self.type = 1
        self.name = name

class IntersectionPoint():
    def __init__(self,point,l1,l2):
        self.leftX = point[0]
        self.leftY = point[1]
        self.l1 = l1
        self.l2 = l2
        self.type = 2


class TreeNode(): 
    def __init__(self, segment): 
        self.segment = segment 
        # self.y = None
        self.segment1 = segment
        self.left = None
        self.right = None
        self.height = 1
  
class AVL_Tree(): 
    def __init__(self):
        self.pre = None
        self.suc = None
  
    def insert(self, root, segment): 
        if not root: 
            node = TreeNode(segment)
            # node.y = segment.leftY
            return node 
        elif segment.leftY < root.segment.leftY: 
            root.left = self.insert(root.left, segment) 
        else: 
            root.right = self.insert(root.right, segment) 
  
        root.height = 1 + max(self.getHeight(root.left), 
                          self.getHeight(root.right)) 
  
        balance = self.getBalance(root) 
  
        if balance > 1 and segment.leftY < root.left.segment.leftY: 
            return self.rightRotate(root) 
  
        if balance < -1 and segment.leftY > root.right.segment.leftY: 
            return self.leftRotate(root) 
  
        if balance > 1 and segment.leftY > root.left.segment.leftY: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        if balance < -1 and segment.leftY < root.right.segment.leftY: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def delete(self, root, segment): 

        if not root: 
            return root 
  
        elif segment.leftY < root.segment.leftY: 
            root.left = self.delete(root.left, segment) 
  
        elif segment.leftY > root.segment.leftY: 
            root.right = self.delete(root.right, segment) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.getMinValueNode(root.right) 
            root.segment = temp.segment
            root.right = self.delete(root.right,temp.segment) 
  
        if root is None: 
            return root 
  
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 
  
        balance = self.getBalance(root) 
  
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
  
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        y.left = z 
        z.right = T2 
  
        z.height = 1 + max(self.getHeight(z.left),  
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left),  
                         self.getHeight(y.right)) 
  
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        y.right = z 
        z.left = T3 
  
        z.height = 1 + max(self.getHeight(z.left), 
                          self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                          self.getHeight(y.right)) 
  
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def getMinValueNode(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.getMinValueNode(root.left) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
        self.preOrder(root.left) 
        print("{0} ".format((root.segment.leftX, root.segment.leftY)), end="") 
        self.preOrder(root.right) 


    def findPreSuc(self,root, segment): 
        if root is None: 
            return
    
        if root.segment1.leftY == segment.leftY: 
    
            if root.left is not None: 
                tmp = root.left  
                while(tmp.right): 
                    tmp = tmp.right  
                self.pre = tmp 
    
    
            if root.right is not None: 
                tmp = root.right 
                while(tmp.left): 
                    tmp = tmp.left  
                self.suc = tmp  
    
            return 
    
        if root.segment1.leftY > segment.leftY : 
            self.suc = root
            self.findPreSuc(root.left, root.segment1) 
    
        else:
            self.pre = root
            self.findPreSuc(root.right, root.segment1) 

    def findNode(self, root, segment):
        if root is None: 
            return
        if root.segment.leftY == segment.leftY:
            return root
        elif root.segment.leftY > segment.leftY:
            return self.findNode(root.left, segment)
        else:
            return self.findNode(root.right, segment)

    def swapSegment(self,root, segment1, segment2):
        node1 = self.findNode(root, segment1)
        node2 = self.findNode(root, segment2)

        # print(node1)
        if node1 == None or node2 == None:
            return 0
        temp = node1.segment1
        node1.segment1 = node2.segment1
        node2.segment1 = temp 


def sweepLine(eventPoints, status, root):
    while len(eventPoints):
        flag = 1
        event = heapq.heappop(eventPoints)
        # print(event)
        X = event[0]
        
        if event[1].type == 1 and X == event[1].leftX :
            root = status.insert(root, event[1])
            
        elif event[1].type == 1 and X == event[1].rightX:
            status.findPreSuc(root,event[1])
            flag = 0
            root = status.delete(root, event[1])
        else:
            flag = 2
            print("Intersection between segment: {} and {} at point {}".format(event[1].l1.name, event[1].l2.name, (event[1].leftX, event[1].leftY)))
            plt.scatter(event[1].leftX, event[1].leftY, color = 'r')
            status.swapSegment(root, event[1].l1, event[1].l2)

        if flag == 1:
            status.findPreSuc(root, event[1])

            if status.pre != None and status.pre.segment != event[1]:
                segment1 = event[1]
                segment2 = status.pre.segment1

                A = (segment1.leftX, segment1.leftY)
                B = (segment1.rightX, segment1.rightY)
                C = (segment2.leftX, segment2.leftY)
                D = (segment2.rightX, segment2.rightY)

                x,y = line_intersection((A,B), (C,D))

                if x == -1:
                    pass
                else:
                    ip = IntersectionPoint((x,y), segment1, segment2)
                    eP = (ip.leftX,ip)
                    heapq.heappush(eventPoints, eP)
                status.pre = None
                status.suc = None

            if status.suc != None and status.suc.segment != event[1]:
                segment1 = event[1]
                segment2 = status.suc.segment1

                A = (segment1.leftX, segment1.leftY)
                B = (segment1.rightX, segment1.rightY)
                C = (segment2.leftX, segment2.leftY)
                D = (segment2.rightX, segment2.rightY)

                x,y = line_intersection((A,B), (C,D))
                if x == -1:
                    pass
                else:
                    ip = IntersectionPoint((x,y), segment1, segment2)
                    eP = (ip.leftX,ip)
                    heapq.heappush(eventPoints, eP)
                status.suc = None
                status.pre = None

        if flag == 0:
            if status.pre != None and status.suc != None and status.pre.segment != event[1]:
                segment1 = status.suc.segment1
                segment2 = status.pre.segment1

                A = (segment1.leftX, segment1.leftY)
                B = (segment1.rightX, segment1.rightY)
                C = (segment2.leftX, segment2.leftY)
                D = (segment2.rightX, segment2.rightY)

                # print((A,B), (C,D))
                x,y = line_intersection((A,B), (C,D))

                if x == -1:
                    # print("No intersection")
                    pass
                else:
                    # print((x,y))
                    ip = IntersectionPoint((x,y), segment1, segment2)
                    eP = (ip.leftX,ip)
                
                    heapq.heappush(eventPoints, eP)
                status.pre = None
                status.suc = None
                

def main():
    s1 = Segment((1,7), (5,7), 's1')
    s2 = Segment((2,8), (11,1), 's2')
    s3 = Segment((3,2), (10,5), 's3')
    s4 = Segment((6,6), (9,6), 's4')
    s5 = Segment((8,5), (12,2), 's5')

    segments = [s1,s2,s3,s4,s5]

    status = AVL_Tree()
    root = None

    eventPoints = []
    xList = []
    yList = []
    for segment in segments:
        xList.append(segment.leftX)
        xList.append(segment.rightX)
        yList.append(segment.leftY)
        yList.append(segment.rightY)
        eventPoints.append((segment.leftX, segment))
        eventPoints.append((segment.rightX, segment))

    heapq.heapify(eventPoints)

    i = 0

    while i < len(xList):
        plt.plot([xList[i],xList[i+1]], [yList[i],yList[i+1]])
        i += 2
 
    sweepLine(eventPoints, status, root)

    plt.show()

main()
import math
class Point:
    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)
    def distance_to(self,other):
        return math.hypot(self.x-other.x,self.y-other.y)
    def midpoint(self,other):
        return Point((self.x+other.x)/2,(self.y+other.y)/2)
    def to_tuple(self):
        return (self.x,self.y)
def line_equation(a,b):
    if a.x==b.x:
        return None, a.x
    m=(b.y-a.y)/(b.x-a.x)
    c=a.y-m*a.x
    return (m,c), None
def reflect_point_over_line(a,b,c):
    ax,ay=a.x,a.y
    bx,by=b.x,b.y
    px,py=c.x,c.y
    abx=bx-ax
    aby=by-ay
    ab_len=math.hypot(abx,aby)
    if ab_len==0:
        return Point(ax,ay)
    ux=abx/ab_len
    uy=aby/ab_len
    apx=px-ax
    apy=py-ay
    proj_len=apx*ux+apy*uy
    projx=ax+proj_len*ux
    projy=ay+proj_len*uy
    rx=2*projx-px
    ry=2*projy-py
    return Point(rx,ry)
a=Point(*map(float,input("Enter A (x y): ").split()))
b=Point(*map(float,input("Enter B (x y): ").split()))
c=Point(*map(float,input("Enter C (x y) for reflection: ").split()))
print("Distance A-B:", a.distance_to(b))
m_c, x_vert = line_equation(a,b)
if m_c is None:
    print("Line: x=", x_vert)
else:
    m,c_val = m_c
    print("Line: y = {}x + {}".format(m,c_val))
mid=a.midpoint(b)
print("Midpoint A-B:", mid.to_tuple())
ref=reflect_point_over_line(a,b,c)
print("Reflection of C over AB:", ref.to_tuple())




import math
import numpy as np
def read_vec(name):
    return np.array(list(map(float,input(f"Enter vector {name} components (x y): ").split())))
A=read_vec('A')
B=read_vec('B')
C=read_vec('C')
R=A+B+C
def mag(v):
    return math.hypot(v[0],v[1])
def dot(u,v):
    return float(np.dot(u,v))
def angle_deg(u,v):
    du=mag(u); dv=mag(v)
    if du==0 or dv==0:
        return None
    cosv=dot(u,v)/(du*dv)
    cosv=max(-1,min(1,cosv))
    return math.degrees(math.acos(cosv))
def proj(u,v):
    dv2=dot(v,v)
    if dv2==0:
        return np.array([0.0,0.0])
    return (dot(u,v)/dv2)*v
print("Resultant R:", tuple(R))
print("Magnitude |A|:", mag(A))
print("Magnitude |B|:", mag(B))
print("Magnitude |C|:", mag(C))
print("Dot A.B:", dot(A,B))
print("Dot A.C:", dot(A,C))
print("Dot B.C:", dot(B,C))
print("Angle A-B (deg):", angle_deg(A,B))
print("Angle A-C (deg):", angle_deg(A,C))
print("Angle B-C (deg):", angle_deg(B,C))
print("Projection of A onto B:", tuple(proj(A,B)))




import math
import numpy as np
Sx,Sy=map(float,input("Enter S (x y): ").split())
Ex,Ey=map(float,input("Enter E (x y): ").split())
Px,Py=map(float,input("Enter P (x y): ").split())
S=np.array([Sx,Sy]); E=np.array([Ex,Ey]); P=np.array([Px,Py])
SE=E-S
length_segment=math.hypot(SE[0],SE[1])
print("Length of segment SE:", length_segment)
se_len2=SE.dot(SE)
if se_len2==0:
    closest=S
else:
    t=((P-S).dot(SE))/se_len2
    t_clamped=max(0,min(1,t))
    closest=S+t_clamped*SE
print("Closest point on SE to P:", (float(closest[0]), float(closest[1])))
dist_point_segment=math.hypot(P[0]-closest[0],P[1]-closest[1])
print("Distance from P to segment SE:", dist_point_segment)





import numpy as np
a1,b1,c1=map(float,input("Enter a1 b1 c1 for a1*x + b1*y = c1: ").split())
a2,b2,c2=map(float,input("Enter a2 b2 c2 for a2*x + b2*y = c2: ").split())
det=a1*b2-a2*b1
if abs(det) > 1e-12:
    x=(c1*b2-c2*b1)/det
    y=(a1*c2-a2*c1)/det
    print("Intersection point (x,y):", (x,y))
else:
    print("Lines are parallel or coincident.")


# version - 2.x
#                                                            points.py
#
# Classes and objects
#

import math

#*********************************************************
# class Point starts here
#
class Point(object):
    # Documentation string
    """
       The class Point represents a 2D point
       Class attributes:    points
       Instance attributes: x
                            y
    """

    # Class attributes:
    #
    # To access a class attribute, use dot notation, e.g., Point.points
    # as is done in __init__ below.
    # Note: there is only one copy of a class attribute
    #       whereas there is a copy of instance attribute in
    #       every Point instance.
    points = []

    # Constructors
    def __init__(self):
        self.x = 0
        self.y = 0
        Point.points.append(self)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.points.append(self)

    # toString method in Java for those who are familiar with Java
    # Generating a string representation of a Point object
    def __str__(self):
       return '(%g, %g)' % (self.x, self.y)
       # return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # Special names methods. . .
    # With this method defined, we can use + to add two point objects
    # as in p1 + p2 which is equivalent to p1.__add__(p2)
    # See http://docs.python.org/ref/specialnames.html for others
    # Also see http://docs.python.org/reference/ for general language
    # reference
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # With this method defined, two point objects can be compared with
    # >, <, and ==.
    def __cmp__(self, other):
        # compare them using the x values first
        if self.x > other.x: return 1
        if self.x < other.x: return -1

        # x values are the same... check y values
        if self.y > other.y: return 1
        if self.y < other.y: return -1

        # y values are the same too. . . it's a tie
        return 0


    # Other general methods
    def distance_from_origin(elf):
        return math.sqrt(elf.x * elf.x + elf.y * elf.y)

    def distance(self, other):
        dx = math.fabs(self.x - other.x)
        dy = math.fabs(self.y - other.y)
        return math.sqrt(dx * dx + dy * dy)

    def isIn1stQuad(self):
        return (self.x > 0) and (self.y > 0)
        
    # class Point ends here
    #*********************************************************


# Now that a class named Point is defined, let's create some
# Point instances (objects) using the class:

p1 = Point(3, 4)

p2 = Point(10, 20)

print '\np1 = '
print p1           # uses __str__ if defined

print '\np2 = '
print p2
print str(p2)

# without __str__ defined, str(p1) would print something like
# <__main__.Point object at 0x1007a2050>.  That is, Python language tries to
# print as much as it knows about the object as a printed representation. 
# We as a programmer would not be very satisfied with that printed
# representation.  We can provide more information by defining a function that
# can produce a more useful printed representation.  '__str__' is that function.
# So, with __str__ defined as above str(p1) would produce '(3, 4)'.
# Run the above program twice: once with __str__ defined and once more
# without.

print '\nPoint.__doc__ ='
print Point.__doc__


# This computes the distance from the origin to p1.
print '\np1.distance_from_origin() ='
print p1.distance_from_origin()


# This one between p1 and p2.
print '\np1.distance(p2) ='
print p1.distance(p2)

# Add two points
print '\np1.__add__(p2) ='
print p1.__add__(p2)
print p1 + p2

print "\np2.__cmp__(p1) = "
print p2.__cmp__(p1)

if p2 < p1:
    print 'p2 is less than p1'
else:
    if p2 > p1:
        print 'p2 is greater than p1'
    else:
        print 'p1 and p2 are the same'

print '\nPoint.points-------------'
print Point.points


#===========================================================================
# Set of objects
#
# Once we know how to create objects, we would probably want to deal with
# a collection of objects as we try to write interesting programs.  For 
# example, we may want to create a list of point objects and deal with
# the list to find the points that are within a certain distance from the
# origin, say.  You can use your imagination as to how this sort of data
# structures would be useful.  Anyway, let us see how to create a list of
# objects.  Well, let's create one using a function:

# Creates a list of point objects, m * n of them:
#
def create_points_set(m, n):
    points = []
    i = 0
    while i < m:
        # print 'i = ' + str(i)
        j = 0
        while j < n:
            # print '   j = ' + str(j)
            points.append(Point(i, j))
            j = j + 1
        i = i + 1
    return points

# Use the function to create a list:
ps = create_points_set(2, 3)

# Once you create a list, you can do whatever you want to do with it.  Here,
# print each by using a function:

def print_points_set(points):
    for p in points:
        print p

print '\nprint_points_set(ps) ='
print_points_set(ps)

# Find points within a certain distance from the origin
def find_points_within(points, d):
    ps = []
    for p in points:
        # print p.distance_from_origin()
        if (p.distance_from_origin() < d):
            ps.append(p)
    return ps

print '\nprint_points_set(find_points_within(ps, 2)) ='
print_points_set(find_points_within(ps, 2))


#************************************************************
# Inheritance
#
class Point3D(Point):
    """
       The class Point3D represents a colored 3D point
       Class attributes:    points
       Instance attributes: x
                            y
                            z
                            color
    """
    # Class attributes:
    # points = []   # Note the one in Point is being inherited
                    # You can override the one from Point by
                    # defining one here - try it and run it.

    def __init__(self, x=0, y=0, z=0, color='white'):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        Point3D.points.append(self)

    def __str__(self):
       return '(%g, %g, %g, %s)' % (self.x, self.y, self.z, self.color)

    def __add__(self, other):
        return Point3D(self.x + other.x,
                       self.y + other.y,
                       self.z + other.z,
                       self.color)

    def distance_from_origin(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def distance(self, other):
        dx = math.fabs(self.x - other.x)
        dy = math.fabs(self.y - other.y)
        dz = math.fabs(self.z - other.z)
        return math.sqrt(dx * dx + dy * dy + dz * dz)

    # End of Point3D
    #=================================================

p3 = Point3D()

print '\np3 = '
print p3

p4 = Point3D(1, 2, 3, 'red')

print '\np4 = '
print p4

print '\nPoint3D.points-------------'
print Point3D.points

# Add two points
p5 = Point3D(10, 20, 30, 'purple')
print '\np4.__add__(p5) = '
print p4.__add__(p5)
print p4 + p5

# This computes the distance from the origin to p5.
print '\np5.distance_from_origin() ='
print p5.distance_from_origin()

# This one between p3 and p4.
print '\np3.distance(p4) ='
print p3.distance(p4)

p5 = Point3D()
p6 = Point3D()

print '\np5 == p6'   # '==' is like 'equals' in Java
print p5 == p6

print '\np5 is p6'   # 'is' is like '==' in Java
print p5 is p6

print '\np3 ='
print p3

print '\np4 ='
print p4

del p4.color

print '\nafter del p4.color. . . p3 ='
print p3

print '\np4 ='
# next line would not work since color has been deleted from p4
# print p4


# Container with different objects
# 
points2 = []
points2.append(Point(3, 4))
points2.append(Point3D(3, 4, 5, 'blue'))

# Below note that isIn1stQuad is not defined for Point3D, but works.
# Why? It is inherited from Point.
# For distance_from_origin, it is defined in both Point and Point3D,
# and the correct one is used.
# All this is possible because of the dynamic method dispatching mechanism
# that Python supports as do most other object-oriented programming languages
# such as Java, C#, etc.
#
print '\npoints2 ='
for p in points2:
    print str(p.isIn1stQuad()) + ', ' + str(p.distance_from_origin())


#
# For more information on classes and objects in Python, see Chapters 15,
# 16, 17, and 18 of [Downey].


# If you want to understand how types are organized in Python, read
# http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html
# Warning: This is an advanced topic though.





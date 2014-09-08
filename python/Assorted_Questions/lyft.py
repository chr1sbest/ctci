"""
Programming Challenge (Optional)

Calculate the detour distance between two different rides. Given four 
latitude / longitude pairs, where driver one is traveling from point 
A to point B and driver two is traveling from point C to point D, 
write a function (in your language of choice) to calculate the shorter 
of the detour distances the drivers would need to take to pick-up and 
drop-off the other driver.
"""

# Driver 1: Goes from A -> B. Optionally from A -> C -> D -> B
# Driver 2: Goes from C -> D. Optionally from C -> A -> B -> D

# I considered applying a weighted graph algorithm (Dijkstra's/Kruskal)
#   but after drawing it out I realized the solution was much simpler!  
# Both potential routes traverse A<->C and D<->B, the only difference is
#   one driver travels C->D while the other travels A->B. The solution is
#   simply which of these paths is shorter.

def gas_saver(start1, start2, end1, end2):
    """Find shorter path between start1->end1 vs. start2->end2"""
    path1, path2 = distance(end1, start1), distance(end2, start2)
    return "Path 1 is shorter!" if path1 < path2 else "Path 2 is shorter!"

def distance(point1, point2):
    """Calculate distance between two (X,Y) points"""
    x_dist = abs(point1[0] - point2[0])
    y_dist = abs(point1[1] - point2[1])
    hypotenuse = ((x_dist ** 2) + (y_dist ** 2)) ** (1/2.0)
    return hypotenuse

def abs(val):
    """Absolute value"""
    return 0 - val if val < 0 else val

if __name__ == "__main__":
    a = (10, 20)
    b = (15, 25)
    c = (5, 15)
    d = (30, 35)
    print "Given points A:{0} B:{1} C:{2} D:{3}".format(a, b, c, d)
    print gas_saver(a, b, c, d)

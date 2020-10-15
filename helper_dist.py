import rospy
import math

wps = rospy.get_param("/waypoints")
N = len(wps)

def euclidean(a, b):
    return math.sqrt((a['x']-b['x'])**2 + (a['y']-b['y'])**2 + (a['z']-b['z'])**2)


wps['init'] = {'position': {'x': 0, 'y': 0, 'z': 0}}
wp_names = ['init'] + ['wp' + str(i) for i in range(1, N+1)]
for a in wp_names:
    for b in wp_names:
        d = euclidean(wps[a]['position'], wps[b]['position'])
        print "    (= (distance " + a + " " + b + ") " + str(d) + ")"
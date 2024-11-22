import sys
import math
import os

grade = 0
segFaults = 0

for line in sys.stdin:
    sys.stdout.write(line)
    if ("❌ Seg" in line):
        segFaults += .34
        segFaults %= 1.03
        grade += math.floor(segFaults)*15
    if ("❌ Ga" in line):
        grade += 15
    if ("❌ Bu" in line):
        grade += 15
    if ("❌ Til" in line):
        grade += 15
    if ("❌ ne" in line):
        grade += 15
    if ("❌ Le" in line):
        grade += 15
    if ("❌ no" in line):
        grade += 15
    if ("❌ Di" in line):
        grade += 5
    if ("❌ In" in line):
        grade += 5
    
    
    
    

f = open("States/grade.txt", "w")
f.write(str(grade))
f.close()
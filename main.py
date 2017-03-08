
#!/usr/bin/python3
import calc
import getDoc
import matplotlib.pyplot as plt

#Use grade points from document as x-coordinates and list item numbers as y-coordinates
#Use the 'calc' module to calculate the accumulated grade point average for each semester
def plot(sems):
    y = []
    x = []
    accGP = []

    for gradePnts in sems:
        accGP.extend(gradePnts)
        x.insert(len(x), calc.calc_gpa(accGP))
        y.insert(len(y), int(len(y)+1))

    plt.plot(y, x)
    plt.xlabel('Semester')
    plt.ylabel('GPA')
    plt.title('Semesterly GPA Chart')
    plt.show()

plot(getDoc.collectPoints())


import matplotlib.pyplot as plt
import calc
def plot(sems):
    y = []
    x = []
    accGP = []

    for gradePnts in sems:
        accGP.extend(gradePnts)
        x.insert(len(x), calc_gpa(accGP))
        y.insert(len(y), int(len(y)+1))

    plt.plot(y, x)
    plt.xlabel('Semester')
    plt.ylabel('GPA')
    plt.title('Semesterly GPA Chart')
    plt.show()

def calc_gpa(subs):
    CP = 6
    sumCP = len(subs) * CP
    accVal = 0
    for mark in subs:
        GP = 0
        if mark < 50:
            GP = 0.5
        elif mark >= 50 and mark <=64:
            GP = 1.5
        elif mark >=65 and mark <=74:
            GP = 2.5
        elif mark >=75 and mark <=84:
            GP = 3.5
        elif mark >=85 and mark <=100:
            GP = 4
    #Grade point scheme determined by UTS 
        accVal = (GP * CP) + accVal
    gpa = accVal/sumCP
    return gpa
    #print 'Total Credit Points Gained: ', sumCP


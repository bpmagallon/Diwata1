def errCatch(num, add):
    if num==1:
        print "No bin file added!"
    elif num==2:
        if len(add)<1:
            print "Check file address!"
            return 2
    elif num==3:
        print "Check gain and exp time!"

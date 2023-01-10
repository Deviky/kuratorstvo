for A in range(10000):
    for x in range (13):
        for y in range (13):
            M=2*pow(15,5)+y*pow(15,4)+2*pow(15,3)+3*pow(15,2)+x*15+5
            N=6*pow(13,4)+7*pow(13,3)+x*pow(13,2)+9*13+y
            if (M+A)%N==0:
                print(A)


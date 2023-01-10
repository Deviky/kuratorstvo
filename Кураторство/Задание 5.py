f = open("D:\Кураторство\hh.txt")
s = f.readline()
k = 0
maxK = 0
i = 0
while i<len(s):
    if (i<len(s)-2) and (s[i]!='A' and s[i]!='O') and (s[i+1]!='A' and s[i+1]!='O') and (s[i+2]=='A' or s[i+2]=='O'):
        k = k+1
        #print("\n", s[i]+s[i+1]+s[i+2])
        i=i+3
    else:
        if maxK<k:
            maxK = k
        k = 0
        i=i+1
    if maxK < k:
        maxK = k
print(maxK)
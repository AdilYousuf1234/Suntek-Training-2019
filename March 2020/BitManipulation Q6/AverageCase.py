def Solution():
    d=dict()
    l=list(map(int,input().split()))
    for i in range(len(l)):
        if(l[i] not in d):
            d[l[i]]=0
        else:
            d[l[i]]+=1
    #print(d)
    for i in d:
        if(d.get(i)==0):
            print(i)
            break
Solution()
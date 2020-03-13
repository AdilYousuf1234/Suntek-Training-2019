def Solution():
    d=dict()                            #create a dictionary
    l=list(map(int,input().split()))    #input
    for i in range(len(l)):             #
        if(l[i] not in d):              #if elements is not a key in dictionary
            d[l[i]]=0                   #initialize with 0
        else:                           #else
            d[l[i]]+=1                  #increment the value
    #print(d)
    for i in d:                         #
        if(d.get(i)==0):                #if value is equal to 0
            print(i)                    #the key is answer
            break
Solution()

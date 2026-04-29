def pr(a,ind=0):
    
    if(ind == len(a)):
        return
    print(a[ind])
    pr(a, ind+1)
    
    


d = [1,2,3,4]

print(pr(d))




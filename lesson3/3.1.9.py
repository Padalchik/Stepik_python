def modify_list(l): 
    x=len(l) 
    i=0 
    while i!=x: 
        if l[i]%2!=0: 
            l.remove(l[i]) 
            x-=1 
        else: 
            l[i]=l[i]//2 
            i+=1

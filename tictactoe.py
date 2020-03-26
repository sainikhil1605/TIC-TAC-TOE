#VATTI SAI NIKHIL REDDY
#17881A0434
a=[]
for i in range(3):
    a.append([0,0,0])



c=0
def printfn():

    for i in range(3):
        for j in range(3):
            if(a[i][j]==0):
                print('Y',end=' ')
            else:    
                print(a[i][j],end=' ')
        print()
def move(k,l):
    h=0
    for i in range(3):
        for j in range(3):
            h=h+1
            if(h==k):
                
                a[i][j]=l
                
                break

    check()
def check():
    f=0
    global c
    for i in range(3):
        j=0
        if(a[i][j]==a[i][j+1] and a[i][j+1]==a[i][j+2] and a[i][j]!=0):
            w=a[i][j]
            f=1
            break
    i=0
    for j in range(3):
        i=0
        if(a[i][j]==a[i+1][j] and a[i+1][j]==a[i+2][j] and a[i][j]!=0):
            w=a[i][j]
            f=1
            break
    j=0
    i=0
    if(a[i][j]==a[i+1][j+1] and a[i+1][j+1]==a[i+2][j+2] and a[i][j]!=0):
        w=a[i][j]
        f=1
    j=2
    i=0
    if(a[i][j]==a[i+1][j-1] and a[i+1][j-1]==a[i+2][j-2] and a[i][j]!=0):
        w=a[i][j]
        f=1
    if(f==1):
        print(str(w)+" is the winner")
    else:
        printfn()
        
        c=c+1
        if(c>9):
            print("It is Draw")
            return
        print("Enter your position of choice")
        l=int(input())
        if(c%2==0):
            move(l,"*")
        else:
            move(l,"O")
check()
        
        
        
                
            
        

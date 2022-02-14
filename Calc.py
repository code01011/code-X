x,y=map(float,input().split())
x=int(x)
if (x+0.5<=y and x%5==0):
    print (float(y-x-0.5)) 
else:
    print(float(y))

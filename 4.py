import math
def minimax(depth, nodeIndex, maxturn) :
    if depth==Depth :
        return values[nodeIndex]
    if maxturn :
        best=minimum
        for i in range(Children) :
            val=minimax(depth+1, nodeIndex*Children+i, False)
            best=max(best,val)
            print(depth+1,nodeIndex*Children+i,best,val)
        return best
    else :
        best=maximum
        for i in range(Children) :
            val=minimax(depth+1, nodeIndex*Children+i, True)
            best=min(best,val)
            print(depth+1,nodeIndex*Children+i,best,val)
        return best
if __name__=="__main__" :
    maximum,minimum=1000,-1000
    values = [3,12,8,2,4,6,14,5,4]
    Children=3
    Depth=math.log(len(values),Children)
    print(values)
    print("The optimal value is :",minimax(0,0,True))


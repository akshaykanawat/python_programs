myStr="{[()](){}}"
openList = ["[","{","("]
closeList = ["]","}",")"]
def balance(myStr):
    stack= []
    for s in myStr:
        if s in openList:
            stack.append(s)
        elif s in closeList:
            pos=closeList.index(s) #it will return indexes
            if ((len(stack)>0) and (openList[pos]==stack[-1])): #check if last value of stack is in any pos index of openList
                stack.pop()
            else:
                return False
    return len(stack)==0
       
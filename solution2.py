# Write code for algorithm 2 below

def numbers(lowerNum, higherNum):
    if lowerNum > higherNum:
        return
    else:
        print(lowerNum)
        numbers(lowerNum + 1, higherNum)

n=10
numbers(1,n)
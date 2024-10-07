# Write code for algorithm 1 below
def count(n):
    if n == 0:
        return 
    else:
        print(n)
        count(n-1)

n = 8 
count(n)
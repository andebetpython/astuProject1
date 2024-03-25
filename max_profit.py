
def solution_two(array):
    profit=0
    minimum=array[0]
    for i in range(1,len(array)):
        minimum=min(minimum,array[i])
        profit=max(profit,array[i]-minimum)
    return profit
a=[7,1,5,3,6,4]
print(solution_two(a))

def climb_star(star):
    prev1=1
    prev2=1
    for i in range(2,star+1):
        current=prev1+prev2
        prev1=prev2
        prev2=current
    return prev2
print(climb_star(7))


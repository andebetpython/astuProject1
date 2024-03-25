#activity selection problem
#method1
def activity():
    act=["A1","A2","A3"]
    start=[12,10,20]
    finish=[25,20,30]
    h=sorted(finish)
    sorted_act=[y for x,y in sorted(zip(finish,act))]
    print(sorted_act[0])
    sorted_act.pop(0)
    for i in range(3):
        if h[0]<=start[i]:
            print(sorted_act[i+1])
print(activity())
#method2
def max_activities(activities, start, finish):
    n = len(activities)
    s=sorted(finish)
    last_finish = s[0]
    selected_activities = [activities[finish.index(last_finish)]]
    for i in range(1, n):
        if start[i] >= last_finish:
            selected_activities.append(activities[i])
    return selected_activities
# Example usage:
activities = ["A1", "A2", "A3"]
start = [12, 10, 20]
finish = [25, 20, 30]
result = max_activities(activities, start, finish)
print(result)

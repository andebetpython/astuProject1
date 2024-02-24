import heapq
heap=[]
l=[10,34,87,9,6]
for i in l:
    heapq.heappush(heap,i)

print(heap)
#this used to remove the smallest element from the lis and return it or used to delate the root node becuse by defult heap method is arrange in min heap form
print(heapq.heappop(heap))
#to conver the given list in to the heap form we use heapify method
heapq.heapify(l)
print(l)
#this method is used to inset new element to heap and delate and return its smalest value or root node
print(heapq.heappushpop(heap,50))
#this method is used first push and then pop the smalest elemeint of the list
print(heapq.heapreplace(heap,800))
#this method is used to find the n smalest numbers from the given list
k=[89,90,45,23,12,32]
print(heapq.nsmallest(2,k))
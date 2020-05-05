#COUNTSORT
def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for a in array1:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1

n = int(input("Enter number of elements : "))

arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

max_val = 0
for i in range(n):
	if(arr[i]>max_val):
		max_val=arr[i]
print(counting_sort(arr,max_val)),
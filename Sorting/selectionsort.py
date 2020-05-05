#SELECTIONSORT
def selection(arr,n):
	for i in range(0,n-1):
		min = i
		for j in range(i,n):
			if(arr[j]<arr[min]):
				min = j 
		arr[min],arr[i]=arr[i],arr[min]

arr =[9 , 1, 3, 6, 4]
n = len(arr)
selection(arr,n)
for i in range(0,n):
	print("%d" %arr[i]),				
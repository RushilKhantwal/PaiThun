#BUBBLESORT
def bubble(arr,n):
	for i in range(0,n-1):
		for j in range(0,n-i-1):
			if(arr[j]>arr[j+1]):
				arr[j],arr[j+1]=arr[j+1],arr[j]

arr =[9 , 1, 3, 6, 4]
n = len(arr)
bubble(arr,n)
for i in range(0,n):
	print("%d" %arr[i]),				
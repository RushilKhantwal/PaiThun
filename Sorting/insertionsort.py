#INSERTIONSORT
def insert(arr,n):
	for i in range(1,n):
		min = arr[i]
		j=i-1
		while(j>= 0 and arr[j]>min):
			arr[j+1] = arr[j]
			j=j-1
		arr[j+1]=min

arr =[9 , 1, 3, 6, 4]
n = len(arr)
insert(arr,n)
for i in range(0,n):
	print("%d" %arr[i]),			
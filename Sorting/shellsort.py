#SHELLSORT
def shellsort(arr):
	n = len(arr)
	gap = n//2

	while gap>0:
		for i in range(gap,n):
			temp = arr[i]
			j=i
			while j>=gap and  arr[j-gap]>temp:
				arr[j]=arr[j-gap]
				j-=gap

			arr[j]=temp

		gap //= 2

n = int(input("Enter number of elements : "))

arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print("Array before sorting: ")
for i in range(n):
	print("%d" %arr[i]),

shellsort(arr)
print("\nArray after sorting: ")
for i in range(n):
	print("%d" %arr[i]),					
## Some misterious code...

def mistery(array,l,r):
	if l > r:
		return -1
	m = (l+r)/2
	if array[m] < m:
		return mistery(array, m+1,r)
	else:
		return mistery(array,l,m-1)

array = [-1,0,2]
l = array[0]
r = array[-1]

print mistery(array,l,r)
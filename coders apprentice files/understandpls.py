#understand this complex looping
#ikon beth


for i in range(3):
	print("Entering the outer loop for i = ", i)
	for j in range(3):
		print("Entering the inner loop for j = ", j)
		print("(i,j) = ({},{})".format(i,j))
		print("Leaving the inner loop")
	print("Leaving the outer loop")

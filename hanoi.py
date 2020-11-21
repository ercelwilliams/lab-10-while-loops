def hanoi(n,f,h,t) :
	if n==0 :
		return

	hanoi(n-1,f,t,h)
	print("Move disk", n, "from", f, "to", t)
	hanoi(n-1,h,f,t)

n = 4
hanoi(n,"A","B","C")

def add(x,y):
	return x+y
def subtract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	return x/y
print("Enter any operation:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.exit")
while True:
	choice=input("enter your choice(1/2/3/4/5)")
	
	if choice in('1','2','3','4'):
		x=float(input("Enter value of x:"))
		y=float(input("Enter value of y:"))
	if choice=='1':
		print(add(x,y))
	elif choice=='2':
		print(subtract(x,y))
		
	elif choice=='3':
		print(multiply(x,y))		
		
	elif choice=='4':
		print(divide(x,y))		
	else:
		print( invalid)	
	 

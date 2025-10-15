'''nt("Hello kitti"),
#function
def sum():
    a = 5
    b = 6
    print("Sum=", a+b)
sum()
#condition
#input 2 number and check
a= int(input("Enter your number a: "))
b= int(input("Enter your number b: "))
if a>=b:
    print(f'a={a} is greater than or equal to b={b}')
else:
    print(f'a={a} is less than b={b}')
#method1
for i in range(10):
    print("i=",i)
#method2
for i in range(5,10,15):
    print("i=",i)'''

U=list(input("Enter your list: "))
print(U)
#ADDSOMETHING
#UPDATE
#p=input ("Enter your update: ")
#huoi_goc = "12345"
chuoi_moi = U.replace("2", "0") # Thay thế '2' bằng '0'
print(chuoi_moi) # Output: 10345

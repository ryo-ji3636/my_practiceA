#input x is equal or not to y
x = int(input("What's x? ->"))
y = int(input ("What's y? ->"))

if x == y:
    print("x is equal to y")

else:
    print("x is not equal to y")

#modulo
def mol(num):
   if num % 2 == 0:
      print(f"{num} is even number")
   else:
       print(f"{num} is odd number")

def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False



#check the score condition
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >=80:
    print("Grade: B")
elif score >=70:
    print("Grade: C")
elif score >=60:
    print("Grade: D")
else:
    print("Grade: F")

#define
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:        
        return True      
    #"return True if n % 2 == 0 else False" is also OK

    else:
        return False


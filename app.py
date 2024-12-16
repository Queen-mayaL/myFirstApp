from icecream import ic
from myHelp.helper import *


ar =[3,4,5,6,]
n1 = int(input("please enter a number: "))
n2 = int(input("please enter a number: "))

if __name__ == '__main__':
    ic(ar)
    print(f"the bigger number is: {bigger(n1,n2)}")
    print(f"the smaller number is: {smaller(n1,n2)}")
    print(f"the multiplied number is: {mult(n1,n2)}")
    print(f"is n1 divisible by n2: {Divisible(n1,n2)}")
    print(f"are the numbers equal: {isEqual(n1,n2)}")
    print(f"the sum is: {sum(n1,n2)}")



import math
import sys

def prime_check(n): #Use a function to determine the primality of a number.
    count = 0 #A count of the number of loops, since we cannot tell whether a number is prime or not until we have exhausted trial division.
    for i in range(2, n + 1):
        count +=1
        if i == n: #We don't need to divide a number by itself since this fits into the definition of a prime number.
            if count == len(range(2, n + 1)): #However, if the number is 2, there are no other numbers by which to divide, so the count should be full and the number determined to be prime.
                x = True
                return x
            continue
        if n % i == 0: #However, if the number has a divisor, then we know it's not prime and exit the function.
            x = False
            return x
        if count == len(range(2, n + 1)): #Once trial division has been exhausted (i.e., we've gone through the entire list of numbers from 2 to n), we know the number is prime and exit the function.
            x = True
            return x

def main(y):
    if y % 2 != 0: #Using a sentinel statement here to determine whether the user has entered an even number or not.
        print("Please enter an even number.") #If the number is even, print this statement and exit the function.
        return
    for n in range(2, y): #Create a list of possible addends for the number the user has entered.
        check = prime_check(n) #Check the each number in the list to determine whether it is prime or not.
        if check == False: continue #If the prime_check function returns a value of false, we know the number not be prime. Continue the loop.
        if check == True: #If a number comes back as prime, subtract it from the even number the user entered. Since subtraction is the inverse of addition, the difference will be the other addend.
            test = y - n
            check2 = prime_check(test) #Then, check the difference to determine whether it is prime or not.
            if check2 == True:
                print("Two prime numbers that add up to your number", y, "are", n, "and", test, ".") #If the difference is prime, then we have our answer!
                break
            if check2 == False: continue #If the difference is not prime, continue the loop.


if __name__ == "__main__":
    y = int(sys.argv[1])
    main(y)

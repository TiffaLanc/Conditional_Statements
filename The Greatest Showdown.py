#Task 1 Identify the greatest: Write a python program that asks the user to enter three numbers. Your code should identify and print out the largest number among the three.

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

largest = max(n1, n2, n3)
print("The largest number is:", largest)





#Task 2 Identify the smallest: Improve upon your code from Task 1 to also determine the smallest number among the three and print it out. 
#Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. "


smallest = min(n1, n2, n3)

print("The smallest number is: ", smallest)
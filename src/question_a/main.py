#add import
from question_a import testHigh, testLow, Total, Average
print("Please enter 5 numbers in a row, press enter when you've decided on a number.")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
useSet = [num1, num2, num3, num4, num5]
print("Highest Number:", testHigh(useSet),"\nLowest Number:", testLow(useSet), "\nTotal:",Total(useSet), "\nAverage:", Average(useSet))

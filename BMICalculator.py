# BMICalculator.py
# Your job is to write a BMI calculator that matches the formula
# and chart on http://flightphysical.com/medical-exam/weight
import math

##weight (lb) / [height (in)]2 x 703
# Define Function below
# be sure to return an integer

def calculateBMI(h, w):
    BMI = w/(h**2)*703
    BMI = round(BMI)
    return BMI
    



if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
##    Example
    answer = calculateBMI(62.0, 120.0)
    print(answer)

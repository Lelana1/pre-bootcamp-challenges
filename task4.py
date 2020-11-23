#  Write a function that takes 2 numbers as input. 
# If either of the numbers is 3 AND the sum of the numbers contains a 3 then return true. Otherwise return false

def three_checker(x,y):
    sum = x + y
    if (x or y) == 3 and '3' in str(sum):
        return True
    else:
        return False

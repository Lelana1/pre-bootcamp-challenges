#  Write a function that takes 2 numbers as input. 
# If either of the numbers is 3 AND the sum of the numbers contains a 3 then return true. Otherwise return false

def three_checker(x, y):
    sum = x + y
    sum = str(sum)
    i = 0
    while i < len(sum):
        if sum[i] == '3':
            return (True)
        i += 1
    if x == 3 or y == 3:
        return (True)
    else:
        return (False)
    
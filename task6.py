# White a function that takes in three numbers and returns the maximum number. Do this without using any builtin methods. Write your own logic from scratch.

def max_number(x, y, z):
    if z >= x and z >= y:
        return z
    if y >= x and y >= z:
        return y
    if x >= y and x >= z:
        return x
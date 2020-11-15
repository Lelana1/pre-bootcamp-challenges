def sum_of_multiple():
    results = 0
    i = 1
    while i <= 1000:
        if i % 3 == 0 or i % 5 == 0:
            results = results + i
        i = i + 1
    print("The sum is", results)
        
sum_of_multiple()
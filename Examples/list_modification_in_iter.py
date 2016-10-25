
numbers = range(10)
for num in numbers:
    if num==3:
        numbers.remove(num)
    print num
    
numbers = range(10)
to_del = []
for num in numbers:
    if num==3:
        to_del.append(num)
for num in to_del:
    numbers.remove(num)
print numbers

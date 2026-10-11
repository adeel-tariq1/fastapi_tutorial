def count_up():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")
    yield 3

gen = count_up()      # nothing runs yet! it just creates a generator object
print(next(gen))      # prints "start", then gives 1
print(next(gen))      # prints "middle", then gives 2
print(next(gen))      # prints "end", then gives 3
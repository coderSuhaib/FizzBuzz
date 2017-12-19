
x = 3
y = 5

for count in range(1,101,1):
    if count % x == 0 and count % y == 0:
        print("FizzBuzz")
    elif count % x == 0:
        print("Fizz")
    elif count % y == 0:
        print("Buzz")
    else:
        print(count)

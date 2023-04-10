print("Digite um número")
número = int(input("> "))

if número % 3 ==0 and número % 5 ==0:
    print("FizzBuzz")
if número % 3 ==0 and número % 5 !=0:
    print("Fizz")
if número % 3 !=0 and número % 5 ==0:
    print("Buzz")
if número % 3 !=0 and número % 5 !=0:
    print(número)

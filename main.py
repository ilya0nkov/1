def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("введите num1\n"))
num2 = int(input("введите num2\n"))

gcd = euclidean(num1, num2)
print(f"НОД({num1}, {num2}) = {gcd}")
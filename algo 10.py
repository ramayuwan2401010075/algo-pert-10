print("perulangan 1")
for a in range(11):
    print(a)

print("perulangan 2")
for b in range(0, 11):
    print(b)

print("perulangan 3") 
for c in range(0, 22, 7):
    print(c)


#hitung total angka 
numbers = [15, 25, 35, 45, 55]
total = 0

for num in numbers:
    total += num

print("Total nilai:", total)


#menghitung bilangan fibonaci
n = int(input("Masukkan jumlah angka Fibonacci: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b



#menghitung bilangan prima
number = int(input("Masukkan angka: "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime and number > 1:
    print(number, "adalah bilangan prima.")
else:
    print(number, "bukan bilangan prima.")

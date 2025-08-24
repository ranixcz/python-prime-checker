user_numbers = input("Enter numbers separated by comma, space or dot: ").replace(',', ' ').replace('.', ' ')
prime = []


try:
    numbers = [int(x) for x in user_numbers.split() if int(x) > 1]
except ValueError:
    print("Incorrect number or you used letter.")
    exit()


for num in numbers:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        prime.append(num)
        print(f"{num} is prime")

print(f"Prime numbers: {prime}")

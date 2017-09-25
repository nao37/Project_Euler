def main():
    prime_list = []
    number = 2
    while True:
        for i in range(2, (number + 1)):
            if number % i == 0 and number != i:
                break
            elif number % i == 0 and number == i:
                prime_list.append(number)
        if len(prime_list) == 10001:
            print(prime_list[-1])
            return False
        number += 1

if __name__ == '__main__':
    main()

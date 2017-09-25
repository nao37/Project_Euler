def main(number):
    prime_list = []
    division_list = []
    # 因数を求める
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            division_list.append(i)
            if len(division_list) >= 2 and (i * division_list[-2] == number or i * i == number):
                break
    for j in division_list:
        divi = number / j
        if not divi in division_list:
            division_list.append(int(divi))
        else:
            break
    # 因数が素数か調べる
    for num in division_list:
        for k in range(2, num + 1):
            if num % k == 0 and k == num:
                prime_list.append(num)
            elif num % k == 0:
                break
    print(prime_list)
if __name__ == '__main__':
    main(600851475143)

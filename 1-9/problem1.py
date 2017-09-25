def main():
    num = [ 1, 2 ]
    for i in range(2000):
        num.append( num[i] + num[i+1] )
        if num[i+1] >= 4000000:
            break
    print(sum( m for m in num if m % 2 == 0 ))
if __name__ == '__main__':
    main()

def main():
    num1 = 1
    num2 = 2
    index = 0
    total = 2
    while True:
        if index % 2 == 0:
            num1 = num1 + num2
            if num1 <= 4000000:
                if num1 % 2 == 0: total += num1
                index += 1
            else:
                break
        else:
            num2 = num1 + num2
            if num2 <= 4000000:
                if num2 % 2 == 0: total += num2
                index += 1
    print(total)
if __name__ == '__main__':
    main()

def main():
    a, b, c = '9', '8', '9'
    while True:
        division_num = 999
        num_array = [a, b, c, c, b, a]
        integer = ''
        for i in num_array:
            integer += i
        while division_num >= 100:
            sum += 1
            if int(integer) / division_num >= 1000:
                break
            elif int(integer) % division_num == 0:
                print(int(integer), division_num, int(int(integer) / division_num))
                return False
            division_num -= 1
        if not int(c) == 0:
            c = str(int(c) - 1)
        else:
            c = '9'
            if not int(b) == 0:
                b = str(int(b) - 1)
            else:
                b = '9'
                if not int(a) == 1:
                    a = str(int(a) - 1)
                else:
                    return False

if __name__ == '__main__':
    main()

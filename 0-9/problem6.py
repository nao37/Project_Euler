def main():
    addition = 0
    multiple = 0
    for i in range(1, 101):
        addition += i**2
        multiple += i
    print(multiple ** 2 - addition)

if __name__ == '__main__':
    main()

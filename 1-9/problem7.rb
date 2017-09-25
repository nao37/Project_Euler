def prime()
  num = 2
  prime_list = []
  division_num = 2
  while prime_list.length < 10001
    if num % division_num == 0
      if division_num == num
        prime_list << num
        division_num = 2
        num += 1
        next
      else
        division_num = 2
        num += 1
        next
      end
    end
    division_num += 1
  end
  p prime_list[10000]
end
prime()

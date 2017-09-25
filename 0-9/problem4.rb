def maltiple()
  a, b, c = 9, 8, 9
  while a != 0
    division_num = 999
    num_list = [a,b,c,c,b,a]
    num = num_list.join.to_i
    while division_num >= 100
      if num % division_num == 0
        answer = num / division_num
        if answer.to_s.length == 3
          p answer
          p division_num
          p num
          return false
        elsif answer.to_s.length > 4
          break
        end
      end
      division_num -= 1
    end
    if c != 0
      c -= 1
    else
      c = 9
      if b != 0
        b -= 1
      else
        b = 9
        a -= 1
      end
    end
  end
end
maltiple()

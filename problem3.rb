require 'prime'
p 600851475143.prime_division

def resolve(number)
  evaluation_num = 1
  prime_numbers = []
  while evaluation_num <= number / 2
    division_num = 1
    division_num_list = []
    while division_num <= evaluation_num
      if evaluation_num % division_num == 0
        division_num_list << division_num
      end
      division_num += 1
    end
    if division_num_list.length == 2
      if number % evaluation_num == 0
        p evaluation_num
        prime_numbers << evaluation_num
      end
    end
    evaluation_num += 2
  end
  p prime_numbers
end
resolve(600851475143)

def difference(num)
  add = 0
  maltiple = 0
  1.upto(num) do |i|
    add += i
    maltiple += i * i
  end
  p add * add - maltiple
end
difference(100)

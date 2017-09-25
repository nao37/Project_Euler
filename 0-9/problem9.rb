require 'complex'
def pythagoras()
  num = 3
  while (1000 - num * num) >= 0
    difference = 1000 - num * num
    list = []
    1.upto(num - 1) do |i|
      list << i * i
    end
    len = list.length
    0.upto(len - 1) do |i|
      i.upto(len - 1) do |j|
        if difference == (list[i] + list[j])
          return num * Math.sqrt(list[i]).to_i * Math.sqrt(list[j]).to_i
        end
      end
    end
    num += 1
  end
end
p pythagoras()

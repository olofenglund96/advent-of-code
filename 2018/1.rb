total = 0
freqs = [0]
arr = File.open('inputs/1')

while true
  arr.each do |line|
    sign = line[0];
    amount = line[1..line.length-1].to_i

    if sign == '-'
      total -= amount
    else
      total += amount
    end

    freqs.each do |f|
      if f == total
        puts total
        return 1
      end
    end

    freqs.push(total)
  end

end

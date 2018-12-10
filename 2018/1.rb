require 'set'
total = 0
freqs = Set[0]
nums = 1
arr = File.open('inputs/1').to_a
loop do
  arr.each do |line|
    sign = line[0]
    amount = line[1..line.length-1].to_i

    if sign == '-'
      total -= amount
    else
      total += amount
    end

    if freqs.include?(total)
      puts total
      return
    end

    freqs.add(total)
  end
end

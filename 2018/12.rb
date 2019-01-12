puts 2370 + (50000000000-89)*21
arr = File.open('inputs/12').to_a

pots = arr[0].strip.chars
patterns = {}
for i in 1..arr.length-1
  s = arr[i].split(' ')
  patterns[s[0]] = s[2]
end
#puts patterns.inspect
generations = Array.new(301) { Array.new(pots.length*100, '.')}

generations[0].insert((pots.length*24).floor, pots).flatten!

#puts generations[0].inspect
prev_score = 0
first_index = 0
generations.first.each_with_index do |p, a|
  if p == '#'
    first_index = a
    break
  end
end
puts first_index
300.times do |b|
  cind = -1
  score = 0
  generations[b].each_with_index do |p, a|
    if p == '#'
      #puts "Index: #{i}, Score: #{i-first_index}"
      if cind == -1
        cind = a
      end
      score += a-first_index
    end
  end
  puts "Iteration: #{b}, Score: #{score}, Score diff: #{score - prev_score}, First Pot index: #{cind}"
  prev_score = score

  for a in 0..generations[0].length-4
    current_pots = generations[b][a..a+4]
    match = false


    patterns.each_key do |k|

      if current_pots == k.chars
        #puts "Pots: #{current_pots.inspect}, Patterns: #{k.chars.inspect}, Result: #{patterns[k]}"
        generations[b+1][a+2] = patterns[k]
        match = true
        break
      end
    end
    generations[b+1][a+2] = generations[b][a+2] unless match
  end
  #puts i
end

first_index = 0

generations.first.each_with_index do |p, i|
  if p == '#'
    first_index = i
    break
  end
end


score = 0
puts first_index
puts '-----------------------'
generations[20].each_with_index do |p, i|
  if p == '#'
    puts "Index: #{i}, Score: #{i-first_index}"
    score += i-first_index
  end
end
=begin
generations.each do |p|
  puts p[40..65].to_s
end
=end
puts '--------------------'
#puts generations[20].inspect
puts score

puts "Mod : #{(5000000000-186) % 11}" #286

#105000000480

# Gissningar
# 1050000000459
# 1050000000480
# 1050000000501

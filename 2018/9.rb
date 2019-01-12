
players = 9 #432
highest_marble = 46+23+23+23+23+23 #71019*100
scores = Array.new(players, 0)
current_marble = 0
index = 1
marbles = [0]
removed_marbles = []
removed_indexes = []
while index <= highest_marble
  unless index % 23 == 0
    next_index = current_marble+2

    if next_index > marbles.length
      next_index -= marbles.length
    end

    marbles.insert(next_index, index)

    current_marble = next_index
  else
    scores[(index) % players] += index
    rm_index = current_marble-7
    rm_index += marbles.length if rm_index < 0
    puts "Index: #{index}, RM: #{marbles[rm_index]}"
   # puts rm_index, marbles[rm_index-3..rm_index+3].inspect
   # puts marbles.inspect
   del = marbles.delete_at(rm_index)
   removed_marbles << del
   removed_indexes << rm_index
    scores[(index) % players] += del
    current_marble = rm_index
  end

  puts "Player: #{((index-1) % players)+1}, Marbles: #{(marbles.each_with_index.map {|m,i| i == current_marble || i == marbles.length + 1 + current_marble ? "(#{m})".to_s : m}).inspect}"
  index += 1
  #printf("\rPercentage: %d%", (index/highest_marble)*100)
end

puts (scores.sort {|a,b| b <=> a})[0..10].inspect

puts '--------------------'
puts removed_marbles.inspect
puts '--------------------'
puts removed_indexes.inspect

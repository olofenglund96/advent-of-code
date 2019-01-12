class Node
  attr_accessor :next, :prev
  attr_reader :value

  def initialize(value)
    @value = value
    @next = self
    @prev = self
  end

  def to_s
    "... #{@prev.value} -> #{@value} -> #{@next.value} ..."
  end
end

def add_next(node, next_node)
  temp = node.next
  node.next = next_node
  next_node.next = temp
  next_node.prev = node
  temp.prev = next_node
  next_node
end

def remove(node)
  node.prev.next = node.next
  node.next.prev = node.prev
  return node.value, node.next
end

def print_marbles(first, current)
  marble = first
  loop do
    if marble == current
      printf("(#{marble.value}) -> ")
    else
      printf("#{marble.value} -> ")
    end
    marble = marble.next
    break if marble == first.prev
  end
  puts "\n --------"
end


players = 432
highest_marble = 71019*100
scores = Array.new(players, 0)
index = 1
current_marble = Node.new(0)
first = current_marble

while index <= highest_marble
  unless index % 23 == 0
    current_marble = add_next(current_marble.next, Node.new(index))
  else
    scores[(index) % players] += index
    #puts "Index: #{index}, RM: #{marbles[rm_index]}"
   # puts rm_index, marbles[rm_index-3..rm_index+3].inspect
   # puts marbles.inspect
    7.times do
     # puts current_marble.prev.value
      current_marble = current_marble.prev
    end

    #puts current_marble.value

    val, next_node = remove(current_marble)
    scores[(index) % players] += val
    #puts next_node
    current_marble = next_node
  end
  #print_marbles(first, current_marble)
  #puts "Player: #{((index-1) % players)+1}, Marbles: #{(marbles.each_with_index.map {|m,i| i == current_marble || i == marbles.length + 1 + current_marble ? "(#{m})".to_s : m}).inspect}"
  index += 1
  #printf("\rPercentage: %d%", (index/highest_marble)*100)
end

first = current_marble

puts ''
puts (scores.sort {|a,b| b <=> a})[0..10].inspect

class Node
  attr_accessor :next, :prev, :index
  attr_reader :value

  def initialize(value, index)
    @value = value
    @index = index
    @next = nil
    @prev = nil
  end

  def to_s
    "... #{@prev.value} -> #{@value} -> #{@next.value} ..."
  end
end

class LinkedList
  attr_accessor :first, :last

  def initialize(node = nil)
    @first = node
    @last = node
  end

  def push_end(node)
    if @last.nil?
      @last = node
      @first = node
    else
      node.prev = @last
      @last.next = node
      @last = node
    end
  end

  def push_start(node)
    if @first.nil?
      @last = node
      @first = node
    else
      node.next = @first
      @first.prev = node
      @first = node
    end
  end

  def to_pot_array
    arr = []
    temp = @first
    loop do
      arr << temp.value
      temp = temp.next
      break if temp == @last
    end

    4.times do
      arr.push('.')
      arr.insert(0,'.')
    end
    arr
  end

  def clear(node = nil)
    @first = node
    @last = node
  end

end

arr = File.open('inputs/12').to_a

pots = arr[0].strip.chars

generation = LinkedList.new
pots.each_with_index do |p, i|
  generation.push_end(Node.new(p, i))
end

patterns = {}
for i in 1..arr.length-1
  s = arr[i].split(' ')
  patterns[s[0]] = s[2]
end


#puts generations[0].inspect

ps = 0
20.times do |i|
  pg = generation.to_pot_array
  cs = 0
  zero_index = generation.first.index
  pg.each_with_index do |p, a|
    if p == '#'
      cs += a-zero_index
    end
  end
  puts cs


  generation.clear
  for a in 0..pg.length-4
    current_pots = pg[a..a+4]
    match = false
    patterns.each_key do |k|
      if current_pots == k.chars
        #puts "Pots: #{current_pots.inspect}, Patterns: #{k.chars.inspect}, Result: #{patterns[k]}"
        generation.push_start(Node.new(patterns[k], zero_index+a-2))
        match = true
        break
      end
    end
    generation.push_start(Node.new(pg[a+2], zero_index+a-2)) unless match
  end
  printf("\rPercentage: %d%", (i*100)/50000000000)
end

first_index = generation.first.index

score = 0
puts first_index
puts '-----------------------'
generation.to_pot_array.each_with_index do |p, i|
  if p == '#'
    score += i-first_index
  end
end

puts '--------------------'
puts score

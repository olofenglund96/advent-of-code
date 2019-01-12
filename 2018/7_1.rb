class Node
  attr_accessor :char, :reqs
  attr_reader :time_finished

  def initialize(char, reqs = [], time_finished = 0)
    @char = char
    @reqs = reqs
    @time_finished = time_finished
  end

  def time_finished=(value)
    @time_finished = value + 60 + (@char.ord-'A'.ord+1)
  end

  def add_req(node)
    index = 0
    @reqs.each do |n|
      if node.char < n.char
        break
      end
      index += 1
    end

    @reqs.insert(index, node)
  end

  def pop_node(node)

  end

  def return_string(string)
    printf self.char
    @next_nodes.reverse.each do |n|
      printf " <- #{n.char}\n"
      string << n.return_string(string)
    end
    string << @char
    string
  end
end

class LinkedList
  attr_accessor :nodes
  def initialize(nodes = [])
    @nodes = nodes
  end

  def find_node(char)
    @nodes.find {|n| n.char == char}
  end

  def produce_string
    string = ''
    while @nodes.length > 0
      cnodes = []
      @nodes.each do |n|
        if n.reqs.length == 0
          cnodes << n
        end
      end

      cnode = cnodes.max {|a, b| b.char <=> a.char}

      string << cnode.char

      @nodes.each do |n|
        if n.reqs.include?(cnode)
          n.reqs.delete(cnode)
        end
      end

      @nodes.delete(cnode)
    end
    string
  end

  def simulate_string
    string = ''
    workers = Array.new(5, nil)
    time = 0
    while @nodes.length > 0
      cnodes = []
      @nodes.each do |n|
        if n.reqs.length == 0
          cnodes << n
        end
      end

      cnodes.sort! {|a, b| a.char <=> b.char}

      free = false
      workers.each do |w|
        if w.nil?
          free = true
          break
        end
      end

      if free
        cnodes.each do |cn|
          unless workers.include?(cn)
            for i in 0..4
              if workers[i].nil?
                workers[i] = cn
                cn.time_finished = time
                break
              end
            end
          end
        end
      end

      #puts (workers.map {|n| n.char unless n.nil?}).inspect

      workers.each_with_index do |cnode, i|
        #puts "TF: #{cnode.time_finished}, T: #{time}" unless cnode.nil?
        if !cnode.nil? && cnode.time_finished <= time+1
          @nodes.each do |n|
            if n.reqs.include?(cnode)
              n.reqs.delete(cnode)
            end
          end

          string << cnode.char
          @nodes.delete(cnode)
          workers[i] = nil
          #puts (workers.map {|n| n.char unless n.nil?}).inspect
          #workers.sort! {|a, b| a.char <=> b.char}
        end
      end
      time += 1
      #puts (@nodes.map {|n| n.char}).inspect

      #gets
    end
    time
  end

  def first_node
    chars = @nodes.map {|n| n.char}

    @nodes.each do |n|
      n.next_nodes.each do |pn|
        if chars.include?(pn.char)
          chars.delete(pn.char)
        end
      end
    end
    @nodes.find {|n| n.char == chars[0]}
  end
end

def get_total_letters(instr)
  l1 = instr.map {|l| l['letter']}
  l2 = instr.map {|l| l['req']}
  l = l1 + l2
  l.uniq
end

arr = File.open('inputs/7').to_a
instructions = []

arr.each do |i|
  instr = {}
  str = i.split(' ')
  instr['letter'] = str[7].chars[0]
  instr['req'] = str[1].chars[0]
  instructions.push(instr)
end

nodes = []
letters = get_total_letters(instructions)

letters.each do |l|
  node = Node.new(l)
  nodes.push(node)
end

list = LinkedList.new(nodes)

#puts list.find_node('A').inspect

instructions.each do |i|
  req = list.find_node(i['req'])
  list.find_node(i['letter']).add_req(req)
end

puts '-----------------------'
list.nodes.each do |node|
  puts "#{node.char}: #{(node.reqs.map {|n|n.char}).inspect}"
end
puts '-----------------------'

#puts (list.nodes.map {|l| l.char}).inspect

#puts list.produce_string
puts list.simulate_string
#puts (list.first_node.req.map {|n| n.char}).inspect
#puts (list.first_node.req.first.next_nodes.map {|n| n.char}).inspect

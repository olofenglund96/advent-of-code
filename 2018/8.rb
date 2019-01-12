require 'tree'

def evaluate_node(index)
  nodes = $arr[index].to_i
  #puts "BF - Index: #{index}, Nodes: #{nodes}"
  #gets
  index += 1
  metacount = $arr[index].to_i

  unless nodes == 0
    for i in 0..nodes-1
      index = evaluate_node(index+1)
    end
  end

  index += 1
  #puts "AF - Index: #{index}, Nodes: #{nodes}"
  for m in 0..metacount-1
    $metadata += $arr[index+m].to_i
  end

  index += metacount-1
  #gets
  index
end

def create_tree(index, node)
  nodes = $arr[index].to_i
  puts "BF - Index: #{index}, Nodes: #{nodes}"
  #gets
  next_node = Tree::TreeNode.new("#{index}", [])
  if node.nil?
    node = next_node
  else
    node << next_node
  end

  index += 1
  metacount = $arr[index].to_i

  unless nodes == 0
    for i in 0..nodes-1
      index, r = create_tree(index+1, next_node)
    end
  end

  index += 1

  metas = []
  puts "AF - Index: #{index}, Nodes: #{nodes}"

  for m in 0..metacount-1
    metas << $arr[index+m].to_i
  end

  next_node.content = metas

  index += metacount-1
  #gets
  return index, node
end

def evaluate_tree(node, value)
  nodes = node.content
  #puts "BF - Nodes: #{nodes.inspect}"
  #gets
  unless node.children.length == 0
    children = node.children
    #puts "ALL CHILDREN: #{children.map {|n| n.name}}"
    nodes.each do |n|
      #puts "N-CHILDREN:: #{children[n-1]}" unless children[n-1].nil?
      unless children[n-1].nil?
         evaluate_tree(children[n-1], value)
      end
    end
  else
    #puts "Node: #{node.name}, Value: #{nodes.inject(0){|sum,x| sum + x }}"
    $sum += nodes.inject(0){|sum,x| sum + x }
    return
  end
 # puts "AF - Node: #{node.name}, Val: #{value}"
  #gets
end

line = File.open('inputs/8').to_a[0]

$arr = line.split(" ")
=begin
root_meta = []

($arr.length-1).downto($arr.length-$arr[1].to_i) do |i|
  root_meta << $arr[i].to_i
end

root = Tree::TreeNode.new("#{0}; Children: #{$arr[0]}", root_meta)
=end
#puts $arr.inspect


i, root = create_tree(0, nil)
$sum = 0
$treelist = (root.map {|n| n})

puts ($treelist.map {|n| "Name: #{n.name}, Content: #{n.content}"}).inspect
puts '--------------------------------------'
puts evaluate_tree(root, 0)
puts $sum

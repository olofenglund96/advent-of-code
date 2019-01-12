require 'ostruct'
require 'ruby2d'


arr = File.open('inputs/6').to_a

$removed = 0
def create_edge(x, y)
  ne = {}
  ne['x'] = x
  ne['y'] = y
  ne
end

def remove_edge(c_current, temp_grid, cell, x, y)
  coord = $coords.find {|c| c.index == cell['index']}

  if c_current.index != coord.index
    deleted = coord.edges.delete_if {|e| e['x'] == x && e['y'] == y}
    if deleted.nil?
      puts "Couldn't delete edge"
    else
      $removed += 1
      coord.area -= 1
    end
  end

  return temp_grid
end

def resolve_gridpoint(c, temp_grid, new_edges, x, y)
  advanced = false
  if x >= 0 && x < temp_grid.length && y >= 0 && y < temp_grid[0].length
    if temp_grid[x][y].nil?
      cell = {}
      cell['index'] = c.index
      cell['taken'] = false
      temp_grid[x][y] = cell
      new_edges.push(create_edge(x, y))
      c.area += 1
      advanced = true
    elsif !temp_grid[x][y]['taken']
      temp_grid = remove_edge(c, temp_grid, temp_grid[x][y], x, y)
      advanced = true
    end
  else
    c.area = -1000
  end
  return c, temp_grid, new_edges, advanced
end

def progress_grid
  advanced = false
  temp_grid = $grid

  $coords.each_with_index do |c, index|
    new_edges = []
    c.edges.each_with_index do |e, i|

      c, temp_grid, new_edges, advanced = resolve_gridpoint(c, temp_grid, new_edges, e['x']-1, e['y'])
      c, temp_grid, new_edges, advanced = resolve_gridpoint(c, temp_grid, new_edges, e['x']+1, e['y'])
      c, temp_grid, new_edges, advanced = resolve_gridpoint(c, temp_grid, new_edges, e['x'], e['y']-1)
      c, temp_grid, new_edges, advanced = resolve_gridpoint(c, temp_grid, new_edges, e['x'], e['y']+1)
=begin
      if advanced
        puts e['y']
        new_edges.delete_at(i)
      end
=end
    end

    if advanced
      c.edges = new_edges
    end

    break if index == 100
  end
  for a in 0..temp_grid.length-1
    for b in 0..temp_grid[0].length-1
      if !temp_grid[a][b].nil? && !temp_grid[a][b]['taken']
        temp_grid[a][b]['taken'] = true
      end
    end
  end


  $grid = temp_grid
  return advanced
end

$coords = []
max_x = 0
max_y = 0

arr.each do |a|
  os = OpenStruct.new
  $coords_temp = a.delete!(' ').split(",")
  os.x = $coords_temp[0].to_i
  os.y = $coords_temp[1].to_i
  os.area = 0
  os.edges = []

  if os.x > max_x
    max_x = os.x
  end

  if os.y > max_y
    max_y = os.y
  end
  $coords.push(os)
end

puts max_x, max_y

$grid = Array.new(max_x) { Array.new(max_y) }

$coords.each_with_index do |c, i|
  cell = {}
  cell['taken'] = true
  cell['index'] = i
  $grid[c.x][c.y] = cell
  edge = {}
  edge['y'] = c.y
  edge['x'] = c.x
  c.edges.push(edge)
  c.area += 1
  c.index = i
end

#puts(($grid.flatten.reject{|g| g.nil?}).sort.inspect)


# Set the window size
set width: $grid.length*4, height: $grid[0].length*4

# Create a new shape

def paint_progress
  $coords.each do |c|
    color = Color.new('random')
    c.edges.each do |e|
      Square.new(
        x: e['x']*4, y: e['y']*4,
        size: 4,
        color: [color.r, color.g, color.b, color.a]
      )
    end
  end
  puts 'Progress?'
  gets
end

loop do
  adv = progress_grid
  if !adv
    break
  end
  #paint_progress
end

=begin
incr = 0
loop do
  adv = progress_grid
  if !adv || incr == 0
    break
  end
  incr += 1
end
=end


$coords.each do |c|
  color = Color.new('random')
  puts c.edges.length
  c.edges.each do |e|
    Square.new(
      x: e['x']*4, y: e['y']*4,
      size: 4,
      color: [color.r, color.g, color.b, color.a]
    )
  end
end

=begin
for a in 0..$grid.length-1
  printf("\rPercentage: %d%", 100*a/($grid.length-1))
  for b in 0..$grid[0].length-1
    if $grid[a][b]['index'] == -1
      Square.new(
        x: a*4, y: b*4,
        size: 4,
        color: 'white'
      )
    end
  end
end
=end
# Show the window
puts 'Calc done'
puts "Removed: #{$removed}"
max_a = $coords.max {|a,b| a.area <=> b.area}

puts max_a.inspect

show

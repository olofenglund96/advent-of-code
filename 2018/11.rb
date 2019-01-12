def sum_area(x, y, s)
  sum = 0
  for a in x..x+s-1
    for b in y..y+s-1
      sum += $grid[a][b]
    end
  end
  sum
end

def sum_edge(x, y, s)
  #puts '---------------------------'
  #puts "Edge: #{x}, #{y}, #{s}"
  sum = 0
  a = x
  loop do
    #puts "X: x: #{a}, y: #{y+s-1}"
    #puts "Grid: #{$grid[a][y+s-1]}"
    #gets
    sum += $grid[a][y+s-1]
    break if a >= x+s-1
    a += 1
  end

  for b in y..y+s-2
    #puts "Y: x: #{a}, y: #{b}"
    #puts "Grid: #{$grid[a][b]}"
    #gets
    sum += $grid[a][b]
  end

  #puts "Sum: #{sum}"
  sum
end


serial = 7511

$grid = Array.new(300) { Array.new(300, 0) }

for x in 0..$grid.length-1
  for y in 0..$grid[0].length-1
    rack = x + 10 + 1
    #puts (((y+1)*rack + serial)*rack)
    val = ((((y+1)*rack + serial)*rack) % 1000)/100
    #puts val
    val = val.floor-5
    #puts val
    #gets
    $grid[x][y] = val
  end
end

puts sum_area(89, 268, 16)
puts sum_area(38, 71, 203)
puts sum_area(235, 287, 12)
puts sum_area(234, 287, 12)

#sum_grid = Array.new(300) { Array.new(300) {Array.new(300)}}
total_calcs = $grid.length
sum = 0
max_index = [0, 0, 0]
max_val = 0


for x in 0..$grid.length
  for y in 0..$grid[0].length
    max = x > y ? x : y
    sum = 0
    for s in 1..$grid.length-max
       sum += sum_edge(x, y, s)
       if sum > max_val
        max_val = sum
        max_index = [x+1, y+1, s]
      end
      if x + s >= 300 && y + s >= 300
        puts "Edge: #{x}, #{y}, #{s}"
      end
    end
  end
  #puts (x*100)/total_calcs
  printf("\rSum Percentage: %d%", (x*100)/total_calcs)
end

=begin
max_index = [0, 0, 0]
max_val = 0
total_calcs = sum_grid.length
for s in 0..sum_grid.length-1
  for x in 0..sum_grid.length-1
    for y in 0..sum_grid[0].length-1
      if sum_grid[x][y] > max_val
        max_val = sum_grid[x][y][s]
        max_index = [x, y, s]
      end
    end
  end
  printf("\rMax Percentage: %d%", (s/total_calcs)*100)
end
=end
puts "\n -----------------------"
puts max_val
puts max_index.inspect

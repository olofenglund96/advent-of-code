arr = File.open('inputs/6').to_a
$coords = []
max_y = 0
max_x = 0
arr.each do |a|
  os = {}
  coords_temp = a.delete!(' ').split(",")
  os['x'] = coords_temp[0].to_i
  os['y'] = coords_temp[1].to_i

  if os['x'] > max_x
    max_x = os['x']
  end

  if os['y'] > max_y
    max_y = os['y']
  end
  $coords.push(os)
end

points = 0
for a in 0..max_x-1
  for b in 0..max_y-1
    sum = 0
    $coords.each do |c|
      sum += (a-c['x']).abs + (b-c['y']).abs
    end
    if sum < 10000
      points += 1
    end
  end
end

puts points

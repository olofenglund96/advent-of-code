def parse_line(line)
  info = line.split(' ')
  ni = []
  ni.push(info[0][/\d+/])
  ni.push(info[2].split(',')[/\d+/])
  puts ni.inspect
  ni.push(info[3].split('x')[0], info[3].split('x')[1])
  ni
end

arr = File.open('inputs/3').to_a
grid_max = 0
grid = []
arr.each do |line|
  info = parse_line(line)
end

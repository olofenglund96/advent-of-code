require 'ostruct'

def parse_line(line)
  info = line.split(' ')
  ni = OpenStruct.new
  ni.id = info[0][/\d+/].to_i
  dims = info[2].split(',')
  ni.cx = dims[0].to_i-1
  ni.cy = dims[1].tr(':', '').to_i-1
  dims = info[3].split('x')
  ni.dx = dims[0].to_i-1
  ni.dy = dims[1].to_i-1
  ni
end

arr = File.open('inputs/3').to_a
grid = Array.new(1000) { Array.new(1000) }
info = []


arr.each do |line|
  info.push(parse_line(line))
end

entry_ids = Array.new(info.last.id, 0)

info.each do |entry|
  for a in entry.cx..(entry.cx + entry.dx)
    for b in entry.cy..(entry.cy + entry.dy)
     if !grid[a][b].nil?
      entry_ids[entry.id] = 1
      entry_ids[grid[a][b]] = 1
     else
      grid[a][b] = entry.id
     end
    end
  end
end

for a in 0..entry_ids.length
  if entry_ids[a] == 0
    puts a
  end
end

require 'ostruct'

def parse_line(line)
  info = line.split(' ')
  ni = OpenStruct.new
  ni.date = info[0].tr('[', '') + ' ' + info[1].tr(']', '')
  ni.id = nil
  ni.event = case info[2]
  when 'falls'
    'f'
  when 'wakes'
    'w'
  when 'Guard'
    ni.id = info[3].tr('#', '').to_i
    'g'
  else
    nil
  end
  ni
end

arr = File.open('inputs/4').to_a
info = []

arr.each do |line|
  info.push(parse_line(line))
end

info.sort! { |a, b| a.date <=> b.date }

puts info

guard_ids = (((info.uniq { |i| i.id }).collect(&:id).reject {|i| i.nil? }).map {|i| i.to_i})

puts guard_ids
guards = []

guard_ids.each do |g|
  go = OpenStruct.new
  go.id = g
  go.th = 0
  go.h = Array.new(60, 0)
  guards.push(go)
end

guard = ''
slp_time = 0
info.each do |i|
  time = i.date.split(' ').last.split(':').last.to_i
  if i.event == 'g'
    guard = guards.find {|g| g.id == i.id}
  elsif i.event == 'f'
    slp_time = time
  else
    for t in slp_time..time-1
      guard.h[t.to_i] += 1
      guard.th += 1
    end
  end
end

max_g = guards.max {|a,b| a.h.max <=> b.h.max }
puts max_g
max_h = max_g.h.each_with_index.max[1]
puts max_h

puts max_h*max_g.id

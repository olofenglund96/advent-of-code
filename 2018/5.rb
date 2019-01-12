def eval_string(line, deleted)
  for i in 0..line.length-2
    if line[i].nil? || line[i] == line[i+1]
    elsif line[i] == line[i+1].upcase || line[i].upcase == line[i+1]
      line[i] = nil
      line[i+1] = nil
      deleted = true
    end
  end

  if deleted
    line.reject! {|l| l.nil?}
    len = eval_string(line, false)
  else
    puts line.length
    return line.length
  end
  len
end

line = File.open('inputs/5').first.chars

line.reject! {|l| l == "\n"}
puts line.last.inspect
puts line.length
lowest_len = 1000000
for letter in 'a'..'z'
  new_line = line.reject {|l| l == letter || l == letter.upcase}
  len = eval_string(new_line, false)
  if len < lowest_len
    lowest_len = len
  end
end

puts lowest_len

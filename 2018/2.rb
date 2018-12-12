arr = File.open('inputs/2').to_a
line_len = arr[0].length
index = 0
arr.each_with_index do |line, a|
  word = line.scan(/\w/)
  for b in a..arr.length-1 do
    diffs = 0
    comp = arr[b].scan(/\w/)
    for c in 0..line_len do
      if word[c] != comp[c]
        diffs += 1
        index = c
      end
    end
    if diffs == 1
      res = comp.delete_at(index)
      puts comp.join('').to_s
      return
    end
  end
end

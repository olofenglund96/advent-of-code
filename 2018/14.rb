#580741

nums = 580741.to_s.chars.map(&:to_i)
recipes = [3, 7]
len = 2
fi = 0
si = 1
next_match = 0

while true
  nr = recipes[fi] + recipes[si]
  nr = nr.to_s.chars
  len += nr.length

  nr.each do |c|
    recipes << c.to_i
  end

  fi = (fi + recipes[fi] + 1) % len
  si = (si + recipes[si] + 1) % len
  #puts recipes.inspect
  #gets
=begin
  if len >= 10
    if recipes[len-7..len-1] == nums
      puts len-10
      break
    end
  end
=end

  nr.length.times do |n|

    if recipes[len-1-(nr.length-(n-1))..len-1] == nums[next_match..next_match+n-1]
      next_match += 1

      if next_match == 6
        puts len-6
        puts recipes[len-10..len].inspects
        return
      end
    else
      if recipes[len-1-nr.length] == 5
        next_match = 1
      else
        next_match = 0
      end
    end
  end
end

#sum = recipes[580741..580741 + 10].join('')

#puts sum

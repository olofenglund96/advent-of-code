require 'ruby2d'
#require 'gosu'
arr = File.open('inputs/10').to_a
$tick = 0
=begin
class StarMap < Gosu::Window
  def initialize(height, width)
    super height, width
    self.caption = 'Star map'
  end

  def update

  end

  def draw
    if $tick % 60 == 0
      update_positions
    end
    $tick += 1
    show_positions
  end
end
=end

$data = []
arr.each do |a|
  dat = {}
  pos_1 = a.index("<")+1
  pos_2 = a.index(">", pos_1)-1
  vel_1 = a.index("<", pos_2)+1
  vel_2 = a.index(">", vel_1)-1
  pos_parsed = a[pos_1..pos_2].split(",")

  dat['posx'] = pos_parsed[0].to_i
  dat['posy'] = pos_parsed[1].to_i

  vel_parsed = a[vel_1..vel_2].split(",")
  dat['velx'] = vel_parsed[0].to_i
  dat['vely'] = vel_parsed[1].to_i

  $data << dat
end

def update_positions
  if get_area > 100000
    loop do
      $data.map do |d|
        d['posx'] += d['velx']
        d['posy'] += d['vely']
      end
      $itr += 1
      break if get_area < 100000
    end
  end

  $data.map do |d|
    d['posx'] += d['velx']
    d['posy'] += d['vely']
  end
  $itr += 1
  #puts $data
 # puts '----------------------'
end

def show_positions
  clear
  $data.each_with_index do |d, i|
    #printf("\rPercentage: %d%", (i/$data.length)*100)
    #Gosu.draw_rect(d['posx']*$scaling,d['posy']*$scaling,$scaling, $scaling, Gosu::Color.new(255, 255, 255, 255))
    Square.new(
      x: d['posx']*$scaling, y: d['posy']*$scaling,
      size: $scaling,
      color: 'white'
    )
  end
end

def get_area
  max_x = ($data.max {|a,b| a['posx'] <=> b['posx']})['posx']
  min_x = ($data.min {|a,b| a['posx'] <=> b['posx']})['posx']
  max_y = ($data.max {|a,b| a['posy'] <=> b['posx']})['posy']
  min_y = ($data.min {|a,b| a['posy'] <=> b['posx']})['posy']
  ((max_x-min_x).abs) * ((max_y-min_y).abs)
end

$scaling = 4
$itr = 0
set width: 2000, height: 1500

#puts $data
past = false
update do
  area = get_area
  puts "Area: #{area}" if $tick % 60 == 0

  if area > 2000
    update_positions
  elsif $tick % 60 == 0

    unless get_area == 244
      update_positions
    end
    show_positions
    puts "ITR: #{$itr}"
  end
  $tick += 1
end

show

#StarMap.new(height*$scaling, width*$scaling).show

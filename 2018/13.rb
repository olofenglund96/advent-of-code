require 'colorize'
PI = Math::PI

class Track
  attr_accessor :pieces, :carts, :yh, :xh

  def initialize(yh, xh)
    @pieces = []
    @carts = []
    @yh = yh
    @xh = xh
  end

  def simulate
    loop do
      self.print_track
      collision = self.step
      gets
      #sleep(1)
      break if collision
    end
  end

  def step
    @carts.sort_by! {|c| [-c.y, c.x]}
    #puts (@carts.map {|c| c.id}).inspect
    #gets
    final = false
    @carts.each do |c|
      self.compute_next_pos(c)
    end

    @carts.delete_if {|c| c.collided}
    final = @carts.length == 1
=begin
    @carts.each do |c|
      collision = self.check_collison(c.x, c.y)
      if collision
        if @carts.length == 3
          #print_track
          #gets
        end
        puts "Collision at: #{c.x}, #{@yh-c.y}"
        @carts.delete_if {|ct| ct.x == c.x && ct.y == c.y}
        final = @carts.length == 1
      end
    end
=end

    if final
      #print_track
      puts @carts.inspect
      puts "Last at: #{@carts.first.x}, #{@yh-@carts.first.y}, Direction: #{@carts.first.direction_str}, Id: #{@carts.first.id}"
      return true
    end
    false
  end

  def compute_next_pos(c)
    rotation = rotation_at(c.x, c.y)
    if rotation.nil?
      puts "ERROR: Can't find piece at #{c.x}, #{c.y}"
      return true
    end
    #puts "BF: Cart: #{c.id}, Current position: #{c.x}, #{c.y}, Direction: #{c.direction_str}, Rotation: #{rotation}"
    x, y = c.move(rotation)
    #puts "AF: Cart: #{c.id}, Current position: #{c.x}, #{c.y}, Direction: #{c.direction_str}"
    #puts '-----------------------------------------------------------------------------'

    collision = self.check_collison(x, y)
    if collision
      if @carts.length == 3
        #print_track
        #gets
      end
      @carts.each do |ct|
         if ct.x == x && ct.y == y
          ct.collided = true
         end
      end
      puts "Collision at: #{x}, #{@yh-y}"
      return true
    end

    false
  end

  def rotation_at(x, y)
    pieces.each do |p|
      return p.rotation if p.x == x && p.y == y
    end
    return nil
  end

  def add_cart(x, y, direction)
    @carts << Cart.new(x, y, direction)
  end

  def remove_carts_at(x, y)

  end

  def add_piece(x, y, rotation, symbol)
    @pieces << Piece.new(x, y, rotation, symbol)
  end

  def decide_turn_direction(x, y, symbol)
    if symbol == '/'
        return 1
    elsif symbol == '\\'
        return -1
    else
      puts "Unrecognized symbol: \"#{symbol}\""
    end
  end

  def cart_at?(x, y)
    @carts.each do |c|
      if c.x == x && c.y == y
        return true
      end
    end
    false
  end

  def check_collison(x, y)
    (@carts.find_all {|c| c.x == x && c.y == y}).length > 1
  end

  def print_track
    for yn in 0..@yh
      y = @yh-yn
      for x in 0..@xh
        cart = @carts.find {|c| c.x == x && c.y == y}
        unless cart.nil?
          print(cart.direction_symbol.red)
        else
          piece = @pieces.find {|c| c.x == x && c.y == y}
          unless piece.nil?
            print(piece.symbol)
          else
            print(' ')
          end
        end
      end
      print("\n")
    end

  end

end

class Piece
  attr_accessor :x, :y, :rotation, :symbol

  def initialize(x, y, rotation = 0, symbol)
    @x = x
    @y = y
    @rotation = rotation
    @symbol = symbol
  end

end

class Cart
  attr_accessor :id, :x, :y, :direction, :turn, :collided

  def initialize(x, y, direction, turn = PI/2, collided = false)
    @id = "#{x}, #{y}"
    @x = x
    @y = y
    @direction = direction
    @turn = turn
    @collided = collided
  end

  def move(rotation)
    current_turn = @direction

    if rotation == 2
      current_turn += @turn
      @turn -= PI/2
      @turn = PI/2 if @turn < -PI/2
    elsif rotation != 0
      if Math.cos(@direction).round == 0
        current_turn -= rotation*PI/2
      else
        current_turn += rotation*PI/2
      end
=begin
      puts rotation.inspect
      cos_rot = rotation.map {|r| Math.cos(r).abs.round}
      puts cos_rot.inspect
      cos_rot.delete(Math.cos(@direction).abs)
      puts cos_rot.inspect
      current_turn = Math.acos(cos_rot[0].to_i)
      puts current_turn
=end
    end

    #puts "CT", current_turn
    #puts "DIR", @direction
    @direction = current_turn
    #puts Math.cos(@direction)
    @x += Math.cos(@direction).to_i
    @y += Math.sin(@direction).to_i
    @direction = ((@direction/PI).round(2) % 2)*PI
   # puts @x, y
    return @x, @y
  end

  def direction_str
    "#{(@direction%(2*PI))/PI}pi"
  end

  def direction_symbol
    dir = ((@direction/PI).round(2)*PI % (2*PI))/PI
    if dir == 0.0
      '>'
    elsif dir == 0.5
      '^'
    elsif dir == 1.0
      '<'
    else
      'v'
    end
  end
end

arr = File.open('inputs/13_e').to_a
max_line = arr.max {|a, b| a.length <=> b.length}
track = Track.new(arr.length-1, max_line.length-1)
cart_symbols = ['>', '^', '<', 'v' ]
straight_piece_symbols = ['-', '|']
turn_piece_symbols = ['/', '\\']
max = arr.length-1
arr.each_with_index do |a, y|
  y = max-y
  a.chars.each_with_index do |c, x|
    #puts "{ x: #{x}, y: #{y} }, Symbol: #{c}"
    if cart_symbols.include?(c)

      track.add_cart(x, y, cart_symbols.index(c)*(PI/2))
      track.add_piece(x, y, 0, straight_piece_symbols[cart_symbols.index(c) % 2])
    else
      if straight_piece_symbols.include?(c)
        track.add_piece(x, y, 0, c)
      else
        if c == '+'
          track.add_piece(x, y, 2, c)
        elsif turn_piece_symbols.include?(c)
          rotation = track.decide_turn_direction(x, y, c)
          track.add_piece(x, y, rotation, c)
        end
      end
    end
  end
end

track.simulate

#puts (track.pieces.map {|p| p.rotation}).inspect

#66,35

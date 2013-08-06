# Find PI to the Nth Digit

puts "Enter the number of decimal places you would like: "
decimals = gets.chomp

puts Math::PI.round(decimals.to_i)

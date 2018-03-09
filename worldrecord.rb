a=6-4*Math.sqrt(2)
y=Math.sqrt(2)-1

(0..9).each do |n|
    y = (1-(1-y*y*y*y)**0.25)/(1+(1-y*y*y*y)**0.25)
    a = (1+y)**4*a-2**(2*n+3)*y*(1+y+y*y)
end

puts 1/a

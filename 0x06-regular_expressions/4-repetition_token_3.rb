#!/usr/bin/env ruby
# Matches test strings hbn, hbtn, hbttn, hbtttn and so on
# Ignores hbon

puts ARGV[0].scan(/hbt*n/).join

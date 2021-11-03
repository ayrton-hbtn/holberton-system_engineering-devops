#!/usr/bin/env ruby
# Matches test strings hbtn, hbttn, hbtttn and so on

puts ARGV[0].scan(/hbt+n/).join

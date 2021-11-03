#!/usr/bin/env ruby
# Matches test strings that starts with h and ends with n
# Must have any single character in between (just one character)

puts ARGV[0].scan(/h.{1}n/).join

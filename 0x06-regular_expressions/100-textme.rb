#!/usr/bin/env ruby
# Run some statistics on the TextMe app text messages transactions
# Output: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]\s/).join(",")

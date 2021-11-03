#!/usr/bin/env ruby
# Accepts one argument and pass it to a regular expression matching method
# Must match "School"

puts ARGV[0].scan(/School/).join

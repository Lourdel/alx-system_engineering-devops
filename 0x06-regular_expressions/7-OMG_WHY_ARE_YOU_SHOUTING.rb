#!/usr/bin/env ruby
#ruby script with regular expression that must match capital letters
puts ARGV[0].scan(/[[:upper:]]/).join

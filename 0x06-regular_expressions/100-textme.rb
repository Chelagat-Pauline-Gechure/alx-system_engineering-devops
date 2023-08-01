#!/usr/bin/env ruby

# Accept the argument from the command line
input = ARGV[0]
regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
matched = input.scan(regex)
formatted = matched.map { |match| match.join(",") }
puts formatted.join("\n")

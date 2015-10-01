require 'popen4'
require 'optparse'
require 'parallel'
require_relative 'ar_fork'

require_relative 'log_pre_processor'

ARGUMENT_COUNT = 2

options = {
    verbose: false
}
OptionParser.new do |opts|
  opts.banner = 'Usage: arunner.rb [options] target assignment'

  options[:verbose] = false
  opts.on('-v', '--[no-]verbose', 'Run verbosely') do |v|
    options[:verbose] = v
  end

  opts.on('-i', '--input FILE', 'Override input file') do |f|
    options[:fileoverride] = f
  end

  opts.on('-p', '--python FILE', 'Override python executable') do |f|
    options[:python] = f
  end

  options
end.parse!

if ARGV.length < ARGUMENT_COUNT
  puts 'Not enough arguments'
  exit(1)
end

def parse_targets(str)
  unless Dir.exist? str
    puts 'Target does not exist or is not a directory!'
    exit(2)
  end
  Dir[File.join(str, '**/*.py')]
end

def parse_assignment(str)
  split = str.split('/')
  ass = (split[1] || 1).to_i
  {assignment: split[0], number: ass}
end

assignment = parse_assignment ARGV[1]
targets = parse_targets(ARGV[0]).map {|f| ARFork.new(options, f)}

p targets
p assignment

string = %w{(Call:Wait:100:othello#wait) (Call:Wait:200:othello#wait) (Error:Index:15:barchart#set_bar_name)}.join("\n")
LogPreProcessor.process_string(string)


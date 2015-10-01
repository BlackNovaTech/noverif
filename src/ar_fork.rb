require_relative 'log_pre_processor'

class ARFork
  def initialize(options, file)
    @options = options
    @file = file
  end

  def run
    python = @options[:python]
    assignment_path = @optiongs[:assignment_path]
    input = @options[:assignment][:input]
    ipy_mock = @options[:ipy_mock]

    stdin = File.read(File.join(assignment_path, 'stdin.txt'))
    stdout = '', stdin = ''
  end
end
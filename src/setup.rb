class SetupParser

  def initialize(file_name)
    @options_hash = {}
    #we only require the file name, we expect it to be at the top of the dir
    @file_name = file_name
  end


  def self.parse_setup_file(file_name)
    if File.exist?(file_name) and File.file?(file_name)
      file_string = File.read(file_name)
      file_string
    else
      raise new Error "could not open file: #{file_name} does not exist!"
    end
  end

  def self.parse_opt(line)
    split_line = line.split('=')
    opt = split_line[0]
    opt = opt.to_sym
    value = split_line[1]
    @options_hash.merge!(opt: value)
  end
end

class LogPreProcessor
  def self.process_string(string)
    string.split("\n").each { |v| process_line v }
  end

  private
    LINE_KEYS = %i{level type value method}
    def self.process_line(string)
      Hash[LINE_KEYS.zip(string[1...-1].split(':'))]
    end
end

#(level:type:value:method)
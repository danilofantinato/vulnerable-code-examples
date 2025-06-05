require 'net/http'
require 'uri'

def secure_function(url)
  begin
    uri = URI.parse(url)
    raise ArgumentError, "Invalid URL" unless uri.kind_of?(URI::HTTP) || uri.kind_of?(URI::HTTPS)

    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = true if uri.scheme == 'https'
    response = http.get(uri.request_uri)
    puts "Response: #{response.body}"
  rescue ArgumentError, URI::InvalidURIError => e
    puts "Error: #{e.message}"
  end
end

print "Enter a URL: "
user_input = gets.chomp
secure_function(user_input)
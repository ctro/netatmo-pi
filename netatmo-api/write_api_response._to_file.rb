require_relative "netatmo_info.rb"
require "json"

ninfo = NetatmoInfo.new

data = { inside: ninfo.inside_data, outside: ninfo.outside_data }

File.open("../netatmo-data.json", "w") do |f|
  f << "#{data.to_json}\n"
end

require "net/http"
require "json"
require "dotenv/load"

class NetatmoInfo
  attr_accessor :data

  def initialize
    # Trigger API requests
    @data = get_station_data
  end

  def inside_string
    id = @data["body"]["devices"].first["dashboard_data"]

    "In :#{c_to_f(id["Temperature"])}° #{arrow(id["temp_trend"])} " \
    "#{id["Humidity"]}% " \
    "#{id["AbsolutePressure"]}mm #{arrow(id["pressure_trend"])} " \
    "#{id["CO2"]}ppm #{id["Noise"]}db"
  end

  def outside_string
    # We only have one module, the outdoor module
    od = @data["body"]["devices"].first["modules"].first["dashboard_data"]

    "Out: #{c_to_f(od["Temperature"])}°#{arrow(od["temp_trend"])} " \
    "[#{c_to_f(od["min_temp"])}° / #{c_to_f(od["max_temp"])}°] " \
    "#{od["Humidity"]}%"
  end

  def authentication_payload
    return { 'grant_type': "password",
             'username': "#{ENV["EMAIL"]}",
             'password': "#{ENV["PASSWORD"]}",
             'client_id': "#{ENV["CLIENT_ID"]}",
             'client_secret': "#{ENV["CLIENT_SECRET"]}",
             'scope': "read_station" }
  end

  def get_access_token
    begin
      uri = URI("https://api.netatmo.com/oauth2/token")
      res = Net::HTTP.post_form(uri, authentication_payload)
    rescue => exception
      puts exception
    end

    jbody = JSON.parse(res.body)
    return jbody["access_token"]
  end

  def get_station_data
    begin
      uri = URI("https://api.netatmo.com/api/getstationsdata")
      res = Net::HTTP.post_form(
        uri,
        "access_token" => get_access_token(),
        "device_id" => ENV["DEVICE_ID"],
      )
    rescue => exception
      puts exception
    end

    return JSON.parse(res.body)
  end

  def arrow(direction)
    case direction
    when "stable"
      "="
    when "up"
      "+"
    when "down"
      "-"
    else
      "WUT"
    end
  end

  def c_to_f(c)
    return ((c * 9 / 5) + 32).to_f.round(1)
  end
end

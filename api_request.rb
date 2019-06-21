require "net/http"
require "json"
require "dotenv/load"

begin

  # Get an access token
  payload = {
    'grant_type': "password",
    'username': "#{ENV["EMAIL"]}",
    'password': "#{ENV["PASSWORD"]}",
    'client_id': "#{ENV["CLIENT_ID"]}",
    'client_secret': "#{ENV["CLIENT_SECRET"]}",
    'scope': "read_station",
  }
  uri = URI("https://api.netatmo.com/oauth2/token")
  res = Net::HTTP.post_form(uri, payload)

  jbody = JSON.parse(res.body)
  access_token = jbody["access_token"]

  uri = URI("https://api.netatmo.com/api/getstationsdata")
  res = Net::HTTP.post_form(
    uri,
    "access_token" => access_token,
    "device_id" => ENV["DEVICE_ID"],
  )
  puts res.body
rescue => exception
  puts exception
end

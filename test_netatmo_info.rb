require "dotenv/load"
require "minitest"
require "minitest/autorun"
require_relative "../netatmo_info.rb"

class NetatmoApiTest < Minitest::Test
  def setup
    @n = NetatmoInfo.new()
  end

  def test_auth_payload
    assert @n.authentication_payload[:username] == "clint@ctro.net"
    assert @n.authentication_payload.is_a?(Hash)
  end

  def test_get_access_token
    assert @n.get_access_token.is_a?(String)
  end

  def test_get_station_data
    @data = @n.get_station_data
    assert @data.is_a?(Hash)
    assert @n.inside.is_a?(NetatmoInfo::Inside)
    assert @n.outside.is_a?(NetatmoInfo::Outside)
  end
end

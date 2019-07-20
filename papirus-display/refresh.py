import json

from papirus import PapirusText
text = PapirusText(0)

# Write text to the screen specifying all options
#text.write(text, [size = <size> ],[fontPath = <fontpath>],[maxLines = <n>])
#text.write("hello world", 17)

# Positional API
from papirus import PapirusTextPos

#relevant_icons = u"\u2302 \u2601 \u2602 \u2600 \u263C \u2B02 \u2198 \u2109 \u00B0 \u2192 \u2197 \u007C \u238B \u231A \u2603" 
largefont=30
smallfont=13
house_icon = u"\u2302" 
sun_icon = u"\u263C"
degree_icon = u"\u00B0"

def c_to_f(c):
    return float(((c * 9 / 5) + 32))

def arrow(direction):
    if (direction == "stable"):
        return u"\u2192"
    elif (direction == "up"):
        return u"\u2197"
    elif (direction == "down"):
        return u"\u2198"
    else:
        return "WUT"

# Get the data
temp_in = ""
temp_in_trend = ""
temp_out = ""
temp_out_trend = ""
pressure = ""
pressure_trend = ""
co2 = ""
noise = ""
max_temp = ""
min_temp = ""
humid_in = ""
humid_out = ""

with open('../netatmo-data.json') as json_file:
    data = json.load(json_file)
    inside = data['inside']
    outside = data['outside']

    temp_in = str(c_to_f(inside['Temperature']))
    temp_in_trend = inside['temp_trend']
    temp_out = str(c_to_f(outside['Temperature']))
    temp_out_trend = outside['temp_trend']
    pressure = str(inside['AbsolutePressure'])
    pressure_trend = inside['pressure_trend']
    co2 = str(inside['CO2'])
    noise = str(inside['Noise'])
    max_temp = str(c_to_f(outside['max_temp']))
    min_temp = str(c_to_f(outside['min_temp']))
    humid_in = str(inside['Humidity'])
    humid_out = str(outside['Humidity'])

# Put together strings
inside = house_icon + temp_in + degree_icon + arrow(temp_in_trend)
outside = sun_icon + temp_out + degree_icon + arrow(temp_out_trend)
meter = pressure + "mm" + arrow(pressure_trend)

inside_more = co2 + " ppm" + "\n" + noise + " db"
outside_more = min_temp + degree_icon + "lo" + "\n" + max_temp + degree_icon
meter_more = humid_in + "% in" + "\n" + humid_out + "% out"

# Write to the screen
text = PapirusTextPos(0)
text.AddText(inside, 0, 0, largefont, Id="inside")
text.AddText(outside, 0, 33, largefont, Id="outside")
text.AddText(meter, 0, 66, largefont, Id="meter")

text.AddText(inside_more, 135, 0, smallfont, Id="inside_more")
text.AddText(outside_more, 135, 33, smallfont, Id="outside_more")
text.AddText(meter_more, 135, 66, smallfont, Id="meter_more")

 
text.WriteAll()

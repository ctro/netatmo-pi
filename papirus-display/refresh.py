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
meter_icon = u"\u238B" 
degree_icon = u"\u00B0"

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


# Put together strings
inside = house_icon + "70.2" + degree_icon + arrow("up")
outside = sun_icon + "76.7" + degree_icon + arrow("down")
meter = meter_icon + "600" + "mm" + arrow("stable")

inside_more = "1000" + " ppm" + "\n" + "100" + " db"
outside_more = "52.0" + degree_icon + "lo" + "\n" + "77.7" + degree_icon + "hi"
meter_more = "33" + "% in" + "\n" + "44" + "% out"

# Write to the screen
text = PapirusTextPos(0)
text.AddText(inside, 0, 0, largefont, Id="inside")
text.AddText(outside, 0, 33, largefont, Id="outside")
text.AddText(meter, 0, 66, largefont, Id="meter")

text.AddText(inside_more, 135, 0, smallfont, Id="inside_more")
text.AddText(outside_more, 135, 33, smallfont, Id="outside_more")
text.AddText(meter_more, 135, 66, smallfont, Id="meter_more")

 
text.WriteAll()

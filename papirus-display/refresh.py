from papirus import PapirusText

text = PapirusText(0)

# Write text to the screen specifying all options
#text.write(text, [size = <size> ],[fontPath = <fontpath>],[maxLines = <n>])
#text.write("hello world", 17)

# text.write(u"\u2302 \u2601 \u2602 \u2600 \u263C \u2B02 \u2198 \u2109 \u00B0 \u2192 \u2197 \u007C \u238B \u231A \u2603" + "hi", 23)

# Positional API
from papirus import PapirusTextPos

# Get the data

# Write to the screen
text = PapirusTextPos(0)
text.AddText("In", 0, 0, Id="inside")
text.AddText("Out", 10, 10, Id="outside")
text.AddText("Meter", 20, 20, Id="meter")

text.WriteAll()

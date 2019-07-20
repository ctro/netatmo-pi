from papirus import PapirusText

text = PapirusText(0)

# Write text to the screen specifying all options
#text.write(text, [size = <size> ],[fontPath = <fontpath>],[maxLines = <n>])
#text.write("hello world", 17)

# text.write(u"\u2302 \u2601 \u2602 \u2600 \u263C \u2B02 \u2198 \u2109 \u00B0 \u2192 \u2197 \u007C \u238B \u231A \u2603" + "hi", 23)

# NEW!
from papirus import PapirusTextPos



# Same as calling "PapirusTextPos(True [,rotation = rot])"

text = PapirusTextPos(0)



# Write text to the screen at selected point, with an Id

# "hello world" will appear on the screen at (10, 10), font size 20, straight away

text.AddText("hello world", 10, 10, Id="Start" )



# Add another line of text, at the default location

# "Another line" will appear on screen at (0, 0), font size 20, straight away

text.AddText("Another line", 0, 0, 55, Id="Top")



# Update the first line

# "hello world" will disappear and "New Text" will be displayed straight away

text.UpdateText("Start", "New Text")

text.AddText("hello world", 10, 10, Id="Start2", invert=True)

text.WriteAll()

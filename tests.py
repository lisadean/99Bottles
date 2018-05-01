from bottles import line, song

result = "72 bottles of beer on the wall, 72 bottles of beer. Take one down, pass it around, 71 bottles of beer on the wall."
assert line(72) == result, "should print out line of song"

number_of_lines = 99
assert len(song(number_of_lines)) == number_of_lines, "song should be correct number of lines"
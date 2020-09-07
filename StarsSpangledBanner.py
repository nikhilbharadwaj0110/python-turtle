import pysynth

scale = [("d",2), ("e",2), ("f#",4), ("f#",4), ("f#",4), ("f#",8), ("f#",2), ("f#",2), ("f#",2)]


pysynth.make_wav(scale, fn="janaganamana.wav")



'''
"F#" "F#" "E" "F#" "G"
"F#" "F#" "F#" "E" "E" "E" "C#" "E" "D"

"D" "A" "A" "A" "A" "A" "A" "A" "A" "Ab" "A" "Ab" "A"
"G" "G" "G" "G" "G" "F#" "E" "F#"
"F#" "F#" "F#" "F#" "F#" "E" "A" "A" "A" "G" "G"
"F#" "F#" "F#" "E" "E" "E" "E" "C#" "E" "D"

"D" "E" "F#" "F#" "F#" "F#" "E" "F#" "G"
"F#" "G" "A" "A" "A" "G" "F#" "E" "G" "F#"
"F#" "F#" "E" "E" "E" "E" "C#" "E" "D"

"A" "A" "A" "A" "A" "A" "A" "A" "A" "A" "Ab" "B" "A"
"G" "G" "G" "G" "G" "F#" "E" "G" "F#"
"C#" "C#" "D"
"C#" "B" "C#"
"B" "A" "B"
"D" "D" "E" "E" "F#" "F#" "E" "F#" "G"
'''
strokes = []
try:
    with open("logs.txt", "r") as file:
        for line in file:
                strokes.append(line.strip())
except FileNotFoundError:
    pass
for stroke in strokes:
     if "ERROR" in stroke:
        print(stroke)
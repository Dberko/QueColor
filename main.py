import sys, colorsys

n = (int(sys.argv[1], 16))
r = ((n & 0xff0000) >> 16) / 255.0
g = ((n & 0x00ff00) >> 8) / 255.0
b = ((n & 0x0000ff)) / 255.0

(h, s, v) = colorsys.rgb_to_hsv(r, g, b)
# Turn saturation up
(r, g, b) = colorsys.hsv_to_rgb(h, 1, v)

match = "[{}, {}, {}]".format(int(r*255), int(g*255), int(b*255))

for line in open("satfaces.txt"):
	if line.startswith(match):
		print("The color you were thinking of was: " + line.split("] ")[1].strip())
		break

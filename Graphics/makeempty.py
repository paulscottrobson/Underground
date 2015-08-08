#
#	Rip the coal parts off collect*.png and add them on top of empty.png
#
from PIL import Image

for i in range(0,10):
	im = Image.open("empty.png")

	cart = Image.open("collect"+str(i)+".png")
	cart = cart.crop((0,0,48,12))

	im.paste(cart,(0,32))
	im.save("empty"+str(i)+".png")
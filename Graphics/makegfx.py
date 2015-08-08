from PIL import Image

#
#	Build empty squares by ripping the top layer off the collect graphics
#
for i in range(0,10):
	im = Image.open("empty.png")

	cart = Image.open("collect"+str(i)+".png")
	cart = cart.crop((0,0,48,12))

	im.paste(cart,(0,32))
	im.save("empty"+str(i)+".png")

#
#	Build the 48x48 and 16x16 tile maps
#
im = Image.new("RGBA",(48*8,48*5),(0,0,0,0))
tileCount = 0

def addTile(fileName):
	global im,tileCount
	tile = Image.open(fileName)
	im.paste(tile, ((tileCount % 8)*48,int(tileCount/8)*48))
	tileCount = tileCount + 1
	del tile

addTile("earth.png")						# tile 0
for i in range(1,16):						# tile 1-15
	addTile("coal"+str(i)+".png")
for i in range(0,10):						# tile 16-25
	addTile("empty"+str(i)+".png")
addTile("shaft.png")
addTile("grass.png")
addTile("rock.png")
addTile("silver.png")
addTile("gold.png")
addTile("diamond.png")
addTile("rail.png")
for i in range(0,6):
	addTile("block"+str(i)+".png")

# write out at 48x48
im.save("tiles.png")

# write out at 16x16
im.resize((int(im.size[0]/3),int(im.size[1]/3))).save("tiles16.png")
#
#	Build the tilemap tile.
#
from PIL import Image

im = Image.new("RGBA",(48*8,48*5),(0,0,0,0))
tileCount = 0

def addTile(fileName):
	print(fileName)
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




im.save("tiles.png")
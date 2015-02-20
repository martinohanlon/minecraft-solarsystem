#Minecraft - Code a solar system
#Martin O'Hanlon
#www.stuffaboutcode.com

#import minecraft api library
import mcpi.minecraft as minecraft
import mcpi.block as block

# draw hollow sphere
def drawHollowSphere(mc, x1, y1, z1, radius, blockType, blockData=0):
    # create sphere
    for x in range(radius*-1,radius):
        for y in range(radius*-1, radius):
            for z in range(radius*-1,radius):
                if (x**2 + y**2 + z**2 < radius**2) and (x**2 + y**2 + z**2 > (radius**2 - (radius * 2))):
                    mc.setBlock(x1 + x, y1 + y, z1 +z, blockType, blockData)

# draw sphere
def drawSphere(mc, x1, y1, z1, radius, blockType, blockData=0):
    # create sphere
    for x in range(radius*-1,radius):
        for y in range(radius*-1, radius):
            for z in range(radius*-1,radius):
                if (x**2 + y**2 + z**2 < radius**2):
                    mc.setBlock(x1 + x, y1 + y, z1 +z, blockType, blockData)

#setup constants (all values in kilometers)
SUN = 1391684
#name, diameter, distance, blockId, blockData
PLANETS = (("mercury", 4879, 57900000, block.WOOL.id, 7),
           ("venus", 12104, 108200000, block.WOOL.id, 0),
           ("earth", 12756, 149600000, block.WOOL.id, 11),
           ("mars", 6792, 227900000, block.WOOL.id, 14),
           ("jupiter", 142984, 778600000, block.WOOL.id, 4),
           ("saturn", 120536, 1433500000, block.WOOL.id, 8),
           ("uranus", 51118, 2872500000, block.WOOL.id, 3),
           ("neptune", 49528, 4495100000, block.WOOL.id, 10),
           ("pluto", 2390, 5870000000, block.WOOL.id, 6))

#how many km's to a block
# change this value to have different sizes in the solar system
KMTOBLOCK = 12756.0

#middle of the minecraft sky, where the centre of the planets will be
MCMIDDLE = 75

#program
print("Minecraft Planets")
print("1 block = {} kilometers".format(KMTOBLOCK))

#connect to minecraft
mc = minecraft.Minecraft.create()

#set the middle of the solar system
pos = minecraft.Vec3(0,MCMIDDLE,0)

#create the sun
sunDiameter = round(SUN / KMTOBLOCK, 2)
sunRadius = int(round(sunDiameter / 2))
print("Sun - Diameter = {} blocks".format(sunDiameter))
drawHollowSphere(mc, pos.x, pos.y, pos.z, sunRadius, block.WOOL.id, 1)
gapToLeave = (sunDiameter / 2) + 20
pos.z = pos.z + gapToLeave

#loop through the planets
for planet in PLANETS:
    name = planet[0]
    diameter = round(planet[1] / KMTOBLOCK, 2)
    radius = int(round(diameter / 2))
    distance = round(planet[2] / KMTOBLOCK, 2)
    print("{} - Diameter = {} blocks - Distance = {} blocks".format(name, diameter, distance))
    #if the diameter is less than 1.5 draw a single block
    if diameter < 1.5:
        mc.setBlock(pos.x, pos.y, pos.z, planet[3], planet[4])
        pass
    else:
        drawSphere(mc, pos.x, pos.y, pos.z, radius, planet[3], planet[4])
        pass
    
    gapToLeave = (diameter / 2) + 20
    pos.z = pos.z + gapToLeave

#move the player to the sun
mc.player.setPos(0,0,0)

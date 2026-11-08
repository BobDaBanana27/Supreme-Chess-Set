import FreeCAD
import Part
import os

os.makedirs("cad", exist_ok=True)

doc = FreeCAD.newDocument("ElectronicsBezel")

# Electronics Caddy & OLED Display Bezel: 76.0mm x 46.0mm x 8.0mm
length = 76.0
width = 46.0
height = 8.0

# Base block
caddy = Part.makeBox(length, width, height)

# Hollow internal cavity for Motherboard (70.0 x 42.0 x 6.0mm)
mb_pocket = Part.makeBox(70.0, 42.0, 6.2)
mb_pocket.translate(FreeCAD.Vector(3.0, 2.0, 1.8))
caddy = caddy.cut(mb_pocket)

# 0.96" OLED Viewing Window (26.0mm x 15.0mm through-cut)
oled_cut = Part.makeBox(26.0, 15.0, 4.0)
oled_cut.translate(FreeCAD.Vector(40.0, 15.0, 0))
caddy = caddy.cut(oled_cut)

# Dual Pushbutton Plunger Holes (dia 4.5mm)
btn1 = Part.makeCylinder(2.25, 4.0)
btn1.translate(FreeCAD.Vector(15.0, 15.0, 0))
caddy = caddy.cut(btn1)

btn2 = Part.makeCylinder(2.25, 4.0)
btn2.translate(FreeCAD.Vector(15.0, 30.0, 0))
caddy = caddy.cut(btn2)

# USB-C Port Passthrough (10.0mm x 4.0mm)
usbc = Part.makeBox(10.0, 6.0, 4.0)
usbc.translate(FreeCAD.Vector(33.0, -1.0, 2.0))
caddy = caddy.cut(usbc)

# 4x Snap-fit retention tabs along perimeter
snap1 = Part.makeBox(6.0, 1.5, 3.0)
snap1.translate(FreeCAD.Vector(10.0, -1.0, 4.0))
snap2 = Part.makeBox(6.0, 1.5, 3.0)
snap2.translate(FreeCAD.Vector(60.0, -1.0, 4.0))
snap3 = Part.makeBox(6.0, 1.5, 3.0)
snap3.translate(FreeCAD.Vector(10.0, width - 0.5, 4.0))
snap4 = Part.makeBox(6.0, 1.5, 3.0)
snap4.translate(FreeCAD.Vector(60.0, width - 0.5, 4.0))

caddy = caddy.fuse(snap1).fuse(snap2).fuse(snap3).fuse(snap4)

obj = doc.addObject("Part::Feature", "Electronics_Caddy_Bezel")
obj.Shape = caddy
doc.recompute()

doc.saveAs("cad/electronics_bezel.FCStd")
Part.export([caddy], "cad/electronics_bezel.step")
print("Successfully generated cad/electronics_bezel.FCStd and cad/electronics_bezel.step")

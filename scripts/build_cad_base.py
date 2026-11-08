import FreeCAD
import Part
import os

os.makedirs("cad", exist_ok=True)

doc = FreeCAD.newDocument("SupremeChessBase")

# Base Chassis Half (for folding clamshell): Length 168mm, Width 92mm, Height 15mm
length = 168.0
width = 92.0
height = 15.0
wall = 2.4

# Outer Solid Block
outer_box = Part.makeBox(length, width, height)

# Hollow Internal Pocket for Board Grid Insert (160 x 80 x 4mm)
board_pocket = Part.makeBox(160.0, 80.0, 4.0)
board_pocket.translate(FreeCAD.Vector(4.0, 6.0, height - 4.0))

# Drawer Slide-Way Cavity (158 x 82 x 8mm) from side
drawer_cavity = Part.makeBox(158.0, 84.0, 7.5)
drawer_cavity.translate(FreeCAD.Vector(5.0, 4.0, 2.0))

# Electronics & Motherboard Pocket (78 x 50 x 8mm)
mcu_pocket = Part.makeBox(78.0, 50.0, 8.0)
mcu_pocket.translate(FreeCAD.Vector(45.0, 20.0, 2.0))

# USB-C Port Cutout on Outer Wall (9.5mm x 3.5mm)
usbc_cutout = Part.makeBox(12.0, 10.0, 4.0)
usbc_cutout.translate(FreeCAD.Vector(80.0, -2.0, 5.0))

# Hinge Pivot Knuckles (Left & Right 12mm x 8mm with 3mm pin hole)
h1 = Part.makeCylinder(4.0, 15.0)
h1.rotate(FreeCAD.Vector(0,0,0), FreeCAD.Vector(1,0,0), 90)
h1.translate(FreeCAD.Vector(20.0, width, 7.5))

h2 = Part.makeCylinder(4.0, 15.0)
h2.rotate(FreeCAD.Vector(0,0,0), FreeCAD.Vector(1,0,0), 90)
h2.translate(FreeCAD.Vector(140.0, width, 7.5))

# Magnetic Latch Recesses (5.2mm dia x 2.2mm deep for 5x2mm disc magnets)
mag1 = Part.makeCylinder(2.6, 2.5)
mag1.translate(FreeCAD.Vector(15.0, 4.0, height - 2.5))

mag2 = Part.makeCylinder(2.6, 2.5)
mag2.translate(FreeCAD.Vector(153.0, 4.0, height - 2.5))

# Boolean Cut operations
chassis = outer_box.cut(board_pocket)
chassis = chassis.cut(drawer_cavity)
chassis = chassis.cut(usbc_cutout)
chassis = chassis.cut(mag1)
chassis = chassis.cut(mag2)

# Add hinge knuckles
chassis = chassis.fuse(h1)
chassis = chassis.fuse(h2)

# Add to document
obj = doc.addObject("Part::Feature", "Chassis_Base_Half")
obj.Shape = chassis
doc.recompute()

doc.saveAs("cad/supreme_chess_base.FCStd")
Part.export([chassis], "cad/supreme_chess_base.step")
print("Successfully generated cad/supreme_chess_base.FCStd and cad/supreme_chess_base.step")

import FreeCAD
import Part
import os

os.makedirs("cad", exist_ok=True)

doc = FreeCAD.newDocument("CaptureTray")

# Slide-Out Capture Tray Body: 156.0mm (length) x 82.0mm (width) x 7.0mm (height)
length = 156.0
width = 82.0
height = 7.0

# Base solid
tray_body = Part.makeBox(length, width, height)

# Drawer Front Pull Lip (6mm x 30mm tab extending from front edge)
pull_tab = Part.makeBox(6.0, 30.0, 4.0)
pull_tab.translate(FreeCAD.Vector(-6.0, 26.0, 1.5))
tray_body = tray_body.fuse(pull_tab)

# Side Guide Ribs (1.2mm x 1.5mm along left and right edges for sliding track)
rib_l = Part.makeBox(length, 1.5, 1.5)
rib_l.translate(FreeCAD.Vector(0, 0, 2.5))
tray_body = tray_body.fuse(rib_l)

rib_r = Part.makeBox(length, 1.5, 1.5)
rib_r.translate(FreeCAD.Vector(0, width - 1.5, 2.5))
tray_body = tray_body.fuse(rib_r)

# Underneath Cavity for Sensor Strip PCB (152mm x 24mm x 2.2mm)
pcb_pocket = Part.makeBox(152.0, 24.0, 2.2)
pcb_pocket.translate(FreeCAD.Vector(2.0, 29.0, 0))
tray_body = tray_body.cut(pcb_pocket)

# 16 Total Molded Sockets (Full 16-Piece Army Storage & Capture Sockets)
# Row 1 (y = 18.0mm): 8 Pawns (13.0mm dia x 4.8mm deep)
cuts = []
for i in range(8):
    px = 12.0 + i * 18.0
    py = 18.0
    pawn_socket = Part.makeCylinder(6.5, 4.8)
    pawn_socket.translate(FreeCAD.Vector(px, py, height - 4.8))
    cuts.append(pawn_socket)

# Row 2 (y = 54.0mm): Major & Minor Pieces + Royal Court (8 Sockets)
# 1. King Socket (15.5mm dia x 4.8mm deep) - 0 points / Resign & Travel home
king_socket = Part.makeCylinder(7.75, 4.8)
king_socket.translate(FreeCAD.Vector(12.0, 54.0, height - 4.8))
cuts.append(king_socket)

# 2. Queen Socket (15.5mm dia x 4.8mm deep) - +9 points
queen_socket = Part.makeCylinder(7.75, 4.8)
queen_socket.translate(FreeCAD.Vector(30.0, 54.0, height - 4.8))
cuts.append(queen_socket)

# 3 & 4. Rooks (14.0mm dia x 4.8mm deep) - +5 points each
r1 = Part.makeCylinder(7.0, 4.8)
r1.translate(FreeCAD.Vector(50.0, 54.0, height - 4.8))
cuts.append(r1)

r2 = Part.makeCylinder(7.0, 4.8)
r2.translate(FreeCAD.Vector(70.0, 54.0, height - 4.8))
cuts.append(r2)

# 5 & 6. Bishops (14.0mm dia x 4.8mm deep) - +3 points each
b1 = Part.makeCylinder(7.0, 4.8)
b1.translate(FreeCAD.Vector(90.0, 54.0, height - 4.8))
cuts.append(b1)

b2 = Part.makeCylinder(7.0, 4.8)
b2.translate(FreeCAD.Vector(110.0, 54.0, height - 4.8))
cuts.append(b2)

# 7 & 8. Knights (14.0mm dia x 4.8mm deep) - +3 points each
n1 = Part.makeCylinder(7.0, 4.8)
n1.translate(FreeCAD.Vector(130.0, 54.0, height - 4.8))
cuts.append(n1)

n2 = Part.makeCylinder(7.0, 4.8)
n2.translate(FreeCAD.Vector(146.0, 54.0, height - 4.8))
cuts.append(n2)

# Apply all 16 socket cuts
final_tray = tray_body
for cut_shape in cuts:
    final_tray = final_tray.cut(cut_shape)

obj = doc.addObject("Part::Feature", "Capture_Tray")
obj.Shape = final_tray
doc.recompute()

doc.saveAs("cad/capture_tray.FCStd")
Part.export([final_tray], "cad/capture_tray.step")
print("Successfully generated updated 16-slot cad/capture_tray.FCStd and cad/capture_tray.step")

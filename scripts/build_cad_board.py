import FreeCAD
import Part
import os

os.makedirs("cad", exist_ok=True)

doc = FreeCAD.newDocument("BoardGridHalf")

# Half board dimensions: 160.0mm (8 squares wide) x 80.0mm (4 squares deep) x 3.5mm thick
width = 160.0
depth = 80.0
height = 3.5
sq_size = 18.0
border = (width - (sq_size * 8)) / 2.0  # 8.0mm border total (4.0mm left & right)

# Base substrate
base = Part.makeBox(width, depth, height)

# Create 32 magnet pockets on bottom surface (5.2mm diameter x 2.2mm deep)
# Leaving 1.3mm solid plastic top surface
cuts = []
for col in range(8):
    for row in range(4):
        cx = border + col * sq_size + (sq_size / 2.0)
        cy = border + row * sq_size + (sq_size / 2.0)
        
        # Cylindrical magnet cavity from bottom up
        cyl = Part.makeCylinder(2.6, 2.2)
        cyl.translate(FreeCAD.Vector(cx, cy, 0))
        cuts.append(cyl)

        # 0.4mm deep groove for tile separation on top
        if col < 7:
            gx = border + (col + 1) * sq_size - 0.25
            gy = border
            g1 = Part.makeBox(0.5, sq_size * 4, 0.4)
            g1.translate(FreeCAD.Vector(gx, gy, height - 0.4))
            cuts.append(g1)
            
        if row < 3:
            gx = border
            gy = border + (row + 1) * sq_size - 0.25
            g2 = Part.makeBox(sq_size * 8, 0.5, 0.4)
            g2.translate(FreeCAD.Vector(gx, gy, height - 0.4))
            cuts.append(g2)

# Apply all cuts
grid_shape = base
for cut_shape in cuts:
    grid_shape = grid_shape.cut(cut_shape)

obj = doc.addObject("Part::Feature", "Board_Grid_Half")
obj.Shape = grid_shape
doc.recompute()

doc.saveAs("cad/board_grid_half.FCStd")
Part.export([grid_shape], "cad/board_grid_half.step")
print("Successfully generated cad/board_grid_half.FCStd and cad/board_grid_half.step")

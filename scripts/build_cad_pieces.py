import FreeCAD
import Part
import os

os.makedirs("cad", exist_ok=True)

doc = FreeCAD.newDocument("ChessPieceSet")

pieces = []

# Helper function to create piece with base magnet cavity
def make_piece(name, x_offset, base_dia, total_h, stem_dia, head_type):
    # Base disc
    base = Part.makeCylinder(base_dia / 2.0, 3.5)
    # Magnet cavity in bottom (5.2mm dia x 2.2mm deep)
    mag_cavity = Part.makeCylinder(2.6, 2.2)
    base = base.cut(mag_cavity)
    
    # Stem cone
    stem = Part.makeCone(base_dia / 2.0 - 0.5, stem_dia / 2.0, total_h - 8.0)
    stem.translate(FreeCAD.Vector(0, 0, 3.5))
    
    # Collar ring
    collar = Part.makeCylinder(stem_dia / 2.0 + 1.0, 1.5)
    collar.translate(FreeCAD.Vector(0, 0, total_h - 4.5))
    
    # Head feature depending on piece type
    if head_type == "pawn":
        head = Part.makeSphere(stem_dia / 2.0 + 1.0)
        head.translate(FreeCAD.Vector(0, 0, total_h - 1.5))
    elif head_type == "rook":
        head = Part.makeCylinder(base_dia / 2.0 - 1.0, 4.0)
        head.translate(FreeCAD.Vector(0, 0, total_h - 3.0))
    elif head_type == "bishop":
        head = Part.makeSphere(stem_dia / 2.0 + 1.5)
        head.translate(FreeCAD.Vector(0, 0, total_h - 2.0))
    elif head_type == "knight":
        head = Part.makeBox(stem_dia, stem_dia * 1.4, 6.0)
        head.translate(FreeCAD.Vector(-stem_dia/2.0, -stem_dia*0.7, total_h - 4.0))
    elif head_type == "queen":
        head = Part.makeCone(stem_dia / 2.0, base_dia / 2.0 - 0.5, 4.5)
        head.translate(FreeCAD.Vector(0, 0, total_h - 3.0))
        crown = Part.makeSphere(1.5)
        crown.translate(FreeCAD.Vector(0, 0, total_h + 1.5))
        head = head.fuse(crown)
    else: # king
        head = Part.makeCylinder(stem_dia / 2.0 + 1.0, 4.0)
        head.translate(FreeCAD.Vector(0, 0, total_h - 3.0))
        cross_v = Part.makeBox(1.2, 1.2, 4.0)
        cross_v.translate(FreeCAD.Vector(-0.6, -0.6, total_h + 1.0))
        cross_h = Part.makeBox(3.0, 1.2, 1.2)
        cross_h.translate(FreeCAD.Vector(-1.5, -0.6, total_h + 2.5))
        head = head.fuse(cross_v).fuse(cross_h)
        
    full_piece = base.fuse(stem).fuse(collar).fuse(head)
    full_piece.translate(FreeCAD.Vector(x_offset, 0, 0))
    return full_piece

p_pawn   = make_piece("Pawn",   0.0,   12.0, 18.0, 6.0, "pawn")
p_rook   = make_piece("Rook",   20.0,  13.5, 22.0, 7.5, "rook")
p_knight = make_piece("Knight", 40.0,  13.5, 24.0, 7.5, "knight")
p_bishop = make_piece("Bishop", 60.0,  13.5, 26.0, 7.0, "bishop")
p_queen  = make_piece("Queen",  80.0,  14.5, 30.0, 8.0, "queen")
p_king   = make_piece("King",   105.0, 14.5, 33.0, 8.0, "king")

all_pieces = p_pawn.fuse(p_rook).fuse(p_knight).fuse(p_bishop).fuse(p_queen).fuse(p_king)

obj = doc.addObject("Part::Feature", "Complete_Piece_Set")
obj.Shape = all_pieces
doc.recompute()

doc.saveAs("cad/chess_pieces.FCStd")
Part.export([all_pieces], "cad/chess_pieces.step")
print("Successfully generated cad/chess_pieces.FCStd and cad/chess_pieces.step")

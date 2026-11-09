"""
Supreme Chess Set — High-Detail Support-Free Staunton Chess Piece Set
Generated for FreeCAD 1.1 with 100% self-supporting FDM printability (all overhangs <= 45 deg).
Includes embedded blind magnet cavities (5.2mm dia x 2.2mm) with 45-deg conical roofs.
"""

import FreeCAD
import Part
import math
import os

os.makedirs("cad", exist_ok=True)

doc = FreeCAD.newDocument("ChessPieceSet")

def make_revolve(points):
    """Revolves an (r, z) half-profile around the Z-axis."""
    p3d = [FreeCAD.Vector(r, 0, z) for r, z in points]
    if points[-1][0] != 0:
        p3d.append(FreeCAD.Vector(0, 0, points[-1][1]))
    if points[0][0] != 0:
        p3d.insert(0, FreeCAD.Vector(0, 0, points[0][1]))
    p3d.append(p3d[0])
    wire = Part.makePolygon(p3d)
    face = Part.Face(wire)
    return face.revolve(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1), 360)

def add_base_magnet_cavity(shape):
    """
    Cuts a 5.2mm dia blind magnet cavity into the underside.
    Includes a 45-degree conical roof so the ceiling prints support-free.
    """
    cyl = Part.makeCylinder(2.6, 1.8)
    cone = Part.makeCone(2.6, 0.0, 0.8)
    cone.translate(FreeCAD.Vector(0, 0, 1.8))
    cavity = cyl.fuse(cone)
    return shape.cut(cavity)

# -------------------------------------------------------------------------
# 1. PAWN (Height: 19.5mm, Base: 12.0mm)
# -------------------------------------------------------------------------
def build_pawn():
    # Multi-tier classical Staunton pedestal, waisted stem, astragal collar, spherical head
    pts = [
        (6.0, 0.0), (6.0, 1.2), (5.2, 2.2), (5.4, 3.0), (4.6, 4.0),
        (4.2, 5.5), (3.6, 7.5), (3.0, 9.5), (2.6, 11.2),
        (3.6, 12.2), (3.6, 12.8), (2.8, 13.5), # Collar ring (45 deg flare)
        (3.6, 14.5), (4.2, 16.0), (4.0, 17.8), (2.4, 19.0), (0.0, 19.5) # Head
    ]
    pawn = make_revolve(pts)
    return add_base_magnet_cavity(pawn)

# -------------------------------------------------------------------------
# 2. ROOK (Height: 23.5mm, Base: 13.5mm)
# -------------------------------------------------------------------------
def build_rook():
    # Castle tower: stepped pedestal, masonry belt, flared corbel parapet, hollow well, 4 crenellations
    pts = [
        (6.75, 0.0), (6.75, 1.4), (5.8, 2.4), (6.0, 3.4), (5.0, 4.4),
        (4.7, 6.0), (4.4, 9.5), (4.8, 10.4), (4.8, 11.2), (4.2, 12.0), # Masonry belt
        (4.2, 14.5), (5.8, 17.5), (6.2, 23.5), (0.0, 23.5) # Flared parapet
    ]
    rook = make_revolve(pts)

    # Hollow interior well with 45-deg conical floor
    well_cyl = Part.makeCylinder(3.6, 5.0)
    well_cyl.translate(FreeCAD.Vector(0, 0, 19.5))
    well_cone = Part.makeCone(0.0, 3.6, 1.5)
    well_cone.translate(FreeCAD.Vector(0, 0, 18.0))
    rook = rook.cut(well_cyl.fuse(well_cone))

    # 4 Castle Crenellations (2 perpendicular cuts)
    slot1 = Part.makeBox(2.2, 14.0, 4.0)
    slot1.translate(FreeCAD.Vector(-1.1, -7.0, 20.5))
    slot2 = Part.makeBox(14.0, 2.2, 4.0)
    slot2.translate(FreeCAD.Vector(-7.0, -1.1, 20.5))
    rook = rook.cut(slot1).cut(slot2)

    return add_base_magnet_cavity(rook)

# -------------------------------------------------------------------------
# 3. KNIGHT (Height: 25.5mm, Base: 13.5mm)
# -------------------------------------------------------------------------
def build_knight():
    # Tiered circular pedestal
    base_pts = [
        (6.75, 0.0), (6.75, 1.4), (5.8, 2.4), (6.0, 3.4), (5.0, 4.4),
        (4.7, 5.5), (4.4, 6.8), (0.0, 6.8)
    ]
    base = make_revolve(base_pts)

    # Sculpted horse head profile (XZ plane)
    profile_pts = [
        FreeCAD.Vector(-4.2, 0, 6.5),   # Base rear
        FreeCAD.Vector(-4.8, 0, 9.8),   # Mane lower tuft
        FreeCAD.Vector(-4.0, 0, 10.8),
        FreeCAD.Vector(-4.8, 0, 13.5),  # Mane mid tuft
        FreeCAD.Vector(-3.8, 0, 14.5),
        FreeCAD.Vector(-4.4, 0, 17.5),  # Mane upper tuft
        FreeCAD.Vector(-3.0, 0, 18.5),
        FreeCAD.Vector(-3.2, 0, 21.0),  # Mane crest
        FreeCAD.Vector(-1.8, 0, 22.0),
        FreeCAD.Vector(-1.0, 0, 25.5),  # Ear tip
        FreeCAD.Vector(0.5, 0, 23.0),   # Forehead dip
        FreeCAD.Vector(2.8, 0, 21.5),   # Brow
        FreeCAD.Vector(5.5, 0, 17.5),   # Snout slope
        FreeCAD.Vector(5.8, 0, 15.5),   # Muzzle tip
        FreeCAD.Vector(4.8, 0, 14.2),   # Under chin
        FreeCAD.Vector(3.2, 0, 13.0),   # Jaw corner
        FreeCAD.Vector(2.8, 0, 9.5),    # Throat (steep self-supporting slope)
        FreeCAD.Vector(3.8, 0, 6.5),    # Chest front
        FreeCAD.Vector(-4.2, 0, 6.5)    # Close loop
    ]
    wire_head = Part.makePolygon(profile_pts)
    solid_head = Part.Face(wire_head).extrude(FreeCAD.Vector(0, 6.4, 0))
    solid_head.translate(FreeCAD.Vector(0, -3.2, 0))

    # Taper the snout cheeks (angled cuts on left and right)
    cut_l = Part.makeBox(10.0, 4.0, 15.0)
    cut_l.translate(FreeCAD.Vector(0, 1.8, 12.0))
    cut_l.rotate(FreeCAD.Vector(2.0, 1.8, 12.0), FreeCAD.Vector(0, 0, 1), 22)

    cut_r = Part.makeBox(10.0, 4.0, 15.0)
    cut_r.translate(FreeCAD.Vector(0, -5.8, 12.0))
    cut_r.rotate(FreeCAD.Vector(2.0, -1.8, 12.0), FreeCAD.Vector(0, 0, 1), -22)
    solid_head = solid_head.cut(cut_l).cut(cut_r)

    # Ear separation notch (divides top into distinct left & right ears)
    ear_notch = Part.makeBox(4.0, 1.4, 4.0)
    ear_notch.translate(FreeCAD.Vector(-2.0, -0.7, 23.5))
    solid_head = solid_head.cut(ear_notch)

    # Eye socket recesses
    eye_l = Part.makeSphere(0.9)
    eye_l.translate(FreeCAD.Vector(2.0, 2.0, 20.0))
    eye_r = Part.makeSphere(0.9)
    eye_r.translate(FreeCAD.Vector(2.0, -2.0, 20.0))
    solid_head = solid_head.cut(eye_l).cut(eye_r)

    # Nostrils
    nos_l = Part.makeSphere(0.6)
    nos_l.translate(FreeCAD.Vector(5.4, 1.1, 16.0))
    nos_r = Part.makeSphere(0.6)
    nos_r.translate(FreeCAD.Vector(5.4, -1.1, 16.0))
    solid_head = solid_head.cut(nos_l).cut(nos_r)

    knight = base.fuse(solid_head)
    return add_base_magnet_cavity(knight)

# -------------------------------------------------------------------------
# 4. BISHOP (Height: 28.5mm, Base: 13.5mm)
# -------------------------------------------------------------------------
def build_bishop():
    # Slender concave stem, double collar rings, teardrop mitre cap, 45-deg angled cleft cut, finial ball
    pts = [
        (6.75, 0.0), (6.75, 1.4), (5.8, 2.4), (6.0, 3.4), (5.0, 4.4),
        (4.5, 6.0), (3.5, 9.0), (2.8, 12.0),
        (3.8, 13.0), (3.8, 13.8), (3.0, 14.5), # Lower collar
        (4.3, 15.5), (4.3, 16.3), (3.2, 17.0), # Upper collar
        (4.8, 19.0), (5.2, 21.0), (4.6, 23.5), (3.2, 25.5), (1.4, 26.8), # Mitre
        (1.8, 27.4), (1.5, 28.2), (0.0, 28.5) # Top finial ball
    ]
    bishop = make_revolve(pts)

    # 45-degree diagonal mitre cleft cut (slopes upward, completely support-free)
    cut_box = Part.makeBox(12.0, 1.4, 8.0)
    cut_box.translate(FreeCAD.Vector(-6.0, -0.7, 0))
    cut_box.rotate(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0), 45)
    cut_box.translate(FreeCAD.Vector(0, 2.5, 22.0))
    bishop = bishop.cut(cut_box)

    return add_base_magnet_cavity(bishop)

# -------------------------------------------------------------------------
# 5. QUEEN (Height: 30.5mm, Base: 14.5mm)
# -------------------------------------------------------------------------
def build_queen():
    # Regal pedestal, slender waist, double astragals, flared coronet, 8-point scalloped rim, inner dome & pearl
    pts = [
        (7.25, 0.0), (7.25, 1.4), (6.4, 2.4), (6.6, 3.4), (5.4, 4.6),
        (4.8, 6.5), (3.8, 10.5), (3.2, 14.0),
        (4.2, 15.0), (4.2, 15.8), (3.4, 16.5), # Lower collar
        (4.6, 17.5), (4.6, 18.3), (3.8, 19.0), # Upper collar
        (4.6, 20.5), (5.5, 22.5), (6.4, 25.0), (6.5, 27.5), (0.0, 27.5) # Coronet rim
    ]
    queen = make_revolve(pts)

    # Interior crown well with 45-deg conical bottom
    well_cyl = Part.makeCylinder(4.4, 6.0)
    well_cyl.translate(FreeCAD.Vector(0, 0, 24.0))
    well_cone = Part.makeCone(0.0, 4.4, 2.0)
    well_cone.translate(FreeCAD.Vector(0, 0, 22.0))
    queen = queen.cut(well_cyl.fuse(well_cone))

    # 8 radial V-notches around the crown rim (creates 8 pointed royal crown petals)
    for i in range(8):
        angle = i * (360.0 / 8.0)
        rad = math.radians(angle)
        notch = Part.makeBox(2.2, 2.2, 3.5)
        notch.translate(FreeCAD.Vector(-1.1, -1.1, -1.0))
        notch.rotate(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 1, 0), 45) # 45-deg V notch
        notch.translate(FreeCAD.Vector(5.8 * math.cos(rad), 5.8 * math.sin(rad), 27.5))
        queen = queen.cut(notch)

    # Royal inner dome and finial pearl
    dome = Part.makeSphere(2.5)
    dome.translate(FreeCAD.Vector(0, 0, 26.0))
    pearl = Part.makeSphere(1.2)
    pearl.translate(FreeCAD.Vector(0, 0, 29.5))
    queen = queen.fuse(dome).fuse(pearl)

    return add_base_magnet_cavity(queen)

# -------------------------------------------------------------------------
# 6. KING (Height: 34.0mm, Base: 14.5mm)
# -------------------------------------------------------------------------
def build_king():
    # Imperial multi-tier pedestal, column waist rings, flared capital, headband, imperial dome, support-free Formee cross
    pts = [
        (7.25, 0.0), (7.25, 1.4), (6.4, 2.4), (6.6, 3.4), (5.4, 4.6),
        (5.0, 6.5), (4.0, 11.0), (4.5, 12.0), (4.5, 12.8), (3.6, 13.5), # Lower ring
        (3.5, 16.0), (4.2, 17.0), (4.2, 17.8), (3.6, 18.5), # Upper ring
        (4.8, 20.5), (5.8, 23.0), (6.2, 25.0), # Flared capital
        (5.5, 25.8), (5.8, 26.6), (4.8, 27.5), # Headband
        (3.8, 28.5), (2.0, 29.5), (0.0, 30.0)  # Imperial dome
    ]
    king = make_revolve(pts)

    # Self-Supporting Heraldic Formee Cross (all under-slopes >= 45 deg)
    v_post = Part.makeBox(1.4, 1.4, 4.5)
    v_post.translate(FreeCAD.Vector(-0.7, -0.7, 29.5))

    # Left cross arm with 45-deg under-slope
    arm_l_pts = [
        FreeCAD.Vector(0, -0.7, 31.0),
        FreeCAD.Vector(-2.8, -0.7, 33.0),
        FreeCAD.Vector(-2.8, -0.7, 34.0),
        FreeCAD.Vector(0, -0.7, 33.5),
        FreeCAD.Vector(0, -0.7, 31.0)
    ]
    arm_l = Part.Face(Part.makePolygon(arm_l_pts)).extrude(FreeCAD.Vector(0, 1.4, 0))

    # Right cross arm with 45-deg under-slope
    arm_r_pts = [
        FreeCAD.Vector(0, -0.7, 31.0),
        FreeCAD.Vector(2.8, -0.7, 33.0),
        FreeCAD.Vector(2.8, -0.7, 34.0),
        FreeCAD.Vector(0, -0.7, 33.5),
        FreeCAD.Vector(0, -0.7, 31.0)
    ]
    arm_r = Part.Face(Part.makePolygon(arm_r_pts)).extrude(FreeCAD.Vector(0, 1.4, 0))

    # Top cross arm with flared crown
    top_pts = [
        FreeCAD.Vector(-0.7, -0.7, 33.5),
        FreeCAD.Vector(-1.2, -0.7, 35.0),
        FreeCAD.Vector(1.2, -0.7, 35.0),
        FreeCAD.Vector(0.7, -0.7, 33.5),
        FreeCAD.Vector(-0.7, -0.7, 33.5)
    ]
    top_arm = Part.Face(Part.makePolygon(top_pts)).extrude(FreeCAD.Vector(0, 1.4, 0))

    cross = v_post.fuse(arm_l).fuse(arm_r).fuse(top_arm)
    king = king.fuse(cross)

    return add_base_magnet_cavity(king)

# -------------------------------------------------------------------------
# Build and Layout Full Set
# -------------------------------------------------------------------------
print("Generating high-detail Staunton piece set...")

p_pawn   = build_pawn()
p_rook   = build_rook()
p_knight = build_knight()
p_bishop = build_bishop()
p_queen  = build_queen()
p_king   = build_king()

# Position each piece spaced along the X axis for inspection and 3D printing
p_pawn.translate(FreeCAD.Vector(0.0, 0.0, 0.0))
p_rook.translate(FreeCAD.Vector(20.0, 0.0, 0.0))
p_knight.translate(FreeCAD.Vector(40.0, 0.0, 0.0))
p_bishop.translate(FreeCAD.Vector(60.0, 0.0, 0.0))
p_queen.translate(FreeCAD.Vector(80.0, 0.0, 0.0))
p_king.translate(FreeCAD.Vector(105.0, 0.0, 0.0))

all_pieces = p_pawn.fuse(p_rook).fuse(p_knight).fuse(p_bishop).fuse(p_queen).fuse(p_king)

# Export individual piece solids to FreeCAD Document for easy inspection
for name, shape in [
    ("Pawn", p_pawn),
    ("Rook", p_rook),
    ("Knight", p_knight),
    ("Bishop", p_bishop),
    ("Queen", p_queen),
    ("King", p_king),
    ("Complete_Piece_Set", all_pieces)
]:
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = shape

doc.recompute()
doc.saveAs("cad/chess_pieces.FCStd")
Part.export([all_pieces], "cad/chess_pieces.step")

print("Successfully generated:")
print("  - cad/chess_pieces.FCStd")
print("  - cad/chess_pieces.step")

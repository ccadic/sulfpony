from solid import *
from solid.utils import *

# Paramètres généraux
pcb_width = 300
pcb_height = 300
corner_radius = 5
thickness = 1.6  # utile si STL
hole_diameter = 3
hole_offset = 10  # distance depuis les bords

# PCB principal avec coins arrondis
pcb_shape = offset(r=corner_radius)(
    square([pcb_width - 2*corner_radius, pcb_height - 2*corner_radius])
)
pcb_shape = translate([corner_radius, corner_radius])(pcb_shape)

# Trous de fixation
holes = []
hole_r = hole_diameter / 2

# Positions des trous (4 coins)
hole_positions = [
    [hole_offset, hole_offset],
    [pcb_width - hole_offset, hole_offset],
    [hole_offset, pcb_height - hole_offset],
    [pcb_width - hole_offset, pcb_height - hole_offset]
]

for pos in hole_positions:
    holes.append(translate(pos)(circle(hole_r)))

# Soustraction des trous au PCB
final_pcb = pcb_shape - union()(*holes)

# Export du fichier SCAD
scad_render_to_file(final_pcb, "pcb_300x300_holes.scad", file_header='$fn = 100;')

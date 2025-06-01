import ezdxf

# Paramètres du PCB
width = 300  # mm
height = 300  # mm
corner_radius = 5  # mm
hole_diameter = 3  # mm
hole_offset = 10   # mm

# Création du document DXF
doc = ezdxf.new(dxfversion="R2010")
msp = doc.modelspace()

# Fonction pour créer les coins arrondis
def draw_rounded_rectangle(msp, x, y, w, h, r):
    # Segments droits
    msp.add_line((x + r, y), (x + w - r, y))               # bas
    msp.add_line((x + w, y + r), (x + w, y + h - r))       # droite
    msp.add_line((x + w - r, y + h), (x + r, y + h))       # haut
    msp.add_line((x, y + h - r), (x, y + r))               # gauche

    # Arcs de coin (sens horaire)
    msp.add_arc(center=(x + w - r, y + r), radius=r, start_angle=270, end_angle=360)
    msp.add_arc(center=(x + w - r, y + h - r), radius=r, start_angle=0, end_angle=90)
    msp.add_arc(center=(x + r, y + h - r), radius=r, start_angle=90, end_angle=180)
    msp.add_arc(center=(x + r, y + r), radius=r, start_angle=180, end_angle=270)

# Dessin du PCB
draw_rounded_rectangle(msp, 0, 0, width, height, corner_radius)

# Ajout des 4 trous de fixation
hole_r = hole_diameter / 2
hole_positions = [
    (hole_offset, hole_offset),
    (width - hole_offset, hole_offset),
    (hole_offset, height - hole_offset),
    (width - hole_offset, height - hole_offset)
]

for x, y in hole_positions:
    msp.add_circle(center=(x, y), radius=hole_r)

# Sauvegarde du fichier
output_file = "pcb_300x300_rounded_holes.dxf"
doc.saveas(output_file)
print(f"Fichier DXF sauvegardé : {output_file}")

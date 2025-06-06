// Generated by SolidPython 1.1.3 on 2025-06-01 23:56:36
$fn = 100;


translate(v = [5, 5]) {
	offset(r = 5) {
		square(size = [290, 290]);
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from solid import *
from solid.utils import *

pcb_width = 300
pcb_height = 300
corner_radius = 5
thickness = 1.6  # utile si export STL en plus du DXF

pcb = offset(r=corner_radius)(
    square([pcb_width - 2*corner_radius, pcb_height - 2*corner_radius])
)
pcb = translate([corner_radius, corner_radius])(pcb)

scad_render_to_file(pcb, "pcb_300x300.scad", file_header='$fn = 100;')
 
 
************************************************/

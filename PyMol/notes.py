Fruit Fly Apoptosome: 3IZ8
http://www.rcsb.org/pdb/files/3IZ8.pdb1.gz

Loading PDB
load $PYMOL_PATH/test/dat/pept.pdb, test  # The object is named "test".

Zoomimng
zoom resi 1-10	# The selector resi 
                # chooses amino acid residues 
                # given by the PDB sequence number 
                # identifier "1-10."
zoom center, 100
zoom

Rendering
ray 2400, 2400
png fileName, dpi=300

renderer = -1 # is default (use value in ray_default_renderer)
renderer = 0 # uses PyMOL's internal renderer
renderer = 1 # uses PovRay's renderer. This is Unix-only and you must have "povray" in your path. It utilizes two temporary files: "tmp_pymol.pov" and "tmp_pymol.png".

povray -W12800 -H9600 +Q11 +A 3IZ8.pov

sudo ./cputhrottle povray 25

# normal color
set ray_trace_mode, 0
 
# normal color + black outline
set ray_trace_mode,  1
 
# black outline only
set ray_trace_mode,  2
 
# quantized color + black outline
set ray_trace_mode,  3


set orthoscopic, off

# Color Script
load /tmp/thy_model/1l9l.pdb;
hide lines;
show cartoon;
set ray_trace_mode, 3; # color
bg_color white;
set antialias, 2;
remove resn HOH
remove resn HET
ray 600,600
png /tmp/1l9l.png


# AutoRender Script
# initialing
reset
zoom center, 20
# positioningn x, -y, z
translate [100, -130, 0]
# first row
# while x > -200
ray 1200, 1200
png 3IZ8_1.png
translate [-50, 0, 0]
ray 1200, 1200
png 3IZ8_2.png
translate [-50, 0, 0]
ray 1200, 1200
png 3IZ8_3.png
translate [-50, 0, 0]
ray 1200, 1200
png 3IZ8_4.png
translate [-50, 0, 0]
ray 1200, 1200
png 3IZ8_5.png

# move to the next row
translate [200, 0, 0]
translate [0, 50, 0]
# while x > -200
ray 1200, 1200
png 3IZ8_6.png
translate [-50, 0, 0]
ray 1200, 1200
png 3IZ8_7.png
translate [-50, 0, 0]
ray 1200, 1200
png 3IZ8_8.png
translate [-50, 0, 0]
ray 1200, 1200
png 3IZ8_9.png
translate [-50, 0, 0]
ray 1200, 1200
png 3IZ8_10.png




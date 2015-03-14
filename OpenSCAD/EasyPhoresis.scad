// DIYbio EasyPhoresis
// by alec_djinn 2014
// www.diybiogroningen.org
// Version: beta 2

// dimensions
width = 40;
height = 20;
depth = 80;
thickness = 2.5;


// body shape
module body(width,height,depth,thickness){
	difference() {
		minkowski(){
			cube([width,depth,height], center=true);
			cylinder(r=thickness, h=1);
		}
		translate([0,0,height]){
			rotate([0,90,0]){
				cylinder (h=2*width, r=height, center=true);
			}
		}
	}
}


module gel(width,height,depth,thickness){
	translate([0,0,-height]){
	difference(){
		difference(){
			union(){
				translate([0,0,-height/8]){
					cube([width+2*thickness,depth/1.5,height/8], center=true);
				}
				cube([width-2,depth/1.5,height/4], center=true);
			}
			translate([0,0,-height/12]){
				cube([width-(2*thickness),depth/1.2,height/4], center=true);
			}
		}
		// comb holder
		translate([-width/2,depth/3.5,-2*thickness]){
			cylinder(h=thickness, r=thickness/2);
		}
		translate([width/2,depth/3.5,-2*thickness]){
			cylinder(h=thickness, r=thickness/2);
		}
		translate([-width/2,-depth/(6*3.5),-2*thickness]){
			cylinder(h=thickness, r=thickness/2);
		}
		translate([width/2,-depth/(6*3.5),-2*thickness]){
			cylinder(h=thickness, r=thickness/2);
		}
	}
	}
}

// 9 wells comb
module comb(width,height,depth,thickness){
	translate([0,0,-1.5*height]){
		union(){
			translate([-width/2,depth/3.5,-2*thickness]){
				cylinder(h=thickness, r=thickness/2);
			}
			translate([width/2,depth/3.5,-2*thickness]){
				cylinder(h=thickness, r=thickness/2);
			}
			translate([0,depth/3.5,(-height/8)-thickness]){
				cube([width+2*thickness,depth/12,height/8],center=true);	
			}
			translate([thickness/2,0,0]){
				// numbers of wells
				for(n=[1:2.4*width/10]){
					translate([(-width/2)+thickness*n*1.5,depth/3.5,-height/10]){
						cube([thickness,depth/64,height/5],center=true);	
					}
				}
			}
		}
	}
}

// body: shape - void
difference(){
	body(width,height,depth,thickness);
	translate([0,0,-thickness]){
		body(width-thickness,height-thickness,depth-thickness);
	}
}

// gel
gel(width,height,depth,thickness);

// comb
comb(width,height,depth,thickness);
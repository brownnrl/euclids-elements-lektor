# One live figure per construction. Each entry: name -> (elements, note)
# Kept deliberately small: the smallest figure that shows what the
# construction does, with the construction's own element named last.

POINT = {
 "free":        (['A;point;free;60,60','B;point;free;180,110'], "Two integer pixel coordinates. Draggable anywhere; drawn red."),
 "fixed":       (['O;point;fixed;120,80','A;point;free;60,130'], "Two or three integer coordinates. Not draggable. Used for anchors and for off-screen construction aids."),
 "first":       (['A;point;free;50,120','B;point;free;190,60','AB;line;connect;A,B','F;point;first;AB'], "The first endpoint of a line, as an addressable point."),
 "last":        (['A;point;free;50,120','B;point;free;190,60','AB;line;connect;A,B','L;point;last;AB'], "The second endpoint."),
 "midpoint":    (['A;point;free;50,120','B;point;free;190,60','AB;line;connect;A,B','M;point;midpoint;A,B'], "Bisects the segment."),
 "intersection":(['A;point;free;40,40','B;point;free;200,130','C;point;free;40,130','D;point;free;200,40','AB;line;connect;A,B','CD;line;connect;C,D','X;point;intersection;A,B,C,D'], "The crossing of lines AB and CD. Line names expand to their endpoints, so this arrives as four points."),
 "foot":        (['B;point;free;40,140','C;point;free;210,140','A;point;free;110,40','BC;line;connect;B,C','M;point;foot;A,B,C','AM;line;connect;A,M;0;0;red'], "Foot of the perpendicular from A to line BC."),
 "extend":      (['A;point;free;50,110','B;point;free;130,110','C;point;free;50,160','D;point;free;110,160','AB;line;connect;A,B','CD;line;connect;C,D','E;point;extend;A,B,C,D','BE;line;connect;B,E;0;0;red'], "Lays |CD| off beyond B along AB. Euclid I.3."),
 "cutoff":      (['A;point;free;50,110','B;point;free;200,110','C;point;free;50,160','D;point;free;110,160','AB;line;connect;A,B','CD;line;connect;C,D','E;point;cutoff;A,B,C,D','AE;line;connect;A,E;0;0;red'], "Cuts |CD| off from A along AB. Euclid I.3."),
 "center":      (['O;point;free;120,90','P;point;free;190,90','circ;circle;radius;O,P','Z;point;center;circ'], "The centre of a circle, as an addressable point."),
 "circumcenter":(['A;point;free;70,40','B;point;free;40,140','C;point;free;200,120','ABC;polygon;triangle;A,B,C;0;0;black;0','O;point;circumcenter;A,B,C'], "Equidistant from three points. A plane may be supplied for the 3D form."),
 "lineSlider":  (['A;point;free;40,130','B;point;free;210,60','AB;line;connect;A,B','P;point;lineSlider;A,B,120,95'], "Draggable along the line only; drawn orange. The trailing integers are the initial coordinates."),
 "circleSlider":(['O;point;free;120,95','R;point;free;190,95','circ;circle;radius;O,R','P;point;circleSlider;circ,60,60'], "Draggable around the circle only."),
 "perpendicular":(['A;point;free;60,165','B;point;free;160,165','AB;line;connect;A,B','D;point;perpendicular;A,B','AD;line;connect;A,D;0;0;red'], "A point D with AD perpendicular to AB. Five signature variants determine |AD|."),
 "parallelogram":(['A;point;free;60,50','B;point;free;40,140','C;point;free;180,150','D;point;parallelogram;A,B,C','ABCD;polygon;quadrilateral;A,B,C,D;0;0;0;cyan'], "The fourth vertex, D = A + C − B."),
 "vertex":      (['A;point;free;70,135','B;point;free;155,155','sq;polygon;square;A,B;0;0;black;cyan','V;point;vertex;sq,3'], "The i-th vertex of a polygon, 1-based."),
}

LINE = {
 "connect":     (['A;point;free;50,120','B;point;free;190,60','AB;line;connect;A,B'], "The segment between two points."),
 "extend":      (['A;point;free;60,120','B;point;free;140,90','C;point;free;60,160','D;point;free;120,160','AB;line;connect;A,B','CD;line;connect;C,D','AE;line;extend;A,B,C,D;0;0;red'], "AB produced by a further |CD|."),
 "parallel":    (['A;point;free;60,140','B;point;free;200,140','P;point;free;110,60','AB;line;connect;A,B','par;line;parallel;P,A,B;0;0;red'], "Through A, parallel and equal to line BC."),
 "perpendicular":(['A;point;free;50,165','B;point;free;150,165','AB;line;connect;A,B','perp;line;perpendicular;A,B;0;0;red'], "Perpendicular to AB at A."),
 "bichord":     (['O1;point;free;80,120','R1;point;free;140,120','O2;point;free;175,70','R2;point;free;235,70','c1;circle;radius;O1,R1;0;0;black;0','c2;circle;radius;O2,R2;0;0;black;0','ch;line;bichord;c1,c2;0;0;red'], "The common chord of two circles. Takes the circle elements themselves, not their centres."),
 "chord":       (['O;point;free;120,95','R;point;free;195,95','circ;circle;radius;O,R','A;point;free;70,60','B;point;free;170,150','ch;line;chord;A,B,circ;0;0;red'], "The chord that line BC cuts from a circle."),
}

CIRCLE = {
 "radius":      (['O;point;free;120,95','P;point;free;195,95','circ;circle;radius;O,P'], "Centre and a point on the circumference. A third point sets the radius instead."),
 "circumcircle":(['A;point;free;70,40','B;point;free;40,140','C;point;free;200,130','ABC;polygon;triangle;A,B,C;0;0;black;0','circ;circle;circumcircle;A,B,C;0;0;red;0'], "Through three points. A plane may be supplied for the 3D form."),
}

SECTOR = {
 "sector":      (['V;point;free;60,150','A;point;free;200,150',
                  'varc;circle;radius;V,A;0;0;0;0',
                  'B;point;circleSlider;varc,150,55',
                  'VA;line;connect;V,A','VB;line;connect;V,B',
                  's;sector;sector;V,A,B;0;0;magenta;magenta'],
                 "The wedge at V between the arms VA and VB. Both arms must be radii of the same "
                 "circle, so B is placed on the circle through A rather than left free."),
 "angleMarker": (['V;point;free;60,150','A;point;free;200,150','B;point;free;150,50','VA;line;connect;V,A','VB;line;connect;V,B','m;sector;angleMarker;V,A,B;0;0;magenta;magenta'], "The interior angle marker at V. Radius defaults to 22px, clamped to 0.45 of the shorter arm. Markers stay hidden in a static figure unless init sets showAngles, since Euclid's own diagrams draw no angle arcs.", (260, 200), {"showAngles": True}),
 "arc":         (['A;point;free;120,120','M;point;free;200,120','B;point;free;120,45',
                  'a;sector;arc;A,M,B;0;0;red;0'],
                 "Three points ON the arc, not a centre and two ends. M lies between A and B."),
}

POLYGON = {
 "triangle":    (['A;point;free;110,40','B;point;free;40,150','C;point;free;190,150','t;polygon;triangle;A,B,C;0;0;black;cyan'], "Three vertices."),
 "quadrilateral":(['A;point;free;60,40','B;point;free;40,150','C;point;free;190,150','D;point;free;200,50','q;polygon;quadrilateral;A,B,C,D;0;0;black;cyan'], "Four vertices in order."),
 "parallelogram":(['A;point;free;60,50','B;point;free;40,150','C;point;free;180,150','p;polygon;parallelogram;A,B,C;0;0;black;cyan'], "Three vertices; the fourth is derived."),
 "square":      (['A;point;free;70,135','B;point;free;155,155','s;polygon;square;A,B;0;0;black;cyan'], "Built on the side AB. Vertex order picks which side it stands on. Euclid I.46."),
 "equilateralTriangle":(['A;point;free;70,140','B;point;free;180,140','t;polygon;equilateralTriangle;A,B;0;0;black;cyan'], "Built on the side AB. Vertex order picks the apex side. Euclid I.1."),
 "regularPolygon":(['A;point;free;105,180','B;point;free;155,180','p;polygon;regularPolygon;A,B,7;0;0;black;cyan'], "Built on the edge AB, not from a centre and radius. n is the trailing integer."),
}

# --- additions: the constructions the first pass didn't demonstrate ---------
# Signatures here follow the SOURCE (src/elements/**/Constructions.ts), not
# the reference table, which disagrees in at least one place — see the
# point;harmonic note below.

# The shared solid-geometry scaffold. A tilted base plane pinned by three
# fixed points, which everything 3D on this page slides on or builds from.
BASE3D = ['P1;point;fixed;32,195,60;0;0',
          'P2;point;fixed;205,195,60;0;0',
          'P3;point;fixed;60,85,0;0;0',
          'base;plane;3points;P1,P2,P3;0;0;lightGray;brighter']

POINT.update({
 "similar":     (['A;point;free;35,165','B;point;free;120,165','D;point;free;165,90','E;point;free;225,90','F;point;free;200,40',
                  'AB;line;connect;A,B','DE;line;connect;D,E','DF;line;connect;D,F','EF;line;connect;E,F',
                  'H;point;similar;A,B,D,E,F','AH;line;connect;A,H;0;0;red','BH;line;connect;B,H;0;0;red'],
                 "The point H for which triangle ABH is similar to DEF."),
 "proportion":  (['S0;point;free;40,35','S1;point;free;140,35','T0;point;free;40,70','T1;point;free;90,70',
                  'U0;point;free;40,105','U1;point;free;160,105','V0;point;free;40,160','V1;point;free;230,160',
                  'S;line;connect;S0,S1','T;line;connect;T0,T1','U;line;connect;U0,U1','V;line;connect;V0,V1',
                  "W;point;proportion;S0,S1,T0,T1,U0,U1,V0,V1",'VW;line;connect;V0,W;0;0;red'],
                 "Eight points. W lies on V0V1 with |S|:|T| = |U|:|V0W| — the fourth proportional, Euclid VI.12."),
 "invert":      (['O;point;free;100,100','R;point;free;170,100','circ;circle;radius;O,R',
                  'A;point;free;140,100',"A';point;invert;A,circ",'OA;line;connect;O,A;0;0;lightGray'],
                 "The image of A inverted in the circle: OA · OA' equals the radius squared."),
 "meanProportional":(['S0;point;free;40,40','S1;point;free;140,40','T0;point;free;40,80','T1;point;free;76,80',
                  'U0;point;free;40,150','U1;point;free;230,150',
                  'S;line;connect;S0,S1','T;line;connect;T0,T1','U;line;connect;U0,U1',
                  "G;point;meanProportional;S0,S1,T0,T1,U0,U1",'UG;line;connect;U0,G;0;0;red'],
                 "Six points. The geometric mean of the first two lengths, laid off along the third."),
 "planeSlider": (BASE3D + ['A;point;planeSlider;base,120,120,40'],
                 "Draggable, confined to the given plane. Three integer coordinates.", (280, 230)),
 "sphereSlider":(['O;point;free;135,115','R;point;free;205,115;0;0','a;point;free;40,40;0;0',
                  'sph;sphere;radius;O,R;0;0;black;0',
                  'X;point;sphereSlider;sph,190,70,60'],
                 "Draggable, confined to the sphere's surface.", (280, 230)),
 "angleBisector":(['A;point;free;130,35','B;point;free;35,165','C;point;free;225,165',
                  'AB;line;connect;A,B','AC;line;connect;A,C','BC;line;connect;B,C',
                  'D;point;angleBisector;B,A,C','AD;line;connect;A,D;0;0;red',
                  'm;sector;angleMarker;A,B,C;0;0;magenta;magenta'],
                 "Where the bisector of angle BAC meets BC. Argument order is B, A, C — the vertex is second. A plane may be supplied.", (260, 200), {"showAngles": True}),
 "angleDivider":(['A;point;free;130,35','B;point;free;35,165','C;point;free;225,165',
                  'AB;line;connect;A,B','AC;line;connect;A,C','BC;line;connect;B,C',
                  'D;point;angleDivider;B,A,C,3','AD;line;connect;A,D;0;0;red',
                  'm;sector;angleMarker;A,B,C;0;0;magenta;magenta'],
                 "As angleBisector, for a 1/n division; n is the trailing integer. Shown here at a third.", (260, 200), {"showAngles": True}),
 "harmonic":    (['C;point;free;30,110','D;point;free;180,110','CD;line;connect;C,D',
                  'B;point;lineSlider;C,D,150,110',"H;point;harmonic;B,C,D"],
                 "The harmonic conjugate of B with respect to C and D. Takes three points."),
})

LINE.update({
 "angleBisector":(['A;point;free;130,35','B;point;free;35,165','C;point;free;225,165',
                  'BA;line;connect;B,A','BC;line;connect;B,C',
                  'bis;line;angleBisector;A,B,C;0;0;red',
                  'm;sector;angleMarker;B,A,C;0;0;magenta;magenta'],
                 "The bisector of angle ABC as a line. The vertex is the second argument.", (260, 200), {"showAngles": True}),
 "angleDivider":(['A;point;free;130,35','B;point;free;35,165','C;point;free;225,165',
                  'BA;line;connect;B,A','BC;line;connect;B,C',
                  'div;line;angleDivider;A,B,C,3;0;0;red',
                  'm;sector;angleMarker;B,A,C;0;0;magenta;magenta'],
                 "The 1/n division of an angle, as a line.", (260, 200), {"showAngles": True}),
 "foot":        (BASE3D + ['A;point;free;150,45','f;line;foot;A,base;0;0;red'],
                 "The perpendicular from a point to a plane. Euclid XI.11.", (280, 230)),
 "similar":     (['A;point;free;35,165','B;point;free;120,165','D;point;free;165,90','E;point;free;225,90','F;point;free;200,40',
                  'AB;line;connect;A,B','DE;line;connect;D,E','DF;line;connect;D,F','EF;line;connect;E,F',
                  'AH;line;similar;A,B,D,E,F;0;0;red'],
                 "Side AH of the triangle on AB similar to DEF."),
 "proportion":  (['S0;point;free;40,35','S1;point;free;140,35','T0;point;free;40,70','T1;point;free;90,70',
                  'U0;point;free;40,105','U1;point;free;160,105','V0;point;free;40,160','V1;point;free;230,160',
                  'S;line;connect;S0,S1','T;line;connect;T0,T1','U;line;connect;U0,U1','V;line;connect;V0,V1',
                  'W;line;proportion;S0,S1,T0,T1,U0,U1,V0,V1;0;0;red'],
                 "The fourth proportional as a segment."),
 "meanProportional":(['S0;point;free;40,40','S1;point;free;140,40','T0;point;free;40,80','T1;point;free;76,80',
                  'U0;point;free;40,150','U1;point;free;230,150',
                  'S;line;connect;S0,S1','T;line;connect;T0,T1','U;line;connect;U0,U1',
                  'G;line;meanProportional;S0,S1,T0,T1,U0,U1;0;0;red'],
                 "The geometric mean as a segment."),
 "path":        (['A;point;free;25,160','B;point;free;80,55','C;point;free;150,150','D;point;free;225,50',
                  'p;line;path;A,B,C,D;0;0;red'],
                 "An open polyline through two or more points, drawn and highlighted as a single element. Does not close back to the first point."),
})

CIRCLE.update({
 "invert":      (['O;point;free;75,110','R;point;free;140,110','c1;circle;radius;O,R;0;0;black;0',
                  'P;point;free;185,55','Q;point;free;225,55','c2;circle;radius;P,Q;0;0;black;0',
                  'c3;circle;invert;c2,c1;0;0;red;0'],
                 "One circle inverted in another. The image is a circle unless the original passes through the centre of inversion."),
})

POLYGON.update({
 "similar":     (['A;point;free;30,165','B;point;free;115,165','D;point;free;165,95','E;point;free;225,95','F;point;free;200,45',
                  'DEF;polygon;triangle;D,E,F;0;0;black;pink',
                  't;polygon;similar;A,B,D,E,F;0;0;black;cyan'],
                 "The triangle on AB similar to DEF, as a fillable region."),
 "application": (['A0;point;free;45,72','B0;point;free;165,72','C0;point;free;105,28',
                  'src;polygon;triangle;A0,B0,C0;0;0;black;pink',
                  'A;point;free;60,225','B;point;free;125,225','C;point;free;90,175',
                  'p;polygon;application;src,A,B,C;0;0;black;cyan'],
                 "A parallelogram on AB, at angle CAB, equal in area to the given polygon. Euclid I.44. "
                 "Lengthening AB flattens the result, the area being fixed.", (300, 250)),
 "starPolygon": (['A;point;free;110,110','B;point;free;185,110',
                  's;polygon;starPolygon;A,B,7,3;0;0;black;cyan'],
                 "The star polygon {n/k} on edge AB. k is the density — how many vertices each edge steps over."),
 "pentagon":    (['A;point;free;125,25','B;point;free;35,90','C;point;free;70,175','D;point;free;185,175','E;point;free;215,90',
                  'p;polygon;pentagon;A,B,C,D,E;0;0;black;cyan'],
                 "Five vertices in order. No regularity assumed."),
 "hexagon":     (['A;point;free;95,25','B;point;free;30,105','C;point;free;80,180','D;point;free;175,180','E;point;free;230,105','F;point;free;180,25',
                  'h;polygon;hexagon;A,B,C,D,E,F;0;0;black;cyan'],
                 "Six vertices in order."),
 "octagon":     (['A;point;free;100,20','B;point;free;45,50','C;point;free;25,110','D;point;free;60,170',
                  'E;point;free;140,180','F;point;free;210,150','G;point;free;235,90','H;point;free;185,30',
                  'o;polygon;octagon;A,B,C,D,E,F,G,H;0;0;black;cyan'],
                 "Eight vertices in order."),
 "curvedTriangle":(['Oa;point;fixed;130,-5;0;0','Ra;point;fixed;275,-5;0;0','ca;circle;radius;Oa,Ra;0;0;0;0',
                  'Ob;point;fixed;225,160;0;0','Rb;point;fixed;370,160;0;0','cb;circle;radius;Ob,Rb;0;0;0;0',
                  'Oc;point;fixed;35,160;0;0','Rc;point;fixed;180,160;0;0','cc;circle;radius;Oc,Rc;0;0;0;0',
                  'ch1;line;bichord;cb,cc;0;0;0','ch2;line;bichord;ca,cb;0;0;0','ch3;line;bichord;ca,cc;0;0;0',
                  'A;point;first;ch1','B;point;first;ch2','C;point;last;ch3',
                  't;polygon;curvedTriangle;A,B,C,cb,ca,cc;0;0;black;cyan'],
                 "Three vertices and three side carriers. Each side is its carrier's arc clipped to the two vertices; a line carrier gives a straight side. Carriers reach the construction unexpanded."),
})

SECTOR.update({
 "angleMarkerReflex":(['V;point;free;60,150','A;point;free;200,150','B;point;free;150,50',
                  'VA;line;connect;V,A','VB;line;connect;V,B',
                  'm;sector;angleMarkerReflex;V,A,B;0;0;magenta;magenta'],
                 "As angleMarker, on the major (reflex) arc.", (260, 200), {"showAngles": True}),
})

PLANE = {
 "3points":     (BASE3D, "A plane through three points.", (280, 230)),
 "perpendicular":(BASE3D + ['O;point;planeSlider;base,120,120,40','X;point;free;185,55',
                  'OX;line;connect;O,X;0;0;lightGray',
                  'perp;plane;perpendicular;O,X;0;0;black;brighter'],
                 "The plane through O perpendicular to line OX. A plane square to a line that lies in "
                 "the base plane appears edge-on.", (280, 230)),
 "parallel":    (['P1;point;fixed;50,185,60;0;0','P2;point;fixed;175,185,60;0;0','P3;point;fixed;80,115,0;0;0',
                  'base;plane;3points;P1,P2,P3;0;0;lightGray;brighter',
                  'Q;point;free;108,92',
                  'above;plane;parallel;base,Q;0;0;black;brighter'],
                 "A plane through a point, parallel to a given plane. Euclid XI.31.", (280, 230)),
 "ambient":     (BASE3D + ['A;point;planeSlider;base,120,120,40',
                  'amb;plane;ambient;A;0;0;red;0'],
                 "The plane a point or circle already lies in. Returns that plane rather than constructing one.", (280, 230)),
}

SPHERE = {
 "radius":      (['O;point;free;130,115','P;point;free;210,115','sph;sphere;radius;O,P;0;0;black;brighter',
                  'OP;line;connect;O,P;0;0;lightGray'],
                 "Centre and one point on the surface.", (280, 230)),
}

POLYHEDRON = {
 "tetrahedron": (BASE3D + ['A;point;planeSlider;base,60,150,50','B;point;planeSlider;base,200,150,50',
                  'C;point;planeSlider;base,130,90,10','D;point;free;140,40',
                  'tet;polyhedron;tetrahedron;A,B,C,D;0;0;black;random'],
                 "Four points: a triangular base and an apex.", (280, 230)),
 "parallelepiped":(BASE3D + ['A;point;planeSlider;base,70,150,45','B;point;planeSlider;base,180,155,55',
                  'C;point;planeSlider;base,120,95,15','D;point;free;105,72',
                  'par;polyhedron;parallelepiped;A,B,C,D;0;0;black;random'],
                 "Four points: three fix the base parallelogram, the fourth gives the sweep direction.", (280, 230)),
 "prism":       (BASE3D + ['A;point;planeSlider;base,60,155,50','B;point;planeSlider;base,175,160,55',
                  'C;point;planeSlider;base,115,100,15',
                  'tri;polygon;triangle;A,B,C;0;0;black;0',
                  'S;point;planeSlider;base,110,130,30;0;0','T;point;free;130,45;0;0',
                  'pri;polyhedron;prism;tri,S,T;0;0;black;random'],
                 "A polygon base and two points giving the sweep direction. Any polygon, not only a triangle.", (280, 230)),
 "pyramid":     (BASE3D + ['A;point;planeSlider;base,55,155,50','B;point;planeSlider;base,190,160,55',
                  'C;point;planeSlider;base,150,105,20','D;point;planeSlider;base,50,100,10',
                  'quad;polygon;quadrilateral;A,B,C,D;0;0;black;0',
                  'V;point;free;125,35',
                  'pyr;polyhedron;pyramid;quad,V;0;0;black;random'],
                 "A polygon base and an apex.", (280, 230)),
}

# Prose that belongs to a whole group rather than to one card.
GROUP_NOTES = {
 "plane": "Depth is conveyed by shading rather than perspective projection. "
          "Drag the points to read a solid's shape.",
}

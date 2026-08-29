# One walkable deck per implemented animation.
# Each entry: (elements, slides_js, target, args, duration, desc, note, (w,h))

A = "geomlib.A."

ANIMS = [
 ("Point.appear", "point", "—", "350 ms",
  "Marker radius scales from zero to its final size.",
  "The plainest reveal. Used for a point the proof introduces at a crossing.",
  ['A;point;free;45,45','B;point;free;255,175','C;point;free;45,175','D;point;free;255,45',
   'AB;line;connect;A,B','CD;line;connect;C,D','X;point;intersection;A,B,C,D'],
  [('Two lines are drawn.', ['A','B','C','D','AB','CD'], [], None),
   ('The point X at which they cut.', ['A','B','C','D','AB','CD','X'], ['X'],
    [('X', 'Point.appear', None)])],
  (300, 220)),

 ("Point.slide", "lineSlider", "{ to: number } or { to: \"E\" }", "650 ms",
  "Glides a slider point along its line, its dependents following each frame.",
  "The scripted counterpart of a reader dragging the slider. A numeric target is the "
  "parameter t along AB; naming an element instead projects that element onto the line, "
  "so the point can land on a derived point and keep tracking it.",
  ['A;point;free;45,155','B;point;free;265,75','AB;line;connect;A,B',
   'P;point;lineSlider;A,B,90,130','C;point;free;150,45','PC;line;connect;P,C;0;0;red'],
  [('P slides along AB. Everything hanging off P follows.', 'ALL', ['P'], None),
   ('Glide P to t = 0.85.', 'ALL', ['P'],
    [('P', 'Point.slide', '{ to: 0.85 }')])],
  (320, 210)),

 ("Point.followPath", "point", "{ via: [...] }, { along: \"AB\" }, { arc: {...} }, { settle }", "1200 ms",
  "Moves a point along a path so the figure visibly reacts as it travels.",
  "Where Point.slide sets a slider to a value, this one is watched. The path starts at the "
  "point's current position. With settle false it retraces its steps and finishes exactly "
  "where it began, so a deck can show a construction breaking and then restore it.",
  ['A;point;free;55,175','B;point;free;265,175','AB;line;connect;A,B',
   'P;point;free;95,60','PA;line;connect;P,A','PB;line;connect;P,B'],
  [('The apex P over the base AB.', 'ALL', ['P'], None),
   ('Walk P along AB and back again.', 'ALL', ['P'],
    [('P', 'Point.followPath', '{ along: "AB" }')])],
  (320, 220)),

 ("Line.straightEdgeConnect", "line", "—", "0.25 px/ms",
  "A pencil stroke from A toward B.",
  "The canonical straightedge between two points that already exist. Short lines are held "
  "to a minimum duration so they stay perceptible.",
  ['A;point;free;50,165','B;point;free;255,60','AB;line;connect;A,B'],
  [('Two points.', ['A','B'], [], None),
   ('Join AB.', ['A','B','AB'], ['AB'], [('AB', 'Line.straightEdgeConnect', None)])],
  (300, 210)),

 ("Line.straightEdgeExtend", "line", "—", "0.25 px/ms",
  "The same trace, for a line produced beyond an existing endpoint.",
  "For Line.extend constructions, where one endpoint sits on an existing line and the "
  "other is the projected new end.",
  ['A;point;free;45,140','B;point;free;135,105','C;point;free;45,185','D;point;free;110,185',
   'AB;line;connect;A,B','CD;line;connect;C,D','AE;line;extend;A,B,C,D;0;0;red'],
  [('AB, and a length CD to add to it.', ['A','B','C','D','AB','CD'], ['CD'], None),
   ('Produce AB by a further CD.', ['A','B','C','D','AB','CD','AE'], ['AE'],
    [('AE', 'Line.straightEdgeExtend', None)])],
  (300, 220)),

 ("Circle.compass", "circle", "{ startAngle?: number }", "0.003 rad/ms",
  "Two steps: the edge sweeps a full turn, then the face fades in over it.",
  "The sweep begins where a real compass would, at the radius-defining point. A circle "
  "with no faceColor skips the second step entirely rather than waiting through it.",
  ['O;point;free;150,115','P;point;free;235,115','circ;circle;radius;O,P;0;0;black;cyan'],
  [('Centre O, radius OP.', ['O','P'], [], None),
   ('Strike the circle.', ['O','P','circ'], ['circ'], [('circ', 'Circle.compass', None)])],
  (300, 230)),

 ("Circle.compassTransfer", "circle", "{ side?: 1 | -1, keepCircles?: string[] }", "0.0055 rad/ms",
  "Euclid I.2 — copying a length to a point — as a single entry.",
  "Declared as circle;radius;P,C,D: centre P, radius the length |CD| being copied. The macro "
  "walks the rigorous I.2 construction as transient gold scaffolding, then reveals the circle "
  "and clears it. keepCircles names the construction circles that should survive as real, "
  "addressable elements for a later slide.",
  ['P;point;free;80,160','C;point;free;185,65','D;point;free;265,105','CD;line;connect;C,D',
   'cop;circle;radius;P,C,D;0;0;black;0'],
  [('The length CD, to be copied to the point P.', ['P','C','D','CD'], ['CD'], None),
   ('Lay it off at P.', ['P','C','D','CD','cop'], ['cop'],
    [('cop', 'Circle.compassTransfer', None)])],
  (330, 240)),

 ("Polygon.outline", "polygon", "—", "0.25 px/ms, min 180 ms",
  "Traces each edge in vertex order.",
  "One 0 to 1 step is partitioned across the edges, so each is drawn in sequence at its own "
  "proportion of the whole.",
  ['A;point;free;150,45','B;point;free;55,175','C;point;free;245,175',
   't;polygon;triangle;A,B,C;0;0;black;0'],
  [('Three vertices.', ['A','B','C'], [], None),
   ('Trace the edges.', ['A','B','C','t'], ['t'], [('t', 'Polygon.outline', None)])],
  (300, 220)),

 ("Polygon.outlineAndFill", "polygon", "—", "outline 0.25 px/ms, fill cap 500 ms",
  "The outline trace, then a face fade-in over it.",
  "The fill is deliberately quicker than the outline: the eye has taken the shape in from the "
  "trace already, so the colour should land promptly. A face-less polygon skips it.",
  ['A;point;free;150,45','B;point;free;55,175','C;point;free;245,175',
   't;polygon;triangle;A,B,C;0;0;black;cyan'],
  [('Three vertices.', ['A','B','C'], [], None),
   ('Outline, then fill.', ['A','B','C','t'], ['t'], [('t', 'Polygon.outlineAndFill', None)])],
  (300, 220)),

 ("Polygon.superpose", "polygon", "{ onto: string }", "translate 0.25 px/ms, hold 800 ms",
  "Euclid's superposition, as in I.4.",
  "A gold ghost copy lifts off, translates so its first vertex meets the target's, rotates to "
  "lay one side onto the other, holds a beat coinciding, then retraces its way home. The real "
  "polygon never moves. The target must have the same vertex count.",
  ['A;point;free;40,60','B;point;free;40,165','C;point;free;115,110',
   'D;point;free;190,60','E;point;free;190,165','F;point;free;265,110',
   't1;polygon;triangle;A,B,C;0;0;black;cyan','t2;polygon;triangle;D,E,F;0;0;black;pink'],
  [('Two triangles, claimed equal.', 'ALL', ['t1','t2'], None),
   ('Apply the one to the other.', 'ALL', ['t1'],
    [('t1', 'Polygon.superpose', '{ onto: "t2" }')])],
  (320, 220)),

 ("Polygon.equilateralBuild", "polygon", "—", "0.0045 rad/ms, fill cap 500 ms",
  "Euclid I.1 as a single entry.",
  "Two gold compass circles sweep out, the triangle outlines and fills, and the circles clear "
  "as it lands. The apex follows whichever side the declared triangle chose, so A,B and B,A "
  "give mirror results.",
  ['A;point;free;115,150','B;point;free;185,150',
   't;polygon;equilateralTriangle;A,B;0;0;black;cyan'],
  [('A given finite straight line.', ['A','B'], [], None),
   ('Build the equilateral triangle on it.', ['A','B','t'], ['t'],
    [('t', 'Polygon.equilateralBuild', None)])],
  (300, 230)),

 ("Sector.sweep", "sector", "—", "0.003 rad/ms, min 250 ms",
  "The arc grows from one arm toward the other.",
  "The angle-marker reveal. A sector with a face sweeps and then fills; one without skips the "
  "fill. A sector with no colours at all renders in the gold emphasis stroke while animating, "
  "which is the invisible angle-marker pattern.",
  ['V;point;free;55,175','A;point;free;265,175','B;point;free;190,55',
   'VA;line;connect;V,A','VB;line;connect;V,B',
   'm;sector;angleMarker;V,A,B;0;0;magenta;magenta'],
  [('The angle at V.', ['V','A','B','VA','VB'], [], None),
   ('Mark it.', ['V','A','B','VA','VB','m'], ['m'], [('m', 'Sector.sweep', None)])],
  (320, 220)),

 ("Group.cloneAside", "any", "{ include?, vary?, dx?, dy?, autoPlace?, variants? }",
  "0.4 px/ms, min 200 ms",
  "Clones part of the figure into displaced copies that slide aside and stay for the slide.",
  "The real figure never moves. vary can set a slider before the snapshot is taken, so a copy "
  "shows a different case — which is how a trichotomy argument gets all three cases on screen "
  "at once. autoPlace centres the figure first and lays the copies in the freed space.",
  ['A;point;free;50,155','B;point;free;125,155','C;point;free;90,80',
   't;polygon;triangle;A,B,C;0;0;black;cyan'],
  [('One triangle.', 'ALL', ['t'], None),
   ('Set a copy beside it.', 'ALL', ['t'],
    [('t', 'Group.cloneAside', '{ include: "all", dx: 130, dy: 0 }')])],
  (330, 220)),

 ("instant", "any", "—", "0 ms",
  "A no-op finalise: the element arrives with no motion.",
  "Used on a slide entry to suppress an animation that would otherwise be inherited, and "
  "fired automatically when a name lookup fails, with one console warning per name. Below, "
  "AB is drawn and CD simply appears.",
  ['A;point;free;45,60','B;point;free;145,175','C;point;free;185,60','D;point;free;285,175',
   'AB;line;connect;A,B','CD;line;connect;C,D'],
  [('Two pairs of points.', ['A','B','C','D'], [], None),
   ('AB is drawn; CD is not.', ['A','B','C','D','AB','CD'], ['AB','CD'],
    [('AB', 'Line.straightEdgeConnect', None), ('CD', 'instant', None)])],
  (330, 220)),
]

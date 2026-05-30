// Euclid's Elements javascripts by D. Joyce, Clark University
//
// booktable is a list of the 13 books
//   first the subdirectory, then the Book name
//

// Inject a viewport meta tag at script-load time so phone browsers
// don't render at desktop width. This runs in <head> (the script tag
// is in <head>), before the body is laid out. Run-once guard avoids
// double-injecting on pages that already declare viewport. No
// maximum-scale cap — that's an accessibility anti-pattern (blocks
// pinch-zoom for low-vision users).
(function () {
    if (!document.querySelector('meta[name="viewport"]')) {
        var meta = document.createElement("meta");
        meta.name = "viewport";
        meta.content = "width=device-width, initial-scale=1.0";
        document.head.appendChild(meta);
    }
})();


var booktable=[
    ["bookI","Book I"],
    ["bookII","Book II"],
    ["bookIII","Book III"],
    ["bookIV","Book IV"],
    ["bookV","Book V"],
    ["bookVI","Book VI"],
    ["bookVII","Book VII"],
    ["bookVIII","Book VIII"],
    ["bookIX","Book IX"],
    ["bookX","Book X"],
    ["bookXI","Book XI"],
    ["bookXII","Book XII"],
    ["bookXIII","Book XIII"]];
// proptable is a array of all the definitions and propositions in the 13 subdirectories
//   first the filename, then the title. 
//
var proptable=[
  [ /* first book */
    ["defI1.html","I.Def.1"],
    ["defI2.html","I.Def.2"],
    ["defI3.html","I.Def.3"],
    ["defI4.html","I.Def.4"],
    ["defI5.html","I.Def.5"],
    ["defI6.html","I.Def.6"],
    ["defI7.html","I.Def.7"],
    ["defI8.html","I.Def.8"],
    ["defI9.html","I.Def.9"],
    ["defI10.html","I.Def.10"],    
    ["defI11.html","I.Def.11-12"],
    ["defI13.html","I.Def.13-14"],
    ["defI15.html","I.Def.15-18"],
    ["defI19.html","I.Def.19"],
    ["defI20.html","I.Def.21"],
    ["defI22.html","I.Def.22"],
    ["defI23.html","I.Def.23"],
    ["cn.html","Common Notions"],
    ["post1.html","I.Post.1"],
    ["post2.html","I.Post.2"],
    ["post3.html","I.Post.3"],
    ["post4.html","I.Post.4"],
    ["post5.html","I.Post.5"],
    ["propI1.html","I.1"],
    ["propI2.html","I.2"],
    ["propI3.html","I.3"],
    ["propI4.html","I.4"],
    ["propI5.html","I.5"],
    ["propI6.html","I.6"],
    ["propI7.html","I.7"],
    ["propI8.html","I.8"],
    ["propI9.html","I.9"],
    ["propI10.html","I.10"],
    ["propI11.html","I.11"],
    ["propI12.html","I.12"],
    ["propI13.html","I.13"],
    ["propI14.html","I.14"],
    ["propI15.html","I.15"],
    ["propI16.html","I.16"],
    ["propI17.html","I.17"],
    ["propI18.html","I.18"],
    ["propI19.html","I.19"],
    ["propI20.html","I.20"],
    ["propI21.html","I.21"],
    ["propI22.html","I.22"],
    ["propI23.html","I.23"],
    ["propI24.html","I.24"],
    ["propI25.html","I.25"],
    ["propI26.html","I.26"],
    ["propI27.html","I.27"],
    ["propI28.html","I.28"],
    ["propI29.html","I.29"],
    ["propI30.html","I.30"],
    ["propI31.html","I.31"],
    ["propI32.html","I.32"],
    ["propI33.html","I.33"],
    ["propI34.html","I.34"],
    ["propI35.html","I.35"],
    ["propI36.html","I.36"],
    ["propI37.html","I.37"],
    ["propI38.html","I.38"],
    ["propI39.html","I.39"],
    ["propI40.html","I.40"],
    ["propI41.html","I.41"],
    ["propI42.html","I.42"],
    ["propI43.html","I.43"],
    ["propI44.html","I.44"],
    ["propI45.html","I.45"],
    ["propI46.html","I.46"],
    ["propI47.html","I.47"],
    ["propI48.html","I.48"]],
  [ /* second book */
    ["defII.html","II.Def.1-2"],
    ["propII1.html","II.1"],
    ["propII2.html","II.2"],
    ["propII3.html","II.3"],
    ["propII4.html","II.4"],
    ["propII5.html","II.5"],
    ["propII6.html","II.6"],
    ["propII7.html","II.7"],
    ["propII8.html","II.8"],
    ["propII9.html","II.9"],
    ["propII10.html","II.10"],
    ["propII11.html","II.11"],
    ["propII12.html","II.12"],
    ["propII13.html","II.13"],
    ["propII14.html","II.14"]],
  [ /* third book */
    ["defIII1.html","III.Def.1"],
    ["defIII2.html","III.Def.2-3"],
    ["defIII4.html","III.Def.4-5"],
    ["defIII6.html","III.Def.6-9"],
    ["defIII10.html","III.Def.10"],    
    ["defIII11.html","III.Def.11"],
    ["propIII1.html","III.1"],
    ["propIII2.html","III.2"],
    ["propIII3.html","III.3"],
    ["propIII4.html","III.4"],
    ["propIII5.html","III.5"],
    ["propIII6.html","III.6"],
    ["propIII7.html","III.7"],
    ["propIII8.html","III.8"],
    ["propIII9.html","III.9"],
    ["propIII10.html","III.10"],
    ["propIII11.html","III.11"],
    ["propIII12.html","III.12"],
    ["propIII13.html","III.13"],
    ["propIII14.html","III.14"],
    ["propIII15.html","III.15"],
    ["propIII16.html","III.16"],
    ["propIII17.html","III.17"],
    ["propIII18.html","III.18"],
    ["propIII19.html","III.19"],
    ["propIII20.html","III.20"],
    ["propIII21.html","III.21"],
    ["propIII22.html","III.22"],
    ["propIII23.html","III.23"],
    ["propIII24.html","III.24"],
    ["propIII25.html","III.25"],
    ["propIII26.html","III.26"],
    ["propIII27.html","III.27"],
    ["propIII28.html","III.28"],
    ["propIII29.html","III.29"],
    ["propIII30.html","III.30"],
    ["propIII31.html","III.31"],
    ["propIII32.html","III.32"],
    ["propIII33.html","III.33"],
    ["propIII34.html","III.34"],
    ["propIII35.html","III.35"],
    ["propIII36.html","III.36"],
    ["propIII37.html","III.37"]],
  [ /* fourth book */
    ["defIV.html","IV.Def.1-7"],
    ["propIV1.html","IV.1"],
    ["propIV2.html","IV.2"],
    ["propIV3.html","IV.3"],
    ["propIV4.html","IV.4"],
    ["propIV5.html","IV.5"],
    ["propIV6.html","IV.6"],
    ["propIV7.html","IV.7"],
    ["propIV8.html","IV.8"],
    ["propIV9.html","IV.9"],
    ["propIV10.html","IV.10"],
    ["propIV11.html","IV.11"],
    ["propIV12.html","IV.12"],
    ["propIV13.html","IV.13"],
    ["propIV14.html","IV.14"],
    ["propIV15.html","IV.15"],
    ["propIV16.html","IV.16"]],
  [ /* fifth book */
    ["defV1.html","V.Def.1-2"],
    ["defV3.html","V.Def.3"],
    ["defV4.html","V.Def.4"],
    ["defV5.html","V.Def.5-6"],
    ["defV7.html","V.Def.7"],
    ["defV8.html","V.Def.8-10"],
    ["defV11.html","V.Def.11-13"],
    ["defV14.html","V.Def.14-16"],
    ["defV17.html","V.Def.17-18"],
    ["propV1.html","V.1"],
    ["propV2.html","V.2"],
    ["propV3.html","V.3"],
    ["propV4.html","V.4"],
    ["propV5.html","V.5"],
    ["propV6.html","V.6"],
    ["propV7.html","V.7"],
    ["propV8.html","V.8"],
    ["propV9.html","V.9"],
    ["propV10.html","V.10"],
    ["propV11.html","V.11"],
    ["propV12.html","V.12"],
    ["propV13.html","V.13"],
    ["propV14.html","V.14"],
    ["propV15.html","V.15"],
    ["propV16.html","V.16"],
    ["propV17.html","V.17"],
    ["propV18.html","V.18"],
    ["propV19.html","V.19"],
    ["propV20.html","V.20"],
    ["propV21.html","V.21"],
    ["propV22.html","V.22"],
    ["propV23.html","V.23"],
    ["propV24.html","V.24"],
    ["propV25.html","V.25"]],
  [ /* sixth book */
    ["defVI1.html","VI.Def.1"],
    ["defVI2.html","VI.Def.2"],
    ["defVI3.html","VI.Def.3"],
    ["defVI4.html","VI.Def.4"],
    ["propVI1.html","VI.1"],
    ["propVI2.html","VI.2"],
    ["propVI3.html","VI.3"],
    ["propVI4.html","VI.4"],
    ["propVI5.html","VI.5"],
    ["propVI6.html","VI.6"],
    ["propVI7.html","VI.7"],
    ["propVI8.html","VI.8"],
    ["propVI9.html","VI.9"],
    ["propVI10.html","VI.10"],
    ["propVI11.html","VI.11"],
    ["propVI12.html","VI.12"],
    ["propVI13.html","VI.13"],
    ["propVI14.html","VI.14"],
    ["propVI15.html","VI.15"],
    ["propVI16.html","VI.16"],
    ["propVI17.html","VI.17"],
    ["propVI18.html","VI.18"],
    ["propVI19.html","VI.19"],
    ["propVI20.html","VI.20"],
    ["propVI21.html","VI.21"],
    ["propVI22.html","VI.22"],
    ["propVI23.html","VI.23"],
    ["propVI24.html","VI.24"],
    ["propVI25.html","VI.25"],
    ["propVI26.html","VI.26"],
    ["propVI27.html","VI.27"],
    ["propVI28.html","VI.28"],
    ["propVI29.html","VI.29"],
    ["propVI30.html","VI.30"],
    ["propVI31.html","VI.31"],
    ["propVI32.html","VI.32"],
    ["propVI33.html","VI.33"]],
  [ /* seventh book */
    ["defVII1.html","VII.Def.1-2"],
    ["defVII3.html","VII.Def.3-5"],
    ["defVII6.html","VII.Def.6-10"],  
    ["defVII11.html","VII.Def.11-14"],
    ["defVII15.html","VII.Def.15-19"],
    ["defVII20.html","VII.Def.20"],
    ["defVII21.html","VII.Def.21"],
    ["defVII22.html","VII.Def.22"],
    ["propVII1.html","VII.1"],
    ["propVII2.html","VII.2"],
    ["propVII3.html","VII.3"],
    ["propVII4.html","VII.4"],
    ["propVII5.html","VII.5"],
    ["propVII6.html","VII.6"],
    ["propVII7.html","VII.7"],
    ["propVII8.html","VII.8"],
    ["propVII9.html","VII.9"],
    ["propVII10.html","VII.10"],
    ["propVII11.html","VII.11"],
    ["propVII12.html","VII.12"],
    ["propVII13.html","VII.13"],
    ["propVII14.html","VII.14"],
    ["propVII15.html","VII.15"],
    ["propVII16.html","VII.16"],
    ["propVII17.html","VII.17"],
    ["propVII18.html","VII.18"],
    ["propVII19.html","VII.19"],
    ["propVII20.html","VII.20"],
    ["propVII21.html","VII.21"],
    ["propVII22.html","VII.22"],
    ["propVII23.html","VII.23"],
    ["propVII24.html","VII.24"],
    ["propVII25.html","VII.25"],
    ["propVII26.html","VII.26"],
    ["propVII27.html","VII.27"],
    ["propVII28.html","VII.28"],
    ["propVII29.html","VII.29"],
    ["propVII30.html","VII.30"],
    ["propVII31.html","VII.31"],
    ["propVII32.html","VII.32"],
    ["propVII33.html","VII.33"],
    ["propVII34.html","VII.34"],
    ["propVII35.html","VII.35"],
    ["propVII36.html","VII.36"],
    ["propVII37.html","VII.37"],
    ["propVII38.html","VII.38"],
    ["propVII39.html","VII.39"]],
  [ /* eighth book */
    ["propVIII1.html","VIII.1"],
    ["propVIII2.html","VIII.2"],
    ["propVIII3.html","VIII.3"],
    ["propVIII4.html","VIII.4"],
    ["propVIII5.html","VIII.5"],
    ["propVIII6.html","VIII.6"],
    ["propVIII7.html","VIII.7"],
    ["propVIII8.html","VIII.8"],
    ["propVIII9.html","VIII.9"],
    ["propVIII10.html","VIII.10"],
    ["propVIII11.html","VIII.11"],
    ["propVIII12.html","VIII.12"],
    ["propVIII13.html","VIII.13"],
    ["propVIII14.html","VIII.14"],
    ["propVIII15.html","VIII.15"],
    ["propVIII16.html","VIII.16"],
    ["propVIII17.html","VIII.17"],
    ["propVIII18.html","VIII.18"],
    ["propVIII19.html","VIII.19"],
    ["propVIII20.html","VIII.20"],
    ["propVIII21.html","VIII.21"],
    ["propVIII22.html","VIII.22"],
    ["propVIII23.html","VIII.23"],
    ["propVIII24.html","VIII.24"],
    ["propVIII25.html","VIII.25"],
    ["propVIII26.html","VIII.26"],
    ["propVIII27.html","VIII.27"]],
  [ /* ninth book */
    ["propIX1.html","IX.1"],
    ["propIX2.html","IX.2"],
    ["propIX3.html","IX.3"],
    ["propIX4.html","IX.4"],
    ["propIX5.html","IX.5"],
    ["propIX6.html","IX.6"],
    ["propIX7.html","IX.7"],
    ["propIX8.html","IX.8"],
    ["propIX9.html","IX.9"],
    ["propIX10.html","IX.10"],
    ["propIX11.html","IX.11"],
    ["propIX12.html","IX.12"],
    ["propIX13.html","IX.13"],
    ["propIX14.html","IX.14"],
    ["propIX15.html","IX.15"],
    ["propIX16.html","IX.16"],
    ["propIX17.html","IX.17"],
    ["propIX18.html","IX.18"],
    ["propIX19.html","IX.19"],
    ["propIX20.html","IX.20"],
    ["propIX21.html","IX.21"],
    ["propIX22.html","IX.22"],
    ["propIX23.html","IX.23"],
    ["propIX24.html","IX.24"],
    ["propIX25.html","IX.25"],
    ["propIX26.html","IX.26"],
    ["propIX27.html","IX.27"],
    ["propIX28.html","IX.28"],
    ["propIX29.html","IX.29"],
    ["propIX30.html","IX.30"],
    ["propIX31.html","IX.31"],
    ["propIX32.html","IX.32"],
    ["propIX33.html","IX.33"],
    ["propIX34.html","IX.34"],
    ["propIX35.html","IX.35"],
    ["propIX36.html","IX.36"]],
  [ /* tenth book */
    ["defX.I.html","X.Def.I"],
    ["propX1.html","X.1"],
    ["propX2.html","X.2"],
    ["propX3.html","X.3"],
    ["propX4.html","X.4"],
    ["propX5.html","X.5"],
    ["propX6.html","X.6"],
    ["propX7.html","X.7"],
    ["propX8.html","X.8"],
    ["propX9.html","X.9"],
    ["propX10.html","X.10"],
    ["propX11.html","X.11"],
    ["propX12.html","X.12"],
    ["propX13.html","X.13"],
    ["propX14.html","X.14"],
    ["propX15.html","X.15"],
    ["propX16.html","X.16"],
    ["propX17.html","X.17"],
    ["propX18.html","X.18"],
    ["propX19.html","X.19"],
    ["propX20.html","X.20"],
    ["propX21.html","X.21"],
    ["propX22.html","X.22"],
    ["propX23.html","X.23"],
    ["propX24.html","X.24"],
    ["propX25.html","X.25"],
    ["propX26.html","X.26"],
    ["propX27.html","X.27"],
    ["propX28.html","X.28"],
    ["propX29.html","X.29"],
    ["propX30.html","X.30"],
    ["propX31.html","X.31"],
    ["propX32.html","X.32"],
    ["propX33.html","X.33"],
    ["propX34.html","X.34"],
    ["propX35.html","X.35"],
    ["propX36.html","X.36"],
    ["propX37.html","X.37"],
    ["propX38.html","X.38"],
    ["propX39.html","X.39"],
    ["propX40.html","X.40"],
    ["propX41.html","X.41"],
    ["propX42.html","X.42"],
    ["propX43.html","X.43"],
    ["propX44.html","X.44"],
    ["propX45.html","X.45"],
    ["propX46.html","X.46"],
    ["propX47.html","X.47"],
    ["defX.II.html","X.Def.II"],
    ["propX48.html","X.48"],
    ["propX49.html","X.49"],
    ["propX50.html","X.50"],
    ["propX51.html","X.51"],
    ["propX52.html","X.52"],
    ["propX53.html","X.53"],
    ["propX54.html","X.54"],
    ["propX55.html","X.55"],
    ["propX56.html","X.56"],
    ["propX57.html","X.57"],
    ["propX58.html","X.58"],
    ["propX59.html","X.59"],
    ["propX60.html","X.60"],
    ["propX61.html","X.61"],
    ["propX62.html","X.62"],
    ["propX63.html","X.63"],
    ["propX64.html","X.64"],
    ["propX65.html","X.65"],
    ["propX66.html","X.66"],
    ["propX67.html","X.67"],
    ["propX68.html","X.68"],
    ["propX69.html","X.69"],
    ["propX70.html","X.70"],
    ["propX71.html","X.71"],
    ["propX72.html","X.72"],
    ["propX73.html","X.73"],
    ["propX74.html","X.74"],
    ["propX75.html","X.75"],
    ["propX76.html","X.76"],
    ["propX77.html","X.77"],
    ["propX78.html","X.78"],
    ["propX79.html","X.79"],
    ["propX80.html","X.80"],
    ["propX81.html","X.81"],
    ["propX82.html","X.82"],
    ["propX83.html","X.83"],
    ["propX84.html","X.84"],
    ["defX.III.html","X.Def.III"],
    ["propX85.html","X.85"],
    ["propX86.html","X.86"],
    ["propX87.html","X.87"],
    ["propX88.html","X.88"],
    ["propX89.html","X.89"],
    ["propX90.html","X.90"],
    ["propX91.html","X.91"],
    ["propX92.html","X.92"],
    ["propX93.html","X.93"],
    ["propX94.html","X.94"],
    ["propX95.html","X.95"],
    ["propX96.html","X.96"],
    ["propX97.html","X.97"],
    ["propX98.html","X.98"],
    ["propX99.html","X.99"],
    ["propX100.html","X.100"],
    ["propX101.html","X.101"],
    ["propX102.html","X.102"],
    ["propX103.html","X.103"],
    ["propX104.html","X.104"],
    ["propX105.html","X.105"],
    ["propX106.html","X.106"],
    ["propX107.html","X.107"],
    ["propX108.html","X.108"],
    ["propX109.html","X.109"],
    ["propX110.html","X.110"],
    ["propX111.html","X.111"],
    ["propX112.html","X.112"],
    ["propX113.html","X.113"],
    ["propX114.html","X.114"],
    ["propX115.html","X.115"]],
  [ /* eleventh book */
    ["defXI1.html","XI.Def.1-2"],
    ["defXI3.html","XI.Def.3-5"],
    ["defXI6.html","XI.Def.6-8"],
    ["defXI9.html","XI.Def.9-10"],
    ["defXI11.html","XI.Def.11"],    
    ["defXI12.html","XI.Def.12-13"],    
    ["defXI14.html","XI.Def.14-17"],    
    ["defXI18.html","XI.Def.18-20"],    
    ["defXI21.html","XI.Def.21-23"],    
    ["defXI24.html","XI.Def.24"],    
    ["defXI25.html","XI.Def.15-28"],
    ["propXI1.html","XI.1"],
    ["propXI2.html","XI.2"],
    ["propXI3.html","XI.3"],
    ["propXI4.html","XI.4"],
    ["propXI5.html","XI.5"],
    ["propXI6.html","XI.6"],
    ["propXI7.html","XI.7"],
    ["propXI8.html","XI.8"],
    ["propXI9.html","XI.9"],
    ["propXI10.html","XI.10"],
    ["propXI11.html","XI.11"],
    ["propXI12.html","XI.12"],
    ["propXI13.html","XI.13"],
    ["propXI14.html","XI.14"],
    ["propXI15.html","XI.15"],
    ["propXI16.html","XI.16"],
    ["propXI17.html","XI.17"],
    ["propXI18.html","XI.18"],
    ["propXI19.html","XI.19"],
    ["propXI20.html","XI.20"],
    ["propXI21.html","XI.21"],
    ["propXI22.html","XI.22"],
    ["propXI23.html","XI.23"],
    ["propXI24.html","XI.24"],
    ["propXI25.html","XI.25"],
    ["propXI26.html","XI.26"],
    ["propXI27.html","XI.27"],
    ["propXI28.html","XI.28"],
    ["propXI29.html","XI.29"],
    ["propXI30.html","XI.30"],
    ["propXI31.html","XI.31"],
    ["propXI32.html","XI.32"],
    ["propXI33.html","XI.33"],
    ["propXI34.html","XI.34"],
    ["propXI35.html","XI.35"],
    ["propXI36.html","XI.36"],
    ["propXI37.html","XI.37"],
    ["propXI38.html","XI.38"],
    ["propXI39.html","XI.39"]],
  [ /* twelfth book */
    ["propXII1.html","XII.1"],
    ["propXII2.html","XII.2"],
    ["propXII3.html","XII.3"],
    ["propXII4.html","XII.4"],
    ["propXII5.html","XII.5"],
    ["propXII6.html","XII.6"],
    ["propXII7.html","XII.7"],
    ["propXII8.html","XII.8"],
    ["propXII9.html","XII.9"],
    ["propXII10.html","XII.10"],
    ["propXII11.html","XII.11"],
    ["propXII12.html","XII.12"],
    ["propXII13.html","XII.13"],
    ["propXII14.html","XII.14"],
    ["propXII15.html","XII.15"],
    ["propXII16.html","XII.16"],
    ["propXII17.html","XII.17"],
    ["propXII18.html","XII.18"]],
  [ /* thirteenth book */
    ["propXIII1.html","XIII.1"],
    ["propXIII2.html","XIII.2"],
    ["propXIII3.html","XIII.3"],
    ["propXIII4.html","XIII.4"],
    ["propXIII5.html","XIII.5"],
    ["propXIII6.html","XIII.6"],
    ["propXIII7.html","XIII.7"],
    ["propXIII8.html","XIII.8"],
    ["propXIII9.html","XIII.9"],
    ["propXIII10.html","XIII.10"],
    ["propXIII11.html","XIII.11"],
    ["propXIII12.html","XIII.12"],
    ["propXIII13.html","XIII.13"],
    ["propXIII14.html","XIII.14"],
    ["propXIII15.html","XIII.15"],
    ["propXIII16.html","XIII.16"],
    ["propXIII17.html","XIII.17"],
    ["propXIII18.html","XIII.18"]]]

//
// Find the current book number based on the URL
// it's needed to access the prop
//
function getbook() {
  var pathArray = window.location.pathname.split( '/' );
  var fn = pathArray[pathArray.length-2];
  var fi = -1; // return -1 if it's not in a book subdirectory
  for(bookitem in booktable) {
    if (booktable[bookitem][0] == fn)
      fi=bookitem;
  }
  return fi;
};
//
// Find the current prop number based on the URL
// it's needed to access the next and previous props
//
function getprop(book) { // pass the correct book as found in getbook
  if (book == -1) return -1; // not in s subdirectory
  var pathArray = window.location.pathname.split( '/' );
  var fn = pathArray[pathArray.length-1];
  var fi = -1; // return -1 if it's not a prop page
  for(propitem in proptable[book]){
    if (proptable[book][propitem][0] == fn)
      fi=propitem;
  }
  return fi;
}
//
// Prepare a link to the book
//
function getBookLink(book) {
  if (book < 0 || book >= booktable.length)
    return '<a href="/">Introduction</a>';
  var str = '<a href="../'+booktable[book][0]+'/'+booktable[book][0]+'.html">';
  str += booktable[book][1]+"</a>";
  return str;
}
//
// Prepare a link to the first page in the book
//
function getFirstPageLink(book) {
  var str = 'First page: <a href="../'+booktable[book][0];
  str += '/'+proptable[book][0][0]+'">';
  str += proptable[book][0][1]+"</a>";
  return str;
}
//
// Prepare a link to the next proposition
//
function getNextProp(book,prop){
  if (book == -1) // not in a subdirectory so no next prop
    return "";
  if (prop == -1) { // not a prop, assume it's the book page, return the first prop
    var nextPropString = "Next: ";
    nextPropString += '<a href="../'+booktable[book][0];
    nextPropString += '/'+proptable[book][0][0]+'">';
    nextPropString += proptable[book][0][1]+"</a>";
    return nextPropString;
  }
  if (prop < proptable[book].length-1) { // not the last prop in the book
    ++prop;
    var nextPropString = "Next: ";
    nextPropString += '<a href="'+proptable[book][prop][0]+'">'
    nextPropString += proptable[book][prop][1]+"</a>";
    return nextPropString;
  }
  if (book < booktable.length-1) { // return the first prop of the next book
    ++book;
    var nextPropString = "Next: ";
    nextPropString += '<a href="../'+booktable[book][0];
    nextPropString += '/'+proptable[book][0][0]+'">';
    nextPropString += proptable[book][0][1]+"</a>";
    return nextPropString;
  }
  // last prop in last book
  return "";
}
//
// Prepare a link to the previous proposition
//
function getPreviousProp(book,prop){
  if (book == -1) // not in a subdirectory so no next prop
    return "";
  if (prop == -1 && book == 0) // book I page
    return "";
  if (prop == -1) { 
    // return previous book page
    --book;
    var previousPropString = "Previous: ";
    previousPropString += '<a href="../'+booktable[book][0];
    previousPropString += '/'+proptable[book][0][0]+'">';
    previousPropString += proptable[book][0][1]+"</a>";
    return previousPropString;
  } 
  if (prop != 0) { // not the first prop in the book
    --prop;
    var previousPropString = "Previous: ";
    previousPropString += '<a href="'+proptable[book][prop][0]+'">';
    previousPropString += proptable[book][prop][1]+"</a>";
    return previousPropString;
  }
  if (book != 0) { // return the last prop of the previous book
    --book;
    prop = proptable[book].length-1;
    var previousPropString = "Previous: ";
    previousPropString += '<a href="../'+booktable[book][0];
    previousPropString += '/'+proptable[book][prop][0]+'">';
    previousPropString += proptable[book][prop][1]+"</a>";
    return previousPropString;
  }
  // first prop in first book
  return ""; // no previous prop
}
//
// Prepare a form for selecting a proposition in the book
//
function getPropForm(book) {
  var formString = '<form name="PropForm">';
  formString += '<select name="select1" size="1" onchange="if (options[selectedIndex].value){ location = options[selectedIndex].value }">';
  formString += '<option value="">Select from '+booktable[book][1];
  formString += '<option value="'+booktable[book][0]+'.html">'+booktable[book][1]+' intro';
  for(propitem in proptable[book]){
    formString += '<option value="';
    formString += proptable[book][propitem][0]+'">';
    formString += proptable[book][propitem][1];
  }
  formString += '</select></form>';
  return formString;
}
//
// Prepare a form for selecting a book
//
function getBookForm(prefix) { // prefix is either empty or "../"
  var formString = '<form name="BookForm">';
  formString += '<select name="select2" size="1" onchange="if (options[selectedIndex].value){ location = options[selectedIndex].value }">';
  formString += '<option value="">Select book';
  for(bookitem in booktable){
    formString += '<option value="';
    formString += prefix+booktable[bookitem][0]+"/"+booktable[bookitem][0]+'.html">';
    formString += booktable[bookitem][1];
  }
  formString += '</select></form>';
  return formString;
}
//
// Prepare a form for selecting among the topics
//
function getTopicForm(prefix) { // prefix is either empty or "../"
  var formString = '<form name="TopicForm">';
  formString += '<select name="select3" size="1" onchange="if (options[selectedIndex].value){ location = options[selectedIndex].value }">';
  formString += '<option value="">Select topic';
  formString += '<option value="/">Introduction';
  formString += '<option value="/elements/">Table of Contents';
  formString += '<option value="/geomlib/usingGeomlib.html">Using geomlib';
  formString += '<option value="'+prefix+'aboutText.html">About the text';
  formString += '<option value="'+prefix+'Euclid.html">Euclid';
  formString += '<option value="'+prefix+'web.html">Web references';
  formString += '<option value="'+prefix+'trip.html">A quick trip';
  formString += '<option value="'+prefix+'subjindex.html">Subject index';
  formString += '</select></form>';
  return formString;
}
//
// The header for each proposition page
//
function loadHeader(){
  var book = getbook();
  var prfx = (book == -1)? "" : "../";
  var prop = getprop(book);
  var headertext = "";
  if (book == -1) { // This is a page in the main directory
    headertext += getEuclidLogoMap(prfx);
  } else if (prop == -1) { // This is a book introduction page
    headertext += getEuclidLogoMap(prfx);
    headertext += "<h1>"+booktable[book][1]+"</h1>";  
  } else { // This is a proposition
    headertext += '<a class="hover" href="/">';
    headertext += "<h1>Euclid's Elements</h1></a>";
    headertext += '<a class="hover" href="'+booktable[book][0]+'.html">';
    headertext += "<h1>"+booktable[book][1]+"</h1></a>";  
  }
  document.getElementById("header").innerHTML = headertext;
}
// 
// Euclid logo map
//
function getEuclidLogoMap(prfx) { // prfx kept for back-compat; URLs are absolute
  var txt = "<center>";
  txt += '<img src="/elements/logo.gif" USEMAP="#tocmap" alt="';
  txt += "Euclid's Elements";
  txt += '" height=238 width=245 border=0>';
  txt +=  "</center>";
  txt +=  '<MAP NAME="tocmap">';
  txt +=  '<AREA SHAPE="RECT" COORDS="59,88,193,164"   HREF="/elements/">';
  txt +=  '<AREA SHAPE="RECT" COORDS="160,10,188,31"   HREF="/elements/bookI/bookI.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="194,34,215,70"   HREF="/elements/bookII/bookII.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="215,73,243,98"   HREF="/elements/bookIII/bookIII.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="217,118,242,139" HREF="/elements/bookIV/bookIV.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="208,163,231,185" HREF="/elements/bookV/bookV.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="176,199,203,219" HREF="/elements/bookVI/bookVI.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="134,215,172,236" HREF="/elements/bookVII/bookVII.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="74,215,115,236"  HREF="/elements/bookVIII/bookVIII.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="44,197,72,218"   HREF="/elements/bookIX/bookIX.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="16,163,44,183"   HREF="/elements/bookX/bookX.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="0,121,31,140"    HREF="/elements/bookXI/bookXI.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="0,78,36,98"      HREF="/elements/bookXII/bookXII.html">';
  txt +=  '<AREA SHAPE="RECT" COORDS="10,32,57,54"     HREF="/elements/bookXIII/bookXIII.html">';
  txt +=  "</MAP>";
  return txt;
}
//
// The footer for each chapter page
//
function loadFooter(copyrightDates){
  //
  // There are small variants depending on the page
  //   1. Different pages have different copyrightDates
  //   2. Links to the next and previous pages depend on the page
  //
  var footerText = "";
  var book = getbook();
  var prfx = (book == -1)? "" : "../";
  var prop = getprop(book);
  footerText += "<br><p><hr size=6><p><center>";
  // build the table of links
  footerText += "<table><tr valign=top>";
  if (book == -1) {// This is a page in the main directory
    footerText += "<td>"+getTopicForm(prfx)+"</td><td>&nbsp;</td>";
    footerText += "<td>"+getBookForm(prfx)+"</td></tr>";
  } else if (prop == -1) { // this is the book introduction page
    footerText += "<td>"+getFirstPageLink(book)+" &nbsp; &nbsp; &nbsp; &nbsp;</td> ";
    footerText += "<td>"+getPropForm(book)+"</td></tr>";
    footerText += "<tr valign=top><td>Next: "+getBookLink(book-1+2)+"</td>";
    footerText += "<td>"+getBookForm(prfx)+"</td></tr>";
    footerText += "<tr valign=top><td>Previous: "+getBookLink(book-1)+"</td>";
    footerText += "<td>"+getTopicForm(prfx)+"</td></tr>";
  } else { // This is a proposition page
    footerText += "<td>"+getNextProp(book,prop)+" &nbsp; &nbsp; &nbsp; &nbsp; </td>";
    footerText += "<td>"+getPropForm(book)+"</td></tr>";
    footerText += "<tr valign=top><td>"+getPreviousProp(book,prop)+"</td>";
    footerText += "<td>"+getBookForm(prfx)+"</td></tr>";
    footerText += "<tr valign=top><td>"+getBookLink(book)+"</td>";
    footerText += "<td>"+getTopicForm(prfx)+"</td></tr>";
  }
  footerText += "</table></center>"
  // that finishes the table of links
  //finish up the footer
  footerText+="<hr size=6><p>";
  footerText+="<font size=-1><a href='/'>Home</a>";
  footerText+="<br>\u00A9"+copyrightDates;
  footerText+="<br>David E. Joyce (Professor Emeritus, <a href='http://www.clarku.edu/'>Clark University</a>)";
  footerText+="<br><a href='/copyright.html'>Copyright Notice</a>";
  footerText+="</font size>";
  //
  // footer is the footer for each chapter page
  //
  document.getElementById("footer").innerHTML=footerText;
}
// 
  /*
    footerText += "<td>"+getNextProp(book,prop)+"</td>";
    // next the from to select propositions from this book
    footerText += "<td>"+getPropForm(book)+"";
    // next the link to the previous proposition
    footerText += "<tr valign=top><td>"+getPreviousProp(book,prop)+"</td>";
  }
  // next the link to the book file
  footerText += '<tr valign=top><td><a href="'+booktable[book][0]+'.html">';
  footerText += booktable[book][1]+" introduction</a>";
  footerText += "&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </td>";
  */


//
// Return a form that allows the user to select which chapter to go to next
// This currently goes in the footer, but it could be placed elsewhere
//
function chapterForm(){
  var tocform="";
  tocform+="<form name='MyForm'><select name='select1' size='1' onchange='if (options[selectedIndex].value){location = options[selectedIndex].value}'>";
  tocform+="<option value=''>Select topic"
  for(pageitem in pagetable){
    tocform+='<option value="'+pagetable[pageitem][0]+'">'+pagetable[pageitem][1]+' ';
  }
  tocform+="</select>";
  return tocform;
}

import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc
import ghpythonlib.components as ghpc


sc.doc = ghdoc

if toggle:
    
    sc.doc = Rhino.RhinoDoc.ActiveDoc
    
    for i in xrange(count):
        
        
        curve = ghpc.ListItem(crvs, i)
#        print(curve)
        sc.doc.Objects.AddCurve(curve)
        
        name_format = "%03d"%i
        export_name = path + str(name_format) + type
        
        
        query = "-ViewCaptureToFile "+ \
            " W=1080 H=1080 S=1 L=_No D=_No R=_No A=_No T=_No " + \
            export_name + \
            " _Enter "
            " _SelAll _Delete"
        
        
        rs.Command(query)
    
        print(query)
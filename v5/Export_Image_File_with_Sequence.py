"""

1. Select Curve with FrameCount
2. Bake Curve
3. rs.Command("-ViewCaptureToFile")
4. rs.Command("_SelAll _Delete")

"""
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
            export_name + \
           " W=1080 H=1080 S=1 D=_No R=_No A=_No T=_Yes " + \
           " _Enter " + \
           " _SelAll _Delete"


        rs.Command(query)

        #print(query)

'''

汚いです

'''


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.components as ghpc



divCrvPts = []
seqCrv = []
render_Pts = []
RENDER = []



### 3 Curve(List Access)



### 30 Point (3 x 10)
for i in xrange(len(crvs)):
    pts = rs.DivideCurve(crvs[i], divCount)

    for j in xrange(divCount):
        tmp_pt = pts[j]
        divCrvPts.append(tmp_pt)
#print(len(divCrvPts))



### Flipping Matrix, ((0,10,20), (1,11,21), ...)
for i in xrange(divCount):
    flipMatPts = []
    flipMat_Line_Z = []

    for j in xrange(len(crvs)):
        # print(int(j*divCount + i))
        tmp_mat = divCrvPts[int(j*divCount + i)]
        tmp_mat_Add_Z_src = rs.AddPoint((tmp_mat.X, tmp_mat.Y, tmp_mat.Z))
        tmp_mat_Add_Z = rs.coerce3dpoint(tmp_mat_Add_Z_src)
        tmp_mat_Add_Z.Z = 1.0

        tmp_Line = rs.AddLine(tmp_mat, tmp_mat_Add_Z)
        flipMatPts.append(tmp_mat)
        flipMat_Line_Z.append(tmp_Line)

    #print(len(flipMatPts))
    #print(len(flipMat_Line_Z))
    #print("- - -")

    tmp_interpCrv = rs.AddInterpCurve(flipMatPts)
    tmp_interpCrv_coerce = rs.coercecurve(tmp_interpCrv)
    tmp_interpCrv_coerce.Domain = rg.Interval(0,1)

    all_v2 = []
    Result_v2 = []

    for k in xrange(len(flipMat_Line_Z)):
        flipMat_Line_Z_coerce = rs.coercecurve(flipMat_Line_Z[k])
        v1, v2 ,v3 = ghpc.CurveXCurve(tmp_interpCrv_coerce, flipMat_Line_Z_coerce)
        #print("v2", v2)
        all_v2.append(v2)

    debug = all_v2

    tmp_Result = 0

    for l in xrange(len(all_v2)):
        tmp_List = all_v2[l]
        if type(tmp_List) is list:
#            print(tmp_List)
#            print(tmp_Result)
            Result_v2.append(tmp_List[tmp_Result])
            tmp_Result+=1
        else:
            Result_v2.append(tmp_List)

    #print(Result_v2)
    #print(len(Result_v2))
#    print(type(Result_v2))
#    print(tmp_interpCrv_coerce)


    shatterCrv = ghpc.Shatter(tmp_interpCrv_coerce, Result_v2)
    #print(len(shtterCrv))
    #print(type(shtterCrv))


    Final_Pts = []
    for m in xrange(len(shatterCrv)):
        tmp_Final_Pts = rs.DivideCurve(shatterCrv[m], SeqCount)
        #pritn(len(tmp_Final_Pts))

        for n in xrange(len(tmp_Final_Pts)):
            Final_Pts.append(tmp_Final_Pts[n])

    #print(Final_Pts)
    #print(len(Final_Pts))

    for o in xrange(len(Final_Pts)):
        render_Pts.append(Final_Pts[o])



#print(len(render_Pts))
#print(len(Final_Pts))
#print(len(crvs))

### Render
for i in xrange(len(Final_Pts)):
    Render_Curve_Pts = []
    for j in xrange(divCount):
        #print(int(j*len(Final_Pts) + i))
        tmp_render_pt = render_Pts[int(j*len(Final_Pts) + i)]
        Render_Curve_Pts.append(tmp_render_pt)
    #print(len(Render_Curve_Pts))
    #RENDER_CRV = rs.AddInterpCurve(Render_Curve_Pts)
    RENDER_CRV, tmp_999, tmp_998 = ghpc.Interpolate(Render_Curve_Pts, 3, True)
    RENDER.append(RENDER_CRV)


crvs_w_sequence = RENDER
calcDomain = rg.Interval(0,len(RENDER)-1)
lastFrame = len(RENDER)-1

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg



### Divide Curve
def divide_crvs(crvs, div_count):
    points_div = []
    
    for i in xrange(len(crvs)):
        tmp_pts = rs.DivideCurve(crvs[i], div_count)
        points_div.append(tmp_pts)
    
    # print points_div
    # print len(points_div)
    # print len(points_div[0])
    
    ### 2D Array
    return points_div



### Flip 2D Array
def flip_2d_array(array_2d):
    
    array_2d_f = list(map(list, zip(*array_2d)))
    # print len(array_2d_f)
    # print len(array_2d_f[0])
    
    return array_2d_f



### InterpCrv
def interp_crvs(array_2d_f):
    in_crvs = []
    
    for i in xrange(len(array_2d_f)):
        crv = rs.AddInterpCurve(array_2d_f[i])
        in_crvs.append(crv)
    
    return in_crvs



### Slice Sequence
def slice_sequence(crvs, seq_count):
    
    pt_slice = []
    
    frame = 1 / seq_count
    # print frame
    
    
    for i in xrange(len(crvs)):
        crv = crvs[i]
        crv = rs.coercecurve(crv)
        start_pt, end_pt = rs.CurveDomain(crv)
        # print start_pt, "to", end_pt ### [0 to len(Curves)]
        
        param_slice = []
        for j in xrange(int(end_pt)):
            
            for k in xrange(seq_count):
                value = j + k*frame
                param_slice.append(value)
        
        param_slice.append(end_pt)
        
        # print param_slice
        # print len(param_slice)
        
        sub_list = []
        for l in xrange(len(param_slice)):
            pt = rg.Curve.PointAt(crv, param_slice[l])
            sub_list.append(pt)
        
        pt_slice.append(sub_list)
    
    return pt_slice



### Generate Frame
def generate_frame(pt_array):
    
    crv_frame = []
    for i in xrange(len(pt_array)):
        
        pt_list = []
        tmp_list = pt_array[i]
        
        ### closed, add -1
        for j in xrange(len(tmp_list)):
            pt_list.append(tmp_list[j])
        
        pt_list.append(tmp_list[0])
        
        crv = rs.AddInterpCurve(pt_list)
        rs.CloseCurve(crv)
        crv_frame.append(crv)
    
    return crv_frame






pts_div_crv = divide_crvs(CURVES, DIV_COUNT)
pts_div_crv_flip = flip_2d_array(pts_div_crv)

crvs_interpolate = interp_crvs(pts_div_crv_flip)

pt_slice = slice_sequence(crvs_interpolate, SEQ_COUNT)
pt_slice_flip = flip_2d_array(pt_slice)

crvs_all_frame = generate_frame(pt_slice_flip)



### Output
CRUVES_w_SEQ = crvs_all_frame
DOMAIN = rg.Interval(0, len(crvs_all_frame)- 1)
LAST_FRAME = len(crvs_all_frame)
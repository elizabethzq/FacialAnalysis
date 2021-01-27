import pandas as pd
import numpy as np
import math
import csv


files = [
         '1.csv',
         '2.csv',
         '3.csv',
         '4.csv',
         '5.csv',
         '6.csv',
         '7.csv',
         '8.csv',
         '9.csv'
         ]

# sample rate = 60 frames/second

def processPoint(pt1, pt2, filename, df, df0):
    # point 44
    point[pt1] = {
        'x_in' : df0[' X_%s' % pt1][0],
        'y_in' : df0[' Y_%s' % pt1][0],
        'z_in' : df0[' Z_%s' % pt1][0]
    }

    df['X_%s_in' % pt1]=df[' X_%s' % pt1]-point[pt1]['x_in']
    df['Y_%s_in' % pt1]=df[' Y_%s' % pt1]-point[pt1]['y_in']
    df['Z_%s_in' % pt1]=df[' Z_%s' % pt1]-point[pt1]['z_in']

    point[pt2] = {
        'x_in' : df0[' X_%s' % pt2][0],
        'y_in' : df0[' Y_%s' % pt2][0],
        'z_in' : df0[' Z_%s' % pt2][0]
    }

    df['X_%s_in' % pt2]=df[' X_%s' % pt2]-point[pt2]['x_in']
    df['Y_%s_in' % pt2]=df[' Y_%s' % pt2]-point[pt2]['y_in']
    df['Z_%s_in' % pt2]=df[' Z_%s' % pt2]-point[pt2]['z_in']



    df['X_%s_f' % pt2]=df['X_%s_in' % pt2]-df['X_%s_in' % pt1]
    df['Y_%s_f' % pt2]=df['Y_%s_in' % pt2]-df['Y_%s_in' % pt1]
    df['Z_%s_f' % pt2]=df['Z_%s_in' % pt2]-df['Z_%s_in' % pt1]

    lstDist = []
    for i in range (len(df['X_%s_f' % pt2])):
        x0= df['X_%s_f' % pt2][i]
        y0= df['Y_%s_f' % pt2][i]
        z0= df['Z_%s_f' % pt2][i]
        x = (df['X_%s_f' % pt2][i])**2
        y = (df['Y_%s_f' % pt2][i])**2
        z = (df['Z_%s_f' % pt2][i])**2

        dist = math.sqrt(x+y+z)
        lstDist.append([x0,y0,z0,dist])

    cols=['X_%s' % pt2,'Y_%s' % pt2,'Z_%s' % pt2,'dist_%s' % pt2]
#     result = pd.concat(lstDist, columns=cols)
#     result = pd.concat(lstDist)
    result = pd.DataFrame(lstDist, columns=cols)
    return result
#     result.to_csv('pt_%s_%s.csv' % (filename,pt2))
#     return result
#

# point = {}
# print (processPoint(30, 40, df, df0))

df0 = pd.read_csv('0.csv')
df0.columns = df0.columns.astype(str)



point = {}
for i in files:
    df = pd.read_csv('%s' % i)
    df.columns = df.columns.astype(str)
#     for j in range(68):
#         result = processPoint(30, j, i, df, df0)

    x30_in = df0[' X_30'][0]
    y30_in = df0[' Y_30'][0]
    z30_in = df0[' Z_30'][0]

    df['X_30_in']=df[' X_30']-x30_in
    df['Y_30_in']=df[' Y_30']-y30_in
    df['Z_30_in']=df[' Z_30']-z30_in

    df_30 = []
    for j in range (len(df['X_30_in'])):
        x0= df['X_30_in'][j]
        y0= df['Y_30_in'][j]
        z0= df['Z_30_in'][j]
        x = (df['X_30_in'][j])**2
        y = (df['Y_30_in'][j])**2
        z = (df['Z_30_in'][j])**2

        dist = math.sqrt(x+y+z)
        df_30.append([x0,y0,z0,dist])

    cols=['X_30','Y_30','Z_30','dist_30']
    result_30 = pd.DataFrame(df_30, columns=cols)

    result_1 = processPoint(30, 1, i, df, df0)
    result_8 = processPoint(30, 8, i, df, df0)
    result_15 = processPoint(30, 15, i, df, df0)
    result_17 = processPoint(30, 17, i, df, df0)
    result_19 = processPoint(30, 19, i, df, df0)
    result_21 = processPoint(30, 21, i, df, df0)
    result_22 = processPoint(30, 22, i, df, df0)
    result_24 = processPoint(30, 24, i, df, df0)
    result_26 = processPoint(30, 26, i, df, df0)
    result_27 = processPoint(30, 27, i, df, df0)
    result_36 = processPoint(30, 36, i, df, df0)
    result_37 = processPoint(30, 37, i, df, df0)
    result_38 = processPoint(30, 38, i, df, df0)
    result_39 = processPoint(30, 39, i, df, df0)
    result_40 = processPoint(30, 40, i, df, df0)
    result_41 = processPoint(30, 41, i, df, df0)
    result_42 = processPoint(30, 42, i, df, df0)
    result_43 = processPoint(30, 43, i, df, df0)
    result_44 = processPoint(30, 43, i, df, df0)
    result_45 = processPoint(30, 45, i, df, df0)
    result_46 = processPoint(30, 46, i, df, df0)
    result_47 = processPoint(30, 47, i, df, df0)
    result_48 = processPoint(30, 48, i, df, df0)
    result_49 = processPoint(30, 49, i, df, df0)
    result_51 = processPoint(30, 50, i, df, df0)
    result_53 = processPoint(30, 53, i, df, df0)
    result_54 = processPoint(30, 54, i, df, df0)
    result_55 = processPoint(30, 55, i, df, df0)
    result_57 = processPoint(30, 57, i, df, df0)
    result_59 = processPoint(30, 59, i, df, df0)

    result = pd.concat ([result_30, result_1, result_8,result_15,result_17, result_19, result_21, result_22,
                     result_24, result_26, result_27, result_36, result_37, result_38, result_39,
                     result_40, result_41, result_42, result_43, result_44, result_45, result_46,
                     result_47, result_48, result_49, result_51, result_53, result_54, result_55,
                     result_57, result_59], axis=1)
    result
    result.to_csv('%s_3D_dist.csv' % i)

    

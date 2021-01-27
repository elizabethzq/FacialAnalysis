import pandas as pd
import numpy as np
import math
import csv


files = ['0.csv',
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

def featureVector(pt1, pt2, ft, filename, df, df0):
# def featureVector(pt1, pt2, ft, df, df0):

    point[pt1] = {
        'x_in' : df0[' X_%s' % pt1][0],
        'y_in' : df0[' Y_%s' % pt1][0],
        'z_in' : df0[' Z_%s' % pt1][0]
    }

    point[pt2] = {
        'x_in' : df0[' X_%s' % pt2][0],
        'y_in' : df0[' Y_%s' % pt2][0],
        'z_in' : df0[' Z_%s' % pt2][0]
    }

    x = (point[pt2]['x_in']-point[pt1]['x_in'])**2
    y = (point[pt2]['y_in']-point[pt1]['y_in'])**2
    z = (point[pt2]['z_in']-point[pt1]['z_in'])**2

    pt1_0 = math.sqrt(x+y+z)

    df['X_%s_f' % pt2]=df[' X_%s' % pt2]-df[' X_%s' % pt1]
    df['Y_%s_f' % pt2]=df[' Y_%s' % pt2]-df[' Y_%s' % pt1]
    df['Z_%s_f' % pt2]=df[' Z_%s' % pt2]-df[' Z_%s' % pt1]

    res = [int(i) for i in filename.split() if i.isdigit()]
    f = str (res)

    lstDist = []
    for i in range (len(df['X_%s_f' % pt2])):
        x0= df[' X_%s' % pt1][i]
        y0= df[' Y_%s' % pt1][i]
        z0= df[' Z_%s' % pt1][i]

        x1= df[' X_%s' % pt2][i]
        y1= df[' Y_%s' % pt2][i]
        z1= df[' Z_%s' % pt2][i]

        x = (df['X_%s_f' % pt2][i])**2
        y = (df['Y_%s_f' % pt2][i])**2
        z = (df['Z_%s_f' % pt2][i])**2

        dist = math.sqrt(x+y+z)
        s_pt1 = dist - pt1_0
        lstDist.append([x0,y0,z0,x1,y1,z1,dist,s_pt1])

    cols=['X_%s' % pt1,'Y_%s' % pt1,'Z_%s' % pt1,'X_%s' % pt2,'Y_%s' % pt2,'Z_%s' % pt2,'dist_%s' % ft,'s_%s' % ft]
#     result = pd.concat(lstDist, columns=cols)
#     result = pd.concat(lstDist)
    result = pd.DataFrame(lstDist, columns=cols)
    return result
#     print (f,result)

#     result.to_csv('vector_%s_%s.csv' % (filename,ft))

# sample rate = 60 frames/second
df0 = pd.read_csv('0.csv')
df0.columns = df0.columns.astype(str)

# filename = "9.csv"
# res = [int(i) for i in filename.split() if i.isdigit()]
# print(res)


point = {}
result = []
for i in files:
    df = pd.read_csv('%s' % i)
    df.columns = df.columns.astype(str)
    result_D1 = featureVector(17, 36, 'D1', i, df, df0)
    result_D2 = featureVector(21, 27, 'D2', i, df, df0)
    result_D3 = featureVector(19, 27, 'D3', i, df, df0)
    result_D4 = featureVector(38, 40, 'D4', i, df, df0)
    result_D5 = featureVector(26, 45, 'D5', i, df, df0)
    result_D6 = featureVector(22, 27, 'D6', i, df, df0)
    result_D7 = featureVector(24, 27, 'D7', i, df, df0)
    result_D8 = featureVector(43, 47, 'D8', i, df, df0)
    result_D9 = featureVector(51, 57, 'D9', i, df, df0)
    result_D10 = featureVector(48, 54, 'D10', i, df, df0)
    result_D11 = featureVector(48, 8, 'D11', i, df, df0)
    result_D12 = featureVector(54, 8, 'D12', i, df, df0)
    result_L3 = featureVector(27, 8, 'L3', i, df, df0)
    result_L4 = featureVector(2, 14, 'L4', i, df, df0)
#     print (result_D1,result_D2)
    result = pd.concat ([result_D1,result_D2,result_D3,result_D4,
                         result_D5,result_D6,result_D7,result_D8,
                         result_D9,result_D10,result_D11,result_D12,
                         result_L3,result_L4], axis=1)
    result.to_csv('%s_features.csv' % i)

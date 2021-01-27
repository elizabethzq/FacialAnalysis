import pandas as pd
import numpy as np
import math
import csv


files = [
         '1.csv_features.csv',
         '2.csv_features.csv',
         '3.csv_features.csv',
         '4.csv_features.csv',
         '5.csv_features.csv',
         '6.csv_features.csv',
         '7.csv_features.csv',
         '8.csv_features.csv',
         '9.csv_features.csv'
         ]

# sample rate = 60 frames/second


df1 = pd.read_csv('1_features.csv')
# df0.columns = df0.columns.astype(str)

df2 = pd.read_csv('2_features.csv')
# df.columns = df.columns.astype(str)
df3 = pd.read_csv('3_features.csv')
df4 = pd.read_csv('4_features.csv')
df5 = pd.read_csv('5_features.csv')
df6 = pd.read_csv('6_features.csv')
df7 = pd.read_csv('7_features.csv')
df8 = pd.read_csv('8_features.csv')
df9 = pd.read_csv('9_features.csv')


result = pd.concat ([df1['D1'],df1['S_D1'],
                     df2['D1'],df2['S_D1'],
                     df3['D1'],df3['S_D1'],
                     df4['D1'],df4['S_D1'],
                     df5['D1'],df5['S_D1'],
                     df6['D1'],df6['S_D1'],
                     df7['D1'],df7['S_D1'],
                     df8['D1'],df8['S_D1'],
                     df9['D1'],df9['S_D1'],
                    ], axis=1)

# D1 from window 1-9
result.columns = ['D1_1', 'S_D1_1',
                  'D1_2', 'S_D1_2',
                  'D1_3', 'S_D1_3',
                  'D1_4', 'S_D1_4',
                  'D1_5', 'S_D1_5',
                  'D1_6', 'S_D1_6',
                  'D1_7', 'S_D1_7',
                  'D1_8', 'S_D1_8',
                  'D1_9', 'S_D1_9',
                 ]


result.to_csv('D1_W1-W9.csv')


# D2 from window 1-9
result = pd.concat ([df1['D2'],df1['S_D2'],
                     df2['D2'],df2['S_D2'],
                     df3['D2'],df3['S_D2'],
                     df4['D2'],df4['S_D2'],
                     df5['D2'],df5['S_D2'],
                     df6['D2'],df6['S_D2'],
                     df7['D2'],df7['S_D2'],
                     df8['D2'],df8['S_D2'],
                     df9['D2'],df9['S_D2'],
                    ], axis=1)

result.columns = ['D2_1', 'S_D2_1',
                  'D2_2', 'S_D2_2',
                  'D2_3', 'S_D2_3',
                  'D2_4', 'S_D2_4',
                  'D2_5', 'S_D2_5',
                  'D2_6', 'S_D2_6',
                  'D2_7', 'S_D2_7',
                  'D2_8', 'S_D2_8',
                  'D2_9', 'S_D2_9',
                 ]
result.to_csv('D2_W1-W9.csv')


# D3 from window 1-9
result = pd.concat ([df1['D3'],df1['S_D3'],
                     df2['D3'],df2['S_D3'],
                     df3['D3'],df3['S_D3'],
                     df4['D3'],df4['S_D3'],
                     df5['D3'],df5['S_D3'],
                     df6['D3'],df6['S_D3'],
                     df7['D3'],df7['S_D3'],
                     df8['D3'],df8['S_D3'],
                     df9['D3'],df9['S_D3'],
                    ], axis=1)

result.columns = ['D3_1', 'S_D3_1',
                  'D3_2', 'S_D3_2',
                  'D3_3', 'S_D3_3',
                  'D3_4', 'S_D3_4',
                  'D3_5', 'S_D3_5',
                  'D3_6', 'S_D3_6',
                  'D3_7', 'S_D3_7',
                  'D3_8', 'S_D3_8',
                  'D3_9', 'S_D3_9',
                 ]
result.to_csv('D3_W1-W9.csv')


# D4 from window 1-9
result = pd.concat ([df1['D4'],df1['S_D4'],
                     df2['D4'],df2['S_D4'],
                     df3['D4'],df3['S_D4'],
                     df4['D4'],df4['S_D4'],
                     df5['D4'],df5['S_D4'],
                     df6['D4'],df6['S_D4'],
                     df7['D4'],df7['S_D4'],
                     df8['D4'],df8['S_D4'],
                     df9['D4'],df9['S_D4'],
                    ], axis=1)

result.columns = ['D4_1', 'S_D4_1',
                  'D4_2', 'S_D4_2',
                  'D4_3', 'S_D4_3',
                  'D4_4', 'S_D4_4',
                  'D4_5', 'S_D4_5',
                  'D4_6', 'S_D4_6',
                  'D4_7', 'S_D4_7',
                  'D4_8', 'S_D4_8',
                  'D4_9', 'S_D4_9',
                 ]
result.to_csv('D4_W1-W9.csv')


# D5 from window 1-9
result = pd.concat ([df1['D5'],df1['S_D5'],
                     df2['D5'],df2['S_D5'],
                     df3['D5'],df3['S_D5'],
                     df4['D5'],df4['S_D5'],
                     df5['D5'],df5['S_D5'],
                     df6['D5'],df6['S_D5'],
                     df7['D5'],df7['S_D5'],
                     df8['D5'],df8['S_D5'],
                     df9['D5'],df9['S_D5'],
                    ], axis=1)

result.columns = ['D5_1', 'S_D5_1',
                  'D5_2', 'S_D5_2',
                  'D5_3', 'S_D5_3',
                  'D5_4', 'S_D5_4',
                  'D5_5', 'S_D5_5',
                  'D5_6', 'S_D5_6',
                  'D5_7', 'S_D5_7',
                  'D5_8', 'S_D5_8',
                  'D5_9', 'S_D5_9',
                 ]
result.to_csv('D5_W1-W9.csv')


# D6 from window 1-9
result = pd.concat ([df1['D6'],df1['S_D6'],
                     df2['D6'],df2['S_D6'],
                     df3['D6'],df3['S_D6'],
                     df4['D6'],df4['S_D6'],
                     df5['D6'],df5['S_D6'],
                     df6['D6'],df6['S_D6'],
                     df7['D6'],df7['S_D6'],
                     df8['D6'],df8['S_D6'],
                     df9['D6'],df9['S_D6'],
                    ], axis=1)

result.columns = ['D6_1', 'S_D6_1',
                  'D6_2', 'S_D6_2',
                  'D6_3', 'S_D6_3',
                  'D6_4', 'S_D6_4',
                  'D6_5', 'S_D6_5',
                  'D6_6', 'S_D6_6',
                  'D6_7', 'S_D6_7',
                  'D6_8', 'S_D6_8',
                  'D6_9', 'S_D6_9',
                 ]
result.to_csv('D6_W1-W9.csv')


# D7 from window 1-9
result = pd.concat ([df1['D7'],df1['S_D7'],
                     df2['D7'],df2['S_D7'],
                     df3['D7'],df3['S_D7'],
                     df4['D7'],df4['S_D7'],
                     df5['D7'],df5['S_D7'],
                     df6['D7'],df6['S_D7'],
                     df7['D7'],df7['S_D7'],
                     df8['D7'],df8['S_D7'],
                     df9['D7'],df9['S_D7'],
                    ], axis=1)

result.columns = ['D7_1', 'S_D7_1',
                  'D7_2', 'S_D7_2',
                  'D7_3', 'S_D7_3',
                  'D7_4', 'S_D7_4',
                  'D7_5', 'S_D7_5',
                  'D7_6', 'S_D7_6',
                  'D7_7', 'S_D7_7',
                  'D7_8', 'S_D7_8',
                  'D7_9', 'S_D7_9',
                 ]
result.to_csv('D7_W1-W9.csv')


# D8 from window 1-9
result = pd.concat ([df1['D8'],df1['S_D8'],
                     df2['D8'],df2['S_D8'],
                     df3['D8'],df3['S_D8'],
                     df4['D8'],df4['S_D8'],
                     df5['D8'],df5['S_D8'],
                     df6['D8'],df6['S_D8'],
                     df7['D8'],df7['S_D8'],
                     df8['D8'],df8['S_D8'],
                     df9['D8'],df9['S_D8'],
                    ], axis=1)

result.columns = ['D8_1', 'S_D8_1',
                  'D8_2', 'S_D8_2',
                  'D8_3', 'S_D8_3',
                  'D8_4', 'S_D8_4',
                  'D8_5', 'S_D8_5',
                  'D8_6', 'S_D8_6',
                  'D8_7', 'S_D8_7',
                  'D8_8', 'S_D8_8',
                  'D8_9', 'S_D8_9',
                 ]
result.to_csv('D8_W1-W9.csv')


# D9 from window 1-9
result = pd.concat ([df1['D9'],df1['S_D9'],
                     df2['D9'],df2['S_D9'],
                     df3['D9'],df3['S_D9'],
                     df4['D9'],df4['S_D9'],
                     df5['D9'],df5['S_D9'],
                     df6['D9'],df6['S_D9'],
                     df7['D9'],df7['S_D9'],
                     df8['D9'],df8['S_D9'],
                     df9['D9'],df9['S_D9'],
                    ], axis=1)

result.columns = ['D9_1', 'S_D9_1',
                  'D9_2', 'S_D9_2',
                  'D9_3', 'S_D9_3',
                  'D9_4', 'S_D9_4',
                  'D9_5', 'S_D9_5',
                  'D9_6', 'S_D9_6',
                  'D9_7', 'S_D9_7',
                  'D9_8', 'S_D9_8',
                  'D9_9', 'S_D9_9',
                 ]
result.to_csv('D9_W1-W9.csv')


# D10 from window 1-9
result = pd.concat ([df1['D10'],df1['S_D10'],
                     df2['D10'],df2['S_D10'],
                     df3['D10'],df3['S_D10'],
                     df4['D10'],df4['S_D10'],
                     df5['D10'],df5['S_D10'],
                     df6['D10'],df6['S_D10'],
                     df7['D10'],df7['S_D10'],
                     df8['D10'],df8['S_D10'],
                     df9['D10'],df9['S_D10'],
                    ], axis=1)

result.columns = ['D10_1', 'S_D10_1',
                  'D10_2', 'S_D10_2',
                  'D10_3', 'S_D10_3',
                  'D10_4', 'S_D10_4',
                  'D10_5', 'S_D10_5',
                  'D10_6', 'S_D10_6',
                  'D10_7', 'S_D10_7',
                  'D10_8', 'S_D10_8',
                  'D10_9', 'S_D10_9',
                 ]
result.to_csv('D10_W1-W9.csv')


# D11 from window 1-9
result = pd.concat ([df1['D11'],df1['S_D11'],
                     df2['D11'],df2['S_D11'],
                     df3['D11'],df3['S_D11'],
                     df4['D11'],df4['S_D11'],
                     df5['D11'],df5['S_D11'],
                     df6['D11'],df6['S_D11'],
                     df7['D11'],df7['S_D11'],
                     df8['D11'],df8['S_D11'],
                     df9['D11'],df9['S_D11'],
                    ], axis=1)

result.columns = ['D11_1', 'S_D11_1',
                  'D11_2', 'S_D11_2',
                  'D11_3', 'S_D11_3',
                  'D11_4', 'S_D11_4',
                  'D11_5', 'S_D11_5',
                  'D11_6', 'S_D11_6',
                  'D11_7', 'S_D11_7',
                  'D11_8', 'S_D11_8',
                  'D11_9', 'S_D11_9',
                 ]
result.to_csv('D11_W1-W9.csv')


# D12 from window 1-9
result = pd.concat ([df1['D12'],df1['S_D12'],
                     df2['D12'],df2['S_D12'],
                     df3['D12'],df3['S_D12'],
                     df4['D12'],df4['S_D12'],
                     df5['D12'],df5['S_D12'],
                     df6['D12'],df6['S_D12'],
                     df7['D12'],df7['S_D12'],
                     df8['D12'],df8['S_D12'],
                     df9['D12'],df9['S_D12'],
                    ], axis=1)

result.columns = ['D12_1', 'S_D12_1',
                  'D12_2', 'S_D12_2',
                  'D12_3', 'S_D12_3',
                  'D12_4', 'S_D12_4',
                  'D12_5', 'S_D12_5',
                  'D12_6', 'S_D12_6',
                  'D12_7', 'S_D12_7',
                  'D12_8', 'S_D12_8',
                  'D12_9', 'S_D12_9',
                 ]
result.to_csv('D12_W1-W9.csv')


# L3 from window 1-9
result = pd.concat ([df1['L3'],df1['S_L3'],
                     df2['L3'],df2['S_L3'],
                     df3['L3'],df3['S_L3'],
                     df4['L3'],df4['S_L3'],
                     df5['L3'],df5['S_L3'],
                     df6['L3'],df6['S_L3'],
                     df7['L3'],df7['S_L3'],
                     df8['L3'],df8['S_L3'],
                     df9['L3'],df9['S_L3'],
                    ], axis=1)

result.columns = ['L3_1', 'S_L3_1',
                  'L3_2', 'S_L3_2',
                  'L3_3', 'S_L3_3',
                  'L3_4', 'S_L3_4',
                  'L3_5', 'S_L3_5',
                  'L3_6', 'S_L3_6',
                  'L3_7', 'S_L3_7',
                  'L3_8', 'S_L3_8',
                  'L3_9', 'S_L3_9',
                 ]
result.to_csv('L3_W1-W9.csv')


# L4 from window 1-9
result = pd.concat ([df1['L4'],df1['S_L4'],
                     df2['L4'],df2['S_L4'],
                     df3['L4'],df3['S_L4'],
                     df4['L4'],df4['S_L4'],
                     df5['L4'],df5['S_L4'],
                     df6['L4'],df6['S_L4'],
                     df7['L4'],df7['S_L4'],
                     df8['L4'],df8['S_L4'],
                     df9['L4'],df9['S_L4'],
                    ], axis=1)

result.columns = ['L4_1', 'S_L4_1',
                  'L4_2', 'S_L4_2',
                  'L4_3', 'S_L4_3',
                  'L4_4', 'S_L4_4',
                  'L4_5', 'S_L4_5',
                  'L4_6', 'S_L4_6',
                  'L4_7', 'S_L4_7',
                  'L4_8', 'S_L4_8',
                  'L4_9', 'S_L4_9',
                 ]
result.to_csv('L4_W1-W9.csv')


# print (result)

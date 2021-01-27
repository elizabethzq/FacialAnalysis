import pandas as pd
import numpy as np
import math
import csv


files = [

         '1.csv_3D_dist.csv',
         '2.csv_3D_dist.csv',
         '3.csv_3D_dist.csv',
         '4.csv_3D_dist.csv',
         '5.csv_3D_dist.csv',
         '6.csv_3D_dist.csv',
         '7.csv_3D_dist.csv',
         '8.csv_3D_dist.csv',
         '9.csv_3D_dist.csv'
           ]

df1 = pd.read_csv('1_3D_dist.csv')
df2 = pd.read_csv('2_3D_dist.csv')
df3 = pd.read_csv('3_3D_dist.csv')
df4 = pd.read_csv('4_3D_dist.csv')
df5 = pd.read_csv('5_3D_dist.csv')
df6 = pd.read_csv('6_3D_dist.csv')
df7 = pd.read_csv('7_3D_dist.csv')
df8 = pd.read_csv('8_3D_dist.csv')
df9 = pd.read_csv('9_3D_dist.csv')

# point 30, 17, 19, 21, 22, 24, 26, 37, 43, 48, 54, 51, 57

# point 30
result = pd.concat ([df1['dist_30'],
                     df2['dist_30'],
                     df3['dist_30'],
                     df4['dist_30'],
                     df5['dist_30'],
                     df6['dist_30'],
                     df7['dist_30'],
                     df8['dist_30'],
                     df9['dist_30']
                    ], axis=1)

result.columns = ['30_1',
                  '30_2',
                  '30_3',
                  '30_4',
                  '30_5',
                  '30_6',
                  '30_7',
                  '30_8',
                  '30_9'
                 ]

result.to_csv('30_W1-W9.csv')

# point 8
result = pd.concat ([df1['dist_8'],
                     df2['dist_8'],
                     df3['dist_8'],
                     df4['dist_8'],
                     df5['dist_8'],
                     df6['dist_8'],
                     df7['dist_8'],
                     df8['dist_8'],
                     df9['dist_8']
                    ], axis=1)

result.columns = ['8_1',
                  '8_2',
                  '8_3',
                  '8_4',
                  '8_5',
                  '8_6',
                  '8_7',
                  '8_8',
                  '8_9'
                 ]

result.to_csv('8_W1-W9.csv')

# point 38
result = pd.concat ([df1['dist_38'],
                     df2['dist_38'],
                     df3['dist_38'],
                     df4['dist_38'],
                     df5['dist_38'],
                     df6['dist_38'],
                     df7['dist_38'],
                     df8['dist_38'],
                     df9['dist_38']
                    ], axis=1)

result.columns = ['38_1',
                  '38_2',
                  '38_3',
                  '38_4',
                  '38_5',
                  '38_6',
                  '38_7',
                  '38_8',
                  '38_9'
                 ]

result.to_csv('38_W1-W9.csv')


# point 17
result = pd.concat ([df1['dist_17'],
                     df2['dist_17'],
                     df3['dist_17'],
                     df4['dist_17'],
                     df5['dist_17'],
                     df6['dist_17'],
                     df7['dist_17'],
                     df8['dist_17'],
                     df9['dist_17']
                    ], axis=1)

result.columns = ['17_1',
                  '17_2',
                  '17_3',
                  '17_4',
                  '17_5',
                  '17_6',
                  '17_7',
                  '17_8',
                  '17_9'
                 ]

result.to_csv('17_W1-W9.csv')

#Point 19
# point 19
result = pd.concat ([df1['dist_19'],
                     df2['dist_19'],
                     df3['dist_19'],
                     df4['dist_19'],
                     df5['dist_19'],
                     df6['dist_19'],
                     df7['dist_19'],
                     df8['dist_19'],
                     df9['dist_19']
                    ], axis=1)

result.columns = ['19_1',
                  '19_2',
                  '19_3',
                  '19_4',
                  '19_5',
                  '19_6',
                  '19_7',
                  '19_8',
                  '19_9'
                 ]

result.to_csv('19_W1-W9.csv')

#point 21
result = pd.concat ([df1['dist_21'],
                     df2['dist_21'],
                     df3['dist_21'],
                     df4['dist_21'],
                     df5['dist_21'],
                     df6['dist_21'],
                     df7['dist_21'],
                     df8['dist_21'],
                     df9['dist_21']
                    ], axis=1)

result.columns = ['21_1',
                  '21_2',
                  '21_3',
                  '21_4',
                  '21_5',
                  '21_6',
                  '21_7',
                  '21_8',
                  '21_9'
                 ]

result.to_csv('21_W1-W9.csv')

#point 22
result = pd.concat ([df1['dist_22'],
                     df2['dist_22'],
                     df3['dist_22'],
                     df4['dist_22'],
                     df5['dist_22'],
                     df6['dist_22'],
                     df7['dist_22'],
                     df8['dist_22'],
                     df9['dist_22']
                    ], axis=1)

result.columns = ['22_1',
                  '22_2',
                  '22_3',
                  '22_4',
                  '22_5',
                  '22_6',
                  '22_7',
                  '22_8',
                  '22_9'
                 ]

result.to_csv('22_W1-W9.csv')

#point 24
result = pd.concat ([df1['dist_24'],
                     df2['dist_24'],
                     df3['dist_24'],
                     df4['dist_24'],
                     df5['dist_24'],
                     df6['dist_24'],
                     df7['dist_24'],
                     df8['dist_24'],
                     df9['dist_24']
                    ], axis=1)

result.columns = ['24_1',
                  '24_2',
                  '24_3',
                  '24_4',
                  '24_5',
                  '24_6',
                  '24_7',
                  '24_8',
                  '24_9'
                 ]

result.to_csv('24_W1-W9.csv')

#point 26
result = pd.concat ([df1['dist_26'],
                     df2['dist_26'],
                     df3['dist_26'],
                     df4['dist_26'],
                     df5['dist_26'],
                     df6['dist_26'],
                     df7['dist_26'],
                     df8['dist_26'],
                     df9['dist_26']
                    ], axis=1)

result.columns = ['26_1',
                  '26_2',
                  '26_3',
                  '26_4',
                  '26_5',
                  '26_6',
                  '26_7',
                  '26_8',
                  '26_9'
                 ]

result.to_csv('26_W1-W9.csv')

#point 37
result = pd.concat ([df1['dist_37'],
                     df2['dist_37'],
                     df3['dist_37'],
                     df4['dist_37'],
                     df5['dist_37'],
                     df6['dist_37'],
                     df7['dist_37'],
                     df8['dist_37'],
                     df9['dist_37']
                    ], axis=1)

result.columns = ['37_1',
                  '37_2',
                  '37_3',
                  '37_4',
                  '37_5',
                  '37_6',
                  '37_7',
                  '37_8',
                  '37_9'
                 ]

result.to_csv('37_W1-W9.csv')

#point 43
result = pd.concat ([df1['dist_43'],
                     df2['dist_43'],
                     df3['dist_43'],
                     df4['dist_43'],
                     df5['dist_43'],
                     df6['dist_43'],
                     df7['dist_43'],
                     df8['dist_43'],
                     df9['dist_43']
                    ], axis=1)

result.columns = ['43_1',
                  '43_2',
                  '43_3',
                  '43_4',
                  '43_5',
                  '43_6',
                  '43_7',
                  '43_8',
                  '43_9'
                 ]

result.to_csv('43_W1-W9.csv')

# point 44

result = pd.concat ([df1['dist_44'],
                     df2['dist_44'],
                     df3['dist_44'],
                     df4['dist_44'],
                     df5['dist_44'],
                     df6['dist_44'],
                     df7['dist_44'],
                     df8['dist_44'],
                     df9['dist_44']
                    ], axis=1)

result.columns = ['44_1',
                  '44_2',
                  '44_3',
                  '44_4',
                  '44_5',
                  '44_6',
                  '44_7',
                  '44_8',
                  '44_9'
                 ]

result.to_csv('44_W1-W9.csv')


#point 48
result = pd.concat ([df1['dist_48'],
                     df2['dist_48'],
                     df3['dist_48'],
                     df4['dist_48'],
                     df5['dist_48'],
                     df6['dist_48'],
                     df7['dist_48'],
                     df8['dist_48'],
                     df9['dist_48']
                    ], axis=1)

result.columns = ['48_1',
                  '48_2',
                  '48_3',
                  '48_4',
                  '48_5',
                  '48_6',
                  '48_7',
                  '48_8',
                  '48_9'
                 ]

result.to_csv('48_W1-W9.csv')

#point 54
result = pd.concat ([df1['dist_54'],
                     df2['dist_54'],
                     df3['dist_54'],
                     df4['dist_54'],
                     df5['dist_54'],
                     df6['dist_54'],
                     df7['dist_54'],
                     df8['dist_54'],
                     df9['dist_54']
                    ], axis=1)

result.columns = ['54_1',
                  '54_2',
                  '54_3',
                  '54_4',
                  '54_5',
                  '54_6',
                  '54_7',
                  '54_8',
                  '54_9'
                 ]

result.to_csv('54_W1-W9.csv')

#point 51
result = pd.concat ([df1['dist_51'],
                     df2['dist_51'],
                     df3['dist_51'],
                     df4['dist_51'],
                     df5['dist_51'],
                     df6['dist_51'],
                     df7['dist_51'],
                     df8['dist_51'],
                     df9['dist_51']
                    ], axis=1)

result.columns = ['51_1',
                  '51_2',
                  '51_3',
                  '51_4',
                  '51_5',
                  '51_6',
                  '51_7',
                  '51_8',
                  '51_9'
                 ]

result.to_csv('51_W1-W9.csv')

#point 57

result = pd.concat ([df1['dist_57'],
                     df2['dist_57'],
                     df3['dist_57'],
                     df4['dist_57'],
                     df5['dist_57'],
                     df6['dist_57'],
                     df7['dist_57'],
                     df8['dist_57'],
                     df9['dist_57']
                    ], axis=1)

result.columns = ['57_1',
                  '57_2',
                  '57_3',
                  '57_4',
                  '57_5',
                  '57_6',
                  '57_7',
                  '57_8',
                  '57_9'
                 ]

result.to_csv('57_W1-W9.csv')

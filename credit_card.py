# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
#
# def test_score(test_feature,test_target):
#     data = pd.read_csv('credit_card_train.csv',header = 0)
#
#     data1 = data.iloc[:,1:14]
#     data2 = pd.get_dummies(data.iloc[:,14:17])
#
#     feature = pd.concat([data1,data2],axis= 1).values
#     target = data['DEFAULT'].values
#
#
#     model = RandomForestClassifier()
#     model.fit(feature,target)
#
#
#
#     score = model.score(test_feature,test_target)
#
#     return score
#



#
# import pandas as pd
# import numpy as np
# from pandas import Series
# def quarter_volume():
#     data = pd.read_csv('apple.csv',header=0)
#     # i = pd.to_datetime(data['Date'].values)
#     # t = data['Volume'].values
#     # result = pd.Series(t,index= i)
#     # p = result.resample('Q').sum()
#     # k = p.sort_values()
#
#     s = pd.Series(data['Volume'].values,index= pd.to_datetime(data['Date']))
#     second_volume = s.resample('Q').sum().sort_values()[-2]
#     return second_volume


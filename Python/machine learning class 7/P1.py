import pandas as pd

stu = {'번호': [1, 2, 3, 4, 5],
       '이름': ['개나리', '진달래', '무궁화', '모과', '월계수'],
       '생년': [1975, 1980, 1992, 2004, 1998]}
df = pd.DataFrame(stu)
df['학과'] = ['소개과', '임배과', '소개과', '임배과', '인공과']
#print(df)
df.loc[5] = ['6', '물망초', '2000', '소개과']
#print(df.dtypes)
df = df.astype({'번호': 'int64', '생년': 'int64'})
#print(df.dtypes)
#df.loc[(df['학과']=='소개과'),['이름','생년']]
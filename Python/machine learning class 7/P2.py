import pandas as pd

df1 = {'번호': ['1', '2', '3', '4', '5'],
       '이름': ['개나리', '진달래', '무궁화', '모과', '월계수'],
       '생년': [1975, 1980, 1992, 2004, 1998]}
stu1 = pd.DataFrame(df1)
df2 = {'번호': ['1', '2', '4', '6'],
       '이름': ['개나리', '진달래', '물망초', '모과'],
       '출생지': ['한국', '한국', '스위스', '캐나다']}
stu2 = pd.DataFrame(df2)
df = pd.merge(stu1, stu2, how='left')
for i, row in df.iterrows():
    birth_year = row['생년']
    if birth_year <= 2004:
        df['구분'] = '성인'
    elif birth_year <= 2007:
        df['구분'] = '고등학생'
    elif birth_year <= 2010:
        df['구분'] = '중학생'
    elif birth_year <= 2016:
        df['구분'] = '초등학생'
    else:
        df['구분'] = '응애'
print(df)

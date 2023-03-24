with open("url.txt",'r') as f:
    lines = f.readlines()

cnt = 0
for i in range(len(lines)):
   lines[i] = lines[i].split('/')


for i in lines:
    if i[2] == 'blog.naver.com':
        cnt += 1
print("blog.naver.com의 갯수는 모두",str(cnt)+"개 입니다.")
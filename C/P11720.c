#include <stdio.h>
#include <string.h>
int main() {
	int result=0,n,len,cnt=0;
    char a[101];
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        result=0;
        cnt=0;
        scanf("%s",a);
        len=strlen(a);
        for(int j=0;j<len;j++){
            if(a[j]=='O'){
                cnt++;
                result+=cnt;
            }else{
                cnt=0;
            }
        }
        printf("%d\n",result);
    }
}
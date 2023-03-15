#include <stdio.h>
#include <string.h>
int main(){
    int n, m, len;
    char a[2001];
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d %s",&m,a);
        len=strlen(a);
        for(int j=0;j<len;j++){
            for(int q=1;q<=m;q++){
                printf("%c",a[j]);
            }
        }
        printf("\n");
    }
}
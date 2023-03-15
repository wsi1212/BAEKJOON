#include <stdio.h>

int main(){
    int a[9]={0,}, max=0,result=0;
    for(int i=0;i<9;i++){
        scanf("%d", &a[i]);
        if(a[i]>=max){
            result=i+1;
            max=a[i];
        }
    }
    printf("%d %d", max, result);
}
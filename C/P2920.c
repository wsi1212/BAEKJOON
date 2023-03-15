#include <stdio.h>

int main(){
    int a[8]={0,};
    for(int i=0;i<8;i++)
        scanf("%d", &a[i]);
    for(int i=0;i<8;i++){
        if(a[i]!=i+1){
            for(int j=0;j<8;j++){
                if(a[j]!=8-j){
                    printf("mixed");
                    return 0;
                }
            }
            printf("descending");
            return 0;
        }
    }
    printf("ascending");
    return 0;
}
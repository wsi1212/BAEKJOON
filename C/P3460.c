#include <stdio.h>
#include <limits.h>

int main() {
    int n, num,j=0;
    int a[10000]={0,};
    scanf("%d", &n);
    for(int i=1;i<=n;i++){
        scanf("%d", &num);
        j=1;
        while(num!=0){
            a[j]=num%2;
            num/=2;
            j++;
        }
        for(int k=1;k<=j;k++){
            if(a[k]==1)
                printf("%d ", k-1);
        }
        printf("\n");
    }
}

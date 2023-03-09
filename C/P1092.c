#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int compare(const void *a, const void *b) // 오름차순 비교 함수 구현
{
    int num1 = *(int *)a; // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴
    int num2 = *(int *)b; // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴

    if (num1 > num2) // a가 b보다 작을 때는
        return -1;   // -1 반환

    if (num1 < num2) // a가 b보다 클 때는
        return 1;    // 1 반환

    return 0; // a와 b가 같을 때는 0 반환
}

int main()
{
    int box[5000] = {
        0,
    },
    con[50000] = {
        0,
    };
    int n, m, t=0 , temp= 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &con[i]);
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++)
    {
        scanf("%d", &box[i]);
    }
    qsort(box, sizeof(box) / sizeof(int), sizeof(int), compare);
    qsort(con, sizeof(con) / sizeof(int), sizeof(int), compare);
    if (box[0] > con[0])
    {
        printf("-1");
        return 0;
    }
    else
    {
        while (box[0]!= 0)
        {
            t++;
            temp=0;
            for (int i = 0; i < n; i++)
            {
                if (con[i] >= box[0])
                {
                    box[0] = 0;
                    qsort(box, sizeof(box) / sizeof(int), sizeof(int), compare);
                }else{
                    while(con[i]<box[temp])
                        temp++;
                    if(box[temp]!=0)
                    box[temp]=0;
                    qsort(box, sizeof(box) / sizeof(int), sizeof(int), compare);
                }
            }
        }
    }
    printf("%d", t);
}

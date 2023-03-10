#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void merge(int data[], int p, int q, int r) {
    int i = p, j = q + 1, k = p;
    int tmp[50000];//임시 배열
    while (i <= q && j <= r) {
        if (data[i] <= data[j])
            tmp[k++] = data[i++];
        else
            tmp[k++] = data[j++];
    }
    // MARK: - 한쪽이 끝날때까지 정렬. 그 후 다른 한쪽에서 남은 값들은 이미 정렬됐으므로 그대로 넣어주면 됨.
    while (i <= q)
        tmp[k++] = data[i++];
    while (j <= r)
        tmp[k++] = data[j++];
    for (int i = p; i <= r; i++) {
        data[i] = tmp[i];
    }//합병한 값을 원래 배열에 넣어줌
}

void mergeSort(int data[], int p, int r) {//오름차순
    if (p < r) {
        int q = (p + r) / 2;
        mergeSort(data, p, q);//전반부 정렬
        mergeSort(data, q + 1, r);//후반부 정렬
        merge(data, p, q, r);//합병
    }
}

int main() {
    int box[50000] = {
            0,
    },
            con[500] = {
            0,
    };
    int check[50000] = {0,};
    int n, m, t = 0, temp = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &con[i]);//크래인
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &box[i]);//박스
    }
    mergeSort(box, 0, m - 1);//오름차순
    mergeSort(con, 0, n - 1);//오름차순
    if (box[m - 1] > con[n-1]) {
        printf("-1");
        return 0;
    } else {
        while (check[m - 1] == 0) {
            t++;
            temp = 0;

            for (int i = 0; i < n; i++) {
                mergeSort(box, 0, m - 1);
                if (con[i] < box[0]) {//이 크래인이 아무 박스도 못드는 경우
                    continue;
                }
                while (check[temp] == 1)
                    temp++;
                if(temp>=50){
                    return 0;
                }
                if (con[i] >= box[n-temp] && check[temp] != 1) {
                    check[temp] = 1;//검사 했다는 의미
                    for (int i = 0; i < m; i++)
                        printf("%d ", check[i]);
                    printf("%d %d %d\n", temp, box[temp], con[i]);
                } else {
                    while (con[i] < box[temp])
                        temp++;
                    if (check[temp]!=1 && con[i] >= box[n-temp]) {
                        check[temp] = 1;
                        for (int i = 0; i < m; i++)
                            printf("%d ", check[i]);
                        printf("%d %d %d\n", temp, box[temp], con[i]);
                    }
                }
            }
        }
    }

    printf("\n%d", t);
}

#include <stdio.h>
int main() {
	int n, a, b, c, sy=1;
	scanf("%d", &n);
	b = n%10+n/10;//각 자리수의 합 42->6
	a = n % 10;//일의 자리 수 42-> 2
	c = a * 10 + b%10;//새로운 수
	while (c!=n) {
		if (c < 10) {
			b = c;
			a = c;
			c = a * 10 + b;
		}
		else {
			b = c % 10 + c / 10;
			a = c % 10;
			c = a * 10 + b % 10;
		}
		sy++;



	}
	printf("%d", sy);
}
#include <stdio.h>

void algorithm(int n) {
	    int a = 2;          /* 执行时间：1 ns */
	        a = a + 1;          /* 执行时间：1 ns */
		    a = a * 2;          /* 执行时间：10 ns */

		        /* 循环 n 次 */
		        for (int i = 0; i < n; i++) {
				        printf("%d", 0); /* 执行时间：5 ns */
					    }
}

int main() {
	    int n = 10;

	        algorithm(n);

		    return 0;
}

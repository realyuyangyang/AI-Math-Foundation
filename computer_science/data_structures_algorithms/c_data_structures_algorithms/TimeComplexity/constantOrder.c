#include <stdio.h>

/* 算法 A 的时间复杂度：常数阶 O(1) */
void algorithm_A(int n) {
	    printf("%d\n", 0);
}

/* 算法 B 的时间复杂度：线性阶 O(n) */
void algorithm_B(int n) {
	    for (int i = 0; i < n; i++) {
		            printf("%d\n", 0);
			        }
}

/* 算法 C 的时间复杂度：常数阶 O(1) */
void algorithm_C(int n) {
	    for (int i = 0; i < 1000000; i++) {
		            printf("%d\n", 0);
			        }
}

int main(void) {
	    int n = 10;

	        algorithm_A(n);

		    algorithm_B(n);

		        algorithm_C(n);

			    return 0;
}

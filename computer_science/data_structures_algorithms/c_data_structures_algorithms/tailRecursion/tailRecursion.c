#include <stdio.h>

/* tail recursion */
int tailRecur(int n, int res) {
	    /* base case */
	    if (n == 0) {
		            return res;
			        }

	        /* tail recursive call */
	        return tailRecur(n - 1, res + n);
}

int main() {
	    int n = 5;

	        int result = tailRecur(n, 0);

		    printf("1 + 2 + ... + %d = %d\n", n, result);

		        return 0;
}

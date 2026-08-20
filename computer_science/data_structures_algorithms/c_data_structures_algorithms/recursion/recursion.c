#include <stdio.h>

/* recursion */
int recur(int n) {
	    /* base case */
	    if (n <= 1) {
		            return n;
			        }

	        /* recursive call */
	        int res = recur(n - 1);

		    /* return */
		    return n + res;
}

int main() {
	    int n = 5;

	        int result = recur(n);

		    printf("1 + 2 + ... + %d = %d\n", n, result);

		        return 0;
}

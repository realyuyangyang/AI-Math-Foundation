#include <stdio.h>

/* Fibonacci sequence: recursion */
int fib(int n) {
	    /* base cases: f(1) = 0, f(2) = 1 */
	    if (n == 1 || n == 2) {
		            return n - 1;
			        }

	        /* recursive relation: f(n) = f(n-1) + f(n-2) */
	        int res = fib(n - 1) + fib(n - 2);

		    /* return f(n) */
		    return res;
}

int main() {
	    int n = 10;

	        int result = fib(n);

		    printf("fib(%d) = %d\n", n, result);

		        return 0;
}

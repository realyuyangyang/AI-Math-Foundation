#include <stdio.h>
/* whileLoop */
int whileLoop(int n) {
	    int res = 0;
	        int i = 1;
		    /* sum from 1 to n */
		    while (i <= n) {
			            res += i;
				            i++;
					        }
		        return res;
}
int main(){
	    int n = 100;
	        int result = whileLoop(n);
		    printf("1 + 2 + ... + %d = %d\n", n, result);
		        return 0;
}

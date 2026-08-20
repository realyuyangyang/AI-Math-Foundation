#include <stdio.h>

int for_loop(int n) {
	    int sum = 0;

	        for (int i = 1; i <= n; i++) {
			        sum += i;
				    }

		    return sum;
}

int main(void) {
	    int result = for_loop(5);
	        printf("%d\n", result);

		    return 0;
}

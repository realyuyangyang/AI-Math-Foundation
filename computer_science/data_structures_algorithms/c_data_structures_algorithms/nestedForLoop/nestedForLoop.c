#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* nested for loop */
char *nestedForLoop(int n) {
	    /*
	     *      * Each "(i, j), " uses at most 26 characters
	     *           * for two 10-digit positive integers.
	     *                * Add 1 byte for the final '\0'.
	     *                     */
	    int size = n * n * 26 + 1;

	        char *res = malloc(size * sizeof(char));

		    if (res == NULL) {
			            return NULL;
				        }

		        /* initialize as an empty string */
		        res[0] = '\0';

			    /* loop i = 1, 2, ..., n */
			    for (int i = 1; i <= n; i++) {

				            /* loop j = 1, 2, ..., n */
				            for (int j = 1; j <= n; j++) {
						                char tmp[27];

								            snprintf(tmp, sizeof(tmp), "(%d, %d), ", i, j);

									                strncat(
													                res,
															                tmp,
																	                size - strlen(res) - 1
																			            );
											        }
					        }

			        return res;
}

int main() {
	    int n = 3;

	        char *result = nestedForLoop(n);

		    if (result != NULL) {
			            printf("%s\n", result);

				            free(result);
					        }

		        return 0;
}

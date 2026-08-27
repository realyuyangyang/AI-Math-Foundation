/* sequential list */

#include <stdio.h>

#define MAX_SIZE 10

/* 顺序表 */
typedef struct {
	    int data[MAX_SIZE];
	        int length;
} SqList;

/* 初始化顺序表 */
void initList(SqList *L) {
	    for (int i = 0; i < MAX_SIZE; i++) {
		            L->data[i] = 0;
			        }

	        L->length = 0;
}

/* 打印顺序表 */
void printList(SqList *L) {
	    printf("length = %d\n", L->length);

	        printf("data: ");
		    for (int i = 0; i < MAX_SIZE; i++) {
			            printf("%d ", L->data[i]);
				        }
		        printf("\n");
}

int main(void) {
	    SqList L;

	        initList(&L);

		    printList(&L);

		        return 0;
}

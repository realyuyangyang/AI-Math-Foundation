/* sequential list */

#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 10

/* 元素类型 */
typedef int ElemType;

/* 顺序表 */
typedef struct {
	    ElemType data[MAX_SIZE];
	        int length;
} SqList;

/* 初始化顺序表 */
void initList(SqList *L) {
	    for (int i = 0; i < MAX_SIZE; i++) {
		            L->data[i] = 0;
			        }

	        L->length = 0;
}

/* 插入操作 */
bool listInsert(SqList *L, int i, ElemType e) {

	    /* 判断插入位置是否合法 */
	    if (i < 1 || i > L->length + 1) {
		            return false;
			        }

	        /* 判断顺序表是否已满 */
	        if (L->length >= MAX_SIZE) {
			        return false;
				    }

		    /* 将第 i 个位置及其后的元素向后移动 */
		    for (int j = L->length; j >= i; j--) {
			            L->data[j] = L->data[j - 1];
				        }

		        /* 插入新元素 */
		        L->data[i - 1] = e;

			    /* 顺序表长度加 1 */
			    L->length++;

			        return true;
}

/* 打印顺序表 */
void printList(SqList *L) {
	    printf("length = %d\n", L->length);

	        printf("data: ");

		    for (int i = 0; i < L->length; i++) {
			            printf("%d ", L->data[i]);
				        }

		        printf("\n");
}

int main(void) {
	    SqList L;

	        initList(&L);

		    listInsert(&L, 1, 10);
		        listInsert(&L, 2, 20);
			    listInsert(&L, 3, 30);
			        listInsert(&L, 2, 15);

				    printList(&L);

				        return 0;
}

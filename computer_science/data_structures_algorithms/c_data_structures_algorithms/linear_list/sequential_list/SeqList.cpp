/* sequential list */

#include <iostream>

#define MAX_SIZE 10

using namespace std;

/* 元素类型 */
typedef int ElemType;

/* 顺序表 */
typedef struct {
	    ElemType data[MAX_SIZE];
	        int length;
} SqList;

/* 初始化顺序表 */
void initList(SqList &L) {
	    for (int i = 0; i < MAX_SIZE; i++) {
		            L.data[i] = 0;
			        }

	        L.length = 0;
}

/* 插入操作 */
bool listInsert(SqList &L, int i, ElemType e) {
	    /* 判断插入位置是否合法 */
	    if (i < 1 || i > L.length + 1) {
		            return false;
			        }

	        /* 判断顺序表是否已满 */
	        if (L.length >= MAX_SIZE) {
			        return false;
				    }

		    /* 将第 i 个位置及其后的元素向后移动 */
		    for (int j = L.length; j >= i; j--) {
			            L.data[j] = L.data[j - 1];
				        }

		        /* 插入新元素 */
		        L.data[i - 1] = e;

			    /* 顺序表长度加 1 */
			    L.length++;

			        return true;
}

/* 删除操作 */
bool listDelete(SqList &L, int i, ElemType &e) {
	    /* 判断删除位置是否合法 */
	    if (i < 1 || i > L.length) {
		            return false;
			        }

	        /* 保存被删除的元素 */
	        e = L.data[i - 1];

		    /* 将第 i 个位置之后的元素向前移动 */
		    for (int j = i; j < L.length; j++) {
			            L.data[j - 1] = L.data[j];
				        }

		        /* 顺序表长度减 1 */
		        L.length--;

			    return true;
}

/* 按值查找 */
int locateElem(const SqList &L, ElemType e) {
	    for (int i = 0; i < L.length; i++) {
		            if (L.data[i] == e) {
				                /* 返回逻辑位置 */
				                return i + 1;
						        }
			        }

	        /* 查找失败 */
	        return 0;
}

/* 按位查找 */
ElemType getElem(const SqList &L, int i) {
	    /* 假设传入的位置合法 */
	    return L.data[i - 1];
}

/* 打印顺序表 */
void printList(const SqList &L) {
	    cout << "length = " << L.length << endl;

	        cout << "data: ";

		    for (int i = 0; i < L.length; i++) {
			            cout << L.data[i] << " ";
				        }

		        cout << endl;
}

int main() {
	    SqList L;

	        /* 初始化 */
	        initList(L);

		    /* 插入元素 */
		    listInsert(L, 1, 10);
		        listInsert(L, 2, 20);
			    listInsert(L, 3, 30);
			        listInsert(L, 2, 15);

				    cout << "After insertion:" << endl;
				        printList(L);

					    /* 按位查找 */
					    cout << "Element at position 3: "
						             << getElem(L, 3) << endl;

					        /* 按值查找 */
					        int position = locateElem(L, 20);

						    cout << "Position of 20: "
							             << position << endl;

						        /* 删除元素 */
						        ElemType deletedElem;

							    if (listDelete(L, 2, deletedElem)) {
								            cout << "Deleted element: "
										                 << deletedElem << endl;
									        }

							        cout << "After deletion:" << endl;
								    printList(L);

								        return 0;
}

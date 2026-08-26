#include <stdio.h>
#include <stdlib.h>

/* 链表节点 */
typedef struct ListNode {
	    int val;
	        struct ListNode *next;
} ListNode;

/* 创建链表节点 */
ListNode *newListNode(int val) {
	    ListNode *node = malloc(sizeof(ListNode));
	        node->val = val;
		    node->next = NULL;
		        return node;
}

/* 二叉树节点 */
typedef struct TreeNode {
	    int val;
	        struct TreeNode *left;
		    struct TreeNode *right;
} TreeNode;

/* 创建二叉树节点 */
TreeNode *newTreeNode(int val) {
	    TreeNode *node = malloc(sizeof(TreeNode));
	        node->val = val;
		    node->left = NULL;
		        node->right = NULL;
			    return node;
}

/* 函数 */
int func() {
	    /* 执行某些操作 */
	    return 0;
}

/* 常数阶 O(1) */
void constant(int n) {
	    /* 常量、变量占用 O(1) 空间 */
	    const int a = 0;
	        int b = 0;

		    /* 固定长度数组占用 O(1) 空间 */
		    int nums[1000];

		        /* 单个节点占用 O(1) 空间 */
		        ListNode *node = newListNode(0);
			    free(node);

			        /* 循环中的变量占用 O(1) 空间 */
			        for (int i = 0; i < n; i++) {
					        int c = 0;
						    }

				    /* 循环中的函数调用占用 O(1) 空间 */
				    for (int i = 0; i < n; i++) {
					            func();
						        }
}

/* 线性阶 O(n) */
void linear(int n) {
	    /* 长度为 n 的数组占用 O(n) 空间 */
	    int *nums = malloc(sizeof(int) * n);
	        free(nums);

		    /* 长度为 n 的链表节点数组占用 O(n) 空间 */
		    ListNode **nodes = malloc(sizeof(ListNode *) * n);

		        for (int i = 0; i < n; i++) {
				        nodes[i] = newListNode(i);
					    }

			    /* 内存释放 */
			    for (int i = 0; i < n; i++) {
				            free(nodes[i]);
					        }

			        free(nodes);
}

/* 平方阶 O(n^2) */
void quadratic(int n) {
	    /* n × n 二维数组占用 O(n^2) 空间 */
	    int **numMatrix = malloc(sizeof(int *) * n);

	        for (int i = 0; i < n; i++) {
			        numMatrix[i] = malloc(sizeof(int) * n);

				        for (int j = 0; j < n; j++) {
						            numMatrix[i][j] = 0;
							            }
					    }

		    /* 内存释放 */
		    for (int i = 0; i < n; i++) {
			            free(numMatrix[i]);
				        }

		        free(numMatrix);
}

/* 指数阶 O(2^n)：建立满二叉树 */
TreeNode *buildTree(int n) {
	    /* 终止条件 */
	    if (n == 0)
		            return NULL;

	        TreeNode *root = newTreeNode(0);

		    root->left = buildTree(n - 1);
		        root->right = buildTree(n - 1);

			    return root;
}

/* 释放二叉树 */
void freeTree(TreeNode *root) {
	    /* 终止条件 */
	    if (root == NULL)
		            return;

	        freeTree(root->left);
		    freeTree(root->right);

		        free(root);
}

/* 对数阶 O(log n) */
void logarithmic(int n) {
	    /* 终止条件 */
	    if (n <= 1)
		            return;

	        /* 每次将问题规模缩小为原来的一半 */
	        logarithmic(n / 2);
}

int main() {
	    int n = 10;

	        /* 常数阶 O(1) */
	        constant(n);

		    /* 线性阶 O(n) */
		    linear(n);

		        /* 平方阶 O(n^2) */
		        quadratic(n);

			    /* 指数阶 O(2^n) */
			    TreeNode *root = buildTree(n);
			        freeTree(root);

				    /* 对数阶 O(log n) */
				    logarithmic(n);

				        return 0;
}

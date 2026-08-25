#include <stdio.h>

/* 1. 常数阶 O(1) */
int constant(int n) {
    int count = 0;
    int size = 100000;

    /* 循环次数固定，与 n 无关 */
    for (int i = 0; i < size; i++) {
        count++;
    }

    return count;
}


/* 2. 线性阶 O(n) */
int linear(int n) {
    int count = 0;

    /* 循环 n 次 */
    for (int i = 0; i < n; i++) {
        count++;
    }

    return count;
}


/* 3. 平方阶 O(n^2) */
int quadratic(int n) {
    int count = 0;

    /* 两层循环，每层都循环 n 次 */
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            count++;
        }
    }

    return count;
}


/* 4. 指数阶 O(2^n) */
int exponential(int n) {
    int count = 0;
    int base = 1;

    /* 每轮工作量依次为 1, 2, 4, 8, ..., 2^(n-1) */
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < base; j++) {
            count++;
        }

        base *= 2;
    }

    /* count = 1 + 2 + 4 + ... + 2^(n-1) = 2^n - 1 */
    return count;
}


/* 5. 对数阶 O(log n) */
int logarithmic(int n) {
    int count = 0;

    /* 每轮将 n 缩小为原来的一半 */
    while (n > 1) {
        n = n / 2;
        count++;
    }

    return count;
}


/* 6. 线性对数阶 O(n log n) */
int linearLogRecur(int n) {
    if (n <= 1) {
        return 1;
    }

    /* 将问题分成两个规模为 n / 2 的子问题 */
    int count = linearLogRecur(n / 2)
              + linearLogRecur(n / 2);

    /* 当前层执行 n 次操作 */
    for (int i = 0; i < n; i++) {
        count++;
    }

    return count;
}


/* 7. 阶乘阶 O(n!) */
int factorialRecur(int n) {
    if (n == 0) {
        return 1;
    }

    int count = 0;

    /* 当前问题产生 n 个规模为 n - 1 的子问题 */
    for (int i = 0; i < n; i++) {
        count += factorialRecur(n - 1);
    }

    return count;
}


int main(void) {
    int n = 5;

    printf("constant:       %d\n", constant(n));
    printf("linear:         %d\n", linear(n));
    printf("quadratic:      %d\n", quadratic(n));
    printf("exponential:    %d\n", exponential(n));
    printf("logarithmic:    %d\n", logarithmic(n));
    printf("linearLogRecur: %d\n", linearLogRecur(n));
    printf("factorialRecur: %d\n", factorialRecur(n));

    return 0;
}
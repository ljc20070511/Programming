//
// Created by HUAWEI on 2026/2/13.
//
#include<stdio.h>
void ic(void);
void br(void);
int main(void) {
    printf("Brazil,Russia,India,China\n");
    ic();
    br();
    return 0;
}
void ic(void) {
    printf("India,China\n");
}
void br(void) {
    printf("Brazil,Russia\n");
}
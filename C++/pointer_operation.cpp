#include <stdio.h>
#include <cstdlib>

void update(int *a,int *b) {
    // Complete this function   
    int temp = *a;
    *a = *a + *b;
    *b = abs(temp - *b); 
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    printf("Enter 2 numbers: \n");
    scanf("%d %d", &a, &b);
    update(pa, pb);

    printf("Sum and absolute difference are: \n%d\n%d\n", a, b);

    return 0;
}
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    // in the first line, take the number of elements
    int n;
    printf("provide the number of elements:\n");
    scanf("%d", &n);
    if (1 <= n && n <=1000){
        // store the values in the array
        int arr[n];
        
        printf("provide the elements to print in reverse order: \n");
        for(int i=0; i<n; i++){
            scanf("%d", &arr[i]);
        }

        // print the elements of the array in reverse order
        for (int i=n; i>=0; i--){
            if (1 <= arr[i] && arr[i] <=10000){
                printf("%d ", arr[i]);
            }
        }
    } else {
        printf("number of elements outside bounds");
    }

    return 0;
}

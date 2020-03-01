#include <iostream>
#include <cstdio>
using namespace std;

int max_of_four(int a, int b, int c, int d){
  int max_value;
  if ((a>b) && (a>c) && (a>d)){
    max_value = a;
  } else if ((b>a) && (b>c) && (b>d)){
    max_value = b;
  } else if ((c>a) && (c>b) && (c>d)){
    max_value = c;
  } else if ((d>a) && (d>b) && (d>c)){
    max_value = d;
  }
  return max_value;
}

int max_of_four_improved(int a, int b, int c, int d){
  int e = a > b ? a : b;
  int f = c > d ? c : b;
  return (e > f ? e : f);
}

int main() {
  int a, b, c, d;
  printf("Enter four numbers: \n");
  scanf("%d %d %d %d", &a, &b, &c, &d);
  int ans = max_of_four(a, b, c, d);
  printf("Their max is: %d\n", ans);
  int ans2 = max_of_four_improved(a, b, c, d);
  printf("Their max is: %d\n", ans);
                    
  return 0;
}

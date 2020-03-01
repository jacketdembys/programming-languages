// tell the compiler that we want to use the iostream
#include<iostream>

using namespace std;

int main(){

    cout << "Enter three numbers : " << endl;
    int v1 =0, v2 = 0, v3 = 0;
    cin >> v1 >> v2 >> v3;
    cout << "The sum of " << v1 << " and " << v2 << " is " << v1+v2 <<"." << endl;
    cout << "The sum of " << v1 << " and " << v2 << " and " << v3 << " is " << v1+v2+v3 <<"." << endl;

    return 0;

}
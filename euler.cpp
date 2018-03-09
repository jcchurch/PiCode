#include <iostream>
using namespace std;
int main() {
    double pi=0,d=1.0;
    for (int i = 0;i < 1000000;i++) {
        pi+=(4.0/d)-(4.0/(d+2.0));
        d+=4.0;
    }
    cout << pi << endl;
    return 0;
}

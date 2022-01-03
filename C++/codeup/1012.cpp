#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    float n ;
    cin >> n;
    cout << fixed << setprecision(6) << n;
}

/* 
기본 cout 정밀도는 6이다. (숫자6개를 출력) 출력자릿수 조정이 필요하므로 iomanip헤더의 setprecision기능을 사용 

fixed와 setprecisino을 같이 쓰게되면, 소수점만 n자리수 출력합니다.

fixed가 없다면, 정수와 소수부분을 합쳐서 n자리수로 출력하게 됩니다.
*/

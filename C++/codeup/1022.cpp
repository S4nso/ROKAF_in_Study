#include <iostream>
#include <iomanip>

using namespace std;
int main(){
    
    char data[2000];
    
    cin.getline(data,2000,'\n'); // data에 2000단어까지 가능하고 줄바꿈(enter)시끝낸다
    cout << data;
    
    return 0;
}

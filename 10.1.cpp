#include <iostream>
#include <windows.h>
using namespace std;

int add(int x,int y){
    return x+y;
}

int maaaaain(){
    cout << add(2,3);
    return 0;
}

int main()
{
	SetConsoleOutputCP(65001);
    cout << "Hello C++" << endl;
    int a;
    cin >>a;
    if(a>60){
        cout <<"及格"; 
    }
    else{
        cout <<"不及格";
    }
    int i; 
    for(i=1;i<=10;i++){
        cout << i << endl;
    } 
    int j=1;
    i = 1; 
    while(i<=10){
        cout <<i;
        i++; 
    }
    int arr[5]={10,20,30,40,50};
    
    return 0;
}
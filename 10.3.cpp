#include<iostream>
#include<unordered_map>
#include<string>
#include<windows.h>
using namespace std;
bool isAnagram(string s,string t){
    if(s.size()!=t.size())
        return false;
    unordered_map<char,int>mp;
    for(char c: s){
        mp[c]++;
    }
    for(char c: t){
        mp[c]--;
        if(mp[c]<0)
            return false;
    }
    return true;
}
int main(){
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
    string s,t;
    cout <<"输入s:";
    cin >>s;
    cout <<"输入t:";
    cin >>t;
    bool res=isAnagram(s,t);
    if(res)
        cout <<"true"<<endl;
    else
        cout <<"false"<<endl;
    return 0;
}
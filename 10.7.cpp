#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;
    int fourSumCount(vector<int>&A,vector<int>&B,vector<int>&C,vector<int>&D){
    unordered_map<int,int>umap;
    for (int a:A){
        for(int b:B){
            umap[a+b]++;
        }
    }
    int count=0;
    for (int c:C){
        for (int d:D){
            if(umap.find(0-(c+d))!=umap.end()){
                count+=umap[0-(c+d)];
            }
        }
    }
    return count;
  }

int main(){
    vector<int> nums1={-1,-1};
    vector<int> nums2={-1,1};
    vector<int> nums3={-1,1};
    vector<int> nums4={1,-1};
    int res =fourSumCount(nums1,nums2,nums3,nums4);
    cout<<"answer=:"<<res<<endl;
    return 0;
}

// #include<iostream>
// using namespace std;
// int main(){
// cout<<43<<endl;
// return 0;}
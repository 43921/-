// #include<iostream>
// using namespace std; 
// int main()
// {
//     int i,a[11],b;
//     int c=0;
//     for(i=1;i<=10;i++)
//     {
//         cin >>a[i];
//     }
//     cin >>b;
//     for(i=1;i<=10;i++)
//     {
//       if (a[i] <= b+30)
//           c++;  
//     }
//     cout <<c;
//     return 0;
// }
// #include <iostream>
// #include <vector>
// #include <unordered_map>
// #include <windows.h>
// using namespace std;

// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         unordered_map<int,int> mp;
//         int n = nums.size();
//         for(int i = 0; i < n; i++)
//         {
//             int need = target - nums[i];
//             if(mp.count(need))
//             {
//                 return {mp[need], i};
//             }
//             mp[nums[i]] = i;
//         }
//         return {};
//     }
// };

// int main()
// {
//     SetConsoleOutputCP(65001);
//     Solution sol;
//     vector<int> nums;
//     int n, target, x;

//     cout << "请输入数组元素个数：";
//     cin >> n;
//     cout << "请输入" << n << "个数字：";
//     for(int i = 0; i < n; i++)
//     {
//         cin >> x;
//         nums.push_back(x);
//     }
//     cout << "请输入target：";
//     cin >> target;

//     vector<int> res = sol.twoSum(nums, target);
//     cout << "答案下标：" << res[0] << " " << res[1] << endl;

//     return 0;
// }
 

#include<iostream>
#include<vector>
#include<unordered_map>
//#include<cstdlib>
using namespace std;
vector<int> twosum(vector<int>& nums,int target){
    unordered_map<int,int>hashmap;
    for(int i=0;i<nums.size();i++){
        int num=nums[i];
        int need=target -num;
        if(hashmap.find(need)!=hashmap.end()){
            return {hashmap[need],i};
        }
        hashmap[num]=i;
    }
    return {};
}
int main(){
    //system("chcp 65001");
    vector<int> nums={2,7,11,15};
    int target=9;
    vector<int> res=twosum(nums,target);
    cout<<"两个下标：" <<res[0]<< ","<<res[1]<<endl;
    return 0;
}
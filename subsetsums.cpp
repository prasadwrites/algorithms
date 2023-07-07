#include<iostream>
#include<vector>
using namespace std;

vector<int> bag = { 2, 8, -2 };
int sum = 6, index=0;
int bagSize;
bool flag = false;

bool printSubsetSums(int index , vector<int> slate){

    //basecase
    if(index == bagSize){
        cout << endl;
        int subsetSum = 0;
        int sizeSlate = slate.size();
        for (auto i : slate){
            //cout << i << " ";
            subsetSum = subsetSum + i;
        }
        if(subsetSum == sum){
            cout <<endl<<"sum found" <<endl;
            for (auto i : slate){
                cout << i << " ";
            }
            flag = true;
            return flag;
        }
        return flag;
    }

    //recursion
    printSubsetSums(index+1 , slate);
    slate.push_back(bag[index]);
    printSubsetSums(index+1, slate);
    slate.pop_back();
}



int main(){

    cout<< "Subset sums"<<endl;
    bagSize = bag.size();
    vector<int> slate ;
    printSubsetSums(index, slate) ;
    cout <<  std::boolalpha << flag;

}
#include <iostream>
#include <vector>

using namespace std;

class StringNum {
public:
    vector<string> result;
    string bag;

    StringNum(string str): bag(str){};
    ~StringNum(){};

    void helper(char *slate, int index){
    //base case

        if (index == bag.length()){
            result.push_back(string(slate));
            return;
        }

    //if its a digit
        if (isdigit(bag[index])){
            slate[index] =  bag[index];
            helper(slate, ++index);
    } else {//if not a digit
        slate[index] = tolower(bag[index]);
        helper(slate, ++index);
        --index;
        slate[index] = toupper(bag[index]);
        helper(slate, ++index);
    }
}
};

int main(int arc, char* argv[]){

    #ifndef LOCAL_PROJECT
    freopen("input.txt", "r",stdin);
    freopen("output.txt", "w", stdout);
    #endif

    string s("a1b2");
    StringNum strObj(s);
    char *slate = (char *) malloc(s.length()*sizeof(char));
    strObj.helper(slate, 0);
    for(auto str : strObj.result){
        cout<<str<<endl;
    }
}


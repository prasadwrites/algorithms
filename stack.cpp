#include <iostream>
#include <vector>

using namespace std;


template <typename T>
class Stack {
public:
	vector <T> vec;
	size_t size;

	Stack(int temp){

		size = (size_t) temp;
	}

	void push(T val){
		cout << "stack size :"<< vec.size() << endl;
		if (vec.size() > size){
			cout << " Stack is full " << endl;
			return;
		}
		vec.push_back(val);
	} 

	T pop(){
		if(vec.empty()){
			cout<< "Stack is empty"<< endl;
			return 0;
		}
		T temp = vec.back();
		vec.pop_back();
		return temp;
	}

	T peek() {
		if (vec.empty()){
			cout<< "Stack is empty" << endl;
			return 0;
		}
		return vec.back();

	}

	void printStack(){

		for ( T val : vec)
			cout << val << " " ;
		cout<<endl;
	}

	void operator << (T val) { 
		cout << "stack size :"<< vec.size() << endl;
         if (vec.size() > size){
			cout << " Stack is full " << endl;
			return;
		}
		vec.push_back(val);
        
    } 


};

int main( int argc, char *argv[]){
	Stack<int> stack(2);
	stack.push(2);

	stack.printStack();
	stack.push(3);
	stack.printStack();
	stack.push(4);
	stack.printStack();
	stack.push(5);
	stack.printStack();
	stack<< 6;
	stack.printStack();
	cout << stack.pop() << endl;
	stack.printStack();
	cout << stack.peek() << endl;
	stack.printStack();
	return 0;


}
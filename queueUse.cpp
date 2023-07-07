
#include <tbb/concurrent_queue.h>
#include <tbb/concurrent_priority_queue.h>
#include <iostream>


int array[10] = { 0,11,22,33,44,55,66,77,88,99 };



void test_queue() {
    //creation of concurrent queue
    tbb::concurrent_queue <int> queue;
    int val;

    //pushing the array items into the queue one by one
    for (int i = 0; i < 10; ++i)
        queue.push(array[i]);


    std::cout << "poped values are " << std::endl;
    //trying to pop out the values one bye one
    for (int i = 0; i < 10; i++) {
        queue.try_pop(val);
        std::cout << val << std::endl;

    }
        
    std::cout << std::endl;
}


int main()
{
    test_queue();
    return 0;
}
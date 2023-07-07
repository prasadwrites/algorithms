#include<iostream>

class TreeNode {
public:
    int data;
    TreeNode* left;
    TreeNode* right;
};

TreeNode* newNode(int data)
{
    TreeNode* node = new TreeNode();
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

TreeNode* createBST(int* arr, int start, int end)
{
    if (start > end) return NULL;
    int mid = (start + end) / 2;
    TreeNode* root = newNode(arr[mid]);
    root->left = createBST(arr, start, mid - 1);
    root->right = createBST(arr, mid + 1, end);
    return root;
}



int main(int argc, char argv[]) {

    int arr[] = { 0, 1,2,3,4,5,6,7,8,9 ,10 };
    int start = 0, end = sizeof(arr) / sizeof(arr[0]);
    TreeNode* root = createBST(arr, start, end-1);
    return 0;
}
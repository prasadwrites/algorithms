#include <iostream>
int main(int argc, char argv[]) {
    //int arr[] = { 5, 10, 1, 3, 3, 7, 60 };
    int arr[] = { 5, 12, 1, 3, 3, 7, 60 };
    int start = 2, sum = 0, xsum = 0, xstart = 0, xend = 0;
    int maxHome = arr[0] + 2;
    int maxCandy = arr[1];
    for (auto end = 2; end <= maxHome + 2; end++) {
        if ((sum > xsum)& (sum < maxCandy)) {
            xsum = sum;
            xstart = start - 2;
            xend = end - 3;
        }
        if ((end == maxHome) & (sum < maxCandy)) {
            printf("1.start from house %d and end in %d to get max %d candies", xstart, xend + 1, sum);
            return 0;
        }
        sum = sum + arr[end];
        if (sum == maxCandy) {
            printf("2.start from house %d and end in %d to get max %d candies", start - 1, end - 1, maxCandy);
            return 0;
        }
        else if (sum > maxCandy) {
            while (sum > maxCandy) {
                sum = sum - arr[start];
                if ((sum > xsum)& (sum < maxCandy)) {
                    xsum = sum;
                    xstart = start;
                    xend = end;
                }
                start++;
            }
            if ((sum == 0) & (start == maxHome)) {
                printf("3.start from house %d and end in %d to get max %d candies", xstart, xend - 1, xsum);
                return 0;
            }
            if (sum == maxCandy) {
                printf("4. start from house %d and end in %d to get max %d candies", start - 1, end - 1, maxCandy);
                return 0;
            }
        }
        if (start == maxHome) {
            printf("No Home Found");
            return 0;
        }
    }
}
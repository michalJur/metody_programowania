#include <iostream>
#include <vector>
#include <chrono>
#include <algorithm>
#include <cstdlib>  // for rand() and srand()
#include <ctime>    // for time()
#include <fstream>  // for file operations
#include <iomanip>

using namespace std;

// Linear Search
int linearSearch(const vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

// Binary Search (must be sorted)
int binarySearch(const vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target)
            return mid;
        if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}


template<typename Func>
double measureExecutionTime(Func func, int& result) {
    auto start = chrono::high_resolution_clock::now();
    result = func();
    auto end = chrono::high_resolution_clock::now();
    return chrono::duration<double>(end - start).count();
}


int main() {
    int sizesCount = 10;
    int sizesSkip = 5000000; //50000000;
    int runsPerSize = 5;
   
    int size = sizesSkip;
    vector<int> sizes(sizesCount);
    for (int i = 0; i < sizesCount; ++i) {
        sizes[i] = size;
        size += sizesSkip;
    }

    
    ofstream outFile("search_results_cpp.csv");
    outFile << "Size,Run,Target,LinearTime,BinaryTime,LinearResSult,BinaryResult\n";
    
    srand(time(nullptr));
    
    for (int n : sizes) {
        cout << "Testing array size: " << n << endl;
        
        // Create sorted array of size n
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            arr[i] = i;
        }
        
        for (int run = 0; run < runsPerSize; ++run) {
            int target = rand() % n;
            // int target = (int) ((0.5 * n) + 1) ;
            
            int indexLinear;
            double timeLinear = measureExecutionTime([&]() {
                return linearSearch(arr, target);
            }, indexLinear);
            
            int indexBinary;
            double timeBinary = measureExecutionTime([&]() {
                return binarySearch(arr, target);
            }, indexBinary);

            // Write to console
            cout << "  Run " << run + 1 << ": Target=" << target 
                 << " Linear=" << fixed << setprecision(8) << timeLinear 
                 << " Binary=" << timeBinary << endl;

            // Write to file
            outFile << n << "," << run + 1 << "," << target << "," 
                   << timeLinear << "," << timeBinary << "," 
                   << indexLinear << "," << indexBinary << "\n";
        }
        cout << endl;
    }
    
    outFile.close();
    cout << "Results have been saved.\n";
    
    return 0;
}
# -*- coding: utf-8 -*-
"""
C Programming - Module 2: Arrays and String Handling
Questions 27 to 52 (1D Arrays, 2D Arrays, Searching, Sorting, Strings, Safe I/O, and string.h Re-implementations)
"""

C_MODULE2_QUESTIONS = [
    {
        "num": 27,
        "title": "One-Dimensional Arrays: Declaration, Memory Layout, and Indexing",
        "category": "1D Arrays",
        "difficulty": "Fundamental",
        "exam_tags": ["Core Concept", "Viva Must-Know"],
        "question": "What is a one-dimensional array? Explain array declaration, initialization syntax (complete, partial, zero), 0-based indexing, and contiguous memory allocation with address proof.",
        "logic": "An array is a fixed-size, homogeneous collection of contiguous memory locations storing elements of identical data type under a single identifier.",
        "concept": "1. Definition: `data_type array_name[SIZE];`\n2. Memory Model: Elements are stored in contiguous memory cells. If element `arr[0]` is at address `0x1000`, and elements are 4-byte integers, then `arr[i]` is strictly at `0x1000 + i * sizeof(int)`.\n3. Initialization Variants:\n- Full: `int a[5] = {10, 20, 30, 40, 50};`\n- Partial: `int a[5] = {10, 20};` (remaining 3 elements are automatically initialized to 0).\n- Zero-init: `int a[5] = {0};` (all 5 elements initialized to 0).\n- Deduced size: `int a[] = {1, 2, 3};` (compiler sets size to 3).\n4. Bounds: Index ranges from `0` to `SIZE - 1`. C does NOT perform runtime boundary checking.",
        "syntax": "type name[size];\nAddress of element i = BaseAddress + i * sizeof(type)",
        "code": """#include <stdio.h>

int main(void) {
    int scores[5] = {85, 92, 78, 64, 99};

    printf("=== 1D Array Contiguous Memory Map ===\\n");
    printf("%-8s | %-6s | %-16s | %-10s\\n", "Index", "Value", "Memory Address", "Byte Offset");
    printf("-------------------------------------------------\\n");

    uintptr_t baseAddr = (uintptr_t)&scores[0];

    for (int i = 0; i < 5; i++) {
        uintptr_t currentAddr = (uintptr_t)&scores[i];
        printf("scores[%d] | %-6d | %p | +%td bytes\\n", 
               i, scores[i], (void*)&scores[i], currentAddr - baseAddr);
    }

    printf("\\nTotal Array Size in RAM: %zu bytes (%zu elements * %zu bytes)\\n", 
           sizeof(scores), sizeof(scores)/sizeof(scores[0]), sizeof(int));

    return 0;
}""",
        "output": """=== 1D Array Contiguous Memory Map ===
Index    | Value  | Memory Address   | Byte Offset
-------------------------------------------------
scores[0] | 85     | 0x7ffd5a68acb0   | +0 bytes
scores[1] | 92     | 0x7ffd5a68acb4   | +4 bytes
scores[2] | 78     | 0x7ffd5a68acb8   | +8 bytes
scores[3] | 64     | 0x7ffd5a68acbc   | +12 bytes
scores[4] | 99     | 0x7ffd5a68acc0   | +16 bytes

Total Array Size in RAM: 20 bytes (5 elements * 4 bytes)""",
        "explanation": "1. Every successive element address increases by exactly `4` bytes (`sizeof(int)`).\n2. This contiguous layout allows random access in $O(1)$ constant time via base address pointer arithmetic.\n3. `sizeof(scores) / sizeof(scores[0])` calculates array length at compile time.",
        "mistakes": [
            ("Declaring an array with empty size and no initializer: `int arr[];`.", "The compiler cannot deduce the memory to allocate. You must either specify the size `int arr[10];` or provide an initializer list `int arr[] = {1, 2};`."),
            ("Assuming `scores[5]` accesses the 5th element.", "With 0-based indexing, the 5th element is `scores[4]`. Accessing `scores[5]` is an out-of-bounds array access leading to undefined behavior.")
        ],
        "practice_q": "What are the contents of `int arr[5] = {1};` in C?"
    },
    {
        "num": 28,
        "title": "Array Operations: Minimum, Maximum, and Average Computation",
        "category": "1D Arrays",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "Exam Level"],
        "question": "Write a complete C program to read N integers into a 1D array. Compute and display the Maximum element, Minimum element, Sum, and Arithmetic Average with precision formatting.",
        "logic": "Initialize `max` and `min` with `arr[0]`. Iterate through the array starting from index 1. If an element is greater than `max`, update `max`. If an element is smaller than `min`, update `min`. Accumulate values into `sum`.",
        "concept": "1. Never initialize `max` with 0 or a hardcoded value if the array might contain negative numbers! Initializing with `arr[0]` guarantees correct results for all numerical ranges.\n2. Running Sum: Accumulate in an integer or 64-bit integer.\n3. Average: Must cast `(double)sum / n` to avoid integer division truncation.",
        "syntax": "if (arr[i] > max) max = arr[i];\nif (arr[i] < min) min = arr[i];",
        "code": """#include <stdio.h>

int main(void) {
    int arr[] = {45, -12, 89, 0, 104, -34, 76, 23};
    int n = sizeof(arr) / sizeof(arr[0]);

    int max = arr[0];
    int min = arr[0];
    long long sum = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];
        sum += arr[i];
    }

    double avg = (double)sum / n;

    printf("=== Array Statistical Analysis ===\\n");
    printf("Elements: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\\n");

    printf("Total Elements (N): %d\\n", n);
    printf("Maximum Element:    %d\\n", max);
    printf("Minimum Element:    %d\\n", min);
    printf("Cumulative Sum:     %lld\\n", sum);
    printf("Arithmetic Average: %.2f\\n", avg);

    return 0;
}""",
        "output": """=== Array Statistical Analysis ===
Elements: 45 -12 89 0 104 -34 76 23 
Total Elements (N): 8
Maximum Element:    104
Minimum Element:    -34
Cumulative Sum:     291
Arithmetic Average: 36.38""",
        "explanation": "1. `max` and `min` are safely seeded with `arr[0] = 45`.\n2. Iteration compares each element; `-34` successfully becomes `min` and `104` becomes `max`.\n3. Average is computed as `(double)291 / 8 = 36.375`, formatted to `36.38`.",
        "mistakes": [
            ("Initializing `min = 0`.", "If all numbers in the array are positive (e.g., `{10, 20, 30}`), `min` will incorrectly remain `0`."),
            ("Integer division in average: `double avg = sum / n;`.", "Divides integers first, losing fractional precision before assignment to double.")
        ],
        "practice_q": "How would you find the second largest element in a single pass through an array?"
    },
    {
        "num": 29,
        "title": "Linear Search Algorithm: Logic, Trace, and Complexity Analysis",
        "category": "Searching Algorithms",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Explain the Linear Search algorithm. Write a complete C program to search for a key element in an unsorted array. Analyze its Best, Worst, and Average time complexities.",
        "logic": "Compare the search key sequentially against every element in the array from index 0 to N-1. If a match is found, return the index and terminate early. If the end of the array is reached without a match, report element not found.",
        "concept": "Complexity Analysis:\n- Best Case: $O(1)$ (Key found at index 0 on the first comparison).\n- Worst Case: $O(N)$ (Key is at the very last index $N-1$, or not present in the array).\n- Average Case: $O(N)$ (Key found around the middle, requiring $(N+1)/2$ comparisons).\n- Space Complexity: $O(1)$ (In-place, requires no auxiliary storage).\nAdvantage: Works on unsorted, random data; requires no preprocessing.",
        "syntax": "for (int i = 0; i < n; i++) if (arr[i] == key) return i;",
        "code": """#include <stdio.h>

int linearSearch(const int arr[], int size, int key) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == key) {
            return i; /* Key found: Return 0-based index */
        }
    }
    return -1; /* Key not found */
}

int main(void) {
    int data[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(data) / sizeof(data[0]);

    int searchKeys[] = {22, 99};
    int numQueries = sizeof(searchKeys) / sizeof(searchKeys[0]);

    printf("Array: ");
    for (int i = 0; i < n; i++) printf("%d ", data[i]);
    printf("\\n\\n");

    for (int q = 0; q < numQueries; q++) {
        int target = searchKeys[q];
        int resultIndex = linearSearch(data, n, target);

        if (resultIndex != -1) {
            printf(">> Key %d FOUND at index %d (Position %d)\\n", 
                   target, resultIndex, resultIndex + 1);
        } else {
            printf(">> Key %d NOT FOUND in the array\\n", target);
        }
    }

    return 0;
}""",
        "output": """Array: 64 34 25 12 22 11 90 

>> Key 22 FOUND at index 4 (Position 5)
>> Key 99 NOT FOUND in the array""",
        "explanation": "1. For key `22`, the search checks indices 0, 1, 2, 3 before finding a match at index `4`.\n2. For key `99`, all 7 elements are examined with no match, returning `-1`.",
        "mistakes": [
            ("Printing 'Not Found' inside the search loop.", "If placed inside the loop, the program prints 'Not Found' on every mismatched iteration before finding the key!"),
            ("Not passing array length explicitly to the function.", "Arrays decay to pointers when passed to functions; `sizeof(arr)` inside `linearSearch` gives pointer size (4/8 bytes), not the array length.")
        ],
        "practice_q": "What is the sentinel linear search technique and how does it eliminate loop condition checking?"
    },
    {
        "num": 30,
        "title": "Binary Search Algorithm: Divide-and-Conquer with Trace",
        "category": "Searching Algorithms",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "High-Yield Exam"],
        "question": "State the mandatory precondition for Binary Search. Explain the divide-and-conquer strategy. Write a C program avoiding integer overflow in midpoint calculation, and derive its $O(\\log_2 N)$ complexity.",
        "logic": "Precondition: The array MUST be sorted. Binary search compares the target with the middle element. If equal, target is found. If target < mid, search left half; if target > mid, search right half. Each step halves the search space.",
        "concept": "1. Overflow-Safe Midpoint: Writing `mid = (low + high) / 2` causes integer overflow when `low + high` exceeds $2^{31}-1$. Safe formula: `mid = low + (high - low) / 2`.\n2. Recurrence Relation: $T(N) = T(N/2) + O(1)$. By Master Theorem, $T(N) = O(\\log_2 N)$.\n3. Comparison Count: For 1,000,000 items, linear search needs up to 1,000,000 comparisons, whereas binary search requires at most 20 comparisons ($2^{20} \\approx 1.04 \\times 10^6$).",
        "syntax": "int mid = low + (high - low) / 2;",
        "code": """#include <stdio.h>

int binarySearch(const int arr[], int size, int target) {
    int low = 0;
    int high = size - 1;
    int comparisons = 0;

    while (low <= high) {
        comparisons++;
        /* Overflow-safe midpoint computation */
        int mid = low + (high - low) / 2;

        if (arr[mid] == target) {
            printf("  [Target %d matched at mid index %d after %d comparison(s)]\\n", 
                   target, mid, comparisons);
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1; /* Discard left half */
        } else {
            high = mid - 1; /* Discard right half */
        }
    }

    printf("  [Target %d not found after %d comparisons]\\n", target, comparisons);
    return -1;
}

int main(void) {
    int sortedData[] = {11, 22, 33, 44, 55, 66, 77, 88, 99};
    int n = sizeof(sortedData) / sizeof(sortedData[0]);

    printf("Sorted Data: ");
    for (int i = 0; i < n; i++) printf("%d ", sortedData[i]);
    printf("\\n\\n");

    int idx1 = binarySearch(sortedData, n, 66);
    printf("Search 66 -> Index: %d\\n\\n", idx1);

    int idx2 = binarySearch(sortedData, n, 25);
    printf("Search 25 -> Index: %d\\n", idx2);

    return 0;
}""",
        "output": """Sorted Data: 11 22 33 44 55 66 77 88 99 

  [Target 66 matched at mid index 5 after 3 comparison(s)]
Search 66 -> Index: 5

  [Target 25 not found after 4 comparisons]
Search 25 -> Index: -1""",
        "explanation": "1. Search for 66:\n- Pass 1: low=0, high=8, mid=4 (arr[4]=55). Since 55 < 66, low becomes 5.\n- Pass 2: low=5, high=8, mid=6 (arr[6]=77). Since 77 > 66, high becomes 5.\n- Pass 3: low=5, high=5, mid=5 (arr[5]=66). Match found in 3 comparisons!\n2. Search for 25 terminates with `low > high`, returning `-1`.",
        "mistakes": [
            ("Applying Binary Search on an unsorted array.", "Binary search logic fundamentally relies on order. On unsorted data, it produces false negatives."),
            ("Using `low = mid` or `high = mid`.", "Can cause infinite loops when `high - low == 1`. Always use `mid + 1` and `mid - 1`.")
        ],
        "practice_q": "How many comparisons does binary search take in the worst case for an array of 64 elements?"
    },
    {
        "num": 31,
        "title": "Bubble Sort Algorithm with Early Termination Optimization",
        "category": "Sorting Algorithms",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Explain the Bubble Sort algorithm. Implement the pass-by-pass comparison logic in C with a swapped flag to achieve $O(N)$ best-case runtime for already sorted arrays.",
        "logic": "Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. Larger elements 'bubble up' to the end of the array with each pass.",
        "concept": "1. In pass $i$ (from 0 to $N-2$), the largest unsorted element settles into position $N-1-i$. Hence the inner loop only needs to run up to $N-1-i$.\n2. Optimization Flag: If an entire pass completes without a single swap, the array is already sorted. Setting a flag `swapped = 0` and breaking early improves best-case time from $O(N^2)$ to $O(N)$.\n3. Time Complexity: Best: $O(N)$ (optimized), Worst: $O(N^2)$, Average: $O(N^2)$. Space: $O(1)$ (stable sort).",
        "syntax": "if (arr[j] > arr[j+1]) { swap(&arr[j], &arr[j+1]); swapped = 1; }",
        "code": """#include <stdio.h>

void bubbleSort(int arr[], int n) {
    int passes = 0;
    int totalSwaps = 0;

    for (int i = 0; i < n - 1; i++) {
        int swapped = 0; /* Optimization flag */
        passes++;

        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                /* Swap adjacent elements */
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

                swapped = 1;
                totalSwaps++;
            }
        }

        /* If no swaps occurred, array is completely sorted */
        if (!swapped) {
            break;
        }
    }
    printf("Sorting completed in %d passes with %d total swaps.\\n", passes, totalSwaps);
}

int main(void) {
    int data[] = {64, 25, 12, 22, 11};
    int n = sizeof(data) / sizeof(data[0]);

    printf("Original Array: ");
    for (int i = 0; i < n; i++) printf("%d ", data[i]);
    printf("\\n");

    bubbleSort(data, n);

    printf("Sorted Array:   ");
    for (int i = 0; i < n; i++) printf("%d ", data[i]);
    printf("\\n");

    return 0;
}""",
        "output": """Original Array: 64 25 12 22 11 
Sorting completed in 4 passes with 8 total swaps.
Sorted Array:   11 12 22 25 64 """,
        "explanation": "1. Pass 1: 64 bubbles to index 4: `{25, 12, 22, 11, 64}`.\n2. Pass 2: 25 bubbles to index 3: `{12, 22, 11, 25, 64}`.\n3. Pass 3: 22 bubbles to index 2: `{12, 11, 22, 25, 64}`.\n4. Pass 4: 12 bubbles to index 1: `{11, 12, 22, 25, 64}`.\n5. Result is completely sorted in ascending order.",
        "mistakes": [
            ("Running inner loop to `N-1` instead of `N-1-i`.", "Running to `N-1` wastes CPU cycles comparing elements that are already sorted at the tail of the array."),
            ("Missing the temporary variable during swap: `a = b; b = a;`.", "Overwrites `a` with `b`, losing the original value of `a`. Always use a temporary storage variable or XOR swap.")
        ],
        "practice_q": "What is the time complexity of the optimized bubble sort on an array that is already sorted?"
    },
    {
        "num": 32,
        "title": "Two-Dimensional Arrays: Row-Major Memory Mapping and Addressing",
        "category": "2D Arrays",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Theory", "Viva Favorite"],
        "question": "Explain 2D array representation in C. Derive the row-major address calculation formula for an element at `A[i][j]` with respect to base address, row count, column count, and element size.",
        "logic": "C physically stores 2D arrays in contiguous 1D linear RAM using Row-Major Order (row 0 followed by row 1, etc.).",
        "concept": "Row-Major Address Formula:\nFor an array declared as `T arr[ROWS][COLS];`:\n$$\\text{Address}(arr[i][j]) = \\text{Base Address} + (i \\times \\text{COLS} + j) \\times \\text{sizeof}(T)$$\nWhere:\n- $i$ = target row index ($0 \\le i < \\text{ROWS}$)\n- $j$ = target column index ($0 \\le j < \\text{COLS}$)\n- $\\text{COLS}$ = total number of columns\n- $\\text{sizeof}(T)$ = bytes per element (e.g., 4 bytes for `int`).\nNote: The row dimension `ROWS` is NOT needed to locate an element; only the column count `COLS` is required. This is why when passing 2D arrays to functions, the column dimension must always be specified: `void f(int a[][COLS])`.",
        "syntax": "Address = Base + (i * COLS + j) * sizeof(element)",
        "code": """#include <stdio.h>
#include <stdint.h>

#define ROWS 3
#define COLS 4

int main(void) {
    int matrix[ROWS][COLS] = {
        {10, 11, 12, 13},
        {20, 21, 22, 23},
        {30, 31, 32, 33}
    };

    uintptr_t base = (uintptr_t)&matrix[0][0];

    printf("=== Row-Major Contiguous Address Verification ===\\n");
    printf("Base Address (&matrix[0][0]): %p\\n\\n", (void*)base);

    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            uintptr_t actualAddr = (uintptr_t)&matrix[i][j];
            uintptr_t computedAddr = base + (i * COLS + j) * sizeof(int);

            printf("matrix[%d][%d]=%d | Actual: %p | Computed: %p | %s\\n",
                   i, j, matrix[i][j], (void*)actualAddr, (void*)computedAddr,
                   (actualAddr == computedAddr) ? "MATCH" : "MISMATCH");
        }
    }

    return 0;
}""",
        "output": """=== Row-Major Contiguous Address Verification ===
Base Address (&matrix[0][0]): 0x7ffd5a68acb0

matrix[0][0]=10 | Actual: 0x7ffd5a68acb0 | Computed: 0x7ffd5a68acb0 | MATCH
matrix[0][1]=11 | Actual: 0x7ffd5a68acb4 | Computed: 0x7ffd5a68acb4 | MATCH
matrix[0][2]=12 | Actual: 0x7ffd5a68acb8 | Computed: 0x7ffd5a68acb8 | MATCH
matrix[0][3]=13 | Actual: 0x7ffd5a68acbc | Computed: 0x7ffd5a68acbc | MATCH
matrix[1][0]=20 | Actual: 0x7ffd5a68acc0 | Computed: 0x7ffd5a68acc0 | MATCH
matrix[1][1]=21 | Actual: 0x7ffd5a68acc4 | Computed: 0x7ffd5a68acc4 | MATCH
matrix[1][2]=22 | Actual: 0x7ffd5a68acc8 | Computed: 0x7ffd5a68acc8 | MATCH
matrix[1][3]=23 | Actual: 0x7ffd5a68accc | Computed: 0x7ffd5a68accc | MATCH
matrix[2][0]=30 | Actual: 0x7ffd5a68acd0 | Computed: 0x7ffd5a68acd0 | MATCH
matrix[2][1]=31 | Actual: 0x7ffd5a68acd4 | Computed: 0x7ffd5a68acd4 | MATCH
matrix[2][2]=32 | Actual: 0x7ffd5a68acd8 | Computed: 0x7ffd5a68acd8 | MATCH
matrix[2][3]=33 | Actual: 0x7ffd5a68acdc | Computed: 0x7ffd5a68acdc | MATCH""",
        "explanation": "1. Every single element computed via `Base + (i * 4 + j) * 4` matches the physical RAM address.\n2. When moving from `matrix[0][3]` to `matrix[1][0]`, the address increases by 4 bytes contiguously.\n3. Row-major order is the standard storage convention across C and C++.",
        "mistakes": [
            ("Writing `void func(int a[][])` in function prototypes.", "The C compiler must know the column width to compute element offsets. You must write `void func(int a[][COLS])`."),
            ("Confusing Row-Major (C) with Column-Major (Fortran/MATLAB).", "In C, rows are contiguous. In Fortran/MATLAB, columns are contiguous.")
        ],
        "practice_q": "If base address of `double M[4][5]` is 2000, what is the address of `M[2][3]` assuming 8-byte doubles?"
    },
    {
        "num": 33,
        "title": "Matrix Addition and Subtraction with Dimension Compatibility Checks",
        "category": "2D Arrays",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "State the mathematical condition for matrix addition and subtraction. Write a complete C program to validate dimensions and perform matrix addition and subtraction.",
        "logic": "Matrices can only be added or subtracted if they share identical dimensions: $R_1 == R_2$ and $C_1 == C_2$. Elements are added element-by-element: $C[i][j] = A[i][j] + B[i][j]$.",
        "concept": "1. Compatibility Rule: Let matrix $A$ be of order $R_1 \\times C_1$ and matrix $B$ be of order $R_2 \\times C_2$. Addition is valid if and only if $R_1 = R_2$ and $C_1 = C_2$.\n2. Time Complexity: $O(R \\times C)$ iterating through nested loops.\n3. Result matrix order is also $R_1 \\times C_1$.",
        "syntax": "C[i][j] = A[i][j] + B[i][j];\nD[i][j] = A[i][j] - B[i][j];",
        "code": """#include <stdio.h>

#define MAX 10

void printMatrix(int r, int c, int m[MAX][MAX], const char *name) {
    printf("Matrix %s (%dx%d):\\n", name, r, c);
    for (int i = 0; i < r; i++) {
        printf("  [ ");
        for (int j = 0; j < c; j++) {
            printf("%4d ", m[i][j]);
        }
        printf("]\\n");
    }
}

int main(void) {
    int r1 = 2, c1 = 3;
    int r2 = 2, c2 = 3;

    int A[MAX][MAX] = {{1, 2, 3}, {4, 5, 6}};
    int B[MAX][MAX] = {{7, 8, 9}, {3, 2, 1}};
    int Sum[MAX][MAX], Diff[MAX][MAX];

    /* Validation Check */
    if (r1 != r2 || c1 != c2) {
        printf("Error: Matrix dimensions incompatible for addition/subtraction!\\n");
        return 1;
    }

    /* Computation */
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c1; j++) {
            Sum[i][j] = A[i][j] + B[i][j];
            Diff[i][j] = A[i][j] - B[i][j];
        }
    }

    printMatrix(r1, c1, A, "A");
    printMatrix(r2, c2, B, "B");
    printMatrix(r1, c1, Sum, "A + B");
    printMatrix(r1, c1, Diff, "A - B");

    return 0;
}""",
        "output": """Matrix A (2x3):
  [    1    2    3 ]
  [    4    5    6 ]
Matrix B (2x3):
  [    7    8    9 ]
  [    3    2    1 ]
Matrix A + B (2x3):
  [    8   10   12 ]
  [    7    7    7 ]
Matrix A - B (2x3):
  [   -6   -6   -6 ]
  [    1    3    5 ]""",
        "explanation": "1. Both matrices have order $2 \\times 3$. The dimension check passes.\n2. Corresponding elements are added and subtracted across 2 nested loops.\n3. Formatted display preserves tabular column alignment.",
        "mistakes": [
            ("Proceeding with matrix addition without validating row/col equality.", "Attempting to add matrices with different dimensions is mathematically undefined and causes array out-of-bound errors in C."),
            ("Swapping row and column indices: writing `m[j][i]` instead of `m[i][j]`.", "Produces the transpose of the intended matrix.")
        ],
        "practice_q": "What is the memory footprint of storing three $10 \\times 10$ integer matrices in C?"
    },
    {
        "num": 34,
        "title": "Matrix Multiplication: Algorithm, Compatibility, and 3-Loop Implementation",
        "category": "2D Arrays",
        "difficulty": "Intermediate",
        "exam_tags": ["High Yield Exam", "VTU Lab Mandatory"],
        "question": "Formulate the mathematical condition for matrix multiplication. Write a complete C program to perform matrix multiplication of two matrices with dimension checks using three nested loops.",
        "logic": "Multiplication $A \\times B$ is defined if and only if the number of columns in $A$ equals the number of rows in $B$ ($C_1 == R_2$). The resulting matrix has dimensions $R_1 \\times C_2$, where $C[i][j] = \\sum_{k=0}^{C_1-1} A[i][k] \\cdot B[k][j]$.",
        "concept": "1. Compatibility: $A_{R_1 \\times C_1} \\times B_{R_2 \\times C_2} \\implies C_1 = R_2$.\n2. Product Size: $R_1 \\times C_2$.\n3. Three Nested Loops:\n- Loop 1 (index $i$ from 0 to $R_1-1$): Selects row of $A$.\n- Loop 2 (index $j$ from 0 to $C_2-1$): Selects column of $B$.\n- Loop 3 (index $k$ from 0 to $C_1-1$): Computes the dot product $\\sum A[i][k] B[k][j]$.\n4. Time Complexity: $O(R_1 \\times C_1 \\times C_2) = O(N^3)$ for square matrices.",
        "syntax": "for(i=0; i<r1; i++) for(j=0; j<c2; j++) { c[i][j]=0; for(k=0; k<c1; k++) c[i][j] += a[i][k]*b[k][j]; }",
        "code": """#include <stdio.h>

#define MAX 10

int main(void) {
    int r1 = 2, c1 = 3;
    int A[MAX][MAX] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    int r2 = 3, c2 = 2;
    int B[MAX][MAX] = {
        {7, 8},
        {9, 1},
        {2, 3}
    };

    int Product[MAX][MAX];

    /* Validation Rule */
    if (c1 != r2) {
        printf("Error: Matrix multiplication impossible. Columns of A (%d) != Rows of B (%d)\\n", c1, r2);
        return 1;
    }

    /* Matrix Multiplication Algorithm */
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            Product[i][j] = 0; /* Clear accumulator before dot product */
            for (int k = 0; k < c1; k++) {
                Product[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    printf("=== Matrix A (%dx%d) * Matrix B (%dx%d) ===\\n", r1, c1, r2, c2);
    printf("Result Matrix C (%dx%d):\\n", r1, c2);
    for (int i = 0; i < r1; i++) {
        printf("  [ ");
        for (int j = 0; j < c2; j++) {
            printf("%4d ", Product[i][j]);
        }
        printf("]\\n");
    }

    return 0;
}""",
        "output": """=== Matrix A (2x3) * Matrix B (3x2) ===
Result Matrix C (2x2):
  [   31   19 ]
  [   85   55 ]""",
        "explanation": "1. Dot product calculation for $C[0][0]$: $(1 \\times 7) + (2 \\times 9) + (3 \\times 2) = 7 + 18 + 6 = 31$.\n2. Dot product for $C[0][1]$: $(1 \\times 8) + (2 \\times 1) + (3 \\times 3) = 8 + 2 + 9 = 19$.\n3. Dot product for $C[1][0]$: $(4 \\times 7) + (5 \\times 9) + (6 \\times 2) = 28 + 45 + 12 = 85$.\n4. Dot product for $C[1][1]$: $(4 \\times 8) + (5 \\times 1) + (6 \\times 3) = 32 + 5 + 18 = 55$.",
        "mistakes": [
            ("Forgetting to initialize `Product[i][j] = 0`.", "If not zeroed before the inner accumulation loop, uninitialized stack garbage will be added to the product."),
            ("Using wrong loop bounds in the 3 loops (e.g. running loop 3 up to `c2` instead of `c1`).", "The accumulation index `k` must iterate across the shared dimension: `k < c1` (or `k < r2`).")
        ],
        "practice_q": "What is the result of multiplying any matrix by an identity matrix of compatible order?"
    },
    {
        "num": 35,
        "title": "Matrix Transpose, Trace, and Symmetric Matrix Verification",
        "category": "2D Arrays",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Define the transpose, trace, and symmetric properties of a matrix. Write a complete C program to compute the transpose, calculate the trace, and verify if a square matrix is Symmetric ($A = A^T$).",
        "logic": "Transpose: Rows become columns ($T[j][i] = A[i][j]$). Trace: Sum of main diagonal elements $\\sum A[i][i]$. Symmetric Matrix: A square matrix where $A[i][j] == A[j][i]$ for all $i, j$.",
        "concept": "1. Trace: Only defined for square matrices ($N \\times N$). It is the sum of elements where row index equals column index ($i == j$).\n2. Symmetric Property: Matrix must be square. If any pair $A[i][j] \\ne A[j][i]$, it is not symmetric.\n3. Optimization: To check symmetry, you only need to inspect elements above the main diagonal ($j > i$).",
        "syntax": "transpose[j][i] = matrix[i][j];\ntrace += matrix[i][i];",
        "code": """#include <stdio.h>

#define N 3

int main(void) {
    int A[N][N] = {
        {1, 7, 3},
        {7, 4, -5},
        {3, -5, 6}
    };
    int T[N][N];
    int trace = 0;
    int isSymmetric = 1;

    /* Compute Transpose, Trace, and Check Symmetry */
    for (int i = 0; i < N; i++) {
        trace += A[i][i]; /* Trace: main diagonal */
        for (int j = 0; j < N; j++) {
            T[j][i] = A[i][j];
            if (A[i][j] != A[j][i]) {
                isSymmetric = 0;
            }
        }
    }

    printf("=== Square Matrix A (3x3) ===\\n");
    for (int i = 0; i < N; i++) {
        printf("  [ ");
        for (int j = 0; j < N; j++) printf("%3d ", A[i][j]);
        printf("]\\n");
    }

    printf("\\nMatrix Trace (Sum of Main Diagonal): %d\\n", trace);
    printf("Symmetry Check: The matrix is %s!\\n", 
           isSymmetric ? "SYMMETRIC (A == A^T)" : "NOT SYMMETRIC");

    return 0;
}""",
        "output": """=== Square Matrix A (3x3) ===
  [   1   7   3 ]
  [   7   4  -5 ]
  [   3  -5   6 ]

Matrix Trace (Sum of Main Diagonal): 11
Symmetry Check: The matrix is SYMMETRIC (A == A^T)!""",
        "explanation": "1. Trace is $1 + 4 + 6 = 11$.\n2. Elements across the diagonal match: $A[0][1] = A[1][0] = 7$, $A[0][2] = A[2][0] = 3$, $A[1][2] = A[2][1] = -5$.\n3. The matrix is confirmed to be symmetric.",
        "mistakes": [
            ("Checking symmetry on rectangular matrices ($M \\times N$ where $M \\ne N$).", "Symmetry is strictly defined only for square matrices."),
            ("Swapping in-place without temporary storage: `A[i][j] = A[j][i]; A[j][i] = A[i][j];`.", "Overwrites `A[i][j]` before saving its original value. In-place transpose requires a temp variable and loop with `j > i`.")
        ],
        "practice_q": "What is the condition for a matrix to be Skew-Symmetric ($A^T = -A$)?"
    },
    {
        "num": 36,
        "title": "Character Arrays vs Strings: The Null Terminator '\\0'",
        "category": "Strings",
        "difficulty": "Fundamental",
        "exam_tags": ["Core Concept", "Viva Must-Know"],
        "question": "What is a string in C? How does a character array differ from a string? Explain the role of the null terminator `\\0` and show what happens when `\\0` is missing.",
        "logic": "In C, a string is a sequence of characters stored in a contiguous 1D `char` array, terminated by a special null character `\\0` (ASCII code 0).",
        "concept": "1. String Representation: C does not have a native primitive `string` data type. Strings are 1D arrays of `char` ending with `\\0`.\n2. Sizing: An array holding a word of $N$ visible characters must be sized at least $N + 1$ to accommodate `\\0`.\n3. String Literal: `\"Hello\"` automatically allocates 6 bytes: `'H'`, `'e'`, `'l'`, `'l'`, `'o'`, `'\\0'`.\n4. Missing `\\0` Danger: Standard functions (`printf(\"%s\")`, `strlen()`, `strcpy()`) rely on `\\0` to know when the string ends. Without it, functions read past the array into adjacent memory until a random zero byte is found, printing garbage or crashing.",
        "syntax": "char str[] = \"Hello\"; /* 6 bytes including \\0 */",
        "code": """#include <stdio.h>

int main(void) {
    /* 1. Proper null-terminated string */
    char validStr[6] = {'H', 'e', 'l', 'l', 'o', '\\0'};

    /* 2. String literal shorthand (compiler appends \\0 automatically) */
    char literalStr[] = "World";

    printf("Valid String:   %s (Length in bytes: %zu)\\n", validStr, sizeof(validStr));
    printf("Literal String: %s (Length in bytes: %zu)\\n", literalStr, sizeof(literalStr));

    /* Demonstration of ASCII value of null character */
    printf("ASCII of '\\\\0': %d (distinguish from character '0' which is ASCII %d)\\n", 
           '\\0', '0');

    return 0;
}""",
        "output": """Valid String:   Hello (Length in bytes: 6)
Literal String: World (Length in bytes: 6)
ASCII of '\\0': 0 (distinguish from character '0' which is ASCII 48)""",
        "explanation": "1. `validStr` contains 5 letters plus `\\0`, totaling 6 bytes.\n2. `literalStr[] = \"World\"` automatically reserves 6 bytes in memory.\n3. `'\\0'` has numerical value 0, whereas character `'0'` has ASCII value 48.",
        "mistakes": [
            ("Declaring `char str[5] = \"Hello\";`.", "The literal requires 6 bytes (5 chars + `\\0`). Storing it in 5 bytes drops `\\0`, causing buffer overreads during printing."),
            ("Confusing single quotes `'A'` with double quotes `\"A\"`.", "`'A'` is a single character (char literal, 1 byte). `\"A\"` is a string literal containing `'A'` and `'\\0'` (2 bytes).")
        ],
        "practice_q": "What is the difference between `char *p = \"Hello\";` and `char p[] = \"Hello\";` regarding mutability?"
    },
    {
        "num": 37,
        "title": "String Input: scanf() Whitespace Limitations and Scansets",
        "category": "Strings",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Question", "Viva Favorite"],
        "question": "Why does `scanf(\"%s\", str)` fail to read a full sentence containing spaces? How does the scanset specifier `scanf(\"%[^\\n]\", str)` resolve this problem?",
        "logic": "`scanf(\"%s\")` treats whitespace (space, tab, newline) as an input delimiter. Reading stops at the very first space. The scanset `\"%[^\\n]\"` reads all characters until a newline is encountered.",
        "concept": "1. `scanf(\"%s\", str)` stops reading at the first space. Entering \"John Doe\" stores only \"John\".\n2. Note that `str` is already a pointer (decayed array base address), so no `&` is used in `scanf(\"%s\", str)`.\n3. Scanset Notation: `%[^\n]` means: accept all characters EXCEPT (`^`) the newline character (`\\n`).\n4. Width Specifier: Always specify maximum buffer width (e.g., `%99[^\n]`) to prevent buffer overflow.",
        "syntax": "scanf(\" %99[^\\n]\", buffer);",
        "code": """#include <stdio.h>

int main(void) {
    char fullName[100];

    /* Simulated input parsing */
    char inputBuffer[] = "Sir Mokshagundam Visvesvaraya\\n";

    /* Using scanset with width limit to read full line with spaces */
    sscanf(inputBuffer, "%99[^\\n]", fullName);

    printf("Extracted Full Name: %s\\n", fullName);
    printf("Length of String:    %zu characters\\n", sizeof(fullName));

    return 0;
}""",
        "output": """Extracted Full Name: Sir Mokshagundam Visvesvaraya
Length of String:    100 characters""",
        "explanation": "1. `sscanf` reads the entire string with spaces until the newline `\\n`.\n2. The full text \"Sir Mokshagundam Visvesvaraya\" is safely stored in `fullName`.\n3. The width limit `%99[^\\n]` guarantees at most 99 characters are read, leaving room for `\\0`.",
        "mistakes": [
            ("Writing `scanf(\"%s\", &str);`.", "`str` already decays to the address of the first element. Passing `&str` passes pointer to array, which has a different type."),
            ("Using `scanf(\"%[^\\n]\", str)` without a leading space after a previous `scanf()`.", "The leftover newline from the previous input will immediately terminate the scanset, reading an empty string.")
        ],
        "practice_q": "What does the scanset `%[0-9]` do in `scanf()`?"
    },
    {
        "num": 38,
        "title": "Safe String Input: Why gets() is Dangerous and How to Use fgets()",
        "category": "Strings & Security",
        "difficulty": "Fundamental",
        "exam_tags": ["Security Critical", "Viva Must-Know", "VTU Exam Favorite"],
        "question": "Why was `gets()` officially removed from the ISO C11 standard? Explain the buffer overflow vulnerability. Provide the standard, safe idiom for using `fgets()` with newline removal.",
        "logic": "`gets()` has no parameter to specify buffer capacity. It continues writing into memory until it finds a newline, overwriting return addresses and stack variables (buffer overflow vulnerability).",
        "concept": "1. The `gets()` Vulnerability: If a program allocates `char buf[10]` and the user enters 50 characters, `gets(buf)` writes all 50 bytes into the stack, overwriting adjacent memory. This is the root cause of classic security exploits like the Morris Worm.\n2. `fgets(buffer, sizeof(buffer), stdin)`: Requires buffer size as an explicit argument. It will never write more than `size - 1` bytes, always ensuring null termination.\n3. Newline Handling: `fgets()` retains the trailing newline character `'\\n'` inside the buffer. Idiomatic removal: replace `'\\n'` with `'\\0'`.",
        "syntax": "fgets(str, sizeof(str), stdin);\nstr[strcspn(str, \"\\n\")] = '\\0';",
        "code": """#include <stdio.h>
#include <string.h>

void safeStringInputDemo(char *buffer, size_t size, const char *simulatedInput) {
    /* Safe read simulated via fgets logic */
    strncpy(buffer, simulatedInput, size - 1);
    buffer[size - 1] = '\\0'; /* Force null termination */

    /* Standard C idiom: Strip trailing newline */
    buffer[strcspn(buffer, "\\r\\n")] = '\\0';
}

int main(void) {
    char userBio[30];

    printf("=== Safe String Input Demonstration ===\\n");
    safeStringInputDemo(userBio, sizeof(userBio), "Computer Science Engineer\\n");

    printf("Stored Bio:   \\\"%s\\\"\\n", userBio);
    printf("String Length: %zu chars (Fits inside 30-byte buffer)\\n", strlen(userBio));

    return 0;
}""",
        "output": """=== Safe String Input Demonstration ===
Stored Bio:   "Computer Science Engineer"
String Length: 25 chars (Fits inside 30-byte buffer)""",
        "explanation": "1. `fgets` restricts reading to `sizeof(buffer) - 1` characters, eliminating buffer overflow.\n2. `strcspn(buffer, \"\\r\\n\")` finds the index of the newline character.\n3. Setting `buffer[index] = '\\0'` removes the newline cleanly.",
        "mistakes": [
            ("Continuing to use `gets()` in modern C.", "`gets()` is removed from C11. Using it causes compilation errors on modern compilers or serious security vulnerabilities."),
            ("Using `sizeof(ptr)` instead of `sizeof(array)` in `fgets()`.", "If the buffer was passed to a function as a pointer, `sizeof(ptr)` gives 4 or 8 bytes (pointer size), NOT the buffer capacity.")
        ],
        "practice_q": "What does `strcspn()` return if the target character is not found in the string?"
    },
    {
        "num": 39,
        "title": "String Length: Built-in strlen() and Custom Implementation",
        "category": "String Operations",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "Viva Question"],
        "question": "What does `<string.h>`'s `strlen()` function return? Implement your own version of `my_strlen()` without using any library functions, using both array indexing and pointer traversal.",
        "logic": "`strlen()` counts the number of characters in a string up to, but NOT including, the terminating null character `\\0`.",
        "concept": "1. Return Type: `strlen()` returns `size_t` (an unsigned integer type).\n2. Contrast with `sizeof`: For `char str[50] = \"Code\";`, `sizeof(str)` is 50 bytes (total allocated buffer), while `strlen(str)` is 4 (visible characters).\n3. Array Approach: Increment an index counter until `str[i] == '\\0'`.\n4. Pointer Approach: Traverse with a pointer until `*p == '\\0'`. The length is `p - str` (pointer subtraction).",
        "syntax": "size_t my_strlen(const char *str);",
        "code": """#include <stdio.h>

/* 1. Implementation using array indexing */
size_t my_strlen_array(const char str[]) {
    size_t length = 0;
    while (str[length] != '\\0') {
        length++;
    }
    return length;
}

/* 2. Implementation using pointer arithmetic */
size_t my_strlen_pointer(const char *str) {
    const char *ptr = str;
    while (*ptr != '\\0') {
        ptr++;
    }
    return (size_t)(ptr - str);
}

int main(void) {
    char testText[] = "Applied Mathematics & C";

    size_t len1 = my_strlen_array(testText);
    size_t len2 = my_strlen_pointer(testText);

    printf("Input Text:            \\\"%s\\\"\\n", testText);
    printf("Length (Array Index):  %zu\\n", len1);
    printf("Length (Pointer Diff): %zu\\n", len2);
    printf("Buffer Size in Memory: %zu bytes\\n", sizeof(testText));

    return 0;
}""",
        "output": """Input Text:            "Applied Mathematics & C"
Length (Array Index):  23
Length (Pointer Diff): 23
Buffer Size in Memory: 24 bytes""",
        "explanation": "1. Both implementations count 23 characters.\n2. The memory buffer occupies 24 bytes because of the terminating `\\0`.\n3. Pointer subtraction `ptr - str` computes the number of elements between two pointers in $O(1)$.",
        "mistakes": [
            ("Writing `for(int i=0; i <= strlen(s); i++)` inside another loop.", "Calling `strlen(s)` inside a loop condition recalculates length on every iteration, turning an $O(N)$ loop into $O(N^2)$."),
            ("Assuming `strlen()` includes the null terminator `\\0`.", "`strlen(\"abc\")` returns 3, not 4.")
        ],
        "practice_q": "What will `strlen(\"Hello\\0World\");` return and why?"
    },
    {
        "num": 40,
        "title": "String Copy: strcpy(), strncpy(), and Custom Safe Implementation",
        "category": "String Operations",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "Viva Favorite"],
        "question": "Explain `strcpy()` and `strncpy()`. Why is `strncpy()` preferred? Implement a custom `my_strcpy()` function without using `<string.h>`.",
        "logic": "Copy characters from source string to destination string one-by-one until `\\0` is encountered and copied. `strncpy()` takes a length limit to avoid buffer overflow.",
        "concept": "1. `char *strcpy(char *dest, const char *src)`: Copies `src` to `dest` including `\\0`. It does NOT check whether `dest` has sufficient capacity!\n2. `char *strncpy(char *dest, const char *src, size_t n)`: Copies at most `n` characters. If `src` length $\\ge n$, `strncpy()` does NOT null-terminate `dest`! Safe practice: explicitly set `dest[n-1] = '\\0'`.\n3. Custom implementation: `while((*dest++ = *src++) != '\\0');`.",
        "syntax": "char *my_strcpy(char *dest, const char *src);",
        "code": """#include <stdio.h>

/* Custom strcpy implementation */
char *my_strcpy(char *dest, const char *src) {
    char *savedDest = dest;
    while (*src != '\\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\\0'; /* Copy terminating null character */
    return savedDest;
}

int main(void) {
    char source[] = "VTU Belagavi Engineering";
    char destination[50];

    my_strcpy(destination, source);

    printf("Source String:      \\\"%s\\\"\\n", source);
    printf("Copied Destination: \\\"%s\\\"\\n", destination);

    return 0;
}""",
        "output": """Source String:      "VTU Belagavi Engineering"
Copied Destination: "VTU Belagavi Engineering" """,
        "explanation": "1. `*src` is read and copied into `*dest` character-by-character.\n2. Once `\\0` is reached, loop terminates and `\\0` is explicitly written to `*dest`.\n3. Returning `savedDest` allows function chaining like `printf(\"%s\", my_strcpy(d, s))`.",
        "mistakes": [
            ("Forgetting to copy the terminating `\\0`.", "Results in `destination` not being properly terminated, causing garbage output on subsequent reads."),
            ("Attempting string assignment directly: `destination = source;`.", "In C, array names are constant pointers. Direct assignment causes a compilation error.")
        ],
        "practice_q": "What happens if the destination buffer is smaller than the source string in `strcpy()`?"
    },
    {
        "num": 41,
        "title": "String Concatenation: strcat() and Custom Re-implementation",
        "category": "String Operations",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "Exam Question"],
        "question": "What is string concatenation? Explain `strcat()`. Implement a custom `my_strcat()` function without `<string.h>` that appends source string to destination.",
        "logic": "Concatenation appends a copy of the source string to the end of the destination string. The terminating `\\0` of the destination is overwritten by the first character of the source, and a new `\\0` is appended at the end.",
        "concept": "1. Destination Capacity: Destination array MUST be large enough to hold `strlen(dest) + strlen(src) + 1` bytes.\n2. Algorithm:\n- Step 1: Find the end of `dest` (locate its `\\0`).\n- Step 2: Copy characters from `src` to `dest` starting at that position.\n- Step 3: Append `\\0` to mark the end of the combined string.",
        "syntax": "char *my_strcat(char *dest, const char *src);",
        "code": """#include <stdio.h>

char *my_strcat(char *dest, const char *src) {
    char *ptr = dest;

    /* Step 1: Advance to end of dest */
    while (*ptr != '\\0') {
        ptr++;
    }

    /* Step 2: Copy src characters */
    while (*src != '\\0') {
        *ptr = *src;
        ptr++;
        src++;
    }

    /* Step 3: Append null terminator */
    *ptr = '\\0';

    return dest;
}

int main(void) {
    char greeting[50] = "Hello, ";
    char name[] = "Antigravity Engineer!";

    printf("Before Concatenation: \\\"%s\\\"\\n", greeting);

    my_strcat(greeting, name);

    printf("After Concatenation:  \\\"%s\\\"\\n", greeting);

    return 0;
}""",
        "output": """Before Concatenation: "Hello, "
After Concatenation:  "Hello, Antigravity Engineer!" """,
        "explanation": "1. Pointer `ptr` advances past `'H'`, `'e'`, `'l'`, `'l'`, `'o'`, `','`, `' '` to find `\\0`.\n2. Characters from `name` are written starting at that position.\n3. The final `\\0` is appended, creating a valid 29-character string.",
        "mistakes": [
            ("Concatenating into an insufficiently sized buffer.", "If `greeting` was only `char greeting[10]`, appending causes a stack buffer overflow."),
            ("Starting copy at `ptr + 1`.", "Leaving the existing `\\0` in place causes `printf` to stop reading before the appended characters.")
        ],
        "practice_q": "What does `strncat(dest, src, n)` do when `n` is smaller than `strlen(src)`?"
    },
    {
        "num": 42,
        "title": "String Comparison: strcmp() Lexicographical Logic and Custom Function",
        "category": "String Operations",
        "difficulty": "Fundamental",
        "exam_tags": ["Viva Must-Know", "Lab Program"],
        "question": "How does `strcmp()` perform lexicographical comparison? Explain its return values (<0, 0, >0). Implement `my_strcmp()` without using library functions.",
        "logic": "Compares characters of two strings one-by-one based on their ASCII values. The comparison stops at the first character difference or when a `\\0` is reached.",
        "concept": "Return Values of `strcmp(str1, str2)`:\n- `0`: Strings are identical (`str1 == str2`).\n- `< 0` (negative): `str1` is lexicographically smaller than `str2` (first differing character in `str1` has smaller ASCII value).\n- `> 0` (positive): `str1` is lexicographically greater than `str2`.\nASCII Reminder: `'A'` (65) < `'a'` (97). Therefore, uppercase letters are lexicographically smaller than lowercase letters: `\"Apple\" < \"apple\"`.",
        "syntax": "int my_strcmp(const char *s1, const char *s2);",
        "code": """#include <stdio.h>

int my_strcmp(const char *s1, const char *s2) {
    while (*s1 != '\\0' && *s2 != '\\0') {
        if (*s1 != *s2) {
            return (unsigned char)*s1 - (unsigned char)*s2;
        }
        s1++;
        s2++;
    }
    return (unsigned char)*s1 - (unsigned char)*s2;
}

int main(void) {
    char w1[] = "Apple";
    char w2[] = "Application";
    char w3[] = "Apple";

    printf("Comparing \\\"%s\\\" vs \\\"%s\\\": %d\\n", w1, w2, my_strcmp(w1, w2));
    printf("Comparing \\\"%s\\\" vs \\\"%s\\\": %d\\n", w2, w1, my_strcmp(w2, w1));
    printf("Comparing \\\"%s\\\" vs \\\"%s\\\": %d\\n", w1, w3, my_strcmp(w1, w3));

    return 0;
}""",
        "output": """Comparing "Apple" vs "Application": -4
Comparing "Application" vs "Apple": 4
Comparing "Apple" vs "Apple": 0""",
        "explanation": "1. Comparing \"Apple\" and \"Application\": Characters `'A'`, `'p'`, `'p'`, `'l'` match.\n2. At index 4, `'e'` (ASCII 101) is compared with `'i'` (ASCII 105).\n3. Difference is $101 - 105 = -4$. Since it is negative, \"Apple\" comes before \"Application\".\n4. Identical strings return `0`.",
        "mistakes": [
            ("Comparing strings using `==` (e.g. `if (s1 == s2)`).", "`s1 == s2` compares memory addresses of the pointers, NOT the string contents! Always use `strcmp()`."),
            ("Assuming `strcmp()` returns only -1, 0, or 1.", "The standard only requires negative, zero, or positive. Never check `if (strcmp(a, b) == -1)`! Always check `if (strcmp(a, b) < 0)`.")
        ],
        "practice_q": "How does `strncmp(s1, s2, n)` differ from `strcmp()`?"
    },
    {
        "num": 43,
        "title": "In-Place String Reversal Algorithm (Two-Pointer Technique)",
        "category": "String Manipulation",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Write a complete C program to reverse a string in-place without using `strrev()` or an auxiliary temporary array. Explain the two-pointer swapping algorithm.",
        "logic": "Maintain two pointer indices: `left = 0` and `right = length - 1`. Swap `str[left]` with `str[right]`, then increment `left` and decrement `right` until `left >= right`.",
        "concept": "1. In-place requirement: Modifies the original memory buffer directly, requiring $O(1)$ auxiliary space.\n2. Algorithm:\n- Find string length $L = \\text{strlen}(str)$.\n- Set $i = 0, j = L - 1$.\n- While $i < j$:\n  - `temp = str[i]; str[i] = str[j]; str[j] = temp;`\n  - $i++, j--$.\n3. Mutability Note: The target string MUST reside in a mutable character array (`char str[]`), NOT in a string literal pointer (`char *s`), as string literals are stored in read-only memory.",
        "syntax": "while (left < right) { swap(str[left++], str[right--]); }",
        "code": """#include <stdio.h>
#include <string.h>

void reverseStringInPlace(char *str) {
    if (str == NULL) return;

    int left = 0;
    int right = (int)strlen(str) - 1;

    while (left < right) {
        /* Swap characters at left and right */
        char temp = str[left];
        str[left] = str[right];
        str[right] = temp;

        left++;
        right--;
    }
}

int main(void) {
    char message[] = "Algorithms & Data Structures";

    printf("Original:  \\\"%s\\\"\\n", message);
    reverseStringInPlace(message);
    printf("Reversed:  \\\"%s\\\"\\n", message);

    return 0;
}""",
        "output": """Original:  "Algorithms & Data Structures"
Reversed:  "serutcurtS ataD & smhtiroglA" """,
        "explanation": "1. `left` starts at index 0 ('A'), `right` starts at index 27 ('s').\n2. Characters are swapped inward until pointers meet in the middle.\n3. The string is reversed in-place without allocating auxiliary memory.",
        "mistakes": [
            ("Passing a string literal to an in-place reverse function: `reverseStringInPlace(\"Hello\");`.", "String literals reside in read-only memory (`.rodata`). Attempting to modify them causes a Segmentation Fault (SIGSEGV)."),
            ("Swapping up to `strlen(str)` instead of `strlen(str) / 2`.", "If the loop runs the entire length, it swaps elements twice, returning the string to its original order!")
        ],
        "practice_q": "How would you reverse the words in a sentence rather than the individual characters?"
    },
    {
        "num": 44,
        "title": "Palindrome String Check: Case-Insensitive and Ignoring Punctuation",
        "category": "String Manipulation",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "Exam Question"],
        "question": "Write a complete C program to check whether a given string is a Palindrome. Implement a case-insensitive check using `<ctype.h>` functions (`tolower()`).",
        "logic": "A string is a palindrome if it reads the same forward and backward (e.g. \"Madam\", \"Racecar\"). Compare characters from both ends moving inward, converting each to lowercase for case insensitivity.",
        "concept": "1. Symmetry: Compare `tolower(str[left])` with `tolower(str[right])`.\n2. If any pair differs, the string is not a palindrome.\n3. Time Complexity: $O(N)$ making at most $N/2$ comparisons.\n4. Space Complexity: $O(1)$ in-place verification.",
        "syntax": "if (tolower(str[left]) != tolower(str[right])) return 0;",
        "code": """#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isPalindrome(const char *str) {
    int left = 0;
    int right = (int)strlen(str) - 1;

    while (left < right) {
        if (tolower((unsigned char)str[left]) != tolower((unsigned char)str[right])) {
            return 0; /* Character mismatch -> Not palindrome */
        }
        left++;
        right--;
    }
    return 1; /* Palindrome verified */
}

int main(void) {
    const char *testCases[] = {"RaceCar", "Madam", "VTUCollege", "Level"};
    int count = sizeof(testCases) / sizeof(testCases[0]);

    printf("=== Palindrome Verification Engine ===\\n");
    for (int i = 0; i < count; i++) {
        const char *word = testCases[i];
        printf("%-12s -> %s\\n", word, 
               isPalindrome(word) ? "PALINDROME (Case-Insensitive)" : "NOT a palindrome");
    }

    return 0;
}""",
        "output": """=== Palindrome Verification Engine ===
RaceCar      -> PALINDROME (Case-Insensitive)
Madam        -> PALINDROME (Case-Insensitive)
VTUCollege   -> NOT a palindrome
Level        -> PALINDROME (Case-Insensitive)""",
        "explanation": "1. \"RaceCar\": `'R'` and `'r'` match under `tolower()`. `'a'` and `'a'`, `'c'` and `'c'` all match -> Palindrome.\n2. \"Madam\": Matches under `tolower()` -> Palindrome.\n3. \"VTUCollege\": Fails at the first check (`'v'` != `'e'`) -> Not a palindrome.",
        "mistakes": [
            ("Forgetting `(unsigned char)` cast in `tolower()`.", "`tolower()` expects an `int` representable as `unsigned char` or `EOF`. Passing signed char can cause undefined behavior with non-ASCII characters."),
            ("Creating a reversed copy of the string to check palindrome.", "Allocating a separate array and calling `strcmp()` wastes $O(N)$ extra memory. The two-pointer in-place check requires $O(1)$ memory.")
        ],
        "practice_q": "How would you modify this program to ignore spaces and punctuation (e.g. \"A man, a plan, a canal: Panama\")?"
    },
    {
        "num": 45,
        "title": "Character Frequency and Categorization (Vowels, Consonants, Digits, Spaces)",
        "category": "String Operations",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "Exam Level"],
        "question": "Write a complete C program to count the total number of vowels, consonants, digits, whitespace characters, and special symbols in a given line of text.",
        "logic": "Traverse the string character by character. Use `<ctype.h>` helper functions (`isalpha`, `isdigit`, `isspace`) and check against vowel set (`a, e, i, o, u`).",
        "concept": "1. Classification Rules:\n- Vowels: `ch` is alphabetic AND matches `'a','e','i','o','u'` (case-insensitive).\n- Consonants: `ch` is alphabetic AND not a vowel.\n- Digits: `'0' <= ch && ch <= '9'` or `isdigit(ch)`.\n- Spaces: `' '`, `'\\t'`, `'\\n'` or `isspace(ch)`.\n- Special characters: All remaining printable characters.",
        "syntax": "isalpha(c), isdigit(c), isspace(c)",
        "code": """#include <stdio.h>
#include <ctype.h>

int main(void) {
    char text[] = "VTU Exam 2026: Linear Algebra & C Programming - 100% Score!";

    int vowels = 0, consonants = 0, digits = 0, spaces = 0, specials = 0;

    for (int i = 0; text[i] != '\\0'; i++) {
        char ch = text[i];
        char lowerCh = (char)tolower((unsigned char)ch);

        if (isalpha((unsigned char)ch)) {
            if (lowerCh == 'a' || lowerCh == 'e' || lowerCh == 'i' || 
                lowerCh == 'o' || lowerCh == 'u') {
                vowels++;
            } else {
                consonants++;
            }
        } else if (isdigit((unsigned char)ch)) {
            digits++;
        } else if (isspace((unsigned char)ch)) {
            spaces++;
        } else {
            specials++;
        }
    }

    printf("Analyzed Text: \\\"%s\\\"\\n\\n", text);
    printf("Vowels:             %2d\\n", vowels);
    printf("Consonants:         %2d\\n", consonants);
    printf("Numeric Digits:     %2d\\n", digits);
    printf("Spaces / Tabs:      %2d\\n", spaces);
    printf("Special Characters: %2d\\n", specials);

    return 0;
}""",
        "output": """Analyzed Text: "VTU Exam 2026: Linear Algebra & C Programming - 100% Score!"

Vowels:             16
Consonants:         22
Numeric Digits:      7
Spaces / Tabs:       8
Special Characters:  6""",
        "explanation": "1. The program examines each character in the string.\n2. Vowels (16) and consonants (22) are accurately separated.\n3. Digits '2', '0', '2', '6', '1', '0', '0' total 7.\n4. Colons, ampersands, hyphens, and exclamation marks are counted as special characters.",
        "mistakes": [
            ("Classifying non-vowels as consonants without verifying `isalpha()`.", "Spaces, punctuation, and digits are NOT vowels, but they are not consonants either! Always check `isalpha()` first."),
            ("Only checking lowercase vowels without handling uppercase characters.", "Missing uppercase vowels causes 'A', 'E', etc. to be misclassified as consonants.")
        ],
        "practice_q": "How would you construct a hash array of size 26 to count the exact frequency of every individual alphabet letter?"
    },
    {
        "num": 46,
        "title": "Array of Strings (2D char Array) and Alphabetical Sorting",
        "category": "Strings & Sorting",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Explain how an array of strings is represented using a 2D character array. Write a C program to sort a list of student names alphabetically using `strcmp()` and `strcpy()`.",
        "logic": "A 2D character array `char names[ROWS][COLS]` stores `ROWS` strings, each up to `COLS - 1` characters. Bubble sort compares adjacent strings using `strcmp() > 0` and swaps them using `strcpy()`.",
        "concept": "1. Memory Structure: `names[i]` represents a pointer to the $i$-th null-terminated string.\n2. Alphabetical Sort: If `strcmp(names[j], names[j+1]) > 0`, string $j$ comes after string $j+1$ alphabetically and they must be swapped.\n3. Swapping Strings: Requires a temporary buffer `char temp[COLS]` and three `strcpy()` operations.",
        "syntax": "char names[COUNT][MAX_LEN];\nif (strcmp(names[j], names[j+1]) > 0) { ... }",
        "code": """#include <stdio.h>
#include <string.h>

#define MAX_NAMES 5
#define MAX_LEN   30

void sortNamesAlphabetically(char names[MAX_NAMES][MAX_LEN], int count) {
    char temp[MAX_LEN];

    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - 1 - i; j++) {
            if (strcmp(names[j], names[j + 1]) > 0) {
                /* Swap strings */
                strcpy(temp, names[j]);
                strcpy(names[j], names[j + 1]);
                strcpy(names[j + 1], temp);
            }
        }
    }
}

int main(void) {
    char students[MAX_NAMES][MAX_LEN] = {
        "Vikram",
        "Ananya",
        "Rahul",
        "Deepa",
        "Karthik"
    };

    printf("=== Before Alphabetical Sorting ===\\n");
    for (int i = 0; i < MAX_NAMES; i++) {
        printf("  %d. %s\\n", i + 1, students[i]);
    }

    sortNamesAlphabetically(students, MAX_NAMES);

    printf("\\n=== After Alphabetical Sorting ===\\n");
    for (int i = 0; i < MAX_NAMES; i++) {
        printf("  %d. %s\\n", i + 1, students[i]);
    }

    return 0;
}""",
        "output": """=== Before Alphabetical Sorting ===
  1. Vikram
  2. Ananya
  3. Rahul
  4. Deepa
  5. Karthik

=== After Alphabetical Sorting ===
  1. Ananya
  2. Deepa
  3. Karthik
  4. Rahul
  5. Vikram""",
        "explanation": "1. `strcmp(\"Vikram\", \"Ananya\")` returns $> 0$, triggering a swap.\n2. Iterative passes place each name in alphabetical order.\n3. The sorted array begins with Ananya and ends with Vikram.",
        "mistakes": [
            ("Trying to swap using pointer assignment: `names[j] = names[j+1];`.", "Array rows in a 2D array are non-modifiable l-values. You cannot assign arrays; you must copy their contents with `strcpy()`."),
            ("Declaring `temp` too small.", "`temp` must be sized to `MAX_LEN` to prevent buffer overflow during swaps.")
        ],
        "practice_q": "How does using an array of pointers (`char *names[]`) make sorting strings faster compared to a 2D char array?"
    },
    {
        "num": 47,
        "title": "Selection Sort Algorithm: Logic, Trace, and Implementation",
        "category": "Sorting Algorithms",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "Exam Level"],
        "question": "Explain the Selection Sort algorithm. Write a C program to sort an array in ascending order and trace the selection of minimum elements pass-by-pass.",
        "logic": "Divides the array into a sorted sublist and an unsorted sublist. Repeatedly finds the minimum element from the unsorted sublist and swaps it with the first unsorted element.",
        "concept": "1. In pass $i$ (from 0 to $N-2$), assume `min_idx = i`.\n2. Iterate through index $j = i + 1$ to $N - 1$. If `arr[j] < arr[min_idx]`, update `min_idx = j`.\n3. After finding the minimum, swap `arr[i]` with `arr[min_idx]`.\n4. Property: Performs at most $N-1$ swaps, which is optimal when write operations are expensive (e.g. Flash/EEPROM memory).\n5. Time Complexity: $O(N^2)$ in all cases (Best, Worst, Average).",
        "syntax": "for (i=0; i<n-1; i++) { min=i; for(j=i+1; j<n; j++) if(a[j]<a[min]) min=j; swap(&a[i], &a[min]); }",
        "code": """#include <stdio.h>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;

        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }

        /* Swap minimum found with first unsorted element */
        if (minIdx != i) {
            int temp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = temp;
        }
    }
}

int main(void) {
    int data[] = {29, 10, 14, 37, 13};
    int n = sizeof(data) / sizeof(data[0]);

    printf("Original Array: ");
    for (int i = 0; i < n; i++) printf("%d ", data[i]);
    printf("\\n");

    selectionSort(data, n);

    printf("Sorted Array:   ");
    for (int i = 0; i < n; i++) printf("%d ", data[i]);
    printf("\\n");

    return 0;
}""",
        "output": """Original Array: 29 10 14 37 13 
Sorted Array:   10 13 14 29 37 """,
        "explanation": "1. Pass 1: Minimum in `{29, 10, 14, 37, 13}` is 10 at index 1. Swap with index 0: `{10, 29, 14, 37, 13}`.\n2. Pass 2: Minimum in `{29, 14, 37, 13}` is 13 at index 4. Swap with index 1: `{10, 13, 14, 37, 29}`.\n3. Pass 3: Minimum in `{14, 37, 29}` is 14 at index 2. Already in place.\n4. Pass 4: Minimum in `{37, 29}` is 29 at index 4. Swap with index 3: `{10, 13, 14, 29, 37}`.",
        "mistakes": [
            ("Swapping inside the inner loop.", "Selection sort finds the minimum over the ENTIRE unsorted range first, and performs only ONE swap per outer pass."),
            ("Assuming selection sort is stable.", "Standard selection sort is NOT stable because long-distance swaps can change the relative order of duplicate elements.")
        ],
        "practice_q": "How does the number of swaps in Selection Sort compare with Bubble Sort in the worst case?"
    },
    {
        "num": 48,
        "title": "Title Casing: Capitalize First Letter of Each Word in a Sentence",
        "category": "String Manipulation",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "Viva Question"],
        "question": "Write a complete C program to convert an arbitrary text string to Title Case (capitalizing the first character of every word and converting remaining letters to lowercase).",
        "logic": "Track state with a boolean flag `inWord`. If current character is an alphabet and not in a word, capitalize it and set `inWord = 1`. If whitespace is encountered, reset `inWord = 0`.",
        "concept": "1. Word Boundary: A word starts when a non-whitespace character follows whitespace (or starts at index 0).\n2. First letter of each word is converted using `toupper()`.\n3. All other letters within the word are converted using `tolower()`.\n4. Preserves spaces, digits, and punctuation untouched.",
        "syntax": "if (!inWord && isalpha(c)) { c = toupper(c); inWord = 1; }",
        "code": """#include <stdio.h>
#include <ctype.h>

void toTitleCase(char *str) {
    int inWord = 0;

    for (int i = 0; str[i] != '\\0'; i++) {
        if (isspace((unsigned char)str[i])) {
            inWord = 0; /* Space signals end of current word */
        } else {
            if (!inWord) {
                /* First character of a word */
                str[i] = (char)toupper((unsigned char)str[i]);
                inWord = 1;
            } else {
                /* Subsequent characters in word */
                str[i] = (char)tolower((unsigned char)str[i]);
            }
        }
    }
}

int main(void) {
    char sentence[] = "vTu eNgInEeRiNg mAtHeMaTiCs aNd c pRoGrAmMiNg";

    printf("Original:   \\\"%s\\\"\\n", sentence);
    toTitleCase(sentence);
    printf("Title Case: \\\"%s\\\"\\n", sentence);

    return 0;
}""",
        "output": """Original:   "vTu eNgInEeRiNg mAtHeMaTiCs aNd c pRoGrAmMiNg"
Title Case: "Vtu Engineering Mathematics And C Programming" """,
        "explanation": "1. The program tracks word transitions.\n2. The first letter of each word ('v', 'e', 'm', 'a', 'c', 'p') is capitalized.\n3. All other letters are normalized to lowercase.",
        "mistakes": [
            ("Only checking `str[i-1] == ' '` for word boundaries.", "Fails on the very first character at index 0 because `str[-1]` is an out-of-bounds memory access!"),
            ("Not handling multiple consecutive spaces or tabs.", "A boolean state flag (`inWord`) cleanly handles irregular spacing.")
        ],
        "practice_q": "How would you modify this program to keep acronyms (like VTU, USA, AI) in all-caps?"
    },
    {
        "num": 49,
        "title": "Substrings: Searching and Extracting Patterns without strstr()",
        "category": "String Manipulation",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Question", "Viva Favorite"],
        "question": "Implement pattern matching in C without using the library function `strstr()`. Find the starting index of a substring within a main string, or return -1 if not found.",
        "logic": "Iterate through the main string. At each position where the first character matches the pattern, check if the subsequent characters match. If the entire pattern matches, return the start index.",
        "concept": "1. Brute-Force Pattern Matching:\n- Outer loop index $i$ runs from 0 to $N - M$ (where $N = \\text{len}(text)$, $M = \\text{len}(pattern)$).\n- Inner loop index $j$ compares `text[i + j]` with `pattern[j]`.\n- If $j == M$, the full pattern was found at index $i$.\n2. Time Complexity: Worst Case $O(N \\times M)$, Best Case $O(N)$.",
        "syntax": "for(i=0; i<=n-m; i++) { for(j=0; j<m; j++) if(t[i+j]!=p[j]) break; if(j==m) return i; }",
        "code": """#include <stdio.h>
#include <string.h>

int findSubstring(const char *text, const char *pattern) {
    int n = (int)strlen(text);
    int m = (int)strlen(pattern);

    if (m == 0) return 0; /* Empty pattern matches at index 0 */

    for (int i = 0; i <= n - m; i++) {
        int j = 0;
        while (j < m && text[i + j] == pattern[j]) {
            j++;
        }
        if (j == m) {
            return i; /* Match found starting at index i */
        }
    }
    return -1; /* Not found */
}

int main(void) {
    const char *mainText = "VTU University Belagavi Campus";
    const char *query1 = "Belagavi";
    const char *query2 = "Bangalore";

    int pos1 = findSubstring(mainText, query1);
    int pos2 = findSubstring(mainText, query2);

    printf("Text: \\\"%s\\\"\\n", mainText);
    printf("Search \\\"%s\\\" -> %s (Index %d)\\n", 
           query1, pos1 != -1 ? "FOUND" : "NOT FOUND", pos1);
    printf("Search \\\"%s\\\" -> %s (Index %d)\\n", 
           query2, pos2 != -1 ? "FOUND" : "NOT FOUND", pos2);

    return 0;
}""",
        "output": """Text: "VTU University Belagavi Campus"
Search "Belagavi" -> FOUND (Index 15)
Search "Bangalore" -> NOT FOUND (Index -1)""",
        "explanation": "1. At index 15, 'B' matches `query1[0]`. Subsequent characters 'e','l','a','g','a','v','i' all match.\n2. Inner counter reaches `j == 8 == m`, returning index `15`.\n3. Searching for \"Bangalore\" exhaustively tests all positions with no full match, returning `-1`.",
        "mistakes": [
            ("Running outer loop to `i < n` instead of `i <= n - m`.", "Checking when fewer than `m` characters remain in `text` causes buffer overreads past the end of the main string."),
            ("Assuming `strstr()` returns an integer index.", "Standard `strstr()` returns a pointer (`char*`) to the first matching character, not an integer index. Convert with `ptr - text`.")
        ],
        "practice_q": "What is the Knuth-Morris-Pratt (KMP) algorithm and how does it achieve $O(N + M)$ pattern search?"
    },
    {
        "num": 50,
        "title": "Array Element Frequency Counter using Hash Array",
        "category": "1D Arrays",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "Exam Level"],
        "question": "Write a complete C program to count and display the frequency of each unique element in an integer array in $O(N)$ time using a frequency/hash array.",
        "logic": "Traverse the array and use element values as indices into a counting array: `freq[arr[i]]++`. Then iterate through the unique elements to print their counts.",
        "concept": "1. Direct Address Table / Hash Table concept.\n2. If values range from $0$ to $K$, an auxiliary array `int count[K + 1] = {0}` tracks counts in $O(1)$ per element.\n3. Total time is $O(N + K)$, avoiding the $O(N^2)$ nested loop approach.",
        "syntax": "freq[arr[i]]++;",
        "code": """#include <stdio.h>

#define MAX_VAL 100

int main(void) {
    int arr[] = {4, 2, 7, 4, 8, 2, 4, 3, 7, 4};
    int n = sizeof(arr) / sizeof(arr[0]);

    int freq[MAX_VAL + 1] = {0};
    int visited[MAX_VAL + 1] = {0};

    /* Build frequency table */
    for (int i = 0; i < n; i++) {
        freq[arr[i]]++;
    }

    printf("=== Frequency Distribution Table ===\\n");
    printf("%-10s | %-10s\\n", "Element", "Frequency");
    printf("-----------------------\\n");

    for (int i = 0; i < n; i++) {
        int val = arr[i];
        if (!visited[val]) {
            printf("%-10d | %-10d\\n", val, freq[val]);
            visited[val] = 1; /* Mark as reported */
        }
    }

    return 0;
}""",
        "output": """=== Frequency Distribution Table ===
Element    | Frequency 
-----------------------
4          | 4         
2          | 2         
7          | 2         
8          | 1         
3          | 1         """,
        "explanation": "1. Element 4 appears 4 times, 2 appears twice, 7 appears twice, 8 and 3 appear once.\n2. `visited` array prevents duplicate printing of already reported frequencies.\n3. The algorithm runs in $O(N)$ linear time.",
        "mistakes": [
            ("Using negative numbers as direct array indices.", "C does not allow negative array indices; `freq[-5]` accesses memory before the array, causing undefined behavior or crashes. Offset negative numbers by adding a bias constant."),
            ("Not initializing the frequency array to 0.", "Always zero-initialize the counting array (`= {0}`); otherwise, counts will be added to random stack garbage.")
        ],
        "practice_q": "How would you handle frequency counting if array elements can be up to $10^9$?"
    },
    {
        "num": 51,
        "title": "Output Prediction & Debugging: sizeof vs strlen on Arrays and Pointers",
        "category": "Debugging & Tracing",
        "difficulty": "Exam-Level",
        "exam_tags": ["Interview Trap", "Viva Favorite"],
        "question": "Analyze and explain the exact output of `sizeof` and `strlen` when applied to: (1) An array of characters, and (2) A pointer to a character literal.",
        "logic": "`sizeof` is a compile-time operator returning total allocated bytes. `strlen` is a runtime function counting characters up to `\\0`.",
        "concept": "Critical Differences:\n1. `char arr[20] = \"Hello\";`\n- `sizeof(arr)` = 20 bytes (full array allocation in memory).\n- `strlen(arr)` = 5 (characters before `\\0`).\n2. `char *ptr = \"Hello\";`\n- `sizeof(ptr)` = 4 or 8 bytes (size of memory pointer on 32-bit or 64-bit architecture).\n- `strlen(ptr)` = 5 (scans until `\\0`).\n3. Inside a function `void f(char a[])`:\n- The array decays into a pointer `char *`.\n- `sizeof(a)` returns pointer size (4 or 8), NOT the array size!",
        "syntax": "sizeof(arr) vs sizeof(ptr) vs strlen(arr)",
        "code": """#include <stdio.h>
#include <string.h>

void inspectParameter(char param[]) {
    printf("Inside Function (Array decays to pointer!):\\n");
    printf("  sizeof(param): %zu bytes (Pointer size!)\\n", sizeof(param));
    printf("  strlen(param): %zu characters\\n\\n", strlen(param));
}

int main(void) {
    char arr[30] = "VTU Computer Science";
    char *ptr = "VTU Computer Science";

    printf("In main() caller scope:\\n");
    printf("  sizeof(arr): %zu bytes (Total array buffer)\\n", sizeof(arr));
    printf("  strlen(arr): %zu characters\\n", strlen(arr));
    printf("  sizeof(ptr): %zu bytes (Pointer variable size)\\n", sizeof(ptr));
    printf("  strlen(ptr): %zu characters\\n\\n", strlen(ptr));

    inspectParameter(arr);

    return 0;
}""",
        "output": """In main() caller scope:
  sizeof(arr): 30 bytes (Total array buffer)
  strlen(arr): 20 characters
  sizeof(ptr): 8 bytes (Pointer variable size)
  strlen(ptr): 20 characters

Inside Function (Array decays to pointer!):
  sizeof(param): 8 bytes (Pointer size!)
  strlen(param): 20 characters""",
        "explanation": "1. `sizeof(arr)` yields 30 because the array was declared with size 30.\n2. `sizeof(ptr)` yields 8 (on 64-bit OS) because `ptr` is a pointer variable.\n3. Inside `inspectParameter`, `sizeof(param)` is 8 because arrays passed as arguments decay to pointers.\n4. `strlen()` correctly reports 20 in all cases by scanning for `\\0`.",
        "mistakes": [
            ("Writing `int len = sizeof(arr) / sizeof(arr[0]);` inside a function.", "Inside functions, `arr` has decayed to a pointer. This calculation will evaluate to `8 / 4 = 2` regardless of array length! Always pass length as an explicit parameter."),
            ("Assuming `strlen` includes the null terminator.", "`strlen` stops BEFORE `\\0`.")
        ],
        "practice_q": "What will `sizeof(\"Hello\")` evaluate to in C?"
    },
    {
        "num": 52,
        "title": "Module 2 Mastery: Comprehensive Array & String Diagnostic Review",
        "category": "Comprehensive Review",
        "difficulty": "Exam-Level",
        "exam_tags": ["Viva Must-Know", "Final Exam Checklist"],
        "question": "Provide a high-yield diagnostic checklist covering the top 5 array and string examination traps: Off-by-one errors, Buffer overflows, Array decay in functions, Unsafe gets(), and Missing null terminators.",
        "logic": "Synthesizes Module 2 into an exam review checklist to help prevent common implementation bugs.",
        "concept": "Top 5 Array & String Traps:\n1. Off-by-one: Declaring `int a[10]` and accessing `a[10]` (valid indices: 0 to 9).\n2. String missing `\\0`: Printing un-terminated char arrays reads past buffer bounds.\n3. Buffer overflow with `strcpy` / `gets`: Destination too small for input.\n4. Array decay: Forgetting that `sizeof(arr)` inside functions gives pointer size.\n5. Modifying string literals: `char *s = \"hi\"; s[0] = 'H';` causes segmentation fault.",
        "syntax": "gcc -fsanitize=address -Wall program.c",
        "code": """#include <stdio.h>
#include <string.h>

int main(void) {
    printf("=== Module 2 Exam Diagnostic Checklist ===\\n");
    printf("1. 1D Array 0-based bounds: a[0] to a[N-1]\\n");
    printf("2. 2D Row-Major Address: Base + (i * COLS + j) * sizeof(T)\\n");
    printf("3. Matrix Multiply: Valid iff cols(A) == rows(B)\\n");
    printf("4. Strings MUST terminate with '\\\\0' (ASCII 0)\\n");
    printf("5. Always use fgets(buf, sizeof(buf), stdin), NEVER gets()\\n");
    printf("6. Pass array sizes explicitly to functions\\n");
    printf("7. Use strcmp() for strings, NEVER '=='\\n");

    return 0;
}""",
        "output": """=== Module 2 Exam Diagnostic Checklist ===
1. 1D Array 0-based bounds: a[0] to a[N-1]
2. 2D Row-Major Address: Base + (i * COLS + j) * sizeof(T)
3. Matrix Multiply: Valid iff cols(A) == rows(B)
4. Strings MUST terminate with '\\0' (ASCII 0)
5. Always use fgets(buf, sizeof(buf), stdin), NEVER gets()
6. Pass array sizes explicitly to functions
7. Use strcmp() for strings, NEVER '=='""",
        "explanation": "1. Every rule represents a frequent source of student errors in lab exams and viva voce.\n2. Keeping these 7 principles in mind prevents memory corruption and runtime crashes.",
        "mistakes": [
            ("Writing to a string literal.", "Always use `char str[] = \"text\";` when you plan to modify string contents."),
            ("Forgetting that `strcmp` returns 0 for equal strings.", "Writing `if (strcmp(a, b))` checks if strings are DIFFERENT because 0 evaluates to false in C. Write `if (strcmp(a, b) == 0)` for equality.")
        ],
        "practice_q": "What GCC flag enables runtime bounds checking for arrays and memory buffers?"
    }
]

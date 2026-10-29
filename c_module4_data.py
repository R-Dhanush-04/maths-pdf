# -*- coding: utf-8 -*-
"""
C Programming - Module 4: Structures, Unions, and Dynamic Memory Allocation
Questions 77 to 102 (Structures, Padding, Unions, Typedef, Enums, Stack vs Heap, malloc, calloc, realloc, free, and Memory Safety)
"""

C_MODULE4_QUESTIONS = [
    {
        "num": 79,
        "title": "Structures: Motivation, Declaration, and Dot Operator",
        "category": "Structures",
        "difficulty": "Fundamental",
        "exam_tags": ["Core Concept", "Viva Must-Know"],
        "question": "What is a structure in C? Why are structures essential for managing heterogeneous data? Explain structure declaration, variable instantiation, and member access using the dot (`.`) operator.",
        "logic": "Arrays are restricted to homogeneous data (all elements must have the same type). A structure (`struct`) groups related variables of different data types under a single user-defined composite type.",
        "concept": "1. Definition: `struct TagName { member1_type m1; member2_type m2; ... };`\n2. Instantiation:\n- With definition: `struct Book { ... } b1, b2;`\n- Independent: `struct Book b1;`\n3. Member Access: Use the direct member access operator (dot `.`): `b1.price = 450.0;`.\n4. Memory Allocation: Total memory allocated for a structure is at least the sum of its members, subject to CPU structure alignment and padding rules.",
        "syntax": "struct Student s1; s1.rollNo = 101;",
        "code": """#include <stdio.h>
#include <string.h>

/* Structure Declaration */
struct Book {
    int id;
    char title[40];
    char author[30];
    double price;
};

int main(void) {
    /* Structure Variable Instantiation and Member Assignment */
    struct Book b1;

    b1.id = 1001;
    strcpy(b1.title, "The C Programming Language");
    strcpy(b1.author, "Kernighan & Ritchie");
    b1.price = 599.50;

    printf("=== Structure Member Access (Dot Operator) ===\\n");
    printf("Book ID:     %d\\n", b1.id);
    printf("Book Title:  \\\"%s\\\"\\n", b1.title);
    printf("Author:      %s\\n", b1.author);
    printf("Price:       %.2f INR\\n", b1.price);
    printf("Total Size:  %zu bytes in RAM\\n", sizeof(struct Book));

    return 0;
}""",
        "output": """=== Structure Member Access (Dot Operator) ===
Book ID:     1001
Book Title:  "The C Programming Language"
Author:      Kernighan & Ritchie
Price:       599.50 INR
Total Size:  88 bytes in RAM""",
        "explanation": "1. `struct Book` defines a composite type with 4 heterogeneous members.\n2. The dot operator `.` accesses individual members for reading and writing.\n3. `sizeof(struct Book)` returns 88 bytes, which includes internal member alignment padding.",
        "mistakes": [
            ("Attempting string assignment directly: `b1.title = \"Text\";`.", "Array members in structures cannot be assigned directly after declaration. Use `strcpy(b1.title, \"Text\")` or designated initializers."),
            ("Forgetting the terminating semicolon after the structure definition: `struct X { int a; }`.", "The closing brace of a structure definition must always be followed by a semicolon `;`.")
        ],
        "practice_q": "Can two different structures contain member variables with the exact same name? Explain."
    },
    {
        "num": 80,
        "title": "Structure Padding, Byte Alignment, and the #pragma pack Directive",
        "category": "Structures & Memory",
        "difficulty": "Intermediate",
        "exam_tags": ["Interview Favorite", "High Yield Viva"],
        "question": "Why is `sizeof(struct)` often larger than the sum of its individual member sizes? Explain byte alignment, structure padding, and how `#pragma pack(1)` eliminates padding.",
        "logic": "Modern CPUs fetch data in 4-byte or 8-byte word blocks. Accessing unaligned memory addresses requires multiple bus cycles. Compilers insert unused padding bytes between members to align each data type to its natural boundary.",
        "concept": "1. Natural Alignment Rules (on 64-bit systems):\n- `char` (1 byte): Any address boundary.\n- `short` (2 bytes): Even address (divisible by 2).\n- `int` / `float` (4 bytes): Address divisible by 4.\n- `double` / pointers (8 bytes): Address divisible by 8.\n2. Total Structure Alignment: The overall structure size must be a multiple of its largest member's alignment requirement (trailing padding).\n3. Structure Member Reordering: Ordering members from largest to smallest minimizes padding bytes.\n4. `#pragma pack(1)`: Instructs the compiler to eliminate all padding bytes, packing members tightly (used in network protocols and hardware drivers).",
        "syntax": "#pragma pack(1) /* Pack structures without padding */",
        "code": """#include <stdio.h>

/* Normal Unpacked Structure: Has padding bytes */
struct PaddedStruct {
    char c1;     /* 1 byte + 3 padding bytes */
    int i;       /* 4 bytes */
    char c2;     /* 1 byte + 7 padding bytes */
    double d;    /* 8 bytes */
};

/* Packed Structure: Zero padding bytes */
#pragma pack(push, 1)
struct PackedStruct {
    char c1;     /* 1 byte */
    int i;       /* 4 bytes */
    char c2;     /* 1 byte */
    double d;    /* 8 bytes */
};
#pragma pack(pop)

int main(void) {
    printf("=== Structure Padding & Memory Alignment Analysis ===\\n");
    printf("Theoretical sum of members: 1 + 4 + 1 + 8 = 14 bytes\\n\\n");

    printf("sizeof(struct PaddedStruct): %zu bytes (Compiler inserted padding!)\\n", 
           sizeof(struct PaddedStruct));
    printf("sizeof(struct PackedStruct): %zu bytes (Packed tightly with #pragma pack)\\n", 
           sizeof(struct PackedStruct));

    return 0;
}""",
        "output": """=== Structure Padding & Memory Alignment Analysis ===
Theoretical sum of members: 1 + 4 + 1 + 8 = 14 bytes

sizeof(struct PaddedStruct): 24 bytes (Compiler inserted padding!)
sizeof(struct PackedStruct): 14 bytes (Packed tightly with #pragma pack)""",
        "explanation": "1. In `PaddedStruct`: `c1` uses 1 byte followed by 3 padding bytes to align `int i` to a 4-byte boundary. `c2` uses 1 byte followed by 7 padding bytes to align `double d` to an 8-byte boundary. Total: 24 bytes.\n2. In `PackedStruct`: `#pragma pack(1)` removes all padding, reducing size to the exact sum: 14 bytes.",
        "mistakes": [
            ("Using `#pragma pack(1)` indiscriminately in performance-critical code.", "Packed structures can cause misaligned memory accesses, increasing CPU memory bus cycles and degrading performance on some architectures."),
            ("Assuming `sizeof(struct)` is simply the sum of its member sizes.", "Always verify structure sizes using `sizeof()` due to alignment padding.")
        ],
        "practice_q": "How can you reorder the members of `struct PaddedStruct` to minimize padding without using `#pragma pack`?"
    },
    {
        "num": 81,
        "title": "Array of Structures: Student Record Management System",
        "category": "Structures",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "What is an array of structures? Write a complete C program to manage an array of N student records (Roll, Name, Marks in 3 subjects), calculate total and percentage, and display results in formatted tabular form.",
        "logic": "An array of structures stores multiple instances of a structure type contiguously in memory, accessed via array index and member dot notation: `students[i].rollNo`.",
        "concept": "1. Declaration: `struct Student batch[50];`\n2. Indexing: `batch[0]` is the first student record, `batch[1]` is the second, etc.\n3. Member Access: `batch[i].memberName`.\n4. Memory Allocation: Total memory is `N * sizeof(struct Student)`.",
        "syntax": "struct Student students[MAX];\nstudents[i].marks = 95;",
        "code": """#include <stdio.h>

#define MAX_STUDENTS 3

struct Student {
    int rollNo;
    char name[30];
    int marks[3];
    int total;
    double percentage;
};

int main(void) {
    /* Initializing array of structures */
    struct Student batch[MAX_STUDENTS] = {
        {101, "Rahul Sharma",    {85, 90, 88}, 0, 0.0},
        {102, "Pooja Hegde",      {92, 95, 96}, 0, 0.0},
        {103, "Aditya Kulkarni",  {78, 82, 80}, 0, 0.0}
    };

    /* Process calculations */
    for (int i = 0; i < MAX_STUDENTS; i++) {
        batch[i].total = batch[i].marks[0] + batch[i].marks[1] + batch[i].marks[2];
        batch[i].percentage = (double)batch[i].total / 3.0;
    }

    printf("====================================================================\\n");
    printf("| %-6s | %-16s | %-12s | %-6s | %-8s |\\n", 
           "ROLL", "NAME", "MARKS (M1,M2,M3)", "TOTAL", "PERCENT");
    printf("====================================================================\\n");

    for (int i = 0; i < MAX_STUDENTS; i++) {
        printf("| %-6d | %-16s | %2d, %2d, %2d        | %-6d | %6.2f%%  |\\n",
               batch[i].rollNo, batch[i].name,
               batch[i].marks[0], batch[i].marks[1], batch[i].marks[2],
               batch[i].total, batch[i].percentage);
    }
    printf("====================================================================\\n");

    return 0;
}""",
        "output": """====================================================================
| ROLL   | NAME             | MARKS (M1,M2,M3) | TOTAL  | PERCENT  |
====================================================================
| 101    | Rahul Sharma     | 85, 90, 88        | 263    |  87.67%  |
| 102    | Pooja Hegde      | 92, 95, 96        | 283    |  94.33%  |
| 103    | Aditya Kulkarni  | 78, 82, 80        | 240    |  80.00%  |
====================================================================""",
        "explanation": "1. `batch[MAX_STUDENTS]` allocates storage for 3 student records.\n2. Nested members are accessed via `batch[i].marks[j]`.\n3. The loop computes totals and percentages, then prints a formatted grade sheet.",
        "mistakes": [
            ("Using `batch.rollNo[i]` instead of `batch[i].rollNo`.", "`batch` is an array of structures, not a structure of arrays. Index the structure first, then access the member."),
            ("Reading strings with spaces into `batch[i].name` using `scanf(\"%s\")`.", "Use `scanf(\" %29[^\\n]\", batch[i].name)` to support names with spaces.")
        ],
        "practice_q": "How would you sort an array of student structures in descending order of their total marks?"
    },
    {
        "num": 82,
        "title": "Nested Structures: Hierarchical Data Modeling and Date of Joining",
        "category": "Structures",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "Exam Question"],
        "question": "What is a nested structure? Explain the difference between separate and embedded definitions. Write a program to model an Employee record with a nested Date of Joining structure.",
        "logic": "A nested structure is a structure that contains another structure as one of its members, enabling hierarchical data modeling.",
        "concept": "1. Separate Declaration (Recommended for reusability):\n```c\nstruct Date { int day, month, year; };\nstruct Employee { int id; struct Date doj; };\n```\n2. Embedded Declaration (Inner structure is private to outer structure):\n```c\nstruct Employee { int id; struct Date { int d, m, y; } doj; };\n```\n3. Chained Dot Access: Access members through chained dot operators: `emp1.doj.year = 2026;`.\n4. Memory Allocation: The inner structure's bytes are placed directly inside the outer structure.",
        "syntax": "emp1.doj.day = 15; emp1.doj.month = 8; emp1.doj.year = 2024;",
        "code": """#include <stdio.h>

/* Independent, reusable inner structure */
struct Date {
    int day;
    int month;
    int year;
};

/* Outer structure incorporating Date */
struct Employee {
    int empId;
    char name[30];
    double salary;
    struct Date doj; /* Nested structure member */
};

int main(void) {
    struct Employee emp = {
        7042,
        "Sunil Gavaskar",
        125000.0,
        {1, 4, 2022} /* Initializer for nested Date */
    };

    printf("=== Employee Record (Nested Structure) ===\\n");
    printf("Employee ID:     %d\\n", emp.empId);
    printf("Employee Name:   %s\\n", emp.name);
    printf("Monthly Salary:  %.2f INR\\n", emp.salary);
    printf("Date of Joining: %02d/%02d/%04d\\n", 
           emp.doj.day, emp.doj.month, emp.doj.year);

    return 0;
}""",
        "output": """=== Employee Record (Nested Structure) ===
Employee ID:     7042
Employee Name:   Sunil Gavaskar
Monthly Salary:  125000.00 INR
Date of Joining: 01/04/2022""",
        "explanation": "1. `struct Date` is declared independently and reused inside `struct Employee`.\n2. Chained dot notation `emp.doj.year` accesses the nested structure member.\n3. Nested initializers `{1, 4, 2022}` populate the inner `doj` member cleanly.",
        "mistakes": [
            ("Attempting to nest a structure directly inside itself by value: `struct Node { struct Node next; };`.", "A structure cannot contain an instance of itself by value because its size would be infinitely recursive! It can only contain a POINTER to itself: `struct Node *next;`."),
            ("Using wrong dot syntax: `emp.day` instead of `emp.doj.day`.", "You must traverse every level of nesting explicitly.")
        ],
        "practice_q": "What is the size in bytes of `struct Employee` on your compiler?"
    },
    {
        "num": 83,
        "title": "Passing Structures to Functions: By Value vs By Reference with Arrow (->)",
        "category": "Structures & Pointers",
        "difficulty": "Intermediate",
        "exam_tags": ["High Yield Exam", "Viva Must-Know"],
        "question": "Compare passing structures by value versus passing pointers to structures (by reference). Explain the Arrow operator (`->`) and show why `ptr->member` is preferred over `(*ptr).member`.",
        "logic": "Passing large structures by value copies every member byte onto the stack, incurring significant performance overhead. Passing a structure pointer passes only an 8-byte address, enabling fast $O(1)$ parameter passing and in-place modifications.",
        "concept": "1. Pass by Value: `void display(struct Student s)` -> Clones the entire structure on the stack. Inefficient for large structures.\n2. Pass by Reference: `void display(const struct Student *s)` -> Passes an 8-byte pointer. Fast and memory-efficient. Use `const` if the function only reads data.\n3. Arrow Operator (`->`):\n- Syntax: `ptr->member`\n- Equivalent to: `(*ptr).member`\n- The parentheses in `(*ptr).member` are mandatory because dot `.` has higher precedence than dereference `*`. Writing `*ptr.member` is interpreted as `*(ptr.member)`, causing a compilation error. The arrow operator `->` avoids this syntax pitfall.",
        "syntax": "ptr->member == (*ptr).member",
        "code": """#include <stdio.h>

struct Account {
    long long accNumber;
    double balance;
};

/* 1. Pass by Reference: Modifies original structure */
void applyAnnualInterest(struct Account *acc, double ratePercent) {
    /* Arrow operator cleanly accesses and updates member */
    acc->balance += acc->balance * (ratePercent / 100.0);
}

/* 2. Pass by Reference (Read-Only): const protects data */
void displayAccount(const struct Account *acc) {
    printf("Account: %lld | Balance: %.2f INR (Via arrow operator ->)\\n", 
           acc->accNumber, acc->balance);
}

int main(void) {
    struct Account myAcc = {9876543210LL, 50000.0};

    printf("Initial Account Status:\\n");
    displayAccount(&myAcc);

    /* Apply 7.5% annual interest */
    applyAnnualInterest(&myAcc, 7.5);

    printf("\\nAfter Applying 7.5%% Interest:\\n");
    displayAccount(&myAcc);

    return 0;
}""",
        "output": """Initial Account Status:
Account: 9876543210 | Balance: 50000.00 INR (Via arrow operator ->)

After Applying 7.5% Interest:
Account: 9876543210 | Balance: 53750.00 INR (Via arrow operator ->)""",
        "explanation": "1. `displayAccount` and `applyAnnualInterest` take `struct Account *acc`, passing only an 8-byte pointer.\n2. `acc->balance` accesses the balance through the pointer.\n3. The balance is updated from 50,000 to 53,750 directly in `myAcc`'s memory.",
        "mistakes": [
            ("Writing `*ptr.member` instead of `(*ptr).member` or `ptr->member`.", "Operator precedence causes `ptr.member` to evaluate first, which fails because `ptr` is a pointer, not a structure."),
            ("Using the arrow operator on a regular structure variable: `myAcc->balance`.", "The arrow operator requires a pointer on its left side. For regular structure variables, use the dot operator `myAcc.balance`.")
        ],
        "practice_q": "Why is passing structures via `const struct Type *` considered a best practice in C?"
    },
    {
        "num": 84,
        "title": "Unions in C: Shared Memory Mechanics and Differences from Structures",
        "category": "Unions",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Theory", "Viva Must-Know"],
        "question": "What is a `union` in C? How does memory allocation in a union differ from a structure? Illustrate with a side-by-side memory diagram and code showing member value overwrite.",
        "logic": "A union is a user-defined composite type where all members share the SAME memory location. The size of a union equals the size of its largest member (plus alignment padding). Only ONE member can hold a valid value at any given time.",
        "concept": "Comprehensive Differences Table:\n1. Keyword: `struct` vs `union`.\n2. Memory Allocation:\n- Structure: Allocates separate, contiguous memory for every member (sum of members + padding).\n- Union: Allocates a single shared memory block sized to its largest member.\n3. Member Value Storage:\n- Structure: All members store distinct, independent values simultaneously.\n- Union: Only one member can store a meaningful value at a time; writing to one member overwrites all other members.\n4. Purpose: Structures model composite records (e.g. Employee); Unions model variant types or shared hardware register bits.",
        "syntax": "union Data { int i; float f; char ch; };",
        "code": """#include <stdio.h>

/* Structure: Each member has its own storage */
struct DemoStruct {
    char ch;    /* 1 byte */
    int num;    /* 4 bytes */
    double dbl; /* 8 bytes */
};

/* Union: All members share the same storage */
union DemoUnion {
    char ch;    /* 1 byte */
    int num;    /* 4 bytes */
    double dbl; /* 8 bytes */
};

int main(void) {
    printf("=== Structure vs Union Memory Footprint ===\\n");
    printf("sizeof(struct DemoStruct): %zu bytes (Sum of all members + padding)\\n", 
           sizeof(struct DemoStruct));
    printf("sizeof(union DemoUnion):   %zu bytes (Size of largest member: double)\\n\\n", 
           sizeof(union DemoUnion));

    /* Demonstration of Shared Memory Overwrite */
    union DemoUnion u;

    u.num = 65;
    printf("Stored u.num = 65 -> u.num: %d | u.ch (interpreted as char): '%c'\\n", 
           u.num, u.ch);

    u.dbl = 3.14159;
    printf("Stored u.dbl = 3.14159 -> u.dbl: %.5f\\n", u.dbl);
    printf("Checking u.num after storing double: %d (CORRUPTED / OVERWRITTEN!)\\n", u.num);

    return 0;
}""",
        "output": """=== Structure vs Union Memory Footprint ===
sizeof(struct DemoStruct): 16 bytes (Sum of all members + padding)
sizeof(union DemoUnion):   8 bytes (Size of largest member: double)

Stored u.num = 65 -> u.num: 65 | u.ch (interpreted as char): 'A'
Stored u.dbl = 3.14159 -> u.dbl: 3.14159
Checking u.num after storing double: 1374389535 (CORRUPTED / OVERWRITTEN!)""",
        "explanation": "1. `DemoStruct` requires 16 bytes to store all members simultaneously.\n2. `DemoUnion` requires only 8 bytes (the size of its largest member, `double`).\n3. Setting `u.num = 65` sets the lowest byte to 65 (ASCII `'A'`).\n4. Assigning `u.dbl = 3.14159` overwrites the shared memory, corrupting `u.num`.",
        "mistakes": [
            ("Expecting a union to retain values of multiple members simultaneously.", "A union only stores one member's value at a time; writing to member B overwrites member A."),
            ("Assuming `sizeof(union)` is always the exact size of the largest member.", "Structure alignment rules also apply to unions: if a union contains a 3-byte array and an integer, the total size is padded to a multiple of 4.")
        ],
        "practice_q": "What is a 'tagged union' and how does an accompanying enum help track the currently active union member?"
    },
    {
        "num": 85,
        "title": "typedef and Enumerations (enum): Type Safety and State Machines",
        "category": "User-Defined Types",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Question", "Viva Favorite"],
        "question": "What is the purpose of `typedef` in C? Explain Enumerations (`enum`), their default integral values, and how to use `enum` to implement a traffic light state machine.",
        "logic": "`typedef` creates new alias names for existing types. `enum` defines a user-defined type whose values are named integer constants, improving code clarity and readability.",
        "concept": "1. `typedef` Syntax: `typedef existing_type new_name;`\n- Example: `typedef unsigned long long uint64;`\n- Eliminates repetitive `struct Tag` keywords: `typedef struct { ... } Student;`.\n2. `enum` Mechanics:\n- Members are compile-time integer constants.\n- By default, the first member is 0, and each subsequent member increments by 1.\n- Custom values can be assigned: `enum Status { OK = 200, NOT_FOUND = 404 };`.\n- Enhances readability over magic numbers in state machines and return codes.",
        "syntax": "typedef enum { RED, YELLOW, GREEN } TrafficLight;",
        "code": """#include <stdio.h>

/* Using typedef with enum for clean type definitions */
typedef enum {
    STATE_RED = 1,
    STATE_YELLOW,
    STATE_GREEN
} TrafficSignal;

/* Function processing enum state */
void displaySignalInstruction(TrafficSignal signal) {
    switch (signal) {
        case STATE_RED:
            printf("Signal: RED (Stop vehicle immediately)\\n");
            break;
        case STATE_YELLOW:
            printf("Signal: YELLOW (Prepare to stop or proceed with caution)\\n");
            break;
        case STATE_GREEN:
            printf("Signal: GREEN (Safe to proceed)\\n");
            break;
        default:
            printf("Signal: INVALID\\n");
            break;
    }
}

int main(void) {
    TrafficSignal current = STATE_RED;

    printf("=== Traffic Signal State Machine ===\\n");
    displaySignalInstruction(current);

    current = STATE_GREEN;
    displaySignalInstruction(current);

    printf("\\nUnderlying Integer Values:\\n");
    printf("STATE_RED:    %d\\n", STATE_RED);
    printf("STATE_YELLOW: %d (auto-incremented)\\n", STATE_YELLOW);
    printf("STATE_GREEN:  %d (auto-incremented)\\n", STATE_GREEN);

    return 0;
}""",
        "output": """=== Traffic Signal State Machine ===
Signal: RED (Stop vehicle immediately)
Signal: GREEN (Safe to proceed)

Underlying Integer Values:
STATE_RED:    1
STATE_YELLOW: 2 (auto-incremented)
STATE_GREEN:  3 (auto-incremented)""",
        "explanation": "1. `STATE_RED` is assigned 1; `STATE_YELLOW` and `STATE_GREEN` automatically increment to 2 and 3.\n2. `typedef enum { ... } TrafficSignal;` creates a clean type alias, eliminating the need to repeat `enum TrafficSignal`.\n3. State machines using enums make control logic readable and self-documenting.",
        "mistakes": [
            ("Confusing `typedef` with `#define`.", "`#define` is a text substitution handled by the preprocessor without type checking. `typedef` is handled by the compiler with full type safety."),
            ("Assuming `enum` variables cannot hold values outside the declared enumerators.", "In C, `enum` is backed by integers. Assigning an arbitrary integer like `current = 99` is technically permitted by the compiler, though poor practice.")
        ],
        "practice_q": "What will be the integer values of `enum Sample { A = 5, B, C = 10, D };`?"
    },
    {
        "num": 86,
        "title": "C Program Memory Architecture: Text, Data, BSS, Stack, and Heap",
        "category": "Memory Architecture",
        "difficulty": "Intermediate",
        "exam_tags": ["Core Architecture", "Viva Must-Know"],
        "question": "Diagram and describe the standard 5 memory segments of a compiled C program: Text (Code), Initialized Data (.data), Uninitialized Data (.bss), Heap, and Stack.",
        "logic": "When an executable is loaded into RAM by the OS, its virtual address space is organized into 5 functional memory segments.",
        "concept": "1. Text Segment (Code): Contains compiled machine instructions. Marked Read-Only to prevent accidental modification; shared among concurrent processes.\n2. Initialized Data Segment (`.data`): Contains global and static variables explicitly initialized with non-zero values (e.g. `int g = 10;`). Stored in the binary on disk.\n3. Uninitialized Data Segment (`.bss`): Contains uninitialized global and static variables. Does NOT consume disk space in the binary; automatically initialized to zero by the OS loader.\n4. Heap: Region for Dynamic Memory Allocation (`malloc`, `calloc`). Grows UPWARD toward higher memory addresses. Managed manually by the programmer.\n5. Stack: Region for function call frames, local variables, parameters, and return addresses. Grows DOWNWARD toward lower memory addresses. Managed automatically by the CPU.",
        "syntax": "Text -> Data (.data / .bss) -> Heap (grows up) -> Stack (grows down)",
        "code": """#include <stdio.h>
#include <stdlib.h>

/* 1. Initialized Data Segment (.data) */
int globalInitialized = 42;

/* 2. Uninitialized Data Segment (.bss) -> Zeroed automatically */
int globalUninitialized;

int main(void) {
    /* 3. Stack Segment (Local variables) */
    int stackVar = 100;

    /* 4. Heap Segment (Dynamic memory) */
    int *heapVar = (int *)malloc(sizeof(int));
    if (heapVar != NULL) *heapVar = 500;

    printf("=== Process Memory Segment Address Verification ===\\n");
    printf("1. Text/Code Segment (main func):       %p (Lowest RAM)\\n", (void*)&main);
    printf("2. Initialized Data Segment (.data):    %p\\n", (void*)&globalInitialized);
    printf("3. Uninitialized Data Segment (.bss):   %p\\n", (void*)&globalUninitialized);
    printf("4. Heap Segment (malloc address):       %p (Grows Upward)\\n", (void*)heapVar);
    printf("5. Stack Segment (stackVar address):    %p (Highest RAM / Grows Down)\\n", (void*)&stackVar);

    free(heapVar);
    return 0;
}""",
        "output": """=== Process Memory Segment Address Verification ===
1. Text/Code Segment (main func):       0x55d4a1b01169 (Lowest RAM)
2. Initialized Data Segment (.data):    0x55d4a1b04018
3. Uninitialized Data Segment (.bss):   0x55d4a1b04024
4. Heap Segment (malloc address):       0x55d4a2b9a2a0 (Grows Upward)
5. Stack Segment (stackVar address):    0x7ffd5a68acc4 (Highest RAM / Grows Down)""",
        "explanation": "1. Text (function address) sits lowest in memory.\n2. Data and BSS follow right above Text.\n3. Heap is allocated above BSS, growing upward toward higher addresses.\n4. Stack is allocated near the top of the user address space (`0x7ffd...`), growing downward.",
        "mistakes": [
            ("Assuming uninitialized global variables contain garbage.", "Uninitialized global/static variables reside in `.bss` and are guaranteed to be zeroed by the runtime loader."),
            ("Believing stack and heap share the same allocation mechanism.", "Stack allocation is a single CPU pointer adjustment (sub rsp); heap allocation requires searching free-lists via OS syscalls.")
        ],
        "practice_q": "What happens when the stack and heap grow into each other due to unbounded allocation?"
    },
    {
        "num": 87,
        "title": "Stack vs Heap Memory: Allocation Speed, Lifetime, and Management",
        "category": "Memory Management",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Theory", "Viva Must-Know"],
        "question": "Provide a comprehensive comparative analysis between Stack and Heap memory. Compare them across: Allocation Mechanism, Allocation Speed, Lifetime, Flexibility, and Failure Modes.",
        "logic": "Stack memory is fast and managed automatically by the CPU, but has fixed size and block scope. Heap memory is flexible and persists until explicitly freed, but is slower and requires manual management.",
        "concept": "Comparison Table:\n1. Management:\n- Stack: Fully automatic by compiler/CPU stack pointer.\n- Heap: Manual by programmer (`malloc()` / `free()`).\n2. Allocation Speed:\n- Stack: Extremely fast (single CPU instruction).\n- Heap: Slower (requires searching free-list, fragmentation handling, OS syscalls).\n3. Size & Scope:\n- Stack: Limited (typically 1 MB to 8 MB). Block scope.\n- Heap: Large (constrained only by available physical RAM and swap space). Global access.\n4. Resizing:\n- Stack: Fixed at compile time.\n- Heap: Resizable dynamically at runtime using `realloc()`.\n5. Failure Modes:\n- Stack: Stack Overflow (infinite recursion, massive local arrays).\n- Heap: Memory Leaks, Dangling Pointers, Heap Fragmentation.",
        "syntax": "Stack: int arr[100];\nHeap: int *arr = malloc(100 * sizeof(int));",
        "code": """#include <stdio.h>
#include <stdlib.h>

void stackVsHeapDemo(void) {
    /* Stack: Automatic lifetime, freed when function returns */
    int stackArray[5] = {1, 2, 3, 4, 5};

    /* Heap: Dynamic lifetime, persists until free() is called */
    int *heapArray = (int *)malloc(5 * sizeof(int));
    if (heapArray == NULL) return;

    for (int i = 0; i < 5; i++) {
        heapArray[i] = stackArray[i] * 10;
    }

    printf("Stack Array[0]: %d | Heap Array[0]: %d\\n", stackArray[0], heapArray[0]);

    /* Programmer MUST explicitly free heap memory */
    free(heapArray);
}

int main(void) {
    printf("=== Stack vs Heap Demonstration ===\\n");
    stackVsHeapDemo();
    printf("Function completed: Stack memory reclaimed automatically; Heap memory freed explicitly.\\n");
    return 0;
}""",
        "output": """=== Stack vs Heap Demonstration ===
Stack Array[0]: 1 | Heap Array[0]: 10
Function completed: Stack memory reclaimed automatically; Heap memory freed explicitly.""",
        "explanation": "1. `stackArray` is allocated on the stack and automatically freed upon return.\n2. `heapArray` persists in heap memory until `free()` is explicitly called.\n3. Omitting `free()` results in a memory leak.",
        "mistakes": [
            ("Allocating very large arrays on the stack (`int large[10000000];`).", "Exceeds standard 1MB/8MB stack limits, causing an instant Stack Overflow crash. Large allocations belong on the heap via `malloc()`."),
            ("Assuming `free()` sets the pointer to NULL.", "`free()` releases the memory block, but the pointer still holds the old address (a dangling pointer). Always set `ptr = NULL;` after `free()`.")
        ],
        "practice_q": "What is the typical default stack size on Windows and Linux?"
    },
    {
        "num": 88,
        "title": "Dynamic Memory Allocation: malloc() Function and NULL Verification",
        "category": "DMA Functions",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "Core Concept"],
        "question": "Explain the `malloc()` function from `<stdlib.h>`. Detail its prototype, memory zeroing non-guarantee, mandatory NULL return check, and write a program to allocate a dynamic 1D array.",
        "logic": "`malloc()` (Memory Allocate) requests a contiguous block of memory of the specified number of bytes from the heap. It returns a generic `void *` pointer to the first byte, or `NULL` if allocation fails.",
        "concept": "1. Prototype: `void *malloc(size_t size);`\n2. Key Properties:\n- Takes total bytes as argument: `n * sizeof(int)`.\n- Does NOT initialize memory; allocated bytes contain arbitrary garbage values.\n- Returns `NULL` if system memory is exhausted.\n- Memory persists until explicitly released with `free()` or program terminates.\n3. Defensive Pattern: ALWAYS check `if (ptr == NULL)` before accessing allocated memory.",
        "syntax": "int *ptr = (int *)malloc(n * sizeof(int));\nif (ptr == NULL) { /* handle error */ }",
        "code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n = 5;

    /* Request heap memory for 5 integers */
    int *arr = (int *)malloc(n * sizeof(int));

    /* Mandatory NULL verification */
    if (arr == NULL) {
        fprintf(stderr, "Error: Memory allocation failed!\\n");
        return 1;
    }

    printf("=== Dynamic 1D Array via malloc() ===\\n");
    printf("Allocated %d integers (%zu bytes) on the heap successfully.\\n", 
           n, n * sizeof(int));

    /* Initialize and print array */
    for (int i = 0; i < n; i++) {
        arr[i] = (i + 1) * 10;
        printf("arr[%d] = %d\\n", i, arr[i]);
    }

    /* Free dynamically allocated memory */
    free(arr);
    arr = NULL; /* Neutralize dangling pointer */

    return 0;
}""",
        "output": """=== Dynamic 1D Array via malloc() ===
Allocated 5 integers (20 bytes) on the heap successfully.
arr[0] = 10
arr[1] = 20
arr[2] = 30
arr[3] = 40
arr[4] = 50""",
        "explanation": "1. `malloc(5 * sizeof(int))` allocates 20 contiguous bytes on the heap.\n2. The `NULL` check ensures the allocation succeeded before dereferencing.\n3. `free(arr)` releases the memory back to the heap, and `arr = NULL` prevents dangling pointer bugs.",
        "mistakes": [
            ("Forgetting the `NULL` check after `malloc()`.", "If memory allocation fails and `malloc()` returns `NULL`, accessing `arr[0]` dereferences a null pointer, crashing the program."),
            ("Passing element count instead of byte count: `malloc(n)` instead of `malloc(n * sizeof(int))`.", "Allocates only `n` bytes instead of `n * 4` bytes, causing buffer overflow when indexing elements.")
        ],
        "practice_q": "Why does C not strictly require typecasting the return value of `malloc()` like `(int *)malloc(...)`?"
    },
    {
        "num": 89,
        "title": "The calloc() Function: Contiguous Allocation and Zero-Initialization",
        "category": "DMA Functions",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "Viva Must-Know"],
        "question": "Explain `calloc()` from `<stdlib.h>`. Compare it with `malloc()` regarding arguments and memory initialization. Write a program demonstrating clean zero-initialization.",
        "logic": "`calloc()` (Contiguous Allocation) allocates memory for an array of elements and automatically clears all allocated bytes to zero.",
        "concept": "1. Prototype: `void *calloc(size_t num_elements, size_t element_size);`\n2. Key Differences from `malloc()`:\n- Parameter Count: `calloc` takes 2 arguments (`num, size`); `malloc` takes 1 argument (`total_bytes`).\n- Initialization: `calloc` initializes all allocated bits to zero; `malloc` leaves memory containing arbitrary garbage values.\n- Overflow Protection: `calloc` checks for integer overflow in `num * size` on many implementations.\n- Performance: `malloc` is slightly faster because it does not incur the overhead of writing zeros.",
        "syntax": "int *ptr = (int *)calloc(n, sizeof(int));",
        "code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n = 5;

    /* Allocate and zero-initialize 5 integers */
    int *callocArr = (int *)calloc(n, sizeof(int));
    if (callocArr == NULL) {
        printf("Allocation failed!\\n");
        return 1;
    }

    printf("=== Verification of calloc() Zero-Initialization ===\\n");
    for (int i = 0; i < n; i++) {
        printf("callocArr[%d] = %d (Guaranteed Zero)\\n", i, callocArr[i]);
    }

    free(callocArr);
    callocArr = NULL;

    return 0;
}""",
        "output": """=== Verification of calloc() Zero-Initialization ===
callocArr[0] = 0 (Guaranteed Zero)
callocArr[1] = 0 (Guaranteed Zero)
callocArr[2] = 0 (Guaranteed Zero)
callocArr[3] = 0 (Guaranteed Zero)
callocArr[4] = 0 (Guaranteed Zero)""",
        "explanation": "1. `calloc(5, sizeof(int))` requests 20 bytes and initializes every byte to `0x00`.\n2. All elements are guaranteed to read as `0` without manual zeroing loops.\n3. Memory is freed cleanly at the end.",
        "mistakes": [
            ("Assuming `calloc` sets floating-point numbers or pointers to zero on non-standard architectures.", "On rare non-IEEE systems, all-bits-zero might not represent `0.0` or `NULL`. On all standard modern systems, it works as expected."),
            ("Using `calloc` when immediately overwriting the entire buffer with new data.", "If you are going to immediately overwrite every element (e.g. reading from a file), the zeroing overhead of `calloc` is wasted; use `malloc` instead.")
        ],
        "practice_q": "How does `calloc(n, s)` compare with `malloc(n * s)` followed by `memset(ptr, 0, n * s)`?"
    },
    {
        "num": 90,
        "title": "The realloc() Function: Safe Buffer Resizing and Expansion",
        "category": "DMA Functions",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "Viva Trap", "High Yield Exam"],
        "question": "Explain `realloc()` in C. Describe how it resizes memory blocks (in-place expansion vs reallocation). Why is writing `ptr = realloc(ptr, new_size)` a dangerous anti-pattern?",
        "logic": "`realloc()` changes the size of an existing dynamically allocated block. It can expand or shrink the memory, preserving existing data up to the minimum of old and new sizes.",
        "concept": "1. Prototype: `void *realloc(void *ptr, size_t new_size);`\n2. Reallocation Scenarios:\n- Case A (In-Place): If contiguous free space is available immediately following the current block, `realloc` extends the block without changing its base address.\n- Case B (Relocate): If space behind the block is occupied, `realloc` allocates a new block elsewhere, copies the existing data, frees the old block, and returns the new pointer address.\n- Case C (Failure): If insufficient memory exists, `realloc` returns `NULL`. The original block remains intact in memory!\n3. The Dangerous Anti-Pattern:\nWriting `ptr = realloc(ptr, new_size);` is hazardous because if `realloc` fails and returns `NULL`, the original pointer is overwritten with `NULL`, losing the reference to the original block and creating an unrecoverable memory leak! Always use a temporary pointer.",
        "syntax": "void *temp = realloc(ptr, new_size);\nif (temp != NULL) ptr = temp;",
        "code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int initialSize = 3;
    int *arr = (int *)malloc(initialSize * sizeof(int));
    if (arr == NULL) return 1;

    for (int i = 0; i < initialSize; i++) arr[i] = (i + 1) * 10;

    printf("=== Initial Allocation (Size: %d) ===\\n", initialSize);
    printf("Initial Buffer Address: %p\\n", (void*)arr);
    for (int i = 0; i < initialSize; i++) printf("arr[%d] = %d\\n", i, arr[i]);

    /* Resizing to 6 elements safely */
    int newSize = 6;
    int *temp = (int *)realloc(arr, newSize * sizeof(int));

    if (temp == NULL) {
        printf("Reallocation failed! Original buffer is preserved.\\n");
        free(arr);
        return 1;
    }

    arr = temp; /* Safe: reassign only after successful allocation */
    printf("\\n=== After realloc() to Size: %d ===\\n", newSize);
    printf("New Buffer Address:     %p\\n", (void*)arr);

    /* Populate the new slots */
    for (int i = initialSize; i < newSize; i++) {
        arr[i] = (i + 1) * 10;
    }

    for (int i = 0; i < newSize; i++) printf("arr[%d] = %d\\n", i, arr[i]);

    free(arr);
    return 0;
}""",
        "output": """=== Initial Allocation (Size: 3) ===
Initial Buffer Address: 0x55d4a2b9a2a0
arr[0] = 10
arr[1] = 20
arr[2] = 30

=== After realloc() to Size: 6 ===
New Buffer Address:     0x55d4a2b9a2a0
arr[0] = 10
arr[1] = 20
arr[2] = 30
arr[3] = 40
arr[4] = 50
arr[5] = 60""",
        "explanation": "1. `arr` is initially allocated for 3 integers.\n2. `realloc(arr, 6 * sizeof(int))` successfully expands the buffer.\n3. Existing elements 10, 20, 30 are preserved intact.\n4. Using `temp` ensures the original memory is not lost if reallocation fails.",
        "mistakes": [
            ("Writing `arr = realloc(arr, new_size)` directly.", "If reallocation fails, `arr` becomes `NULL` while the old block remains allocated, causing a permanent memory leak."),
            ("Assuming newly allocated bytes from `realloc()` are zeroed.", "Newly expanded bytes contain uninitialized garbage values; initialize them explicitly.")
        ],
        "practice_q": "What happens if you pass `NULL` as the first argument to `realloc(NULL, size)`?"
    },
    {
        "num": 91,
        "title": "Dynamic 2D Arrays: Array of Pointers and Row-by-Row Deallocation",
        "category": "DMA Advanced",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Write a complete C program to allocate a 2D matrix of arbitrary dimensions (R x C) dynamically at runtime using an array of pointers (`int **`). Demonstrate proper row-by-row deallocation.",
        "logic": "Allocate an array of $R$ pointers (`int **matrix = malloc(R * sizeof(int *))`). Then iterate through each row and allocate $C$ integers for that row (`matrix[i] = malloc(C * sizeof(int))`). Deallocation must be performed in reverse order.",
        "concept": "1. Double Pointer Allocation Pattern:\n- Step 1: Allocate row pointer array: `int **matrix = malloc(R * sizeof(int *));`\n- Step 2: Allocate each row individually: `for(i=0; i<R; i++) matrix[i] = malloc(C * sizeof(int));`\n2. Access: Elements are accessed naturally using standard 2D notation: `matrix[i][j]`.\n3. Deallocation Order (Crucial):\n- Step 1: Free each individual row first: `for(i=0; i<R; i++) free(matrix[i]);`\n- Step 2: Free the row pointer array: `free(matrix);`\nIf you free `matrix` first, you lose the pointers to each row, creating $R$ unrecoverable memory leaks!",
        "syntax": "int **m = malloc(r * sizeof(int*)); for(i) m[i] = malloc(c * sizeof(int));",
        "code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int rows = 3, cols = 4;

    /* Step 1: Allocate array of row pointers */
    int **matrix = (int **)malloc(rows * sizeof(int *));
    if (matrix == NULL) return 1;

    /* Step 2: Allocate columns for each row */
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int *)malloc(cols * sizeof(int));
        if (matrix[i] == NULL) {
            /* Cleanup previously allocated rows on failure */
            for (int k = 0; k < i; k++) free(matrix[k]);
            free(matrix);
            return 1;
        }
    }

    /* Populate matrix */
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = (i + 1) * 10 + (j + 1);
        }
    }

    printf("=== Dynamic 2D Matrix (%dx%d) ===\\n", rows, cols);
    for (int i = 0; i < rows; i++) {
        printf("Row %d (%p): [ ", i, (void*)matrix[i]);
        for (int j = 0; j < cols; j++) {
            printf("%3d ", matrix[i][j]);
        }
        printf("]\\n");
    }

    /* Proper Deallocation in Reverse Order */
    for (int i = 0; i < rows; i++) {
        free(matrix[i]); /* Free individual row buffers */
    }
    free(matrix);        /* Free the pointer array */
    matrix = NULL;

    printf("\\nMatrix deallocated cleanly without memory leaks!\\n");
    return 0;
}""",
        "output": """=== Dynamic 2D Matrix (3x4) ===
Row 0 (0x55d4a2b9a2d0): [  11  12  13  14 ]
Row 1 (0x55d4a2b9a2f0): [  21  22  23  24 ]
Row 2 (0x55d4a2b9a310): [  31  32  33  34 ]

Matrix deallocated cleanly without memory leaks!""",
        "explanation": "1. `matrix` holds 3 pointers (`sizeof(int*) = 8` bytes each).\n2. Each `matrix[i]` holds 4 integers (`16` bytes each).\n3. Rows are freed first in a loop, followed by `free(matrix)`.",
        "mistakes": [
            ("Freeing `free(matrix)` before freeing the individual rows.", "Leaves all row allocations orphaned in the heap, causing serious memory leaks."),
            ("Assuming rows in an `int **` allocation are contiguous in memory.", "Individual rows are separate heap allocations and may not be contiguous. You cannot compute flat addresses like `Base + i*cols + j` on an `int**`.")
        ],
        "practice_q": "How can you allocate a dynamic 2D array as a single contiguous 1D block and access it using pointer-to-array syntax?"
    },
    {
        "num": 92,
        "title": "Memory Leaks: Root Causes, Consequences, and Detection Tools",
        "category": "Memory Safety",
        "difficulty": "Intermediate",
        "exam_tags": ["Viva Must-Know", "Security Critical"],
        "question": "What is a Memory Leak in C? What are its real-world consequences in long-running services? Detail how memory leaks occur and explain detection using Valgrind and AddressSanitizer.",
        "logic": "A memory leak occurs when dynamically allocated heap memory (`malloc`, `calloc`) is no longer referenced by any pointer in the program, but has not been returned to the OS via `free()`.",
        "concept": "1. Root Causes:\n- Reassigning a pointer before freeing its existing block (`p = malloc(10); p = malloc(20);` -> first 10 bytes leaked!).\n- Returning from a function without freeing local heap allocations.\n- Premature `return` or error exits bypassing cleanup code.\n2. Consequences:\n- In short scripts, the OS reclaims all memory when the process terminates.\n- In long-running processes (operating systems, web servers, databases, embedded devices), memory leaks slowly exhaust available RAM, leading to performance degradation, paging/swapping, and eventual Out-Of-Memory (OOM) crashes.\n3. Detection Tools:\n- Valgrind: `valgrind --leak-check=full ./program`\n- AddressSanitizer (ASan): `gcc -fsanitize=address -g program.c`.",
        "syntax": "gcc -fsanitize=address -g leak_test.c -o leak_test",
        "code": """#include <stdio.h>
#include <stdlib.h>

void intentionalLeak(void) {
    /* 1. Leaked Allocation: Pointer is local and not freed before return */
    int *leakPtr = (int *)malloc(100 * sizeof(int));
    if (leakPtr != NULL) leakPtr[0] = 42;
    /* Function returns without free(leakPtr) -> 400 bytes leaked! */
}

void cleanAllocation(void) {
    int *cleanPtr = (int *)malloc(100 * sizeof(int));
    if (cleanPtr != NULL) {
        cleanPtr[0] = 42;
        free(cleanPtr); /* Properly freed */
        cleanPtr = NULL;
    }
}

int main(void) {
    printf("=== Memory Leak Demonstration ===\\n");
    printf("Simulating clean function execution...\\n");
    cleanAllocation();
    printf("Clean allocation completed without memory leak.\\n");

    return 0;
}""",
        "output": """=== Memory Leak Demonstration ===
Simulating clean function execution...
Clean allocation completed without memory leak.""",
        "explanation": "1. In `intentionalLeak`, when the function exits, local variable `leakPtr` is popped from the stack, but the 400 heap bytes remain allocated with no remaining pointer to reference them.\n2. In `cleanAllocation`, `free(cleanPtr)` returns the block to the heap before the function exits.",
        "mistakes": [
            ("Assuming the compiler warns about memory leaks automatically.", "Standard compilers do not warn about missing `free()` calls. You must use static analysis tools or runtime sanitizers like Valgrind or ASan."),
            ("Thinking garbage collection exists in standard C.", "C has no automatic garbage collector. Memory management is entirely the programmer's responsibility.")
        ],
        "practice_q": "What is the single most common design pattern in C for ensuring cleanup before early function returns?"
    },
    {
        "num": 93,
        "title": "Dangling Pointers and Double Free Vulnerabilities",
        "category": "Memory Safety",
        "difficulty": "Intermediate",
        "exam_tags": ["Security Critical", "Viva Trap"],
        "question": "What is a Dangling Pointer? What is a Double Free error? Explain the security risks associated with them and provide the defensive programming idiom to eliminate both.",
        "logic": "A dangling pointer points to memory that has already been deallocated. A double free occurs when `free()` is called twice on the same memory address without re-allocation, corrupting heap metadata.",
        "concept": "1. Dangling Pointer:\n- Occurs when memory is freed via `free(ptr)`, but `ptr` still holds the old memory address.\n- Accessing `*ptr` reads invalid or reallocated memory.\n2. Double Free Error:\n- Calling `free(ptr)` twice on the same pointer corrupts the heap manager's free-list or bin metadata.\n- Attackers exploit double-free vulnerabilities to execute arbitrary code (Common Vulnerabilities and Exposures - CVEs).\n3. Defensive Pattern:\nIn standard C, `free(NULL)` is guaranteed to be a safe no-op. Therefore, immediately setting a pointer to `NULL` after freeing it neutralizes both problems:\n```c\nfree(ptr);\nptr = NULL; /* Neutralizes dangling pointer AND prevents double free */\n```",
        "syntax": "free(ptr); ptr = NULL;",
        "code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *ptr = (int *)malloc(sizeof(int));
    if (ptr == NULL) return 1;

    *ptr = 77;
    printf("Allocated Value: %d at %p\\n", *ptr, (void*)ptr);

    /* 1. Free the allocated memory */
    free(ptr);

    /* 2. Defensive Neutralization: Immediately assign NULL */
    ptr = NULL;

    printf("Pointer neutralized to: %p\\n", (void*)ptr);

    /* 3. Safe Double Free Proof: free(NULL) is guaranteed safe by ANSI C */
    free(ptr); /* Completely safe! Does nothing when ptr is NULL */
    printf("Second free(ptr) executed safely without crash because ptr was NULL!\\n");

    return 0;
}""",
        "output": """Allocated Value: 77 at 0x55d4a2b9a2a0
Pointer neutralized to: (nil)
Second free(ptr) executed safely without crash because ptr was NULL!""",
        "explanation": "1. Memory is freed, returning the block to the heap.\n2. `ptr = NULL` ensures `ptr` no longer points to the deallocated address.\n3. The second call `free(ptr)` evaluates to `free(NULL)`, which the C standard defines as a safe no-op.",
        "mistakes": [
            ("Accessing a pointer after calling `free(ptr)` without reassigning.", "Reading or writing through a dangling pointer causes undefined behavior, subtle memory corruption, or security vulnerabilities."),
            ("Assuming `free()` sets the pointer to NULL automatically.", "In C, parameters are passed by value. `free(ptr)` receives a copy of the pointer address, so it cannot modify the caller's pointer variable.")
        ],
        "practice_q": "How can you write a preprocessor macro `SAFE_FREE(ptr)` that frees a pointer and sets it to NULL in one step?"
    },
    {
        "num": 94,
        "title": "Self-Referential Structures: Foundation of Linked Lists and Trees",
        "category": "Data Structures Foundation",
        "difficulty": "Exam-Level",
        "exam_tags": ["Lab Program", "VTU Exam Favorite", "Core Concept"],
        "question": "What is a self-referential structure? Why can a structure contain a pointer to itself, but not an instance of itself by value? Implement a 3-node singly linked list in C.",
        "logic": "A self-referential structure contains a pointer member that points to another structure of the exact same type. This forms the foundation of dynamic data structures like Linked Lists, Trees, and Graphs.",
        "concept": "1. Why an instance by value is illegal:\n```c\nstruct BadNode { int val; struct BadNode next; }; /* ILLEGAL! Infinite size */\n```\nThe compiler cannot determine the memory size because it requires infinite recursion.\n2. Why a pointer member is legal:\n```c\nstruct Node { int val; struct Node *next; }; /* LEGAL! */\n```\nA pointer has a fixed, known size (8 bytes on 64-bit systems) regardless of the type it points to.\n3. Singly Linked List: Nodes are linked sequentially via their `next` pointers, terminating with `NULL`.",
        "syntax": "struct Node { int data; struct Node *next; };",
        "code": """#include <stdio.h>
#include <stdlib.h>

/* Self-Referential Structure Definition */
struct Node {
    int data;
    struct Node *next; /* Pointer to structure of same type */
};

/* Helper to create a new heap-allocated node */
struct Node *createNode(int value) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (newNode != NULL) {
        newNode->data = value;
        newNode->next = NULL;
    }
    return newNode;
}

int main(void) {
    /* Construct a 3-node singly linked list: 10 -> 20 -> 30 -> NULL */
    struct Node *head = createNode(10);
    head->next = createNode(20);
    head->next->next = createNode(30);

    printf("=== Singly Linked List Traversal ===\\n");
    struct Node *current = head;
    while (current != NULL) {
        printf("[Data: %d | Next: %p] -> ", current->data, (void*)current->next);
        current = current->next;
    }
    printf("NULL\\n\\n");

    /* Free all allocated nodes */
    current = head;
    while (current != NULL) {
        struct Node *temp = current->next;
        free(current);
        current = temp;
    }
    printf("All nodes freed successfully without memory leaks!\\n");

    return 0;
}""",
        "output": """=== Singly Linked List Traversal ===
[Data: 10 | Next: 0x55d4a2b9a2f0] -> [Data: 20 | Next: 0x55d4a2b9a310] -> [Data: 30 | Next: (nil)] -> NULL

All nodes freed successfully without memory leaks!""",
        "explanation": "1. `struct Node` contains an integer `data` and a self-referential pointer `next`.\n2. Three nodes are created on the heap and linked together.\n3. Traversal follows `current = current->next` until `current == NULL`.\n4. Nodes are freed in order using a temporary pointer to preserve the next address.",
        "mistakes": [
            ("Freeing `current` before saving `current->next`: `free(curr); curr = curr->next;`.", "Once `curr` is freed, accessing `curr->next` is a use-after-free bug. Always save `next` in a temporary variable first."),
            ("Missing the structure tag name when declaring the self-referential pointer.", "Inside the structure definition, the `typedef` alias is not yet available; you must use `struct Node *next`.")
        ],
        "practice_q": "How would you modify `struct Node` to create a Doubly Linked List?"
    },
    {
        "num": 95,
        "title": "Tagged Unions (Discriminated Unions) for Variant Data Types",
        "category": "Unions & Design",
        "difficulty": "Intermediate",
        "exam_tags": ["Design Pattern", "Viva Favorite"],
        "question": "What is a Tagged Union (or Discriminated Union)? How does combining an enumeration tag with a union provide type-safe access to variant data types in C?",
        "logic": "Since a raw union does not track which member is currently active, reading the wrong member causes data corruption. A tagged union wraps the union alongside an `enum` tag inside an enclosing structure, guaranteeing safe inspection.",
        "concept": "1. Pattern Structure:\n```c\ntypedef struct {\n    enum { TYPE_INT, TYPE_FLOAT, TYPE_STRING } type;\n    union {\n        int i;\n        double d;\n        char str[32];\n    } data;\n} Value;\n```\n2. Safety: Any function inspecting `Value` checks `val.type` via a `switch` statement before accessing `val.data`, ensuring type-safe access.\n3. Applications: JSON parsers, compiler Abstract Syntax Trees (AST nodes), database query results, and packet network protocols.",
        "syntax": "switch(val.type) { case TYPE_INT: printf(\"%d\", val.data.i); break; ... }",
        "code": """#include <stdio.h>
#include <string.h>

typedef enum {
    TYPE_INT,
    TYPE_FLOAT,
    TYPE_STRING
} DataTypeTag;

typedef struct {
    DataTypeTag tag;
    union {
        int iVal;
        double dVal;
        char sVal[32];
    } payload;
} VariantValue;

void printVariant(const VariantValue *v) {
    switch (v->tag) {
        case TYPE_INT:
            printf("Variant holds INTEGER: %d\\n", v->payload.iVal);
            break;
        case TYPE_FLOAT:
            printf("Variant holds DOUBLE:  %.4f\\n", v->payload.dVal);
            break;
        case TYPE_STRING:
            printf("Variant holds STRING:  \\\"%s\\\"\\n", v->payload.sVal);
            break;
    }
}

int main(void) {
    VariantValue v1, v2, v3;

    v1.tag = TYPE_INT;
    v1.payload.iVal = 1024;

    v2.tag = TYPE_FLOAT;
    v2.payload.dVal = 3.14159;

    v3.tag = TYPE_STRING;
    strcpy(v3.payload.sVal, "VTU Engineering");

    printf("=== Tagged Union Type-Safe Access ===\\n");
    printVariant(&v1);
    printVariant(&v2);
    printVariant(&v3);

    return 0;
}""",
        "output": """=== Tagged Union Type-Safe Access ===
Variant holds INTEGER: 1024
Variant holds DOUBLE:  3.14159
Variant holds STRING:  "VTU Engineering" """,
        "explanation": "1. `VariantValue` wraps a union payload with a discriminator tag `DataTypeTag`.\n2. `printVariant` safely checks `v->tag` before reading the payload.\n3. This implements type safety on top of C's raw memory unions.",
        "mistakes": [
            ("Updating `payload` without updating `tag`.", "If you assign `payload.dVal` but forget to update `tag = TYPE_FLOAT`, the program will read the double as an integer, producing garbage values."),
            ("Assuming union members are isolated.", "Writing to `payload.sVal` overwrites any prior integer or float values in the union.")
        ],
        "practice_q": "How does C++ `std::variant` implement the tagged union pattern modernly?"
    },
    {
        "num": 96,
        "title": "Bit-Fields in Structures: Packing Hardware Flags into Minimal Bits",
        "category": "Structures & Hardware",
        "difficulty": "Intermediate",
        "exam_tags": ["Embedded Systems", "Exam Question"],
        "question": "What are Bit-Fields in C structures? How do they allow programmers to allocate specific bit widths for members? Write a program packing hardware control flags into a single byte.",
        "logic": "Bit-fields allow integer structure members to be declared with explicit bit widths using colon notation (`unsigned int flag : 1;`), enabling precise memory packing for hardware registers and network packet headers.",
        "concept": "1. Syntax: `type member_name : bit_width;`\n- Typically declared with `unsigned int`, `signed int`, or `_Bool`.\n- Example: `unsigned int isRunning : 1;` occupies exactly 1 bit (values: 0 or 1).\n- `unsigned int priority : 3;` occupies 3 bits (values: 0 to 7).\n2. Hardware Mapping: A single 8-bit unsigned char or 32-bit int can hold multiple flags.\n3. Address Limitation: You CANNOT take the memory address of a bit-field member using `&` (`&flags.isRunning` causes a compile error) because CPUs address memory by bytes, not individual bits.",
        "syntax": "struct Register { unsigned int read : 1; unsigned int write : 1; unsigned int mode : 2; };",
        "code": """#include <stdio.h>

/* Normal structure without bit-fields: 4 * 4 = 16 bytes */
struct NormalFlags {
    unsigned int isPowerOn;
    unsigned int isConnected;
    unsigned int isOverheated;
    unsigned int operationMode; /* 0 to 7 */
};

/* Packed structure with bit-fields: All fit in a single 32-bit word! */
struct BitFieldFlags {
    unsigned int isPowerOn     : 1; /* 1 bit (0 or 1) */
    unsigned int isConnected   : 1; /* 1 bit */
    unsigned int isOverheated  : 1; /* 1 bit */
    unsigned int operationMode : 3; /* 3 bits (0 to 7) */
};

int main(void) {
    printf("=== Bit-Fields Memory Footprint Comparison ===\\n");
    printf("sizeof(struct NormalFlags):   %zu bytes\\n", sizeof(struct NormalFlags));
    printf("sizeof(struct BitFieldFlags): %zu bytes (Packed into a single 4-byte word!)\\n\\n", 
           sizeof(struct BitFieldFlags));

    struct BitFieldFlags device;
    device.isPowerOn = 1;
    device.isConnected = 1;
    device.isOverheated = 0;
    device.operationMode = 5; /* 3-bit binary: 101 */

    printf("Device Status:\\n");
    printf("  Power:     %s\\n", device.isPowerOn ? "ON" : "OFF");
    printf("  Network:   %s\\n", device.isConnected ? "CONNECTED" : "OFFLINE");
    printf("  Thermal:   %s\\n", device.isOverheated ? "OVERHEAT ALERT" : "NORMAL");
    printf("  Mode Code: %u (Binary: 101)\\n", device.operationMode);

    return 0;
}""",
        "output": """=== Bit-Fields Memory Footprint Comparison ===
sizeof(struct NormalFlags):   16 bytes
sizeof(struct BitFieldFlags): 4 bytes (Packed into a single 4-byte word!)

Device Status:
  Power:     ON
  Network:   CONNECTED
  Thermal:   NORMAL
  Mode Code: 5 (Binary: 101)""",
        "explanation": "1. `NormalFlags` uses 16 bytes (4 separate 4-byte integers).\n2. `BitFieldFlags` uses bit-fields totaling $1 + 1 + 1 + 3 = 6$ bits, packing everything into a single 4-byte allocation.\n3. Useful for embedded systems and network protocol header parsing.",
        "mistakes": [
            ("Attempting to take the address of a bit-field: `&device.isPowerOn`.", "Compile error: `cannot take address of bit-field`. Bit-fields do not have individual byte addresses."),
            ("Assigning a value exceeding the bit capacity (e.g. assigning 10 to a 3-bit field).", "A 3-bit unsigned field can only hold values from 0 to 7. Assigning 10 truncates to $10 \\% 8 = 2$ silently.")
        ],
        "practice_q": "What happens if the sum of bit widths exceeds 32 bits in an `unsigned int` bit-field?"
    },
    {
        "num": 97,
        "title": "Structure Copy Assignment and Designated Initializers",
        "category": "Structures",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Question", "Viva Favorite"],
        "question": "Can two structure variables of the same type be directly assigned using `=`? Explain structure assignment (`s1 = s2`) and demonstrate C99 Designated Initializers.",
        "logic": "In C, structure variables of the same type CAN be directly copied using the assignment operator `=`. The compiler performs a bitwise copy (shallow copy) of all members.",
        "concept": "1. Direct Structure Assignment: `struct Point p2 = p1;` copies all bytes of `p1` into `p2`.\n- Note: Arrays inside structures ARE copied automatically during structure assignment!\n- Limitation: If a structure contains pointers, the pointer address is copied (shallow copy), not the memory pointed to.\n2. C99 Designated Initializers: Allows initializing members explicitly by name in any order: `struct Point p = {.y = 20, .x = 10};`.\n- Unspecified members are automatically initialized to zero.",
        "syntax": "struct Point p = {.x = 10, .y = 20};\nstruct Point p2 = p; /* Direct bitwise copy */",
        "code": """#include <stdio.h>

struct Vector3D {
    double x;
    double y;
    double z;
};

int main(void) {
    /* 1. C99 Designated Initializer (Named member initialization in arbitrary order) */
    struct Vector3D v1 = {
        .z = 9.81,
        .x = 3.50,
        .y = 4.25
    };

    printf("=== C99 Designated Initializers ===\\n");
    printf("v1: (x=%.2f, y=%.2f, z=%.2f)\\n\\n", v1.x, v1.y, v1.z);

    /* 2. Direct Structure Assignment: Complete bitwise copy */
    struct Vector3D v2;
    v2 = v1; /* Valid: copies all 24 bytes in one operation */

    printf("=== Direct Structure Assignment (v2 = v1) ===\\n");
    printf("v2: (x=%.2f, y=%.2f, z=%.2f)\\n", v2.x, v2.y, v2.z);

    /* Modify v2 to prove independent storage */
    v2.x = 99.0;
    printf("After modifying v2.x = 99.0:\\n");
    printf("v1.x: %.2f (Unaltered)\\n", v1.x);
    printf("v2.x: %.2f (Modified)\\n", v2.x);

    return 0;
}""",
        "output": """=== C99 Designated Initializers ===
v1: (x=3.50, y=4.25, z=9.81)

=== Direct Structure Assignment (v2 = v1) ===
v2: (x=3.50, y=4.25, z=9.81)
After modifying v2.x = 99.0:
v1.x: 3.50 (Unaltered)
v2.x: 99.00 (Modified)""",
        "explanation": "1. Designated initializers allow setting `.z`, `.x`, `.y` out of order without ambiguity.\n2. `v2 = v1` performs a bitwise copy of all 24 bytes from `v1` into `v2`.\n3. Modifying `v2.x` does not affect `v1.x`, confirming independent storage.",
        "mistakes": [
            ("Comparing two structures directly with `==`: `if (s1 == s2)`.", "Direct equality comparison `==` on structures is ILLEGAL in C because unused padding bytes contain random values. Compare members individually or use `memcmp()`."),
            ("Assuming structure assignment performs a deep copy of dynamic heap buffers.", "If a structure member is a heap pointer (`char *name`), `s2 = s1` copies only the pointer address, so both structures share the same heap memory.")
        ],
        "practice_q": "Why did the ANSI C committee allow structure assignment `=` but forbid structure comparison `==`?"
    },
    {
        "num": 98,
        "title": "Dynamic Array Resizing: Implementing a Vector Growth Pattern",
        "category": "DMA Patterns",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "Data Structures"],
        "question": "Implement a dynamically growing array (similar to C++ std::vector) in C. Show how to use `realloc()` to double capacity whenever the buffer becomes full.",
        "logic": "Start with an initial capacity (e.g. 2). When element count reaches capacity, double the capacity using `realloc()` (`new_capacity = capacity * 2`). This achieves amortized $O(1)$ append time.",
        "concept": "1. Vector Structure:\n```c\ntypedef struct {\n    int *data;\n    size_t size;\n    size_t capacity;\n} DynamicArray;\n```\n2. Growth Strategy: Doubling capacity ensures that appending $N$ items requires only $O(N)$ total reallocation operations, resulting in amortized $O(1)$ time per append.\n3. Memory Safety: Free the underlying dynamic buffer when finished.",
        "syntax": "new_cap = cap * 2; temp = realloc(arr, new_cap * sizeof(int));",
        "code": """#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *items;
    size_t size;
    size_t capacity;
} IntVector;

IntVector createVector(size_t initialCapacity) {
    IntVector vec;
    vec.size = 0;
    vec.capacity = initialCapacity > 0 ? initialCapacity : 2;
    vec.items = (int *)malloc(vec.capacity * sizeof(int));
    return vec;
}

void vectorPush(IntVector *vec, int value) {
    if (vec->size >= vec->capacity) {
        /* Double capacity when full */
        size_t newCap = vec->capacity * 2;
        int *temp = (int *)realloc(vec->items, newCap * sizeof(int));
        if (temp == NULL) {
            fprintf(stderr, "Vector expansion failed!\\n");
            return;
        }
        vec->items = temp;
        vec->capacity = newCap;
        printf("  [Vector expanded to capacity %zu]\\n", vec->capacity);
    }
    vec->items[vec->size++] = value;
}

void freeVector(IntVector *vec) {
    free(vec->items);
    vec->items = NULL;
    vec->size = 0;
    vec->capacity = 0;
}

int main(void) {
    IntVector v = createVector(2);

    printf("=== Dynamic Vector Growth Demonstration ===\\n");
    for (int i = 1; i <= 6; i++) {
        printf("Appending %d: ", i * 10);
        vectorPush(&v, i * 10);
        printf("Size: %zu / Capacity: %zu\\n", v.size, v.capacity);
    }

    printf("\\nFinal Vector Contents: ");
    for (size_t i = 0; i < v.size; i++) printf("%d ", v.items[i]);
    printf("\\n");

    freeVector(&v);
    return 0;
}""",
        "output": """=== Dynamic Vector Growth Demonstration ===
Appending 10: Size: 1 / Capacity: 2
Appending 20: Size: 2 / Capacity: 2
Appending 30:   [Vector expanded to capacity 4]
Size: 3 / Capacity: 4
Appending 40: Size: 4 / Capacity: 4
Appending 50:   [Vector expanded to capacity 8]
Size: 5 / Capacity: 8
Appending 60: Size: 6 / Capacity: 8

Final Vector Contents: 10 20 30 40 50 60 """,
        "explanation": "1. Vector starts with capacity 2.\n2. When appending 30, it doubles to 4.\n3. When appending 50, it doubles to 8.\n4. Amortized append cost is $O(1)$. Memory is cleanly released at the end.",
        "mistakes": [
            ("Incrementing capacity by only 1 in `realloc()` (`capacity + 1`).", "Reallocating on every single append results in $O(N^2)$ time complexity. Exponential growth (doubling) is required for amortized $O(1)$ performance."),
            ("Forgetting to update `vec->capacity` after reallocation.", "Failing to update capacity leads to premature reallocations or out-of-bounds writes.")
        ],
        "practice_q": "What is the amortized time complexity of inserting N elements into a vector with a doubling growth strategy?"
    },
    {
        "num": 99,
        "title": "Anonymous Structures and Unions in Modern C (C11 Feature)",
        "category": "Modern C Features",
        "difficulty": "Intermediate",
        "exam_tags": ["Modern C", "Viva Question"],
        "question": "What are anonymous structures and anonymous unions in C11? How do they eliminate redundant member name qualification in nested types?",
        "logic": "An anonymous structure or union is an unnamed member within an enclosing structure or union. Its members are accessed directly as if they were declared in the outer structure.",
        "concept": "1. Traditional Nested Access:\n```c\nstruct Outer { struct { int x, y; } point; };\nobj.point.x = 10; /* Requires .point qualification */\n```\n2. C11 Anonymous Structure:\n```c\nstruct Outer { struct { int x, y; }; };\nobj.x = 10; /* Direct access without intermediate name! */\n```\n3. Benefits: Common in 2D/3D math libraries (vector components accessible as both `.x, .y` and `.arr[0], .arr[1]` via anonymous unions) and hardware register definitions.",
        "syntax": "struct Vector { union { struct { float x, y, z; }; float raw[3]; }; };",
        "code": """#include <stdio.h>

/* C11 Anonymous Union & Structure */
typedef struct {
    union {
        /* Anonymous Structure 1: Named coordinates */
        struct {
            double x;
            double y;
            double z;
        };
        /* Anonymous Structure 2: Alternative color names */
        struct {
            double r;
            double g;
            double b;
        };
        /* Raw array view of the same memory */
        double data[3];
    };
} Vec3;

int main(void) {
    Vec3 point;

    /* Direct access without intermediate member names */
    point.x = 1.0;
    point.y = 2.0;
    point.z = 3.0;

    printf("=== C11 Anonymous Member Access ===\\n");
    printf("Access via Coordinates: (x=%.1f, y=%.1f, z=%.1f)\\n", 
           point.x, point.y, point.z);
    printf("Access via Colors:      (r=%.1f, g=%.1f, b=%.1f)\\n", 
           point.r, point.g, point.b);
    printf("Access via Raw Array:   [%.1f, %.1f, %.1f]\\n", 
           point.data[0], point.data[1], point.data[2]);

    return 0;
}""",
        "output": """=== C11 Anonymous Member Access ===
Access via Coordinates: (x=1.0, y=2.0, z=3.0)
Access via Colors:      (r=1.0, g=2.0, b=3.0)
Access via Raw Array:   [1.0, 2.0, 3.0]""",
        "explanation": "1. `point.x`, `point.r`, and `point.data[0]` all refer to the exact same 8-byte memory location.\n2. Anonymous members remove boilerplate qualification while allowing multiple views of the same data.",
        "mistakes": [
            ("Using anonymous members when compiling with older `-std=c89` or `-std=c99` flags.", "Anonymous structures/unions were standardized in ISO C11. Use `-std=c11` or `-std=c17` in GCC/Clang."),
            ("Name collisions between anonymous members.", "All members inside anonymous structures must have unique names within the enclosing scope.")
        ],
        "practice_q": "How do graphics engines use anonymous unions to represent 4D vectors and colors simultaneously?"
    },
    {
        "num": 100,
        "title": "Alignment Control in C11: alignof, alignas, and aligned_alloc()",
        "category": "Memory & Performance",
        "difficulty": "Exam-Level",
        "exam_tags": ["Modern C", "Advanced Concept"],
        "question": "Explain memory alignment specifications in C11 using `<stdalign.h>`. How do `alignof`, `alignas`, and `aligned_alloc()` enable high-performance SIMD data structures?",
        "logic": "SIMD (Single Instruction Multiple Data) vector instructions (AVX, NEON) require memory buffers to be aligned to 16, 32, or 64-byte boundaries. C11 introduced standardized alignment controls.",
        "concept": "1. `alignof(type)`: Returns the alignment requirement of a type in bytes.\n2. `alignas(N)`: Forces a variable or structure member to be aligned to an $N$-byte boundary.\n3. `aligned_alloc(alignment, size)`: Allocates dynamically from the heap with the specified alignment boundary.\n- `alignment` must be a valid power of 2 supported by the implementation.\n- `size` must be an integral multiple of `alignment`.",
        "syntax": "#include <stdalign.h>\nalignas(64) float buffer[16];",
        "code": """#include <stdio.h>
#include <stdalign.h>
#include <stdint.h>

/* Normal structure */
struct DefaultAlign {
    double d;
};

/* Forced 64-byte cache-line aligned structure */
struct alignas(64) CacheAligned {
    double d;
};

int main(void) {
    printf("=== C11 Memory Alignment Inspection ===\\n");
    printf("alignof(char):               %zu byte\\n", alignof(char));
    printf("alignof(int):                %zu bytes\\n", alignof(int));
    printf("alignof(double):             %zu bytes\\n", alignof(double));
    printf("alignof(struct DefaultAlign):%zu bytes\\n", alignof(struct DefaultAlign));
    printf("alignof(struct CacheAligned):%zu bytes (Forces 64-byte cache alignment)\\n\\n", 
           alignof(struct CacheAligned));

    struct CacheAligned obj;
    printf("Address of obj: %p\\n", (void*)&obj);
    printf("Is address divisible by 64? %s\\n", 
           ((uintptr_t)&obj % 64 == 0) ? "YES (Aligned!)" : "NO");

    return 0;
}""",
        "output": """=== C11 Memory Alignment Inspection ===
alignof(char):               1 byte
alignof(int):                4 bytes
alignof(double):             8 bytes
alignof(struct DefaultAlign):8 bytes
alignof(struct CacheAligned):64 bytes (Forces 64-byte cache alignment)

Address of obj: 0x7ffd5a68ac40
Is address divisible by 64? YES (Aligned!)""",
        "explanation": "1. `alignof` reveals natural hardware alignment boundaries.\n2. `alignas(64)` forces `obj` to align to a 64-byte boundary, matching CPU L1 cache line sizes.\n3. Address `0x...c40` modulo 64 is 0, confirming alignment.",
        "mistakes": [
            ("Specifying an alignment that is not a power of 2 (e.g. `alignas(10)`).", "Alignments must strictly be powers of 2 (1, 2, 4, 8, 16, 32, 64...)."),
            ("Passing a size to `aligned_alloc()` that is not a multiple of alignment.", "In C11, `size` must be an exact multiple of `alignment`; otherwise, `aligned_alloc` returns `NULL`.")
        ],
        "practice_q": "Why does memory alignment to 64 bytes prevent false sharing in multithreaded programming?"
    },
    {
        "num": 101,
        "title": "Comprehensive Pointer Taxonomy: Null, Wild, Dangling, and Void Pointers",
        "category": "Pointers Mastery",
        "difficulty": "Fundamental",
        "exam_tags": ["Viva Must-Know", "Core Foundation"],
        "question": "Provide a complete taxonomic comparison of the four special pointer states in C: Null Pointer, Wild Pointer, Dangling Pointer, and Void (Generic) Pointer. Detail their definitions, causes, hazards, and mitigation.",
        "logic": "Understanding the distinct states of pointers is essential for memory safety and debugging in C.",
        "concept": "Comparison Taxonomy:\n1. Null Pointer:\n- Definition: Explicitly points to address 0 (`NULL`).\n- Hazard: Dereferencing causes an immediate, clean crash (SIGSEGV).\n- Mitigation: Intentionally used as a safe sentinel value.\n2. Wild Pointer:\n- Definition: An uninitialized pointer variable containing random stack garbage.\n- Hazard: Can overwrite random memory without crashing immediately, causing silent corruption.\n- Mitigation: Always initialize on declaration (`int *p = NULL;`).\n3. Dangling Pointer:\n- Definition: Points to memory that has been deallocated (via `free()` or function return).\n- Hazard: Reading/writing to reallocated memory causes undefined behavior and security exploits.\n- Mitigation: Assign `ptr = NULL;` immediately after `free(ptr)`.\n4. Void Pointer (`void *`):\n- Definition: A generic pointer with no associated data type.\n- Hazard: Cannot be dereferenced or used in arithmetic without an explicit typecast.\n- Purpose: Foundation of generic libraries and dynamic memory allocation.",
        "syntax": "Taxonomy: NULL vs Wild vs Dangling vs Void*",
        "code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    /* 1. Null Pointer */
    int *nullPtr = NULL;

    /* 2. Void (Generic) Pointer */
    int target = 42;
    void *voidPtr = &target;
    printf("Void Pointer dereferenced via cast: %d\\n", *(int *)voidPtr);

    /* 3. Dangling Pointer Neutralization */
    int *dynamicPtr = (int *)malloc(sizeof(int));
    if (dynamicPtr != NULL) {
        *dynamicPtr = 100;
        free(dynamicPtr);
        dynamicPtr = NULL; /* Neutralized: No longer dangling! */
    }

    /* 4. Defensive check prevents crashing on NULL */
    if (nullPtr == NULL && dynamicPtr == NULL) {
        printf("All pointers safely initialized and neutralized to NULL!\\n");
    }

    return 0;
}""",
        "output": """Void Pointer dereferenced via cast: 42
All pointers safely initialized and neutralized to NULL!""",
        "explanation": "1. `nullPtr` is initialized to `NULL`.\n2. `voidPtr` stores the address of `target` and is dereferenced via an explicit cast `*(int *)`.\n3. `dynamicPtr` is freed and immediately set to `NULL`, preventing it from becoming a dangling pointer.",
        "mistakes": [
            ("Treating Wild Pointers and Dangling Pointers as identical.", "A wild pointer was never initialized; a dangling pointer once pointed to valid memory that has since been deallocated."),
            ("Assuming `if (ptr)` protects against wild or dangling pointers.", "`if (ptr)` only checks if `ptr != 0`. Wild and dangling pointers contain non-zero addresses, so they pass the test and crash on dereference.")
        ],
        "practice_q": "What is the difference between `NULL`, `'\\0'`, and `0` in C?"
    },
    {
        "num": 102,
        "title": "Output Prediction & Debugging: Memory Leaks and Dangling Pointer Tracing",
        "category": "Debugging & Tracing",
        "difficulty": "Exam-Level",
        "exam_tags": ["Interview Trap", "Bug Hunting"],
        "question": "Trace and diagnose the three critical memory management defects in the following code snippet: (1) Leaked allocation, (2) Use-after-free, and (3) Double free.",
        "logic": "Traces common memory lifecycle bugs and demonstrates their corrected, safe implementations.",
        "concept": "Bug Identification:\n1. Memory Leak: Allocating a new block and overwriting the pointer without freeing the previous block.\n2. Use-After-Free: Reading from or writing to a pointer after `free()` has been called on it.\n3. Double Free: Calling `free()` twice on the same pointer without an intervening allocation, corrupting heap metadata.",
        "syntax": "free(p); p = NULL;",
        "code": """#include <stdio.h>
#include <stdlib.h>

void safeLifecycleDemonstration(void) {
    /* Safe Lifecycle without leaks or double frees */
    int *p1 = (int *)malloc(sizeof(int));
    if (p1 == NULL) return;
    *p1 = 10;
    printf("p1 allocated: %d\\n", *p1);

    /* Clean deallocation */
    free(p1);
    p1 = NULL; /* Prevents dangling access and double free */

    /* Second allocation */
    p1 = (int *)malloc(sizeof(int));
    if (p1 == NULL) return;
    *p1 = 20;
    printf("p1 re-allocated: %d\\n", *p1);

    free(p1);
    p1 = NULL;
}

int main(void) {
    printf("=== Memory Lifecycle Diagnostics ===\\n");
    safeLifecycleDemonstration();
    printf("Diagnostic completed cleanly with zero defects!\\n");
    return 0;
}""",
        "output": """=== Memory Lifecycle Diagnostics ===
p1 allocated: 10
p1 re-allocated: 20
Diagnostic completed cleanly with zero defects!""",
        "explanation": "1. The program demonstrates the complete lifecycle of heap allocations.\n2. Setting `p1 = NULL` after every `free()` eliminates both dangling pointer access and double free vulnerabilities.\n3. The pointer is safely reused for a second allocation without leaking the first.",
        "mistakes": [
            ("Writing `p = malloc(10); p = malloc(20);`.", "The first 10 bytes are permanently leaked because the pointer holding their address was overwritten before calling `free()`."),
            ("Accessing `*p` after `free(p)`.", "This is a Use-After-Free bug. The heap manager may have already reassigned that memory block to another part of the program.")
        ],
        "practice_q": "What is a memory arena and how does it prevent individual memory leaks?"
    },
    {
        "num": 103,
        "title": "Output Prediction: Structure Size with Bit-Fields and Alignment Padding",
        "category": "Debugging & Tracing",
        "difficulty": "Exam-Level",
        "exam_tags": ["Interview Trap", "Viva Favorite"],
        "question": "Predict the exact value of `sizeof(struct Test)` on a 64-bit system: `struct Test { char a; int b : 5; int c : 11; double d; };`. Explain the step-by-step memory layout calculation.",
        "logic": "The compiler packs bit-fields `b` (5 bits) and `c` (11 bits) into a shared 4-byte `int` allocation (16 bits total). Member `d` (8 bytes) requires 8-byte alignment, forcing padding before and after.",
        "concept": "Step-by-Step Memory Layout Calculation:\n1. `char a`: Offset 0, size 1 byte.\n2. Padding: 3 padding bytes inserted (offsets 1-3) to align `int` bit-fields to a 4-byte boundary.\n3. `int b:5` + `int c:11`: Total 16 bits $\\le$ 32 bits. Both fit inside a single 4-byte `int` at offsets 4-7.\n4. `double d`: Requires 8-byte alignment. Offset 8 is divisible by 8, so `d` occupies offsets 8-15 (8 bytes).\n5. Total size: 16 bytes. Since 16 is divisible by the largest alignment (8 for `double`), no trailing padding is needed.\nResult: `sizeof(struct Test) = 16` bytes.",
        "syntax": "sizeof(struct Test) calculation with alignment",
        "code": """#include <stdio.h>

struct Test {
    char a;         /* 1 byte + 3 padding bytes */
    int b : 5;      /* 5 bits  \\_ packed into one 4-byte int */
    int c : 11;     /* 11 bits /                             */
    double d;       /* 8 bytes */
};

int main(void) {
    printf("=== Step-by-Step Sizeof Prediction ===\\n");
    printf("sizeof(struct Test): %zu bytes\\n", sizeof(struct Test));

    printf("\\nMemory Map Breakdown:\\n");
    printf("  [0..0]:  char a (1 byte)\\n");
    printf("  [1..3]:  Alignment padding (3 bytes)\\n");
    printf("  [4..7]:  int b:5 & c:11 packed (4 bytes)\\n");
    printf("  [8..15]: double d (8 bytes)\\n");
    printf("  Total:   16 bytes (Aligned to 8-byte boundary)\\n");

    return 0;
}""",
        "output": """=== Step-by-Step Sizeof Prediction ===
sizeof(struct Test): 16 bytes

Memory Map Breakdown:
  [0..0]:  char a (1 byte)
  [1..3]:  Alignment padding (3 bytes)
  [4..7]:  int b:5 & c:11 packed (4 bytes)
  [8..15]: double d (8 bytes)
  Total:   16 bytes (Aligned to 8-byte boundary)""",
        "explanation": "1. `b` and `c` share a single 4-byte allocation (16 bits used out of 32).\n2. `double d` aligns cleanly at offset 8.\n3. Total structure size is verified as 16 bytes.",
        "mistakes": [
            ("Counting individual bit widths without checking storage units.", "Bit-fields are packed into their underlying type (`int`), which occupies at least 4 bytes in memory."),
            ("Forgetting alignment padding before 8-byte `double`.", "If padding is omitted from calculation, the computed size will be incorrect.")
        ],
        "practice_q": "What would `sizeof(struct Test)` be if `char a` was moved after `double d`?"
    },
    {
        "num": 104,
        "title": "Module 4 Mastery: Comprehensive Structures & DMA Diagnostic Review",
        "category": "Comprehensive Review",
        "difficulty": "Exam-Level",
        "exam_tags": ["Viva Must-Know", "Final Exam Checklist"],
        "question": "Provide a high-yield diagnostic checklist of the top 7 most critical examination rules for Structures, Unions, and Dynamic Memory Allocation.",
        "logic": "Summarizes the essential principles of Module 4 into a quick-reference study guide for exams and viva voce.",
        "concept": "Top 7 Module 4 Rules:\n1. Structure dot vs arrow: Use `.` on variables (`s.x`), use `->` on pointers (`ptr->x`).\n2. Alignment padding: `sizeof(struct)` is often larger than the sum of member sizes.\n3. Unions share memory: Size equals largest member; writing one member overwrites others.\n4. Always check `malloc() == NULL`: Verify allocation succeeded before dereferencing.\n5. Match every `malloc()` with `free()`: Prevent memory leaks.\n6. Neutralize dangling pointers: Always set `ptr = NULL;` immediately after `free(ptr)`.\n7. Deallocate dynamic 2D arrays in reverse order: Free rows first, then free the row pointer array.",
        "syntax": "Diagnostic Checklist: struct, union, malloc, calloc, realloc, free",
        "code": """#include <stdio.h>

int main(void) {
    printf("=== Module 4 Final Exam Diagnostic Checklist ===\\n");
    printf("1. Use '.' on structure variables; use '->' on structure pointers\\n");
    printf("2. Structure size includes alignment padding; pack with #pragma pack if needed\\n");
    printf("3. Union members share memory; size equals largest member\\n");
    printf("4. ALWAYS check if malloc() / calloc() / realloc() returned NULL\\n");
    printf("5. realloc(ptr, size) anti-pattern: Use temp pointer to prevent leaks on failure\\n");
    printf("6. Always set ptr = NULL after free(ptr) to prevent dangling & double frees\\n");
    printf("7. Dynamic 2D arrays: Free individual rows FIRST, then free the pointer array\\n");

    return 0;
}""",
        "output": """=== Module 4 Final Exam Diagnostic Checklist ===
1. Use '.' on structure variables; use '->' on structure pointers
2. Structure size includes alignment padding; pack with #pragma pack if needed
3. Union members share memory; size equals largest member
4. ALWAYS check if malloc() / calloc() / realloc() returned NULL
5. realloc(ptr, size) anti-pattern: Use temp pointer to prevent leaks on failure
6. Always set ptr = NULL after free(ptr) to prevent dangling & double frees
7. Dynamic 2D arrays: Free individual rows FIRST, then free the pointer array""",
        "explanation": "1. These 7 rules cover the most common exam questions and lab practical issues in Module 4.\n2. Reviewing this checklist helps ensure robust memory management and clean structure usage.",
        "mistakes": [
            ("Neglecting to free dynamically allocated memory before program exit.", "While modern desktop operating systems reclaim memory upon process termination, embedded systems and long-running services do not."),
            ("Assuming `sizeof(union)` is always the size of the first member.", "It is the size of the LARGEST member, rounded up to the union's alignment requirement.")
        ],
        "practice_q": "What is the difference between shallow copy and deep copy when copying structures containing pointers?"
    }
]


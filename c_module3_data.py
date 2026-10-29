# -*- coding: utf-8 -*-
"""
C Programming - Module 3: Functions, Pointers, and Recursion
Questions 53 to 78 (Functions, Storage Classes, Pointers, Pointer Arithmetic, Recursion, and Tower of Hanoi)
"""

C_MODULE3_QUESTIONS = [
    {
        "num": 53,
        "title": "Modular Programming: Function Prototypes, Definitions, and Calls",
        "category": "Functions",
        "difficulty": "Fundamental",
        "exam_tags": ["Core Concept", "Viva Must-Know"],
        "question": "What is modular programming? Differentiate between a function prototype (declaration), definition, and call. Why are function prototypes strongly recommended in C?",
        "logic": "Modular programming decomposes a large program into smaller, reusable, independently verifiable functional units. A prototype informs the compiler of a function's name, return type, and parameter list before its definition.",
        "concept": "1. Function Prototype: `return_type function_name(param_type1, param_type2);`\n- Allows calling functions defined later in the file or in external translation units.\n- Enables compile-time argument type checking and implicit type promotions.\n2. Function Definition: Contains the actual code implementation inside braces `{ ... }`.\n3. Function Call: Transmits actual arguments, transfers CPU execution to the function, and receives the return value upon completion.\n4. If a prototype is omitted in legacy C, the compiler assumes an implicit return type of `int`, causing severe bugs if the function actually returns `float`, `double`, or a pointer.",
        "syntax": "double computeHypotenuse(double a, double b); /* Prototype */\nresult = computeHypotenuse(3.0, 4.0);         /* Call */",
        "code": """#include <stdio.h>
#include <math.h>

/* Function Prototype */
double computeHypotenuse(double sideA, double sideB);

int main(void) {
    double a = 3.0, b = 4.0;

    /* Function Call */
    double c = computeHypotenuse(a, b);

    printf("Right Triangle Sides: a = %.2f, b = %.2f\\n", a, b);
    printf("Computed Hypotenuse: c = %.2f\\n", c);

    return 0;
}

/* Function Definition */
double computeHypotenuse(double sideA, double sideB) {
    return sqrt(sideA * sideA + sideB * sideB);
}""",
        "output": """Right Triangle Sides: a = 3.00, b = 4.00
Computed Hypotenuse: c = 5.00""",
        "explanation": "1. Prototype at line 5 informs `main()` that `computeHypotenuse` accepts two `double` arguments and returns a `double`.\n2. When `main()` executes the call, arguments `3.0` and `4.0` are pushed to the stack/registers.\n3. `sqrt(9 + 16) = sqrt(25) = 5.0` is computed and returned to `c`.",
        "mistakes": [
            ("Placing a semicolon after the function definition header: `double calc(double x); { ... }`.", "This breaks compilation because the semicolon turns the definition into an isolated declaration, leaving the following `{ ... }` block detached."),
            ("Assuming `void func()` in C means 'takes no arguments'.", "In C, `void func()` means 'takes an unspecified number of arguments'! To specify zero arguments, you must explicitly declare `void func(void)`.")
        ],
        "practice_q": "What happens if the data type of an argument passed to a function does not match the prototype declaration?"
    },
    {
        "num": 54,
        "title": "Call by Value: Parameter Passing Mechanism and Proof of Value Isolation",
        "category": "Functions",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Question", "Viva Favorite"],
        "question": "Explain the Call by Value mechanism in C. Write a program attempting to swap two numbers using Call by Value, proving that formal parameters are local copies that cannot alter caller arguments.",
        "logic": "In Call by Value, the values of actual arguments are copied into separate storage allocated for formal parameters on the function's stack frame. Modifications to formal parameters affect only the local copies.",
        "concept": "1. Actual Arguments: Variables passed in the function call (`main` scope).\n2. Formal Parameters: Variables defined in the function header (function scope).\n3. Value Isolation: The called function operates on a cloned copy. Once the function finishes, its stack frame is popped, discarding the modified copies without affecting the caller's variables.\n4. Default in C: C passes ALL scalar variables (`int`, `char`, `float`, structures) strictly by value.",
        "syntax": "void swapByValue(int x, int y);",
        "code": """#include <stdio.h>

/* Attempted Swap using Call by Value */
void swapByValue(int a, int b) {
    printf("  [Inside swapByValue - Before Swap]: a = %d, b = %d\\n", a, b);
    int temp = a;
    a = b;
    b = temp;
    printf("  [Inside swapByValue - After Swap]:  a = %d, b = %d (Copies changed)\\n", a, b);
}

int main(void) {
    int num1 = 10, num2 = 20;

    printf("In main() BEFORE calling swapByValue: num1 = %d, num2 = %d\\n\\n", num1, num2);
    swapByValue(num1, num2);
    printf("\\nIn main() AFTER returning from swapByValue: num1 = %d, num2 = %d (UNALTERED!)\\n", 
           num1, num2);

    return 0;
}""",
        "output": """In main() BEFORE calling swapByValue: num1 = 10, num2 = 20

  [Inside swapByValue - Before Swap]: a = 10, b = 20
  [Inside swapByValue - After Swap]:  a = 20, b = 10 (Copies changed)

In main() AFTER returning from swapByValue: num1 = 10, num2 = 20 (UNALTERED!)""",
        "explanation": "1. `num1` (10) and `num2` (20) in `main` are copied into `a` and `b` on `swapByValue`'s stack frame.\n2. `a` and `b` are swapped locally inside `swapByValue`.\n3. When `swapByValue` returns, its stack frame is destroyed. `num1` and `num2` in `main` remain 10 and 20.",
        "mistakes": [
            ("Expecting `swapByValue(x, y)` to alter variables in the caller.", "Call by Value never alters original caller variables. You must pass memory addresses (pointers) to achieve modification."),
            ("Assuming passing an array passes the array by value.", "Arrays decay to pointers. When you pass an array, you pass the memory address of its first element, so elements CAN be modified by the function.")
        ],
        "practice_q": "Can a function in C return multiple values directly using the `return` statement? How do we achieve multiple outputs?"
    },
    {
        "num": 55,
        "title": "Storage Classes in C: auto, extern, static, and register",
        "category": "Storage Classes",
        "difficulty": "Intermediate",
        "exam_tags": ["High Yield Exam", "Viva Must-Know"],
        "question": "Compare the four C storage classes (`auto`, `extern`, `static`, `register`). Detail their Scope, Lifetime, Default Initial Value, and Memory Storage Location in a comprehensive comparison table.",
        "logic": "Storage classes determine the scope (visibility), lifetime (longevity), default value, and physical memory region (CPU registers, stack, data segment, or BSS) of a variable.",
        "concept": "Comprehensive Comparison:\n1. `auto`:\n- Keyword: `auto` (default for local variables)\n- Storage: Stack memory\n- Scope: Block / Local\n- Lifetime: Till end of enclosing block\n- Default: Garbage value\n2. `register`:\n- Keyword: `register`\n- Storage: CPU hardware registers (if available, else Stack)\n- Scope: Block / Local\n- Lifetime: Till end of block\n- Default: Garbage value\n- Note: Cannot take its address using `&` (`&regVar` causes compile error!)\n3. `static`:\n- Keyword: `static`\n- Storage: Data segment (Initialized) or BSS segment (Uninitialized)\n- Scope: Block (if local) or File (if global)\n- Lifetime: Entire program execution\n- Default: Zero (`0` or `NULL`)\n4. `extern`:\n- Keyword: `extern`\n- Storage: Data segment / BSS\n- Scope: Global / Program-wide (across multiple files)\n- Lifetime: Entire program execution\n- Default: Zero",
        "syntax": "auto int x; register int y; static int z; extern int g;",
        "code": """#include <stdio.h>

/* Global variable with file scope */
int globalCounter = 100;

void storageClassDemo(void) {
    auto int autoVar = 1;     /* Stack allocated, re-created on each call */
    static int staticVar = 1; /* Data segment, persists across calls */

    printf("autoVar = %d (re-initialized) | staticVar = %d (persisted)\\n", 
           autoVar, staticVar);

    autoVar++;
    staticVar++;
}

int main(void) {
    printf("=== Storage Class Behavior Across 3 Calls ===\\n");
    for (int i = 1; i <= 3; i++) {
        printf("Call %d: ", i);
        storageClassDemo();
    }

    /* Demonstration of register variable */
    register int fastIndex = 0;
    for (fastIndex = 0; fastIndex < 3; fastIndex++) {
        /* CPU register hints faster loop execution */
    }
    printf("\\nRegister loop completed successfully (fastIndex = %d)\\n", fastIndex);

    return 0;
}""",
        "output": """=== Storage Class Behavior Across 3 Calls ===
Call 1: autoVar = 1 (re-initialized) | staticVar = 1 (persisted)
Call 2: autoVar = 1 (re-initialized) | staticVar = 2 (persisted)
Call 3: autoVar = 1 (re-initialized) | staticVar = 3 (persisted)

Register loop completed successfully (fastIndex = 3)""",
        "explanation": "1. `autoVar` is allocated on the stack each time `storageClassDemo` is called and destroyed on exit; it remains `1` at the start of every call.\n2. `staticVar` is initialized once in the data segment when the program starts. Its value persists across calls, incrementing to 2, then 3.\n3. `register` requests CPU register storage for frequently used variables like loop counters.",
        "mistakes": [
            ("Attempting to take the address of a register variable: `&fastIndex`.", "Compilers generate a compilation error: `error: address of register variable requested`. Registers lack memory bus RAM addresses."),
            ("Assuming `static` global variables are accessible across different files.", "A `static` global variable is restricted to file scope; other files cannot link to it even with `extern`.")
        ],
        "practice_q": "What is the difference between defining `int count;` versus `extern int count;`?"
    },
    {
        "num": 56,
        "title": "Introduction to Pointers: Addresses, Declarations, and Dereferencing",
        "category": "Pointers",
        "difficulty": "Fundamental",
        "exam_tags": ["Core Concept", "Viva Must-Know"],
        "question": "What is a pointer variable in C? Explain the Address-of operator `&` and Indirection/Dereferencing operator `*`. Illustrate memory address mapping with a diagrammatic trace.",
        "logic": "A pointer is a variable that stores the physical memory address of another variable. The `&` operator retrieves an address, and the `*` operator accesses the value at that address.",
        "concept": "1. Declaration: `data_type *ptr_name;` (e.g. `int *p`).\n- The `*` indicates `p` is a pointer.\n- The `data_type` indicates the type of data stored at the target address.\n2. Address-of `&`: Unary operator returning the memory address of its operand.\n3. Dereference `*`: Unary operator accessing or modifying the value stored at the target address (`*p = 50;`).\n4. Pointer Size: Pointers store memory addresses. On a 32-bit architecture, ALL pointers are 4 bytes; on a 64-bit architecture, ALL pointers are 8 bytes, regardless of whether they point to `char`, `int`, or `double`.",
        "syntax": "int x = 10; int *p = &x; *p = 25;",
        "code": """#include <stdio.h>

int main(void) {
    int count = 42;
    int *pCount = &count; /* Pointer pCount holds the address of count */

    printf("=== Pointer and Memory Address Demonstration ===\\n");
    printf("Value of 'count':                 %d\\n", count);
    printf("Memory Address of 'count' (&count): %p\\n", (void*)&count);
    printf("Value stored in pointer 'pCount':  %p\\n", (void*)pCount);
    printf("Value accessed via *pCount:        %d\\n", *pCount);
    printf("Memory Address of pointer itself:  %p\\n\\n", (void*)&pCount);

    /* Modifying count indirectly through pointer dereferencing */
    *pCount = 99;
    printf("After *pCount = 99 -> Value of 'count' is now: %d\\n", count);

    printf("\\nPointer Sizes on this system:\\n");
    printf("sizeof(char*):   %zu bytes\\n", sizeof(char*));
    printf("sizeof(int*):    %zu bytes\\n", sizeof(int*));
    printf("sizeof(double*): %zu bytes\\n", sizeof(double*));

    return 0;
}""",
        "output": """=== Pointer and Memory Address Demonstration ===
Value of 'count':                 42
Memory Address of 'count' (&count): 0x7ffd5a68acbc
Value stored in pointer 'pCount':  0x7ffd5a68acbc
Value accessed via *pCount:        42
Memory Address of pointer itself:  0x7ffd5a68acc0

After *pCount = 99 -> Value of 'count' is now: 99

Pointer Sizes on this system:
sizeof(char*):   8 bytes
sizeof(int*):    8 bytes
sizeof(double*): 8 bytes""",
        "explanation": "1. `count` has value `42` at memory address `0x7ffd5a68acbc`.\n2. `pCount` stores that address. Dereferencing `*pCount` yields `42`.\n3. Modifying `*pCount = 99` changes the value of `count` directly in memory.\n4. All pointer types have identical size (8 bytes on 64-bit OS).",
        "mistakes": [
            ("Dereferencing an uninitialized pointer (`int *p; *p = 10;`).", "Uninitialized pointers contain random garbage addresses. Writing to a random memory address causes a segmentation fault or memory corruption."),
            ("Confusing `*p` with `p`.", "`p` is the memory address; `*p` is the value stored at that address.")
        ],
        "practice_q": "What is a `NULL` pointer and why should uninitialized pointers always be set to `NULL`?"
    },
    {
        "num": 57,
        "title": "Call by Reference: Pointer-Based Argument Modification and Swapping",
        "category": "Pointers & Functions",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Explain how C simulates 'Call by Reference' using pointers. Write a complete C program to swap two integers using pointers and demonstrate how functions can return multiple values.",
        "logic": "By passing the memory addresses of variables as arguments (`&a, &b`), the function's formal pointer parameters can directly dereference and modify caller variables in place.",
        "concept": "1. Memory Sharing: Caller passes `&x`. Callee receives `int *ptr`. Callee performs `*ptr = new_val`, altering `x` in the caller's stack frame.\n2. Simulating Multiple Return Values: A C function can only return one value via `return`. By passing pointers as output parameters, a function can return 2, 3, or more results (e.g., quotient and remainder, or min and max).",
        "syntax": "void swap(int *x, int *y);\nswap(&num1, &num2);",
        "code": """#include <stdio.h>

/* Swapping two numbers using pointers (Call by Reference) */
void swapByReference(int *ptrA, int *ptrB) {
    int temp = *ptrA;
    *ptrA = *ptrB;
    *ptrB = temp;
}

/* Function returning multiple values: Quotient and Remainder */
void divideWithRemainder(int dividend, int divisor, int *quotient, int *remainder) {
    *quotient = dividend / divisor;
    *remainder = dividend % divisor;
}

int main(void) {
    int x = 100, y = 200;

    printf("=== Swapping via Pointers ===\\n");
    printf("Before Swap: x = %d, y = %d\\n", x, y);
    swapByReference(&x, &y);
    printf("After Swap:  x = %d, y = %d (Successfully Swapped!)\\n\\n", x, y);

    int q, r;
    divideWithRemainder(29, 4, &q, &r);
    printf("=== Multiple Return Simulation (29 / 4) ===\\n");
    printf("Quotient:  %d\\n", q);
    printf("Remainder: %d\\n", r);

    return 0;
}""",
        "output": """=== Swapping via Pointers ===
Before Swap: x = 100, y = 200
After Swap:  x = 200, y = 100 (Successfully Swapped!)

=== Multiple Return Simulation (29 / 4) ===
Quotient:  7
Remainder: 1""",
        "explanation": "1. In `swapByReference(&x, &y)`, the addresses of `x` and `y` are passed.\n2. Dereferencing `*ptrA` and `*ptrB` accesses and modifies `x` and `y` directly in `main`'s memory.\n3. `divideWithRemainder` writes both quotient and remainder directly into `q` and `r` in `main`.",
        "mistakes": [
            ("Calling `swapByReference(x, y)` without `&`.", "Passing values instead of addresses triggers a compiler type mismatch error (`int` to `int*`)."),
            ("Writing `temp = ptrA;` instead of `temp = *ptrA;`.", "Assigns the memory address rather than the integer value, causing a type mismatch error.")
        ],
        "practice_q": "Write a function prototype that computes the roots of a quadratic equation and returns both roots using pointers."
    },
    {
        "num": 58,
        "title": "Pointer Arithmetic: Scaling Rules, Valid Operations, and Subtraction",
        "category": "Pointers",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Question", "Viva Must-Know"],
        "question": "Explain the rules of pointer arithmetic in C. Why does `ptr + 1` not simply add 1 byte to the address? Detail all valid and invalid operations on pointers.",
        "logic": "Pointer arithmetic is automatically scaled by the size of the data type pointed to. Adding $1$ to a pointer increments the address by `sizeof(*ptr)` bytes.",
        "concept": "1. Scaling Formula: `Address(ptr + n) = Address(ptr) + n * sizeof(*ptr)`.\n- For `int *p` (4 bytes): `p + 1` advances by 4 bytes.\n- For `double *p` (8 bytes): `p + 1` advances by 8 bytes.\n2. Valid Operations:\n- Adding an integer to a pointer: `ptr + n`, `ptr - n`\n- Increment / Decrement: `++ptr`, `--ptr`\n- Subtracting two pointers of the SAME array: `ptr1 - ptr2` (yields the number of elements between them as `ptrdiff_t`)\n- Pointer comparisons: `<`, `<=`, `>`, `==`, `!=`\n3. Strictly ILLEGAL Operations in C:\n- Adding two pointers (`p1 + p2` -> Compile Error)\n- Multiplying or dividing a pointer by a number (`p * 2` -> Compile Error)\n- Modulus on pointers (`p % 2` -> Compile Error)",
        "syntax": "ptr + n advances by n * sizeof(*ptr) bytes\nptr2 - ptr1 returns number of elements",
        "code": """#include <stdio.h>
#include <stddef.h>

int main(void) {
    int arr[] = {10, 20, 30, 40, 50};
    int *p1 = &arr[0];
    int *p4 = &arr[3];

    printf("Base Address (p1 = &arr[0]): %p (Value: %d)\\n", (void*)p1, *p1);
    printf("Target Address (p4 = &arr[3]): %p (Value: %d)\\n\\n", (void*)p4, *p4);

    printf("=== Pointer Arithmetic Scaling ===\\n");
    printf("p1 + 1 address: %p (+%td bytes = 1 * sizeof(int))\\n", 
           (void*)(p1 + 1), (char*)(p1 + 1) - (char*)p1);
    printf("p1 + 2 address: %p (+%td bytes = 2 * sizeof(int))\\n", 
           (void*)(p1 + 2), (char*)(p1 + 2) - (char*)p1);

    printf("\\n=== Pointer Subtraction ===\\n");
    ptrdiff_t diff = p4 - p1;
    printf("p4 - p1 = %td elements (arr[3] is 3 elements ahead of arr[0])\\n", diff);

    return 0;
}""",
        "output": """Base Address (p1 = &arr[0]): 0x7ffd5a68acb0 (Value: 10)
Target Address (p4 = &arr[3]): 0x7ffd5a68acbc (Value: 40)

=== Pointer Arithmetic Scaling ===
p1 + 1 address: 0x7ffd5a68acb4 (+4 bytes = 1 * sizeof(int))
p1 + 2 address: 0x7ffd5a68acb8 (+8 bytes = 2 * sizeof(int))

=== Pointer Subtraction ===
p4 - p1 = 3 elements (arr[3] is 3 elements ahead of arr[0])""",
        "explanation": "1. `p1 + 1` advances by 4 bytes (the size of `int`), landing on `arr[1]`.\n2. `p1 + 2` advances by 8 bytes, landing on `arr[2]`.\n3. Subtracting `p4 - p1` yields `3` (the number of `int` elements between them, not the byte difference).",
        "mistakes": [
            ("Attempting to add two pointers: `ptr1 + ptr2`.", "Adding memory addresses has no physical or semantic meaning; the compiler flags this as an error."),
            ("Subtracting pointers that point to different arrays.", "Pointer subtraction is only defined when both pointers point into the same array object or one past its end.")
        ],
        "practice_q": "What will `sizeof(p1)` return versus `sizeof(*p1)`?"
    },
    {
        "num": 59,
        "title": "Pointers and Arrays: Equivalence of *(arr + i) and arr[i]",
        "category": "Pointers & Arrays",
        "difficulty": "Intermediate",
        "exam_tags": ["Viva Trap", "Exam Question"],
        "question": "Demonstrate the relationship between arrays and pointers in C. Prove that `arr[i]`, `*(arr + i)`, and `i[arr]` evaluate to the exact same value. Why is an array name a pointer constant?",
        "logic": "In C, the subscript notation `arr[i]` is defined by the standard as syntactic sugar for `*(arr + i)`. Addition is commutative, so `*(arr + i) == *(i + arr) == i[arr]`.",
        "concept": "1. Array Decay: In most expressions, an array name evaluates to a pointer to its first element (`&arr[0]`).\n2. Pointer Constant: Unlike a pointer variable (`int *p`), an array name (`arr`) is a constant. You CANNOT reassign it (`arr = p` or `arr++` causes a compile error).\n3. Syntactic Sugar Equivalence:\n- `arr[i]` $\\iff$ `*(arr + i)`\n- `i[arr]` $\\iff$ `*(i + arr)`\n- `&arr[i]` $\\iff$ `(arr + i)`.",
        "syntax": "*(arr + i) == arr[i] == i[arr]",
        "code": """#include <stdio.h>

int main(void) {
    int numbers[5] = {10, 20, 30, 40, 50};
    int *ptr = numbers; /* Array name decays to &numbers[0] */

    printf("=== Verification of Array-Pointer Equivalence ===\\n");
    for (int i = 0; i < 5; i++) {
        printf("Index %d -> arr[%d]: %d | *(arr+%d): %d | *(ptr+%d): %d | %d[arr]: %d\\n",
               i, i, numbers[i], i, *(numbers + i), i, *(ptr + i), i, i[numbers]);
    }

    printf("\\nPointer Variable Increment (Valid):\\n");
    printf("Initial *ptr: %d\\n", *ptr);
    ptr++; /* Valid: ptr now points to numbers[1] */
    printf("After ptr++:  %d\\n", *ptr);

    /* numbers++; -> Compilation Error: lvalue required as increment operand */

    return 0;
}""",
        "output": """=== Verification of Array-Pointer Equivalence ===
Index 0 -> arr[0]: 10 | *(arr+0): 10 | *(ptr+0): 10 | 0[arr]: 10
Index 1 -> arr[1]: 20 | *(arr+1): 20 | *(ptr+1): 20 | 1[arr]: 20
Index 2 -> arr[2]: 30 | *(arr+2): 30 | *(ptr+2): 30 | 2[arr]: 30
Index 3 -> arr[3]: 40 | *(arr+3): 40 | *(ptr+3): 40 | 3[arr]: 40
Index 4 -> arr[4]: 50 | *(arr+4): 50 | *(ptr+4): 50 | 4[arr]: 50

Pointer Variable Increment (Valid):
Initial *ptr: 10
After ptr++:  20""",
        "explanation": "1. `numbers[i]`, `*(numbers + i)`, and `i[numbers]` all evaluate to the same value.\n2. `ptr` is a modifiable pointer variable, so `ptr++` is valid.\n3. `numbers` is an array name (a pointer constant), so `numbers++` is rejected by the compiler.",
        "mistakes": [
            ("Attempting `numbers++` to traverse an array.", "Array names are not modifiable l-values. Assign `int *p = numbers;` and increment `p++` instead."),
            ("Assuming `sizeof(numbers)` and `sizeof(ptr)` are identical.", "`sizeof(numbers)` gives the full array size ($5 \\times 4 = 20$ bytes). `sizeof(ptr)` gives 8 bytes (pointer size).")
        ],
        "practice_q": "What will `*ptr++` do versus `(*ptr)++`?"
    },
    {
        "num": 60,
        "title": "Double Pointers (Pointer to Pointer): Concepts and Dynamic Allocation",
        "category": "Pointers",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Question", "Viva Favorite"],
        "question": "What is a double pointer (pointer to pointer)? Explain its syntax, memory address chaining, and its application in modifying pointer values inside functions.",
        "logic": "A double pointer stores the memory address of another pointer variable. To modify where a pointer points inside a called function, you must pass the address of that pointer (`&ptr`), which requires a double pointer parameter (`type **`).",
        "concept": "1. Declaration: `int **pp;`\n2. Addressing Chain: `var` (value 50 at 0x1000) $\\leftarrow$ `p` (holds 0x1000 at 0x2000) $\\leftarrow$ `pp` (holds 0x2000 at 0x3000).\n3. Dereference Levels:\n- `pp`: Address of pointer `p` (0x2000)\n- `*pp`: Value of `p` (0x1000, address of `var`)\n- `**pp`: Value of `var` (50)\n4. Primary Use Cases: Dynamic 2D arrays, modifying caller's head pointer in linked lists, and command-line arguments (`char **argv`).",
        "syntax": "int x = 10; int *p = &x; int **pp = &p;",
        "code": """#include <stdio.h>

/* Function that modifies the caller's pointer using a double pointer */
void redirectPointer(int **ptrToPtr, int *newTarget) {
    *ptrToPtr = newTarget; /* Modifies caller's pointer */
}

int main(void) {
    int a = 10, b = 20;
    int *myPtr = &a;
    int **doublePtr = &myPtr;

    printf("=== Double Pointer Addressing Chain ===\\n");
    printf("Value of 'a':                     %d\\n", a);
    printf("Address of 'a' (&a):              %p\\n", (void*)&a);
    printf("Value of 'myPtr' (points to a):   %p\\n", (void*)myPtr);
    printf("Address of 'myPtr' (&myPtr):      %p\\n", (void*)&myPtr);
    printf("Value of 'doublePtr':             %p\\n", (void*)doublePtr);
    printf("Dereferenced once (*doublePtr):   %p\\n", (void*)*doublePtr);
    printf("Dereferenced twice (**doublePtr): %d\\n\\n", **doublePtr);

    /* Redirect myPtr to point to b */
    redirectPointer(&myPtr, &b);
    printf("After redirectPointer(&myPtr, &b):\\n");
    printf("myPtr now points to address of 'b': %p (Value: %d)\\n", 
           (void*)myPtr, *myPtr);

    return 0;
}""",
        "output": """=== Double Pointer Addressing Chain ===
Value of 'a':                     10
Address of 'a' (&a):              0x7ffd5a68acbc
Value of 'myPtr' (points to a):   0x7ffd5a68acbc
Address of 'myPtr' (&myPtr):      0x7ffd5a68acc0
Value of 'doublePtr':             0x7ffd5a68acc0
Dereferenced once (*doublePtr):   0x7ffd5a68acbc
Dereferenced twice (**doublePtr): 10

After redirectPointer(&myPtr, &b):
myPtr now points to address of 'b': 0x7ffd5a68acb8 (Value: 20)""",
        "explanation": "1. `doublePtr` holds `&myPtr`.\n2. `**doublePtr` dereferences twice to access `a` (10).\n3. `redirectPointer` receives `&myPtr` and updates `myPtr` to point to `b`.",
        "mistakes": [
            ("Passing `myPtr` instead of `&myPtr` to redirect a pointer.", "Passing `myPtr` passes the pointer by value. Changes to the pointer will only affect a local copy."),
            ("Missing the second asterisk during dereferencing (`*doublePtr = 50`).", "Assigns integer 50 as a memory address to the single pointer, causing a crash on next access.")
        ],
        "practice_q": "How does `char **argv` in `main(int argc, char **argv)` represent command-line arguments?"
    },
    {
        "num": 61,
        "title": "const with Pointers: Pointer to Constant vs Constant Pointer",
        "category": "Pointers & Modifiers",
        "difficulty": "Intermediate",
        "exam_tags": ["Interview Favorite", "Viva Must-Know"],
        "question": "Differentiate between: (1) `const int *p`, (2) `int * const p`, and (3) `const int * const p`. Provide the clockwise/spiral rule for reading complex declarations.",
        "logic": "The placement of `const` relative to the asterisk `*` dictates whether the pointer address is constant or the data pointed to is constant.",
        "concept": "1. Pointer to Constant (`const int *p` or `int const *p`):\n- Data is read-only. You CANNOT modify the value through `*p` (`*p = 10` is an error).\n- Pointer address is modifiable. You CAN reassign `p = &other`.\n- Commonly used for read-only function parameters like `strcmp(const char *s1, const char *s2)`.\n2. Constant Pointer (`int * const p`):\n- Data is modifiable. You CAN change the value: `*p = 10`.\n- Pointer address is fixed. You CANNOT reassign `p = &other`.\n3. Constant Pointer to Constant (`const int * const p`):\n- Both the address and the data are strictly read-only.\n4. Reading Rule: Read right-to-left. `int * const p` is 'p is a constant pointer to an int'.",
        "syntax": "const int *p;       /* Data is const */\nint * const p = &x; /* Address is const */",
        "code": """#include <stdio.h>

int main(void) {
    int x = 10;
    int y = 20;

    /* 1. Pointer to Constant */
    const int *ptrToConst = &x;
    printf("ptrToConst points to value: %d\\n", *ptrToConst);
    ptrToConst = &y; /* OK: Pointer can be redirected */
    printf("ptrToConst redirected to y: %d\\n", *ptrToConst);
    /* *ptrToConst = 30; -> Compile Error: assignment of read-only location */

    /* 2. Constant Pointer */
    int * const constPtr = &x;
    *constPtr = 99; /* OK: Target data can be modified */
    printf("x modified via constPtr:    %d\\n", x);
    /* constPtr = &y; -> Compile Error: assignment of read-only variable */

    /* 3. Constant Pointer to Constant */
    const int * const frozen = &x;
    printf("frozen value:               %d\\n", *frozen);
    /* *frozen = 50; -> Error! */
    /* frozen = &y;  -> Error! */

    return 0;
}""",
        "output": """ptrToConst points to value: 10
ptrToConst redirected to y: 20
x modified via constPtr:    99
frozen value:               99""",
        "explanation": "1. `ptrToConst` can be redirected to point to `y`, but `*ptrToConst` cannot modify the underlying integer.\n2. `constPtr` cannot be redirected to another address, but can modify `x` to `99`.\n3. `frozen` locks both the pointer address and the target value.",
        "mistakes": [
            ("Thinking `const int *p` means the variable itself cannot change.", "The variable can still be modified directly (`x = 50;`). It just cannot be modified THROUGH `*p`."),
            ("Declaring an uninitialized `int * const p;`.", "Since a constant pointer cannot be reassigned, it must be initialized when declared.")
        ],
        "practice_q": "Why should pointer parameters in functions that only read data (like `strlen`) always be declared with `const`?"
    },
    {
        "num": 62,
        "title": "Function Pointers: Callback Architecture and Dispatch Tables",
        "category": "Advanced Pointers",
        "difficulty": "Exam-Level",
        "exam_tags": ["High Yield Exam", "Advanced Concept"],
        "question": "What is a function pointer in C? Detail its declaration syntax and show how to use function pointers as callbacks and in jump/dispatch tables.",
        "logic": "Functions reside in executable memory (the Code/Text segment). A function pointer holds the starting memory address of a function's machine instructions, allowing functions to be passed as arguments.",
        "concept": "1. Declaration Syntax: `return_type (*func_ptr_name)(param_types);`\n- Parentheses around `(*func_ptr_name)` are mandatory; without them, `int *f(int)` declares a function returning a pointer to `int`!\n2. Assignment: `func_ptr = &function_name;` (or simply `func_ptr = function_name`).\n3. Invocation: `(*func_ptr)(arg1, arg2);` or `func_ptr(arg1, arg2);`.\n4. Applications: Callbacks (e.g. `qsort()` comparison function), event-driven systems, state machines, and dispatch tables.",
        "syntax": "int (*operation)(int, int);",
        "code": """#include <stdio.h>

/* Callback Target Functions */
int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }
int multiply(int a, int b) { return a * b; }

/* Higher-Order Function accepting a function pointer callback */
int executeOperation(int x, int y, int (*opCallback)(int, int)) {
    return opCallback(x, y);
}

int main(void) {
    int a = 12, b = 4;

    printf("=== Function Pointer Callbacks ===\\n");
    printf("Add via Callback:      %d\\n", executeOperation(a, b, add));
    printf("Subtract via Callback: %d\\n", executeOperation(a, b, subtract));
    printf("Multiply via Callback: %d\\n", executeOperation(a, b, multiply));

    /* Function Pointer Array (Dispatch Table) */
    int (*dispatchTable[3])(int, int) = {add, subtract, multiply};
    const char *names[] = {"ADD", "SUBTRACT", "MULTIPLY"};

    printf("\\n=== Dispatch Table Execution ===\\n");
    for (int i = 0; i < 3; i++) {
        printf("Op %s: %d\\n", names[i], dispatchTable[i](a, b));
    }

    return 0;
}""",
        "output": """=== Function Pointer Callbacks ===
Add via Callback:      16
Subtract via Callback: 8
Multiply via Callback: 48

=== Dispatch Table Execution ===
Op ADD: 16
Op SUBTRACT: 8
Op MULTIPLY: 48""",
        "explanation": "1. `executeOperation` accepts `add`, `subtract`, or `multiply` and calls them through `opCallback`.\n2. `dispatchTable` is an array of function pointers, allowing operations to be selected dynamically by index in $O(1)$ time without `switch-case`.",
        "mistakes": [
            ("Omitting parentheses: writing `int *f(int, int)`.", "Declares a normal function returning `int*`. A function pointer requires `int (*f)(int, int)`."),
            ("Calling through a `NULL` function pointer.", "Invoking a null or uninitialized function pointer jumps to address 0, causing an immediate segmentation fault.")
        ],
        "practice_q": "How does standard library `qsort()` use a function pointer for custom sorting?"
    },
    {
        "num": 63,
        "title": "Introduction to Recursion: Base Cases, Recursive Steps, and Call Stack",
        "category": "Recursion",
        "difficulty": "Fundamental",
        "exam_tags": ["Core Concept", "Viva Must-Know"],
        "question": "What is recursion in C? Explain the two essential components of any recursive function (Base Case and Recursive Step). Describe what happens to the call stack during recursive execution.",
        "logic": "Recursion occurs when a function calls itself directly or indirectly to solve smaller instances of the same problem. A base case terminates recursion; without it, infinite recursion causes a stack overflow.",
        "concept": "1. Base Case: The stopping condition that returns a result directly without further recursive calls.\n2. Recursive Step: The rule that reduces the original problem into a smaller subproblem of the same form.\n3. Call Stack Mechanics:\n- Each recursive call creates a new Activation Record (stack frame) containing parameters, local variables, and return address.\n- Winding Phase: Stack frames accumulate as recursive calls descend.\n- Unwinding Phase: Once the base case is reached, functions return values and their stack frames are popped one by one in reverse order (LIFO).\n4. Stack Overflow: If recursion does not terminate, the stack exhausts allocated memory, crashing the program with a segmentation fault.",
        "syntax": "return (n <= 1) ? 1 : n * factorial(n - 1);",
        "code": """#include <stdio.h>

void printCountdown(int n) {
    /* 1. Base Case */
    if (n == 0) {
        printf(">> Liftoff! (Base Case Reached at n=0)\\n");
        return;
    }

    /* Winding Phase */
    printf("Descending: n = %d (Stack frame pushed)\\n", n);

    /* 2. Recursive Step */
    printCountdown(n - 1);

    /* Unwinding Phase */
    printf("Returning:  n = %d (Stack frame popped)\\n", n);
}

int main(void) {
    printf("=== Call Stack Demonstration (n = 3) ===\\n");
    printCountdown(3);
    return 0;
}""",
        "output": """=== Call Stack Demonstration (n = 3) ===
Descending: n = 3 (Stack frame pushed)
Descending: n = 2 (Stack frame pushed)
Descending: n = 1 (Stack frame pushed)
>> Liftoff! (Base Case Reached at n=0)
Returning:  n = 1 (Stack frame popped)
Returning:  n = 2 (Stack frame popped)
Returning:  n = 3 (Stack frame popped)""",
        "explanation": "1. Calls descend: `printCountdown(3)` $\\to$ `(2)` $\\to$ `(1)` $\\to$ `(0)`.\n2. Base case at `n = 0` prints 'Liftoff!' and begins the return sequence.\n3. Stack frames pop in reverse order: 1, 2, 3.",
        "mistakes": [
            ("Omitting the base case.", "Causes infinite recursive calls until the OS kills the process due to stack overflow."),
            ("Making a recursive call that does not reduce toward the base case (e.g. `f(n)` instead of `f(n-1)`).", "Recursion must strictly converge toward the base case.")
        ],
        "practice_q": "What is tail recursion and how can a modern compiler optimize it into a loop?"
    },
    {
        "num": 64,
        "title": "Factorial Computation using Recursion: Stack Frame Trace",
        "category": "Recursion",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Write a complete C program to compute the factorial of a non-negative integer using recursion. Provide a step-by-step trace of activation records and address integer overflow.",
        "logic": "Mathematical definition: $0! = 1$, and $n! = n \\times (n - 1)!$ for $n > 0$. The base case is $n \\le 1$ returning $1$.",
        "concept": "1. Recurrence: $F(n) = n \\cdot F(n - 1)$ for $n > 1$; $F(0) = F(1) = 1$.\n2. Stack Trace for `factorial(4)`:\n- Call 1: `factorial(4) = 4 * factorial(3)`\n- Call 2: `factorial(3) = 3 * factorial(2)`\n- Call 3: `factorial(2) = 2 * factorial(1)`\n- Call 4: `factorial(1) = 1` (Base Case)\n- Unwinds: $2 \\times 1 = 2 \\to 3 \\times 2 = 6 \\to 4 \\times 6 = 24$.\n3. Data Type: Factorials grow rapidly ($13!$ overflows 32-bit `int`, $21!$ overflows 64-bit `long long`). Use `unsigned long long` for calculations up to $20!$.",
        "syntax": "unsigned long long factorial(unsigned int n);",
        "code": """#include <stdio.h>

unsigned long long factorial(unsigned int n) {
    /* Base Case */
    if (n <= 1) {
        return 1ULL;
    }
    /* Recursive Step */
    return (unsigned long long)n * factorial(n - 1);
}

int main(void) {
    unsigned int testValues[] = {0, 1, 5, 10, 15, 20};
    int count = sizeof(testValues) / sizeof(testValues[0]);

    printf("=== Recursive Factorial Computations ===\\n");
    for (int i = 0; i < count; i++) {
        unsigned int val = testValues[i];
        printf("%2u! = %llu\\n", val, factorial(val));
    }

    return 0;
}""",
        "output": """=== Recursive Factorial Computations ===
 0! = 1
 1! = 1
 5! = 120
10! = 3628800
15! = 1307674368000
20! = 2432902008176640000""",
        "explanation": "1. `0!` correctly returns 1 via the base case `n <= 1`.\n2. Computations unwind and multiply up the call stack.\n3. `20!` evaluates to `2432902008176640000`, which fits inside 64-bit unsigned integer.",
        "mistakes": [
            ("Using signed 32-bit `int` for factorials $> 12$.", "$13! = 6,227,020,800$, which exceeds $2^{31}-1 = 2,147,483,647$, producing negative overflow values."),
            ("Calling `factorial(-5)` without input validation.", "Negative integers never satisfy `n == 1`, causing an infinite recursion stack overflow.")
        ],
        "practice_q": "What is the time and space complexity of recursive factorial for input N?"
    },
    {
        "num": 65,
        "title": "Fibonacci Sequence: Recursion Tree and Exponential Overhead",
        "category": "Recursion",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "Viva Favorite"],
        "question": "Implement recursive Fibonacci in C. Draw the recursion call tree for $N = 4$ and explain why naive recursive Fibonacci has exponential time complexity $O(2^N)$.",
        "logic": "Fibonacci relation: $F(0) = 0, F(1) = 1$, and $F(n) = F(n-1) + F(n-2)$. Naive recursion recalculates identical subproblems repeatedly.",
        "concept": "1. Recurrence: $T(N) = T(N-1) + T(N-2) + O(1) \\implies O(2^N)$ time complexity.\n2. Call Tree for $F(4)$:\n```\n                 F(4)\n               /      \\\n            F(3)       F(2)\n           /    \\      /   \\\n        F(2)   F(1)  F(1)  F(0)\n       /    \\\n     F(1)  F(0)\n```\nNotice that $F(2)$ is computed independently 2 times, $F(1)$ is called 3 times, and $F(0)$ is called 2 times. For $N = 50$, this requires over $10^{15}$ operations, taking days to finish!\n3. Iterative alternative runs in $O(N)$ linear time with $O(1)$ space.",
        "syntax": "if (n <= 1) return n; return fib(n-1) + fib(n-2);",
        "code": """#include <stdio.h>

long long recursiveCallCount = 0;

long long fibonacciRecursive(int n) {
    recursiveCallCount++;
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

int main(void) {
    int testTerms[] = {4, 6, 8, 10};

    printf("=== Recursive Fibonacci & Call Overhead Analysis ===\\n");
    printf("%-6s | %-12s | %-16s\\n", "Term N", "Fib(N)", "Function Calls");
    printf("---------------------------------------\\n");

    for (int i = 0; i < 4; i++) {
        int n = testTerms[i];
        recursiveCallCount = 0;
        long long val = fibonacciRecursive(n);
        printf("F(%2d)  | %-12lld | %-16lld\\n", n, val, recursiveCallCount);
    }

    return 0;
}""",
        "output": """=== Recursive Fibonacci & Call Overhead Analysis ===
Term N | Fib(N)       | Function Calls  
---------------------------------------
F( 4)  | 3            | 9               
F( 6)  | 8            | 25              
F( 8)  | 21           | 67              
F(10)  | 55           | 177             """,
        "explanation": "1. For $N = 4$, computing $F(4) = 3$ requires 9 function calls.\n2. By $N = 10$, the call count grows to 177.\n3. The exponential call overhead illustrates why dynamic programming (memoization) or iteration is preferred for Fibonacci.",
        "mistakes": [
            ("Using naive recursive Fibonacci for $N > 40$.", "The program will appear to freeze because $2^{45}$ operations take several minutes to compute."),
            ("Assuming recursive Fibonacci has $O(N)$ complexity.", "Its time complexity is $O(1.618^N) \\approx O(2^N)$ due to overlapping subproblems.")
        ],
        "practice_q": "How does dynamic programming reduce Fibonacci time complexity from $O(2^N)$ to $O(N)$?"
    },
    {
        "num": 66,
        "title": "GCD using Euclid's Algorithm: Mathematical Basis and Recursive Implementation",
        "category": "Recursion",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "State Euclidean algorithm for Greatest Common Divisor (GCD). Write a recursive C program to compute the GCD and LCM of two positive integers.",
        "logic": "Euclid's theorem: $\\gcd(a, b) = \\gcd(b, a \\% b)$, with base case $\\gcd(a, 0) = a$. LCM is derived using the relation: $\\text{LCM}(a, b) = (a \\times b) / \\gcd(a, b)$.",
        "concept": "1. Mathematical Principle: If $d$ divides both $a$ and $b$, then $d$ also divides the remainder $a \\% b$.\n2. Base Case: When $b == 0$, the GCD is $a$.\n3. Recursive Step: `return gcd(b, a % b);`.\n4. Efficiency: Logarithmic time complexity $O(\\log(\\min(a, b)))$. By Gabriel Lamé's Theorem, the number of steps never exceeds 5 times the number of digits in the smaller number.",
        "syntax": "int gcd(int a, int b) { return (b == 0) ? a : gcd(b, a % b); }",
        "code": """#include <stdio.h>

/* Recursive implementation of Euclid's Algorithm */
long long gcd(long long a, long long b) {
    if (b == 0) {
        return a; /* Base Case */
    }
    return gcd(b, a % b); /* Recursive Step */
}

/* LCM using verified mathematical identity */
long long lcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd(a, b)) * b; /* Divide first to prevent integer overflow */
}

int main(void) {
    long long pairs[][2] = {
        {48, 18},
        {1071, 462},
        {17, 19},
        {252, 105}
    };
    int count = sizeof(pairs) / sizeof(pairs[0]);

    printf("=== Euclidean GCD & LCM System ===\\n");
    for (int i = 0; i < count; i++) {
        long long n1 = pairs[i][0];
        long long n2 = pairs[i][1];

        long long g = gcd(n1, n2);
        long long l = lcm(n1, n2);

        printf("Numbers (%lld, %lld) -> GCD = %lld | LCM = %lld\\n", n1, n2, g, l);
    }

    return 0;
}""",
        "output": """=== Euclidean GCD & LCM System ===
Numbers (48, 18) -> GCD = 6 | LCM = 144
Numbers (1071, 462) -> GCD = 21 | LCM = 23562
Numbers (17, 19) -> GCD = 1 | LCM = 323
Numbers (252, 105) -> GCD = 21 | LCM = 1260""",
        "explanation": "1. For (48, 18): `gcd(48, 18)` $\\to$ `gcd(18, 12)` $\\to$ `gcd(12, 6)` $\\to$ `gcd(6, 0) = 6`.\n2. For coprime numbers (17, 19), GCD is 1 and LCM is $17 \\times 19 = 323$.\n3. In `lcm`, dividing first `(a / gcd) * b` prevents integer overflow.",
        "mistakes": [
            ("Writing `(a * b) / gcd(a, b)` for LCM.", "If `a` and `b` are large, `a * b` will overflow before division. Compute `(a / gcd(a, b)) * b` instead."),
            ("Not handling negative numbers.", "GCD is defined as a positive integer. Apply `labs()` to arguments before calculation.")
        ],
        "practice_q": "How does Euclid's algorithm handle `gcd(a, b)` if the smaller number is passed first (e.g. `gcd(18, 48)`)?"
    },
    {
        "num": 67,
        "title": "Tower of Hanoi: Recursive Formulation, Move Trace, and Minimal Moves",
        "category": "Recursion",
        "difficulty": "Exam-Level",
        "exam_tags": ["Lab Program", "VTU Exam Favorite", "Viva Must-Know"],
        "question": "Solve the classic Tower of Hanoi problem using recursion. Formulate the recurrence relation, state the minimal moves theorem ($2^n - 1$), and write a C program that outputs the step-by-step disk movements.",
        "logic": "To move $N$ disks from Source peg A to Destination peg C using Auxiliary peg B: (1) Move top $N-1$ disks from A to B, (2) Move largest disk $N$ from A to C, (3) Move the $N-1$ disks from B to C.",
        "concept": "1. Rules:\n- Only one disk can be moved at a time.\n- Each move takes the upper disk from one stack and places it on top of another.\n- No larger disk may be placed on top of a smaller disk.\n2. Recurrence Relation:\n$$M(N) = 2 M(N-1) + 1, \\quad M(1) = 1$$\nSolving by substitution: $M(N) = 2^N - 1$.\n- For 3 disks: $2^3 - 1 = 7$ moves.\n- For 4 disks: $2^4 - 1 = 15$ moves.\n3. Time Complexity: $O(2^N)$. Space Complexity: $O(N)$ call stack frames.",
        "syntax": "void towerOfHanoi(int n, char from, char to, char aux);",
        "code": """#include <stdio.h>

long long moveCounter = 0;

void towerOfHanoi(int n, char source, char destination, char auxiliary) {
    /* Base Case: Move 1 disk directly */
    if (n == 1) {
        moveCounter++;
        printf("  Step %2lld: Move Disk 1 from Peg %c -> Peg %c\\n", 
               moveCounter, source, destination);
        return;
    }

    /* Step 1: Move top n-1 disks from Source to Auxiliary (using Destination as temp) */
    towerOfHanoi(n - 1, source, auxiliary, destination);

    /* Step 2: Move the nth (largest) disk directly to Destination */
    moveCounter++;
    printf("  Step %2lld: Move Disk %d from Peg %c -> Peg %c\\n", 
           moveCounter, n, source, destination);

    /* Step 3: Move the n-1 disks from Auxiliary to Destination (using Source as temp) */
    towerOfHanoi(n - 1, auxiliary, destination, source);
}

int main(void) {
    int disks = 3;

    printf("=== Tower of Hanoi Solution (%d Disks) ===\\n", disks);
    printf("Expected Minimal Moves: 2^%d - 1 = %d\\n\\n", disks, (1 << disks) - 1);

    towerOfHanoi(disks, 'A', 'C', 'B');

    printf("\\nSuccessfully completed in %lld moves!\\n", moveCounter);

    return 0;
}""",
        "output": """=== Tower of Hanoi Solution (3 Disks) ===
Expected Minimal Moves: 2^3 - 1 = 7

  Step  1: Move Disk 1 from Peg A -> Peg C
  Step  2: Move Disk 2 from Peg A -> Peg B
  Step  3: Move Disk 1 from Peg C -> Peg B
  Step  4: Move Disk 3 from Peg A -> Peg C
  Step  5: Move Disk 1 from Peg B -> Peg A
  Step  6: Move Disk 2 from Peg B -> Peg C
  Step  7: Move Disk 1 from Peg A -> Peg C

Successfully completed in 7 moves!""",
        "explanation": "1. Disk 1 moves A -> C, Disk 2 moves A -> B, Disk 1 moves C -> B. Now top 2 disks are on peg B.\n2. Disk 3 (largest) moves from A to C.\n3. The 2 disks on B are moved to C: Disk 1 to A, Disk 2 to C, Disk 1 to C.\n4. All 3 disks are on peg C in exactly 7 moves.",
        "mistakes": [
            ("Swapping the parameter order in recursive calls.", "Step 1 uses `(n-1, source, auxiliary, destination)`. Step 3 uses `(n-1, auxiliary, destination, source)`. Swapping peg arguments causes invalid disk placements."),
            ("Assuming Tower of Hanoi can be solved in polynomial time.", "The minimal move count $2^N - 1$ is mathematically proved optimal; an exponential number of moves is mandatory.")
        ],
        "practice_q": "How many seconds would it take to solve a 64-disk Tower of Hanoi at the rate of 1 move per microsecond?"
    },
    {
        "num": 68,
        "title": "Sum of Digits and Power Function (x^n) using Recursion",
        "category": "Recursion",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "Exam Question"],
        "question": "Write recursive C functions to: (1) Compute the sum of digits of an integer, and (2) Compute $x^n$ using fast binary exponentiation in $O(\\log n)$ time.",
        "logic": "Sum of digits: `(n % 10) + sumOfDigits(n / 10)`. Fast power: If $n$ is even, $x^n = (x^{n/2})^2$; if $n$ is odd, $x^n = x \\times x^{n-1}$.",
        "concept": "1. Sum of Digits: Base case `n == 0` returns 0. Time complexity is $O(\\log_{10} N)$.\n2. Binary Exponentiation:\n- Naive recursive power $x \\times x^{n-1}$ takes $O(n)$ steps.\n- Fast power halves $n$ at each step:\n$$x^n = \\begin{cases} 1 & n = 0 \\\\ (x^{n/2})^2 & n \\text{ is even} \\\\ x \\cdot x^{n-1} & n \\text{ is odd} \\end{cases}$$\nTime complexity improves to $O(\\log_2 n)$. Computing $2^{60}$ requires only 60 multiplications instead of $10^{18}$!",
        "syntax": "double fastPower(double x, int n);",
        "code": """#include <stdio.h>

/* 1. Recursive Sum of Digits */
int sumOfDigits(int n) {
    if (n < 0) n = -n;
    if (n == 0) return 0; /* Base Case */
    return (n % 10) + sumOfDigits(n / 10);
}

/* 2. Fast Binary Exponentiation: O(log N) */
double fastPower(double x, int n) {
    if (n == 0) return 1.0; /* Base Case */
    if (n < 0) return 1.0 / fastPower(x, -n); /* Negative exponent handling */

    double half = fastPower(x, n / 2);
    if (n % 2 == 0) {
        return half * half; /* Even exponent: (x^(n/2))^2 */
    } else {
        return x * half * half; /* Odd exponent: x * (x^(n/2))^2 */
    }
}

int main(void) {
    int number = 94827;
    printf("Sum of digits of %d: %d\\n\\n", number, sumOfDigits(number));

    printf("=== Fast Exponentiation (O(log n)) ===\\n");
    printf("2.0 ^ 10 = %.4f\\n", fastPower(2.0, 10));
    printf("3.0 ^ 5  = %.4f\\n", fastPower(3.0, 5));
    printf("5.0 ^ -2 = %.4f\\n", fastPower(5.0, -2));

    return 0;
}""",
        "output": """Sum of digits of 94827: 30

=== Fast Exponentiation (O(log n)) ===
2.0 ^ 10 = 1024.0000
3.0 ^ 5  = 243.0000
5.0 ^ -2 = 0.0400""",
        "explanation": "1. Sum of digits: $9 + 4 + 8 + 2 + 7 = 30$.\n2. `fastPower(2, 10)` computes `half = fastPower(2, 5)`, which computes `half = fastPower(2, 2)`, etc. Resolves in 4 steps.\n3. Handles negative exponents cleanly by taking the reciprocal.",
        "mistakes": [
            ("Writing `fastPower(x, n/2) * fastPower(x, n/2)` without caching `half`.", "Calling the function twice doubles the work, reverting complexity back from $O(\\log n)$ to $O(n)$! Store in `double half` first."),
            ("Not handling negative powers like $5^{-2}$.", "Without negative exponent handling, $n < 0$ causes an infinite recursion stack overflow.")
        ],
        "practice_q": "How many multiplications does fast binary exponentiation take to compute $x^{1024}$?"
    },
    {
        "num": 69,
        "title": "Recursion vs Iteration: Comprehensive Technical Comparison",
        "category": "Recursion",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Theory", "Viva Must-Know"],
        "question": "Provide a thorough comparative analysis between Recursion and Iteration across: Time Overhead, Stack Memory, Code Readability, Risk of Failure, and Infinite Execution Behavior.",
        "logic": "Every recursive algorithm can be converted to an iterative algorithm (using an explicit stack if necessary). Choosing between them involves balancing readability with memory and execution performance.",
        "concept": "Detailed Comparison Table:\n1. Basic Construct:\n- Recursion: Self-referential function calls with a base case.\n- Iteration: Loop structures (`for`, `while`, `do-while`) with a loop condition.\n2. Memory Overhead:\n- Recursion: High. Every call pushes an activation record (parameters, locals, return address) onto the call stack ($O(N)$ space).\n- Iteration: Minimal. Variables are modified in-place ($O(1)$ space).\n3. Execution Speed:\n- Recursion: Slower due to function call overhead, register preservation, and stack allocation.\n- Iteration: Faster; compiles to direct jumps and branch instructions.\n4. Failure Mode:\n- Recursion: Stack overflow (SIGSEGV / crash) if recursion depth is too large.\n- Iteration: Infinite loop (CPU consumption) if termination condition is never met.\n5. When to Prefer Recursion: Naturally hierarchical or branching problems (Tree traversal, Graph DFS, QuickSort, MergeSort, Tower of Hanoi).",
        "syntax": "Recursion: F(N) = N * F(N-1)\nIteration: for(int i=1; i<=N; i++) fact *= i;",
        "code": """#include <stdio.h>
#include <time.h>

/* Iterative Factorial */
unsigned long long factorialIterative(int n) {
    unsigned long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

/* Recursive Factorial */
unsigned long long factorialRecursive(int n) {
    if (n <= 1) return 1;
    return n * factorialRecursive(n - 1);
}

int main(void) {
    int n = 20;

    printf("=== Factorial: Iteration vs Recursion ===\\n");
    printf("Iterative Result: %llu (Uses O(1) stack memory)\\n", factorialIterative(n));
    printf("Recursive Result: %llu (Uses O(N) call stack frames)\\n", factorialRecursive(n));

    return 0;
}""",
        "output": """=== Factorial: Iteration vs Recursion ===
Iterative Result: 2432902008176640000 (Uses O(1) stack memory)
Recursive Result: 2432902008176640000 (Uses O(N) call stack frames)""",
        "explanation": "1. Both functions produce identical results ($20!$).\n2. The iterative version executes in fixed memory without function call overhead.\n3. The recursive version mirrors the mathematical definition at the cost of 20 stack frames.",
        "mistakes": [
            ("Using recursion for simple linear problems like array traversal.", "Using recursion to traverse an array of 1,000,000 elements creates 1,000,000 stack frames and crashes the process. Use a `for` loop."),
            ("Assuming recursion is always slower after compiler optimization.", "With tail-call optimization (`-O2`), smart compilers convert tail-recursive functions into iterative assembly loops automatically.")
        ],
        "practice_q": "What is tail-call optimization (TCO) and under what conditions can a compiler apply it?"
    },
    {
        "num": 70,
        "title": "Passing Arrays to Functions: 1D and 2D Decay to Pointers",
        "category": "Pointers & Arrays",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "Exam Level"],
        "question": "Explain array decay when passing 1D and 2D arrays to functions. Write a complete C program demonstrating how to pass 1D arrays and 2D matrices cleanly with correct parameter syntax.",
        "logic": "Arrays cannot be passed by value in C. Passing an array passes a pointer to its first element. For 1D arrays, size must be passed separately. For 2D arrays, the column dimension must be fixed in the prototype.",
        "concept": "1. 1D Array Parameter: `void process(int *arr, int size)` or `void process(int arr[], int size)`. Both are completely identical to the compiler.\n2. 2D Array Parameter: `void processMatrix(int matrix[][COLS], int rows)`. The column dimension `COLS` is mandatory so the compiler can compute the element address `i * COLS + j`.\n3. In C99 and later, Variable-Length Array (VLA) parameter syntax allows passing dynamic dimensions: `void f(int r, int c, int m[r][c]);`.",
        "syntax": "void func(int arr[], int n);\nvoid func2D(int r, int c, int m[][c]);",
        "code": """#include <stdio.h>

#define MATRIX_COLS 3

/* 1D array processor */
void doubleArrayElements(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        arr[i] *= 2; /* Modifies original array in caller */
    }
}

/* 2D matrix printer */
void displayMatrix(const int matrix[][MATRIX_COLS], int rows) {
    for (int i = 0; i < rows; i++) {
        printf("  [ ");
        for (int j = 0; j < MATRIX_COLS; j++) {
            printf("%3d ", matrix[i][j]);
        }
        printf("]\\n");
    }
}

int main(void) {
    int list[4] = {5, 10, 15, 20};

    printf("1D Array Before Doubling: ");
    for (int i = 0; i < 4; i++) printf("%d ", list[i]);
    printf("\\n");

    doubleArrayElements(list, 4);

    printf("1D Array After Doubling:  ");
    for (int i = 0; i < 4; i++) printf("%d ", list[i]);
    printf("\\n\\n");

    int grid[2][MATRIX_COLS] = {
        {1, 2, 3},
        {4, 5, 6}
    };
    printf("2D Matrix Display via Function:\\n");
    displayMatrix(grid, 2);

    return 0;
}""",
        "output": """1D Array Before Doubling: 5 10 15 20 
1D Array After Doubling:  10 20 30 40 

2D Matrix Display via Function:
  [   1   2   3 ]
  [   4   5   6 ]""",
        "explanation": "1. `doubleArrayElements` modifies `list` in `main` because `arr` points to the original array memory.\n2. `displayMatrix` declares `const int matrix[][MATRIX_COLS]`, which guarantees the function will not modify matrix contents and provides the required column dimension.",
        "mistakes": [
            ("Writing `void func(int matrix[][])` for 2D arrays.", "Compiler error: `array type has incomplete element type`. The column width must be specified."),
            ("Expecting `sizeof(arr)` inside `doubleArrayElements` to return 16.", "It returns 8 (pointer size) due to array decay.")
        ],
        "practice_q": "How can you pass a dynamically allocated 2D array of arbitrary runtime dimensions to a function in C?"
    },
    {
        "num": 71,
        "title": "Binary Search using Recursion: Algorithm and Recursive Trace",
        "category": "Recursion & Searching",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Implement the Binary Search algorithm using recursion in C. Compare its recursive call stack depth with its logarithmic time complexity $O(\\log N)$.",
        "logic": "Compute `mid = low + (high - low) / 2`. If `arr[mid] == key`, return `mid`. If `arr[mid] > key`, recurse on left half `(low, mid - 1)`. If `arr[mid] < key`, recurse on right half `(mid + 1, high)`.",
        "concept": "1. Base Cases:\n- `low > high`: Target not found, return `-1`.\n- `arr[mid] == key`: Target found, return `mid`.\n2. Stack Depth: The array size is halved with each recursive call. Maximum stack depth is $\\lceil \\log_2 N \\rceil + 1$. For an array of 1,000,000 elements, recursion depth never exceeds 21 stack frames.",
        "syntax": "int recBinarySearch(const int arr[], int low, int high, int key);",
        "code": """#include <stdio.h>

int recBinarySearch(const int arr[], int low, int high, int key, int depth) {
    if (low > high) {
        printf("  [Depth %d]: Search space exhausted (low=%d, high=%d) -> Not Found\\n", 
               depth, low, high);
        return -1; /* Base Case: Key not found */
    }

    int mid = low + (high - low) / 2;
    printf("  [Depth %d]: Checking mid=%d (Value=%d) in range [%d, %d]\\n", 
           depth, mid, arr[mid], low, high);

    if (arr[mid] == key) {
        return mid; /* Base Case: Match found */
    } else if (arr[mid] > key) {
        return recBinarySearch(arr, low, mid - 1, key, depth + 1); /* Search left */
    } else {
        return recBinarySearch(arr, mid + 1, high, key, depth + 1); /* Search right */
    }
}

int main(void) {
    int data[] = {10, 20, 30, 40, 50, 60, 70, 80};
    int n = sizeof(data) / sizeof(data[0]);

    printf("=== Recursive Binary Search Trace (Key = 70) ===\\n");
    int idx = recBinarySearch(data, 0, n - 1, 70, 1);
    printf("Result: Key 70 found at index %d\\n\\n", idx);

    printf("=== Recursive Binary Search Trace (Key = 25) ===\\n");
    int missingIdx = recBinarySearch(data, 0, n - 1, 25, 1);
    printf("Result: Key 25 search returned %d\\n", missingIdx);

    return 0;
}""",
        "output": """=== Recursive Binary Search Trace (Key = 70) ===
  [Depth 1]: Checking mid=3 (Value=40) in range [0, 7]
  [Depth 2]: Checking mid=5 (Value=60) in range [4, 7]
  [Depth 3]: Checking mid=6 (Value=70) in range [6, 7]
Result: Key 70 found at index 6

=== Recursive Binary Search Trace (Key = 25) ===
  [Depth 1]: Checking mid=3 (Value=40) in range [0, 7]
  [Depth 2]: Checking mid=1 (Value=20) in range [0, 2]
  [Depth 3]: Checking mid=2 (Value=30) in range [2, 2]
  [Depth 4]: Search space exhausted (low=2, high=1) -> Not Found
Result: Key 25 search returned -1""",
        "explanation": "1. Key 70 is found in 3 recursive steps (Depth 3).\n2. Key 25 is determined to be absent when `low > high` at Depth 4.\n3. The algorithm requires at most $\\log_2 8 = 3$ comparisons.",
        "mistakes": [
            ("Forgetting `return` before recursive calls: `recBinarySearch(..);`.", "If `return` is omitted, the function fails to propagate the found index back up the call stack, returning an undefined value to the caller."),
            ("Recursing with `high = mid` instead of `mid - 1`.", "Can cause infinite recursion when `low == high`.")
        ],
        "practice_q": "Why is the iterative version of binary search often preferred over the recursive version in embedded systems?"
    },
    {
        "num": 72,
        "title": "Void Pointers (Generic Pointers) and Type Casting Mechanics",
        "category": "Pointers",
        "difficulty": "Intermediate",
        "exam_tags": ["Viva Must-Know", "Exam Question"],
        "question": "What is a `void *` (generic pointer) in C? Can you dereference a `void *` directly? Explain why pointer type casting is mandatory and show how standard library functions use `void *`.",
        "logic": "A `void *` can hold the memory address of any data type without an explicit cast. However, because it has no associated type, the compiler does not know the data size, so dereferencing or arithmetic on `void *` is not permitted.",
        "concept": "1. Generic Pointer: Any pointer type (`int*`, `double*`, `char*`, struct pointer) can be assigned to `void*` and back without an explicit cast.\n2. Dereferencing Restriction: `*vptr` causes a compilation error (`invalid use of void expression`). You MUST cast it first: `*(int *)vptr`.\n3. Pointer Arithmetic Restriction: `vptr + 1` is illegal in standard C because `sizeof(void)` is undefined (though GCC has an extension treating `sizeof(void) == 1`).\n4. Applications: Dynamic memory allocation (`malloc()` returns `void*`), generic data structures, and memory manipulation functions (`memcpy`, `memset`).",
        "syntax": "void *genericPtr = &x;\nint val = *(int *)genericPtr;",
        "code": """#include <stdio.h>

void printGenericData(const void *dataPtr, char typeIndicator) {
    switch (typeIndicator) {
        case 'i':
            printf("Integer Value:   %d\\n", *(const int *)dataPtr);
            break;
        case 'f':
            printf("Double Value:    %.2f\\n", *(const double *)dataPtr);
            break;
        case 'c':
            printf("Character Value: '%c'\\n", *(const char *)dataPtr);
            break;
        default:
            printf("Unknown type indicator\\n");
            break;
    }
}

int main(void) {
    int num = 1024;
    double pi = 3.14159;
    char letter = 'Z';

    printf("=== Generic Function with void* ===\\n");
    printGenericData(&num, 'i');
    printGenericData(&pi, 'f');
    printGenericData(&letter, 'c');

    return 0;
}""",
        "output": """=== Generic Function with void* ===
Integer Value:   1024
Double Value:    3.14
Character Value: 'Z'""",
        "explanation": "1. `printGenericData` takes a `const void *`, accepting addresses of any data type.\n2. Inside the switch, the pointer is cast to the appropriate type (`(const int *)`, etc.) before dereferencing.\n3. This demonstrates how generic functions operate in C without templates.",
        "mistakes": [
            ("Attempting direct dereference: `printf(\"%d\", *dataPtr)`.", "Compilation error: ISO C forbids dereferencing pointers to void."),
            ("Casting to the wrong data type (e.g. casting an `int*` to `double*`).", "Reads adjacent memory bytes, producing nonsensical values or alignment faults.")
        ],
        "practice_q": "Why does `malloc()` in C not require an explicit cast like `(int *)malloc(...)`?"
    },
    {
        "num": 73,
        "title": "Pointers to Strings: String Pointers vs Character Arrays",
        "category": "Pointers & Strings",
        "difficulty": "Intermediate",
        "exam_tags": ["Interview Trap", "Viva Question"],
        "question": "Compare `char str[] = \"Hello\";` with `char *ptr = \"Hello\";`. Explain mutability, memory allocation regions, and why modifying a string literal causes a Segmentation Fault.",
        "logic": "`char str[]` allocates an array on the stack and copies the characters into it (mutable). `char *ptr` points directly to the string literal stored in read-only memory (immutable).",
        "concept": "Comparison:\n1. `char str[] = \"Hello\";`\n- Memory: Stack segment\n- Mutability: Mutable. `str[0] = 'M'` is valid and changes string to \"Mello\".\n- Pointer Reassignment: `str = other` is ILLEGAL (array name is a pointer constant).\n2. `char *ptr = \"Hello\";`\n- Memory: Pointer is on stack; literal is in `.rodata` (Read-Only Data Segment).\n- Mutability: Immutable. `ptr[0] = 'M'` causes Segmentation Fault (SIGSEGV)!\n- Pointer Reassignment: `ptr = \"World\"` is valid.\nBest Practice: Always declare string literal pointers with `const`: `const char *ptr = \"Hello\";` to catch accidental write attempts at compile time.",
        "syntax": "char mutableArr[] = \"text\";\nconst char *immutablePtr = \"text\";",
        "code": """#include <stdio.h>

int main(void) {
    /* 1. Mutable Character Array on Stack */
    char stackStr[] = "Hello";
    printf("Initial stackStr: %s\\n", stackStr);
    stackStr[0] = 'J'; /* Valid: modifies stack memory */
    printf("Modified stackStr: %s\\n\\n", stackStr);

    /* 2. Pointer to String Literal in Read-Only Data */
    const char *rodataPtr = "World";
    printf("rodataPtr: %s\\n", rodataPtr);
    rodataPtr = "Universe"; /* Valid: redirecting pointer */
    printf("Redirected rodataPtr: %s\\n", rodataPtr);

    /* rodataPtr[0] = 'W'; -> Compile Error with const! (Crash without const) */

    return 0;
}""",
        "output": """Initial stackStr: Hello
Modified stackStr: Jello

rodataPtr: World
Redirected rodataPtr: Universe""",
        "explanation": "1. `stackStr` resides on the stack, allowing in-place modification of `'H'` to `'J'`.\n2. `rodataPtr` points to read-only memory. Reassigning the pointer to `\"Universe\"` works, but modifying the string data itself is prohibited.\n3. Using `const` catches modification attempts at compile time.",
        "mistakes": [
            ("Writing `char *s = \"vtu\"; s[0] = 'V';` without `const`.", "Compiles without error on older standards, but crashes with a runtime Segmentation Fault when executed."),
            ("Assuming `sizeof(stackStr)` and `sizeof(rodataPtr)` are equal.", "`sizeof(stackStr)` is 6 bytes. `sizeof(rodataPtr)` is 8 bytes (pointer size).")
        ],
        "practice_q": "Where in program memory is the string literal `\"Hello\"` stored in a compiled binary?"
    },
    {
        "num": 74,
        "title": "Output Prediction: Dangling Pointers from Returning Local Stack Addresses",
        "category": "Debugging & Tracing",
        "difficulty": "Exam-Level",
        "exam_tags": ["Interview Trap", "Viva Must-Know"],
        "question": "What is wrong with the following C function and why is it dangerous: `int *getLocalAddress(void) { int x = 10; return &x; }`? Explain the concept of a Dangling Pointer.",
        "logic": "Local variables allocated on the stack are deallocated when the function returns. Returning the address of a local variable returns a pointer to memory that no longer belongs to that variable (a dangling pointer).",
        "concept": "1. Lifetime Violation: The lifetime of `int x` ends as soon as `getLocalAddress()` returns and its stack frame is popped.\n2. Dangling Pointer: A pointer holding the memory address of an object that has already been deallocated.\n3. Undefined Behavior: Accessing `*danglingPtr` might appear to work initially, but subsequent function calls will overwrite that stack space, corrupting the value.\n4. Solutions:\n- Pass a pointer from caller as an argument.\n- Allocate on heap using `malloc()`.\n- Declare the local variable as `static` (persists for the entire program).",
        "syntax": "static int x = 10; return &x; /* Safe */",
        "code": """#include <stdio.h>

/* Safe Solution 1: Static Variable (Persists in data segment) */
int *getSafeStaticAddress(void) {
    static int persistentVar = 42;
    return &persistentVar; /* Safe: lifetime is entire program */
}

/* Safe Solution 2: Caller-Provided Buffer */
void fillCallerBuffer(int *outVal) {
    *outVal = 99; /* Writes into caller's stack frame */
}

int main(void) {
    int *p1 = getSafeStaticAddress();
    printf("Safe Static Access:  *p1 = %d\\n", *p1);

    int callerVar = 0;
    fillCallerBuffer(&callerVar);
    printf("Caller-Buffer Access: callerVar = %d\\n", callerVar);

    return 0;
}""",
        "output": """Safe Static Access:  *p1 = 42
Caller-Buffer Access: callerVar = 99""",
        "explanation": "1. `persistentVar` is declared `static`, placing it in the data segment where it remains valid for the duration of the program.\n2. `fillCallerBuffer` receives a pointer to memory allocated in `main`'s stack frame, which remains valid throughout the call.",
        "mistakes": [
            ("Returning pointer to local array: `char *f() { char s[] = \"hi\"; return s; }`.", "The local array `s` is deallocated on return, causing immediate stack memory corruption on the caller side."),
            ("Ignoring compiler warnings: `function returns address of local variable`.", "This warning always indicates a severe bug. Never ignore it.")
        ],
        "practice_q": "How does `malloc()` allow a function to safely return a newly created array or object to its caller?"
    },
    {
        "num": 75,
        "title": "Output Prediction & Debugging: Uninitialized Pointer Dereferencing",
        "category": "Debugging & Tracing",
        "difficulty": "Exam-Level",
        "exam_tags": ["Viva Trap", "Bug Hunting"],
        "question": "Predict the runtime behavior and diagnose the defect in: `int *ptr; *ptr = 50; printf(\"%d\", *ptr);`. Explain wild pointers and how to neutralize them.",
        "logic": "The pointer `ptr` is an uninitialized local variable (a wild pointer). It contains an indeterminate garbage address. Dereferencing `*ptr = 50` attempts to write integer 50 to an arbitrary memory address, causing an immediate Segmentation Fault.",
        "concept": "1. Wild Pointer: A pointer that has been declared but not initialized to any valid memory address or `NULL`.\n2. In protected operating systems (Windows, Linux), attempting to write to unauthorized memory addresses triggers a hardware memory protection fault (SIGSEGV).\n3. Defense Strategy:\n- Always initialize pointers upon declaration: `int *ptr = NULL;`\n- Check for `NULL` before dereferencing: `if (ptr != NULL) *ptr = 50;`\n- Assign valid memory before dereferencing: `int val; int *ptr = &val;`.",
        "syntax": "int *ptr = NULL;\nif (ptr != NULL) { ... }",
        "code": """#include <stdio.h>

int main(void) {
    /* 1. Safe pointer initialization */
    int *safePtr = NULL;

    printf("=== Safe Pointer Defensive Check ===\\n");
    if (safePtr == NULL) {
        printf("safePtr is NULL: Access safely prevented! (No segmentation fault)\\n");
    }

    /* 2. Properly bounded assignment */
    int target = 0;
    safePtr = &target;

    if (safePtr != NULL) {
        *safePtr = 50;
        printf("safePtr now points to 'target': *safePtr = %d\\n", *safePtr);
    }

    return 0;
}""",
        "output": """=== Safe Pointer Defensive Check ===
safePtr is NULL: Access safely prevented! (No segmentation fault)
safePtr now points to 'target': *safePtr = 50""",
        "explanation": "1. `safePtr` is initialized to `NULL` (address 0).\n2. The defensive check `if (safePtr == NULL)` catches the unassigned state, preventing a crash.\n3. Once assigned `&target`, dereferencing `*safePtr = 50` safely updates `target` to 50.",
        "mistakes": [
            ("Assuming `int *ptr;` points to address 0 automatically.", "Local variables in C contain random stack garbage. It does NOT automatically equal `NULL` unless explicitly assigned."),
            ("Dereferencing `NULL` directly: `int *p = NULL; *p = 5;`.", "Dereferencing `NULL` causes an instant crash on all modern operating systems.")
        ],
        "practice_q": "What tools or compiler flags help detect wild pointer dereferencing during development?"
    },
    {
        "num": 76,
        "title": "Module 3 Mastery: Comprehensive Functions, Pointers, and Recursion Diagnostic",
        "category": "Comprehensive Review",
        "difficulty": "Exam-Level",
        "exam_tags": ["Viva Must-Know", "Final Exam Checklist"],
        "question": "Provide a comprehensive diagnostic review of the top 5 pointer and recursion exam traps: Array decay, Call by Value misconceptions, Dangling pointers, Base case omission, and Pointer operator precedence.",
        "logic": "Consolidates all critical rules and concepts from Module 3 into a quick-reference review checklist.",
        "concept": "Top 5 Pitfalls in Module 3:\n1. Array decay: Forgetting that arrays decay to pointers inside functions.\n2. Call by value: Expecting a function to modify caller variables without passing pointers.\n3. Dangling pointer: Returning the address of a local stack variable.\n4. Missing base case: Forgetting the stopping condition in recursive functions, causing stack overflow.\n5. Precedence: Confusing `*ptr++` (increments pointer) with `(*ptr)++` (increments the value pointed to).",
        "syntax": "*ptr++ vs (*ptr)++ vs *(ptr++)",
        "code": """#include <stdio.h>

int main(void) {
    int arr[] = {10, 20, 30};
    int *p1 = arr;
    int *p2 = arr;

    printf("=== Pointer Increment Precedence Trap ===\\n");
    printf("Initial: arr[0] = %d, arr[1] = %d\\n\\n", arr[0], arr[1]);

    /* Test 1: *p1++ -> fetches *p1, then increments pointer p1 */
    int val1 = *p1++;
    printf("*p1++ evaluated to: %d | p1 now points to value: %d\\n", val1, *p1);

    /* Test 2: (*p2)++ -> fetches *p2, then increments the VALUE in memory */
    int val2 = (*p2)++;
    printf("(*p2)++ evaluated to: %d | arr[0] in memory is now: %d\\n", val2, arr[0]);

    return 0;
}""",
        "output": """=== Pointer Increment Precedence Trap ===
Initial: arr[0] = 10, arr[1] = 20

*p1++ evaluated to: 10 | p1 now points to value: 20
(*p2)++ evaluated to: 10 | arr[0] in memory is now: 11""",
        "explanation": "1. In `*p1++`, postfix `++` has higher precedence than `*`. It evaluates to `*p1` (10), then increments `p1` to point to `arr[1]` (20).\n2. In `(*p2)++`, parentheses force `*p2` to be evaluated first, incrementing the integer value at `arr[0]` from 10 to 11 in memory.\n3. This is one of the most common pointer syntax questions in technical interviews.",
        "mistakes": [
            ("Writing `*ptr++` when intending to increment the value.", "Parentheses are mandatory: `(*ptr)++` increments the value; `*ptr++` increments the pointer address."),
            ("Assuming `sizeof` inside a recursive function reflects total recursion depth.", "`sizeof` is a compile-time operator that only measures static type sizes.")
        ],
        "practice_q": "What does `*++ptr` evaluate to?"
    }
,
    {
        "num": 77,
        "title": "Direct vs Indirect (Mutual) Recursion: Even/Odd Numbers Verification",
        "category": "Recursion Types",
        "difficulty": "Intermediate",
        "exam_tags": ["Viva Question", "Core Concept"],
        "question": "Differentiate between Direct and Indirect (Mutual) Recursion. Implement mutually recursive functions isEven() and isOdd() in C.",
        "logic": "Direct recursion occurs when function A calls A. Indirect (mutual) recursion occurs when function A calls B, and function B calls A, forming a cycle of calls.",
        "concept": "1. Direct Recursion: A -> A -> A.\n2. Indirect Recursion: A -> B -> A -> B.\n3. Requires function prototype declarations so both functions know about each other before definition.\n4. Termination: Both functions must have base cases to prevent mutual infinite recursion.",
        "syntax": "int isEven(int n); int isOdd(int n);",
        "code": """#include <stdio.h>

int isOdd(int n); /* Prototype required for mutual recursion */

int isEven(int n) {
    if (n == 0) return 1; /* Base Case: 0 is even */
    return isOdd(n - 1);  /* Mutual call to isOdd */
}

int isOdd(int n) {
    if (n == 0) return 0;  /* Base Case: 0 is not odd */
    return isEven(n - 1); /* Mutual call to isEven */
}

int main(void) {
    int testNums[] = {0, 7, 12, 19, 42};
    printf("=== Mutual (Indirect) Recursion Demo ===\n");
    for (int i = 0; i < 5; i++) {
        int val = testNums[i];
        printf("Number %2d is %s\n", val, isEven(val) ? "EVEN" : "ODD");
    }
    return 0;
}""",
        "output": """=== Mutual (Indirect) Recursion Demo ===
Number  0 is EVEN
Number  7 is ODD
Number 12 is EVEN
Number 19 is ODD
Number 42 is EVEN""",
        "explanation": "1. isEven(7) calls isOdd(6) -> isEven(5) -> isOdd(4) -> isEven(3) -> isOdd(2) -> isEven(1) -> isOdd(0) which returns 0 (false).\n2. Shows how mutual recursion operates with mutual base conditions.",
        "mistakes": [
            ("Omitting the forward prototype declaration of the second function.", "In mutual recursion, one function must be called before its definition. Without a prototype, compilation fails."),
            ("Failing to decrement n.", "Both mutual functions must decrement or converge toward the base case.")
        ],
        "practice_q": "How can mutual recursion be used to parse alternating grammar tokens in a compiler?"
    },
    {
        "num": 78,
        "title": "Generic Sorting with qsort() and Custom Comparator Function Pointers",
        "category": "Function Pointers",
        "difficulty": "Exam-Level",
        "exam_tags": ["High Yield Exam", "Viva Must-Know"],
        "question": "Explain the standard library qsort() function from <stdlib.h>. Detail the comparator prototype int (*compare)(const void*, const void*) and write a complete C program sorting integers in ascending and descending order.",
        "logic": "qsort() is a generic quicksort function. It takes base address, element count, element size, and a comparison function pointer that defines sort order.",
        "concept": "1. Prototype: void qsort(void *base, size_t nitems, size_t size, int (*compar)(const void *, const void *));\n2. Comparator Rules:\n- Return < 0 if first element should precede second.\n- Return 0 if both elements are equal.\n- Return > 0 if first element should follow second.\n3. Typecasting void pointers: const int *a = (const int *)p1; int diff = *a - *b;",
        "syntax": "int compareAsc(const void *a, const void *b) { return (*(int*)a - *(int*)b); }",
        "code": """#include <stdio.h>
#include <stdlib.h>

int compareAsc(const void *a, const void *b) {
    return (*(const int *)a - *(const int *)b);
}

int compareDesc(const void *a, const void *b) {
    return (*(const int *)b - *(const int *)a);
}

int main(void) {
    int data[] = {45, 12, 89, 7, 63, 28};
    int n = sizeof(data) / sizeof(data[0]);

    printf("Original:   ");
    for (int i = 0; i < n; i++) printf("%d ", data[i]);
    printf("\n");

    qsort(data, n, sizeof(int), compareAsc);
    printf("Ascending:  ");
    for (int i = 0; i < n; i++) printf("%d ", data[i]);
    printf("\n");

    qsort(data, n, sizeof(int), compareDesc);
    printf("Descending: ");
    for (int i = 0; i < n; i++) printf("%d ", data[i]);
    printf("\n");

    return 0;
}""",
        "output": """Original:   45 12 89 7 63 28 
Ascending:  7 12 28 45 63 89 
Descending: 89 63 45 28 12 7 """,
        "explanation": "1. qsort works generically on any data type through void* comparator callbacks.\n2. compareAsc sorts in ascending order.\n3. compareDesc inverts comparison order to sort descending.",
        "mistakes": [
            ("Integer overflow in subtraction: return (*a - *b); when numbers are very large and opposite signs.", "If a is large positive and b is large negative, subtraction overflows. Safe comparison: if (*a > *b) return 1; if (*a < *b) return -1; else return 0;"),
            ("Dereferencing void pointers without casting.", "Void pointers must be cast to concrete type pointers before dereferencing.")
        ],
        "practice_q": "Write a comparator for qsort to sort an array of strings alphabetically."
    }
]

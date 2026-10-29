# -*- coding: utf-8 -*-
"""
C Programming - Module 1: C Fundamentals and Control Statements
Questions 1 to 26 (Fundamental Concepts, Operators, I/O, Decision Making, Loops, and Control Statements)
"""

C_MODULE1_QUESTIONS = [
    {
        "num": 1,
        "title": "History, Features, and Architecture of C Language",
        "category": "Concepts & History",
        "difficulty": "Fundamental",
        "exam_tags": ["VTU Exam Favorite", "Viva Must-Know"],
        "question": "Discuss the evolution of C language. Why is C referred to as a 'middle-level programming language'? State its key characteristics and modern real-world applications.",
        "logic": "C was developed by Dennis Ritchie at Bell Labs in 1972 from B and BCPL. It bridges the gap between low-level assembly language and high-level abstract languages.",
        "concept": "C is termed 'middle-level' because it combines the power, hardware control, and memory manipulation capabilities of assembly language (via pointers and bitwise operators) with the user-friendliness, modularity, and structured syntax of high-level languages.",
        "syntax": "Dennis Ritchie (1972) -> K&R C (1978) -> ANSI C / C89 -> C99 -> C11 -> C17/C23.",
        "code": """#include <stdio.h>

/* Demonstration of C's low-level access & high-level abstraction */
int main(void) {
    int number = 42;
    int *ptr = &number; /* Low-level memory address manipulation */

    printf("High-Level Abstraction: Value = %d\\n", number);
    printf("Low-Level Memory Access: Address = %p\\n", (void*)ptr);
    printf("Bitwise Hardware Control: 42 << 1 = %d\\n", number << 1);

    return 0;
}""",
        "output": """High-Level Abstraction: Value = 42
Low-Level Memory Access: Address = 0x7ffd5b68acbc
Bitwise Hardware Control: 42 << 1 = 84""",
        "explanation": "1. In this program, `number` demonstrates high-level data encapsulation.\n2. `int *ptr = &number` demonstrates direct physical RAM address referencing, typical of low-level languages.\n3. The bitwise left shift `number << 1` demonstrates micro-level ALU manipulation, executing in a single CPU cycle.",
        "mistakes": [
            ("Calling C an Object-Oriented Language.", "C is purely a procedural/structured language. It lacks classes, inheritance, and polymorphism."),
            ("Assuming 'middle-level' means mediocre performance.", "Middle-level means it has both low-level hardware control and high-level constructs; it is one of the fastest languages in existence.")
        ],
        "practice_q": "List 5 major operating systems and embedded engines written primarily in C."
    },
    {
        "num": 2,
        "title": "Structure of a C Program & Compilation Stages",
        "category": "Architecture & Build",
        "difficulty": "Fundamental",
        "exam_tags": ["High Yield Exam Question", "Viva Favorite"],
        "question": "Explain the standard anatomy/structure of a C program. Describe the four distinct phases of C compilation and execution (Preprocessing, Compiling, Assembling, and Linking).",
        "logic": "A C program follows a well-defined sequence: Documentation, Link section (#include), Definition section (#define), Global declarations, `main()` function, and Subprograms.",
        "concept": "Source code (.c) undergoes 4 stages:\n1. Preprocessing (gcc -E): Removes comments, expands macros, includes header files -> .i file.\n2. Compilation (gcc -S): Translates preprocessed C code into assembly instructions -> .s file.\n3. Assembly (gcc -c): Converts assembly code into machine-readable object code -> .o or .obj file.\n4. Linking (gcc): Merges object files with library functions (e.g., libc.a, printf code) -> Executable (.exe or a.out).",
        "syntax": "gcc -Wall -o output program.c\nStage 1: cpp (preprocessor) -> Stage 2: cc1 (compiler) -> Stage 3: as (assembler) -> Stage 4: ld (linker).",
        "code": """#include <stdio.h>

#define PI 3.14159265359 /* Preprocessor symbolic constant */

/* Function Prototype */
double calculateCircleArea(double radius);

/* Main Entry Point */
int main(void) {
    double radius = 7.0;
    double area = calculateCircleArea(radius);

    printf("Radius: %.2f units\\n", radius);
    printf("Area:   %.4f sq. units\\n", area);

    return 0; /* Exit code 0 indicates normal termination */
}

/* Subprogram Definition */
double calculateCircleArea(double r) {
    return PI * r * r;
}""",
        "output": """Radius: 7.00 units
Area:   153.9380 sq. units""",
        "explanation": "1. `#include <stdio.h>` directs the preprocessor to paste standard input/output prototypes.\n2. `#define PI` is an object-like macro replaced textually before syntax analysis.\n3. `main()` returns an integer exit status to the operating system shell (0 = success, non-zero = error).\n4. Linker resolves the external call to `printf` against `libc`.",
        "mistakes": [
            ("Thinking the compiler directly creates the .exe file.", "The compiler only produces assembly code; the assembler and linker are necessary to create the executable."),
            ("Using `void main()` in standard C programs.", "ISO C standards require `int main(void)` or `int main(int argc, char *argv[])` returning an integer.")
        ],
        "practice_q": "What command-line flags in GCC allow you to stop compilation after the preprocessing stage and after the assembly stage?"
    },
    {
        "num": 3,
        "title": "Tokens, Keywords, Identifiers, and Reserved Rules",
        "category": "C Tokens",
        "difficulty": "Fundamental",
        "exam_tags": ["Viva Favorite", "Exam Question"],
        "question": "What is a C token? Differentiate between keywords and identifiers. State all the syntactic rules governing the creation of valid identifiers in C.",
        "logic": "Tokens are the smallest individual building blocks of a C program. There are 6 types: Keywords, Identifiers, Constants, Strings, Special Symbols, and Operators.",
        "concept": "1. Keywords: 32 reserved words in C89 (44 in C99/C11) that possess special, predefined meanings to the compiler (e.g., `int`, `return`, `volatile`). They cannot be used as variable names.\n2. Identifiers: User-defined names given to variables, functions, arrays, and labels.\nRules:\n- Must begin with an alphabet (A-Z, a-z) or an underscore (`_`).\n- Followed by alphabets, digits (0-9), or underscores.\n- No special characters or spaces permitted (`$`, `@`, `#`, ` `).\n- C is case-sensitive (`Total`, `total`, and `TOTAL` are 3 distinct identifiers).\n- Keywords cannot be used as identifiers.",
        "syntax": "valid: total_sum, _counter, student12, MAX_VAL\ninvalid: 2ndValue, total sum, int, tax-rate, price$card",
        "code": """#include <stdio.h>

int main(void) {
    /* Valid Identifiers */
    int _studentCount = 65;
    double marks_percentage = 88.5;
    int rollNo01 = 101;

    printf("Roll No: %d | Count: %d | Marks: %.1f%%\\n", 
           rollNo01, _studentCount, marks_percentage);

    return 0;
}""",
        "output": """Roll No: 101 | Count: 65 | Marks: 88.5%""",
        "explanation": "1. `_studentCount` starts with an underscore, which is valid.\n2. `marks_percentage` uses underscore as word separator.\n3. `rollNo01` contains alphanumeric characters where digits appear after the leading letter.",
        "mistakes": [
            ("Starting an identifier with a digit (e.g. `1count`).", "Identifiers must begin strictly with a letter or underscore."),
            ("Assuming uppercase and lowercase identifiers are identical.", "C is strictly case-sensitive: `num` and `Num` are completely different memory locations.")
        ],
        "practice_q": "Identify which of the following are invalid identifiers and why: `switch`, `_99`, `avg-marks`, `float_val`, `return_code`, `3rd_year`."
    },
    {
        "num": 4,
        "title": "Data Types, Modifiers, and Memory Sizes with sizeof()",
        "category": "Data Representation",
        "difficulty": "Fundamental",
        "exam_tags": ["Viva Must-Know", "Core Foundation"],
        "question": "Categorize primitive data types in C. Explain type qualifiers (`short`, `long`, `signed`, `unsigned`) and demonstrate memory footprint using `sizeof`.",
        "logic": "C data types are categorized into: Basic/Primitive (`char`, `int`, `float`, `double`), Derived (arrays, pointers, functions), Enumeration (`enum`), and User-defined (`struct`, `union`, `void`).",
        "concept": "Type modifiers alter the range or size of basic types:\n- `signed`: Allows positive and negative values (default for `int`).\n- `unsigned`: Only non-negative values; doubles positive range ($0$ to $2^n-1$).\n- `short`: Reduces memory size (at least 16 bits).\n- `long`: Increases memory size (at least 32 or 64 bits).\n- `sizeof`: Compile-time unary operator returning size in bytes as `size_t`.",
        "syntax": "sizeof(type) or sizeof(expression)",
        "code": """#include <stdio.h>

int main(void) {
    printf("--- C Primitive Data Type Footprints ---\\n");
    printf("char:               %2zu byte(s)  [Range: %d to %d]\\n", sizeof(char), -128, 127);
    printf("unsigned char:      %2zu byte(s)  [Range: 0 to %u]\\n", sizeof(unsigned char), 255);
    printf("short int:          %2zu bytes    [Range: -32,768 to 32,767]\\n", sizeof(short));
    printf("int:                %2zu bytes    [Standard 32-bit Integer]\\n", sizeof(int));
    printf("unsigned int:       %2zu bytes    [0 to 4,294,967,295]\\n", sizeof(unsigned int));
    printf("long int:           %2zu bytes\\n", sizeof(long));
    printf("long long int:      %2zu bytes\\n", sizeof(long long));
    printf("float (single-prec):%2zu bytes    [~6-7 decimal digits]\\n", sizeof(float));
    printf("double (double-prec):%zu bytes   [~15-17 decimal digits]\\n", sizeof(double));
    printf("long double:        %2zu bytes\\n", sizeof(long double));

    return 0;
}""",
        "output": """--- C Primitive Data Type Footprints ---
char:                1 byte(s)  [Range: -128 to 127]
unsigned char:       1 byte(s)  [Range: 0 to 255]
short int:           2 bytes    [Range: -32,768 to 32,767]
int:                 4 bytes    [Standard 32-bit Integer]
unsigned int:        4 bytes    [0 to 4,294,967,295]
long int:            4 bytes
long long int:       8 bytes
float (single-prec): 4 bytes    [~6-7 decimal digits]
double (double-prec):8 bytes   [~15-17 decimal digits]
long double:        16 bytes""",
        "explanation": "1. `sizeof` is evaluated at compile time, not runtime.\n2. On modern 32/64-bit systems, `int` is typically 4 bytes (32 bits).\n3. `unsigned` data types never store negative numbers, utilizing the sign bit to double the positive capacity.",
        "mistakes": [
            ("Assuming `sizeof` is a function.", "`sizeof` is a compile-time operator. Parentheses are optional for variable names: `sizeof x` is valid."),
            ("Using `%d` instead of `%zu` for `sizeof` output.", "`sizeof` returns type `size_t`, which requires the `%zu` format specifier according to C99 standard.")
        ],
        "practice_q": "What happens when you assign -1 to an `unsigned int` variable in C?"
    },
    {
        "num": 5,
        "title": "Constants, Literals, and const vs #define",
        "category": "Variables & Storage",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Theory", "Viva Question"],
        "question": "What are constants in C? Differentiate between integer, floating-point, character, and string literals. Provide a rigorous comparison between `const` keyword and `#define` preprocessor directive.",
        "logic": "Constants are values that cannot be altered during program execution. They can be created using literal notation, the `const` type qualifier, or `#define`.",
        "concept": "1. `#define MACRO value`:\n- Handled by preprocessor via textual search-and-replace.\n- Has no data type (no type safety).\n- Consumes no RAM storage in data segment.\n- Has global file scope from point of definition.\n2. `const type var = value`:\n- Handled by compiler with strict type verification.\n- Has a definite data type and respects scope rules (block/local).\n- Can be inspected in a debugger.\n- Stored in read-only data segment (`.rodata`).",
        "syntax": "#define MAX_USERS 100\nconst int MaxUsers = 100;",
        "code": """#include <stdio.h>

#define TAX_RATE_MACRO 0.18
const double TAX_RATE_CONST = 0.18;

int main(void) {
    double itemPrice = 1500.0;
    
    double tax1 = itemPrice * TAX_RATE_MACRO;
    double tax2 = itemPrice * TAX_RATE_CONST;

    printf("Item Base Price: %.2f INR\\n", itemPrice);
    printf("Tax via #define: %.2f INR\\n", tax1);
    printf("Tax via const:   %.2f INR\\n", tax2);

    /* TAX_RATE_CONST = 0.20; -> Compilation Error: assignment of read-only variable */

    return 0;
}""",
        "output": """Item Base Price: 1500.00 INR
Tax via #define: 270.00 INR
Tax via const:   270.00 INR""",
        "explanation": "1. `TAX_RATE_MACRO` is replaced textually before syntax analysis occurs.\n2. `TAX_RATE_CONST` creates a read-only variable with double precision type checking enforced by the compiler.\n3. Attempting to assign a new value to `TAX_RATE_CONST` triggers a compile-time error.",
        "mistakes": [
            ("Adding a semicolon at the end of `#define` (e.g., `#define MAX 100;`).", "The semicolon becomes part of the replacement text, causing severe syntax errors during expression evaluation."),
            ("Assuming `const` pointers cannot have their pointee modified.", "Syntax matters: `const int *p` protects the target value; `int * const p` protects the pointer address.")
        ],
        "practice_q": "Demonstrate the syntax for an octal literal and a hexadecimal literal in C."
    },
    {
        "num": 6,
        "title": "Format Specifiers, Modifiers, and Escape Sequences",
        "category": "I/O System",
        "difficulty": "Fundamental",
        "exam_tags": ["Core I/O", "Viva Question"],
        "question": "Explain format specifiers and width/precision field modifiers in `printf()`. Tabulate key escape sequences with their visual effects.",
        "logic": "Format specifiers inform `printf` and `scanf` how to interpret the binary bits of variables. Escape sequences represent non-printable control characters.",
        "concept": "Key Specifiers:\n- `%d` / `%i`: Signed decimal integer\n- `%u`: Unsigned integer\n- `%f`: Float (standard decimal)\n- `%lf`: Double\n- `%c`: Single character\n- `%s`: Null-terminated string\n- `%p`: Pointer address in hex\n- `%x` / `%X`: Lowercase/Uppercase Hexadecimal\n- `%o`: Octal\n- `%e` / `%E`: Scientific exponential notation\nModifiers:\n- `%10d`: Minimum field width 10 (right-aligned)\n- `%-10d`: Left-aligned in 10-char field\n- `%.2f`: Float rounded to 2 decimal places\nEscape sequences: `\\n` (newline), `\\t` (horizontal tab), `\\\\` (backslash), `\\\"` (quote), `\\a` (alert beep), `\\r` (carriage return).",
        "syntax": "%[flags][width][.precision][length]specifier",
        "code": """#include <stdio.h>

int main(void) {
    int id = 7;
    char name[] = "Algorithm";
    double score = 94.6789;

    printf("======================================\\n");
    printf("| %-6s | %-12s | %-8s |\\n", "ID", "SUBJECT", "SCORE");
    printf("======================================\\n");
    printf("| %06d | %-12s | %8.2f |\\n", id, name, score);
    printf("======================================\\n");

    /* Escape sequence demonstration */
    printf("First Line\\nSecond Line with tab:\\t[TAB]\\n");
    printf("Displaying quotes: \\\"Hello, C!\\\" and backslash: \\\\\\n");

    return 0;
}""",
        "output": """======================================
| ID     | SUBJECT      | SCORE    |
======================================
| 000007 | Algorithm    |    94.68 |
======================================
First Line
Second Line with tab:	[TAB]
Displaying quotes: "Hello, C!" and backslash: \\""",
        "explanation": "1. `%-12s` prints a string left-justified within a 12-character space.\n2. `%06d` zero-pads the integer `7` to 6 digits (`000007`).\n3. `%8.2f` rounds `94.6789` to 2 decimal places (`94.68`) right-aligned in 8 spaces.",
        "mistakes": [
            ("Using `%f` in `scanf()` to read a `double`.", "In `scanf()`, you MUST use `%lf` for `double` and `%f` for `float`. Using `%f` for double leads to memory corruption."),
            ("Forgetting `&` in `scanf` for non-pointer types.", "`scanf` requires addresses to store user input. Omitting `&` causes segmentation faults.")
        ],
        "practice_q": "What will `printf(\"%%d\", 10);` output on the console?"
    },
    {
        "num": 7,
        "title": "Arithmetic Operators, Integer Division, and Type Casting",
        "category": "Operators & Expressions",
        "difficulty": "Fundamental",
        "exam_tags": ["Common Pitfall", "Exam Level"],
        "question": "Explain arithmetic operators in C. Discuss the integer division trap (`5 / 2 = 2`) and demonstrate both implicit type conversion (promotion) and explicit type casting.",
        "logic": "Arithmetic operators include `+`, `-`, `*`, `/`, and `%` (modulus). When both operands of `/` are integers, C truncates the fractional portion.",
        "concept": "1. Integer Division: In integer arithmetic, `a / b` discards any remainder. For example, `7 / 2` evaluates to integer `3`, not `3.5`.\n2. Modulus Operator `%`: Computes the remainder. Operands must be integers; floating-point modulus requires `fmod()` from `<math.h>`.\n3. Implicit Promotion: When operands differ in types, C promotes the smaller type to the larger type (e.g., `int` + `double` becomes `double`).\n4. Explicit Casting: Syntax `(target_type)expression` instructs compiler to temporarily treat the variable as another type.",
        "syntax": "(type)value\ne.g., (double)5 / 2",
        "code": """#include <stdio.h>

int main(void) {
    int a = 7, b = 2;

    int intResult = a / b;                /* Integer division trap: 3 */
    double floatResultWrong = a / b;       /* Still 3.0 because division completes first! */
    double floatResultRight = (double)a / b; /* 3.5 via explicit type cast */

    printf("Given: a = %d, b = %d\\n", a, b);
    printf("Integer Division (a / b):        %d\\n", intResult);
    printf("Uncasted Assignment (double = a/b): %.4f (Truncated!)\\n", floatResultWrong);
    printf("Explicit Cast ((double)a / b):   %.4f (Accurate!)\\n", floatResultRight);
    printf("Modulus Operator (a %% b):        %d\\n", a % b);

    return 0;
}""",
        "output": """Given: a = 7, b = 2
Integer Division (a / b):        3
Uncasted Assignment (double = a/b): 3.0000 (Truncated!)
Explicit Cast ((double)a / b):   3.5000 (Accurate!)
Modulus Operator (a % b):        1""",
        "explanation": "1. In `a / b`, both `a` and `b` are `int`, so the CPU performs an integer division producing `3`.\n2. Assigning that `3` to a `double` merely converts integer `3` to `3.0000`.\n3. In `(double)a / b`, `a` is explicitly cast to `7.0`, causing `b` to be implicitly promoted to `2.0`, producing `3.5000`.",
        "mistakes": [
            ("Writing `(double)(a / b)` expecting 3.5.", "The parentheses force `a / b` to evaluate first (yielding 3), and casting 3 to double still yields 3.0. Cast the operand: `(double)a / b`."),
            ("Using `%` on floating-point numbers (`5.5 % 2`).", "The `%` operator strictly requires integer operands. Use `fmod(5.5, 2.0)` for floats.")
        ],
        "practice_q": "What is the result of `-17 % 5` and `17 % -5` in C99 standard?"
    },
    {
        "num": 8,
        "title": "Relational, Logical Operators, and Short-Circuit Evaluation",
        "category": "Operators & Expressions",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Level", "Output Tracing Favorite"],
        "question": "Detail relational (`==`, `!=`, `<`, `>`, `<=`, `>=`) and logical (`&&`, `||`, `!`) operators. Explain the critical concept of short-circuit evaluation with code demonstration.",
        "logic": "Relational operators compare values and return integer `1` (true) or `0` (false). Logical operators combine boolean conditions.",
        "concept": "Short-Circuit Evaluation:\n- Logical AND (`&&`): If the left operand evaluates to `0` (false), the entire expression MUST be false. Therefore, the right operand is NEVER evaluated.\n- Logical OR (`||`): If the left operand evaluates to non-zero (true), the entire expression MUST be true. Therefore, the right operand is NEVER evaluated.\nThis behavior is crucial for preventing null-pointer dereferences and division-by-zero errors.",
        "syntax": "condition1 && condition2\ncondition1 || condition2\n!condition",
        "code": """#include <stdio.h>

int main(void) {
    int x = 0;
    int y = 10;

    /* Short-circuit in &&: Left side is 0 (false), so ++y is SKIPPED */
    if (x != 0 && ++y > 10) {
        printf("Condition met\\n");
    }
    printf("After && test: x = %d, y = %d (y was NOT incremented!)\\n", x, y);

    /* Short-circuit in ||: Left side is true, so ++y is SKIPPED */
    int a = 5;
    if (a == 5 || ++y > 10) {
        printf("First condition was true in ||\\n");
    }
    printf("After || test: a = %d, y = %d (y was STILL NOT incremented!)\\n", a, y);

    return 0;
}""",
        "output": """After && test: x = 0, y = 10 (y was NOT incremented!)
First condition was true in ||
After || test: a = 5, y = 10 (y was STILL NOT incremented!)""",
        "explanation": "1. In `x != 0 && ++y > 10`, `x != 0` evaluates to `0`. C short-circuits and skips `++y > 10`. Hence `y` remains `10`.\n2. In `a == 5 || ++y > 10`, `a == 5` is `1`. C short-circuits and skips `++y > 10`. Hence `y` remains `10`.",
        "mistakes": [
            ("Confusing assignment `=` with relational equality `==`.", "Writing `if (x = 5)` assigns 5 to x (which evaluates to true) instead of checking equality. Always use `if (x == 5)`."),
            ("Placing state-modifying side-effects in the second operand of logical expressions.", "Because of short-circuiting, code like `if (valid && ++index < max)` will not increment `index` if `valid` is false.")
        ],
        "practice_q": "Predict the value of `b` after executing: `int a = 0, b = 4; if (a && ++b) {}`."
    },
    {
        "num": 9,
        "title": "Increment, Decrement (Prefix vs Postfix), and Compound Assignment",
        "category": "Operators & Expressions",
        "difficulty": "Intermediate",
        "exam_tags": ["Viva Trap", "Exam Question"],
        "question": "Distinguish between prefix (`++x`, `--x`) and postfix (`x++`, `x--`) operators. Explain why expressions modifying a variable multiple times without sequence points invoke Undefined Behavior.",
        "logic": "Prefix increments/decrements first, then produces the updated value. Postfix produces the original value first, then increments/decrements the variable.",
        "concept": "1. Prefix (`++i`): Value of expression is `i + 1`. Side-effect happens immediately.\n2. Postfix (`i++`): Value of expression is `i`. Side effect happens before the next sequence point.\n3. Sequence Points: Points in code execution where all previous side-effects are guaranteed to be complete (e.g., semicolon `;`, comma `,`, `&&`, `||`).\n4. Undefined Behavior: Writing `i = i++` or `printf(\"%d %d\", i, i++)` violates the sequence point rule in C standards. The result is compiler-dependent and completely unpredictable.",
        "syntax": "prefix:  val = ++i;  /* i = i+1; val = i; */\npostfix: val = i++;  /* val = i; i = i+1; */",
        "code": """#include <stdio.h>

int main(void) {
    int a = 5, b = 5;

    int preResult = ++a;  /* a increments to 6, then preResult receives 6 */
    int postResult = b++; /* postResult receives 5, then b increments to 6 */

    printf("Prefix (++a):  preResult = %d, a = %d\\n", preResult, a);
    printf("Postfix (b++): postResult = %d, b = %d\\n", postResult, b);

    /* Compound Assignment Operators */
    int count = 10;
    count += 5; /* count = count + 5 -> 15 */
    count *= 2; /* count = count * 2 -> 30 */
    count %= 7; /* count = count % 7 -> 2 */
    printf("Compound Assignment Result: count = %d\\n", count);

    return 0;
}""",
        "output": """Prefix (++a):  preResult = 6, a = 6
Postfix (b++): postResult = 5, b = 6
Compound Assignment Result: count = 2""",
        "explanation": "1. In prefix `++a`, the operand is incremented before its value is extracted for `preResult`.\n2. In postfix `b++`, the old value 5 is extracted for `postResult`, and then `b` becomes 6 in memory.\n3. Compound assignments (`+=`, `*=`) are more concise and allow the compiler to generate efficient single-instruction assembly.",
        "mistakes": [
            ("Writing multiple increments in one expression like `x = ++x + x++`.", "This is Undefined Behavior according to the ISO C standard. Never modify a variable more than once between sequence points."),
            ("Applying `++` to constants or expressions like `++(x + 1)`.", "Increment and decrement operators require a modifiable l-value (a memory location). Expressions cannot be incremented.")
        ],
        "practice_q": "What are the values of `x` and `y` after: `int x = 3; int y = x++ * 2;`?"
    },
    {
        "num": 10,
        "title": "Bitwise Operators and Low-Level Bit Manipulation",
        "category": "Bitwise Operations",
        "difficulty": "Intermediate",
        "exam_tags": ["High Yield Viva", "VTU Exam Favorite"],
        "question": "Explain bitwise operators in C (`&`, `|`, `^`, `~`, `<<`, `>>`). Demonstrate with complete working code how to: (1) Set a bit, (2) Clear a bit, (3) Toggle a bit, and (4) Check if a number is even or odd.",
        "logic": "Bitwise operators operate directly on the binary representation of integer types bit-by-bit.",
        "concept": "1. Bitwise AND `&`: 1 only if both bits are 1.\n2. Bitwise OR `|`: 1 if at least one bit is 1.\n3. Bitwise XOR `^`: 1 if bits differ (0^1=1, 1^0=1, 0^0=0, 1^1=0).\n4. Bitwise NOT `~`: Inverts all bits (one's complement).\n5. Left Shift `<<`: `x << n` multiplies `x` by $2^n$.\n6. Right Shift `>>`: `x >> n` divides `x` by $2^n$ (integer floor).\nCommon Bit Manipulation Idioms:\n- Set bit k: `num |= (1 << k)`\n- Clear bit k: `num &= ~(1 << k)`\n- Toggle bit k: `num ^= (1 << k)`\n- Check bit k: `(num >> k) & 1`\n- Even/Odd check: `(num & 1) == 0` (even) else odd.",
        "syntax": "num & (1 << pos)\nnum | (1 << pos)\nnum ^ (1 << pos)",
        "code": """#include <stdio.h>

void printBinary8(unsigned char n) {
    for (int i = 7; i >= 0; i--) {
        printf("%d", (n >> i) & 1);
    }
    printf(" (Decimal: %u)\\n", n);
}

int main(void) {
    unsigned char val = 12; /* Binary: 00001100 */

    printf("Initial value:     ");
    printBinary8(val);

    /* 1. Set bit 0 (position 0) -> (1 << 0) is 00000001 */
    val |= (1 << 0);
    printf("After Setting Bit 0: ");
    printBinary8(val); /* 00001101 -> 13 */

    /* 2. Clear bit 2 -> ~(1 << 2) is 11111011 */
    val &= ~(1 << 2);
    printf("After Clearing Bit 2:");
    printBinary8(val); /* 00001001 -> 9 */

    /* 3. Toggle bit 3 -> (1 << 3) is 00001000 */
    val ^= (1 << 3);
    printf("After Toggling Bit 3:");
    printBinary8(val); /* 00000001 -> 1 */

    /* 4. Check Even or Odd using Bitwise AND */
    int testNum = 27;
    printf("Is %d Even or Odd? -> %s\\n", 
           testNum, (testNum & 1) ? "ODD" : "EVEN");

    return 0;
}""",
        "output": """Initial value:     00001100 (Decimal: 12)
After Setting Bit 0: 00001101 (Decimal: 13)
After Clearing Bit 2:00001001 (Decimal: 9)
After Toggling Bit 3:00000001 (Decimal: 1)
Is 27 Even or Odd? -> ODD""",
        "explanation": "1. `(1 << k)` creates a bitmask with a single 1 at bit index `k`.\n2. `val |= mask` forces the target bit to 1 without touching any other bit.\n3. `val &= ~mask` forces the target bit to 0 because `~mask` has 0 at position `k` and 1 everywhere else.\n4. `testNum & 1` tests the least significant bit (LSB). For any odd number, LSB is 1; for even numbers, LSB is 0.",
        "mistakes": [
            ("Confusing logical AND `&&` with bitwise AND `&`.", "`&&` is a boolean operator with short-circuit evaluation; `&` operates on individual bits."),
            ("Shifting by negative or oversized offsets (`x << 35` on 32-bit int).", "Shifting by a number greater than or equal to the bit width of the integer is Undefined Behavior in C.")
        ],
        "practice_q": "Write a one-line C expression using bitwise operators to determine if an integer `n` is a power of 2."
    },
    {
        "num": 11,
        "title": "Conditional (Ternary) Operator and Nested Decisions",
        "category": "Operators & Expressions",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Level", "Viva Question"],
        "question": "What is the conditional operator `(?:)` in C? Why is it called a ternary operator? Write a complete program to find the maximum among three numbers using nested conditional operators.",
        "logic": "The conditional operator takes three operands: a condition, an expression if true, and an expression if false. It is the only ternary operator in C.",
        "concept": "Syntax: `condition ? expression1 : expression2`\nIf `condition` evaluates to non-zero (true), `expression1` is evaluated and becomes the result. If false, `expression2` is evaluated.\nIt can be nested: `(a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c)`.",
        "syntax": "result = (condition) ? value_if_true : value_if_false;",
        "code": """#include <stdio.h>

int main(void) {
    int a = 45, b = 89, c = 62;

    /* Nested ternary operator to find maximum of three values */
    int max = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);

    printf("Numbers: a = %d, b = %d, c = %d\\n", a, b, c);
    printf("The Maximum Value is: %d\\n", max);

    /* Absolute value calculation using ternary operator */
    int diff = a - b;
    int absDiff = (diff < 0) ? -diff : diff;
    printf("Absolute Difference |a - b|: %d\\n", absDiff);

    return 0;
}""",
        "output": """Numbers: a = 45, b = 89, c = 62
The Maximum Value is: 89
Absolute Difference |a - b|: 44""",
        "explanation": "1. If `a > b` is true, the left branch `(a > c ? a : c)` is evaluated.\n2. Since `45 > 89` is false, the right branch `(b > c ? b : c)` is evaluated.\n3. In that branch, `89 > 62` is true, returning `89` directly into `max`.",
        "mistakes": [
            ("Overusing deeply nested ternary operators.", "More than 2 levels of nested ternary expressions harms readability. Use `if-else` ladders for complex logic."),
            ("Assuming ternary operator can execute arbitrary statements without returning a value.", "The operands of `?:` must be expressions that return values of compatible types.")
        ],
        "practice_q": "Rewrite `if (score >= 40) pass = 1; else pass = 0;` as a single statement using the ternary operator."
    },
    {
        "num": 12,
        "title": "Operator Precedence and Associativity Table",
        "category": "Operators & Expressions",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Theory", "Output Prediction"],
        "question": "Explain operator precedence and associativity. Construct the hierarchy table from highest to lowest precedence and evaluate a complex expression step-by-step.",
        "logic": "Precedence determines which operator is evaluated first in an expression with different operators. Associativity determines the evaluation direction (left-to-right or right-to-left) when operators share the same precedence.",
        "concept": "Hierarchy Summary:\n1. Highest: Postfix `()`, `[]`, `->`, `.`, `++`, `--` (Left-to-Right)\n2. Unary: Prefix `++`, `--`, `+`, `-`, `!`, `~`, `*`, `&`, `sizeof` (Right-to-Left)\n3. Multiplicative: `*`, `/`, `%` (Left-to-Right)\n4. Additive: `+`, `-` (Left-to-Right)\n5. Shift: `<<`, `>>` (Left-to-Right)\n6. Relational: `<`, `<=`, `>`, `>=` (Left-to-Right)\n7. Equality: `==`, `!=` (Left-to-Right)\n8. Bitwise: `&` then `^` then `|` (Left-to-Right)\n9. Logical: `&&` then `||` (Left-to-Right)\n10. Conditional: `?:` (Right-to-Left)\n11. Assignment: `=`, `+=`, `-=`, etc. (Right-to-Left)\n12. Lowest: Comma `,` (Left-to-Right)",
        "syntax": "Precedence determines binding strength; parentheses `()` override all default rules.",
        "code": """#include <stdio.h>

int main(void) {
    int a = 10, b = 5, c = 2, d = 3;

    /* Expression evaluation */
    int result = a + b * c - d / c + a % d;
    /*
     * Step 1: b * c = 5 * 2 = 10
     * Step 2: d / c = 3 / 2 = 1
     * Step 3: a % d = 10 % 3 = 1
     * Expression becomes: a + 10 - 1 + 1
     * Step 4: 10 + 10 = 20
     * Step 5: 20 - 1 = 19
     * Step 6: 19 + 1 = 20
     */

    printf("a = %d, b = %d, c = %d, d = %d\\n", a, b, c, d);
    printf("Expression: a + b * c - d / c + a %% d\\n");
    printf("Evaluated Result: %d\\n", result);

    return 0;
}""",
        "output": """a = 10, b = 5, c = 2, d = 3
Expression: a + b * c - d / c + a % d
Evaluated Result: 20""",
        "explanation": "1. Multiplicative operators `*`, `/`, `%` possess higher precedence than additive operators `+`, `-`.\n2. Left-to-right associativity ensures `b * c` is evaluated, then `d / c`, then `a % d`.\n3. Additive operations are then resolved left-to-right: `10 + 10 - 1 + 1 = 20`.",
        "mistakes": [
            ("Relying on memory for complex precedence rules instead of using parentheses.", "Always use parentheses `()` to clarify order of operations and make code self-documenting."),
            ("Assuming order of evaluation of function arguments is defined by precedence.", "In `func(f1(), f2())`, C does NOT define which function is called first. Do not rely on argument order.")
        ],
        "practice_q": "Evaluate: `int ans = 2 + 3 * 4 > 10 && 5 == 5;`. What is the value of `ans`?"
    },
    {
        "num": 13,
        "title": "Formatted vs Unformatted I/O Functions",
        "category": "I/O System",
        "difficulty": "Fundamental",
        "exam_tags": ["Viva Favorite", "Exam Question"],
        "question": "Compare formatted I/O (`printf()`, `scanf()`) with unformatted I/O (`getchar()`, `putchar()`, `getch()`, `puts()`). Explain the buffer flush issue when reading characters after numbers.",
        "logic": "Formatted I/O functions interpret data according to format conversion specifications (%d, %f). Unformatted I/O reads/writes raw bytes or single characters without formatting overhead.",
        "concept": "1. `getchar()` / `putchar()`: Standard ANSI C functions reading/writing one character via line-buffered stdin/stdout.\n2. `getch()` / `getche()`: Non-standard `<conio.h>` functions (Windows/DOS) reading immediate keystrokes without waiting for Enter.\n3. `puts()`: Prints string automatically appending a newline `\\n`.\n4. Input Buffer Trap: `scanf(\"%d\", &num)` reads the integer but leaves the trailing newline character `\\n` in the stdin buffer. A subsequent `getchar()` or `fgets()` will consume that `\\n` immediately instead of waiting for user input! Fix: consume whitespace using `scanf(\" %c\", &ch)` with a leading space.",
        "syntax": "ch = getchar();\nputchar(ch);\nputs(\"Text\");",
        "code": """#include <stdio.h>

int main(void) {
    int age;
    char grade;

    printf("Enter student age: ");
    if (scanf("%d", &age) != 1) return 1;

    /* Leading space in format string ' %c' tells scanf to skip whitespace & leftover newlines */
    printf("Enter student grade (A/B/C): ");
    scanf(" %c", &grade);

    printf("\\n--- Unformatted Display ---\\n");
    puts("Student Details Registered Successfully:");
    printf("Age: %d\\n", age);
    printf("Grade: ");
    putchar(grade);
    putchar('\\n');

    return 0;
}""",
        "output": """Enter student age: 19
Enter student grade (A/B/C): A

--- Unformatted Display ---
Student Details Registered Successfully:
Age: 19
Grade: A""",
        "explanation": "1. Entering `19` and pressing Enter puts `'1'`, `'9'`, `'\\n'` into the stdin buffer.\n2. `scanf(\"%d\")` consumes `19`, leaving `'\\n'`.\n3. The leading space in `\" %c\"` instructs `scanf` to discard any leading whitespace characters, cleanly reading `'A'`.",
        "mistakes": [
            ("Using `fflush(stdin)` to clear keyboard input.", "`fflush()` on input streams is Undefined Behavior in standard C. Use `while(getchar() != '\\n');` or a leading space in format string."),
            ("Using `gets()`.", "`gets()` does not perform boundary checks and causes catastrophic buffer overflows. It was deprecated in C99 and removed from C11.")
        ],
        "practice_q": "What does `getchar()` return when it reaches the end of an input stream or file?"
    },
    {
        "num": 14,
        "title": "Selection Control: Simple if, if-else, and Nested Decisions",
        "category": "Decision Control",
        "difficulty": "Fundamental",
        "exam_tags": ["Programming Problem", "Exam Question"],
        "question": "Write a complete C program to check whether a given year is a Leap Year. Explain the full decision logic considering century year exceptions.",
        "logic": "A year is a leap year if: (Year is divisible by 400) OR (Year is divisible by 4 AND NOT divisible by 100).",
        "concept": "Leap Year Rules:\n1. If a year is evenly divisible by 400, it is a leap year (e.g., 2000, 2400).\n2. If a year is divisible by 100 but not 400, it is NOT a leap year (e.g., 1700, 1800, 1900).\n3. If a year is divisible by 4 and not a century year, it is a leap year (e.g., 2024, 2028).\n4. All other years are common years.",
        "syntax": "if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))",
        "code": """#include <stdio.h>

int isLeapYear(int year) {
    if (year % 400 == 0) {
        return 1; /* Divisible by 400 -> Leap year */
    } else if (year % 100 == 0) {
        return 0; /* Century year not divisible by 400 -> Not leap year */
    } else if (year % 4 == 0) {
        return 1; /* Divisible by 4 -> Leap year */
    } else {
        return 0; /* Common year */
    }
}

int main(void) {
    int testYears[] = {2000, 1900, 2024, 2023};
    int count = sizeof(testYears) / sizeof(testYears[0]);

    printf("=== VTU Leap Year Verification System ===\\n");
    for (int i = 0; i < count; i++) {
        int yr = testYears[i];
        if (isLeapYear(yr)) {
            printf("Year %d: LEAP YEAR (366 Days, Feb has 29 days)\\n", yr);
        } else {
            printf("Year %d: COMMON YEAR (365 Days, Feb has 28 days)\\n", yr);
        }
    }

    return 0;
}""",
        "output": """=== VTU Leap Year Verification System ===
Year 2000: LEAP YEAR (366 Days, Feb has 29 days)
Year 1900: COMMON YEAR (365 Days, Feb has 28 days)
Year 2024: LEAP YEAR (366 Days, Feb has 29 days)
Year 2023: COMMON YEAR (365 Days, Feb has 28 days)""",
        "explanation": "1. 2000 is divisible by 400, so condition 1 succeeds -> Leap Year.\n2. 1900 is divisible by 100, reaching branch 2 -> Not a Leap Year.\n3. 2024 is divisible by 4 and not 100 -> Leap Year.\n4. 2023 is not divisible by 4 -> Common Year.",
        "mistakes": [
            ("Writing only `year % 4 == 0` for leap year check.", "This incorrectly classifies century years like 1900, 1800, and 2100 as leap years."),
            ("Placing a semicolon after the if condition: `if (year % 4 == 0);`.", "The semicolon terminates the if statement, making the code block execute unconditionally.")
        ],
        "practice_q": "Write the leap year check as a single return statement using logical operators."
    },
    {
        "num": 15,
        "title": "else-if Ladder: Student Grading and Range Classification",
        "category": "Decision Control",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Question", "Lab Program"],
        "question": "Implement an `else-if` ladder program to determine a student's grade and division based on marks in 5 engineering subjects with input validation.",
        "logic": "The `else-if` ladder tests sequential conditions. Once a condition evaluates to true, the corresponding block executes and the rest of the ladder is skipped.",
        "concept": "Grading Scale:\n- Marks >= 90: Distinction (Grade O)\n- Marks >= 80 and < 90: First Class Exemplary (Grade A+)\n- Marks >= 70 and < 80: First Class (Grade A)\n- Marks >= 60 and < 70: Second Class (Grade B)\n- Marks >= 50 and < 60: Pass Class (Grade C)\n- Marks < 50: Fail (Grade F)\n- Marks < 0 or > 100: Invalid Marks.",
        "syntax": "if (cond1) { ... } else if (cond2) { ... } else { ... }",
        "code": """#include <stdio.h>

int main(void) {
    int marks[] = {85, 92, 78, 88, 90};
    int total = 0;
    int subjects = 5;

    for (int i = 0; i < subjects; i++) {
        total += marks[i];
    }

    double percentage = (double)total / subjects;

    printf("Total Marks: %d / %d\\n", total, subjects * 100);
    printf("Percentage:  %.2f%%\\n", percentage);
    printf("Classification: ");

    if (percentage >= 90.0) {
        printf("Grade O (Distinction / Outstanding)\\n");
    } else if (percentage >= 80.0) {
        printf("Grade A+ (First Class with Distinction)\\n");
    } else if (percentage >= 70.0) {
        printf("Grade A (First Class)\\n");
    } else if (percentage >= 60.0) {
        printf("Grade B (Second Class)\\n");
    } else if (percentage >= 50.0) {
        printf("Grade C (Pass Class)\\n");
    } else {
        printf("Grade F (Fail - Reappear Required)\\n");
    }

    return 0;
}""",
        "output": """Total Marks: 433 / 500
Percentage:  86.60%
Classification: Grade A+ (First Class with Distinction)""",
        "explanation": "1. Marks sum to 433. Percentage is $433 / 5 = 86.60\\%$.\n2. The first condition `percentage >= 90.0` is false.\n3. The second condition `percentage >= 80.0` evaluates to true. Grade A+ is printed and the remaining conditions are skipped.",
        "mistakes": [
            ("Writing multiple standalone `if` statements instead of `else if`.", "Independent `if` statements all evaluate sequentially. If you write `if (p >= 50)` first, a student with 95 will match every single condition!"),
            ("Using overlapping ranges like `percentage > 80 && percentage < 90` redundantly.", "In an `else if` ladder, if the previous condition `percentage >= 90` failed, you already know `percentage < 90`.")
        ],
        "practice_q": "How would you modify this program to enforce that if a student scores < 40 in ANY single subject, they automatically receive Grade F regardless of overall percentage?"
    },
    {
        "num": 16,
        "title": "The switch-case Statement: Rules, Fall-Through, and Menu Calculator",
        "category": "Decision Control",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Explain the syntax, working rules, and limitations of the `switch-case` statement. What is fall-through behavior? Write a menu-driven arithmetic calculator program.",
        "logic": "`switch` evaluates an integral or character expression and matches it against `case` constant labels. `break` prevents execution from falling through into subsequent cases.",
        "concept": "Rules of `switch-case`:\n1. The switch expression must evaluate to an integer or character (`int`, `char`, `short`, `enum`). Floating-point types (`float`, `double`) are strictly prohibited.\n2. Case labels must be compile-time constants or constant expressions (e.g., `case 5:`, `case 'A':`, `case 2+3:`). Variables are NOT allowed.\n3. No two case labels can have duplicate values.\n4. Fall-Through: If a `break` statement is omitted, execution cascades sequentially through all subsequent case blocks until a `break` or closing brace is reached.\n5. `default` block executes when no case matches.",
        "syntax": "switch(expr) { case CONST1: ...; break; default: ...; }",
        "code": """#include <stdio.h>

int main(void) {
    char operator = '*';
    double num1 = 12.5, num2 = 4.0;
    double result = 0.0;
    int valid = 1;

    switch (operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 != 0.0) {
                result = num1 / num2;
            } else {
                printf("Error: Division by zero is undefined.\\n");
                valid = 0;
            }
            break;
        default:
            printf("Error: Unsupported operator '%c'\\n", operator);
            valid = 0;
            break;
    }

    if (valid) {
        printf("Calculation: %.2f %c %.2f = %.2f\\n", num1, operator, num2, result);
    }

    return 0;
}""",
        "output": """Calculation: 12.50 * 4.00 = 50.00""",
        "explanation": "1. `operator` contains `'*'`. Its ASCII integer value (42) matches `case '*'`. \n2. `result = num1 * num2` produces `50.00`.\n3. The `break` statement terminates the switch block, skipping `case '/'` and `default`.",
        "mistakes": [
            ("Attempting to use a float in switch: `switch (3.14)`.", "Switch expressions strictly require integer or character types. Float cases cause compilation errors."),
            ("Omitting `break` accidentally.", "Omitting `break` causes unintentional fall-through, executing unexpected statements below the matched case.")
        ],
        "practice_q": "Give an example of intentional fall-through in a `switch` statement (e.g. grouping vowels)."
    },
    {
        "num": 17,
        "title": "The for Loop: Structure, Multiple Expressions, and Multiplication Table",
        "category": "Loops & Iteration",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Question", "Viva Favorite"],
        "question": "Explain the mechanics of the `for` loop in C. Explain how initialization, condition, and increment expressions interact. Write a program to generate a formatted multiplication table.",
        "logic": "The `for` loop is an entry-controlled loop. Execution flow: (1) Initialization runs once, (2) Condition is evaluated; if true, body runs, (3) Update expression executes, (4) Repeat from step 2.",
        "concept": "General Syntax: `for (init; condition; update) { ... }`\nAdvanced Features:\n1. All three expressions are optional. `for (;;)` creates an intentional infinite loop.\n2. Multiple variables can be initialized and updated using the comma operator `,`: `for (i = 0, j = 10; i < j; i++, j--)`.\n3. In C99 and later, variables can be declared directly inside the initialization clause: `for (int i = 0; ...)`.",
        "syntax": "for (initialization; test_condition; update_step)",
        "code": """#include <stdio.h>

int main(void) {
    int n = 7;
    int limit = 10;

    printf("=== Multiplication Table for %d ===\\n", n);
    for (int i = 1; i <= limit; i++) {
        printf("%2d  x  %2d  =  %3d\\n", n, i, n * i);
    }

    /* Demonstration of multiple loop variables using comma operator */
    printf("\\n--- Two-variable Convergence Loop ---\\n");
    for (int left = 1, right = 10; left < right; left++, right--) {
        printf("left = %d, right = %d, sum = %d\\n", left, right, left + right);
    }

    return 0;
}""",
        "output": """=== Multiplication Table for 7 ===
 7  x   1  =    7
 7  x   2  =   14
 7  x   3  =   21
 7  x   4  =   28
 7  x   5  =   35
 7  x   6  =   42
 7  x   7  =   49
 7  x   8  =   56
 7  x   9  =   63
 7  x  10  =   70

--- Two-variable Convergence Loop ---
left = 1, right = 10, sum = 11
left = 2, right = 9, sum = 11
left = 3, right = 8, sum = 11
left = 4, right = 7, sum = 11
left = 5, right = 6, sum = 11""",
        "explanation": "1. In loop 1, `i` increments from 1 to 10. Once `i = 11`, the condition `11 <= 10` is false and the loop terminates.\n2. In loop 2, `left` increments while `right` decrements simultaneously. The loop stops when `left` meets `right` at 6 and 5.",
        "mistakes": [
            ("Putting a semicolon after the for loop header: `for (i = 0; i < 10; i++);`.", "The semicolon acts as an empty statement body. The loop runs 10 times doing nothing, and the subsequent block executes only once with `i = 10`."),
            ("Modifying the loop index variable inside the loop body unpredictably.", "Altering the loop counter inside the body makes debugging hard and can cause unexpected infinite loops.")
        ],
        "practice_q": "What happens when you execute `for (int i = 0; i < 5; ) { printf(\"%d \", i); }`?"
    },
    {
        "num": 18,
        "title": "The while Loop: Entry-Controlled Iteration and Palindrome Number",
        "category": "Loops & Iteration",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "What is an entry-controlled loop? Explain the working of the `while` loop. Write a complete C program to reverse a given integer and check if it is a Palindrome.",
        "logic": "The condition is tested BEFORE executing the loop body. If the condition is false initially, the body will not execute even once. To reverse an integer: extract the last digit using `% 10`, append it to the reversed number via `rev = rev * 10 + digit`, and truncate with `/ 10`.",
        "concept": "Algorithm to Reverse an Integer:\n1. Store original number in a temporary variable `temp`.\n2. Initialize `reversedNum = 0`.\n3. While `num > 0`:\n   a. `rem = num % 10` (extract last digit)\n   b. `reversedNum = reversedNum * 10 + rem`\n   c. `num = num / 10` (remove last digit)\n4. If `reversedNum == temp`, the number is a Palindrome.",
        "syntax": "while (condition) { /* statements */ }",
        "code": """#include <stdio.h>

int main(void) {
    int originalNumber = 12321;
    int num = originalNumber;
    int reversedNumber = 0;
    int remainder;

    while (num != 0) {
        remainder = num % 10;
        reversedNumber = reversedNumber * 10 + remainder;
        num /= 10;
    }

    printf("Original Number: %d\\n", originalNumber);
    printf("Reversed Number: %d\\n", reversedNumber);

    if (originalNumber == reversedNumber) {
        printf("Result: PALINDROME (Reads identically forward and backward)\\n");
    } else {
        printf("Result: NOT A PALINDROME\\n");
    }

    return 0;
}""",
        "output": """Original Number: 12321
Reversed Number: 12321
Result: PALINDROME (Reads identically forward and backward)""",
        "explanation": "1. Iteration 1: `rem = 1`, `rev = 1`, `num = 1232`\n2. Iteration 2: `rem = 2`, `rev = 12`, `num = 123`\n3. Iteration 3: `rem = 3`, `rev = 123`, `num = 12`\n4. Iteration 4: `rem = 2`, `rev = 1232`, `num = 1`\n5. Iteration 5: `rem = 1`, `rev = 12321`, `num = 0`\n6. Loop terminates since `num == 0`. `12321 == 12321`, confirming palindrome.",
        "mistakes": [
            ("Comparing `num == reversedNumber` at the end.", "`num` becomes 0 after the while loop finishes! Always save the initial value in a temporary variable (`originalNumber`)."),
            ("Integer overflow when reversing large numbers.", "Reversing numbers like `1999999999` exceeds the 32-bit signed integer maximum ($2^{31}-1 = 2,147,483,647$), causing negative overflow.")
        ],
        "practice_q": "How would you modify this program to calculate the sum of digits of a number?"
    },
    {
        "num": 19,
        "title": "The do-while Loop: Exit-Controlled Logic and Input Validation",
        "category": "Loops & Iteration",
        "difficulty": "Fundamental",
        "exam_tags": ["Viva Favorite", "Exam Question"],
        "question": "Differentiate between entry-controlled and exit-controlled loops. Explain the `do-while` loop and write a program demonstrating robust input validation for menu choices.",
        "logic": "The `do-while` loop evaluates its condition at the bottom. The loop body is guaranteed to execute AT LEAST ONCE, regardless of whether the condition is true or false.",
        "concept": "Comparison Table:\n- `while`: Condition evaluated at entry. Body executed 0 or more times. Syntax has no semicolon after while.\n- `do-while`: Condition evaluated at exit. Body executed 1 or more times. MUST end with a semicolon after while: `do { ... } while (cond);`.\nBest suited for: Menus, user prompts, reading at least one item before testing.",
        "syntax": "do { /* statements */ } while (condition);",
        "code": """#include <stdio.h>

int main(void) {
    int choice;
    int simulatedInputs[] = {-1, 5, 2}; /* Simulates user entering invalid options first */
    int inputIndex = 0;

    do {
        choice = simulatedInputs[inputIndex++];
        printf("Prompt: Enter menu choice (1: Start, 2: Config, 3: Exit) -> Entered: %d\\n", choice);

        if (choice < 1 || choice > 3) {
            printf(">> Invalid choice! Please select an option between 1 and 3.\\n\\n");
        }
    } while (choice < 1 || choice > 3);

    printf(">> Access Granted: Valid Choice %d Accepted!\\n", choice);

    return 0;
}""",
        "output": """Prompt: Enter menu choice (1: Start, 2: Config, 3: Exit) -> Entered: -1
>> Invalid choice! Please select an option between 1 and 3.

Prompt: Enter menu choice (1: Start, 2: Config, 3: Exit) -> Entered: 5
>> Invalid choice! Please select an option between 1 and 3.

Prompt: Enter menu choice (1: Start, 2: Config, 3: Exit) -> Entered: 2
>> Access Granted: Valid Choice 2 Accepted!""",
        "explanation": "1. Iteration 1 receives `-1`. Error message printed. Condition `-1 < 1` is true -> loop repeats.\n2. Iteration 2 receives `5`. Error message printed. Condition `5 > 3` is true -> loop repeats.\n3. Iteration 3 receives `2`. Valid! Condition evaluates to false -> loop exits.",
        "mistakes": [
            ("Forgetting the semicolon after `while (cond);` in do-while.", "A common syntax error in C is omitting the trailing semicolon in `do { ... } while (condition);`."),
            ("Using `while` for menus where the menu must be displayed before taking input.", "`do-while` is the natural choice because you always need to display the menu at least once.")
        ],
        "practice_q": "What will `int x = 10; do { printf(\"%d \", x); x++; } while (x < 5);` output?"
    },
    {
        "num": 20,
        "title": "Nested Loops and Pattern Printing: Floyd's Triangle & Pyramids",
        "category": "Loops & Iteration",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Question", "Lab Classic"],
        "question": "What is a nested loop? Write a C program to print: (1) Floyd's Triangle of numbers, and (2) An equilateral star pyramid of height N.",
        "logic": "A nested loop is a loop inside another loop. The outer loop controls the rows, while the inner loop controls the columns or elements in each row.",
        "concept": "1. Floyd's Triangle:\nRow 1: 1\nRow 2: 2 3\nRow 3: 4 5 6\nRow 4: 7 8 9 10\nContinuous sequential counter that increments across row and column boundaries.\n2. Star Pyramid:\nRow $i$ (1 to N) requires:\n- $N - i$ leading spaces.\n- $2i - 1$ asterisks.",
        "syntax": "for (int r = 1; r <= N; r++) { for (int c = 1; c <= r; c++) { ... } }",
        "code": """#include <stdio.h>

void printFloydsTriangle(int rows) {
    int counter = 1;
    printf("--- Floyd's Triangle (%d rows) ---\\n", rows);
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%-3d ", counter++);
        }
        printf("\\n");
    }
}

void printStarPyramid(int height) {
    printf("\\n--- Equilateral Star Pyramid (%d levels) ---\\n", height);
    for (int i = 1; i <= height; i++) {
        /* Print leading spaces: height - i */
        for (int s = 1; s <= height - i; s++) {
            printf(" ");
        }
        /* Print asterisks: 2*i - 1 */
        for (int k = 1; k <= (2 * i - 1); k++) {
            printf("*");
        }
        printf("\\n");
    }
}

int main(void) {
    printFloydsTriangle(4);
    printStarPyramid(5);
    return 0;
}""",
        "output": """--- Floyd's Triangle (4 rows) ---
1   
2   3   
4   5   6   
7   8   9   10  

--- Equilateral Star Pyramid (5 levels) ---
    *
   ***
  *****
 *******
*********""",
        "explanation": "1. In Floyd's Triangle, the outer loop runs from `i = 1` to `rows`. The inner loop runs `j` from 1 to `i`. `counter++` prints consecutive integers.\n2. In the Star Pyramid, for row `i = 1`, it prints $5 - 1 = 4$ spaces, then $2(1) - 1 = 1$ star.\n3. For row `i = 5`, it prints $5 - 5 = 0$ spaces, and $2(5) - 1 = 9$ stars.",
        "mistakes": [
            ("Re-initializing the Floyd's counter inside the row loop.", "If `counter = 1` is placed inside the outer loop, every row restarts at 1 instead of continuing the sequence."),
            ("Using the same loop variable for both outer and inner loops (`for (int i... for (int i...)`).", "The inner loop overwrites the outer loop's counter, creating an infinite loop.")
        ],
        "practice_q": "How many total asterisks are printed in an equilateral star pyramid of height N?"
    },
    {
        "num": 21,
        "title": "Jump Statements: break vs continue with Prime Number Search",
        "category": "Control Flow",
        "difficulty": "Intermediate",
        "exam_tags": ["Viva Must-Know", "Exam Question"],
        "question": "Differentiate between `break` and `continue` statements. Write a complete C program to search for prime numbers in a range, using `break` to optimize divisor testing and `continue` to skip even numbers.",
        "logic": "`break` terminates the entire loop immediately, transferring control out. `continue` skips the remainder of the current iteration and jumps to the next cycle.",
        "concept": "Comparison:\n- `break`: Exits the innermost loop or switch immediately. Remaining iterations are aborted.\n- `continue`: Skips remaining statements in the current iteration. In `for`, jumps to update expression; in `while`, jumps to condition check.\nPrime Search Optimization:\n- Skip even numbers > 2 immediately with `continue`.\n- Test odd divisors up to $\\sqrt{n}$. If a divisor is found, set flag and `break` immediately.",
        "syntax": "if (found) break;\nif (skip_condition) continue;",
        "code": """#include <stdio.h>

int isPrime(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0; /* Exclude all other evens */

    /* Check odd divisors up to d * d <= n */
    for (int d = 3; d * d <= n; d += 2) {
        if (n % d == 0) {
            return 0; /* Divisible -> Not prime, early exit */
        }
    }
    return 1;
}

int main(void) {
    int start = 10, end = 30;

    printf("Prime Numbers between %d and %d:\\n", start, end);
    for (int num = start; num <= end; num++) {
        /* Optimization: Skip even numbers using continue */
        if (num % 2 == 0) {
            continue; /* Skips to next num immediately */
        }

        if (isPrime(num)) {
            printf("%d ", num);
        }
    }
    printf("\\n");

    return 0;
}""",
        "output": """Prime Numbers between 10 and 30:
11 13 17 19 23 29 """,
        "explanation": "1. For `num = 10, 12, 14...`, `continue` skips the rest of the loop without calling `isPrime()`.\n2. In `isPrime()`, checking up to `d * d <= n` reduces time complexity from $O(n)$ to $O(\\sqrt{n})$.\n3. As soon as any divisor is found, `return 0` acts as an early exit.",
        "mistakes": [
            ("Thinking `break` exits all nested loops.", "`break` ONLY terminates the innermost enclosing loop or switch. Outer loops continue running."),
            ("Using `continue` inside a `switch` statement.", "`continue` cannot be used inside `switch` unless that `switch` is located inside a loop; in that case, it affects the enclosing loop.")
        ],
        "practice_q": "Why does testing divisors up to $\\sqrt{n}$ suffice to prove an integer $n$ is prime?"
    },
    {
        "num": 22,
        "title": "The goto Statement: Unconditional Branching and Safe Usages",
        "category": "Control Flow",
        "difficulty": "Fundamental",
        "exam_tags": ["Viva Favorite", "Exam Question"],
        "question": "What is the `goto` statement? Why is its unstructured usage strongly discouraged in software engineering? Identify the single acceptable, clean use-case for `goto` in modern C.",
        "logic": "`goto` performs an unconditional jump to a labeled statement within the same function. Uncontrolled usage leads to 'spaghetti code', making debugging and formal verification nearly impossible.",
        "concept": "1. Syntax: `goto label_name; ... label_name: statement;`\n2. Scope: A label has function scope. You cannot jump across different functions.\n3. The 'Spaghetti Code' Danger: Arbitrary jumps bypass variable initializations, break loop invariants, and obscure program control flow.\n4. Clean / Acceptable Idiom in C: Multi-level error handling and resource cleanup in systems programming (e.g., Linux kernel). When allocating multiple resources (files, memory, locks), a single `goto cleanup;` avoids deeply nested `if-else` cascades.",
        "syntax": "goto error_handler;\n...\nerror_handler:\n    free(buffer);\n    return -1;",
        "code": """#include <stdio.h>
#include <stdlib.h>

/* Safe Idiom: Deeply Nested Loop Breakout */
int searchMatrix(int matrix[3][3], int target) {
    int foundRow = -1, foundCol = -1;

    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
            if (matrix[r][c] == target) {
                foundRow = r;
                foundCol = c;
                goto search_complete; /* Breaks out of BOTH nested loops cleanly */
            }
        }
    }

search_complete:
    if (foundRow != -1) {
        printf("Target %d found at row %d, col %d!\\n", target, foundRow, foundCol);
        return 1;
    } else {
        printf("Target %d not present in matrix.\\n", target);
        return 0;
    }
}

int main(void) {
    int grid[3][3] = {
        {10, 20, 30},
        {40, 50, 60},
        {70, 80, 90}
    };

    searchMatrix(grid, 50);
    searchMatrix(grid, 99);

    return 0;
}""",
        "output": """Target 50 found at row 2, col 2!
Target 99 not present in matrix.""",
        "explanation": "1. Standard `break` only exits one inner loop level, requiring extra boolean flags in the outer loop.\n2. `goto search_complete;` immediately transfers control outside all nested loops to the cleanup/result label.\n3. This is one of the few accepted uses of `goto` in idiomatic C.",
        "mistakes": [
            ("Using `goto` to simulate standard loops (`for`, `while`).", "Writing loops using `goto` is poor practice and leads to unreadable code. Use structured loop constructs."),
            ("Jumping past variable declarations with initializers.", "In C99, jumping over a variable-length array (VLA) declaration using `goto` is illegal and causes compilation failure.")
        ],
        "practice_q": "Can a `goto` statement jump from one function into the middle of another function? Explain."
    },
    {
        "num": 23,
        "title": "Output Prediction & Debugging: Precedence and Assignment Traps",
        "category": "Debugging & Tracing",
        "difficulty": "Exam-Level",
        "exam_tags": ["High Yield Viva", "VTU Exam Favorite"],
        "question": "Predict the exact output of the following C code snippet and explain the underlying language mechanics: `int x = 5; if (x = 0) printf(\"A\"); else printf(\"B\");`.",
        "logic": "The expression `x = 0` inside the `if` condition uses the assignment operator `=`, not the equality comparison `==`. The value of an assignment expression in C is the value assigned.",
        "concept": "1. Assignment Expression Value: `(x = 0)` assigns `0` to `x` and evaluates to `0`.\n2. Truth in C: In C, `0` is treated as false, and any non-zero value is treated as true.\n3. Since `0` is false, the `if` condition evaluates to false, causing the `else` branch to execute.\n4. Prevention: 'Yoda Conditions' like `if (0 == x)` prevent this bug because `0 = x` triggers a compile error.",
        "syntax": "if (x == 0) /* Comparison */\nif (x = 0)  /* Assignment (Evaluates to 0 -> False) */",
        "code": """#include <stdio.h>

int main(void) {
    int x = 5;

    printf("Before if: x = %d\\n", x);

    if (x = 0) {
        printf("Branch A Executed (True)\\n");
    } else {
        printf("Branch B Executed (False)\\n");
    }

    printf("After if:  x = %d (x was overwritten!)\\n", x);

    /* Yoda Condition Technique */
    int status = 1;
    if (1 == status) {
        printf("Yoda Condition succeeded safely: status == 1\\n");
    }

    return 0;
}""",
        "output": """Before if: x = 5
Branch B Executed (False)
After if:  x = 0 (x was overwritten!)
Yoda Condition succeeded safely: status == 1""",
        "explanation": "1. In `if (x = 0)`, `0` is assigned to `x`. The expression evaluates to `0`.\n2. C interprets `0` as boolean FALSE. The `if` branch is skipped.\n3. The `else` branch executes, printing `Branch B`.\n4. Notice that `x` is permanently modified from `5` to `0`.",
        "mistakes": [
            ("Writing `if (x = 10)` thinking it checks if x equals 10.", "`x = 10` assigns 10, which evaluates to true. The block will ALWAYS execute regardless of what `x` was before!"),
            ("Ignoring compiler warnings like `suggest parentheses around assignment used as truth value`.", "Modern compilers (GCC/Clang) warn about assignment in conditions. Always compile with `-Wall`.")
        ],
        "practice_q": "What will `int a = 3, b = 2; printf(\"%d\", a > b ? a++ : b++);` output, and what will `a` and `b` be?"
    },
    {
        "num": 24,
        "title": "Floating-Point Representation and Precision Comparison Trap",
        "category": "Debugging & Tracing",
        "difficulty": "Exam-Level",
        "exam_tags": ["Interview Classic", "Viva Trap"],
        "question": "Why does the statement `float x = 0.1f; if (x == 0.1) printf(\"Equal\"); else printf(\"Not Equal\");` print 'Not Equal' in C? Explain IEEE 754 floating-point precision and how to properly compare floats.",
        "logic": "Floating-point literals without suffix (like `0.1`) are treated as `double` by default. $0.1$ has an infinite repeating binary representation and cannot be represented exactly in binary floating-point.",
        "concept": "1. IEEE 754 Representation: Binary floats represent numbers as powers of 2 (1/2, 1/4, 1/8, etc.). Fractions like 1/10 ($0.1$) cannot be represented with finite binary digits ($0.000110011...$).\n2. Type Mismatch: `0.1f` is a 32-bit single-precision float (24 bits mantissa). `0.1` is a 64-bit double-precision float (53 bits mantissa).\n3. When comparing `x == 0.1`, `x` is promoted to `double`. The lower bits padded into the double differ from the 53-bit approximation of `0.1`, causing the equality check to fail.\n4. Solution: Never compare floating-point numbers with `==`. Compare using an epsilon tolerance: `fabs(a - b) < EPSILON`.",
        "syntax": "#include <math.h>\n#define EPSILON 1e-6\nif (fabs(a - b) < EPSILON)",
        "code": """#include <stdio.h>
#include <math.h>

int main(void) {
    float x = 0.1f;

    printf("--- Direct Equality Test ---\\n");
    if (x == 0.1) {
        printf("Equal\\n");
    } else {
        printf("Not Equal (Float 0.1f != Double 0.1!)\\n");
    }

    printf("Direct print of float  x:   %.20f\\n", x);
    printf("Direct print of double 0.1: %.20f\\n", 0.1);

    /* Safe Comparison using Epsilon */
    printf("\\n--- Safe Epsilon Comparison ---\\n");
    const double EPSILON = 1e-7;
    if (fabs(x - 0.1f) < EPSILON) {
        printf("Equal within epsilon tolerance!\\n");
    }

    return 0;
}""",
        "output": """--- Direct Equality Test ---
Not Equal (Float 0.1f != Double 0.1!)
Direct print of float  x:   0.10000000149011611938
Direct print of double 0.1: 0.10000000000000000555

--- Safe Epsilon Comparison ---
Equal within epsilon tolerance!""",
        "explanation": "1. `x` stored as `float` is actually `0.10000000149011611938`.\n2. The literal `0.1` stored as `double` is `0.10000000000000000555`.\n3. Since their binary representations differ in the lower bits, direct `==` evaluation yields false.\n4. `fabs(x - 0.1f) < EPSILON` correctly checks that the difference is within negligible rounding tolerance.",
        "mistakes": [
            ("Writing `while (f != 1.0f)` with a loop increment `f += 0.1f`.", "Due to rounding errors, `f` might become `0.999999` and then `1.099999`, missing `1.0` entirely and looping infinitely!"),
            ("Using integer `abs()` instead of `fabs()` for floating-point calculations.", "`abs()` truncates floats to integer. Always use `fabs()` from `<math.h>` for floats/doubles.")
        ],
        "practice_q": "What suffix must you append to a floating literal to force it to be stored as a `long double`?"
    },
    {
        "num": 25,
        "title": "Comprehensive Program: Fibonacci Series with Prime Tagging",
        "category": "Comprehensive Integration",
        "difficulty": "Exam-Level",
        "exam_tags": ["Exam High-Scorer", "Integration Problem"],
        "question": "Write a complete C program to generate the first N terms of the Fibonacci sequence ($0, 1, 1, 2, 3, 5, 8, \\dots$). For each generated term, check and display whether it is a Prime Number.",
        "logic": "Fibonacci sequence begins with $F_0 = 0, F_1 = 1$, and each subsequent term is $F_n = F_{n-1} + F_{n-2}$. Each term is tested for primality using trial division.",
        "concept": "1. Sequence Generation: Use iterative approach with two variables `t1 = 0, t2 = 1`. In each step, `nextTerm = t1 + t2`, then update `t1 = t2; t2 = nextTerm;`.\n2. Prime Check: 0 and 1 are neither prime nor composite. 2 is prime. For other numbers, test divisors up to $\\sqrt{n}$.",
        "syntax": "next = first + second; first = second; second = next;",
        "code": """#include <stdio.h>

int checkPrime(long long n) {
    if (n <= 1) return 0;
    if (n == 2 || n == 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;

    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0)
            return 0;
    }
    return 1;
}

int main(void) {
    int n = 12;
    long long t1 = 0, t2 = 1, nextTerm;

    printf("=== First %d Terms of Fibonacci Series ===\\n", n);
    printf("%-5s | %-12s | %-10s\\n", "Term", "Value", "Status");
    printf("---------------------------------\\n");

    for (int i = 1; i <= n; i++) {
        if (i == 1) {
            nextTerm = t1;
        } else if (i == 2) {
            nextTerm = t2;
        } else {
            nextTerm = t1 + t2;
            t1 = t2;
            t2 = nextTerm;
        }

        int prime = checkPrime(nextTerm);
        printf("F(%2d) | %-12lld | %s\\n", 
               i, nextTerm, prime ? "PRIME" : (nextTerm <= 1 ? "Neither" : "Composite"));
    }

    return 0;
}""",
        "output": """=== First 12 Terms of Fibonacci Series ===
Term  | Value        | Status    
---------------------------------
F( 1) | 0            | Neither
F( 2) | 1            | Neither
F( 3) | 1            | Neither
F( 4) | 2            | PRIME
F( 5) | 3            | PRIME
F( 6) | 5            | PRIME
F( 7) | 8            | Composite
F( 8) | 13           | PRIME
F( 9) | 21           | Composite
F(10) | 34           | Composite
F(11) | 55           | Composite
F(12) | 89           | PRIME""",
        "explanation": "1. `t1` and `t2` are initialized to 0 and 1.\n2. In each iteration, `nextTerm = t1 + t2` calculates the subsequent term.\n3. `checkPrime()` uses the $6k \\pm 1$ optimization, testing divisibility up to $\\sqrt{n}$.\n4. Fibonacci numbers 2, 3, 5, 13, and 89 are identified as prime.",
        "mistakes": [
            ("Declaring 0 or 1 as prime numbers.", "By mathematical definition, prime numbers are integers strictly greater than 1 with exactly two distinct positive divisors: 1 and itself."),
            ("Using 32-bit `int` for higher Fibonacci numbers.", "Fibonacci numbers grow exponentially. The 47th Fibonacci term exceeds $2^{31}-1$, requiring `unsigned long long`.")
        ],
        "practice_q": "What is the maximum Fibonacci number that fits into a standard 64-bit unsigned integer?"
    },
    {
        "num": 26,
        "title": "Module 1 Mastery: Exam Traps, Viva Q&A, and Debugging Diagnostic",
        "category": "Comprehensive Review",
        "difficulty": "Exam-Level",
        "exam_tags": ["Viva Must-Know", "Final Exam Checklist"],
        "question": "Provide a high-yield diagnostic review of the top 5 most common compilation and runtime pitfalls in C Fundamentals (Semicolon after loops, Buffer leaks, Array bounds, Format mismatches, and Uninitialized pointers).",
        "logic": "Summarizes Module 1 fundamentals into an actionable debugging checklist for examination and viva preparation.",
        "concept": "Top 5 Pitfalls:\n1. Semicolon after loop header (`for(..);`): Causes empty loop body.\n2. Dangling `\\n` in stdin buffer: Swallows subsequent character reads.\n3. `=` vs `==`: Accidental assignment in conditions.\n4. Type mismatch in `printf`/`scanf`: `%f` vs `%lf`, `%d` vs `%ld`.\n5. Uninitialized variables: C does not automatically zero local stack variables; they contain indeterminate garbage values.",
        "syntax": "Debug flags: gcc -Wall -Wextra -pedantic -fsanitize=address",
        "code": """#include <stdio.h>

int main(void) {
    /* 1. Uninitialized variable demonstration */
    int garbageValue; /* Not initialized -> contains whatever bit pattern was on stack */
    
    /* 2. Proper zero-initialization */
    int cleanValue = 0;

    printf("Module 1 High-Yield Diagnostic:\\n");
    printf("- Garbage stack variable: %d (Unpredictable!)\\n", garbageValue);
    printf("- Clean initialized var:  %d (Reliable)\\n", cleanValue);
    printf("- Float promotion test:   %zu bytes (float promoted to double in printf)\\n", sizeof(1.0f + 2.0));

    return 0;
}""",
        "output": """Module 1 High-Yield Diagnostic:
- Garbage stack variable: 32767 (Unpredictable!)
- Clean initialized var:  0 (Reliable)
- Float promotion test:   8 bytes (float promoted to double in printf)""",
        "explanation": "1. Local (automatic) variables in C have undefined initial contents. Always explicitly initialize variables (`int x = 0;`).\n2. In expressions mixing `float` and `double`, C promotes `float` to `double` (8 bytes).\n3. In variable argument lists like `printf()`, `float` is automatically promoted to `double`.",
        "mistakes": [
            ("Assuming local variables are automatically set to 0.", "Only global and `static` variables are initialized to zero by default. Stack variables have random garbage values."),
            ("Compiling without compiler warnings enabled.", "Always pass `-Wall -Wextra` to GCC. The compiler will catch 95% of these subtle bugs automatically.")
        ],
        "practice_q": "What is the storage class and default value of a variable declared at file level outside all functions?"
    }
]

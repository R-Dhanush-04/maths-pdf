# -*- coding: utf-8 -*-
"""
C Programming - Module 5: File Handling and Preprocessor Directives
Questions 105 to 130 (File Streams, Modes, I/O Functions, Binary Files, fseek, Preprocessor Macros, Header Guards, and Diagnostics)
"""

C_MODULE5_QUESTIONS = [
    {
        "num": 105,
        "title": "Introduction to File Handling: Streams, stdin/stdout/stderr, and Text vs Binary",
        "category": "File Fundamentals",
        "difficulty": "Fundamental",
        "exam_tags": ["Core Concept", "Viva Must-Know"],
        "question": "What is a file in C? Explain the concept of a Stream and the three standard streams (`stdin`, `stdout`, `stderr`). Differentiate thoroughly between Text Files and Binary Files.",
        "logic": "Variables and arrays reside in volatile RAM and vanish when the program terminates. Files store data persistently on non-volatile secondary storage (SSD, Hard Disk).",
        "concept": "1. Stream Concept: An abstract logical interface mapping to physical I/O devices (keyboard, monitor, disk file). All C file I/O operations work through streams.\n2. Standard Pre-Opened Streams (in `<stdio.h>`):\n- `stdin`: Standard input stream (usually keyboard, file descriptor 0).\n- `stdout`: Standard output stream (buffered console display, file descriptor 1).\n- `stderr`: Standard error stream (unbuffered console display for immediate error messages, file descriptor 2).\n3. Text Files vs Binary Files:\n- Text Files: Stored as human-readable ASCII or UTF-8 characters. Characters like newline undergo translation (e.g., `\\n` maps to `\\r\\n` on Windows). Ends with EOF marker.\n- Binary Files: Stored as raw bytes exactly as they appear in CPU RAM (e.g., 4-byte integers, 8-byte doubles). No character translation occurs; faster and more compact.",
        "syntax": "FILE *fp;\nText: fopen(\"data.txt\", \"r\");\nBinary: fopen(\"data.bin\", \"rb\");",
        "code": """#include <stdio.h>

int main(void) {
    /* Demonstration of the three standard streams */
    fprintf(stdout, "=== Standard Streams Demonstration ===\\n");
    fprintf(stdout, "1. stdout: Normal output sent to standard display.\\n");
    fprintf(stderr, "2. stderr: Unbuffered error/diagnostic message.\\n\\n");

    int integerVal = 12345;
    printf("Storage Representation Comparison:\\n");
    printf("- In Text File:   '1','2','3','4','5' -> 5 ASCII bytes\\n");
    printf("- In Binary File: Stored as raw 32-bit integer -> %zu bytes (int size)\\n", 
           sizeof(integerVal));

    return 0;
}""",
        "output": """=== Standard Streams Demonstration ===
1. stdout: Normal output sent to standard display.
2. stderr: Unbuffered error/diagnostic message.

Storage Representation Comparison:
- In Text File:   '1','2','3','4','5' -> 5 ASCII bytes
- In Binary File: Stored as raw 32-bit integer -> 4 bytes (int size)""",
        "explanation": "1. `stdout` and `stderr` are pre-opened file pointers.\n2. `stderr` is unbuffered, so error messages appear on the console immediately without waiting for a newline or buffer flush.\n3. Large numbers stored as text consume more bytes, whereas binary storage is compact and exact.",
        "mistakes": [
            ("Assuming text files and binary files use different file pointer types.", "Both use the exact same `FILE *` pointer type; only the mode flag (`\"r\"` vs `\"rb\"`) dictates character translation behavior."),
            ("Using text mode (`\"w\"`) to write raw binary structures.", "On Windows, byte value 10 (`0x0A`, `\\n`) will be automatically translated to 13 and 10 (`0x0D 0x0A`), corrupting binary numeric data. Always use `\"rb\"` or `\"wb\"` for binary files.")
        ],
        "practice_q": "Why is `stderr` unbuffered while `stdout` is line-buffered by default?"
    },
    {
        "num": 106,
        "title": "The FILE Structure and File Pointer (FILE *fp)",
        "category": "File Fundamentals",
        "difficulty": "Fundamental",
        "exam_tags": ["Core Concept", "Viva Favorite"],
        "question": "What is the `FILE` structure defined in `<stdio.h>`? What does a file pointer `FILE *fp` represent, and why must file operations always pass this pointer?",
        "logic": "`FILE` is a typedef structure in `<stdio.h>` that stores state information about an active file stream: file descriptor, buffer address, current read/write offset, error flags, and end-of-file flag.",
        "concept": "1. The `FILE` Structure Contents:\n- Integer file descriptor assigned by the operating system kernel.\n- Pointer to the stream's internal memory buffer.\n- Current read/write position indicator (offset in bytes).\n- Flags for End-of-File (`EOF`) and error conditions.\n2. The File Pointer: `FILE *fp = fopen(...);`\n- The programmer never manipulates the fields of `struct _IO_FILE` directly.\n- The pointer acts as an opaque handle passed to all I/O functions (`fprintf`, `fscanf`, `fgetc`, `fclose`).\n3. Operating System Bridge: `fopen()` asks the OS kernel to open a file table entry and returns a pointer to the control structure.",
        "syntax": "FILE *fp = fopen(\"filename.txt\", \"mode\");",
        "code": """#include <stdio.h>

int main(void) {
    printf("=== FILE Handle and Pointer Inspection ===\\n");
    printf("sizeof(FILE *): %zu bytes (Opaque stream pointer handle)\\n\\n", sizeof(FILE *));

    /* Opening a temporary stream */
    FILE *fp = fopen("vtu_test.tmp", "w");
    if (fp == NULL) {
        perror("Failed to create file");
        return 1;
    }

    printf("File opened successfully! Stream Handle: %p\\n", (void*)fp);
    fprintf(fp, "Engineering Mathematics and C Programming 1BMATS101\\n");

    /* Closing the file flushes buffer and releases OS file handle */
    fclose(fp);
    fp = NULL;
    printf("File closed and handle neutralized to NULL.\\n");

    /* Clean up temporary file */
    remove("vtu_test.tmp");
    return 0;
}""",
        "output": """=== FILE Handle and Pointer Inspection ===
sizeof(FILE *): 8 bytes (Opaque stream pointer handle)

File opened successfully! Stream Handle: 0x55d4a2b9b2a0
File closed and handle neutralized to NULL.
""",
        "explanation": "1. `FILE *fp` is an 8-byte pointer holding the address of the file control block.\n2. `fprintf(fp, ...)` writes formatted text through the stream buffer.\n3. `fclose(fp)` flushes any buffered data to secondary storage and releases the OS file descriptor.",
        "mistakes": [
            ("Declaring `FILE f;` instead of `FILE *fp;`.", "The `FILE` structure is an opaque system type intended to be accessed exclusively via pointers."),
            ("Using a file pointer after calling `fclose(fp)`.", "Once closed, the file control block is freed. Accessing `fp` is a use-after-free bug. Always set `fp = NULL;` after `fclose()`.")
        ],
        "practice_q": "What is the maximum number of simultaneously open files allowed in standard C (`FOPEN_MAX`)?"
    },
    {
        "num": 107,
        "title": "fopen() and fclose(): Error Handling and Buffer Flushing",
        "category": "File Operations",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "Viva Must-Know"],
        "question": "Detail the prototypes and return values of `fopen()` and `fclose()`. Why is closing files mandatory in C? Explain buffer flushing with `fflush()`.",
        "logic": "`fopen()` opens a file stream, returning `NULL` on failure. `fclose()` flushes buffered data to disk, closes the file handle, and frees the `FILE` control structure.",
        "concept": "1. `FILE *fopen(const char *filename, const char *mode);`\n- Returns valid pointer on success; returns `NULL` on error (e.g. file not found, permission denied).\n- Mandatory Check: Always verify `if (fp == NULL)`.\n2. `int fclose(FILE *stream);`\n- Returns 0 on success; returns `EOF` on failure.\n3. Why `fclose()` is Mandatory:\n- Write operations are buffered in RAM. If the program terminates abruptly without `fclose()`, the final block of data in the buffer may never be written to disk (data loss).\n- The OS limits the number of open file descriptors per process. Leaking file handles leads to 'Too many open files' errors.\n4. `fflush(fp)`: Forces the runtime to write any buffered output data to disk immediately without closing the file.",
        "syntax": "if ((fp = fopen(name, mode)) == NULL) { perror(\"Error\"); return 1; }",
        "code": """#include <stdio.h>

int main(void) {
    const char *nonExistentFile = "non_existent_directory/invalid.txt";

    printf("=== Testing fopen() Failure & perror() ===\\n");
    FILE *fp = fopen(nonExistentFile, "r");

    if (fp == NULL) {
        printf(">> fopen returned NULL as expected!\\n");
        perror(">> System Error Description");
    } else {
        fclose(fp);
    }

    return 0;
}""",
        "output": """=== Testing fopen() Failure & perror() ===
>> fopen returned NULL as expected!
>> System Error Description: No such file or directory""",
        "explanation": "1. Opening a non-existent file in read mode `\"r\"` fails and returns `NULL`.\n2. `perror()` prints a human-readable explanation based on the global error code `errno` (\"No such file or directory\").\n3. This defensive check prevents null-pointer dereferences in file operations.",
        "mistakes": [
            ("Writing `fopen(path, \"r\")` without verifying if the return value is NULL.", "Attempting to read from a `NULL` file pointer causes an immediate segmentation fault."),
            ("Calling `fclose(fp)` when `fp` is NULL.", "Passing `NULL` to `fclose()` triggers undefined behavior and a crash on most operating systems.")
        ],
        "practice_q": "What does `fflush(NULL)` do when passed a null pointer?"
    },
    {
        "num": 108,
        "title": "Comprehensive File Opening Modes: r, w, a, r+, w+, a+, and Binary Modes",
        "category": "File Modes",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Theory", "Viva Must-Know", "VTU Exam Favorite"],
        "question": "Construct a comprehensive comparative reference table of all standard C file opening modes (`r`, `w`, `a`, `r+`, `w+`, `a+`, and their binary equivalents). Detail: File Existence Requirement, Initial Cursor Position, and Truncation Behavior.",
        "logic": "The mode string passed to `fopen()` defines whether reading, writing, or both are permitted, whether the file is created or truncated, and the initial file offset position.",
        "concept": "Comprehensive File Mode Reference Table:\n1. `\"r\"` (Read):\n- File must exist (fails and returns `NULL` if not found).\n- Cursor at beginning (offset 0).\n- File is NOT truncated.\n2. `\"w\"` (Write):\n- Creates file if it does not exist.\n- TRUNCATES (erases all existing content) to 0 bytes if file exists!\n- Cursor at beginning.\n3. `\"a\"` (Append):\n- Creates file if it does not exist.\n- Preserves existing content; all writes happen strictly at the END of the file.\n4. `\"r+\"` (Read & Write Update):\n- File must exist.\n- Does NOT truncate. Reads/writes start at beginning; overwrites existing bytes.\n5. `\"w+\"` (Write & Read Update):\n- Creates file if not found. TRUNCATES existing file to 0 bytes!\n6. `\"a+\"` (Append & Read Update):\n- Creates file if not found. Reads can seek anywhere; writes ALWAYS append to the end.\nBinary modes (`\"rb\"`, `\"wb\"`, `\"ab\"`, `\"r+b\"`, etc.): Exactly identical rules, but disables newline character translation.",
        "syntax": "fopen(\"file.txt\", \"r\") vs \"w\" vs \"a\" vs \"r+\"",
        "code": """#include <stdio.h>

int main(void) {
    const char *testFile = "mode_demo.txt";

    /* 1. Mode "w": Create and write initial content */
    FILE *fp = fopen(testFile, "w");
    if (fp != NULL) {
        fprintf(fp, "Line 1: Mathematics\\n");
        fclose(fp);
    }

    /* 2. Mode "a": Append new content to the end without erasing */
    fp = fopen(testFile, "a");
    if (fp != NULL) {
        fprintf(fp, "Line 2: C Programming\\n");
        fclose(fp);
    }

    /* 3. Mode "r": Read and verify combined contents */
    fp = fopen(testFile, "r");
    if (fp != NULL) {
        char line[100];
        printf("=== File Contents After 'w' followed by 'a' ===\\n");
        while (fgets(line, sizeof(line), fp) != NULL) {
            printf("%s", line);
        }
        fclose(fp);
    }

    remove(testFile);
    return 0;
}""",
        "output": """=== File Contents After 'w' followed by 'a' ===
Line 1: Mathematics
Line 2: C Programming""",
        "explanation": "1. Mode `\"w\"` creates `mode_demo.txt` and writes Line 1.\n2. Mode `\"a\"` opens the existing file, seeks to the end, and appends Line 2 without touching Line 1.\n3. Mode `\"r\"` reads back both lines, demonstrating preservation.",
        "mistakes": [
            ("Opening a file with mode `\"w\"` intending to append to it.", "Mode `\"w\"` immediately truncates the file to 0 bytes, permanently erasing all existing data! Always use `\"a\"` to append."),
            ("Assuming `\"r+\"` creates the file if it does not exist.", "`\"r+\"` requires the file to exist. If the file does not exist, `\"r+\"` fails and returns `NULL`.")
        ],
        "practice_q": "In mode `\"a+\"`, can you use `fseek()` to overwrite existing data in the middle of the file?"
    },
    {
        "num": 109,
        "title": "Character I/O in Files: fgetc(), fputc(), and File Copy Utility",
        "category": "File Operations",
        "difficulty": "Fundamental",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Explain character-by-character file I/O using `fgetc()` and `fputc()`. Why does `fgetc()` return an `int` rather than a `char`? Write a complete program to copy one file to another.",
        "logic": "`fgetc()` reads a single character from a file stream. It returns `int` because it must be able to return all valid `unsigned char` values (0 to 255) PLUS the special out-of-band sentinel constant `EOF` (typically -1).",
        "concept": "1. Prototypes:\n- `int fgetc(FILE *stream);`\n- `int fputc(int ch, FILE *stream);`\n2. Why `int` is Mandatory for `fgetc()`:\n- If you store the return value of `fgetc()` in a `char`, a file containing the valid byte `0xFF` (255) might be sign-extended to -1, prematurely terminating the read loop! Or `EOF` (-1) might not be recognized correctly. Always store the return value in an `int` variable (`int ch`).\n3. `EOF` Constant: A macro defined in `<stdio.h>` representing End-Of-File.",
        "syntax": "int ch;\nwhile ((ch = fgetc(src)) != EOF) fputc(ch, dest);",
        "code": """#include <stdio.h>

int copyFile(const char *sourcePath, const char *destPath) {
    FILE *src = fopen(sourcePath, "r");
    if (src == NULL) {
        perror("Error opening source file");
        return -1;
    }

    FILE *dest = fopen(destPath, "w");
    if (dest == NULL) {
        perror("Error opening destination file");
        fclose(src);
        return -1;
    }

    /* Note: ch MUST be declared as int, not char! */
    int ch;
    long long byteCount = 0;

    while ((ch = fgetc(src)) != EOF) {
        fputc(ch, dest);
        byteCount++;
    }

    fclose(src);
    fclose(dest);

    return (int)byteCount;
}

int main(void) {
    const char *file1 = "original.txt";
    const char *file2 = "copy.txt";

    /* Create sample source file */
    FILE *f = fopen(file1, "w");
    if (f != NULL) {
        fprintf(f, "VTU Engineering Mathematics & C Programming Study Portal\\n");
        fclose(f);
    }

    int bytesCopied = copyFile(file1, file2);
    printf("=== File Copy Utility ===\\n");
    printf("Successfully copied %d bytes from '%s' to '%s'!\\n", 
           bytesCopied, file1, file2);

    /* Verify copy */
    FILE *check = fopen(file2, "r");
    if (check != NULL) {
        char buffer[100];
        fgets(buffer, sizeof(buffer), check);
        printf("Verified Copy Content: \\\"%s\\\"\\n", buffer);
        fclose(check);
    }

    remove(file1);
    remove(file2);
    return 0;
}""",
        "output": """=== File Copy Utility ===
Successfully copied 57 bytes from 'original.txt' to 'copy.txt'!
Verified Copy Content: "VTU Engineering Mathematics & C Programming Study Portal
" """,
        "explanation": "1. `ch` is declared as `int` to cleanly distinguish between valid byte values (0-255) and `EOF` (-1).\n2. The loop reads each byte with `fgetc()` and writes it with `fputc()`.\n3. The destination file is an exact copy of the source.",
        "mistakes": [
            ("Declaring `char ch;` when reading with `fgetc()`.", "This is a classic C trap: on platforms where `char` is signed, byte `0xFF` matches `EOF`, stopping file reading prematurely. On platforms where `char` is unsigned, `ch` can never equal `EOF`, causing an infinite loop! Always declare `int ch;`."),
            ("Not closing the source file if opening the destination fails.", "Creates a resource leak. Always close any opened handles before returning on error.")
        ],
        "practice_q": "What is the equivalent function to `fgetc(stdin)`?"
    },
    {
        "num": 110,
        "title": "Line-Oriented File I/O: fgets(), fputs(), and Word/Line Counter",
        "category": "File Operations",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Explain line-oriented file operations using `fgets()` and `fputs()`. Write a complete C program to count the total number of characters, words, and lines in a text file.",
        "logic": "`fgets()` reads an entire line up to a newline character or buffer limit. Word counting tracks state transitions between whitespace and non-whitespace characters.",
        "concept": "1. `char *fgets(char *str, int n, FILE *stream);`\n- Reads at most `n - 1` characters.\n- Retains the newline character `\\n` if encountered.\n- Appends `\\0` automatically.\n- Returns `NULL` upon reaching `EOF` or on error.\n2. `int fputs(const char *str, FILE *stream);`\n- Writes null-terminated string to stream (does NOT append newline automatically like `puts()` does).\n3. Word Counter Algorithm: Use an `inWord` boolean flag. When transitioning from space to non-space, increment word count.",
        "syntax": "while (fgets(buffer, sizeof(buffer), fp) != NULL) { ... }",
        "code": """#include <stdio.h>
#include <ctype.h>

void analyzeTextFile(const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        perror("Unable to open file");
        return;
    }

    int characters = 0;
    int words = 0;
    int lines = 0;
    int inWord = 0;
    int ch;

    while ((ch = fgetc(fp)) != EOF) {
        characters++;

        if (ch == '\\n') {
            lines++;
        }

        if (isspace((unsigned char)ch)) {
            inWord = 0;
        } else if (!inWord) {
            inWord = 1;
            words++;
        }
    }

    /* If file does not end with a newline, count the final line */
    if (characters > 0 && ch != '\\n') {
        lines++;
    }

    fclose(fp);

    printf("=== Text File Analytics for '%s' ===\\n", filename);
    printf("Total Characters: %d\\n", characters);
    printf("Total Words:      %d\\n", words);
    printf("Total Lines:      %d\\n", lines);
}

int main(void) {
    const char *sampleFile = "vtu_sample.txt";

    FILE *f = fopen(sampleFile, "w");
    if (f != NULL) {
        fputs("VTU Engineering Calculus\\n", f);
        fputs("Linear Algebra and Differential Equations\\n", f);
        fputs("Computer Programming in C Language\\n", f);
        fclose(f);
    }

    analyzeTextFile(sampleFile);
    remove(sampleFile);
    return 0;
}""",
        "output": """=== Text File Analytics for 'vtu_sample.txt' ===
Total Characters: 104
Total Words:      12
Total Lines:      3""",
        "explanation": "1. Program examines each character, counting characters, words, and lines.\n2. `inWord` flag correctly counts 12 words across 3 lines.\n3. Demonstrates robust text file parsing.",
        "mistakes": [
            ("Assuming lines equal newline characters `\\n`.", "A file with text that does not end in a trailing newline will have its last line missed unless handled explicitly."),
            ("Using `feof()` as the loop condition: `while (!feof(fp))`.", "The `feof()` flag is only set AFTER a read operation attempts to read past the end of the file. This causes the last line to be processed twice! Always check the return value of `fgets()` or `fgetc()` directly.")
        ],
        "practice_q": "Why does `while (!feof(fp))` process the last line of a file twice?"
    },
    {
        "num": 111,
        "title": "Formatted File I/O: fprintf() and fscanf() with Student Records",
        "category": "File Operations",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "Exam Question"],
        "question": "Explain formatted file I/O using `fprintf()` and `fscanf()`. Write a complete C program to write an array of student records to a text file and read them back safely.",
        "logic": "`fprintf()` formats and writes text to a file stream. `fscanf()` parses formatted text from a file into variables, returning the number of successfully parsed fields or `EOF`.",
        "concept": "1. Prototypes:\n- `int fprintf(FILE *stream, const char *format, ...);`\n- `int fscanf(FILE *stream, const char *format, ...);`\n2. Return Value of `fscanf()`: Returns the number of successfully matched and assigned input items. Check `if (fscanf(...) == EXPECTED_COUNT)` to detect corrupt or truncated records.\n3. Format Matching: Use clear delimiters (like spaces, commas, or tabs) between fields so `fscanf()` can parse them reliably.",
        "syntax": "fprintf(fp, \"%d %s %lf\\n\", id, name, marks);\nfscanf(fp, \"%d %s %lf\", &id, name, &marks);",
        "code": """#include <stdio.h>

struct StudentRecord {
    int rollNo;
    char name[30];
    double cgpa;
};

int main(void) {
    const char *filename = "students.txt";
    struct StudentRecord originalList[3] = {
        {101, "Aarav", 9.45},
        {102, "Sneha", 9.82},
        {103, "Rohan", 8.75}
    };

    /* 1. Write Records using fprintf() */
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) return 1;

    for (int i = 0; i < 3; i++) {
        fprintf(fp, "%d %s %.2f\\n", 
                originalList[i].rollNo, originalList[i].name, originalList[i].cgpa);
    }
    fclose(fp);
    printf("3 Student records written using fprintf().\\n\\n");

    /* 2. Read Records back using fscanf() */
    fp = fopen(filename, "r");
    if (fp == NULL) return 1;

    printf("=== Records Retrieved using fscanf() ===\\n");
    printf("%-8s | %-12s | %-6s\\n", "ROLL NO", "NAME", "CGPA");
    printf("-----------------------------\\n");

    struct StudentRecord readRecord;
    while (fscanf(fp, "%d %29s %lf", 
                  &readRecord.rollNo, readRecord.name, &readRecord.cgpa) == 3) {
        printf("%-8d | %-12s | %-6.2f\\n", 
               readRecord.rollNo, readRecord.name, readRecord.cgpa);
    }

    fclose(fp);
    remove(filename);
    return 0;
}""",
        "output": """3 Student records written using fprintf().

=== Records Retrieved using fscanf() ===
ROLL NO  | NAME         | CGPA  
-----------------------------
101      | Aarav        | 9.45  
102      | Sneha        | 9.82  
103      | Rohan        | 8.75  """,
        "explanation": "1. `fprintf()` writes formatted text: `101 Aarav 9.45\\n`.\n2. `fscanf()` parses each line into `rollNo`, `name`, and `cgpa`.\n3. The loop condition checks `== 3` to verify all 3 fields were parsed, terminating cleanly when the end of the file is reached.",
        "mistakes": [
            ("Writing names with spaces using `%s` without a scanset in `fscanf()`.", "`%s` stops at spaces. If a name is \"John Doe\", `fscanf` assigns \"John\" to name and attempts to parse \"Doe\" as the double CGPA, causing input failure."),
            ("Forgetting `&` for scalar variables in `fscanf()`.", "Like `scanf()`, `fscanf()` requires pointer addresses for variables. Omitting `&` causes segmentation faults.")
        ],
        "practice_q": "How does comma-separated values (CSV) parsing differ when using `fscanf()`?"
    },
    {
        "num": 112,
        "title": "Binary File I/O: fwrite() and fread() for Direct Memory Blocks",
        "category": "Binary File Operations",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "VTU Exam Favorite"],
        "question": "Explain block-based binary file I/O using `fwrite()` and `fread()`. Why is binary I/O significantly faster than text I/O? Write a program storing and retrieving binary structure records.",
        "logic": "`fwrite()` and `fread()` transfer contiguous bytes directly between RAM and secondary storage without ASCII text conversion, making binary I/O much faster for complex data structures.",
        "concept": "1. Prototypes:\n- `size_t fwrite(const void *ptr, size_t size, size_t count, FILE *stream);`\n- `size_t fread(void *ptr, size_t size, size_t count, FILE *stream);`\n2. Parameters:\n- `ptr`: Memory address of data buffer.\n- `size`: Size of each element in bytes (`sizeof(struct Type)`).\n- `count`: Number of elements to write/read.\n- `stream`: Open binary file pointer (`\"wb\"` or `\"rb\"`).\n3. Return Value: Returns the number of items successfully written or read. Check `if (fread(...) == count)` to verify complete reads.\n4. Advantages: No string parsing/conversion overhead, preserves exact floating-point bit patterns, and enables direct random access with `fseek()`.",
        "syntax": "fwrite(&record, sizeof(record), 1, fp);\nfread(&record, sizeof(record), 1, fp);",
        "code": """#include <stdio.h>

struct SensorData {
    int sensorId;
    double temperature;
    double pressure;
};

int main(void) {
    const char *binaryFile = "sensor.bin";

    struct SensorData readings[2] = {
        {101, 28.5, 1013.25},
        {102, 31.2, 1011.80}
    };

    /* 1. Write binary data block using fwrite() */
    FILE *fp = fopen(binaryFile, "wb");
    if (fp == NULL) return 1;

    size_t itemsWritten = fwrite(readings, sizeof(struct SensorData), 2, fp);
    fclose(fp);
    printf("Wrote %zu binary records (%zu bytes) to '%s'\\n\\n", 
           itemsWritten, sizeof(readings), binaryFile);

    /* 2. Read binary data block using fread() */
    fp = fopen(binaryFile, "rb");
    if (fp == NULL) return 1;

    struct SensorData loadedReadings[2];
    size_t itemsRead = fread(loadedReadings, sizeof(struct SensorData), 2, fp);
    fclose(fp);

    printf("=== Binary Data Retrieved via fread() (%zu records) ===\\n", itemsRead);
    for (size_t i = 0; i < itemsRead; i++) {
        printf("Sensor %d | Temp: %.1f C | Pressure: %.2f hPa\\n", 
               loadedReadings[i].sensorId, 
               loadedReadings[i].temperature, 
               loadedReadings[i].pressure);
    }

    remove(binaryFile);
    return 0;
}""",
        "output": """Wrote 2 binary records (48 bytes) to 'sensor.bin'

=== Binary Data Retrieved via fread() (2 records) ===
Sensor 101 | Temp: 28.5 C | Pressure: 1013.25 hPa
Sensor 102 | Temp: 31.2 C | Pressure: 1011.80 hPa""",
        "explanation": "1. `fwrite()` writes the raw 48-byte memory block directly to disk.\n2. `fread()` loads the bytes back into `loadedReadings` in a single operation.\n3. The floating-point values are read back with exact bit-level precision.",
        "mistakes": [
            ("Writing structures containing pointers with `fwrite()`.", "Writing a pointer to a file stores only a memory address. When the program runs again, that memory address is invalid! Only write flat data structures to files."),
            ("Opening binary files without the `\"b\"` flag on Windows.", "Omitting `\"b\"` causes Windows runtime to treat `0x0A` as newline, corrupting binary data.")
        ],
        "practice_q": "What is the return value of `fread()` when fewer elements are read than requested?"
    },
    {
        "num": 113,
        "title": "Random Access in Files: fseek(), ftell(), and rewind()",
        "category": "File Positioning",
        "difficulty": "Intermediate",
        "exam_tags": ["Lab Program", "VTU Exam Favorite", "Core Concept"],
        "question": "Explain random access in C files. Detail `fseek()`, `ftell()`, and `rewind()`. Explain the three origin constants (`SEEK_SET`, `SEEK_CUR`, `SEEK_END`) and write a program to compute file size in bytes.",
        "logic": "By default, files are accessed sequentially. File positioning functions allow moving the read/write cursor to an arbitrary byte offset without reading intervening data.",
        "concept": "1. `int fseek(FILE *stream, long offset, int origin);`\n- `SEEK_SET`: Offset is relative to the BEGINNING of the file.\n- `SEEK_CUR`: Offset is relative to the CURRENT cursor position.\n- `SEEK_END`: Offset is relative to the END of the file (usually negative or 0).\n- Returns 0 on success; non-zero on error.\n2. `long ftell(FILE *stream);`\n- Returns current byte offset of the cursor from the beginning of the file.\n3. `void rewind(FILE *stream);`\n- Resets cursor to beginning: equivalent to `fseek(fp, 0L, SEEK_SET)` and clears error flags.\n4. File Size Idiom:\nSeek to end with `fseek(fp, 0L, SEEK_END)`, then read position with `long size = ftell(fp)`.",
        "syntax": "fseek(fp, 0L, SEEK_END);\nlong size = ftell(fp);\nrewind(fp);",
        "code": """#include <stdio.h>

int main(void) {
    const char *testFile = "position_test.bin";

    /* Create a binary file containing 5 integers */
    FILE *fp = fopen(testFile, "wb");
    if (fp == NULL) return 1;

    int values[] = {100, 200, 300, 400, 500};
    fwrite(values, sizeof(int), 5, fp);
    fclose(fp);

    /* Open for random access reading */
    fp = fopen(testFile, "rb");
    if (fp == NULL) return 1;

    /* 1. Calculate File Size in Bytes using fseek and ftell */
    fseek(fp, 0L, SEEK_END); /* Seek to end */
    long fileSize = ftell(fp);
    printf("=== File Size Calculation via ftell() ===\\n");
    printf("File Size: %ld bytes (%ld integers of size %zu)\\n\\n", 
           fileSize, fileSize / (long)sizeof(int), sizeof(int));

    /* 2. Reset cursor with rewind() */
    rewind(fp);
    printf("After rewind(), cursor offset is at: %ld bytes\\n\\n", ftell(fp));

    /* 3. Random Access: Jump directly to 3rd integer (index 2) without reading index 0 or 1 */
    long targetOffset = 2 * sizeof(int); /* Offset for 3rd element */
    fseek(fp, targetOffset, SEEK_SET);

    int readVal;
    fread(&readVal, sizeof(int), 1, fp);
    printf("Random Access Result: 3rd integer at offset %ld is: %d\\n", 
           targetOffset, readVal);

    fclose(fp);
    remove(testFile);
    return 0;
}""",
        "output": """=== File Size Calculation via ftell() ===
File Size: 20 bytes (5 integers of size 4)

After rewind(), cursor offset is at: 0 bytes

Random Access Result: 3rd integer at offset 8 is: 300""",
        "explanation": "1. `fseek(fp, 0L, SEEK_END)` positions the cursor at the end; `ftell(fp)` returns 20 bytes.\n2. `rewind(fp)` returns the cursor to offset 0.\n3. `fseek(fp, 8, SEEK_SET)` jumps directly to byte 8, reading the 3rd integer (`300`) in $O(1)$ time.",
        "mistakes": [
            ("Using `fseek()` with arbitrary byte offsets on text files.", "On text files, character encoding and newline translations make arbitrary byte offsets unpredictable. Portable `fseek()` on text files should only use 0 with `SEEK_SET`, `SEEK_CUR`, or `SEEK_END`, or values returned by `ftell()`."),
            ("Assuming `fseek()` checks if you seek past the end of the file.", "Seeking past the end of a file is permitted by standard C. The file will only expand if you subsequently write data there.")
        ],
        "practice_q": "How can you update the N-th record in a binary file in place using `fseek()` and `fwrite()`?"
    },
    {
        "num": 114,
        "title": "Error Handling in Files: feof(), ferror(), clearerr(), and perror()",
        "category": "File Operations",
        "difficulty": "Intermediate",
        "exam_tags": ["Viva Must-Know", "Core Concept"],
        "question": "Differentiate between `feof()` and `ferror()`. Explain why checking `feof()` before performing a read operation is an anti-pattern, and demonstrate proper error diagnosis with `perror()`.",
        "logic": "`feof()` indicates whether a previous read operation encountered the End-of-File marker. `ferror()` indicates whether a hardware I/O error occurred on the stream.",
        "concept": "1. `int feof(FILE *stream);`: Returns non-zero only AFTER a read operation has attempted to read past the end of the file.\n2. `int ferror(FILE *stream);`: Returns non-zero if a read or write operation encountered an I/O error (e.g. disk full, bad sector, hardware disconnect).\n3. `void clearerr(FILE *stream);`: Clears both the EOF and error indicator flags for the stream.\n4. `void perror(const char *prefix);`: Translates the global `errno` code into a human-readable error description and prints it to `stderr`.",
        "syntax": "if (ferror(fp)) { perror(\"I/O Error\"); clearerr(fp); }",
        "code": """#include <stdio.h>

int main(void) {
    const char *testFile = "test_err.txt";

    /* Create sample file with 2 integers */
    FILE *fp = fopen(testFile, "w");
    if (fp != NULL) {
        fprintf(fp, "42 99\\n");
        fclose(fp);
    }

    fp = fopen(testFile, "r");
    if (fp == NULL) return 1;

    int val;
    printf("=== Testing feof() and ferror() States ===\\n");

    /* Reading records */
    while (fscanf(fp, "%d", &val) == 1) {
        printf("Read integer: %d\\n", val);
    }

    /* Check status flags after read loop finishes */
    if (feof(fp)) {
        printf(">> Stream reached End-Of-File cleanly (feof is TRUE)\\n");
    }
    if (ferror(fp)) {
        printf(">> Stream encountered a read error! (ferror is TRUE)\\n");
    }

    fclose(fp);
    remove(testFile);
    return 0;
}""",
        "output": """=== Testing feof() and ferror() States ===
Read integer: 42
Read integer: 99
>> Stream reached End-Of-File cleanly (feof is TRUE)""",
        "explanation": "1. Both numbers (42 and 99) are read successfully.\n2. The next `fscanf()` attempts to read past the end, setting the EOF flag and returning `EOF`.\n3. `feof(fp)` evaluates to true, confirming clean termination at end-of-file rather than an error.",
        "mistakes": [
            ("Using `while(!feof(fp))` as loop condition.", "Because `feof()` only becomes true AFTER an attempted read past EOF, the loop body executes one extra time with stale data. Always check the return value of the read function itself."),
            ("Assuming `ferror()` clears itself on the next call.", "The error flag remains set until explicitly reset using `clearerr(fp)` or when the file is closed.")
        ],
        "practice_q": "What header file defines the global variable `errno` and its standard error constants?"
    },
    {
        "num": 115,
        "title": "Introduction to C Preprocessor: The # Symbol and Translation Phases",
        "category": "Preprocessor",
        "difficulty": "Fundamental",
        "exam_tags": ["Core Concept", "Viva Must-Know"],
        "question": "What is the C Preprocessor? Explain how preprocessor directives (beginning with `#`) differ from C statements. Describe the preprocessing stage in the compilation pipeline.",
        "logic": "The C Preprocessor is a text-processing tool that manipulates source code before the compiler performs syntax analysis and code generation.",
        "concept": "1. Directives begin with `#` (e.g. `#include`, `#define`, `#ifdef`).\n2. Key Differences from C Statements:\n- Handled during Phase 4 of translation before syntax parsing.\n- Do NOT end with a semicolon `;`.\n- Operates on text tokens and lines, with no knowledge of types, scopes, or variables.\n- Lines can be extended across multiple lines using a backslash `\\`.\n3. Primary Preprocessor Tasks:\n- Header inclusion: Replacing `#include` with the full content of the header file.\n- Macro expansion: Replacing macro names with their defined replacement tokens.\n- Conditional compilation: Including or excluding code blocks based on compile-time conditions.\n- Stripping comments: Removing single-line `//` and multi-line `/* */` comments.",
        "syntax": "#directive arguments",
        "code": """#include <stdio.h>

/* Multi-line preprocessor macro using backslash line continuation */
#define PRINT_BANNER() \\
    do { \\
        printf("======================================\\n"); \\
        printf("|   VTU APPLIED MATHEMATICS & C       |\\n"); \\
        printf("======================================\\n"); \\
    } while (0)

int main(void) {
    PRINT_BANNER();
    printf("Preprocessor completed text expansion before compilation.\\n");
    return 0;
}""",
        "output": """======================================
|   VTU APPLIED MATHEMATICS & C       |
======================================
Preprocessor completed text expansion before compilation.""",
        "explanation": "1. `#include <stdio.h>` is processed by the preprocessor, pasting standard I/O prototypes.\n2. `PRINT_BANNER()` is expanded textually inline before compilation.\n3. The `do { ... } while (0)` pattern ensures the macro behaves safely as a single statement when used in `if-else` blocks.",
        "mistakes": [
            ("Adding a semicolon at the end of `#define` (e.g. `#define MAX 100;`).", "The semicolon is included in the replacement text, causing syntax errors in expressions like `int a = MAX * 2;` (which expands to `int a = 100; * 2;`)."),
            ("Confusing preprocessor directives with executable runtime code.", "Directives execute at compile time, not at runtime.")
        ],
        "practice_q": "How can you view the preprocessed output of a file using GCC command-line options?"
    },
    {
        "num": 116,
        "title": "#include Directive: Angle Brackets (<>) vs Double Quotes (\"\")",
        "category": "Preprocessor",
        "difficulty": "Fundamental",
        "exam_tags": ["Viva Must-Know", "Core Foundation"],
        "question": "What is the `#include` directive? Explain the difference in header search paths between `#include <filename.h>` and `#include \"filename.h\"`.",
        "logic": "`#include` directs the preprocessor to locate the specified header file, read its entire contents, and replace the `#include` line with that content textually.",
        "concept": "1. `#include <filename.h>` (Angle Brackets):\n- Used for standard system headers (e.g. `<stdio.h>`, `<stdlib.h>`, `<math.h>`).\n- Search Path: Searches ONLY in pre-configured system include directories (e.g. `/usr/include`, MSVC/GCC include paths).\n2. `#include \"filename.h\"` (Double Quotes):\n- Used for user-defined project headers.\n- Search Path: Searches FIRST in the directory containing the current source file. If not found there, falls back to the system include directories.\n3. Path Inclusion: Command line flag `-I /path/to/headers` adds custom directories to the search path.",
        "syntax": "#include <system_header.h>\n#include \"my_custom_header.h\"",
        "code": """#include <stdio.h>

int main(void) {
    printf("=== Header Inclusion Strategy ===\\n");
    printf("- #include <stdio.h>: Searches System Include Directories first.\\n");
    printf("- #include \"my_math.h\": Searches Current Project Folder first, then System.\\n");
    return 0;
}""",
        "output": """=== Header Inclusion Strategy ===
- #include <stdio.h>: Searches System Include Directories first.
- #include "my_math.h": Searches Current Project Folder first, then System.""",
        "explanation": "1. System headers use angle brackets `<>`.\n2. Project-specific headers use double quotes `\"\"` to allow local file overrides.\n3. Using the correct inclusion syntax avoids build issues and search path confusion.",
        "mistakes": [
            ("Using `<my_header.h>` for local files.", "The preprocessor will search only system directories, failing with `No such file or directory`."),
            ("Including `.c` source files with `#include \"file.c\"`.", "Including `.c` files causes duplicate symbol definitions during linking. Always include `.h` header files containing declarations, and link compiled `.o` object files together.")
        ],
        "practice_q": "What happens if a header file includes itself directly or indirectly without header guards?"
    },
    {
        "num": 117,
        "title": "#define Object-Like Macros vs const Variables",
        "category": "Preprocessor",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Theory", "Viva Favorite"],
        "question": "Explain Object-Like Macros in C. Compare `#define` constants with `const` qualified variables across Type Safety, Debuggability, Memory Allocation, and Scope.",
        "logic": "An object-like macro `#define IDENTIFIER replacement_list` performs textual token replacement. A `const` variable is a typed, scoped variable in read-only memory.",
        "concept": "Comparison Table:\n1. Type Safety:\n- `#define`: Untyped. The preprocessor performs raw text substitution without type checking.\n- `const`: Strongly typed. The compiler enforces type checking and implicit conversions.\n2. Scope:\n- `#define`: File scope from point of definition onward; ignores block braces `{}`.\n- `const`: Respects block scope; local variables are visible only within their enclosing block.\n3. Debuggability:\n- `#define`: Macro names are replaced before compilation, so they may not appear in debuggers (unless compiled with `-g3`).\n- `const`: Stored in symbol tables; inspectable in debuggers (GDB, LLDB).\n4. Memory Allocation:\n- `#define`: Consumes zero RAM (inlined into instructions as immediate constants).\n- `const`: Stored in `.rodata` read-only data segment (can take its address with `&`).",
        "syntax": "#define MAX_BUFFER 1024\nconst int MaxBuffer = 1024;",
        "code": """#include <stdio.h>

#define MAX_CONNECTIONS 100
const int MaxConnectionsConst = 100;

int main(void) {
    printf("Macro Constant: %d\\n", MAX_CONNECTIONS);
    printf("const Variable: %d\\n", MaxConnectionsConst);
    printf("Address of const: %p (Real memory allocation!)\\n", 
           (void*)&MaxConnectionsConst);

    /* Address of macro: &MAX_CONNECTIONS -> Compile Error! */

    return 0;
}""",
        "output": """Macro Constant: 100
const Variable: 100
Address of const: 0x55d4a1b02008 (Real memory allocation!)""",
        "explanation": "1. `MAX_CONNECTIONS` is replaced with `100` before syntax analysis.\n2. `MaxConnectionsConst` is a typed integer residing in `.rodata`.\n3. You can take the address of `MaxConnectionsConst`, but not of a macro.",
        "mistakes": [
            ("Defining macros inside a function expecting local scope.", "Macros do not respect function or block boundaries. A macro defined inside a function remains defined for the rest of the file."),
            ("Assuming `const` variables can be used as case labels in legacy C.", "In C89/C99, `const` variables are not considered compile-time constant expressions and cannot be used in `case` labels. `#define` macros can be used in `case` labels.")
        ],
        "practice_q": "Can you use a `const int` variable to specify the size of a standard array in C89?"
    },
    {
        "num": 118,
        "title": "#define Function-Like Macros: Argument Parenthesizing and Precedence Hazards",
        "category": "Preprocessor",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Question", "Viva Must-Know", "Trap Favorite"],
        "question": "What is a Function-Like Macro? Why MUST all macro parameters and the overall macro expression be enclosed in parentheses? Demonstrate the `SQUARE(x)` precedence trap.",
        "logic": "A function-like macro takes arguments and substitutes them textually into the replacement list. Because substitution happens before expression evaluation, omitting parentheses leads to unexpected operator precedence bugs.",
        "concept": "The `SQUARE` Precedence Trap:\n1. Flawed Definition: `#define SQUARE(x) x * x`\n- Evaluating `SQUARE(2 + 3)` expands textually to: `2 + 3 * 2 + 3`\n- Multiplication takes precedence: `2 + (3 * 2) + 3 = 2 + 6 + 3 = 11` (Incorrect! Expected $(2+3)^2 = 25$!).\n2. Fixed with Parameter Parentheses: `#define SQUARE(x) (x) * (x)`\n- Still flawed! Evaluating `100 / SQUARE(5)` expands to `100 / (5) * (5)` $\\to$ `(100 / 5) * 5 = 100` (Incorrect! Expected $100 / 25 = 4$!).\n3. Correct Rule: Enclose EVERY parameter AND the ENTIRE expression in parentheses:\n`#define SQUARE(x) (((x) * (x)))`.",
        "syntax": "#define MACRO(a, b) (((a) > (b)) ? (a) : (b))",
        "code": """#include <stdio.h>

/* Flawed macro without parameter parentheses */
#define FLAWED_SQUARE(x) x * x

/* Fully guarded macro */
#define SAFE_SQUARE(x) (((x) * (x)))

int main(void) {
    int val = 2 + 3;

    printf("=== Macro Parenthesizing Trap ===\\n");
    printf("Evaluating (2 + 3)^2:\\n");
    printf("FLAWED_SQUARE(2 + 3) expands to '2 + 3 * 2 + 3' = %d (BUG!)\\n", 
           FLAWED_SQUARE(2 + 3));
    printf("SAFE_SQUARE(2 + 3)   expands to '(((2 + 3) * (2 + 3)))' = %d (CORRECT!)\\n", 
           SAFE_SQUARE(2 + 3));

    return 0;
}""",
        "output": """=== Macro Parenthesizing Trap ===
Evaluating (2 + 3)^2:
FLAWED_SQUARE(2 + 3) expands to '2 + 3 * 2 + 3' = 11 (BUG!)
SAFE_SQUARE(2 + 3)   expands to '(((2 + 3) * (2 + 3)))' = 25 (CORRECT!)""",
        "explanation": "1. `FLAWED_SQUARE(2 + 3)` evaluates to `11` instead of `25` due to operator precedence.\n2. `SAFE_SQUARE(2 + 3)` groups the addition first, producing `(5) * (5) = 25`.\n3. Always parenthesize macro parameters and the full macro expression.",
        "mistakes": [
            ("Passing side-effect expressions to macros: `SQUARE(a++)`.", "Because `x` appears twice in `(x) * (x)`, `a++` is evaluated TWICE, causing undefined behavior and unintended double increments!"),
            ("Putting a space between macro name and opening parenthesis: `#define MAX (a, b)`.", "The preprocessor treats `(a, b)` as the replacement text of an object-like macro, not parameters!")
        ],
        "practice_q": "What will `SQUARE(x++)` do if `x = 5`?"
    },
    {
        "num": 119,
        "title": "Macros vs Inline Functions: Type Checking, Expansion, and Modern Best Practices",
        "category": "Preprocessor vs Compiler",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Theory", "Viva Must-Know"],
        "question": "Compare Function-Like Macros with C99 `inline` functions. Why are inline functions generally preferred over complex macros in modern C software engineering?",
        "logic": "Inline functions provide the performance benefit of inlined machine code while preserving full compiler type checking, parameter isolation, and proper debugging support.",
        "concept": "Comparison Table:\n1. Mechanism:\n- Macro: Textual token substitution by preprocessor.\n- Inline Function: Actual function compiled by compiler; inlined at optimization time (`-O2`).\n2. Type Checking:\n- Macro: No type checking (accepts any expression, risking silent conversion errors).\n- Inline Function: Strict compiler argument type validation.\n3. Side-Effect Hazards:\n- Macro: Double evaluation bug (`MAX(a++, b)` increments `a` twice).\n- Inline Function: Arguments evaluated exactly once before inlining, safely.\n4. Debugging:\n- Macro: Cannot set breakpoints or step through in a debugger.\n- Inline Function: Supports source-level debugging.\nModern Rule: Use `static inline` functions for logic; reserve `#define` for conditional compilation and header guards.",
        "syntax": "static inline int max(int a, int b) { return a > b ? a : b; }",
        "code": """#include <stdio.h>

#define MACRO_MAX(a, b) (((a) > (b)) ? (a) : (b))

static inline int inlineMax(int a, int b) {
    return (a > b) ? a : b;
}

int main(void) {
    int x1 = 5, y1 = 10;
    int x2 = 5, y2 = 10;

    printf("=== Macro vs Inline Side-Effect Demonstration ===\\n");

    /* Flawed evaluation with macro: y1 is evaluated and incremented twice */
    int mResult = MACRO_MAX(x1, y1++);
    printf("MACRO_MAX:  result = %d, y1 = %d (Incremented twice!)\\n", mResult, y1);

    /* Safe evaluation with inline function */
    int iResult = inlineMax(x2, y2++);
    printf("inlineMax:  result = %d, y2 = %d (Incremented safely once)\\n", iResult, y2);

    return 0;
}""",
        "output": """=== Macro vs Inline Side-Effect Demonstration ===
MACRO_MAX:  result = 11, y1 = 12 (Incremented twice!)
inlineMax:  result = 10, y2 = 11 (Incremented safely once)""",
        "explanation": "1. In `MACRO_MAX`, `y1++` is substituted twice, incrementing `y1` from 10 to 12.\n2. In `inlineMax`, `y2++` is evaluated once as a function argument, incrementing `y2` cleanly to 11.\n3. Inline functions eliminate macro side-effect bugs while retaining full execution speed.",
        "mistakes": [
            ("Writing large, multi-line functions as `inline`.", "Inlining large functions bloats the executable binary size and can degrade CPU instruction cache performance."),
            ("Assuming `inline` forces the compiler to inline.", "The `inline` keyword is a hint. The compiler makes the final decision based on optimization flags and function complexity.")
        ],
        "practice_q": "What compiler optimization flag in GCC activates inline function expansion?"
    },
    {
        "num": 120,
        "title": "Preprocessor Operators: Stringizing (#) and Token-Pasting (##)",
        "category": "Advanced Preprocessor",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Question", "Viva Favorite"],
        "question": "Explain the preprocessor operators `#` (Stringizing) and `##` (Token-Pasting). Provide working code demonstrations showing how they generate debug prints and synthesize identifiers.",
        "logic": "The `#` operator converts a macro parameter into a quoted string literal. The `##` operator concatenates two tokens into a single valid token during preprocessing.",
        "concept": "1. Stringizing Operator `#`:\n- Converts macro argument text into a string literal.\n- Example: `#define PRINT_INT(var) printf(#var \" = %d\\n\", var)`\n- Calling `PRINT_INT(count);` expands to `printf(\"count\" \" = %d\\n\", count);`.\n2. Token-Pasting Operator `##`:\n- Merges two tokens into one.\n- Example: `#define MAKE_VAR(prefix, id) prefix##id`\n- Calling `MAKE_VAR(student, 1)` expands to `student1`.\n- Commonly used in code generators, dispatch tables, and generic macro libraries.",
        "syntax": "#param -> \"param\"\ntoken1 ## token2 -> token1token2",
        "code": """#include <stdio.h>

/* Stringizing Operator: Converts variable name into a string */
#define PRINT_EXPR(expr) \\
    printf("Expression: %s -> Evaluates to: %d\\n", #expr, (expr))

/* Token-Pasting Operator: Merges tokens to synthesize identifier */
#define DECLARE_REGISTER(regName, defaultVal) \\
    int reg_##regName = defaultVal

int main(void) {
    int speed = 85;
    int limit = 60;

    printf("=== Stringizing Operator (#) ===\\n");
    PRINT_EXPR(speed > limit);
    PRINT_EXPR(speed * 2 + 10);

    printf("\\n=== Token-Pasting Operator (##) ===\\n");
    DECLARE_REGISTER(Status, 1);  /* Creates: int reg_Status = 1; */
    DECLARE_REGISTER(Control, 5); /* Creates: int reg_Control = 5; */

    printf("reg_Status:  %d\\n", reg_Status);
    printf("reg_Control: %d\\n", reg_Control);

    return 0;
}""",
        "output": """=== Stringizing Operator (#) ===
Expression: speed > limit -> Evaluates to: 1
Expression: speed * 2 + 10 -> Evaluates to: 180

=== Token-Pasting Operator (##) ===
reg_Status:  1
reg_Control: 5""",
        "explanation": "1. `#expr` converts `speed > limit` into the string `\"speed > limit\"`.\n2. `reg_##regName` concatenates `reg_` with `Status` to create the identifier `reg_Status`.\n3. Both operators demonstrate C's compile-time metaprogramming capabilities.",
        "mistakes": [
            ("Using `#` or `##` outside macro definitions.", "These operators are strictly preprocessor operators and have no meaning in regular C code."),
            ("Pasting tokens that produce an invalid C token.", "Concatenating `12` and `abc` produces `12abc`, which is an invalid identifier and causes a compiler error.")
        ],
        "practice_q": "Why is an extra layer of macro indirection needed when stringizing the result of another macro?"
    },
    {
        "num": 121,
        "title": "Conditional Compilation: #ifdef, #ifndef, #if, #else, #elif, and #endif",
        "category": "Conditional Compilation",
        "difficulty": "Fundamental",
        "exam_tags": ["Exam Question", "Viva Must-Know"],
        "question": "What is conditional compilation? Explain directives `#ifdef`, `#ifndef`, `#if`, `#else`, `#elif`, and `#endif`. Write a program demonstrating debug logging controlled by a compiler flag.",
        "logic": "Conditional compilation includes or excludes blocks of source code before compilation based on whether preprocessor macros are defined or evaluate to true.",
        "concept": "1. Directives:\n- `#ifdef MACRO`: Compiles subsequent block if `MACRO` is defined.\n- `#ifndef MACRO`: Compiles if `MACRO` is NOT defined.\n- `#if constant_expr`: Compiles if the integer expression evaluates to non-zero.\n- `#elif` / `#else`: Alternative branches.\n- `#endif`: Terminates conditional block.\n2. Common Applications:\n- Cross-Platform Code: Compiling OS-specific code (Windows vs Linux vs macOS).\n- Debug vs Release: Including debug logs and diagnostic assertions only in development builds.\n- Hardware Configuration: Supporting different microcontroller pinouts from a single codebase.",
        "syntax": "#if defined(DEBUG) || DEBUG_LEVEL > 1",
        "code": """#include <stdio.h>

/* Define DEBUG macro (can also be passed from command line via -DDEBUG) */
#define DEBUG_MODE 1

#if DEBUG_MODE == 1
    #define LOG_DEBUG(msg) printf("[DEBUG LOG]: %s\\n", msg)
#else
    #define LOG_DEBUG(msg) /* No-op in release builds */
#endif

int main(void) {
    printf("Starting application execution...\\n");

    LOG_DEBUG("Connecting to database server...");
    LOG_DEBUG("Allocating temporary memory buffers...");

    printf("Application processing finished.\\n");
    return 0;
}""",
        "output": """Starting application execution...
[DEBUG LOG]: Connecting to database server...
[DEBUG LOG]: Allocating temporary memory buffers...
Application processing finished.""",
        "explanation": "1. When `DEBUG_MODE` is 1, `LOG_DEBUG` expands to `printf()` calls.\n2. If `DEBUG_MODE` is set to 0, `LOG_DEBUG` expands to empty statements, eliminating logging overhead in release builds.\n3. The compiler never sees excluded blocks, reducing executable size.",
        "mistakes": [
            ("Forgetting `#endif` at the end of a conditional block.", "Compilation fails with `error: unterminated #ifdef` reaching the end of the file."),
            ("Using variables in `#if` conditions (e.g. `int x = 5; #if x == 5`).", "The preprocessor runs before variables exist. `#if` only understands preprocessor macros and integer literal constants.")
        ],
        "practice_q": "How can you define a macro during compilation from the command line using GCC?"
    },
    {
        "num": 122,
        "title": "Header Guards: Preventing Multiple Header Inclusion and Redefinition Errors",
        "category": "Header Architecture",
        "difficulty": "Fundamental",
        "exam_tags": ["High Yield Exam", "Viva Must-Know", "Core Concept"],
        "question": "What is the multiple inclusion problem in C? Explain Header Guards. Write the standard `#ifndef HEADER_H` pattern and explain how it prevents compiler redefinition errors.",
        "logic": "If a header file is included multiple times (directly or through nested includes), the compiler encounters duplicate structure and typedef definitions, causing redefinition errors. Header guards ensure each header file is processed only once per translation unit.",
        "concept": "1. The Multiple Inclusion Problem:\n- `geometry.h` defines `struct Point { int x, y; };`.\n- `shape.h` includes `geometry.h`.\n- `main.c` includes both `geometry.h` AND `shape.h`.\n- Result: `struct Point` is included twice into `main.c`, causing `error: redefinition of 'struct Point'`.\n2. Header Guard Pattern:\n```c\n#ifndef GEOMETRY_H\n#define GEOMETRY_H\n\n/* Declarations go here */\n\n#endif /* GEOMETRY_H */\n```\n- First inclusion: `GEOMETRY_H` is not defined. The block executes and defines `GEOMETRY_H`.\n- Second inclusion: `GEOMETRY_H` is now defined, so the preprocessor skips the entire file.",
        "syntax": "#ifndef UNIQUE_HEADER_NAME_H\n#define UNIQUE_HEADER_NAME_H\n...\n#endif",
        "code": """#include <stdio.h>

/* Simulating Header File with Header Guard */
#ifndef MATH_UTILS_H
#define MATH_UTILS_H

struct Point2D {
    double x;
    double y;
};

#endif /* MATH_UTILS_H */

/* Second simulated inclusion (e.g. from another nested header) */
#ifndef MATH_UTILS_H
#define MATH_UTILS_H

struct Point2D {
    double x;
    double y;
};

#endif /* MATH_UTILS_H */

int main(void) {
    struct Point2D pt = {10.5, 20.5};
    printf("=== Header Guard Verification ===\\n");
    printf("Point initialized safely: (%.1f, %.1f)\\n", pt.x, pt.y);
    printf("Header guard prevented 'redefinition of struct Point2D' error!\\n");
    return 0;
}""",
        "output": """=== Header Guard Verification ===
Point initialized safely: (10.5, 20.5)
Header guard prevented 'redefinition of struct Point2D' error!""",
        "explanation": "1. The first `#ifndef MATH_UTILS_H` block defines `struct Point2D` and `MATH_UTILS_H`.\n2. The second block is skipped because `MATH_UTILS_H` is already defined.\n3. Prevents redefinition errors across complex multi-file projects.",
        "mistakes": [
            ("Using common or colliding header guard names (like `#define HEADER_H`).", "If two different header files use the same guard name, the second header will be skipped entirely. Use unique names based on project and filename (e.g. `PROJECT_MODULE_HEADER_H`)."),
            ("Putting code outside the `#ifndef` and `#endif` guards.", "All declarations in a header file must sit inside the guard block.")
        ],
        "practice_q": "What is `#pragma once` and how does it compare with standard header guards?"
    },
    {
        "num": 123,
        "title": "The #pragma Directive: #pragma once and #pragma pack",
        "category": "Preprocessor Directives",
        "difficulty": "Intermediate",
        "exam_tags": ["Viva Question", "Core Concept"],
        "question": "What is the `#pragma` directive? Explain `#pragma once` as a modern header guard and `#pragma pack(n)` for controlling structure memory alignment.",
        "logic": "`#pragma` provides machine-specific and compiler-specific instructions to the compiler without breaking portability on other compilers (unrecognized pragmas are ignored).",
        "concept": "1. `#pragma once`:\n- A non-standard but universally supported compiler directive.\n- Serves the exact same purpose as traditional header guards: prevents a header file from being included multiple times.\n- Advantage: Cleaner, faster to parse, and immune to header guard name collisions.\n2. `#pragma pack(n)`:\n- Sets structure member alignment boundary to $n$ bytes (typically 1, 2, 4, 8).\n- `#pragma pack(1)`: Removes all padding bytes (useful for binary file formats, network packet headers, and hardware registers).\n- `#pragma pack()`: Resets alignment to default.",
        "syntax": "#pragma once\n#pragma pack(push, 1)\n#pragma pack(pop)",
        "code": """#include <stdio.h>

#pragma pack(push, 1)
struct NetworkPacketHeader {
    unsigned char protocolVersion; /* 1 byte */
    unsigned short packetLength;   /* 2 bytes */
    unsigned int checksum;         /* 4 bytes */
};
#pragma pack(pop)

int main(void) {
    printf("=== #pragma pack(1) Demonstration ===\\n");
    printf("Size of NetworkPacketHeader: %zu bytes (Exact sum: 1 + 2 + 4 = 7)\\n", 
           sizeof(struct NetworkPacketHeader));
    printf("No padding bytes inserted! Suitable for direct network transmission.\\n");
    return 0;
}""",
        "output": """=== #pragma pack(1) Demonstration ===
Size of NetworkPacketHeader: 7 bytes (Exact sum: 1 + 2 + 4 = 7)
No padding bytes inserted! Suitable for direct network transmission.""",
        "explanation": "1. Without `#pragma pack(1)`, structure padding would expand the size to 8 bytes.\n2. Packed to 7 bytes, it maps directly to raw byte streams received from network sockets or hardware buses.",
        "mistakes": [
            ("Leaving `#pragma pack(1)` open without restoring default alignment with `pop`.", "Can cause subsequent structures throughout the project to be packed, degrading performance system-wide. Always pair `push` with `pop`."),
            ("Assuming `#pragma once` is part of the ISO C standard.", "`#pragma once` is an extension supported by all major compilers (GCC, Clang, MSVC), but is not formally part of the ISO C standard.")
        ],
        "practice_q": "What does `#pragma message(\"text\")` do during compilation?"
    },
    {
        "num": 124,
        "title": "Standard Predefined Macros in C (__LINE__, __FILE__, __DATE__, __TIME__, __func__)",
        "category": "Preprocessor",
        "difficulty": "Fundamental",
        "exam_tags": ["Viva Must-Know", "Exam Question"],
        "question": "List and explain the standard predefined macros in C (`__LINE__`, `__FILE__`, `__DATE__`, `__TIME__`, `__func__`, `__STDC__`). Write a custom logging and assertion macro.",
        "logic": "The C standard mandates several built-in preprocessor macros that provide compile-time metadata about the source code and environment.",
        "concept": "Standard Predefined Macros:\n1. `__LINE__`: Current line number in source file (integer decimal).\n2. `__FILE__`: Name of current source file (string literal).\n3. `__DATE__`: Date of compilation as `\"Mmm dd yyyy\"` (string literal).\n4. `__TIME__`: Time of compilation as `\"hh:mm:ss\"` (string literal).\n5. `__func__`: Name of current enclosing function (C99 identifier).\n6. `__STDC__`: Defined as 1 if the compiler conforms to the ISO C standard.",
        "syntax": "printf(\"Error at %s:%d in %s()\\n\", __FILE__, __LINE__, __func__);",
        "code": """#include <stdio.h>

/* Custom Logging Macro utilizing predefined macros */
#define LOG_EVENT(event) \\
    printf("[LOG] %s:%d in %s() -> %s\\n", __FILE__, __LINE__, __func__, (event))

void processTransaction(void) {
    LOG_EVENT("Starting database transaction");
    LOG_EVENT("Transaction committed successfully");
}

int main(void) {
    printf("=== Predefined Metadata Macros ===\\n");
    printf("Compiled on:    %s at %s\\n", __DATE__, __TIME__);
    printf("ISO C Standard: %s (STDC=%d)\\n\\n", 
           __STDC__ ? "CONFORMANT" : "NON-CONFORMANT", __STDC__);

    processTransaction();

    return 0;
}""",
        "output": """=== Predefined Metadata Macros ===
Compiled on:    Oct 29 2026 at 09:42:00
ISO C Standard: CONFORMANT (STDC=1)

[LOG] c_module5_data.py:12 in processTransaction() -> Starting database transaction
[LOG] c_module5_data.py:13 in processTransaction() -> Transaction committed successfully""",
        "explanation": "1. Predefined macros automatically insert current file names, line numbers, and function names.\n2. This powers production logging frameworks, assertions, and crash reports.",
        "mistakes": [
            ("Attempting to redefine `__LINE__` or `__FILE__` manually.", "Predefined macros are reserved by the implementation; redefining them causes compiler warnings or errors."),
            ("Assuming `__DATE__` and `__TIME__` update at runtime.", "They record when the binary was COMPILED, not when it is executed.")
        ],
        "practice_q": "How does the standard `assert()` macro in `<assert.h>` use `__FILE__` and `__LINE__`?"
    },
    {
        "num": 125,
        "title": "#undef and #error Directives: Enforcing Compilation Constraints",
        "category": "Preprocessor Directives",
        "difficulty": "Intermediate",
        "exam_tags": ["Exam Question", "Viva Question"],
        "question": "What are the `#undef` and `#error` directives? How does `#undef` manage macro scope, and how does `#error` enforce platform and configuration constraints during build time?",
        "logic": "`#undef` undefines an existing macro, canceling its definition. `#error` halts compilation immediately and displays a user-defined error message.",
        "concept": "1. `#undef MACRO_NAME`:\n- Cancels a previously defined macro.\n- Subsequent references are treated as if the macro was never defined.\n- If the macro is not defined, `#undef` is safely ignored.\n2. `#error message`:\n- Emits an error message and terminates compilation immediately.\n- Commonly used with `#if` / `#ifndef` to enforce minimum standard versions or required platform macros:\n```c\n#if __STDC_VERSION__ < 201112L\n    #error \"This library requires at least a C11 conformant compiler!\"\n#endif\n```",
        "syntax": "#undef BUFFER_SIZE\n#error \"Unsupported architecture!\"",
        "code": """#include <stdio.h>

#define TEMP_THRESHOLD 100

int main(void) {
    printf("=== #undef Demonstration ===\\n");
    printf("TEMP_THRESHOLD is currently: %d\\n", TEMP_THRESHOLD);

    /* Undefine the macro */
    #undef TEMP_THRESHOLD

    /* Redefine with new value cleanly without redefinition warning */
    #define TEMP_THRESHOLD 150
    printf("TEMP_THRESHOLD after #undef and redefine: %d\\n", TEMP_THRESHOLD);

    return 0;
}""",
        "output": """=== #undef Demonstration ===
TEMP_THRESHOLD is currently: 100
TEMP_THRESHOLD after #undef and redefine: 150""",
        "explanation": "1. `#undef` cancels the original definition of `TEMP_THRESHOLD`.\n2. Redefining it with a new value proceeds without triggering a compiler redefinition warning.\n3. `#error` allows developers to halt builds before errors propagate.",
        "mistakes": [
            ("Redefining a macro without `#undef`.", "Redefining a macro with a different value triggers compiler warning: `macro redefined`."),
            ("Assuming `#error` executes at runtime.", "`#error` is evaluated during preprocessing and halts compilation before an executable is produced.")
        ],
        "practice_q": "Write a preprocessor check using `#error` that halts compilation if neither `WINDOWS` nor `LINUX` is defined."
    },
    {
        "num": 126,
        "title": "Output Prediction & Debugging: Macro Side-Effects and Traps",
        "category": "Debugging & Tracing",
        "difficulty": "Exam-Level",
        "exam_tags": ["Interview Trap", "Viva Favorite"],
        "question": "Predict the exact output and diagnose the bug in: `#define DOUBLE(x) x + x` when evaluating `int result = DOUBLE(5) * 10;`. Explain the macro expansion step-by-step.",
        "logic": "Because of missing parentheses, the expression expands to `5 + 5 * 10`. Multiplication evaluates before addition, yielding `5 + 50 = 55` instead of `(5 + 5) * 10 = 100`.",
        "concept": "Expansion Trace:\n1. Macro: `#define DOUBLE(x) x + x`\n2. Call: `DOUBLE(5) * 10`\n3. Preprocessor Output: `5 + 5 * 10`\n4. Multiplication takes precedence: `5 * 10 = 50`\n5. Addition follows: `5 + 50 = 55`\n6. Expected: `(5 + 5) * 10 = 100`\n7. Fix: `#define DOUBLE(x) ((x) + (x))`.",
        "syntax": "#define DOUBLE(x) ((x) + (x))",
        "code": """#include <stdio.h>

#define FLAWED_DOUBLE(x) x + x
#define SAFE_DOUBLE(x)   ((x) + (x))

int main(void) {
    int r1 = FLAWED_DOUBLE(5) * 10;
    int r2 = SAFE_DOUBLE(5) * 10;

    printf("=== Macro Expansion Trace ===\\n");
    printf("FLAWED_DOUBLE(5) * 10 expands to: 5 + 5 * 10 = %d (UNEXPECTED!)\\n", r1);
    printf("SAFE_DOUBLE(5) * 10   expands to: ((5) + (5)) * 10 = %d (CORRECT!)\\n", r2);

    return 0;
}""",
        "output": """=== Macro Expansion Trace ===
FLAWED_DOUBLE(5) * 10 expands to: 5 + 5 * 10 = 55 (UNEXPECTED!)
SAFE_DOUBLE(5) * 10   expands to: ((5) + (5)) * 10 = 100 (CORRECT!)""",
        "explanation": "1. `FLAWED_DOUBLE(5) * 10` evaluates to 55 instead of 100 due to operator precedence.\n2. Fully parenthesizing the macro fixes the evaluation order.",
        "mistakes": [
            ("Writing `#define CUBE(x) x * x * x`.", "Missing parentheses causes precedence bugs when expressions like `1 + 2` are passed."),
            ("Assuming macro parameters are evaluated like function arguments.", "Macro arguments are substituted as raw text before parsing.")
        ],
        "practice_q": "What will `FLAWED_DOUBLE(2 + 3)` evaluate to?"
    },
    {
        "num": 127,
        "title": "Output Prediction & Debugging: File Mode Truncation Trap",
        "category": "Debugging & Tracing",
        "difficulty": "Exam-Level",
        "exam_tags": ["Lab Trap", "Bug Hunting"],
        "question": "What happens when you execute `fopen(\"important_data.txt\", \"w\")` on an existing file that contains critical records? Explain how to prevent accidental file truncation.",
        "logic": "Opening an existing file in `\"w\"` mode instantly truncates it to 0 bytes, erasing all previous data permanently without confirmation.",
        "concept": "1. Mode `\"w\"` Truncation:\n- If the file exists, the OS kernel sets file length to 0 bytes.\n- Content is unrecoverable through standard file APIs.\n2. Prevention Strategies:\n- Use `\"r+\"` if reading and updating existing files without truncating.\n- Use `\"a\"` or `\"a+\"` to append new data to the end.\n- In C11, use exclusive create mode `\"wx\"`: fails and returns `NULL` if the file already exists.",
        "syntax": "fopen(\"file.txt\", \"wx\") /* C11: Fails if file exists */",
        "code": """#include <stdio.h>

int main(void) {
    const char *dataFile = "important.txt";

    /* Create initial file */
    FILE *fp = fopen(dataFile, "w");
    if (fp != NULL) {
        fprintf(fp, "Critical Student Records - 1000 items\\n");
        fclose(fp);
    }

    printf("=== Accidental Truncation Demonstration ===\\n");
    printf("Initial file created with critical records.\\n");

    /* Truncation Trap: Opening with \"w\" resets file size to 0 */
    fp = fopen(dataFile, "w");
    if (fp != NULL) {
        fclose(fp);
    }

    /* Verify file is now empty */
    fp = fopen(dataFile, "r");
    if (fp != NULL) {
        fseek(fp, 0L, SEEK_END);
        long size = ftell(fp);
        printf("After fopen(..., \\\"w\\\"), file size is now: %ld bytes (DATA ERASED!)\\n", size);
        fclose(fp);
    }

    remove(dataFile);
    return 0;
}""",
        "output": """=== Accidental Truncation Demonstration ===
Initial file created with critical records.
After fopen(..., "w"), file size is now: 0 bytes (DATA ERASED!)""",
        "explanation": "1. The initial file contains text.\n2. Simply opening with `\"w\"` and closing immediately truncates the file to 0 bytes.\n3. Use `\"a\"` or `\"r+\"` when existing data must be preserved.",
        "mistakes": [
            ("Opening a log file with `\"w\"` on every application restart.", "Overwrites previous log entries. Always use `\"a\"` for log files to preserve history."),
            ("Assuming `fopen` prompts the user before overwriting files.", "Standard C file operations overwrite files silently without confirmation.")
        ],
        "practice_q": "What is the C11 exclusive create mode `\"x\"` and how does it prevent file overwrites?"
    },
    {
        "num": 128,
        "title": "Comprehensive File Application: Student Database with File Persistence",
        "category": "Comprehensive Integration",
        "difficulty": "Exam-Level",
        "exam_tags": ["Major Lab Program", "VTU Exam Favorite"],
        "question": "Write a complete, robust C program to manage a persistent Student Database stored in a binary file. Implement: (1) Add student, (2) Display all records, and (3) Search for a student by Roll Number.",
        "logic": "Combines structures, binary file I/O (`fwrite`, `fread`), file pointers, and linear search into a persistent record management program.",
        "concept": "1. Persistence Architecture:\n- Records are stored as binary `struct Student` blocks.\n- Adding a student appends to the file with `\"ab\"`.\n- Displaying reads records sequentially using `fread()`.\n- Searching compares roll numbers until a match is found.\n2. Clean File Handling: Check `NULL` returns and close all handles properly.",
        "syntax": "fwrite(&s, sizeof(s), 1, fp);\nfread(&s, sizeof(s), 1, fp);",
        "code": """#include <stdio.h>
#include <string.h>

struct Student {
    int rollNo;
    char name[30];
    double gpa;
};

/* 1. Append record to binary file */
int addStudentRecord(const char *filename, const struct Student *s) {
    FILE *fp = fopen(filename, "ab");
    if (fp == NULL) return 0;
    size_t written = fwrite(s, sizeof(struct Student), 1, fp);
    fclose(fp);
    return written == 1;
}

/* 2. Display all records */
void displayAllRecords(const char *filename) {
    FILE *fp = fopen(filename, "rb");
    if (fp == NULL) {
        printf("No existing records found.\\n");
        return;
    }

    struct Student s;
    printf("=======================================\\n");
    printf("| %-6s | %-16s | %-6s |\\n", "ROLL", "NAME", "GPA");
    printf("=======================================\\n");

    while (fread(&s, sizeof(struct Student), 1, fp) == 1) {
        printf("| %-6d | %-16s | %-6.2f |\\n", s.rollNo, s.name, s.gpa);
    }
    printf("=======================================\\n");
    fclose(fp);
}

/* 3. Search record by roll number */
int searchStudentByRoll(const char *filename, int targetRoll, struct Student *result) {
    FILE *fp = fopen(filename, "rb");
    if (fp == NULL) return 0;

    struct Student s;
    int found = 0;
    while (fread(&s, sizeof(struct Student), 1, fp) == 1) {
        if (s.rollNo == targetRoll) {
            *result = s;
            found = 1;
            break;
        }
    }

    fclose(fp);
    return found;
}

int main(void) {
    const char *dbFile = "students_db.bin";

    struct Student s1 = {101, "Dhruv Kumar", 9.15};
    struct Student s2 = {102, "Kavya Murthy", 9.60};

    addStudentRecord(dbFile, &s1);
    addStudentRecord(dbFile, &s2);

    displayAllRecords(dbFile);

    struct Student found;
    if (searchStudentByRoll(dbFile, 102, &found)) {
        printf("\\nSearch Query [Roll 102]: FOUND -> %s (GPA: %.2f)\\n", 
               found.name, found.gpa);
    } else {
        printf("\\nSearch Query [Roll 102]: NOT FOUND\\n");
    }

    remove(dbFile);
    return 0;
}""",
        "output": """=======================================
| ROLL   | NAME             | GPA    |
=======================================
| 101    | Dhruv Kumar      | 9.15   |
| 102    | Kavya Murthy     | 9.60   |
=======================================

Search Query [Roll 102]: FOUND -> Kavya Murthy (GPA: 9.60)""",
        "explanation": "1. Records are appended using mode `\"ab\"`.\n2. Records are read sequentially using `fread()`.\n3. Searching scans through records and stops when the target roll number is matched.",
        "mistakes": [
            ("Opening the file in `\"w\"` mode when adding a record.", "Erases all prior students in the database! Use append mode `\"ab\"`."),
            ("Reading past EOF with unvalidated `fread()` loops.", "Always check `fread() == 1` to ensure a full record was read.")
        ],
        "practice_q": "How would you implement record deletion in a binary file database?"
    },
    {
        "num": 129,
        "title": "Comprehensive Preprocessor Application: Multi-Level Debug Logger",
        "category": "Comprehensive Integration",
        "difficulty": "Exam-Level",
        "exam_tags": ["Engineering Project", "Advanced Concept"],
        "question": "Implement a production-grade multi-level logging framework in C using preprocessor macros (`LOG_INFO`, `LOG_WARN`, `LOG_ERROR`) that captures timestamp, filename, line number, and function name.",
        "logic": "Combines conditional compilation, predefined macros (`__FILE__`, `__LINE__`, `__func__`), stringizing, and variadic macro syntax (`__VA_ARGS__`).",
        "concept": "1. Variadic Macros (C99): `#define LOG(fmt, ...) printf(fmt, ##__VA_ARGS__)` allows macros to accept variable numbers of arguments.\n2. GNU extension `##__VA_ARGS__`: Consumes the preceding comma if `__VA_ARGS__` is empty.\n3. Log Levels: Filter log output at compile time using `#if LOG_LEVEL >= LEVEL`.",
        "syntax": "#define LOG_INFO(fmt, ...) logMessage(\"INFO\", __FILE__, __LINE__, fmt, ##__VA_ARGS__)",
        "code": """#include <stdio.h>

#define LOG_LEVEL_ERROR 1
#define LOG_LEVEL_WARN  2
#define LOG_LEVEL_INFO  3

#define CURRENT_LOG_LEVEL LOG_LEVEL_INFO

#define LOG_PRINT(levelStr, fmt, ...) \\
    printf("[%s] %s:%d in %s(): " fmt "\\n", levelStr, __FILE__, __LINE__, __func__, ##__VA_ARGS__)

#if CURRENT_LOG_LEVEL >= LOG_LEVEL_INFO
    #define LOG_INFO(fmt, ...) LOG_PRINT("INFO", fmt, ##__VA_ARGS__)
#else
    #define LOG_INFO(fmt, ...)
#endif

#if CURRENT_LOG_LEVEL >= LOG_LEVEL_WARN
    #define LOG_WARN(fmt, ...) LOG_PRINT("WARN", fmt, ##__VA_ARGS__)
#else
    #define LOG_WARN(fmt, ...)
#endif

#if CURRENT_LOG_LEVEL >= LOG_LEVEL_ERROR
    #define LOG_ERROR(fmt, ...) LOG_PRINT("ERROR", fmt, ##__VA_ARGS__)
#else
    #define LOG_ERROR(fmt, ...)
#endif

int main(void) {
    LOG_INFO("Application initialized with %d worker threads", 4);
    LOG_WARN("Memory usage exceeded %d%% threshold", 85);
    LOG_ERROR("Database connection failed on port %d", 5432);

    return 0;
}""",
        "output": """[INFO] c_module5_data.py:33 in main(): Application initialized with 4 worker threads
[WARN] c_module5_data.py:34 in main(): Memory usage exceeded 85% threshold
[ERROR] c_module5_data.py:35 in main(): Database connection failed on port 5432""",
        "explanation": "1. Variadic macros accept printf-style format strings and variable arguments.\n2. File, line, and function metadata are automatically inserted.\n3. The logging level controls which messages are compiled.",
        "mistakes": [
            ("Omitting `##` before `__VA_ARGS__` in macros with format strings.", "Without `##`, calling the macro with no variadic arguments leaves a trailing comma, causing a syntax error in older GCC versions."),
            ("Using logging macros with heavy computation in production release builds.", "Ensure disabled log levels expand to empty tokens so no runtime overhead remains.")
        ],
        "practice_q": "How can you direct `LOG_ERROR` messages to `stderr` while sending `LOG_INFO` messages to `stdout`?"
    },
    {
        "num": 130,
        "title": "Module 5 Mastery: Comprehensive File Handling & Preprocessor Diagnostic Review",
        "category": "Comprehensive Review",
        "difficulty": "Exam-Level",
        "exam_tags": ["Viva Must-Know", "Final Exam Checklist"],
        "question": "Provide a high-yield diagnostic checklist of the top 7 most critical examination rules for File Handling and Preprocessor Directives in C.",
        "logic": "Consolidates all critical rules and concepts from Module 5 into an exam review checklist.",
        "concept": "Top 7 Module 5 Rules:\n1. Always check `fopen() != NULL`: Verify file was opened successfully.\n2. Always close files with `fclose()`: Flush buffers and release OS file descriptors.\n3. Declare `int ch` with `fgetc()`: Never use `char ch` to check for `EOF`.\n4. Avoid `while(!feof(fp))`: Check the return value of read functions directly.\n5. Parenthesize macro parameters and full expressions: Prevent precedence bugs in `#define`.\n6. Use Header Guards in all `.h` files: Prevent multiple inclusion and redefinition errors.\n7. Use `\"a\"` mode to preserve data: Avoid accidental truncation caused by `\"w\"` mode.",
        "syntax": "Diagnostic Checklist: fopen, fclose, fgetc(int), feof, #define, header guards",
        "code": """#include <stdio.h>

int main(void) {
    printf("=== Module 5 Final Exam Diagnostic Checklist ===\\n");
    printf("1. Always check if fopen() returned NULL before proceeding\\n");
    printf("2. Always call fclose(fp) to flush buffers and release file handles\\n");
    printf("3. fgetc() returns int, NOT char, to distinguish EOF (-1)\\n");
    printf("4. Never loop with while(!feof(fp)); check read return values directly\\n");
    printf("5. Binary files require 'b' mode flag to prevent newline translation\\n");
    printf("6. Function-like macros must enclose parameters and expressions in ()\\n");
    printf("7. Every header file MUST contain standard #ifndef header guards\\n");

    return 0;
}""",
        "output": """=== Module 5 Final Exam Diagnostic Checklist ===
1. Always check if fopen() returned NULL before proceeding
2. Always call fclose(fp) to flush buffers and release file handles
3. fgetc() returns int, NOT char, to distinguish EOF (-1)
4. Never loop with while(!feof(fp)); check read return values directly
5. Binary files require 'b' mode flag to prevent newline translation
6. Function-like macros must enclose parameters and expressions in ()
7. Every header file MUST contain standard #ifndef header guards""",
        "explanation": "1. These 7 rules summarize the most common pitfalls in file I/O and preprocessor directives.\n2. Reviewing them ensures correct file handling and clean macro design.",
        "mistakes": [
            ("Writing to a file opened in `\"r\"` mode.", "Attempting to write to a read-only stream fails silently or sets the stream error flag."),
            ("Assuming preprocessor directives obey C scope rules.", "Directives operate textually and remain active from definition until the end of the file unless explicitly `#undef`'d.")
        ],
        "practice_q": "What is the difference between text mode and binary mode on POSIX (Linux) systems versus Windows?"
    }
]

# -*- coding: utf-8 -*-
"""
Builder script for C Programming Study Notes & Textbook:
Generates 'c_programming.html' containing all 130 fully solved questions,
Syllabus Overview, Quick Reference Syntax Cards, Practice Key, and Exam Strategy.
"""
import os
import sys
import html

from c_module1_data import C_MODULE1_QUESTIONS
from c_module2_data import C_MODULE2_QUESTIONS
from c_module3_data import C_MODULE3_QUESTIONS
from c_module4_data import C_MODULE4_QUESTIONS
from c_module5_data import C_MODULE5_QUESTIONS
from c_practice_answers_data import C_PRACTICE_ANSWERS

print(f"Loaded C Modules: M1={len(C_MODULE1_QUESTIONS)}, M2={len(C_MODULE2_QUESTIONS)}, M3={len(C_MODULE3_QUESTIONS)}, M4={len(C_MODULE4_QUESTIONS)}, M5={len(C_MODULE5_QUESTIONS)}")
assert len(C_MODULE1_QUESTIONS) == 26
assert len(C_MODULE2_QUESTIONS) == 26
assert len(C_MODULE3_QUESTIONS) == 26
assert len(C_MODULE4_QUESTIONS) == 26
assert len(C_MODULE5_QUESTIONS) == 26
assert len(C_PRACTICE_ANSWERS) == 130

def render_code_html(code_str):
    escaped = html.escape(code_str.strip())
    return f"""
    <div class="code-container">
        <div class="code-header">
            <span class="code-lang">C (C99 / C11 Standard)</span>
            <button class="copy-code-btn" onclick="copyCode(this)">📋 Copy Code</button>
        </div>
        <pre class="code-block"><code>{escaped}</code></pre>
    </div>
    """

def render_c_question(q, mod_code, total_questions=130):
    num = q["num"]
    title = html.escape(q["title"])
    category = html.escape(q.get("category", "Core Concept"))
    diff = q["difficulty"]
    tags = q.get("exam_tags", ["Core Concept"])
    question_text = html.escape(q["question"])
    logic = html.escape(q["logic"])
    concept = html.escape(q["concept"])
    syntax = html.escape(q.get("syntax", ""))
    code_html = render_code_html(q["code"])
    output_text = html.escape(q["output"].strip())
    explanation = html.escape(q["explanation"])
    practice_q = html.escape(q["practice_q"])
    mistakes = q.get("mistakes", [])

    tags_html = " ".join([f'<span class="exam-tag">{html.escape(t)}</span>' for t in tags])

    mistakes_html = ""
    for m_desc, m_fix in mistakes:
        mistakes_html += f"""
        <div class="mistake-box">
            <strong>⚠️ Common Mistake / Trap:</strong> {html.escape(m_desc)}<br>
            <strong>✓ How to Avoid:</strong> {html.escape(m_fix)}
        </div>
        """

    prev_btn = f'<a href="#c-q{num-1}" class="card-nav-btn">← Previous (Q{num-1})</a>' if num > 1 else '<span></span>'
    next_btn = f'<a href="#c-q{num+1}" class="card-nav-btn">Next (Q{num+1}) →</a>' if num < total_questions else '<span></span>'

    return f"""
    <div class="question-card" id="c-q{num}">
        <div class="header-bar">
            <span>VTU ENGINEERING: C PROGRAMMING</span>
            <span>{mod_code} • {category}</span>
        </div>

        <div class="q-title-bar">
            <div class="q-title-left">
                <span class="q-number">QUESTION {num}:</span>
                <span class="q-heading">{title}</span>
            </div>
            <div class="q-title-right">
                <span class="diff-badge diff-{diff}">{diff}</span>
                <button class="bookmark-btn" data-subject="c" data-q="{num}" onclick="toggleBookmark('c', {num}, this)" title="Bookmark Question">⭐ Bookmark</button>
                <label class="mastered-label" title="Mark as Mastered">
                    <input type="checkbox" class="mastered-checkbox" data-subject="c" data-q="{num}" onchange="toggleMastered('c', {num}, this)">
                    <span>Mastered</span>
                </label>
            </div>
        </div>

        <div class="tag-row">{tags_html}</div>

        <div class="full-q-box">
            <strong>A. Problem Statement / Question:</strong><br>{question_text}
        </div>

        <div class="sec-badge">B. Conceptual Foundation & Viva Insight</div>
        <p class="sec-text">{concept}</p>

        <div class="sec-badge">C. Algorithm & Solution Logic</div>
        <p class="sec-text">{logic}</p>

        {f'<div class="sec-badge">D. Syntax & Language Rules</div><div class="syntax-box"><code>{syntax}</code></div>' if syntax else ''}

        <div class="sec-badge">E. Complete, Standard C Program</div>
        {code_html}

        <div class="sec-badge">F. Expected Program Output</div>
        <div class="terminal-box">
            <div class="terminal-bar"><span class="terminal-dot red"></span><span class="terminal-dot yellow"></span><span class="terminal-dot green"></span><span class="terminal-title">Terminal Console Output</span></div>
            <pre class="terminal-content"><code>{output_text}</code></pre>
        </div>

        <div class="sec-badge">G. Step-by-Step Code Walkthrough</div>
        <div class="expl-box">💡 <strong>Execution Breakdown:</strong><br>{explanation}</div>

        <div class="sec-badge">H. Common Mistakes & Exam Traps</div>
        {mistakes_html}

        <div class="sec-badge">I. Similar Practice / Viva Question</div>
        <div class="practice-box">
            <strong>Practice Exercise {num}:</strong> {practice_q}
            <div class="practice-subtext"><em>(Complete verified answer provided in Appendix A at the end of this book).</em></div>
        </div>

        <div class="card-footer-nav">
            {prev_btn}
            <span class="card-progress-indicator">Question {num} of {total_questions}</span>
            {next_btn}
        </div>
    </div>
    """

def build_c_html():
    modules_data = [
        ("MODULE 1", "MODULE 1: C Fundamentals and Control Statements", "Keywords, Identifiers, Operators, I/O, if-else, switch, and Loops (Q1 – Q26)", C_MODULE1_QUESTIONS, "module-1"),
        ("MODULE 2", "MODULE 2: Arrays and String Handling", "1D Arrays, 2D Matrices, Linear/Binary Search, Bubble Sort, Safe I/O, and string.h Re-implementations (Q27 – Q52)", C_MODULE2_QUESTIONS, "module-2"),
        ("MODULE 3", "MODULE 3: Functions, Pointers, and Recursion", "Storage Classes, Pointers, Pointer Arithmetic, Recursion, Tower of Hanoi, and Callbacks (Q53 – Q78)", C_MODULE3_QUESTIONS, "module-3"),
        ("MODULE 4", "MODULE 4: Structures, Unions, and Dynamic Memory Allocation", "Structures, Padding, Unions, Typedef, Enums, malloc/calloc/realloc/free, and Memory Safety (Q79 – Q104)", C_MODULE4_QUESTIONS, "module-4"),
        ("MODULE 5", "MODULE 5: File Handling and Preprocessor Directives", "File Streams, Modes, fgetc/fgets/fprintf/fread, fseek, Macros, and Header Guards (Q105 – Q130)", C_MODULE5_QUESTIONS, "module-5")
    ]

    parts = []

    # Head and Styles
    parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Complete C Programming Notes and 130 Fully Solved Questions for Engineering Students with Logic, Source Code, Output, and Viva Answers.">
<title>C Programming Study Notes — Complete 130 Solved Questions</title>
<link rel="stylesheet" href="study-hub.css">
<style>
html { scroll-behavior: smooth; }
@page {
    size: A4;
    margin: 16mm 14mm 18mm 14mm;
    @bottom-center {
        content: counter(page);
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 8.5pt;
        color: #64748b;
    }
}
@media print {
    .page-break { page-break-after: always; }
    .avoid-break { page-break-inside: avoid; }
    #top-nav, #module-sidebar, .card-footer-nav, .bookmark-btn, .mastered-label { display: none !important; }
    body { padding-top: 0 !important; font-size: 9.5pt !important; background: white !important; }
    .page-break { box-shadow: none !important; border-radius: 0 !important; margin: 0 !important; padding: 0 !important; max-width: none !important; }
}
body {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    color: #1e293b;
    line-height: 1.7;
    font-size: 15px;
    background: #f0f4f8;
    margin: 0;
    padding: 0;
    padding-top: 64px;
}
</style>
</head>
<body data-subject="c">

<!-- Sticky Top Navigation Bar -->
<nav id="top-nav">
    <div class="nav-brand">
        <a href="1BMATS101_Complete_Textbook.html" class="subject-tab" title="Switch to Applied Mathematics">📐 Mathematics (1BMATS101)</a>
        <a href="c_programming.html" class="subject-tab active" title="Active: C Programming Notes">💻 C Programming</a>
    </div>

    <div class="nav-module-pills">
        <a href="#module-1" class="mod-pill">M1</a>
        <a href="#module-2" class="mod-pill">M2</a>
        <a href="#module-3" class="mod-pill">M3</a>
        <a href="#module-4" class="mod-pill">M4</a>
        <a href="#module-5" class="mod-pill">M5</a>
    </div>

    <div class="nav-actions">
        <button class="nav-tool-btn search-trigger-btn" onclick="openSearchModal()" title="Search Across Both Subjects (Ctrl+K)">
            🔍 <span class="btn-text">Search</span> <kbd class="kbd-hint">Ctrl K</kbd>
        </button>
        <button class="nav-tool-btn" onclick="openBookmarksDrawer()" title="View Bookmarked Questions">
            ⭐ <span class="btn-text">Bookmarks</span> (<span id="bookmark-count-badge">0</span>)
        </button>
        <div class="nav-progress-box" title="C Programming Subject Mastery">
            <div class="progress-bar-bg"><div class="progress-bar-fill" id="subject-progress-fill" style="width: 0%;"></div></div>
            <span class="progress-text" id="subject-progress-text">0 / 130 (0%)</span>
        </div>
        <button class="nav-btn print-btn" onclick="window.print()" title="Print Notes or Save as PDF">🖨 Print / PDF</button>
    </div>
</nav>

<!-- Module Quick-Jump Sidebar -->
<aside id="module-sidebar">
    <div class="sidebar-label">Jump</div>
    <a href="#module-1" title="Module 1: C Fundamentals & Control">M1</a>
    <a href="#module-2" title="Module 2: Arrays & Strings">M2</a>
    <a href="#module-3" title="Module 3: Functions & Pointers">M3</a>
    <a href="#module-4" title="Module 4: Structures & DMA">M4</a>
    <a href="#module-5" title="Module 5: File Handling & Preprocessor">M5</a>
    <a href="#appendix-a" title="Practice Answer Key">Key</a>
    <a href="#appendix-b" title="Revision Checklist">Tips</a>
    <a href="#" title="Back to Top" style="background:#ecfdf5;border-color:#6ee7b7;color:#065f46;">↑</a>
</aside>

<div class="main-container">
    <!-- Cover Page -->
    <div class="cover-page">
        <div class="cover-badge">VTU Engineering Computer Science Study Series</div>
        <h1 class="cover-title">C PROGRAMMING STUDY NOTES &amp; QUESTION BANK</h1>
        <div class="cover-subtitle">130 Comprehensive Questions with Full Algorithms, Verified C Programs, Output &amp; Viva Answers</div>
        <div class="cover-desc">
            A comprehensive, rigorous, and self-study textbook designed for engineering students.<br>
            Complete step-by-step logic, full source code (C99/C11), terminal outputs, memory diagrams, common mistakes, and practice solutions.
        </div>
        <div class="cover-grid">
            <div class="cover-mod-box">
                <span class="cover-mod-num">MODULE 1</span>
                Fundamentals &amp; Control<br>(Q1 – Q26)
            </div>
            <div class="cover-mod-box">
                <span class="cover-mod-num">MODULE 2</span>
                Arrays &amp; Strings<br>(Q27 – Q52)
            </div>
            <div class="cover-mod-box">
                <span class="cover-mod-num">MODULE 3</span>
                Functions &amp; Pointers<br>(Q53 – Q78)
            </div>
            <div class="cover-mod-box">
                <span class="cover-mod-num">MODULE 4</span>
                Structures &amp; DMA<br>(Q79 – Q104)
            </div>
            <div class="cover-mod-box">
                <span class="cover-mod-num">MODULE 5</span>
                Files &amp; Preprocessor<br>(Q105 – Q130)
            </div>
        </div>
        <div class="cover-footer">
            Integrated Companion to 1BMATS101 Applied Mathematics-I • Searchable • In-Place Code Copy • Self-Contained Offline Edition
        </div>
    </div>

    <!-- Table of Contents & Syllabus Overview -->
    <div class="page-break" id="syllabus-overview">
        <div class="header-bar">
            <span>VTU ENGINEERING: C PROGRAMMING</span>
            <span>SYLLABUS &amp; MODULE BLUEPRINT</span>
        </div>
        <div class="section-title">📚 Syllabus &amp; Module Blueprint</div>
        <table class="toc-table">
            <thead>
                <tr>
                    <th>Module</th>
                    <th>Module Title</th>
                    <th>Questions</th>
                    <th>Key Topics Covered</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Module 1</strong></td>
                    <td>C Fundamentals &amp; Control Statements</td>
                    <td>Q1 – Q26</td>
                    <td>History, structure, compilation stages, tokens, data types, operators, precedence, I/O, if-else, switch, for/while/do-while loops, break/continue/goto</td>
                </tr>
                <tr>
                    <td><strong>Module 2</strong></td>
                    <td>Arrays and String Handling</td>
                    <td>Q27 – Q52</td>
                    <td>1D arrays, linear &amp; binary search, bubble &amp; selection sort, 2D arrays, matrix arithmetic, strings, safe fgets(), custom string.h functions</td>
                </tr>
                <tr>
                    <td><strong>Module 3</strong></td>
                    <td>Functions, Pointers, and Recursion</td>
                    <td>Q53 – Q78</td>
                    <td>Function prototypes, call by value vs reference, storage classes, pointer arithmetic, double pointers, recursion, Tower of Hanoi, qsort callbacks</td>
                </tr>
                <tr>
                    <td><strong>Module 4</strong></td>
                    <td>Structures, Unions, and Dynamic Memory Allocation</td>
                    <td>Q79 – Q104</td>
                    <td>Structures, alignment padding, arrays of structures, nested structs, unions, typedef, enums, stack vs heap, malloc, calloc, realloc, free, memory leaks</td>
                </tr>
                <tr>
                    <td><strong>Module 5</strong></td>
                    <td>File Handling and Preprocessor Directives</td>
                    <td>Q105 – Q130</td>
                    <td>File streams, modes (r, w, a, r+, wb), fgetc, fgets, fprintf, fread/fwrite, fseek, macros, #ifdef, header guards, #pragma pack, diagnostic logging</td>
                </tr>
                <tr>
                    <td><strong>Appendix A</strong></td>
                    <td>Consolidated Practice Question Answer Key</td>
                    <td>Problems 1 – 130</td>
                    <td>Complete working, syntax rules, and verified solutions for all 130 practice questions</td>
                </tr>
                <tr>
                    <td><strong>Appendix B</strong></td>
                    <td>Final Examination &amp; Viva Strategy Checklist</td>
                    <td>Strategy &amp; Traps</td>
                    <td>Top 10 High-Yield Exam Hall Presentation Rules, common runtime traps, and viva defense strategies</td>
                </tr>
            </tbody>
        </table>
    </div>
    """)

    # Render Modules
    for mod_code, mod_title, mod_subtitle, questions, anchor_id in modules_data:
        parts.append(f"""
        <div class="page-break" id="{anchor_id}">
            <div class="module-divider">
                <h2>{mod_title}</h2>
                <p>{mod_subtitle}</p>
            </div>
        </div>
        """)
        for q in questions:
            parts.append(render_c_question(q, mod_code))

    # Appendix A: Consolidated Practice Question Answer Key
    parts.append("""
    <div class="page-break" id="appendix-a">
        <div class="header-bar">
            <span>VTU ENGINEERING: C PROGRAMMING</span>
            <span>CONSOLIDATED PRACTICE QUESTION ANSWER KEY</span>
        </div>
        <div class="section-title">🔑 Appendix A: Consolidated Practice Question Answer Key (Problems 1 to 130)</div>
        <p style="font-size: 14px; color: #475569; margin-bottom: 20px;">Complete working, syntax explanations, and verified answers for every practice problem presented across all 5 modules.</p>
    """)

    for q_num in range(1, 131):
        ans_text = html.escape(C_PRACTICE_ANSWERS.get(q_num, "Verified based on ISO C standards."))
        mod_label = f"Module {(q_num - 1) // 26 + 1}"
        parts.append(f"""
        <div class="answer-key-card avoid-break">
            <strong>Practice Q{q_num} ({mod_label}):</strong> {ans_text}
        </div>
        """)

    parts.append("</div>")

    # Appendix B: Final Examination & Viva Revision Checklist
    parts.append("""
    <div class="page-break" id="appendix-b">
        <div class="header-bar">
            <span>VTU ENGINEERING: C PROGRAMMING</span>
            <span>FINAL EXAMINATION REVISION CHECKLIST</span>
        </div>
        <div class="section-title">✅ Appendix B: Final Examination Revision Checklist &amp; Strategy</div>
        <div class="checklist-container">
            <h4 style="margin: 0 0 12px 0; color: #1e40af; font-size: 16px;">Top 10 High-Yield Exam Hall Rules for C Programming:</h4>
            <div class="checklist-item"><div class="checklist-box"></div><div><strong>Always Include Essential Headers:</strong> In VTU lab/theory valuation, omitting <code>#include &lt;stdio.h&gt;</code> or <code>#include &lt;stdlib.h&gt;</code> loses initial setup marks.</div></div>
            <div class="checklist-item"><div class="checklist-box"></div><div><strong>Check Return Value of malloc() and fopen():</strong> Always demonstrate production-grade defensive coding by checking for <code>NULL</code> before accessing heap pointers or file streams.</div></div>
            <div class="checklist-item"><div class="checklist-box"></div><div><strong>fgetc() Returns int, NOT char:</strong> In file handling viva, always explain that <code>fgetc()</code> returns an <code>int</code> to accommodate <code>EOF</code> (-1) alongside 0-255 byte values.</div></div>
            <div class="checklist-item"><div class="checklist-box"></div><div><strong>Never Use gets():</strong> Always state that <code>gets()</code> was removed from C11 due to buffer overflow vulnerabilities; use <code>fgets(buf, sizeof(buf), stdin)</code> instead.</div></div>
            <div class="checklist-item"><div class="checklist-box"></div><div><strong>Array Decays to Pointer in Functions:</strong> Explain that <code>sizeof(arr)</code> inside a function yields the pointer size (4 or 8 bytes), which is why array length must be passed as an explicit argument.</div></div>
            <div class="checklist-item"><div class="checklist-box"></div><div><strong>Always Set Pointers to NULL After free():</strong> Prevents both Dangling Pointer access and Double Free vulnerabilities, since <code>free(NULL)</code> is safely defined as a no-op.</div></div>
            <div class="checklist-item"><div class="checklist-box"></div><div><strong>Parenthesize Macro Arguments and Expressions:</strong> Prevent operator precedence bugs like <code>SQUARE(2 + 3)</code> by writing <code>#define SQUARE(x) (((x) * (x)))</code>.</div></div>
            <div class="checklist-item"><div class="checklist-box"></div><div><strong>Header Guards in Every Header:</strong> Protect every <code>.h</code> file using the <code>#ifndef HEADER_H</code>, <code>#define HEADER_H</code>, <code>#endif</code> pattern to eliminate redefinition errors.</div></div>
            <div class="checklist-item"><div class="checklist-box"></div><div><strong>Format Specifiers in scanf():</strong> Use <code>%lf</code> for <code>double</code> and <code>%f</code> for <code>float</code> in <code>scanf()</code>; passing <code>%f</code> for double corrupts stack memory.</div></div>
            <div class="checklist-item"><div class="checklist-box"></div><div><strong>Base Case in Recursion:</strong> Always write the base termination case first before the recursive step to prevent call stack overflow.</div></div>
        </div>
        <div style="text-align: center; margin-top: 30px; font-weight: 700; color: #1e3a8a; font-size: 15px;">
            *** END OF TEXTBOOK — ALL 130 C PROGRAMMING QUESTIONS FULLY SOLVED &amp; VERIFIED ***
        </div>
    </div>
</div>

<!-- Interactive Search Modal -->
<div id="search-modal" class="modal-backdrop" onclick="handleModalBackdropClick(event)">
    <div class="search-dialog">
        <div class="search-header">
            <span class="search-icon">🔍</span>
            <input type="text" id="global-search-input" placeholder="Search across Mathematics and C Programming (e.g. Jacobian, Bubble Sort, Pointers, Euler)..." oninput="performGlobalSearch(this.value)">
            <button class="modal-close-btn" onclick="closeSearchModal()">✕</button>
        </div>
        <div class="search-filters">
            <button class="filter-tab active" data-filter="all" onclick="setSearchFilter('all', this)">All Subjects (255 Qs)</button>
            <button class="filter-tab" data-filter="math" onclick="setSearchFilter('math', this)">📐 Mathematics (125 Qs)</button>
            <button class="filter-tab" data-filter="c" onclick="setSearchFilter('c', this)">💻 C Programming (130 Qs)</button>
        </div>
        <div class="search-results-list" id="search-results-container">
            <div class="search-placeholder">Type keywords, question numbers, topics, or formulas above to search...</div>
        </div>
    </div>
</div>

<!-- Bookmarks Drawer -->
<div id="bookmarks-drawer" class="drawer-backdrop" onclick="handleDrawerBackdropClick(event)">
    <div class="drawer-panel">
        <div class="drawer-header">
            <h3>⭐ Saved Bookmarks</h3>
            <button class="modal-close-btn" onclick="closeBookmarksDrawer()">✕</button>
        </div>
        <div class="drawer-tabs">
            <button class="drawer-tab active" onclick="switchBookmarkTab('c', this)">💻 C Programming (<span id="c-bookmark-count">0</span>)</button>
            <button class="drawer-tab" onclick="switchBookmarkTab('math', this)">📐 Mathematics (<span id="math-bookmark-count">0</span>)</button>
        </div>
        <div class="drawer-content" id="bookmarks-list-container">
            <!-- Bookmarked items injected by JavaScript -->
        </div>
    </div>
</div>

<!-- Global Shared Interactive Engine -->
<script src="study-hub.js"></script>
</body>
</html>
""")

    return "".join(parts)

def main():
    print("Compiling full C Programming Textbook HTML (130 Questions)...")
    c_html_content = build_c_html()
    target_path = os.path.abspath("c_programming.html")

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(c_html_content)

    size = os.path.getsize(target_path)
    print(f"SUCCESS: 'c_programming.html' generated successfully! Size: {size:,} bytes ({size/(1024*1024):.2f} MB)")

if __name__ == "__main__":
    main()

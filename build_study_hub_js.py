# -*- coding: utf-8 -*-
"""
Generator for study-hub.js:
Extracts metadata from all 125 Math questions and 130 C Programming questions
to create a lightning-fast client-side search index and learning engine.
"""
import json

from module1_data import MODULE1_QUESTIONS
from module2_data import MODULE2_QUESTIONS
from module3_data import MODULE3_QUESTIONS
from module4_data import MODULE4_QUESTIONS
from module5_data import MODULE5_QUESTIONS

from c_module1_data import C_MODULE1_QUESTIONS
from c_module2_data import C_MODULE2_QUESTIONS
from c_module3_data import C_MODULE3_QUESTIONS
from c_module4_data import C_MODULE4_QUESTIONS
from c_module5_data import C_MODULE5_QUESTIONS

math_index = []
math_modules = [
    ("Module 1", MODULE1_QUESTIONS),
    ("Module 2", MODULE2_QUESTIONS),
    ("Module 3", MODULE3_QUESTIONS),
    ("Module 4", MODULE4_QUESTIONS),
    ("Module 5", MODULE5_QUESTIONS)
]
for mod_name, q_list in math_modules:
    for q in q_list:
        math_index.append({
            "subject": "math",
            "num": q["num"],
            "title": q["title"],
            "module": mod_name,
            "concept": q["concept"][:120],
            "url": f"1BMATS101_Complete_Textbook.html#q{q['num']}"
        })

c_index = []
c_modules = [
    ("Module 1", C_MODULE1_QUESTIONS),
    ("Module 2", C_MODULE2_QUESTIONS),
    ("Module 3", C_MODULE3_QUESTIONS),
    ("Module 4", C_MODULE4_QUESTIONS),
    ("Module 5", C_MODULE5_QUESTIONS)
]
for mod_name, q_list in c_modules:
    for q in q_list:
        c_index.append({
            "subject": "c",
            "num": q["num"],
            "title": q["title"],
            "module": mod_name,
            "category": q.get("category", "Core"),
            "concept": q["concept"][:120],
            "url": f"c_programming.html#c-q{q['num']}"
        })

js_content = f"""/* ==========================================================================
   STUDY HUB UNIFIED INTERACTIVE CLIENT-SIDE ENGINE
   Seamlessly powers Mathematics (1BMATS101) and C Programming
   ========================================================================== */

const MATH_SEARCH_INDEX = {json.dumps(math_index, indent=2)};
const C_SEARCH_INDEX = {json.dumps(c_index, indent=2)};

let currentSearchFilter = 'all';
let currentActiveBookmarkTab = 'c';

// Initialize when DOM loads
document.addEventListener('DOMContentLoaded', () => {{
    initSubjectNavigation();
    initLearningState();
    initShortcuts();
}});

/* ---- Navigation & Header Enhancement ---- */
function initSubjectNavigation() {{
    const topNav = document.getElementById('top-nav');
    if (!topNav) return;

    // Detect if we are on the Mathematics page and enhance top nav if needed
    const isMathPage = window.location.pathname.includes('1BMATS101') || 
                       document.title.includes('1BMATS101') ||
                       document.body.getAttribute('data-subject') === 'math';

    if (isMathPage && !document.querySelector('.nav-brand')) {{
        // We are on Mathematics page: Upgrade top nav with subject switcher tabs
        const navTitle = topNav.querySelector('.nav-title');
        if (navTitle) {{
            navTitle.innerHTML = `
                <div class="nav-brand">
                    <a href="1BMATS101_Complete_Textbook.html" class="subject-tab active" title="Active: Applied Mathematics Notes">📐 Mathematics (1BMATS101)</a>
                    <a href="c_programming.html" class="subject-tab" title="Switch to C Programming Notes">💻 C Programming</a>
                </div>
            `;
        }}

        // Add search and bookmark triggers to actions
        const navActions = topNav.querySelector('.nav-actions');
        if (navActions && !navActions.querySelector('.search-trigger-btn')) {{
            const searchBtn = document.createElement('button');
            searchBtn.className = 'nav-tool-btn search-trigger-btn';
            searchBtn.innerHTML = '🔍 <span class="btn-text">Search</span> <kbd class="kbd-hint">Ctrl K</kbd>';
            searchBtn.onclick = openSearchModal;
            navActions.insertBefore(searchBtn, navActions.firstChild);

            const bmBtn = document.createElement('button');
            bmBtn.className = 'nav-tool-btn';
            bmBtn.innerHTML = '⭐ <span class="btn-text">Bookmarks</span> (<span id="bookmark-count-badge">0</span>)';
            bmBtn.onclick = openBookmarksDrawer;
            navActions.insertBefore(bmBtn, searchBtn.nextSibling);

            // Add progress box
            const progBox = document.createElement('div');
            progBox.className = 'nav-progress-box';
            progBox.innerHTML = `
                <div class="progress-bar-bg"><div class="progress-bar-fill" id="subject-progress-fill" style="width: 0%;"></div></div>
                <span class="progress-text" id="subject-progress-text">0 / 125 (0%)</span>
            `;
            navActions.insertBefore(progBox, bmBtn.nextSibling);
        }}

        // Ensure search modal and drawer exist on math page too
        ensureModalsExist();
        document.body.setAttribute('data-subject', 'math');
    }}
}}

function ensureModalsExist() {{
    if (!document.getElementById('search-modal')) {{
        const modalDiv = document.createElement('div');
        modalDiv.id = 'search-modal';
        modalDiv.className = 'modal-backdrop';
        modalDiv.onclick = handleModalBackdropClick;
        modalDiv.innerHTML = `
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
        `;
        document.body.appendChild(modalDiv);
    }}

    if (!document.getElementById('bookmarks-drawer')) {{
        const drawerDiv = document.createElement('div');
        drawerDiv.id = 'bookmarks-drawer';
        drawerDiv.className = 'drawer-backdrop';
        drawerDiv.onclick = handleDrawerBackdropClick;
        drawerDiv.innerHTML = `
            <div class="drawer-panel">
                <div class="drawer-header">
                    <h3>⭐ Saved Bookmarks</h3>
                    <button class="modal-close-btn" onclick="closeBookmarksDrawer()">✕</button>
                </div>
                <div class="drawer-tabs">
                    <button class="drawer-tab" id="tab-btn-c" onclick="switchBookmarkTab('c', this)">💻 C Programming (<span id="c-bookmark-count">0</span>)</button>
                    <button class="drawer-tab" id="tab-btn-math" onclick="switchBookmarkTab('math', this)">📐 Mathematics (<span id="math-bookmark-count">0</span>)</button>
                </div>
                <div class="drawer-content" id="bookmarks-list-container">
                    <!-- Injected dynamically -->
                </div>
            </div>
        `;
        document.body.appendChild(drawerDiv);
    }}
}}

/* ---- Bookmarks & Progress State Management ---- */
function getStorageKey(type, subject) {{
    return `studyhub_${{type}}_${{subject}}`;
}}

function getBookmarks(subject) {{
    try {{
        return JSON.parse(localStorage.getItem(getStorageKey('bookmarks', subject)) || '[]');
    }} catch (e) {{
        return [];
    }}
}}

function saveBookmarks(subject, list) {{
    localStorage.setItem(getStorageKey('bookmarks', subject), JSON.stringify(list));
    updateBadges();
}}

function getMastered(subject) {{
    try {{
        return JSON.parse(localStorage.getItem(getStorageKey('mastered', subject)) || '[]');
    }} catch (e) {{
        return [];
    }}
}}

function saveMastered(subject, list) {{
    localStorage.setItem(getStorageKey('mastered', subject), JSON.stringify(list));
    updateProgressUI();
}}

function initLearningState() {{
    const currentSubject = document.body.getAttribute('data-subject') || 'c';

    // Restore bookmarks buttons
    const bmList = getBookmarks(currentSubject);
    bmList.forEach(num => {{
        const btn = document.querySelector(`.bookmark-btn[data-q="${{num}}"]`);
        if (btn) {{
            btn.classList.add('bookmarked');
            btn.innerHTML = '★ Bookmarked';
        }}
    }});

    // Restore mastered checkboxes
    const masteredList = getMastered(currentSubject);
    masteredList.forEach(num => {{
        const cb = document.querySelector(`.mastered-checkbox[data-q="${{num}}"]`);
        if (cb) {{
            cb.checked = true;
            const label = cb.closest('.mastered-label');
            if (label) label.classList.add('is-mastered');
        }}
    }});

    updateBadges();
    updateProgressUI();
}}

function toggleBookmark(subject, qNum, btn) {{
    let list = getBookmarks(subject);
    const index = list.indexOf(qNum);

    if (index === -1) {{
        list.push(qNum);
        if (btn) {{
            btn.classList.add('bookmarked');
            btn.innerHTML = '★ Bookmarked';
        }}
    }} else {{
        list.splice(index, 1);
        if (btn) {{
            btn.classList.remove('bookmarked');
            btn.innerHTML = '⭐ Bookmark';
        }}
    }}

    saveBookmarks(subject, list);
    renderBookmarksDrawerContent();
}}

function toggleMastered(subject, qNum, checkbox) {{
    let list = getMastered(subject);
    const index = list.indexOf(qNum);

    if (checkbox.checked) {{
        if (index === -1) list.push(qNum);
        const label = checkbox.closest('.mastered-label');
        if (label) label.classList.add('is-mastered');
    }} else {{
        if (index !== -1) list.splice(index, 1);
        const label = checkbox.closest('.mastered-label');
        if (label) label.classList.remove('is-mastered');
    }}

    saveMastered(subject, list);
}}

function updateProgressUI() {{
    const currentSubject = document.body.getAttribute('data-subject') || 'c';
    const total = currentSubject === 'c' ? 130 : 125;
    const list = getMastered(currentSubject);
    const completedCount = list.length;
    const percent = Math.min(100, Math.round((completedCount / total) * 100));

    const fill = document.getElementById('subject-progress-fill');
    const text = document.getElementById('subject-progress-text');
    if (fill) fill.style.width = `${{percent}}%`;
    if (text) text.innerText = `${{completedCount}} / ${{total}} (${{percent}}%)`;
}}

function updateBadges() {{
    const currentSubject = document.body.getAttribute('data-subject') || 'c';
    const cBookmarks = getBookmarks('c');
    const mathBookmarks = getBookmarks('math');

    const totalCurrent = currentSubject === 'c' ? cBookmarks.length : mathBookmarks.length;

    const navBadge = document.getElementById('bookmark-count-badge');
    if (navBadge) navBadge.innerText = totalCurrent;

    const cCountEl = document.getElementById('c-bookmark-count');
    if (cCountEl) cCountEl.innerText = cBookmarks.length;

    const mathCountEl = document.getElementById('math-bookmark-count');
    if (mathCountEl) mathCountEl.innerText = mathBookmarks.length;
}}

/* ---- Search Engine Implementation ---- */
function openSearchModal() {{
    ensureModalsExist();
    const modal = document.getElementById('search-modal');
    if (modal) {{
        modal.classList.add('active');
        const input = document.getElementById('global-search-input');
        if (input) {{
            input.focus();
            input.select();
        }}
    }}
}}

function closeSearchModal() {{
    const modal = document.getElementById('search-modal');
    if (modal) modal.classList.remove('active');
}}

function handleModalBackdropClick(e) {{
    if (e.target.id === 'search-modal') closeSearchModal();
}}

function setSearchFilter(filter, btn) {{
    currentSearchFilter = filter;
    document.querySelectorAll('.search-filters .filter-tab').forEach(t => t.classList.remove('active'));
    if (btn) btn.classList.add('active');
    const input = document.getElementById('global-search-input');
    if (input) performGlobalSearch(input.value);
}}

function performGlobalSearch(query) {{
    const container = document.getElementById('search-results-container');
    if (!container) return;

    const cleanQ = query.trim().toLowerCase();
    if (!cleanQ) {{
        container.innerHTML = '<div class="search-placeholder">Type keywords, question numbers, topics, or formulas above to search...</div>';
        return;
    }}

    let combined = [];
    if (currentSearchFilter === 'all' || currentSearchFilter === 'math') {{
        combined = combined.concat(MATH_SEARCH_INDEX);
    }}
    if (currentSearchFilter === 'all' || currentSearchFilter === 'c') {{
        combined = combined.concat(C_SEARCH_INDEX);
    }}

    const matches = combined.filter(item => {{
        const qNumStr = `q${{item.num}}`;
        const numStr = `${{item.num}}`;
        return item.title.toLowerCase().includes(cleanQ) ||
               item.module.toLowerCase().includes(cleanQ) ||
               (item.category && item.category.toLowerCase().includes(cleanQ)) ||
               (item.concept && item.concept.toLowerCase().includes(cleanQ)) ||
               qNumStr === cleanQ ||
               numStr === cleanQ;
    }});

    if (matches.length === 0) {{
        container.innerHTML = `<div class="search-placeholder">No matching questions found for "${{escapeHtml(query)}}". Try searching for "derivative", "bubble sort", "pointer", "matrix", etc.</div>`;
        return;
    }}

    container.innerHTML = matches.slice(0, 40).map(item => {{
        const isC = item.subject === 'c';
        const subjName = isC ? 'C Programming' : 'Applied Mathematics';
        const subjClass = isC ? 'c' : 'math';
        return `
            <a href="${{item.url}}" class="search-result-item" onclick="closeSearchModal()">
                <div class="res-header">
                    <span class="res-subject ${{subjClass}}">${{subjName}}</span>
                    <span style="color:#64748b; font-weight:700;">${{item.module}} • Q${{item.num}}</span>
                </div>
                <div class="res-title">${{escapeHtml(item.title)}}</div>
                <div class="res-snippet">${{escapeHtml(item.concept || '')}}</div>
            </a>
        `;
    }}).join('');
}}

/* ---- Bookmarks Drawer Implementation ---- */
function openBookmarksDrawer() {{
    ensureModalsExist();
    const drawer = document.getElementById('bookmarks-drawer');
    if (drawer) {{
        drawer.classList.add('active');
        const currentSubject = document.body.getAttribute('data-subject') || 'c';
        switchBookmarkTab(currentSubject);
    }}
}}

function closeBookmarksDrawer() {{
    const drawer = document.getElementById('bookmarks-drawer');
    if (drawer) drawer.classList.remove('active');
}}

function handleDrawerBackdropClick(e) {{
    if (e.target.id === 'bookmarks-drawer') closeBookmarksDrawer();
}}

function switchBookmarkTab(subject, btn) {{
    currentActiveBookmarkTab = subject;
    document.querySelectorAll('.drawer-tabs .drawer-tab').forEach(t => t.classList.remove('active'));
    const targetTabBtn = btn || document.getElementById(`tab-btn-${{subject}}`);
    if (targetTabBtn) targetTabBtn.classList.add('active');
    renderBookmarksDrawerContent();
}}

function renderBookmarksDrawerContent() {{
    const container = document.getElementById('bookmarks-list-container');
    if (!container) return;

    const list = getBookmarks(currentActiveBookmarkTab);
    const indexList = currentActiveBookmarkTab === 'c' ? C_SEARCH_INDEX : MATH_SEARCH_INDEX;

    if (list.length === 0) {{
        container.innerHTML = `
            <div style="padding: 40px 20px; text-align: center; color: #94a3b8;">
                <p style="font-size: 28px; margin: 0 0 10px 0;">⭐</p>
                <p style="font-weight: 600;">No bookmarked questions in ${{currentActiveBookmarkTab === 'c' ? 'C Programming' : 'Mathematics'}} yet.</p>
                <p style="font-size: 12px;">Click the ⭐ Bookmark button on any question card to save it for rapid revision.</p>
            </div>
        `;
        return;
    }}

    container.innerHTML = list.map(qNum => {{
        const item = indexList.find(i => i.num === qNum);
        if (!item) return '';
        return `
            <div class="bookmark-item">
                <a href="${{item.url}}" class="bm-info" onclick="closeBookmarksDrawer()">
                    <div class="bm-qnum">${{item.module}} • Question ${{item.num}}</div>
                    <div class="bm-title">${{escapeHtml(item.title)}}</div>
                </a>
                <button class="bm-remove-btn" onclick="toggleBookmark('${{currentActiveBookmarkTab}}', ${{item.num}}); event.stopPropagation();" title="Remove Bookmark">✕</button>
            </div>
        `;
    }}).join('');
}}

/* ---- Copy Code Utility ---- */
function copyCode(btn) {{
    const codeBlock = btn.closest('.code-container').querySelector('.code-block code');
    if (!codeBlock) return;

    const textToCopy = codeBlock.innerText;
    if (navigator.clipboard && navigator.clipboard.writeText) {{
        navigator.clipboard.writeText(textToCopy).then(() => {{
            showCopiedFeedback(btn);
        }}).catch(() => {{
            fallbackCopy(textToCopy, btn);
        }});
    }} else {{
        fallbackCopy(textToCopy, btn);
    }}
}}

function fallbackCopy(text, btn) {{
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.left = '-9999px';
    document.body.appendChild(textarea);
    textarea.focus();
    textarea.select();
    try {{
        document.execCommand('copy');
        showCopiedFeedback(btn);
    }} catch (err) {{
        console.error('Fallback copy failed', err);
    }}
    document.body.removeChild(textarea);
}}

function showCopiedFeedback(btn) {{
    const originalText = btn.innerHTML;
    btn.innerHTML = '✓ Copied!';
    btn.classList.add('copied');
    setTimeout(() => {{
        btn.innerHTML = originalText;
        btn.classList.remove('copied');
    }}, 2000);
}}

/* ---- Keyboard Shortcuts ---- */
function initShortcuts() {{
    window.addEventListener('keydown', (e) => {{
        // Ctrl+K or Cmd+K opens search
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {{
            e.preventDefault();
            openSearchModal();
        }}
        // Escape closes modals
        if (e.key === 'Escape') {{
            closeSearchModal();
            closeBookmarksDrawer();
        }}
    }});
}}

function escapeHtml(str) {{
    if (!str) return '';
    return str.replace(/&/g, '&amp;')
              .replace(/</g, '&lt;')
              .replace(/>/g, '&gt;')
              .replace(/"/g, '&quot;')
              .replace(/'/g, '&#039;');
}}
"""

with open("study-hub.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"SUCCESS: study-hub.js generated successfully! Size: {len(js_content):,} bytes")

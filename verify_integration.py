import os
import re

def verify():
    assert os.path.exists('1BMATS101_Complete_Textbook.html')
    assert os.path.exists('c_programming.html')
    assert os.path.exists('study-hub.css')
    assert os.path.exists('study-hub.js')
    
    m_size = os.path.getsize('1BMATS101_Complete_Textbook.html')
    c_size = os.path.getsize('c_programming.html')
    css_size = os.path.getsize('study-hub.css')
    js_size = os.path.getsize('study-hub.js')
    print(f"Math HTML size: {m_size:,} bytes")
    print(f"C Programming HTML size: {c_size:,} bytes")
    print(f"CSS size: {css_size:,} bytes")
    print(f"JS size: {js_size:,} bytes")
    
    with open('1BMATS101_Complete_Textbook.html', 'r', encoding='utf-8') as f:
        m_content = f.read()
    with open('c_programming.html', 'r', encoding='utf-8') as f:
        c_content = f.read()
        
    # Check Math question anchors
    m_q_matches = re.findall(r'id=["\']q(\d+)["\']', m_content)
    print(f"Math question IDs found: {len(m_q_matches)} (First: {m_q_matches[0] if m_q_matches else 'None'}, Last: {m_q_matches[-1] if m_q_matches else 'None'})")
    assert len(m_q_matches) == 125, f"Expected 125 math question IDs, got {len(m_q_matches)}"
    
    # Check C question anchors
    c_q_matches = re.findall(r'id=["\']c-q(\d+)["\']', c_content)
    print(f"C Programming question IDs found: {len(c_q_matches)} (First: {c_q_matches[0] if c_q_matches else 'None'}, Last: {c_q_matches[-1] if c_q_matches else 'None'})")
    assert len(c_q_matches) == 130, f"Expected 130 C question IDs, got {len(c_q_matches)}"
    
    # Check subject switcher in both
    assert 'c_programming.html' in m_content, "Math HTML missing link to C programming"
    assert '1BMATS101_Complete_Textbook.html' in c_content, "C HTML missing link to Math"
    assert 'study-hub.css' in m_content and 'study-hub.css' in c_content
    assert 'study-hub.js' in m_content and 'study-hub.js' in c_content
    
    # Check modules in C content
    for mod in [1, 2, 3, 4, 5]:
        assert f'id="module-{mod}"' in c_content, f"Missing id=module-{mod}"
        
    print("ALL INTEGRATION CHECKS PASSED PERFECTLY!")

if __name__ == '__main__':
    verify()

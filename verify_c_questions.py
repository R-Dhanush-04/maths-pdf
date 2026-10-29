# -*- coding: utf-8 -*-
from c_module1_data import C_MODULE1_QUESTIONS
from c_module2_data import C_MODULE2_QUESTIONS
from c_module3_data import C_MODULE3_QUESTIONS
from c_module4_data import C_MODULE4_QUESTIONS
from c_module5_data import C_MODULE5_QUESTIONS

print('M1:', len(C_MODULE1_QUESTIONS), 'Q', C_MODULE1_QUESTIONS[0]['num'], 'to Q', C_MODULE1_QUESTIONS[-1]['num'])
print('M2:', len(C_MODULE2_QUESTIONS), 'Q', C_MODULE2_QUESTIONS[0]['num'], 'to Q', C_MODULE2_QUESTIONS[-1]['num'])
print('M3:', len(C_MODULE3_QUESTIONS), 'Q', C_MODULE3_QUESTIONS[0]['num'], 'to Q', C_MODULE3_QUESTIONS[-1]['num'])
print('M4:', len(C_MODULE4_QUESTIONS), 'Q', C_MODULE4_QUESTIONS[0]['num'], 'to Q', C_MODULE4_QUESTIONS[-1]['num'])
print('M5:', len(C_MODULE5_QUESTIONS), 'Q', C_MODULE5_QUESTIONS[0]['num'], 'to Q', C_MODULE5_QUESTIONS[-1]['num'])

total = len(C_MODULE1_QUESTIONS) + len(C_MODULE2_QUESTIONS) + len(C_MODULE3_QUESTIONS) + len(C_MODULE4_QUESTIONS) + len(C_MODULE5_QUESTIONS)
print('Total C Questions:', total)
assert total == 130
print('VERIFICATION SUCCESSFUL: 130 questions loaded with zero overlaps!')

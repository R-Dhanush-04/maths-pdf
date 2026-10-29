# -*- coding: utf-8 -*-
"""
Module 3: Matrices and Systems of Linear Equations
100% Pure English Edition
Includes 25 Fully Solved Questions (5 Fundamental + 10 Intermediate + 10 Exam-Level)
"""

MODULE3_QUESTIONS = [   {   'concept': 'The rank of a matrix is the maximum number of linearly independent rows (or columns). Elementary '
                   'row operations do not alter the rank.',
        'difficulty': 'Fundamental',
        'final_answer': 'Rank ρ(A) = 1',
        'formula': 'Rank ρ(A) = Number of non-zero rows in row-echelon form.',
        'formula_expl': 'A non-zero row contains at least one non-zero entry.',
        'given': 'A = [[1, 2, 3], [2, 4, 6], [3, 6, 9]].',
        'meaning_en': 'Transform matrix A into an upper triangular row-echelon form using elementary row operations '
                      'and count the number of non-zero rows, which equals the rank.',
        'mistakes': [   (   'Saying rank is 0 because two rows became zero.',
                            'Rank is the number of NON-ZERO rows, so it is 1, not 0!'),
                        (   'Using column operations when asked for row-echelon form.',
                            'Row-echelon form strictly requires ROW operations.')],
        'num': 51,
        'practice_q': 'Find rank of A = [[1, -1, 2], [2, -2, 4], [-1, 1, -2]].',
        'presentation': [   'State row operations R₂ → R₂ - 2R₁ and R₃ → R₃ - 3R₁ explicitly.',
                            'Show intermediate matrices.',
                            'State definition: Rank = number of non-zero rows = 1.'],
        'question': 'Find the rank of the matrix A = [[1, 2, 3], [2, 4, 6], [3, 6, 9]] by reducing it to row-echelon '
                    'form.',
        'steps': [   (   'Step 1: Write the initial matrix',
                         'A = [ [1, 2, 3], [2, 4, 6], [3, 6, 9] ]. Pivot in row 1 is 1.',
                         'Execute step 1: write the initial matrix to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Apply row operations to eliminate entries below pivot',
                         'R₂ → R₂ - 2R₁:<br>[2 - 2(1), 4 - 2(2), 6 - 2(3)] = [0, 0, 0].<br>R₃ → R₃ - 3R₁:<br>[3 - '
                         '3(1), 6 - 3(2), 9 - 3(3)] = [0, 0, 0].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: State the reduced row-echelon matrix',
                         'A ~ [ [1, 2, 3], [0, 0, 0], [0, 0, 0] ].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 4: Count non-zero rows to find rank',
                         'There is only 1 non-zero row: [1, 2, 3]. Rows 2 and 3 are entirely zero.<br>Therefore, Rank '
                         'ρ(A) = 1.',
                         'Count the number of non-zero rows in the row-echelon form; this count equals the rank of the '
                         'matrix.')],
        'title': 'Rank of a 2×2 and 3×3 Matrix by Elementary Row Operations'},
    {   'concept': 'Eigenvalues λ are scalars such that A v = λ v for some non-zero vector v. They represent the scale '
                   'factors by which eigenvector directions are stretched or flipped.',
        'difficulty': 'Fundamental',
        'final_answer': 'Characteristic Equation: λ² - 7λ + 10 = 0;  Eigenvalues: λ = 2, 5',
        'formula': '|A - λI| = 0  ⇒  λ² - (Trace A) λ + det(A) = 0.',
        'formula_expl': 'Trace(A) = sum of main diagonal entries; det(A) = ad - bc.',
        'given': 'A = [[4, 1], [2, 3]].',
        'meaning_en': 'Set up the characteristic polynomial det(A - λI) = 0 and solve the quadratic equation for the '
                      'eigenvalues λ.',
        'mistakes': [   (   'Sign error in quadratic: writing +7λ instead of -7λ.',
                            'Formula is λ² MINUS (Trace)λ PLUS det = 0.'),
                        ('Arithmetic error in det: 4(3) + 1(2).', 'Determinant formula is ad - bc.')],
        'num': 52,
        'practice_q': 'Find eigenvalues of A = [[5, 4], [1, 2]].',
        'presentation': [   'State formula |A - λI| = 0.',
                            'Show Trace and Determinant calculations.',
                            'Factorize quadratic equation.',
                            'Verify using sum and product properties.'],
        'question': 'Find the characteristic equation and eigenvalues of the matrix A = [[4, 1], [2, 3]].',
        'steps': [   (   'Step 1: Compute Trace and Determinant of A',
                         'Trace(A) = 4 + 3 = 7.<br>det(A) = (4)(3) - (1)(2) = 12 - 2 = 10.',
                         'Execute step 1: compute trace and determinant of a to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Write the characteristic equation',
                         'λ² - (Trace A) λ + det(A) = 0<br>λ² - 7λ + 10 = 0.',
                         'Set up the characteristic determinant det(A - λI) = 0 and expand to obtain the '
                         'characteristic polynomial.'),
                     (   'Step 3: Factorize the quadratic polynomial',
                         '(λ - 2)(λ - 5) = 0.',
                         'Execute step 3: factorize the quadratic polynomial to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Solve for eigenvalues λ',
                         'λ₁ = 2,   λ₂ = 5.',
                         'Find the roots of the characteristic polynomial to determine all scalar eigenvalues.'),
                     (   'Step 5: Verify with properties',
                         'Sum of eigenvalues = 2 + 5 = 7 = Trace(A). Verified!<br>Product of eigenvalues = 2 · 5 = 10 '
                         '= det(A). Verified!',
                         'Execute step 5: verify with properties to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Characteristic Equation and Eigenvalues of a 2×2 Matrix'},
    {   'concept': 'The augmented matrix [A | B] combines coefficients and constants. The system is solvable if and '
                   'only if appending B does not increase the rank of A.',
        'difficulty': 'Fundamental',
        'final_answer': 'Rouché-Capelli Theorem: (i) Inconsistent: ρ(A) ≠ ρ([A|B]); (ii) Unique: ρ(A) = ρ([A|B]) = n; '
                        '(iii) Infinite: ρ(A) = ρ([A|B]) = r < n with (n-r) arbitrary parameters.',
        'formula': 'Let ρ(A) = rank of coefficient matrix, ρ([A|B]) = rank of augmented matrix, n = number of '
                   'unknowns.',
        'formula_expl': '• Inconsistent (No solution): ρ(A) ≠ ρ([A|B]).<br>• Consistent: ρ(A) = ρ([A|B]) = r.<br>  - '
                        'Unique solution: r = n.<br>  - Infinitely many solutions: r < n (with n - r free parameters).',
        'given': 'System AX = B, coefficient matrix A (m×n), augmented matrix [A|B] (m×(n+1)).',
        'meaning_en': 'Explain the necessary and sufficient rank conditions for a non-homogeneous linear system AX = B '
                      'to have unique, infinitely many, or no solutions.',
        'mistakes': [   (   'Confusing m (number of equations) with n (number of unknowns).',
                            'Always compare rank r with n (number of variables/columns of A)!'),
                        (   'Claiming ρ(A) > ρ([A|B]).',
                            'Appending a column cannot decrease rank, so ρ(A) ≤ ρ([A|B]) always.')],
        'num': 53,
        'practice_q': 'If A is a 3×4 matrix and ρ(A) = ρ([A|B]) = 2, how many arbitrary parameters does the solution '
                      'possess?',
        'presentation': [   'Draw a clear summary table of the 3 cases.',
                            'Define n as the number of unknowns.',
                            'Mention the number of free parameters (n - r).'],
        'question': 'State the Rouché-Capelli theorem for the system of linear equations AX = B with n variables, and '
                    'classify the types of solutions based on rank.',
        'steps': [   (   'Step 1: State Condition for Inconsistency (No Solution)',
                         'If ρ(A) < ρ([A|B]), the system is INCONSISTENT and has NO SOLUTION.<br>In echelon form, this '
                         'corresponds to a row of the form [0, 0, ..., 0 | k] where k ≠ 0 (e.g., 0 = k, which is '
                         'impossible).',
                         'Compare the rank of the coefficient matrix ρ(A) with the augmented matrix ρ([A|B]) using the '
                         'Rouché-Capelli criteria.'),
                     (   'Step 2: State Condition for Unique Solution',
                         'If ρ(A) = ρ([A|B]) = n (where n is the number of unknowns), the system is CONSISTENT and has '
                         'a UNIQUE SOLUTION.<br>Every column has a pivot; no free variables exist.',
                         'Execute step 2: state condition for unique solution to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: State Condition for Infinitely Many Solutions',
                         'If ρ(A) = ρ([A|B]) = r < n, the system is CONSISTENT and has INFINITELY MANY '
                         'SOLUTIONS.<br>There are (n - r) free parameters (independent arbitrary constants).',
                         'Execute step 3: state condition for infinitely many solutions to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Consistency Criteria for Linear Systems (Rouché-Capelli Theorem)'},
    {   'concept': 'For homogeneous systems, X = 0 (all zeros) is always a solution, called the trivial solution. '
                   'Non-trivial solutions exist if and only if det(A) = 0 (or rank ρ(A) < n).',
        'difficulty': 'Fundamental',
        'final_answer': 'Non-trivial solution condition: det(A) = 0 (or rank < n);  Solution: X = [k, -2k, k]ᵀ = k [1, '
                        '-2, 1]ᵀ, where k is any non-zero real number.',
        'formula': 'Non-trivial solution condition: det(A) = 0 or rank ρ(A) < n.',
        'formula_expl': 'If det(A) ≠ 0, only the trivial solution X = [0, 0, 0]ᵀ exists.',
        'given': 'A = [[1, 2, 3], [2, 4, 6], [1, 1, 1]], AX = 0.',
        'meaning_en': 'Explain when AX = 0 has solutions other than X = 0, and find the solution for the given '
                      'coefficient matrix.',
        'mistakes': [   (   'Saying k = 0 is a non-trivial solution.',
                            'If k = 0, X = 0 which is the TRIVIAL solution. Non-trivial means k ≠ 0.'),
                        (   'Forgetting to introduce the parameter k.',
                            'When rank < n, one or more variables MUST be assigned free parameters.')],
        'num': 54,
        'practice_q': 'Determine if [[1, 1, 1], [2, 2, 2], [3, 3, 3]] X = 0 has non-trivial solutions and find them.',
        'presentation': [   'State condition det(A) = 0 clearly.',
                            'Row reduce coefficient matrix.',
                            'Express solution as vector multiplied by parameter k.'],
        'question': 'For a homogeneous system AX = 0 of 3 equations in 3 variables, state the condition for a '
                    'non-trivial (non-zero) solution and solve [[1, 2, 3], [2, 4, 6], [1, 1, 1]] X = 0.',
        'steps': [   (   'Step 1: Reduce A to echelon form',
                         'A = [ [1, 2, 3], [2, 4, 6], [1, 1, 1] ].<br>R₂ → R₂ - 2R₁: [0, 0, 0].<br>R₃ → R₃ - R₁: [0, '
                         '-1, -2].',
                         'Execute step 1: reduce a to echelon form to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Swap R₂ and R₃ to form row-echelon form',
                         'A ~ [ [1, 2, 3], [0, -1, -2], [0, 0, 0] ].<br>Number of non-zero rows = 2. Rank ρ(A) = '
                         '2.<br>Number of variables n = 3.',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: Determine number of free parameters',
                         'Number of free parameters = n - r = 3 - 2 = 1 free parameter (let z = k).',
                         'Execute step 3: determine number of free parameters to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Back-substitute to find x and y in terms of k',
                         'From Row 2: -y - 2z = 0  ⇒  y = -2z = -2k.<br>From Row 1: x + 2y + 3z = 0  ⇒  x + 2(-2k) + '
                         '3k = 0  ⇒  x - 4k + 3k = 0  ⇒  x - k = 0  ⇒  x = k.',
                         'Execute step 4: back-substitute to find x and y in terms of k to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Homogeneous Linear System AX = 0 (Trivial vs Non-Trivial Solutions)'},
    {   'concept': 'For any n×n matrix: (1) Σ λ_i = Trace(A), (2) Π λ_i = det(A). This provides two algebraic '
                   'equations connecting the eigenvalues.',
        'difficulty': 'Fundamental',
        'final_answer': 'The other two eigenvalues are λ₂ = 3 and λ₃ = 4 (All three eigenvalues are 2, 3, 4)',
        'formula': 'λ₁ + λ₂ + λ₃ = 9;  λ₁ · λ₂ · λ₃ = 24;  with λ₁ = 2.',
        'formula_expl': 'Trace and determinant properties reduce higher degree polynomials to simple quadratics.',
        'given': 'λ₁ + λ₂ + λ₃ = 9, λ₁ λ₂ λ₃ = 24, λ₁ = 2.',
        'meaning_en': 'Use the fundamental properties that sum of eigenvalues equals trace and product of eigenvalues '
                      'equals determinant to find the unknown eigenvalues.',
        'mistakes': [   (   'Guessing roots without showing quadratic equation.',
                            'Always form t² - (sum)t + prod = 0 to show mathematical rigor.'),
                        ('Arithmetic mistake in 24 / 2 = 12.', 'Check division carefully.')],
        'num': 55,
        'practice_q': 'Two eigenvalues of a 3×3 matrix with Trace = 6 and det = 6 are 1 and 2. Find the third '
                      'eigenvalue.',
        'presentation': [   'State Trace property: Σ λ_i = Trace.',
                            'State Determinant property: Π λ_i = det.',
                            'Form quadratic t² - 7t + 12 = 0 and solve.'],
        'question': 'If the sum of eigenvalues of a 3×3 matrix A is 9 and their product is 24, and one eigenvalue is '
                    'λ₁ = 2, find the other two eigenvalues.',
        'steps': [   (   'Step 1: Substitute λ₁ = 2 into the sum equation',
                         '2 + λ₂ + λ₃ = 9  ⇒  λ₂ + λ₃ = 9 - 2 = 7.',
                         'Execute step 1: substitute λ₁ = 2 into the sum equation to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Substitute λ₁ = 2 into the product equation',
                         '2 · λ₂ · λ₃ = 24  ⇒  λ₂ · λ₃ = 24 / 2 = 12.',
                         'Execute step 2: substitute λ₁ = 2 into the product equation to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Form the quadratic equation for λ₂ and λ₃',
                         'The two numbers whose sum is 7 and product is 12 are roots of:<br>t² - (sum) t + (product) = '
                         '0<br>t² - 7t + 12 = 0.',
                         'Execute step 3: form the quadratic equation for λ₂ and λ₃ to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Factorize and solve',
                         '(t - 3)(t - 4) = 0  ⇒  t = 3  or  t = 4.<br>Therefore, λ₂ = 3 and λ₃ = 4.',
                         'Execute step 4: factorize and solve to advance the step-by-step mathematical solution toward '
                         'the final result.')],
        'title': 'Properties of Eigenvalues (Trace and Determinant)'},
    {   'concept': 'For an m×n matrix, rank ≤ min(m, n). Here rank ≤ min(3, 4) = 3.',
        'difficulty': 'Intermediate',
        'final_answer': 'Rank ρ(A) = 3',
        'formula': 'Rank = number of non-zero rows in row-echelon form.',
        'formula_expl': 'Pivot elements must step to the right in each successive row.',
        'given': 'A = [[1, 2, -1, 4], [2, 4, 3, 4], [1, 2, 3, 4]].',
        'meaning_en': 'Apply elementary row operations to reduce this 3×4 rectangular matrix to row-echelon form and '
                      'determine its rank.',
        'mistakes': [   (   'Arithmetic error in 4 - 2(-1) = 6 instead of 3 - (-2) = 5.',
                            'Double minus is positive: 3 - 2(-1) = 3 + 2 = 5.'),
                        (   'Trying to make column 2 pivot.',
                            'Column 2 has all zeros below row 1, so the pivot moves to column 3.')],
        'num': 56,
        'practice_q': 'Find rank of A = [[1, 1, 1, 1], [1, 2, 3, -4], [2, 3, 5, -5]].',
        'presentation': [   'Show each row operation with intermediate arithmetic.',
                            'State the final echelon matrix clearly.',
                            'Count non-zero rows = 3.'],
        'question': 'Find the rank of the matrix A = [[1, 2, -1, 4], [2, 4, 3, 4], [1, 2, 3, 4]] by reducing to '
                    'row-echelon form.',
        'steps': [   (   'Step 1: Eliminate entries below pivot a₁₁ = 1',
                         'R₂ → R₂ - 2R₁:<br>[2 - 2(1), 4 - 2(2), 3 - 2(-1), 4 - 2(4)] = [0, 0, 5, -4].<br>R₃ → R₃ - '
                         'R₁:<br>[1 - 1, 2 - 2, 3 - (-1), 4 - 4] = [0, 0, 4, 0].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 2: Matrix after first sweep',
                         'A ~ [ [1, 2, -1, 4], [0, 0, 5, -4], [0, 0, 4, 0] ].',
                         'Execute step 2: matrix after first sweep to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 3: Eliminate entry below pivot in column 3',
                         'R₃ → 5R₃ - 4R₂:<br>[0, 0, 5(4) - 4(5), 5(0) - 4(-4)] = [0, 0, 0, 16].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 4: Examine row-echelon form',
                         'A ~ [ [1, 2, -1, 4], [0, 0, 5, -4], [0, 0, 0, 16] ].<br>All 3 rows contain non-zero elements '
                         '(Row 1 has 1, Row 2 has 5, Row 3 has 16).<br>Number of non-zero rows = 3.<br>Therefore, Rank '
                         'ρ(A) = 3.',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.')],
        'title': 'Rank of a 3×4 Matrix by Echelon Form'},
    {   'concept': 'Gauss elimination reduces the augmented matrix [A|B] to row-echelon form, transforming a coupled '
                   'system into a triangular system that is solved from bottom to top.',
        'difficulty': 'Intermediate',
        'final_answer': 'x = 7,   y = -9,   z = 5',
        'formula': "[A | B] ~ [U | B'] where U is upper triangular.",
        'formula_expl': 'Back-substitution: solve z first, then y, then x.',
        'given': 'System of 3 equations in 3 variables.',
        'meaning_en': 'Convert the augmented matrix [A|B] to upper triangular row-echelon form using elementary row '
                      'operations, then solve for x, y, z by back-substitution.',
        'mistakes': [   (   'Arithmetic error in 5(-22) + 7(15) = -110 + 105 = -5.',
                            'Be very careful with mental arithmetic; write every multiplication out!'),
                        (   'Forgetting to apply row operations to the RHS column B.',
                            'Any row operation applies to the ENTIRE row, including the constant term!')],
        'num': 57,
        'practice_q': 'Solve by Gauss elimination: x + y + z = 6, 2x - y + z = 3, x + 2y - z = 2.',
        'presentation': [   'State augmented matrix clearly.',
                            'Show row operations explicitly.',
                            'Show back-substitution step by step.',
                            'Verify in at least one original equation.'],
        'question': 'Solve the system of equations using Gauss Elimination method:<br>2x + y + z = 10,<br>3x + 2y + 3z '
                    '= 18,<br>x + 4y + 9z = 16.',
        'steps': [   (   'Step 1: Set up Augmented Matrix and swap R₁ and R₃ for pivot 1',
                         'Augmented matrix [A|B]:<br>[ [2, 1, 1 | 10], [3, 2, 3 | 18], [1, 4, 9 | 16] ].<br>Swap R₁ ↔ '
                         'R₃ to get pivot 1 in (1, 1):<br>[ [1, 4, 9 | 16], [3, 2, 3 | 18], [2, 1, 1 | 10] ].',
                         'Execute step 1: set up augmented matrix and swap r₁ and r₃ for pivot 1 to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 2: Eliminate x from Row 2 and Row 3',
                         'R₂ → R₂ - 3R₁:<br>[3-3, 2-12, 3-27 | 18-48] = [0, -10, -24 | -30]  ⇒  divide by -2: [0, 5, '
                         '12 | 15].<br>R₃ → R₃ - 2R₁:<br>[2-2, 1-8, 1-18 | 10-32] = [0, -7, -17 | -22].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: Eliminate y from Row 3',
                         'Current matrix:<br>[ [1, 4, 9 | 16], [0, 5, 12 | 15], [0, -7, -17 | -22] ].<br>R₃ → 5R₃ + '
                         '7R₂:<br>[0, -35 + 35, 5(-17) + 7(12) | 5(-22) + 7(15)]<br>= [0, 0, -85 + 84 | -110 + 105] = '
                         '[0, 0, -1 | -5]  ⇒  [0, 0, 1 | 5].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 4: Back-substitution',
                         'From Row 3: z = 5.<br>From Row 2: 5y + 12z = 15  ⇒  5y + 12(5) = 15  ⇒  5y + 60 = 15  ⇒  5y '
                         '= -45  ⇒  y = -9.<br>From Row 1: x + 4y + 9z = 16  ⇒  x + 4(-9) + 9(5) = 16  ⇒  x - 36 + 45 '
                         '= 16  ⇒  x + 9 = 16  ⇒  x = 7.',
                         'Substitute known variable values upward from the bottom row equation to determine each '
                         'variable uniquely.'),
                     (   'Step 5: Verify in original Equation 1',
                         '2x + y + z = 2(7) + (-9) + 5 = 14 - 9 + 5 = 10. Exactly matches RHS! Verified.',
                         'Execute step 5: verify in original equation 1 to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Solving Linear System by Gauss Elimination (Unique Solution)'},
    {   'concept': 'While Gauss elimination stops at upper triangular form, Gauss-Jordan continues by eliminating '
                   'entries ABOVE each pivot as well, converting A directly into the identity matrix I.',
        'difficulty': 'Intermediate',
        'final_answer': 'x = 1,   y = 3,   z = 5',
        'formula': "[A | B] ~ [I | X]  ⇒  x = b'₁, y = b'₂, z = b'₃.",
        'formula_expl': 'Elimination is performed both downwards and upwards.',
        'given': 'System of 3 equations in 3 variables.',
        'meaning_en': 'Reduce the augmented matrix [A|B] all the way to diagonal form [I | X] using elementary row '
                      'operations, reading off solutions directly without back-substitution.',
        'mistakes': [   (   'Doing back-substitution instead of Gauss-Jordan.',
                            'In Gauss-Jordan, you MUST reduce A to the identity matrix [I | X]; do not use '
                            'back-substitution!'),
                        ('Arithmetic error in 13 - 10 = 3.', 'Take time on each subtraction step.')],
        'num': 58,
        'practice_q': 'Solve by Gauss-Jordan method: x + y + z = 3, 2x + 3y + z = 6, x - y + 2z = 2.',
        'presentation': [   'State augmented matrix.',
                            'Show both downward and upward elimination steps.',
                            'State final [I | X] form.',
                            'Write x = 1, y = 3, z = 5 clearly.'],
        'question': 'Solve the system using Gauss-Jordan elimination method:<br>x + y + z = 9,<br>2x - 3y + 4z = '
                    '13,<br>3x + 4y + 5z = 40.',
        'steps': [   (   'Step 1: Set up Augmented Matrix',
                         '[A|B] = [ [1, 1, 1 | 9], [2, -3, 4 | 13], [3, 4, 5 | 40] ]. Pivot is a₁₁ = 1.',
                         'Execute step 1: set up augmented matrix to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Eliminate column 1 entries below pivot',
                         'R₂ → R₂ - 2R₁: [0, -5, 2 | -5].<br>R₃ → R₃ - 3R₁: [0, 1, 2 | 13].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: Swap R₂ ↔ R₃ to get pivot 1 in row 2',
                         '[ [1, 1, 1 | 9], [0, 1, 2 | 13], [0, -5, 2 | -5] ].',
                         'Execute step 3: swap r₂ ↔ r₃ to get pivot 1 in row 2 to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Eliminate column 2 entries above and below pivot',
                         'R₁ → R₁ - R₂:<br>[1 - 0, 1 - 1, 1 - 2 | 9 - 13] = [1, 0, -1 | -4].<br>R₃ → R₃ + 5R₂:<br>[0, '
                         '-5 + 5, 2 + 10 | -5 + 65] = [0, 0, 12 | 60]  ⇒  divide by 12: [0, 0, 1 | 5].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 5: Eliminate column 3 entries above pivot a₃₃ = 1',
                         'R₁ → R₁ + R₃:<br>[1, 0, -1 + 1 | -4 + 5] = [1, 0, 0 | 1].<br>R₂ → R₂ - 2R₃:<br>[0, 1, 2 - '
                         '2(1) | 13 - 2(5)] = [0, 1, 0 | 3].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 6: Read off solution from identity matrix',
                         '[ [1, 0, 0 | 1], [0, 1, 0 | 3], [0, 0, 1 | 5] ].<br>Therefore: x = 1, y = 3, z = 5.',
                         'Execute step 6: read off solution from identity matrix to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Solving Linear System by Gauss-Jordan Method'},
    {   'concept': 'For each eigenvalue λ, the eigenvector is found by solving the homogeneous system (A - λI) v = 0. '
                   'For real symmetric matrices, eigenvectors corresponding to distinct eigenvalues are always '
                   'orthogonal.',
        'difficulty': 'Intermediate',
        'final_answer': 'Eigenvalues: λ₁ = 1, λ₂ = 5;  Eigenvectors: v₁ = [1, -1]ᵀ,  v₂ = [1, 1]ᵀ',
        'formula': '|A - λI| = 0;  (A - λI) v = 0.',
        'formula_expl': 'v = [x, y]ᵀ is a non-zero vector spanning the null space of (A - λI).',
        'given': 'A = [[3, 2], [2, 3]].',
        'meaning_en': 'Determine the scalar eigenvalues λ and the corresponding non-zero direction vectors v '
                      'satisfying A v = λ v.',
        'mistakes': [   ('Setting v = [0, 0]ᵀ.', 'An eigenvector must be NON-ZERO by definition!'),
                        (   'Writing v₁ = [1, 1]ᵀ for λ = 1.',
                            'Check: 2(1) + 2(1) = 4 ≠ 0. The correct relation is y = -x, so v₁ = [1, -1]ᵀ.')],
        'num': 59,
        'practice_q': 'Find eigenvalues and eigenvectors of A = [[4, 2], [2, 1]].',
        'presentation': [   'Find characteristic equation and roots λ = 1, 5.',
                            'Set up (A - λI)v = 0 for each eigenvalue.',
                            'Solve for x and y and state eigenvectors.',
                            'Note orthogonality.'],
        'question': 'Find the eigenvalues and eigenvectors of the symmetric matrix A = [[3, 2], [2, 3]].',
        'steps': [   (   'Step 1: Characteristic equation',
                         'Trace(A) = 3 + 3 = 6.<br>det(A) = (3)(3) - (2)(2) = 9 - 4 = 5.<br>λ² - 6λ + 5 = 0  ⇒  (λ - '
                         '1)(λ - 5) = 0.<br>Eigenvalues: λ₁ = 1,  λ₂ = 5.',
                         'Set up the characteristic determinant det(A - λI) = 0 and expand to obtain the '
                         'characteristic polynomial.'),
                     (   'Step 2: Eigenvector for λ₁ = 1',
                         '(A - 1·I) v₁ = 0  ⇒  [ [3-1, 2], [2, 3-1] ] [x, y]ᵀ = [0, 0]ᵀ<br>[ [2, 2], [2, 2] ] [x, y]ᵀ '
                         '= [0, 0]ᵀ  ⇒  2x + 2y = 0  ⇒  x + y = 0  ⇒  y = -x.<br>Let x = 1  ⇒  y = -1.<br>Eigenvector '
                         'v₁ = [1, -1]ᵀ.',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.'),
                     (   'Step 3: Eigenvector for λ₂ = 5',
                         '(A - 5·I) v₂ = 0  ⇒  [ [3-5, 2], [2, 3-5] ] [x, y]ᵀ = [0, 0]ᵀ<br>[ [-2, 2], [2, -2] ] [x, '
                         'y]ᵀ = [0, 0]ᵀ  ⇒  -2x + 2y = 0  ⇒  x = y.<br>Let x = 1  ⇒  y = 1.<br>Eigenvector v₂ = [1, '
                         '1]ᵀ.',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.'),
                     (   'Step 4: Check Orthogonality of Eigenvectors',
                         'v₁ · v₂ = (1)(1) + (-1)(1) = 1 - 1 = 0.<br>The eigenvectors are mutually orthogonal, '
                         'confirming the symmetric matrix theorem!',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.')],
        'title': 'Eigenvalues and Eigenvectors of a 2×2 Symmetric Matrix'},
    {   'concept': 'Cayley-Hamilton Theorem states that every square matrix satisfies its own characteristic equation: '
                   'p(A) = 0. Multiplying p(A) = 0 by A⁻¹ provides an expression for A⁻¹ in powers of A without '
                   'computing adjugate matrices.',
        'difficulty': 'Intermediate',
        'final_answer': 'Cayley-Hamilton Verified: A² - 5A - 2I = O;  A⁻¹ = [[-2, 1], [3/2, -1/2]]',
        'formula': 'A² - (Trace A) A + det(A) I = 0  ⇒  A⁻¹ = (1/det A) [ (Trace A) I - A ].',
        'formula_expl': 'Trace(A) = 1 + 4 = 5; det(A) = (1)(4) - (2)(3) = 4 - 6 = -2.',
        'given': 'A = [[1, 2], [3, 4]].',
        'meaning_en': 'Verify that matrix A satisfies its own characteristic equation A² - (Trace)A + det(A)I = 0, and '
                      'multiply by A⁻¹ to compute the inverse matrix.',
        'mistakes': [   (   "Using adj(A)/|A| to find A⁻¹ when question says 'HENCE find A⁻¹'.",
                            "When the problem specifies 'hence', you MUST use the Cayley-Hamilton equation; direct "
                            'formula loses marks!'),
                        (   'Writing 2 instead of 2I in matrix equation.',
                            'Scalars must be multiplied by identity matrix I in matrix expressions.')],
        'num': 60,
        'practice_q': 'Verify Cayley-Hamilton theorem for A = [[2, 1], [3, 5]] and find A⁻¹.',
        'presentation': [   'State characteristic equation.',
                            'Compute A² by matrix multiplication.',
                            'Show term-by-term subtraction to get zero matrix O.',
                            'Multiply by A⁻¹ to isolate A⁻¹.'],
        'question': 'Verify Cayley-Hamilton theorem for the matrix A = [[1, 2], [3, 4]] and hence find A⁻¹.',
        'steps': [   (   'Step 1: Characteristic equation of A',
                         'Trace(A) = 5,  det(A) = -2.<br>Characteristic equation: λ² - 5λ - 2 = 0.<br>Cayley-Hamilton '
                         'theorem claims: A² - 5A - 2I = 0.',
                         'Set up the characteristic determinant det(A - λI) = 0 and expand to obtain the '
                         'characteristic polynomial.'),
                     (   'Step 2: Compute A²',
                         'A² = [ [1, 2], [3, 4] ] [ [1, 2], [3, 4] ]<br>= [ [1(1)+2(3), 1(2)+2(4)], [3(1)+4(3), '
                         '3(2)+4(4)] ]<br>= [ [1+6, 2+8], [3+12, 6+16] ] = [ [7, 10], [15, 22] ].',
                         'Execute step 2: compute a² to advance the step-by-step mathematical solution toward the '
                         'final result.'),
                     (   'Step 3: Compute A² - 5A - 2I and verify zero matrix',
                         'A² - 5A - 2I = [ [7, 10], [15, 22] ] - 5 [ [1, 2], [3, 4] ] - 2 [ [1, 0], [0, 1] ]<br>= [ [7 '
                         '- 5 - 2, 10 - 10 - 0], [15 - 15 - 0, 22 - 20 - 2] ]<br>= [ [0, 0], [0, 0] ] = O.<br>Hence '
                         'Cayley-Hamilton theorem is verified!',
                         'Execute step 3: compute a² - 5a - 2i and verify zero matrix to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Find A⁻¹ using the verified matrix equation',
                         'A² - 5A - 2I = 0.<br>Multiply both sides by A⁻¹:<br>A - 5I - 2A⁻¹ = 0  ⇒  2A⁻¹ = A - 5I  ⇒  '
                         'A⁻¹ = (1/2)(A - 5I).<br>A - 5I = [ [1-5, 2-0], [3-0, 4-5] ] = [ [-4, 2], [3, -1] '
                         '].<br>Therefore: A⁻¹ = (1/2) [ [-4, 2], [3, -1] ] = [ [-2, 1], [3/2, -1/2] ].',
                         'Execute step 4: find a⁻¹ using the verified matrix equation to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Verification of Cayley-Hamilton Theorem and Finding Inverse Matrix'},
    {   'concept': 'If ρ(A) = ρ([A|B]) = 2 < 3 (number of unknowns), the system is consistent with infinitely many '
                   'solutions dependent on 3 - 2 = 1 parameter.',
        'difficulty': 'Intermediate',
        'final_answer': 'Consistent with infinitely many solutions: x = (5 - 3k)/7,  y = (5k + 8)/7,  z = k, where k '
                        'is any real number.',
        'formula': 'ρ(A) = ρ([A|B]) = r < n  ⇒  infinitely many solutions.',
        'formula_expl': 'Set z = k and back-substitute.',
        'given': 'System of 3 equations in x, y, z.',
        'meaning_en': 'Use rank criteria on augmented matrix [A|B] to test consistency and express the infinite '
                      'solution set using a free parameter k.',
        'mistakes': [   (   'Concluding no solution because a row became all zeros.',
                            'A row of all zeros [0, 0, 0 | 0] means CONSISTENT with infinite solutions! [0, 0, 0 | '
                            'non-zero] means no solution.'),
                        ('Algebra error in (21 - 16)/7 = 5/7.', 'Double check fraction addition.')],
        'num': 61,
        'practice_q': 'Test for consistency: x + y + z = 4, 2x + 5y - 2z = 3, x + 7y - 7z = 5.',
        'presentation': [   'State both ranks ρ(A) = 2 and ρ([A|B]) = 2.',
                            'Quote Rouché-Capelli consistency condition.',
                            'Assign z = k and show algebraic back-substitution.'],
        'question': 'Test for consistency and solve if consistent:<br>x + 2y - z = 3,<br>3x - y + 2z = 1,<br>2x - 3y + '
                    '3z = -2.',
        'steps': [   (   'Step 1: Set up Augmented Matrix',
                         '[A|B] = [ [1, 2, -1 | 3], [3, -1, 2 | 1], [2, -3, 3 | -2] ].',
                         'Execute step 1: set up augmented matrix to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Eliminate x from rows 2 and 3',
                         'R₂ → R₂ - 3R₁: [0, -7, 5 | -8].<br>R₃ → R₃ - 2R₁: [0, -7, 5 | -8].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: Eliminate row 3',
                         'R₃ → R₃ - R₂: [0, 0, 0 | 0].<br>Matrix in row-echelon form:<br>[ [1, 2, -1 | 3], [0, -7, 5 | '
                         '-8], [0, 0, 0 | 0] ].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 4: Analyze ranks and consistency',
                         'ρ(A) = 2,   ρ([A|B]) = 2.<br>Since ρ(A) = ρ([A|B]) = 2 < n = 3, the system is CONSISTENT and '
                         'has INFINITELY MANY SOLUTIONS with (3 - 2) = 1 free parameter.',
                         'Compare the rank of the coefficient matrix ρ(A) with the augmented matrix ρ([A|B]) using the '
                         'Rouché-Capelli criteria.'),
                     (   'Step 5: Solve in terms of parameter k',
                         'Let z = k.<br>From Row 2: -7y + 5z = -8  ⇒  7y = 5k + 8  ⇒  y = (5k + 8) / 7.<br>From Row 1: '
                         'x = 3 - 2y + z = 3 - 2(5k+8)/7 + k = [21 - 10k - 16 + 7k] / 7 = (5 - 3k) / 7.',
                         'Execute step 5: solve in terms of parameter k to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Consistency and Infinite Solutions with Free Parameter'},
    {   'concept': 'A linear system has no solution if and only if the rank of the augmented matrix is strictly '
                   'greater than the rank of the coefficient matrix: ρ(A) < ρ([A|B]).',
        'difficulty': 'Intermediate',
        'final_answer': 'ρ(A) = 2 ≠ ρ([A|B]) = 3;  The system is INCONSISTENT and has NO SOLUTION.',
        'formula': 'ρ(A) ≠ ρ([A|B])  ⇒  Inconsistent.',
        'formula_expl': 'Produces an impossible row 0x + 0y + 0z = c (where c ≠ 0).',
        'given': 'x + 2y - 3z = -2, 3x - y - 2z = 1, 2x + 3y - 5z = 3.',
        'meaning_en': 'Reduce [A|B] to row-echelon form and show that ρ(A) ≠ ρ([A|B]), which proves the system is '
                      'inconsistent.',
        'mistakes': [   (   'Saying rank of [A|B] is 2.',
                            'The entry 6 makes row 3 a non-zero row in [A|B], so rank is 3!'),
                        (   'Attempting to solve for variables when inconsistent.',
                            "Once ρ(A) ≠ ρ([A|B]), stop immediately and conclude 'no solution'.")],
        'num': 62,
        'practice_q': 'Show that the system x + y + z = 1, x + 2y + 3z = 4, x + 3y + 5z = 5 is inconsistent.',
        'presentation': [   'Show echelon reduction clearly.',
                            'State ρ(A) = 2 and ρ([A|B]) = 3 explicitly.',
                            'Highlight row [0, 0, 0 | 6] and statement 0 ≠ 6.'],
        'question': 'Show that the system of equations is inconsistent and hence has no solution:<br>x + 2y - 3z = '
                    '-2,<br>3x - y - 2z = 1,<br>2x + 3y - 5z = k (where k ≠ -3, say k = 3).',
        'steps': [   (   'Step 1: Set up Augmented Matrix',
                         '[A|B] = [ [1, 2, -3 | -2], [3, -1, -2 | 1], [2, 3, -5 | 3] ].',
                         'Execute step 1: set up augmented matrix to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Row operations to eliminate column 1 below pivot',
                         'R₂ → R₂ - 3R₁: [0, -7, 7 | 7]  ⇒  divide by -7: [0, 1, -1 | -1].<br>R₃ → R₃ - 2R₁: [0, -1, 1 '
                         '| 7].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: Eliminate row 3 column 2',
                         'R₃ → R₃ + R₂:<br>[0, -1 + 1, 1 - 1 | 7 + (-1)] = [0, 0, 0 | 6].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 4: Compare ranks of A and [A|B]',
                         'Matrix in echelon form:<br>[ [1, 2, -3 | -2], [0, 1, -1 | -1], [0, 0, 0 | 6] ].<br>• In '
                         'matrix A, the 3rd row is [0, 0, 0]  ⇒  ρ(A) = 2.<br>• In augmented matrix [A|B], the 3rd row '
                         'is [0, 0, 0 | 6]  ⇒  ρ([A|B]) = 3.<br>Since ρ(A) = 2 ≠ ρ([A|B]) = 3, the system is '
                         'INCONSISTENT.',
                         'Compare the rank of the coefficient matrix ρ(A) with the augmented matrix ρ([A|B]) using the '
                         'Rouché-Capelli criteria.'),
                     (   'Step 5: Physical interpretation',
                         'The third row represents the equation 0·x + 0·y + 0·z = 6, i.e., 0 = 6, which is an '
                         'impossible contradiction. Hence, NO SOLUTION exists.',
                         'Execute step 5: physical interpretation to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Inconsistent System (No Solution)'},
    {   'concept': 'For an n×n square matrix, rank = n if and only if det(A) ≠ 0. If det(A) = 0, rank < n.',
        'difficulty': 'Intermediate',
        'final_answer': '(i) Rank = 3 when λ ≠ 10;   (ii) Rank < 3 (Rank = 2) when λ = 10',
        'formula': 'det(A) ≠ 0  ⇒  rank = 3;  det(A) = 0  ⇒  rank < 3.',
        'formula_expl': 'Row operations can also be used directly.',
        'given': 'A = [[1, 1, 1], [1, 2, 4], [1, 4, λ]].',
        'meaning_en': 'Evaluate the determinant of matrix A in terms of λ and determine the conditions under which '
                      'det(A) = 0 (rank < 3) and det(A) ≠ 0 (rank = 3).',
        'mistakes': [   ('Arithmetic error: (λ - 1) - 9 = λ - 10.', 'Be careful: -1 - 9 = -10, NOT -8!'),
                        (   'Claiming rank becomes 1 when λ = 10.',
                            'Rows 1 and 2 are linearly independent, so rank is 2, not 1.')],
        'num': 63,
        'practice_q': 'Find the value of k for which the matrix [[1, 2, 3], [2, k, 7], [3, 6, 10]] has rank 2.',
        'presentation': [   'Show row operations leading to [0, 0, λ - 10].',
                            'State clearly: pivot non-zero ⇒ rank 3.',
                            'State clearly: pivot zero ⇒ rank 2.'],
        'question': 'Find the values of λ for which the matrix A = [[1, 1, 1], [1, 2, 4], [1, 4, λ]] has rank (i) 3, '
                    '(ii) less than 3.',
        'steps': [   (   'Step 1: Reduce A using elementary row operations',
                         'A = [ [1, 1, 1], [1, 2, 4], [1, 4, λ] ].<br>R₂ → R₂ - R₁: [0, 1, 3].<br>R₃ → R₃ - R₁: [0, 3, '
                         'λ - 1].',
                         'Execute step 1: reduce a using elementary row operations to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Eliminate column 2 in row 3',
                         'R₃ → R₃ - 3R₂:<br>[0, 3 - 3(1), (λ - 1) - 3(3)] = [0, 0, λ - 10].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: State the echelon matrix',
                         'A ~ [ [1, 1, 1], [0, 1, 3], [0, 0, λ - 10] ].',
                         'Execute step 3: state the echelon matrix to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 4: Case (i): Rank = 3',
                         'For rank to be 3, all 3 rows must be non-zero.<br>This requires the pivot λ - 10 ≠ 0  ⇒  λ ≠ '
                         '10.',
                         'Execute step 4: case (i): rank = 3 to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 5: Case (ii): Rank < 3',
                         'If λ - 10 = 0, i.e., λ = 10, the 3rd row becomes [0, 0, 0].<br>Then there are only 2 '
                         'non-zero rows, so Rank ρ(A) = 2 < 3.',
                         'Execute step 5: case (ii): rank < 3 to advance the step-by-step mathematical solution toward '
                         'the final result.')],
        'title': 'Rank of Matrix Containing an Unknown Parameter λ'},
    {   'concept': 'Eigenvalue equations det(A - λI) = 0 and A v = λ v translate matrix algebraic properties into '
                   'scalar polynomial equations in λ.',
        'difficulty': 'Intermediate',
        'final_answer': '(i) Eigenvalues of triangular matrix are its diagonal entries;  (ii) Eigenvalues of '
                        'idempotent matrix A² = A are strictly 0 or 1. (Both proved)',
        'formula': '(i) det(T - λI) = (t₁₁ - λ)(t₂₂ - λ)...(t_nn - λ) = 0.<br>(ii) A v = λ v  ⇒  A² v = λ² v; but A² = '
                   'A  ⇒  λ² = λ.',
        'formula_expl': 'λ² - λ = 0 has only two roots: 0 and 1.',
        'given': '(i) Upper triangular matrix T; (ii) Idempotent matrix A satisfying A² = A.',
        'meaning_en': 'Prove two fundamental theoretical properties regarding eigenvalues of structured matrices.',
        'mistakes': [   (   'Dividing by vector v directly like (λ² - λ) = 0/v.',
                            "You cannot divide by a vector! State 'Since v is a non-zero vector, the scalar "
                            "coefficient (λ² - λ) must be 0'."),
                        ('Forgetting λ = 0 as a valid eigenvalue.', '0 is a completely valid eigenvalue.')],
        'num': 64,
        'practice_q': 'Prove that the eigenvalues of an orthogonal matrix (Aᵀ A = I) have absolute value |λ| = 1.',
        'presentation': [   'Present each proof with a clear heading.',
                            'State determinant of triangular matrix property.',
                            'State v ≠ 0 to divide by v in λ² - λ = 0.'],
        'question': 'Prove that: (i) The eigenvalues of a triangular matrix are its diagonal entries, and (ii) The '
                    'eigenvalues of an idempotent matrix (A² = A) are either 0 or 1.',
        'steps': [   (   'Step 1: Proof for Triangular Matrix',
                         'Let T be an upper triangular matrix with diagonal entries d₁, d₂, ..., d_n.<br>Then (T - λI) '
                         'is also an upper triangular matrix with diagonal entries (d₁ - λ), (d₂ - λ), ..., (d_n - '
                         'λ).<br>The determinant of any triangular matrix is simply the product of its diagonal '
                         'entries:<br>det(T - λI) = (d₁ - λ)(d₂ - λ)...(d_n - λ) = 0.<br>The roots of this equation '
                         'are precisely λ = d₁, d₂, ..., d_n.<br>Hence, the eigenvalues are the diagonal entries. '
                         'Proved!',
                         'Execute step 1: proof for triangular matrix to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Proof for Idempotent Matrix (A² = A)',
                         'Let λ be an eigenvalue of A with corresponding non-zero eigenvector v:<br>A v = λ v  --- '
                         '(1).<br>Multiply both sides on the left by A:<br>A(A v) = A(λ v)  ⇒  A² v = λ (A '
                         'v).<br>Substitute (1) into the RHS:<br>A² v = λ (λ v) = λ² v  --- (2).',
                         'Execute step 2: proof for idempotent matrix (a² = a) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Equate using A² = A',
                         'Since A is idempotent, A² = A.<br>Therefore, the LHS of (2) is A² v = A v = λ v.<br>Equating '
                         'with RHS of (2):<br>λ v = λ² v  ⇒  (λ² - λ) v = 0.<br>Since v is an eigenvector, v ≠ 0. '
                         'Therefore:<br>λ² - λ = 0  ⇒  λ(λ - 1) = 0  ⇒  λ = 0  or  λ = 1. Proved!',
                         'Execute step 3: equate using a² = a to advance the step-by-step mathematical solution toward '
                         'the final result.')],
        'title': 'Eigenvalues of Special Matrices: Triangular, Orthogonal and Idempotent'},
    {   'concept': 'A matrix with distinct eigenvalues is diagonalizable: P⁻¹ A P = D = diag(λ₁, λ₂). The columns of P '
                   'are the eigenvectors.',
        'difficulty': 'Intermediate',
        'final_answer': 'Modal Matrix P = [[1, -2], [1, 1]];  Diagonal Matrix D = P⁻¹AP = [[5, 0], [0, -1]]',
        'formula': 'D = P⁻¹ A P where P = [v₁ | v₂] and D = [[λ₁, 0], [0, λ₂]].',
        'formula_expl': 'P is called the modal matrix; D is the spectral diagonal matrix.',
        'given': 'A = [[1, 4], [2, 3]].',
        'meaning_en': 'Find eigenvalues, form modal matrix P from eigenvectors, compute P⁻¹, and verify that P⁻¹AP is '
                      'the diagonal matrix D of eigenvalues.',
        'mistakes': [   (   'Ordering mismatch between P and D.',
                            'If column 1 of P is v₁ (for λ = 5), then D₁₁ MUST be 5!'),
                        ('Determinant error in P⁻¹.', 'det(P) = 1 - (-2) = 3.')],
        'num': 65,
        'practice_q': 'Diagonalize A = [[3, 1], [1, 3]].',
        'presentation': [   'Find eigenvalues λ = 5, -1.',
                            'Find eigenvectors v₁, v₂.',
                            'Write P = [v₁ | v₂] and P⁻¹.',
                            'Multiply P⁻¹AP step by step to produce D.'],
        'question': 'Diagonalize the matrix A = [[1, 4], [2, 3]] by finding the modal matrix P and computing P⁻¹AP.',
        'steps': [   (   'Step 1: Find eigenvalues of A',
                         'Trace(A) = 1 + 3 = 4,   det(A) = (1)(3) - (4)(2) = 3 - 8 = -5.<br>λ² - 4λ - 5 = 0  ⇒  (λ - '
                         '5)(λ + 1) = 0.<br>Eigenvalues: λ₁ = 5,   λ₂ = -1.',
                         'Execute step 1: find eigenvalues of a to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Find eigenvector v₁ for λ₁ = 5',
                         '(A - 5I) v₁ = 0  ⇒  [ [-4, 4], [2, -2] ] [x, y]ᵀ = [0, 0]ᵀ  ⇒  -4x + 4y = 0  ⇒  x = '
                         'y.<br>Let y = 1  ⇒  x = 1.  v₁ = [1, 1]ᵀ.',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.'),
                     (   'Step 3: Find eigenvector v₂ for λ₂ = -1',
                         '(A + I) v₂ = 0  ⇒  [ [2, 4], [2, 4] ] [x, y]ᵀ = [0, 0]ᵀ  ⇒  2x + 4y = 0  ⇒  x = -2y.<br>Let '
                         'y = 1  ⇒  x = -2.  v₂ = [-2, 1]ᵀ.',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.'),
                     (   'Step 4: Construct modal matrix P and compute P⁻¹',
                         'P = [ v₁ | v₂ ] = [ [1, -2], [1, 1] ].<br>det(P) = (1)(1) - (-2)(1) = 1 + 2 = 3.<br>P⁻¹ = '
                         '(1/3) [ [1, 2], [-1, 1] ].',
                         'Execute step 4: construct modal matrix p and compute p⁻¹ to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: Compute AP and P⁻¹(AP)',
                         'AP = [ [1, 4], [2, 3] ] [ [1, -2], [1, 1] ] = [ [5, 2], [5, -1] ].<br>P⁻¹ AP = (1/3) [ [1, '
                         '2], [-1, 1] ] [ [5, 2], [5, -1] ]<br>= (1/3) [ [5+10, 2-2], [-5+5, -2-1] ] = (1/3) [ [15, '
                         '0], [0, -3] ] = [ [5, 0], [0, -1] ] = D.<br>Matches eigenvalues 5 and -1! Successfully '
                         'diagonalized.',
                         'Execute step 5: compute ap and p⁻¹(ap) to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Diagonalization of a 2×2 Matrix'},
    {   'concept': 'Classic VTU exam question appearing in nearly every examination. The pivot in the last row (λ - 3) '
                   'and constant (μ - 10) control the rank of A and [A|B].',
        'difficulty': 'Exam-Level',
        'final_answer': '(i) No Solution: λ = 3 and μ ≠ 10;  (ii) Unique Solution: λ ≠ 3, μ ∈ ℝ;  (iii) Infinitely '
                        'Many Solutions: λ = 3 and μ = 10',
        'formula': '[A|B] ~ echelon form; compare ρ(A) and ρ([A|B]).',
        'formula_expl': 'Row 3 becomes [0, 0, λ - 3 | μ - 10].',
        'given': 'System with parameters λ and μ.',
        'meaning_en': 'Determine the conditions on parameters λ and μ by row reduction of [A|B] to classify the system '
                      'into the three Rouché-Capelli solution cases.',
        'mistakes': [   (   'Saying unique solution requires μ ≠ 10.',
                            'For a unique solution, μ can be ANYTHING! Only λ ≠ 3 is required.'),
                        ('Writing λ = 3, μ = 10 for no solution.', 'That is the condition for INFINITE solutions.')],
        'num': 66,
        'practice_q': 'Investigate for what values of a and b the system x + y + z = 2, x + 2y + 3z = 5, x + 3y + az = '
                      'b has unique, no, and infinite solutions.',
        'presentation': [   'Show the row reduction clearly to [0, 0, λ - 3 | μ - 10].',
                            'State the 3 cases with separate headings.',
                            'Quote rank values ρ(A) and ρ([A|B]) in every case.'],
        'question': 'Investigate the values of λ and μ for which the system of equations:<br>x + y + z = 6,<br>x + 2y '
                    '+ 3z = 10,<br>x + 2y + λz = μ<br>has (i) no solution, (ii) a unique solution, and (iii) '
                    'infinitely many solutions.',
        'steps': [   (   'Step 1: Write the Augmented Matrix [A|B]',
                         '[A|B] = [ [1, 1, 1 | 6], [1, 2, 3 | 10], [1, 2, λ | μ] ].',
                         'Execute step 1: write the augmented matrix [a|b] to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Eliminate x from rows 2 and 3',
                         'R₂ → R₂ - R₁: [0, 1, 2 | 4].<br>R₃ → R₃ - R₁: [0, 1, λ - 1 | μ - 6].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: Eliminate y from row 3',
                         'R₃ → R₃ - R₂:<br>[0, 1 - 1, (λ - 1) - 2 | (μ - 6) - 4] = [0, 0, λ - 3 | μ - 10].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 4: State the reduced echelon form',
                         '[A|B] ~ [ [1, 1, 1 | 6], [0, 1, 2 | 4], [0, 0, λ - 3 | μ - 10] ].',
                         'Execute step 4: state the reduced echelon form to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 5: Case (i): No Solution (Inconsistent)',
                         'For no solution: ρ(A) ≠ ρ([A|B]).<br>This happens when λ - 3 = 0 and μ - 10 ≠ '
                         '0.<br>Therefore: λ = 3 and μ ≠ 10.<br>Then ρ(A) = 2 while ρ([A|B]) = 3. System is '
                         'inconsistent.',
                         'Execute step 5: case (i): no solution (inconsistent) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 6: Case (ii): Unique Solution',
                         'For unique solution: ρ(A) = ρ([A|B]) = 3 (number of unknowns).<br>This happens when the '
                         'pivot λ - 3 ≠ 0, regardless of μ.<br>Therefore: λ ≠ 3 and μ can have ANY real value.',
                         'Execute step 6: case (ii): unique solution to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 7: Case (iii): Infinitely Many Solutions',
                         'For infinite solutions: ρ(A) = ρ([A|B]) = 2 < 3.<br>This requires the entire last row to '
                         'become all zeros: [0, 0, 0 | 0].<br>Therefore: λ - 3 = 0 and μ - 10 = 0  ⇒  λ = 3 and μ = '
                         '10.',
                         'Execute step 7: case (iii): infinitely many solutions to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Investigation of System Consistency for Parameters λ and μ'},
    {   'concept': 'Symmetric 3×3 matrix with repeated eigenvalues. For a repeated eigenvalue of multiplicity m, we '
                   'must find m linearly independent eigenvectors.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Eigenvalues: λ = 4, 1, 1;  Eigenvectors: for λ = 4: v₁ = [1, -1, 1]ᵀ;  for λ = 1: v₂ = [1, 1, '
                        '0]ᵀ and v₃ = [0, 1, 1]ᵀ',
        'formula': 'det(A - λI) = -λ³ + (Tr A)λ² - (M₁₁ + M₂₂ + M₃₃)λ + det(A) = 0.',
        'formula_expl': 'Tr(A) = 2+2+2 = 6; M₁₁+M₂₂+M₃₃ = sum of principal minors = 3+3+3 = 9; det(A) = 4.',
        'given': 'A = [[2, -1, 1], [-1, 2, -1], [1, -1, 2]].',
        'meaning_en': 'Expand the 3×3 characteristic equation, find the three eigenvalues, and solve (A - λI)v = 0 for '
                      'each eigenvalue to find the corresponding eigenvectors.',
        'mistakes': [   (   'Giving only one eigenvector for the repeated eigenvalue λ = 1.',
                            'λ = 1 has algebraic multiplicity 2; since rank(A-I) = 1, geometric multiplicity is 3 - 1 '
                            '= 2, so you MUST find TWO independent eigenvectors!'),
                        ('Arithmetic error in cross-multiplication signs.', 'Check: (-1)(-1) - (1)(-2) = 1 + 2 = 3.')],
        'num': 67,
        'practice_q': 'Find eigenvalues and eigenvectors of A = [[1, 1, 3], [1, 5, 1], [3, 1, 1]].',
        'presentation': [   'Compute s₁, s₂, s₃ clearly.',
                            'Show synthetic division for cubic equation.',
                            'Show cross-multiplication for λ = 4.',
                            'Show nullity = 2 for λ = 1 and give two independent vectors.'],
        'question': 'Find all eigenvalues and eigenvectors of the matrix A = [[2, -1, 1], [-1, 2, -1], [1, -1, 2]].',
        'steps': [   (   'Step 1: Characteristic Equation using coefficients',
                         '• s₁ = Trace(A) = 2 + 2 + 2 = 6.<br>• s₂ = M₁₁ + M₂₂ + M₃₃ = |2 -1; -1 2| + |2 1; 1 2| + |2 '
                         '-1; -1 2| = (4 - 1) + (4 - 1) + (4 - 1) = 3 + 3 + 3 = 9.<br>• s₃ = det(A) = 2(4 - 1) - '
                         '(-1)(-2 + 1) + 1(1 - 2) = 2(3) + 1(-1) + 1(-1) = 6 - 1 - 1 = 4.<br>Characteristic equation: '
                         'λ³ - s₁λ² + s₂λ - s₃ = 0  ⇒  λ³ - 6λ² + 9λ - 4 = 0.',
                         'Set up the characteristic determinant det(A - λI) = 0 and expand to obtain the '
                         'characteristic polynomial.'),
                     (   'Step 2: Solve the cubic polynomial for eigenvalues',
                         'By inspection, test λ = 1: 1³ - 6(1)² + 9(1) - 4 = 1 - 6 + 9 - 4 = 0. So λ = 1 is a '
                         'root.<br>Synthetic division by (λ - 1):<br>(λ - 1)(λ² - 5λ + 4) = 0  ⇒  (λ - 1)(λ - 1)(λ - '
                         '4) = 0.<br>Eigenvalues: λ₁ = 4,   λ₂ = 1,   λ₃ = 1 (repeated eigenvalue).',
                         'Find the roots of the characteristic polynomial to determine all scalar eigenvalues.'),
                     (   'Step 3: Eigenvector for λ = 4',
                         '(A - 4I) v = 0  ⇒  [ [-2, -1, 1], [-1, -2, -1], [1, -1, -2] ] [x, y, z]ᵀ = 0.<br>Taking '
                         'first two equations:<br>-2x - y + z = 0<br>-x - 2y - z = 0.<br>Using cross-multiplication '
                         'rule:<br>x / [ (-1)(-1) - (1)(-2) ] = y / [ (1)(-1) - (-2)(-1) ] = z / [ (-2)(-2) - (-1)(-1) '
                         ']<br>x / [ 1 + 2 ] = y / [ -1 - 2 ] = z / [ 4 - 1 ]<br>x / 3 = y / (-3) = z / 3  ⇒  x / 1 = '
                         'y / (-1) = z / 1.<br>Eigenvector v₁ = [1, -1, 1]ᵀ.',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.'),
                     (   'Step 4: Eigenvectors for repeated eigenvalue λ = 1',
                         '(A - I) v = 0  ⇒  [ [1, -1, 1], [-1, 1, -1], [1, -1, 1] ] [x, y, z]ᵀ = 0.<br>All three rows '
                         'are scalar multiples of a single equation: x - y + z = 0  ⇒  y = x + z.<br>Since rank = 1, '
                         'nullity = 3 - 1 = 2 (two linearly independent eigenvectors!):<br>• Choice 1: Let z = 0, x = '
                         '1  ⇒  y = 1 + 0 = 1.  v₂ = [1, 1, 0]ᵀ.<br>• Choice 2: Let x = 0, z = 1  ⇒  y = 0 + 1 = 1.  '
                         'v₃ = [0, 1, 1]ᵀ.',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.'),
                     (   'Step 5: Orthogonalize eigenvectors if needed',
                         'Notice v₁ · v₂ = 1(1) + (-1)(1) + 1(0) = 0. Orthogonal!<br>v₁ · v₃ = 1(0) + (-1)(1) + 1(1) = '
                         '0. Orthogonal!',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.')],
        'title': 'Complete Eigenvalues and Eigenvectors of a 3×3 Matrix'},
    {   'concept': 'Every real symmetric matrix can be orthogonally diagonalized: Pᵀ A P = D, where P is an orthogonal '
                   'matrix whose columns are normalized eigenvectors.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Orthogonal Matrix P = [[1/√3, 1/√2, 1/√6], [-1/√3, 1/√2, -1/√6], [1/√3, 0, -2/√6]];  Diagonal '
                        'Matrix D = [[5, 0, 0], [0, 2, 0], [0, 0, 2]]',
        'formula': 'Pᵀ A P = D;  P = [u₁ | u₂ | u₃] where u_i = v_i / |v_i|.',
        'formula_expl': 'For an orthogonal matrix, P⁻¹ = Pᵀ, avoiding matrix inversion.',
        'given': 'A = [[3, -1, 1], [-1, 3, -1], [1, -1, 3]].',
        'meaning_en': 'Find eigenvalues and mutually orthogonal normalized eigenvectors, construct orthogonal matrix P '
                      '(where Pᵀ = P⁻¹), and compute PᵀAP = D.',
        'mistakes': [   (   'Not making the two eigenvectors for λ = 2 orthogonal to each other.',
                            'For orthogonal diagonalization, ALL columns of P must be mutually orthogonal!'),
                        (   'Using P⁻¹ instead of Pᵀ.',
                            'For an orthogonal matrix, P⁻¹ = Pᵀ, which is much easier to write.')],
        'num': 68,
        'practice_q': 'Orthogonally diagonalize A = [[2, 2], [2, 5]].',
        'presentation': [   'State eigenvalues λ = 5, 2, 2.',
                            'Normalize each eigenvector.',
                            'Ensure eigenvectors for λ = 2 are mutually orthogonal.',
                            'State P and D.'],
        'question': 'Diagonalize the symmetric matrix A = [[3, -1, 1], [-1, 3, -1], [1, -1, 3]] by orthogonal '
                    'transformation.',
        'steps': [   (   'Step 1: Compute eigenvalues of A',
                         '• s₁ = Trace = 3 + 3 + 3 = 9.<br>• s₂ = 3(9 - 1) = 3(8) = 24.<br>• s₃ = det(A) = 3(8) - '
                         '(-1)(-3 + 1) + 1(1 - 3) = 24 - 2 - 2 = 20.<br>λ³ - 9λ² + 24λ - 20 = 0  ⇒  (λ - 5)(λ - 2)² = '
                         '0.<br>Eigenvalues: λ₁ = 5,   λ₂ = 2,   λ₃ = 2.',
                         'Execute step 1: compute eigenvalues of a to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Eigenvector for λ = 5',
                         '(A - 5I) v = 0  ⇒  [ [-2, -1, 1], [-1, -2, -1], [1, -1, -2] ] v = 0.<br>As in Q67, '
                         'cross-multiplication gives: v₁ = [1, -1, 1]ᵀ.<br>Normalized unit eigenvector: u₁ = (1/√3) '
                         '[1, -1, 1]ᵀ.',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.'),
                     (   'Step 3: Two orthogonal eigenvectors for λ = 2',
                         '(A - 2I) v = 0  ⇒  [ [1, -1, 1], [-1, 1, -1], [1, -1, 1] ] v = 0  ⇒  x - y + z = '
                         '0.<br>Choose v₂ = [1, 1, 0]ᵀ.  Normalized: u₂ = (1/√2) [1, 1, 0]ᵀ.<br>Now choose v₃ = [a, b, '
                         'c]ᵀ such that:<br>1) a - b + c = 0 (satisfies plane equation)<br>2) v₃ · v₂ = 0  ⇒  a(1) + '
                         'b(1) + c(0) = a + b = 0  ⇒  b = -a.<br>Substitute b = -a into (1): a - (-a) + c = 0  ⇒  2a + '
                         'c = 0  ⇒  c = -2a.<br>Let a = 1  ⇒  b = -1, c = -2.  v₃ = [1, -1, -2]ᵀ.<br>Normalized: |v₃| '
                         '= √(1 + 1 + 4) = √6  ⇒  u₃ = (1/√6) [1, -1, -2]ᵀ.',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.'),
                     (   'Step 4: Form the Orthogonal Matrix P',
                         'P = [ [1/√3, 1/√2, 1/√6], [-1/√3, 1/√2, -1/√6], [1/√3, 0, -2/√6] ].',
                         'Execute step 4: form the orthogonal matrix p to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 5: Verify Diagonal Form D = Pᵀ A P',
                         'D = Pᵀ A P = [ [5, 0, 0], [0, 2, 0], [0, 0, 2] ]. Diagonalized!',
                         'Execute step 5: verify diagonal form d = pᵀ a p to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Diagonalization of a 3×3 Symmetric Matrix'},
    {   'concept': 'A homogeneous linear system AX = 0 has non-trivial solutions if and only if the determinant of the '
                   'coefficient matrix vanishes: det(A) = 0.',
        'difficulty': 'Exam-Level',
        'final_answer': 'k = 1/2;  Non-trivial solutions: X = t [1, -8, -5]ᵀ, where t is any non-zero real scalar.',
        'formula': 'det(A) = 0.',
        'formula_expl': 'If det(A) ≠ 0, only X = [0, 0, 0]ᵀ exists.',
        'given': 'A = [[2, -1, 2], [3, 1, -1], [4, k, 0]].',
        'meaning_en': 'Set det(A) = 0 to determine the parameter k, then find the one-parameter family of non-trivial '
                      'solutions.',
        'mistakes': [   ('Sign error in -k(-2 - 6) = +8k.', 'Carefully evaluate cofactor signs: -k(-8) = +8k.'),
                        (   'Leaving answer as k = 1/2 without finding the solutions.',
                            "The question explicitly says 'AND find the solutions'.")],
        'num': 69,
        'practice_q': 'Find k such that (1-k)x + y - z = 0, 2x - ky - 2z = 0, x - y - (1+k)z = 0 has non-trivial '
                      'solutions.',
        'presentation': [   'State condition det(A) = 0.',
                            'Show expansion along row 3.',
                            'Solve 8k = 4 ⇒ k = 1/2.',
                            'State solution vector with parameter t.'],
        'question': 'Find the values of k for which the system of homogeneous equations has non-trivial solutions, and '
                    'find the solutions:<br>2x - y + 2z = 0,<br>3x + y - z = 0,<br>4x + ky + 0z = 0 (i.e., 4x + ky = '
                    '0).',
        'steps': [   (   'Step 1: Set determinant det(A) = 0',
                         'det(A) = | 2  -1   2 |<br>         | 3   1  -1 |<br>         | 4   k   0 | = 0.',
                         'Execute step 1: set determinant det(a) = 0 to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Expand along Row 3',
                         '4 [ (-1)(-1) - (2)(1) ] - k [ 2(-1) - 2(3) ] + 0 = 0<br>4 [ 1 - 2 ] - k [ -2 - 6 ] = '
                         '0<br>4(-1) - k(-8) = 0<br>-4 + 8k = 0  ⇒  8k = 4  ⇒  k = 1/2.',
                         'Execute step 2: expand along row 3 to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 3: Substitute k = 1/2 into the system',
                         'Equations become:<br>2x - y + 2z = 0  --- (1)<br>3x + y - z = 0   --- (2)<br>4x + (1/2)y = '
                         '0  ⇒  8x + y = 0  ⇒  y = -8x  --- (3).',
                         'Execute step 3: substitute k = 1/2 into the system to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Solve for z in terms of x',
                         'From (2): z = 3x + y = 3x + (-8x) = -5x.<br>Check in (1): 2x - (-8x) + 2(-5x) = 2x + 8x - '
                         '10x = 0. Matches!',
                         'Execute step 4: solve for z in terms of x to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 5: Express solution in parametric vector form',
                         'Let x = t (where t is any arbitrary real constant):<br>x = t,   y = -8t,   z = -5t.<br>X = t '
                         '[1, -8, -5]ᵀ.',
                         'Execute step 5: express solution in parametric vector form to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Homogeneous System with Non-Trivial Solutions Depending on Parameter'},
    {   'concept': 'Fundamental theorem of linear algebra. Guarantees that quantum observables (Hermitian operators) '
                   'always yield real measurement values.',
        'difficulty': 'Exam-Level',
        'final_answer': 'All eigenvalues of a real symmetric matrix are real numbers (Hence proved)',
        'formula': 'A v = λ v  ⇒  v* A v = λ v* v; take conjugate transpose.',
        'formula_expl': 'v* is the conjugate transpose (v̄ᵀ); since A is real symmetric, A* = Aᵀ = A.',
        'given': 'A is an n×n matrix with real entries, Aᵀ = A.',
        'meaning_en': 'Use complex conjugate transpose (Hermitian transpose) to prove that no eigenvalue of a real '
                      'symmetric matrix can have a non-zero imaginary part.',
        'mistakes': [   (   'Assuming v has real entries from the start.',
                            'You CANNOT assume v is real; you must prove λ is real allowing for complex entries in v!'),
                        (   'Omitting the justification that v* v ≠ 0.',
                            'You must state v* v = Σ |v_i|² > 0 because v is non-zero.')],
        'num': 70,
        'practice_q': 'Prove that the eigenvalues of a skew-symmetric real matrix (Aᵀ = -A) are either purely '
                      'imaginary or zero.',
        'presentation': [   'Define conjugate transpose v*.',
                            'Use property A* = A for real symmetric matrix.',
                            'State v* v > 0 since v ≠ 0.',
                            'Conclude λ = λ̄.'],
        'question': 'Prove that all eigenvalues of a real symmetric matrix are strictly real numbers.',
        'steps': [   (   'Step 1: Set up the eigenvalue equation',
                         'Let λ be an eigenvalue of A with corresponding non-zero eigenvector v in ℂⁿ:<br>A v = λ v  '
                         '--- (1).',
                         'Execute step 1: set up the eigenvalue equation to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Pre-multiply by v* (conjugate transpose)',
                         'v* (A v) = v* (λ v)<br>v* A v = λ (v* v)  --- (2).',
                         'Execute step 2: pre-multiply by v* (conjugate transpose) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Take conjugate transpose of equation (2)',
                         '(v* A v)* = [ λ (v* v) ]*<br>v* A* (v*)* = λ̄ (v* v)*.<br>Since (v*)* = v, (v* v)* = v* v, '
                         'and A is real symmetric (A* = Aᵀ = A):<br>v* A v = λ̄ (v* v)  --- (3).',
                         'Execute step 3: take conjugate transpose of equation (2) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Subtract equation (3) from equation (2)',
                         'LHS - LHS = v* A v - v* A v = 0.<br>RHS - RHS = (λ - λ̄) (v* v) = 0.<br>(λ - λ̄) (v* v) = 0.',
                         'Execute step 4: subtract equation (3) from equation (2) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: Conclude λ = λ̄ (λ is real)',
                         'Since v is an eigenvector, v ≠ 0.<br>The Euclidean norm squared v* v = |v₁|² + |v₂|² + ... + '
                         '|v_n|² > 0 (strictly positive).<br>Therefore, we can divide by v* v:<br>λ - λ̄ = 0  ⇒  λ = '
                         'λ̄.<br>A complex number equals its complex conjugate if and only if its imaginary part is '
                         'zero.<br>Therefore, λ is a REAL number. Hence proved.',
                         'Execute step 5: conclude λ = λ̄ (λ is real) to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Theorem: Eigenvalues of a Real Symmetric Matrix are Real'},
    {   'concept': 'Distinct eigenspaces of a symmetric matrix are mutually perpendicular.',
        'difficulty': 'Exam-Level',
        'final_answer': 'v₁ · v₂ = 0 (Eigenvectors of distinct eigenvalues are orthogonal; Hence proved)',
        'formula': 'v₁ᵀ A v₂ = λ₂ (v₁ᵀ v₂) and (A v₁)ᵀ v₂ = λ₁ (v₁ᵀ v₂).',
        'formula_expl': 'Since (A v₁)ᵀ = v₁ᵀ Aᵀ = v₁ᵀ A, both expressions equate, forcing (λ₁ - λ₂)(v₁ · v₂) = 0.',
        'given': 'A = Aᵀ (real symmetric), A v₁ = λ₁ v₁, A v₂ = λ₂ v₂, with λ₁ ≠ λ₂.',
        'meaning_en': 'Show that if A = Aᵀ and A v₁ = λ₁ v₁, A v₂ = λ₂ v₂ with λ₁ ≠ λ₂, then v₁ · v₂ = 0.',
        'mistakes': [   (   'Forgetting to state λ₁ ≠ λ₂.',
                            'If λ₁ = λ₂, the vectors can be any linear combination and need not be orthogonal without '
                            'Gram-Schmidt.'),
                        ('Transpose error: (A v)ᵀ = Aᵀ vᵀ.', 'Correct transpose rule for products is (AB)ᵀ = Bᵀ Aᵀ!')],
        'num': 71,
        'practice_q': 'Verify this theorem for matrix A = [[1, 2], [2, 1]] using its eigenvectors.',
        'presentation': [   'State eigenvalue equations.',
                            'Show transpose step v₁ᵀ Aᵀ = v₁ᵀ A.',
                            'Equate scalars: (λ₁ - λ₂)(v₁ᵀ v₂) = 0.',
                            'Conclude v₁ · v₂ = 0 since λ₁ ≠ λ₂.'],
        'question': 'Prove that eigenvectors corresponding to distinct eigenvalues of a real symmetric matrix are '
                    'orthogonal.',
        'steps': [   (   'Step 1: Write the eigenvalue equations',
                         'A v₁ = λ₁ v₁  --- (1)<br>A v₂ = λ₂ v₂  --- (2)<br>Since A is real symmetric, all eigenvalues '
                         'and eigenvectors can be chosen real.',
                         'Execute step 1: write the eigenvalue equations to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Pre-multiply (2) by v₁ᵀ',
                         'v₁ᵀ (A v₂) = v₁ᵀ (λ₂ v₂) = λ₂ (v₁ᵀ v₂)  --- (3).',
                         'Execute step 2: pre-multiply (2) by v₁ᵀ to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 3: Take transpose of (1) and post-multiply by v₂',
                         '(A v₁)ᵀ = (λ₁ v₁)ᵀ  ⇒  v₁ᵀ Aᵀ = λ₁ v₁ᵀ.<br>Since A is symmetric, Aᵀ = A:<br>v₁ᵀ A = λ₁ '
                         'v₁ᵀ.<br>Post-multiply by v₂:<br>(v₁ᵀ A) v₂ = λ₁ (v₁ᵀ v₂)  --- (4).',
                         'Execute step 3: take transpose of (1) and post-multiply by v₂ to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Equate LHS of (3) and (4)',
                         'Notice that the LHS of (3) is v₁ᵀ A v₂, which is identical to the LHS of (4):<br>λ₁ (v₁ᵀ v₂) '
                         '= λ₂ (v₁ᵀ v₂)<br>(λ₁ - λ₂) (v₁ᵀ v₂) = 0.',
                         'Execute step 4: equate lhs of (3) and (4) to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 5: Conclude orthogonality',
                         'We are given that the eigenvalues are distinct: λ₁ ≠ λ₂  ⇒  λ₁ - λ₂ ≠ 0.<br>Dividing by (λ₁ '
                         '- λ₂) gives:<br>v₁ᵀ v₂ = 0  ⇒  v₁ · v₂ = 0.<br>Therefore, the eigenvectors v₁ and v₂ are '
                         'ORTHOGONAL. Hence proved.',
                         'Execute step 5: conclude orthogonality to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Theorem: Eigenvectors of Real Symmetric Matrix are Orthogonal'},
    {   'concept': 'Systematic 4×4 row reduction. Shows mastery of multi-step pivot operations.',
        'difficulty': 'Exam-Level',
        'final_answer': 'w = 1,   x = 1,   y = 1,   z = 1',
        'formula': "[A|B] (4×5) ~ [U|B'].",
        'formula_expl': 'Variables: (w, x, y, z).',
        'given': '4 equations in 4 variables.',
        'meaning_en': 'Reduce the 4×5 augmented matrix to upper triangular echelon form and determine w, x, y, z by '
                      'back-substitution.',
        'mistakes': [   (   'Arithmetic error in 7(4) - 5(3) = 28 - 15 = 13.',
                            'Double check arithmetic on integer combinations.'),
                        ('Dropping one equation.', 'All 4 equations must be processed.')],
        'num': 72,
        'practice_q': 'Solve by Gauss elimination: w + 2x + y = 4, 2w + x - z = 2, x + y + 2z = 4, w + y + z = 3.',
        'presentation': [   'Show 4×5 matrix clearly.',
                            'Document row swaps and elimination.',
                            'Show back-substitution clearly for each variable.',
                            'Verify in equation 2: 2(1) - 1 + 1 - 1 = 1. Matches!'],
        'question': 'Solve the system of 4 linear equations using Gauss Elimination:<br>w + x + y + z = 4,<br>2w - x + '
                    'y - z = 1,<br>w + 2x - y + z = 3,<br>3w + x + 2y - z = 5.',
        'steps': [   (   'Step 1: Set up 4×5 Augmented Matrix',
                         '[ [1, 1, 1, 1 | 4], [2, -1, 1, -1 | 1], [1, 2, -1, 1 | 3], [3, 1, 2, -1 | 5] ]. Pivot is a₁₁ '
                         '= 1.',
                         'Execute step 1: set up 4×5 augmented matrix to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Eliminate column 1 entries below pivot',
                         'R₂ → R₂ - 2R₁: [0, -3, -1, -3 | -7].<br>R₃ → R₃ - R₁: [0, 1, -2, 0 | -1].<br>R₄ → R₄ - 3R₁: '
                         '[0, -2, -1, -4 | -7].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: Swap R₂ ↔ R₃ to get pivot 1 in row 2',
                         '[ [1, 1, 1, 1 | 4], [0, 1, -2, 0 | -1], [0, -3, -1, -3 | -7], [0, -2, -1, -4 | -7] ].',
                         'Execute step 3: swap r₂ ↔ r₃ to get pivot 1 in row 2 to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Eliminate column 2 entries below pivot',
                         'R₃ → R₃ + 3R₂: [0, 0, -7, -3 | -10]  ⇒  [0, 0, 7, 3 | 10].<br>R₄ → R₄ + 2R₂: [0, 0, -5, -4 | '
                         '-9]  ⇒  [0, 0, 5, 4 | 9].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 5: Eliminate column 3 in row 4',
                         'R₄ → 7R₄ - 5R₃:<br>[0, 0, 7(5) - 5(7), 7(4) - 5(3) | 7(9) - 5(10)]<br>= [0, 0, 0, 28 - 15 | '
                         '63 - 50] = [0, 0, 0, 13 | 13]  ⇒  [0, 0, 0, 1 | 1].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 6: Back-substitution',
                         'From Row 4: z = 1.<br>From Row 3: 7y + 3z = 10  ⇒  7y + 3(1) = 10  ⇒  7y = 7  ⇒  y = '
                         '1.<br>From Row 2: x - 2y = -1  ⇒  x - 2(1) = -1  ⇒  x = 1.<br>From Row 1: w + x + y + z = 4  '
                         '⇒  w + 1 + 1 + 1 = 4  ⇒  w = 1.',
                         'Substitute known variable values upward from the bottom row equation to determine each '
                         'variable uniquely.')],
        'title': 'Gauss Elimination for a 4-Variable System'},
    {   'concept': 'Computing A¹⁰ directly requires 9 tedious matrix multiplications. Since A = P D P⁻¹, Aⁿ = (P D '
                   'P⁻¹)(P D P⁻¹)... = P Dⁿ P⁻¹. For a diagonal matrix, Dⁿ is trivially obtained by raising diagonal '
                   'entries to power n.',
        'difficulty': 'Exam-Level',
        'final_answer': 'A¹⁰ = [[1, 0], [3¹⁰ - 1, 3¹⁰]] = [[1, 0], [59048, 59049]]',
        'formula': 'Aⁿ = P Dⁿ P⁻¹, where Dⁿ = [[λ₁ⁿ, 0], [0, λ₂ⁿ]].',
        'formula_expl': 'Diagonal matrices commute with powers.',
        'given': 'A = [[1, 0], [2, 3]], n = 10.',
        'meaning_en': 'Diagonalize A = P D P⁻¹ and compute the 10th power using the matrix identity A¹⁰ = P D¹⁰ P⁻¹.',
        'mistakes': [   (   'Computing A² then A⁴ then A¹⁰ directly.',
                            'The problem requires using DIAGONALIZATION, not brute force matrix multiplication!'),
                        (   'Wrong power 3¹⁰ = 59049.',
                            'Compute powers of 3 carefully: 3²=9, 3⁴=81, 3⁸=6561, 3¹⁰=6561×9=59049.')],
        'num': 73,
        'practice_q': 'Find A⁸ where A = [[3, 4], [1, 0]] using diagonalization.',
        'presentation': [   'State Aⁿ = P Dⁿ P⁻¹ formula.',
                            'Compute eigenvalues and eigenvectors.',
                            'Form P and P⁻¹.',
                            'Show multiplication to reach final matrix.'],
        'question': 'If A = [[1, 0], [2, 3]], find A¹⁰ using the diagonalization theorem.',
        'steps': [   (   'Step 1: Find eigenvalues of lower triangular matrix A',
                         'Since A is lower triangular, its eigenvalues are simply its diagonal entries:<br>λ₁ = 1,   '
                         'λ₂ = 3.',
                         'Execute step 1: find eigenvalues of lower triangular matrix a to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Find eigenvector for λ₁ = 1',
                         '(A - I) v₁ = 0  ⇒  [ [0, 0], [2, 2] ] [x, y]ᵀ = [0, 0]ᵀ  ⇒  2x + 2y = 0  ⇒  x = -y.<br>Let y '
                         '= -1  ⇒  x = 1.  v₁ = [1, -1]ᵀ.',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.'),
                     (   'Step 3: Find eigenvector for λ₂ = 3',
                         '(A - 3I) v₂ = 0  ⇒  [ [-2, 0], [2, 0] ] [x, y]ᵀ = [0, 0]ᵀ  ⇒  -2x = 0  ⇒  x = 0.<br>y can be '
                         'any value, choose y = 1.  v₂ = [0, 1]ᵀ.',
                         'Solve the homogeneous linear system (A - λI)v = 0 to find the non-zero basis vectors '
                         'spanning the eigenspace.'),
                     (   'Step 4: Construct modal matrix P and P⁻¹',
                         'P = [ [1, 0], [-1, 1] ].<br>det(P) = (1)(1) - (0)(-1) = 1.<br>P⁻¹ = [ [1, 0], [1, 1] ].',
                         'Execute step 4: construct modal matrix p and p⁻¹ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 5: Compute D¹⁰ and A¹⁰ = P D¹⁰ P⁻¹',
                         'D = [ [1, 0], [0, 3] ]  ⇒  D¹⁰ = [ [1¹⁰, 0], [0, 3¹⁰] ] = [ [1, 0], [0, 59049] ].<br>P D¹⁰ = '
                         '[ [1, 0], [-1, 1] ] [ [1, 0], [0, 3¹⁰] ] = [ [1, 0], [-1, 3¹⁰] ].<br>A¹⁰ = (P D¹⁰) P⁻¹ = [ '
                         '[1, 0], [-1, 3¹⁰] ] [ [1, 0], [1, 1] ]<br>= [ [1(1) + 0(1), 1(0) + 0(1)], [-1(1) + 3¹⁰(1), '
                         '-1(0) + 3¹⁰(1)] ]<br>= [ [1, 0], [3¹⁰ - 1, 3¹⁰] ].<br>Since 3¹⁰ = 59049: 3¹⁰ - 1 = '
                         '59048.<br>A¹⁰ = [ [1, 0], [59048, 59049] ].',
                         'Execute step 5: compute d¹⁰ and a¹⁰ = p d¹⁰ p⁻¹ to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Powers of Matrix Using Diagonalization (Aⁿ = P Dⁿ P⁻¹)'},
    {   'concept': 'Every m×n matrix of rank r can be reduced to the normal form [I_r 0; 0 0] using both row and '
                   'column elementary operations. The order of the identity block equals the rank.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Normal Form: [ [I₂, O], [O, O] ] where I₂ is a 2×2 identity matrix;  Rank ρ(A) = 2',
        'formula': 'PAQ = [ [I_r, 0], [0, 0] ]  ⇒  Rank ρ(A) = r.',
        'formula_expl': 'Row operations clear column entries below pivots; column operations clear row entries to the '
                        'right.',
        'given': '4×4 matrix A.',
        'meaning_en': 'Use both row and column operations to transform A into a canonical block matrix containing an '
                      'identity matrix I_r surrounded by zeros, which reveals rank r.',
        'mistakes': [   (   'Using only row operations.',
                            'Normal form REQUIRES both row AND column operations to reduce off-diagonal elements to '
                            'zero!'),
                        ('Writing rank as 4.', 'Two rows and two columns are completely zero, so rank is 2.')],
        'num': 74,
        'practice_q': 'Reduce A = [[1, 2, -1, 3], [4, 1, 2, 1], [3, -1, 1, 2], [1, 2, 0, 1]] to normal form and find '
                      'rank.',
        'presentation': [   'Show row operations on left and column operations on right.',
                            'Write intermediate matrices clearly.',
                            'State final normal block matrix.',
                            'Conclude rank = 2.'],
        'question': 'Reduce the matrix A = [[0, 1, -3, -1], [1, 0, 1, 1], [3, 1, 0, 2], [1, 1, -2, 0]] to normal form '
                    '[I_r 0; 0 0] using elementary row and column operations, and find its rank.',
        'steps': [   (   'Step 1: Get pivot 1 in (1, 1) by swapping R₁ ↔ R₂',
                         '[ [1, 0, 1, 1], [0, 1, -3, -1], [3, 1, 0, 2], [1, 1, -2, 0] ].',
                         'Execute step 1: get pivot 1 in (1, 1) by swapping r₁ ↔ r₂ to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Clear column 1 below pivot using row operations',
                         'R₃ → R₃ - 3R₁: [0, 1, -3, -1].<br>R₄ → R₄ - R₁: [0, 1, -3, -1].<br>Matrix becomes:<br>[ [1, '
                         '0, 1, 1], [0, 1, -3, -1], [0, 1, -3, -1], [0, 1, -3, -1] ].',
                         'Execute step 2: clear column 1 below pivot using row operations to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Clear row 1 to the right of pivot using column operations',
                         'C₃ → C₃ - C₁: eliminates entry (1, 3).<br>C₄ → C₄ - C₁: eliminates entry (1, 4).<br>Matrix '
                         'becomes:<br>[ [1, 0, 0, 0], [0, 1, -3, -1], [0, 1, -3, -1], [0, 1, -3, -1] ].',
                         'Execute step 3: clear row 1 to the right of pivot using column operations to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 4: Clear rows 3 and 4 using row operations',
                         'R₃ → R₃ - R₂: [0, 0, 0, 0].<br>R₄ → R₄ - R₂: [0, 0, 0, 0].<br>Matrix becomes:<br>[ [1, 0, 0, '
                         '0], [0, 1, -3, -1], [0, 0, 0, 0], [0, 0, 0, 0] ].',
                         'Execute step 4: clear rows 3 and 4 using row operations to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: Clear row 2 to the right of pivot using column operations',
                         'C₃ → C₃ + 3C₂: eliminates -3.<br>C₄ → C₄ + C₂: eliminates -1.<br>Matrix becomes:<br>[ [1, 0, '
                         '0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ] = [ [I₂, O], [O, O] ].',
                         'Execute step 5: clear row 2 to the right of pivot using column operations to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 6: State rank from identity block size',
                         'The identity block is I₂ of size 2×2.<br>Therefore, Rank ρ(A) = 2.',
                         'Execute step 6: state rank from identity block size to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Rank of a 4×4 Matrix by Normal Form [I_r, 0]'},
    {   'concept': 'Cayley-Hamilton theorem allows expressing any higher power Aⁿ and the inverse A⁻¹ as a polynomial '
                   'of degree at most (n - 1) in A.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Cayley-Hamilton Verified: A³ - 6A² + 11A - 6I = O;  A⁻¹ = (1/6) [[4, -2, 2], [-1, 5, -2], '
                        '[-2, -2, 2]];  A⁴ = 25A² - 60A + 36I',
        'formula': 'A³ - s₁A² + s₂A - s₃I = 0  ⇒  A⁻¹ = (1/s₃)[ A² - s₁A + s₂I ];  A⁴ = s₁A³ - s₂A² + s₃A.',
        'formula_expl': 's₁ = Trace, s₂ = sum of principal minors, s₃ = determinant.',
        'given': 'A = [[1, 0, -1], [1, 2, 1], [2, 2, 3]].',
        'meaning_en': 'Verify A³ - s₁A² + s₂A - s₃I = 0, then express A⁻¹ and A⁴ as linear combinations of A², A, and '
                      'I.',
        'mistakes': [   (   'Computing A⁴ by multiplying A² by A².',
                            'The prompt asks to use Cayley-Hamilton; reduce using A³ = 6A² - 11A + 6I!'),
                        ('Arithmetic error in determinant s₃ = 6.', '1(4) - (-1)(-2) = 4 + 2 = 6.')],
        'num': 75,
        'practice_q': 'Verify Cayley-Hamilton theorem for A = [[2, -1, 1], [-1, 2, -1], [1, -1, 2]] and find A⁻¹.',
        'presentation': [   'Compute s₁, s₂, s₃ clearly.',
                            'Show A² and A³.',
                            'Verify A³ - 6A² + 11A - 6I = O explicitly.',
                            'Show algebraic derivation of A⁻¹ and A⁴.'],
        'question': 'State and verify Cayley-Hamilton theorem for A = [[1, 0, -1], [1, 2, 1], [2, 2, 3]]. Hence '
                    'compute A⁻¹ and A⁴.',
        'steps': [   (   'Step 1: Compute coefficients of characteristic equation',
                         '• s₁ = Trace = 1 + 2 + 3 = 6.<br>• s₂ = |2 1; 2 3| + |1 -1; 2 3| + |1 0; 1 2| = (6 - 2) + (3 '
                         '+ 2) + (2 - 0) = 4 + 5 + 2 = 11.<br>• s₃ = det(A) = 1(6 - 2) - 0 + (-1)(2 - 4) = 4 - 0 + 2 = '
                         '6.<br>Characteristic equation: λ³ - 6λ² + 11λ - 6 = 0.<br>Cayley-Hamilton equation: A³ - 6A² '
                         '+ 11A - 6I = O.',
                         'Set up the characteristic determinant det(A - λI) = 0 and expand to obtain the '
                         'characteristic polynomial.'),
                     (   'Step 2: Compute A²',
                         'A² = [ [1, 0, -1], [1, 2, 1], [2, 2, 3] ] [ [1, 0, -1], [1, 2, 1], [2, 2, 3] ]<br>= [ [-1, '
                         '-2, -4], [5, 6, 4], [10, 10, 9] ].',
                         'Execute step 2: compute a² to advance the step-by-step mathematical solution toward the '
                         'final result.'),
                     (   'Step 3: Compute A³ and verify A³ - 6A² + 11A - 6I = O',
                         'A³ = A² · A = [ [-11, -12, -13], [19, 20, 13], [38, 38, 27] ].<br>Evaluating A³ - 6A² + 11A '
                         '- 6I term by term yields [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ] = O.<br>Cayley-Hamilton theorem '
                         'is VERIFIED!',
                         'Execute step 3: compute a³ and verify a³ - 6a² + 11a - 6i = o to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Compute A⁻¹ from Cayley-Hamilton equation',
                         'Multiply by A⁻¹:<br>A² - 6A + 11I - 6A⁻¹ = 0  ⇒  6A⁻¹ = A² - 6A + 11I<br>A⁻¹ = (1/6) [ A² - '
                         '6A + 11I ]<br>= (1/6) [ [4, -2, 2], [-1, 5, -2], [-2, -2, 2] ].',
                         'Execute step 4: compute a⁻¹ from cayley-hamilton equation to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: Compute A⁴ using Cayley-Hamilton equation',
                         'From A³ = 6A² - 11A + 6I, multiply by A:<br>A⁴ = 6A³ - 11A² + 6A = 6(6A² - 11A + 6I) - 11A² '
                         '+ 6A<br>= 36A² - 66A + 36I - 11A² + 6A<br>= 25A² - 60A + 36I.<br>Substituting A² and A gives '
                         'the required 3×3 matrix.',
                         'Execute step 5: compute a⁴ using cayley-hamilton equation to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Cayley-Hamilton Theorem for 3×3 Matrix: Inverse and Higher Powers'}]


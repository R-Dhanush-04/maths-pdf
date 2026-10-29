# -*- coding: utf-8 -*-
"""
Module 5: Linear Transformations
100% Pure English Edition
Includes 25 Fully Solved Questions (5 Fundamental + 10 Intermediate + 10 Exam-Level)
"""

MODULE5_QUESTIONS = [   {   'concept': 'A linear transformation is a function between vector spaces that respects the algebraic '
                   'operations: the transformation of a sum is the sum of transformations, and scaling can be factored '
                   'out.',
        'difficulty': 'Fundamental',
        'final_answer': 'T: V → W is linear if T(a u + b v) = a T(u) + b T(v); Properties: T(0) = 0 and T(-v) = -T(v) '
                        '(Both proved)',
        'formula': 'T(u + v) = T(u) + T(v)  and  T(c u) = c T(u)  for all u, v ∈ V, c ∈ ℝ.<br>Combined: T(a u + b v) = '
                   'a T(u) + b T(v).',
        'formula_expl': 'V is called the domain; W is called the codomain.',
        'given': 'Mapping T: V → W.',
        'meaning_en': 'State the mathematical definition of a linear mapping preserving vector addition and scalar '
                      'multiplication, and prove the preservation of zero vector and negatives.',
        'mistakes': [   (   'Confusing 0 in V with 0 in W.',
                            'T maps the zero vector of domain V to the zero vector of codomain W: T(0_V) = 0_W.'),
                        (   'Assuming every function with T(0)=0 is linear.',
                            'T(0)=0 is a NECESSARY condition, not sufficient (e.g., f(x) = x² has f(0)=0 but is not '
                            'linear).')],
        'num': 101,
        'practice_q': 'Prove that T(u - v) = T(u) - T(v) for any linear transformation T.',
        'presentation': [   'State both additivity and homogeneity.',
                            'Show algebraic proof of T(0) = 0.',
                            'Show T(-v) = -T(v) using c = -1.'],
        'question': 'Define a linear transformation T: V → W between two real vector spaces, and state its two basic '
                    'properties: (i) T(0) = 0 and (ii) T(-v) = -T(v).',
        'steps': [   (   'Step 1: Definition of Linear Transformation',
                         'A mapping T: V → W is called a LINEAR TRANSFORMATION if for all u, v ∈ V and all scalars c ∈ '
                         'ℝ:<br>1. Additivity: T(u + v) = T(u) + T(v).<br>2. Homogeneity: T(c u) = c T(u).',
                         'Verify that the mapping preserves vector addition T(u + v) = T(u) + T(v) and scalar scaling '
                         'T(cu) = c T(u).'),
                     (   'Step 2: Proof that T(0_V) = 0_W',
                         'In vector space V, 0 = 0 + 0.<br>Applying T:<br>T(0) = T(0 + 0) = T(0) + T(0) (by '
                         'additivity).<br>Subtract T(0) from both sides in W:<br>T(0) - T(0) = T(0) + T(0) - T(0)  ⇒  '
                         '0_W = T(0).<br>Hence, T(0) = 0. Proved!',
                         'Execute step 2: proof that t(0_v) = 0_w to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 3: Proof that T(-v) = -T(v)',
                         'For any vector v ∈ V, -v = (-1) v.<br>Applying homogeneity with scalar c = -1:<br>T(-v) = '
                         'T((-1) v) = (-1) T(v) = -T(v). Hence proved!',
                         'Execute step 3: proof that t(-v) = -t(v) to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Definition and Properties of a Linear Transformation'},
    {   'concept': 'A linear transformation must map the origin to the origin. If T(0) ≠ 0, it is immediately '
                   'non-linear. If T(0) = 0, we verify T(a u + b v) = a T(u) + b T(v).',
        'difficulty': 'Fundamental',
        'final_answer': '(i) T is a LINEAR TRANSFORMATION;  (ii) S is NOT a linear transformation because S(0, 0) = '
                        '(1, 0) ≠ (0, 0).',
        'formula': 'Linearity test: T(a u + b v) = a T(u) + b T(v).',
        'formula_expl': 'u = (x₁, y₁), v = (x₂, y₂).',
        'given': 'T(x, y) = (x + y, x - y, 2x);  S(x, y) = (x + 1, y).',
        'meaning_en': 'Test transformation T for additivity and scalar homogeneity; test transformation S to show it '
                      'fails linearity because S(0, 0) ≠ (0, 0).',
        'mistakes': [   (   'Testing only with numbers (e.g. u=(1,2)).',
                            'A numerical example can DISPROVE linearity, but PROVING linearity requires arbitrary '
                            'algebraic variables!'),
                        (   'Claiming S is linear because its graph is a straight line.',
                            "In linear algebra, 'linear' means passing through the origin (y = mx), NOT affine (y = mx "
                            '+ c with c ≠ 0).')],
        'num': 102,
        'practice_q': 'Determine if T(x, y) = (xy, x) is a linear transformation.',
        'presentation': [   'Test S first using S(0) ≠ 0 for immediate 2-line conclusion.',
                            'For T, write out T(a u + b v) and group into a T(u) + b T(v).'],
        'question': 'Determine whether the following transformations are linear: (i) T: ℝ² → ℝ³, T(x, y) = (x + y, x - '
                    'y, 2x), and (ii) S: ℝ² → ℝ², S(x, y) = (x + 1, y).',
        'steps': [   (   'Step 1: Test S(x, y) = (x + 1, y)',
                         'Evaluate S at the origin (0, 0):<br>S(0, 0) = (0 + 1, 0) = (1, 0) ≠ (0, 0).<br>Since a '
                         'linear transformation MUST map the zero vector to the zero vector, S(0) ≠ 0 implies S is NOT '
                         'A LINEAR TRANSFORMATION.',
                         'Execute step 1: test s(x, y) = (x + 1, y) to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Test T(x, y) = (x + y, x - y, 2x) for Linearity',
                         'Let u = (x₁, y₁), v = (x₂, y₂) and a, b ∈ ℝ.<br>a u + b v = (a x₁ + b x₂, a y₁ + b '
                         'y₂).<br>Applying T:<br>T(a u + b v) = ( [a x₁ + b x₂] + [a y₁ + b y₂], [a x₁ + b x₂] - [a y₁ '
                         '+ b y₂], 2[a x₁ + b x₂] )<br>= ( a(x₁ + y₁) + b(x₂ + y₂), a(x₁ - y₁) + b(x₂ - y₂), a(2x₁) + '
                         'b(2x₂) )<br>= a (x₁ + y₁, x₁ - y₁, 2x₁) + b (x₂ + y₂, x₂ - y₂, 2x₂)<br>= a T(u) + b T(v).',
                         'Execute step 2: test t(x, y) = (x + y, x - y, 2x) for linearity to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Conclude for T',
                         'Since T(a u + b v) = a T(u) + b T(v) for all vectors u, v and all scalars a, b, T IS A '
                         'LINEAR TRANSFORMATION.',
                         'Execute step 3: conclude for t to advance the step-by-step mathematical solution toward the '
                         'final result.')],
        'title': 'Testing Linearity of a Transformation (Passing vs Failing)'},
    {   'concept': 'The kernel is the set of all input vectors that collapse to zero in W. The range is the set of all '
                   'output vectors actually reached by T.',
        'difficulty': 'Fundamental',
        'final_answer': 'ker(T) = {v ∈ V : T(v) = 0}; Range(T) = {T(v) : v ∈ V}; ker(T) is a subspace of V (Hence '
                        'proved)',
        'formula': 'ker(T) = { v ∈ V : T(v) = 0_W };  Range(T) = { T(v) ∈ W : v ∈ V }.',
        'formula_expl': 'ker(T) ⊆ V (domain); Range(T) ⊆ W (codomain).',
        'given': 'Linear transformation T: V → W.',
        'meaning_en': 'Provide formal definitions of ker(T) and range(T), and prove that ker(T) satisfies the subspace '
                      'criteria in V.',
        'mistakes': [   (   'Thinking ker(T) is a subspace of W.',
                            'ker(T) is a subspace of the DOMAIN V! Range(T) is a subspace of the CODOMAIN W!'),
                        (   'Confusing ker(T) with the zero vector itself.',
                            'ker(T) is a SET of vectors, not just {0}. It can be multi-dimensional.')],
        'num': 103,
        'practice_q': 'Prove that Range(T) is a subspace of W.',
        'presentation': [   'State both definitions.',
                            'Show 0 ∈ ker(T).',
                            'Show u, v ∈ ker(T) ⇒ u + v ∈ ker(T).',
                            'Show c u ∈ ker(T).'],
        'question': 'Define the Kernel (Null space) and Range (Image) of a linear transformation T: V → W, and prove '
                    'that Kernel(T) is a subspace of V.',
        'steps': [   (   'Step 1: Definitions',
                         '• Kernel of T: ker(T) = { v ∈ V : T(v) = 0_W }.<br>• Range of T: Im(T) = Range(T) = { w ∈ W '
                         ': w = T(v) for some v ∈ V }.',
                         'Execute step 1: definitions to advance the step-by-step mathematical solution toward the '
                         'final result.'),
                     (   'Step 2: Prove ker(T) contains 0_V',
                         'From Q101, T(0_V) = 0_W. Therefore, 0_V ∈ ker(T). (ker(T) is non-empty).',
                         'Execute step 2: prove ker(t) contains 0_v to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 3: Prove Closure under Addition in ker(T)',
                         'Let u, v ∈ ker(T). By definition, T(u) = 0 and T(v) = 0.<br>T(u + v) = T(u) + T(v) = 0 + 0 = '
                         '0.<br>Therefore, (u + v) ∈ ker(T).',
                         'Take two arbitrary elements from the subset and prove their vector sum also satisfies the '
                         'defining condition.'),
                     (   'Step 4: Prove Closure under Scalar Multiplication in ker(T)',
                         'Let c ∈ ℝ and u ∈ ker(T). Then T(u) = 0.<br>T(c u) = c T(u) = c (0) = 0.<br>Therefore, c u ∈ '
                         'ker(T).<br>Since ker(T) satisfies all subspace axioms, ker(T) is a SUBSPACE of V. Hence '
                         'proved.',
                         'Multiply an arbitrary element by an arbitrary scalar and prove the resulting vector remains '
                         'in the subset.')],
        'title': 'Kernel (Null Space) and Range (Image) Definitions'},
    {   'concept': 'The total dimension of the domain V is conserved: every dimension either gets mapped into a '
                   'non-zero output dimension (contributing to rank) or is squashed into zero (contributing to '
                   'nullity).',
        'difficulty': 'Fundamental',
        'final_answer': 'Rank(T) = 2,  Nullity(T) = 1;  Rank + Nullity = 2 + 1 = 3 = dim(ℝ³) (Rank-Nullity Theorem '
                        'Verified)',
        'formula': 'dim(V) = rank(T) + nullity(T), where rank(T) = dim(Range T) and nullity(T) = dim(ker T).',
        'formula_expl': 'dim(Domain) = Rank + Nullity.',
        'given': 'T: ℝ³ → ℝ², T(x, y, z) = (x - y, 2z). Domain V = ℝ³, dim(V) = 3.',
        'meaning_en': 'State dim(V) = rank(T) + nullity(T), and compute rank and nullity of the given transformation '
                      'to verify the theorem.',
        'mistakes': [   (   'Using codomain dimension instead of domain.',
                            'dim(V) is the DOMAIN ℝ³ (dim=3), NOT the codomain ℝ² (dim=2)!'),
                        (   'Arithmetic error: saying nullity = 2.',
                            'Only y is free, so basis has 1 vector, nullity = 1.')],
        'num': 104,
        'practice_q': 'Verify Rank-Nullity theorem for T: ℝ³ → ℝ³, T(x, y, z) = (x + y, y + z, x - z).',
        'presentation': [   'State Rank-Nullity theorem formula.',
                            'Solve for ker(T) to find nullity = 1.',
                            'Find Range(T) basis to get rank = 2.',
                            'Add rank + nullity = 3 and compare with dim(Domain).'],
        'question': 'State the Rank-Nullity Theorem (Dimension Theorem) for a linear transformation T: V → W where V '
                    'is finite-dimensional, and verify it for T: ℝ³ → ℝ², T(x, y, z) = (x - y, 2z).',
        'steps': [   (   'Step 1: State the Rank-Nullity Theorem',
                         'Let V and W be vector spaces, with V finite-dimensional. If T: V → W is a linear '
                         'transformation, then:<br>dim(V) = rank(T) + nullity(T)<br>where rank(T) = dim(Range T) and '
                         'nullity(T) = dim(ker T).',
                         'Execute step 1: state the rank-nullity theorem to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Find ker(T) for the given transformation',
                         'T(x, y, z) = (0, 0)  ⇒  (x - y, 2z) = (0, 0).<br>x - y = 0  ⇒  x = y.<br>2z = 0  ⇒  z = '
                         '0.<br>y is a free variable.<br>Vector: (x, y, z) = (y, y, 0) = y (1, 1, 0).<br>Basis for '
                         'ker(T) = {(1, 1, 0)}.<br>Nullity(T) = dim(ker T) = 1.',
                         'Execute step 2: find ker(t) for the given transformation to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Find Range(T) and Rank(T)',
                         'T(x, y, z) = (x - y, 2z) = x (1, 0) + y (-1, 0) + z (0, 2).<br>Spanning vectors of Range(T) '
                         'are (1, 0) and (0, 2).<br>Since these 2 vectors in ℝ² are linearly independent (det |1 0; 0 '
                         '2| = 2 ≠ 0), they form a basis for Range(T).<br>Rank(T) = dim(Range T) = 2.',
                         'Determine the subspace spanned by the images of the domain basis vectors to construct the '
                         'range.'),
                     (   'Step 4: Verify Rank-Nullity Theorem',
                         'dim(Domain V) = dim(ℝ³) = 3.<br>rank(T) + nullity(T) = 2 + 1 = 3.<br>Since dim(V) = rank(T) '
                         '+ nullity(T) = 3, the theorem is VERIFIED!',
                         'Verify the dimension theorem: the sum of the rank and the nullity equals the dimension of '
                         'the domain space.')],
        'title': 'Rank-Nullity Theorem Statement and Verification'},
    {   'concept': 'Any linear transformation T: ℝⁿ → ℝᵐ is completely determined by its action on the standard basis '
                   'vectors: [T] = [ T(e₁) | T(e₂) | ... | T(e_n) ].',
        'difficulty': 'Fundamental',
        'final_answer': 'Standard Matrix [T] = [[0, -1], [-1, 0]]',
        'formula': '[T] = [ T(1, 0) | T(0, 1) ].',
        'formula_expl': 'Rotation by 90°: R = [[0, -1], [1, 0]]; Reflection across x-axis: M = [[1, 0], [0, -1]]. [T] '
                        '= M · R.',
        'given': 'Operations: R_90 followed by reflection across x-axis.',
        'meaning_en': 'Evaluate T on standard basis vectors e₁ = (1, 0) and e₂ = (0, 1), and place the transformed '
                      'vectors as columns of matrix [T].',
        'mistakes': [   (   'Reversing the order of composition: R · M instead of M · R.',
                            "Transformation 'A followed by B' corresponds to matrix B · A!"),
                        (   'Placing T(e₁) as a row instead of a column.',
                            'Standard matrix puts images of basis vectors as COLUMNS.')],
        'num': 105,
        'practice_q': 'Find the standard matrix of reflection across the line y = x in ℝ².',
        'presentation': [   'Show transformation of e₁ = (1, 0) and e₂ = (0, 1).',
                            'Form matrix with T(e₁) and T(e₂) as columns.',
                            'Verify using matrix product M · R.'],
        'question': 'Find the standard matrix [T] for the linear transformation T: ℝ² → ℝ² that first rotates a vector '
                    'counterclockwise by 90° and then reflects it across the x-axis.',
        'steps': [   (   'Step 1: Track e₁ = (1, 0)',
                         '• Rotate 90° counterclockwise: (1, 0) → (0, 1).<br>• Reflect across x-axis: (0, 1) → (0, '
                         '-1).<br>Thus: T(e₁) = [0, -1]ᵀ (Column 1 of [T]).',
                         'Execute step 1: track e₁ = (1, 0) to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 2: Track e₂ = (0, 1)',
                         '• Rotate 90° counterclockwise: (0, 1) → (-1, 0).<br>• Reflect across x-axis: (-1, 0) → (-1, '
                         '0) (points on x-axis do not change under reflection).<br>Thus: T(e₂) = [-1, 0]ᵀ (Column 2 of '
                         '[T]).',
                         'Execute step 2: track e₂ = (0, 1) to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 3: Construct the Standard Matrix [T]',
                         '[T] = [ T(e₁) | T(e₂) ] = [ [0, -1], [-1, 0] ].',
                         'Evaluate the transformation on each standard basis vector and place the resulting coordinate '
                         'vectors as columns of [T].'),
                     (   'Step 4: Verify by matrix multiplication [T] = M · R',
                         'R = [ [cos 90°, -sin 90°], [sin 90°, cos 90°] ] = [ [0, -1], [1, 0] ].<br>M = [ [1, 0], [0, '
                         '-1] ].<br>M · R = [ [1, 0], [0, -1] ] [ [0, -1], [1, 0] ] = [ [0, -1], [-1, 0] ]. Matches!',
                         'Execute step 4: verify by matrix multiplication [t] = m · r to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Standard Matrix of a Linear Transformation'},
    {   'concept': 'A linear transformation is completely and uniquely determined by its values on a basis of the '
                   'domain. Any vector (x, y) = c₁ v₁ + c₂ v₂ satisfies T(x, y) = c₁ T(v₁) + c₂ T(v₂).',
        'difficulty': 'Intermediate',
        'final_answer': 'General formula: T(x, y) = (3x - y, 2x + y);  T(3, 5) = (4, 11)',
        'formula': '(x, y) = c₁ (1, 1) + c₂ (1, -1)  ⇒  c₁ = (x + y)/2,  c₂ = (x - y)/2.<br>T(x, y) = c₁ T(1, 1) + c₂ '
                   'T(1, -1).',
        'formula_expl': 'Linearity allows distributing T over the basis expansion.',
        'given': 'T(1, 1) = (2, 3), T(1, -1) = (4, 1).',
        'meaning_en': 'Express arbitrary vector (x, y) in terms of basis {(1, 1), (1, -1)}, use linearity to find T(x, '
                      'y), and evaluate for (3, 5).',
        'mistakes': [   ('Arithmetic error in 3(3) - 5 = 4.', 'Be careful with basic arithmetic.'),
                        (   'Attempting to guess the formula.',
                            'Always use the systematic basis expansion (x, y) = c₁ v₁ + c₂ v₂.')],
        'num': 106,
        'practice_q': 'If T(1, 0) = (1, 2) and T(0, 1) = (-1, 3), find T(x, y) and T(2, -4).',
        'presentation': [   'Solve for c₁ and c₂ in terms of x and y.',
                            'Use T(x, y) = c₁ T(v₁) + c₂ T(v₂).',
                            'Simplify components clearly.',
                            'Substitute (3, 5) to evaluate.'],
        'question': 'A linear transformation T: ℝ² → ℝ² satisfies T(1, 1) = (2, 3) and T(1, -1) = (4, 1). Find a '
                    'general formula for T(x, y) and evaluate T(3, 5).',
        'steps': [   (   'Step 1: Express (x, y) as linear combination of (1, 1) and (1, -1)',
                         '(x, y) = c₁ (1, 1) + c₂ (1, -1) = (c₁ + c₂, c₁ - c₂).<br>c₁ + c₂ = x<br>c₁ - c₂ = '
                         'y.<br>Adding: 2c₁ = x + y  ⇒  c₁ = (x + y) / 2.<br>Subtracting: 2c₂ = x - y  ⇒  c₂ = (x - y) '
                         '/ 2.',
                         'Execute step 1: express (x, y) as linear combination of (1, 1) and (1, -1) to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 2: Apply linear transformation T',
                         'T(x, y) = c₁ T(1, 1) + c₂ T(1, -1)<br>= [ (x + y)/2 ] (2, 3) + [ (x - y)/2 ] (4, 1).',
                         'Execute step 2: apply linear transformation t to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Simplify components',
                         '• First component: [(x + y)/2](2) + [(x - y)/2](4) = (x + y) + 2(x - y) = x + y + 2x - 2y = '
                         '3x - y.<br>• Second component: [(x + y)/2](3) + [(x - y)/2](1) = [3x + 3y + x - y] / 2 = [4x '
                         '+ 2y] / 2 = 2x + y.<br>Therefore: T(x, y) = (3x - y, 2x + y).',
                         'Execute step 3: simplify components to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 4: Verify with given conditions',
                         'T(1, 1) = (3(1) - 1, 2(1) + 1) = (2, 3). Matches!<br>T(1, -1) = (3(1) - (-1), 2(1) + (-1)) = '
                         '(4, 1). Matches!',
                         'Execute step 4: verify with given conditions to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 5: Evaluate T(3, 5)',
                         'T(3, 5) = ( 3(3) - 5, 2(3) + 5 ) = ( 9 - 5, 6 + 5 ) = (4, 11).',
                         'Execute step 5: evaluate t(3, 5) to advance the step-by-step mathematical solution toward '
                         'the final result.')],
        'title': 'Finding a Linear Transformation from Its Action on a Basis'},
    {   'concept': 'The matrix of T is A. Null space of A gives ker(T); Column space of A gives Range(T).',
        'difficulty': 'Intermediate',
        'final_answer': 'Kernel: Basis = {(3, -1, 1)}, Nullity = 1;  Range: Basis = {(1, 0, 1), (2, 1, 1)}, Rank = 2',
        'formula': 'A = [ [1, 2, -1], [0, 1, 1], [1, 1, -2] ].',
        'formula_expl': 'Columns of A generate Range(T); solutions of AX = 0 form ker(T).',
        'given': 'T(x, y, z) = (x + 2y - z, y + z, x + y - 2z).',
        'meaning_en': 'Row reduce the matrix of T to compute the nullity, null space basis, rank, and range basis.',
        'mistakes': [   (   'Using echelon columns for Range basis.',
                            'You must take the PIVOT COLUMNS OF THE ORIGINAL MATRIX A, not the reduced matrix!'),
                        ('Arithmetic error in x = -2(-z) + z = 3z.', '2z + z = 3z.')],
        'num': 107,
        'practice_q': 'Find basis and dimension of ker(T) and Range(T) for T(x, y, z) = (x - y + z, 2x + y - z, 3x).',
        'presentation': [   'Write matrix A.',
                            'Show row reduction to echelon form.',
                            'Solve for ker(T) with free variable z.',
                            'Select pivot columns for Range(T).',
                            'State Rank and Nullity.'],
        'question': 'For the linear transformation T: ℝ³ → ℝ³ defined by T(x, y, z) = (x + 2y - z, y + z, x + y - 2z), '
                    'find: (i) a basis and dimension for the Kernel, and (ii) a basis and dimension for the Range.',
        'steps': [   (   'Step 1: Set up coefficient matrix A',
                         'A = [ [1, 2, -1], [0, 1, 1], [1, 1, -2] ].',
                         'Execute step 1: set up coefficient matrix a to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Reduce A to row-echelon form',
                         'R₃ → R₃ - R₁: [0, -1, -1].<br>R₃ → R₃ + R₂: [0, 0, 0].<br>Echelon form:<br>[ [1, 2, -1], [0, '
                         '1, 1], [0, 0, 0] ].<br>Pivots in columns 1 and 2 (x, y). Free variable is z.',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: Solve for Kernel (Null Space)',
                         'From Row 2: y + z = 0  ⇒  y = -z.<br>From Row 1: x + 2y - z = 0  ⇒  x = -2y + z = -2(-z) + z '
                         '= 3z.<br>Vector: (x, y, z) = (3z, -z, z) = z (3, -1, 1).<br>Basis for ker(T): B_ker = {(3, '
                         '-1, 1)}.<br>Nullity(T) = dim(ker T) = 1.',
                         'Find all input vectors that map to the zero vector by setting T(v) = 0 and solving the '
                         'resulting homogeneous system.'),
                     (   'Step 4: Find Range(T) and Rank(T)',
                         'Since pivots are in columns 1 and 2, the corresponding original columns of A form a basis '
                         'for Range(T):<br>Basis for Range(T): B_range = {(1, 0, 1), (2, 1, 1)}.<br>Rank(T) = '
                         'dim(Range T) = 2.',
                         'Determine the subspace spanned by the images of the domain basis vectors to construct the '
                         'range.'),
                     (   'Step 5: Verify Rank-Nullity Theorem',
                         'Rank + Nullity = 2 + 1 = 3 = dim(Domain ℝ³). Verified!',
                         'Verify the dimension theorem: the sum of the rank and the nullity equals the dimension of '
                         'the domain space.')],
        'title': 'Kernel, Nullity, Range, and Rank of a Transformation from ℝ³ to ℝ³'},
    {   'concept': 'For a linear operator between spaces of the same finite dimension: T is one-to-one ⇔ T is onto ⇔ '
                   'det(A) ≠ 0 ⇔ ker(T) = {0} ⇔ T is invertible (isomorphism).',
        'difficulty': 'Intermediate',
        'final_answer': 'det(A) = 2 ≠ 0;  (i) T is ONE-TO-ONE,  (ii) T is ONTO,  (iii) T is an ISOMORPHISM.',
        'formula': 'det(A) ≠ 0  ⇒  T is both one-to-one and onto.',
        'formula_expl': 'Matrix A = [[1, 1, 0], [0, 1, 1], [1, 0, 1]].',
        'given': 'T(x, y, z) = (x + y, y + z, x + z).',
        'meaning_en': 'Check if ker(T) = {0} (one-to-one) and if rank(T) = dim(codomain) (onto). If both hold, T is an '
                      'isomorphism.',
        'mistakes': [   ('Computing det(A) as 0.', 'Carefully expand: 1(1) - 1(-1) = 1 + 1 = 2, NOT 1 - 1 = 0!'),
                        (   'Thinking one-to-one and onto must always be checked separately.',
                            'When domain and codomain have the same finite dimension, det ≠ 0 guarantees BOTH '
                            'simultaneously!')],
        'num': 108,
        'practice_q': 'Determine if T(x, y, z) = (x - y, y - z, z - x) is one-to-one and onto.',
        'presentation': [   'Construct matrix A.',
                            'Evaluate det(A) = 2 ≠ 0.',
                            'State theorem: ker(T) = {0} ⇔ one-to-one.',
                            'State theorem: rank(T) = dim(codomain) ⇔ onto.',
                            'Conclude isomorphism.'],
        'question': 'Determine whether the linear transformation T: ℝ³ → ℝ³ defined by T(x, y, z) = (x + y, y + z, x + '
                    'z) is: (i) one-to-one (injective), (ii) onto (surjective), and (iii) an isomorphism.',
        'steps': [   (   'Step 1: Write matrix representation A',
                         'A = [ [1, 1, 0], [0, 1, 1], [1, 0, 1] ].',
                         'Execute step 1: write matrix representation a to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Evaluate det(A)',
                         'det(A) = 1(1·1 - 0·1) - 1(0·1 - 1·1) + 0<br>= 1(1) - 1(-1) = 1 + 1 = 2.',
                         'Evaluate the Hessian discriminant D = rt - s²; D > 0 and r > 0 indicates a local minimum, '
                         'while D > 0 and r < 0 indicates a local maximum.'),
                     (   'Step 3: Test for One-to-One (Injective)',
                         'Since det(A) = 2 ≠ 0, the homogeneous system AX = 0 has ONLY the trivial solution X = '
                         '0.<br>Therefore, ker(T) = {(0, 0, 0)}.<br>Since ker(T) contains only the zero vector, T is '
                         'ONE-TO-ONE.',
                         'Show that the kernel contains only the zero vector, which proves the transformation is '
                         'injective (one-to-one).'),
                     (   'Step 4: Test for Onto (Surjective)',
                         'Rank(T) = rank(A) = 3 (since det(A) ≠ 0).<br>Dimension of codomain W = dim(ℝ³) = 3.<br>Since '
                         'rank(T) = dim(codomain), Range(T) = ℝ³.<br>Therefore, T is ONTO.',
                         'Show that the rank of the transformation equals the dimension of the codomain, proving '
                         'surjectivity (onto).'),
                     (   'Step 5: Conclude Isomorphism',
                         'Since T is both one-to-one and onto (a bijective linear transformation), T IS AN '
                         'ISOMORPHISM.',
                         'Execute step 5: conclude isomorphism to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Testing Whether a Linear Transformation is One-to-One and Onto'},
    {   'concept': "The j-th column of the matrix representation [T]_{B, B'} consists of the coordinate vector of "
                   "T(u_j) relative to the basis B': Col_j = [ T(u_j) ]_{B'}.",
        'difficulty': 'Intermediate',
        'final_answer': "Matrix Representation [T]_{B, B'} = [[1, 2], [4, 1], [1, 1]]",
        'formula': "[T]_{B, B'} = [ [T(u₁)]_{B'} | [T(u₂)]_{B'} ].",
        'formula_expl': 'Size of matrix is dim(W) × dim(V) = 3 × 2.',
        'given': "T(x, y) = (2x - y, x + 3y, x), B = {(1, 1), (1, 0)}, B' = standard basis of ℝ³.",
        'meaning_en': "Compute T on each basis vector of B, express the outputs in terms of B', and construct matrix "
                      "[T]_{B, B'}.",
        'mistakes': [   (   'Writing matrix as 2×3 instead of 3×2.',
                            'The matrix size is always dim(Codomain) × dim(Domain) = 3 × 2!'),
                        (   'Placing vectors as rows.',
                            'Coordinate vectors must form COLUMNS of the transformation matrix.')],
        'num': 109,
        'practice_q': 'Find matrix of T(x, y) = (x + y, x - y) relative to basis B = {(1, 2), (2, 1)} in ℝ².',
        'presentation': [   'Evaluate T(u₁) and T(u₂).',
                            'Write outputs as columns of the 3×2 matrix.',
                            'Verify with test coordinate vector.'],
        'question': "Find the matrix representation [T]_{B, B'} of the linear transformation T: ℝ² → ℝ³ defined by "
                    "T(x, y) = (2x - y, x + 3y, x) relative to the bases B = {u₁ = (1, 1), u₂ = (1, 0)} of ℝ² and B' = "
                    '{e₁, e₂, e₃} (standard basis) of ℝ³.',
        'steps': [   (   'Step 1: Apply T to first basis vector u₁ = (1, 1)',
                         "T(1, 1) = ( 2(1) - 1, 1 + 3(1), 1 ) = (1, 4, 1).<br>Relative to standard basis B', "
                         "[T(u₁)]_{B'} = [1, 4, 1]ᵀ (Column 1).",
                         'Execute step 1: apply t to first basis vector u₁ = (1, 1) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Apply T to second basis vector u₂ = (1, 0)',
                         "T(1, 0) = ( 2(1) - 0, 1 + 3(0), 1 ) = (2, 1, 1).<br>Relative to standard basis B', "
                         "[T(u₂)]_{B'} = [2, 1, 1]ᵀ (Column 2).",
                         'Execute step 2: apply t to second basis vector u₂ = (1, 0) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   "Step 3: Construct the matrix [T]_{B, B'}",
                         "Assemble the two column vectors into a 3×2 matrix:<br>[T]_{B, B'} = [ [1, 2], [4, 1], [1, 1] "
                         '].',
                         "Execute step 3: construct the matrix [t]_{b, b'} to advance the step-by-step mathematical "
                         'solution toward the final result.'),
                     (   'Step 4: Verify by applying to vector u₁ = (1, 1)',
                         "In basis B, coordinate of u₁ is [1, 0]ᵀ.<br>[T]_{B, B'} [1, 0]ᵀ = [1, 4, 1]ᵀ. Matches T(1, "
                         '1)! Verified.',
                         'Execute step 4: verify by applying to vector u₁ = (1, 1) to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Matrix Representation Relative to Non-Standard Bases'},
    {   'concept': 'The matrix of a composition of linear transformations is the product of their individual standard '
                   'matrices: [S ∘ T] = [S] [T].',
        'difficulty': 'Intermediate',
        'final_answer': '[T] = [[-1, 0], [0, 1]];  [S] = (1/√2)[[1, -1], [1, 1]];  [S ∘ T] = (1/√2)[[-1, -1], [-1, 1]]',
        'formula': '[S ∘ T] = [S] · [T].',
        'formula_expl': 'Reflection across y-axis: (x, y) → (-x, y); Rotation by θ: [[cos θ, -sin θ], [sin θ, cos θ]].',
        'given': 'T = reflection across y-axis, S = rotation by θ = 45°.',
        'meaning_en': 'Find matrices [T] and [S], then multiply them in the correct order [S ∘ T] = [S] · [T].',
        'mistakes': [   (   'Multiplying in reverse order [T] [S].',
                            'S ∘ T means T is applied first, then S, so the matrix is [S] · [T]!'),
                        (   'Sign error in reflection: (-x, y).',
                            'Reflecting across the y-axis flips the sign of x, leaving y unchanged.')],
        'num': 110,
        'practice_q': 'Find the matrix of (T ∘ S) and verify that [S ∘ T] ≠ [T ∘ S] (non-commutativity).',
        'presentation': [   'State [T] and [S] clearly.',
                            'State composition formula [S ∘ T] = [S] [T].',
                            'Show matrix multiplication step by step.'],
        'question': 'Let T: ℝ² → ℝ² be reflection across the y-axis, and S: ℝ² → ℝ² be counterclockwise rotation by '
                    '45°. Find the standard matrices [T] and [S], and find the matrix of the composite transformation '
                    '(S ∘ T).',
        'steps': [   (   'Step 1: Find matrix [T] for reflection across y-axis',
                         'T(1, 0) = (-1, 0)<br>T(0, 1) = (0, 1).<br>[T] = [ [-1, 0], [0, 1] ].',
                         'Execute step 1: find matrix [t] for reflection across y-axis to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Find matrix [S] for rotation by 45°',
                         'cos 45° = 1/√2,   sin 45° = 1/√2.<br>[S] = [ [cos 45°, -sin 45°], [sin 45°, cos 45°] ] = '
                         '(1/√2) [ [1, -1], [1, 1] ].',
                         'Execute step 2: find matrix [s] for rotation by 45° to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Compute matrix product [S ∘ T] = [S] · [T]',
                         '[S ∘ T] = (1/√2) [ [1, -1], [1, 1] ] [ [-1, 0], [0, 1] ]<br>= (1/√2) [ [1(-1) + (-1)(0), '
                         '1(0) + (-1)(1)], [1(-1) + 1(0), 1(0) + 1(1)] ]<br>= (1/√2) [ [-1, -1], [-1, 1] ].',
                         'Execute step 3: compute matrix product [s ∘ t] = [s] · [t] to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Composition of Linear Transformations and Matrix Multiplication'},
    {   'concept': 'Calculus operations like differentiation and integration are linear transformations on polynomial '
                   'and function spaces. Differential equations can thus be solved using matrix methods.',
        'difficulty': 'Intermediate',
        'final_answer': 'Matrix [D] = [[0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3]];  Rank = 3,  Nullity = 1',
        'formula': 'D(xⁿ) = n xⁿ⁻¹;  dim(P₃) = rank(D) + nullity(D) = 4.',
        'formula_expl': "B has 4 basis elements; B' has 3 basis elements.",
        'given': "D: P₃ → P₂, D(p) = p'(x).",
        'meaning_en': "Differentiate each basis vector of P₃, express outputs in basis B', construct matrix [D], and "
                      'state rank and nullity.',
        'mistakes': [   (   'Thinking D(1) = 1.',
                            'The derivative of constant 1 is ZERO: D(1) = 0, so column 1 is all zeros!'),
                        ('Matrix size 4×3 instead of 3×4.', 'dim(Codomain P₂) = 3 rows, dim(Domain P₃) = 4 columns.')],
        'num': 111,
        'practice_q': 'Find matrix of integration operator T: P₂ → P₃, T(p) = ∫₀^x p(t) dt.',
        'presentation': [   'Differentiate each basis vector.',
                            'Write outputs as columns of 3×4 matrix.',
                            'Identify rank = 3 from non-zero rows.',
                            'Identify nullity = 1 from constants.'],
        'question': "Let D: P₃ → P₂ be the differentiation operator defined by D(p(x)) = p'(x). Find the matrix "
                    "representation of D relative to the standard bases B = {1, x, x², x³} and B' = {1, x, x²}, and "
                    'find its rank and nullity.',
        'steps': [   (   'Step 1: Differentiate each basis vector of B = {1, x, x², x³}',
                         '• D(1) = 0 = 0(1) + 0(x) + 0(x²)<br>• D(x) = 1 = 1(1) + 0(x) + 0(x²)<br>• D(x²) = 2x = 0(1) '
                         '+ 2(x) + 0(x²)<br>• D(x³) = 3x² = 0(1) + 0(x) + 3(x²).',
                         'Execute step 1: differentiate each basis vector of b = {1, x, x², x³} to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 2: Construct the 3×4 matrix [D]',
                         'Columns are the coordinate vectors:<br>[D] = [ [0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3] ].',
                         'Execute step 2: construct the 3×4 matrix [d] to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Determine Rank(D)',
                         'The matrix [D] is in row-echelon form with 3 non-zero rows (pivots at cols 2, 3, '
                         '4).<br>Therefore, Rank(D) = 3.',
                         'Execute step 3: determine rank(d) to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 4: Determine Nullity(D) and Kernel',
                         "ker(D) consists of polynomials whose derivative is 0: p'(x) = 0  ⇒  p(x) = c (constant "
                         'polynomials).<br>Basis for ker(D) = {1}.<br>Nullity(D) = dim(ker D) = 1.',
                         'Find all input vectors that map to the zero vector by setting T(v) = 0 and solving the '
                         'resulting homogeneous system.'),
                     (   'Step 5: Verify Rank-Nullity Theorem',
                         'dim(P₃) = 4.<br>Rank + Nullity = 3 + 1 = 4 = dim(P₃). Verified!',
                         'Verify the dimension theorem: the sum of the rank and the nullity equals the dimension of '
                         'the domain space.')],
        'title': 'Linear Transformation on Polynomial Space: Differentiation Operator'},
    {   'concept': 'A linear operator is invertible if and only if its standard matrix [T] is invertible: [T⁻¹] = '
                   '[T]⁻¹.',
        'difficulty': 'Intermediate',
        'final_answer': 'det[T] = -1 ≠ 0 (Invertible);  Inverse Formula: T⁻¹(x, y) = (-3x + 5y, 2x - 3y)',
        'formula': '[T] = [[3, 5], [2, 3]];  [T⁻¹] = [T]⁻¹ = (1/det) [[d, -b], [-c, a]].',
        'formula_expl': 'det = ad - bc = 9 - 10 = -1.',
        'given': 'T(x, y) = (3x + 5y, 2x + 3y).',
        'meaning_en': 'Show det([T]) ≠ 0 to prove invertibility, invert the matrix [T]⁻¹, and multiply by (x, y) to '
                      'find T⁻¹(x, y).',
        'mistakes': [   (   'Sign error in 2×2 matrix inverse.',
                            'Remember formula: swap diagonal entries, negate off-diagonal entries, divide by det.'),
                        (   'Forgetting to divide by det = -1.',
                            'Dividing by -1 flips all signs in the adjugate matrix.')],
        'num': 112,
        'practice_q': 'Find T⁻¹(x, y) for T(x, y) = (x + 2y, 2x + 5y).',
        'presentation': [   'Find standard matrix [T].',
                            'Show det[T] = -1 ≠ 0 to prove invertibility.',
                            'Compute [T]⁻¹.',
                            'Write T⁻¹(x, y) and verify.'],
        'question': 'Show that the linear operator T: ℝ² → ℝ² defined by T(x, y) = (3x + 5y, 2x + 3y) is invertible, '
                    'and find the formula for T⁻¹(x, y).',
        'steps': [   (   'Step 1: Write standard matrix [T]',
                         '[T] = [ [3, 5], [2, 3] ].',
                         'Evaluate the transformation on each standard basis vector and place the resulting coordinate '
                         'vectors as columns of [T].'),
                     (   'Step 2: Check invertibility via determinant',
                         'det[T] = (3)(3) - (5)(2) = 9 - 10 = -1 ≠ 0.<br>Since det[T] ≠ 0, the matrix [T] is '
                         'invertible, and therefore T is an INVERTIBLE LINEAR OPERATOR.',
                         'Execute step 2: check invertibility via determinant to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Compute matrix inverse [T]⁻¹',
                         '[T]⁻¹ = (1 / -1) [ [3, -5], [-2, 3] ] = [ [-3, 5], [2, -3] ].',
                         'Execute step 3: compute matrix inverse [t]⁻¹ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Form the formula for T⁻¹(x, y)',
                         'T⁻¹(x, y) = [ [-3, 5], [2, -3] ] [x, y]ᵀ = [ -3x + 5y, 2x - 3y ]ᵀ.<br>T⁻¹(x, y) = (-3x + 5y, '
                         '2x - 3y).',
                         'Execute step 4: form the formula for t⁻¹(x, y) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 5: Verify T ∘ T⁻¹ = Identity',
                         'T(T⁻¹(x, y)) = T(-3x + 5y, 2x - 3y)<br>= ( 3(-3x + 5y) + 5(2x - 3y), 2(-3x + 5y) + 3(2x - '
                         '3y) )<br>= ( -9x + 15y + 10x - 15y, -6x + 10y + 6x - 9y )<br>= (x, y). Exactly identity! '
                         'Verified.',
                         'Execute step 5: verify t ∘ t⁻¹ = identity to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Inverse of an Invertible Linear Transformation'},
    {   'concept': 'Two matrices represent the same linear operator in different coordinate systems if and only if '
                   "they are similar: A' = P⁻¹ A P, where P is the change of basis matrix.",
        'difficulty': 'Intermediate',
        'final_answer': "[T]_{B'} = P⁻¹ [T]_B P = [[13/3, 8/3], [-2/3, -4/3]] (Verified)",
        'formula': "[T]_{B'} = P⁻¹ [T]_B P, where P = [v₁ | v₂].",
        'formula_expl': 'v₁ = (1, 1), v₂ = (2, -1).',
        'given': "T(x, y) = (x + 2y, 3x + 2y), B = standard, B' = {(1, 1), (2, -1)}.",
        'meaning_en': 'Verify the similarity transformation relating matrix representations of the same linear '
                      'operator under different bases.',
        'mistakes': [   ('Computing P [T] P⁻¹ instead of P⁻¹ [T] P.', "Remember: [T]_{B'} = P⁻¹ [T]_B P!"),
                        ('Determinant error in det(P) = -3.', '1(-1) - 2(1) = -3.')],
        'num': 113,
        'practice_q': "Find [T]_{B'} for T(x, y) = (2x, 3y) with B' = {(1, 1), (1, -1)}.",
        'presentation': [   'Find [T]_B and P.',
                            'Compute P⁻¹.',
                            'Show matrix multiplications to get P⁻¹ [T] P.',
                            'Verify with direct basis transformation.'],
        'question': 'Let T: ℝ² → ℝ² be defined by T(x, y) = (x + 2y, 3x + 2y). Find the matrix [T]_B relative to '
                    "standard basis B, and the matrix [T]_{B'} relative to basis B' = {(1, 1), (2, -1)}, and verify "
                    "that [T]_{B'} = P⁻¹ [T]_B P.",
        'steps': [   (   'Step 1: Standard matrix [T]_B',
                         '[T]_B = [ [1, 2], [3, 2] ].',
                         'Evaluate the transformation on each standard basis vector and place the resulting coordinate '
                         'vectors as columns of [T].'),
                     (   'Step 2: Transition matrix P and P⁻¹',
                         'P = [ [1, 2], [1, -1] ].<br>det(P) = (1)(-1) - (2)(1) = -1 - 2 = -3.<br>P⁻¹ = (1 / -3) [ '
                         '[-1, -2], [-1, 1] ] = (1/3) [ [1, 2], [1, -1] ].',
                         'Execute step 2: transition matrix p and p⁻¹ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Compute P⁻¹ [T]_B P',
                         '[T]_B P = [ [1, 2], [3, 2] ] [ [1, 2], [1, -1] ] = [ [1+2, 2-2], [3+2, 6-2] ] = [ [3, 0], '
                         '[5, 4] ].<br>P⁻¹ ([T]_B P) = (1/3) [ [1, 2], [1, -1] ] [ [3, 0], [5, 4] ]<br>= (1/3) [ '
                         '[3+10, 0+8], [3-5, 0-4] ] = (1/3) [ [13, 8], [-2, -4] ] = [ [13/3, 8/3], [-2/3, -4/3] ].',
                         'Execute step 3: compute p⁻¹ [t]_b p to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   "Step 4: Compute [T]_{B'} directly",
                         '• T(1, 1) = (3, 5). Write (3, 5) = c₁ (1, 1) + c₂ (2, -1):<br>c₁ + 2c₂ = 3, c₁ - c₂ = 5  ⇒  '
                         '3c₂ = -2  ⇒  c₂ = -2/3, c₁ = 13/3.<br>• T(2, -1) = (2 - 2, 6 - 2) = (0, 4) = d₁ (1, 1) + d₂ '
                         "(2, -1):<br>d₁ + 2d₂ = 0, d₁ - d₂ = 4  ⇒  3d₂ = -4  ⇒  d₂ = -4/3, d₁ = 8/3.<br>[T]_{B'} = [ "
                         '[13/3, 8/3], [-2/3, -4/3] ]. Exactly matches! Verified.',
                         "Execute step 4: compute [t]_{b'} directly to advance the step-by-step mathematical solution "
                         'toward the final result.')],
        'title': 'Similarity of Matrix Representations under Change of Basis'},
    {   'concept': 'For any matrix transformation T_A(x) = A x, rank(T_A) = rank(A) and nullity(T_A) = n - rank(A).',
        'difficulty': 'Intermediate',
        'final_answer': 'rank(T_A) = 2;  nullity(T_A) = 2',
        'formula': 'rank(T) = rank(A);  nullity(T) = 4 - rank(A).',
        'formula_expl': 'Number of columns n = 4.',
        'given': 'A = [[1, -2, 1, 0], [2, -4, 3, -1], [-1, 2, 1, -2]].',
        'meaning_en': 'Reduce matrix A to echelon form to find rank = number of pivot rows, and use Rank-Nullity '
                      'theorem to find nullity = 4 - rank.',
        'mistakes': [   (   'Computing nullity as 3 - rank.',
                            'n is the number of COLUMNS (4), not rows (3)! Domain is ℝ⁴!'),
                        ('Counting column 2 as a pivot.', 'Column 2 has no pivot; it contains a free variable.')],
        'num': 114,
        'practice_q': 'Find rank and nullity of T_A for A = [[1, 1, 2], [1, 0, 1], [2, 1, 3]].',
        'presentation': [   'Show row reduction of A.',
                            'Count non-zero rows for rank = 2.',
                            'Apply nullity = n - rank = 4 - 2 = 2.',
                            'State final values clearly.'],
        'question': 'For the matrix transformation T_A: ℝ⁴ → ℝ³ defined by T_A(x) = A x, where A = [[1, -2, 1, 0], [2, '
                    '-4, 3, -1], [-1, 2, 1, -2]], find rank(T_A) and nullity(T_A).',
        'steps': [   (   'Step 1: Reduce A to row-echelon form',
                         'A = [ [1, -2, 1, 0], [2, -4, 3, -1], [-1, 2, 1, -2] ].<br>R₂ → R₂ - 2R₁: [0, 0, 1, '
                         '-1].<br>R₃ → R₃ + R₁: [0, 0, 2, -2].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 2: Eliminate row 3',
                         'R₃ → R₃ - 2R₂: [0, 0, 0, 0].<br>Row-echelon form:<br>[ [1, -2, 1, 0], [0, 0, 1, -1], [0, 0, '
                         '0, 0] ].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: Determine Rank',
                         'Number of non-zero rows = 2.<br>Therefore: rank(T_A) = rank(A) = 2.',
                         'Execute step 3: determine rank to advance the step-by-step mathematical solution toward the '
                         'final result.'),
                     (   'Step 4: Determine Nullity using Rank-Nullity Theorem',
                         'Number of columns (dimension of domain ℝ⁴) n = 4.<br>nullity(T_A) = n - rank(T_A) = 4 - 2 = '
                         '2.',
                         'Execute step 4: determine nullity using rank-nullity theorem to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Rank and Nullity of a Matrix Transformation'},
    {   'concept': 'An orthogonal projection onto a subspace satisfies two algebraic properties: idempotency P² = P '
                   '(projecting twice gives the same result) and self-adjointness Pᵀ = P.',
        'difficulty': 'Intermediate',
        'final_answer': 'Standard Matrix P = [[1, 0, 0], [0, 1, 0], [0, 0, 0]];  P² = P (Idempotent) and Pᵀ = P '
                        '(Symmetric) (Both verified)',
        'formula': 'T(x, y, z) = (x, y, 0);  P = diag(1, 1, 0).',
        'formula_expl': 'z-component is zeroed out.',
        'given': 'Projection onto xy-plane in ℝ³.',
        'meaning_en': 'Determine matrix P projecting (x, y, z) → (x, y, 0), and verify the algebraic projection '
                      'properties P² = P and Pᵀ = P.',
        'mistakes': [   (   'Thinking projection matrix has non-zero entry at (3, 3).',
                            'Projection onto xy-plane eliminates z, so entry (3, 3) must be 0!'),
                        ('Claiming P is invertible.', 'det(P) = 0, so projection matrices are NEVER invertible.')],
        'num': 115,
        'practice_q': 'Find standard matrix for orthogonal projection onto the line y = 2x in ℝ².',
        'presentation': [   'Show images of e₁, e₂, e₃.',
                            'Write diagonal matrix P.',
                            'Show P² = P multiplication.',
                            'Show Pᵀ = P.'],
        'question': 'Find the standard matrix P of the linear operator T: ℝ³ → ℝ³ that orthogonally projects every '
                    'vector onto the xy-plane, and show that P² = P and Pᵀ = P (orthogonal projection is idempotent '
                    'and symmetric).',
        'steps': [   (   'Step 1: Evaluate T on standard basis vectors',
                         'T(1, 0, 0) = (1, 0, 0)<br>T(0, 1, 0) = (0, 1, 0)<br>T(0, 0, 1) = (0, 0, 0).',
                         'Execute step 1: evaluate t on standard basis vectors to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Construct standard matrix P',
                         'P = [ [1, 0, 0], [0, 1, 0], [0, 0, 0] ].',
                         'Evaluate the transformation on each standard basis vector and place the resulting coordinate '
                         'vectors as columns of [T].'),
                     (   'Step 3: Verify idempotency P² = P',
                         'P² = [ [1, 0, 0], [0, 1, 0], [0, 0, 0] ] [ [1, 0, 0], [0, 1, 0], [0, 0, 0] ]<br>= [ [1, 0, '
                         '0], [0, 1, 0], [0, 0, 0] ] = P. Verified!',
                         'Execute step 3: verify idempotency p² = p to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 4: Verify symmetry Pᵀ = P',
                         'Pᵀ = [ [1, 0, 0], [0, 1, 0], [0, 0, 0] ]ᵀ = [ [1, 0, 0], [0, 1, 0], [0, 0, 0] ] = P. '
                         'Verified!',
                         'Exploit the algebraic symmetry between x and y to write the corresponding partial derivative '
                         'directly.')],
        'title': 'Orthogonal Projection Operator in ℝ³: Matrix and Properties'},
    {   'concept': 'Foundational theorem of linear algebra. Shows that every dimension of V is accounted for: either '
                   'mapped injectively into Range(T) or mapped to 0 in ker(T).',
        'difficulty': 'Exam-Level',
        'final_answer': 'dim(V) = rank(T) + nullity(T) (Rank-Nullity Theorem Hence proved)',
        'formula': 'dim(V) = dim(Range T) + dim(ker T) = rank(T) + nullity(T).',
        'formula_expl': 'Let nullity(T) = k, dim(V) = n. Show rank(T) = n - k.',
        'given': 'Linear transformation T: V → W, dim(V) = n.',
        'meaning_en': 'Start with a basis of ker(T), extend it to a basis of V using the basis extension theorem, and '
                      'prove that the images of the added vectors form a basis for Range(T).',
        'mistakes': [   (   'Forgetting to prove independence of S.',
                            'A basis proof REQUIRES proving BOTH spanning AND linear independence!'),
                        (   'Applying T to the whole equation without justifying T(u_i) = 0.',
                            'Explicitly state that T(u_i) = 0 because u_i ∈ ker(T).')],
        'num': 116,
        'practice_q': 'Apply the Rank-Nullity theorem to show that a linear transformation T: ℝ⁵ → ℝ³ cannot be '
                      'one-to-one.',
        'presentation': [   'State theorem statement.',
                            'Define basis of ker(T) with k vectors.',
                            'Extend to basis of V with n vectors.',
                            'Prove {T(v₁), ..., T(v_{n-k})} spans Range(T).',
                            'Prove independence using ker(T) property.',
                            'Conclude rank = n - k.'],
        'question': 'State and prove the Rank-Nullity Theorem (Dimension Theorem) for a linear transformation T: V → W '
                    'where V is a finite-dimensional vector space.',
        'steps': [   (   'Step 1: Choose a basis for ker(T)',
                         'Let nullity(T) = dim(ker T) = k.<br>Let B_ker = {u₁, u₂, ..., u_k} be a basis for '
                         'ker(T).<br>If k = 0, ker(T) = {0} and basis is empty.',
                         'Execute step 1: choose a basis for ker(t) to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Extend B_ker to a basis of V',
                         'By the Basis Extension Theorem, any linearly independent set in a finite-dimensional vector '
                         'space can be extended to a basis of V.<br>Extend B_ker by adding (n - k) vectors {v₁, v₂, '
                         '..., v_{n-k}} so that:<br>B_V = {u₁, ..., u_k, v₁, ..., v_{n-k}} is a basis for V.<br>Here '
                         'dim(V) = k + (n - k) = n.',
                         'Execute step 2: extend b_ker to a basis of v to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Propose a basis for Range(T)',
                         'We claim that S = {T(v₁), T(v₂), ..., T(v_{n-k})} is a BASIS for Range(T).<br>To prove this, '
                         'we must show two things: (i) S spans Range(T), and (ii) S is linearly independent.',
                         'Determine the subspace spanned by the images of the domain basis vectors to construct the '
                         'range.'),
                     (   'Step 4: Prove S spans Range(T)',
                         'Let w ∈ Range(T). Then w = T(v) for some v ∈ V.<br>Since B_V is a basis for V, v can be '
                         'written as:<br>v = c₁ u₁ + ... + c_k u_k + d₁ v₁ + ... + d_{n-k} v_{n-k}.<br>Applying T and '
                         'using linearity:<br>w = T(v) = Σ c_i T(u_i) + Σ d_j T(v_j).<br>Since each u_i ∈ ker(T), '
                         'T(u_i) = 0.<br>Therefore: w = 0 + d₁ T(v₁) + ... + d_{n-k} T(v_{n-k}).<br>Thus, any vector '
                         'in Range(T) is a linear combination of S. S spans Range(T).',
                         'Determine the subspace spanned by the images of the domain basis vectors to construct the '
                         'range.'),
                     (   'Step 5: Prove S is linearly independent',
                         'Set a linear combination of S to zero:<br>d₁ T(v₁) + d₂ T(v₂) + ... + d_{n-k} T(v_{n-k}) = '
                         '0.<br>By linearity of T:<br>T( d₁ v₁ + ... + d_{n-k} v_{n-k} ) = 0.<br>This means the vector '
                         'x = (d₁ v₁ + ... + d_{n-k} v_{n-k}) belongs to ker(T)!<br>Since {u₁, ..., u_k} is a basis '
                         'for ker(T), x can be written as:<br>d₁ v₁ + ... + d_{n-k} v_{n-k} = c₁ u₁ + ... + c_k '
                         'u_k<br>⇒  c₁ u₁ + ... + c_k u_k - d₁ v₁ - ... - d_{n-k} v_{n-k} = 0.<br>Since B_V is a basis '
                         'for V, all vectors are linearly independent. Therefore, all coefficients MUST be zero:<br>c₁ '
                         '= ... = c_k = 0  and  d₁ = ... = d_{n-k} = 0.<br>Since d_j = 0, the set S is LINEARLY '
                         'INDEPENDENT.',
                         'Execute step 5: prove s is linearly independent to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 6: Conclude the theorem',
                         'Since S is a linearly independent spanning set for Range(T), S is a basis for '
                         'Range(T).<br>Therefore: rank(T) = dim(Range T) = |S| = n - k.<br>rank(T) = dim(V) - '
                         'nullity(T)<br>⇒  dim(V) = rank(T) + nullity(T). Hence proved!',
                         'Execute step 6: conclude the theorem to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Complete Proof of the Rank-Nullity Theorem'},
    {   'concept': 'In general non-linear functions, f(a) = f(b) cannot be tested by checking f(x) = 0. But for linear '
                   'transformations, T(u) - T(v) = T(u - v), so injectivity globally reduces to testing the kernel at '
                   'the origin.',
        'difficulty': 'Exam-Level',
        'final_answer': 'T is one-to-one if and only if ker(T) = {0} (Hence proved)',
        'formula': 'T(u) = T(v)  ⇔  T(u - v) = 0  ⇔  (u - v) ∈ ker(T).',
        'formula_expl': 'If ker(T) = {0}, u - v = 0 ⇒ u = v.',
        'given': 'Linear transformation T: V → W.',
        'meaning_en': 'Prove both directions: if T is injective, only 0 maps to 0; conversely, if only 0 maps to 0, '
                      'T(u) = T(v) implies u = v.',
        'mistakes': [   (   'Proving only one direction.',
                            "'If and only if' demands proving BOTH forward and backward directions!"),
                        ('Writing T(u/v).', 'Division of vectors is completely undefined in linear algebra.')],
        'num': 117,
        'practice_q': 'Use this theorem to prove that T(x, y) = (2x - y, x + y) is one-to-one.',
        'presentation': [   'State proof structure: part 1 (⇒), part 2 (⇐).',
                            'Use linearity T(u) - T(v) = T(u - v).',
                            'Conclude u = v.'],
        'question': 'Prove that a linear transformation T: V → W is one-to-one (injective) if and only if ker(T) = '
                    '{0}.',
        'steps': [   (   'Step 1: Prove Forward Direction (⇒)',
                         'Assume T is one-to-one.<br>We must show ker(T) = {0}.<br>Let v ∈ ker(T). Then T(v) = '
                         '0.<br>We already know T(0) = 0.<br>Therefore: T(v) = T(0).<br>Since T is assumed one-to-one: '
                         'v = 0.<br>Therefore, the only vector in ker(T) is 0, so ker(T) = {0}.',
                         'Execute step 1: prove forward direction (⇒) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Prove Reverse Direction (⇐)',
                         'Assume ker(T) = {0}.<br>We must show T is one-to-one.<br>Let u, v ∈ V such that T(u) = '
                         'T(v).<br>Subtract T(v) from both sides in W:<br>T(u) - T(v) = 0.<br>By linearity of T: T(u - '
                         'v) = T(u) - T(v) = 0.<br>This means (u - v) ∈ ker(T).<br>Since ker(T) = {0}, the only vector '
                         'in ker(T) is zero:<br>u - v = 0  ⇒  u = v.<br>Since T(u) = T(v) implies u = v, T is '
                         'ONE-TO-ONE.',
                         'Execute step 2: prove reverse direction (⇐) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Conclude the proof',
                         'Both implications have been proven.<br>Therefore, T is one-to-one if and only if ker(T) = '
                         '{0}. Hence proved.',
                         'Execute step 3: conclude the proof to advance the step-by-step mathematical solution toward '
                         'the final result.')],
        'title': 'Theorem: T is One-to-One if and only if Kernel(T) = {0}'},
    {   'concept': 'Pigeonhole principle for vector spaces. If a linear map between spaces of equal dimension loses no '
                   'information (nullity = 0), it must cover the entire target space (rank = n).',
        'difficulty': 'Exam-Level',
        'final_answer': 'For dim(V) = dim(W) = n: T is one-to-one ⇔ nullity = 0 ⇔ rank = n ⇔ T is onto (Hence proved)',
        'formula': 'n = rank(T) + nullity(T).',
        'formula_expl': 'T is 1-to-1 ⇔ nullity = 0 ⇔ rank = n ⇔ T is onto.',
        'given': 'dim(V) = dim(W) = n, T: V → W linear.',
        'meaning_en': 'Use the Rank-Nullity Theorem dim(V) = rank(T) + nullity(T) with dim(V) = dim(W) = n to '
                      'establish the equivalence of injectivity and surjectivity.',
        'mistakes': [   (   'Applying this theorem when dim(V) ≠ dim(W).',
                            'This theorem is FALSE if dimensions differ! (e.g., T: ℝ³ → ℝ² can be onto but cannot be '
                            '1-to-1).'),
                        ('Forgetting to state nullity = 0 ⇔ 1-to-1.', 'Quote the theorem from Q117.')],
        'num': 118,
        'practice_q': 'Show that T: ℝ³ → ℝ², T(x, y, z) = (x, y) is onto but not one-to-one.',
        'presentation': [   'Quote Rank-Nullity Theorem: n = rank + nullity.',
                            'Show 1-to-1 ⇒ nullity = 0 ⇒ rank = n ⇒ onto.',
                            'Show onto ⇒ rank = n ⇒ nullity = 0 ⇒ 1-to-1.'],
        'question': 'Prove that if V and W are vector spaces of the same finite dimension n, then a linear '
                    'transformation T: V → W is one-to-one if and only if it is onto.',
        'steps': [   (   'Step 1: State the Rank-Nullity formula',
                         'By the Rank-Nullity Theorem:<br>dim(V) = rank(T) + nullity(T)<br>n = rank(T) + nullity(T)  '
                         '--- (1).',
                         'Execute step 1: state the rank-nullity formula to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Prove Forward Implication (One-to-One ⇒ Onto)',
                         'Assume T is one-to-one.<br>By Q117, ker(T) = {0}, so nullity(T) = dim(ker T) = '
                         '0.<br>Substitute nullity(T) = 0 into (1):<br>n = rank(T) + 0  ⇒  rank(T) = n.<br>Since '
                         'rank(T) = dim(Range T) = n = dim(W), the subspace Range(T) has the same dimension as the '
                         'ambient space W.<br>A subspace of dimension n inside a space of dimension n must be the '
                         'entire space:<br>Range(T) = W.<br>Therefore, T is ONTO.',
                         'Show that the kernel contains only the zero vector, which proves the transformation is '
                         'injective (one-to-one).'),
                     (   'Step 3: Prove Reverse Implication (Onto ⇒ One-to-One)',
                         'Assume T is onto.<br>Then Range(T) = W, so rank(T) = dim(Range T) = dim(W) = '
                         'n.<br>Substitute rank(T) = n into (1):<br>n = n + nullity(T)  ⇒  nullity(T) = 0.<br>Since '
                         'nullity(T) = 0, ker(T) = {0}.<br>By Q117, this implies T is ONE-TO-ONE.',
                         'Show that the kernel contains only the zero vector, which proves the transformation is '
                         'injective (one-to-one).'),
                     (   'Step 4: Conclude the theorem',
                         'Both implications hold. Thus, T is one-to-one if and only if it is onto. Hence proved.',
                         'Execute step 4: conclude the theorem to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Equivalence of One-to-One and Onto for Equal Finite Dimensions'},
    {   'concept': 'M₂₂(ℝ) is a 4-dimensional vector space. A + Aᵀ = 0 means Aᵀ = -A (skew-symmetric). Thus ker(T) is '
                   'the subspace of skew-symmetric matrices.',
        'difficulty': 'Exam-Level',
        'final_answer': 'T is linear;  Kernel Basis: { [[0, 1], [-1, 0]] }, Nullity = 1;  Rank = 3',
        'formula': 'T(A + B) = (A + B) + (A + B)ᵀ;  T(c A) = c T(A);  dim(M₂₂) = 4.',
        'formula_expl': 'ker(T) = {A : Aᵀ = -A}; Range(T) = {A : Aᵀ = A}.',
        'given': 'T: M₂₂(ℝ) → M₂₂(ℝ), T(A) = A + Aᵀ.',
        'meaning_en': 'Verify linearity for matrix operation A + Aᵀ, find which matrices satisfy A + Aᵀ = 0 '
                      '(skew-symmetric matrices), and find rank and nullity.',
        'mistakes': [   ('Thinking dim(M₂₂) = 2.', 'M₂₂(ℝ) has 4 entries, so its dimension is 2 × 2 = 4!'),
                        (   'Missing the condition a = 0 and d = 0 for skew-symmetric.',
                            'Diagonal entries of a skew-symmetric matrix must be zero: a = -a ⇒ 2a = 0 ⇒ a = 0.')],
        'num': 119,
        'practice_q': 'Find rank and nullity of T(A) = A - Aᵀ on M₂₂(ℝ).',
        'presentation': [   'Show T(A+B) = T(A)+T(B) and T(cA) = cT(A).',
                            'Show A + Aᵀ = 0 gives Aᵀ = -A (skew-symmetric).',
                            'Extract basis matrix for ker(T).',
                            'Apply Rank-Nullity: Rank = 4 - 1 = 3.'],
        'question': 'Let T: M₂₂(ℝ) → M₂₂(ℝ) be defined by T(A) = A + Aᵀ. Show that T is a linear transformation, find '
                    'a basis for its Kernel, and find its Rank and Nullity.',
        'steps': [   (   'Step 1: Verify Linearity of T',
                         '• T(A + B) = (A + B) + (A + B)ᵀ = A + B + Aᵀ + Bᵀ = (A + Aᵀ) + (B + Bᵀ) = T(A) + T(B).<br>• '
                         'T(c A) = (c A) + (c A)ᵀ = c A + c Aᵀ = c (A + Aᵀ) = c T(A).<br>Therefore, T is a LINEAR '
                         'TRANSFORMATION.',
                         'Verify that the mapping preserves vector addition T(u + v) = T(u) + T(v) and scalar scaling '
                         'T(cu) = c T(u).'),
                     (   'Step 2: Find the Kernel of T',
                         'T(A) = O  ⇒  A + Aᵀ = O  ⇒  Aᵀ = -A.<br>Thus, ker(T) is the set of all 2×2 SKEW-SYMMETRIC '
                         'matrices.<br>For A = [[a, b], [c, d]]: Aᵀ = -A implies a = 0, d = 0, and c = -b.<br>A = [ '
                         '[0, b], [-b, 0] ] = b [ [0, 1], [-1, 0] ].<br>Basis for ker(T): B_ker = { [ [0, 1], [-1, 0] '
                         '] }.<br>Nullity(T) = dim(ker T) = 1.',
                         'Find all input vectors that map to the zero vector by setting T(v) = 0 and solving the '
                         'resulting homogeneous system.'),
                     (   'Step 3: Find Rank(T) using Rank-Nullity Theorem',
                         'dim(Domain M₂₂) = 2 · 2 = 4.<br>rank(T) = dim(M₂₂) - nullity(T) = 4 - 1 = 3.',
                         'Execute step 3: find rank(t) using rank-nullity theorem to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Identify Range(T)',
                         'Since (A + Aᵀ)ᵀ = Aᵀ + (Aᵀ)ᵀ = Aᵀ + A = A + Aᵀ, every output of T is a SYMMETRIC '
                         'matrix!<br>The space of 2×2 symmetric matrices has dimension 3 (from Q89).<br>Matches Rank = '
                         '3 exactly!',
                         'Determine the subspace spanned by the images of the domain basis vectors to construct the '
                         'range.')],
        'title': 'Linear Transformation on Matrix Space M₂₂(ℝ): Trace and Transpose'},
    {   'concept': 'A composition cannot recover lost information. Applying T first squashes the domain into Range(T) '
                   '⊆ V, and applying S can only further reduce dimension.',
        'difficulty': 'Exam-Level',
        'final_answer': 'rank(S ∘ T) ≤ min(rank S, rank T) and nullity(S ∘ T) ≤ nullity(T) + nullity(S) (Both proved)',
        'formula': 'Range(S ∘ T) = S(Range T) ⊆ Range(S);  ker(T) ⊆ ker(S ∘ T).',
        'formula_expl': 'Subspace inclusions directly imply dimension inequalities.',
        'given': 'T: U → V, S: V → W.',
        'meaning_en': 'Prove the fundamental inequalities governing how dimension is lost when linear transformations '
                      'are composed.',
        'mistakes': [   ('Claiming rank(ST) = rank(S) · rank(T).', 'Rank is dimension (addition), NOT multiplication!'),
                        (   'Assuming ker(S ∘ T) = ker(T).',
                            'ker(S ∘ T) contains ker(T), but can be strictly larger if Range(T) hits ker(S)!')],
        'num': 120,
        'practice_q': 'If A is 3×4 and B is 4×2, what is the maximum possible rank of AB?',
        'presentation': [   'Show Range(ST) ⊆ Range(S).',
                            'Use Rank-Nullity on restricted map S|_{Range T}.',
                            'Combine to state min(rank S, rank T).',
                            'State nullity inequality.'],
        'question': 'Prove that for two linear transformations T: U → V and S: V → W: (i) rank(S ∘ T) ≤ min(rank S, '
                    'rank T), and (ii) nullity(S ∘ T) ≤ nullity(T) + nullity(S).',
        'steps': [   (   'Step 1: Prove rank(S ∘ T) ≤ rank(S)',
                         'By definition, Range(S ∘ T) = { S(T(u)) : u ∈ U } = S(Range T).<br>Since Range(T) ⊆ V: '
                         'S(Range T) ⊆ S(V) = Range(S).<br>Since Range(S ∘ T) is a subspace of '
                         'Range(S):<br>dim(Range(S ∘ T)) ≤ dim(Range(S))<br>⇒  rank(S ∘ T) ≤ rank(S)  --- (1).',
                         'Execute step 1: prove rank(s ∘ t) ≤ rank(s) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Prove rank(S ∘ T) ≤ rank(T)',
                         'Consider the restriction of S to Range(T), denoted S|_{Range T} : Range(T) → W.<br>The image '
                         'of this restricted map is Range(S ∘ T).<br>By the Rank-Nullity theorem on the restricted '
                         'map:<br>dim(Range T) = dim(Image S|_{Range T}) + dim(ker S|_{Range T})<br>rank(T) = rank(S ∘ '
                         'T) + nullity(S|_{Range T}).<br>Since nullity is non-negative (≥ 0):<br>rank(S ∘ T) ≤ '
                         'rank(T)  --- (2).',
                         'Execute step 2: prove rank(s ∘ t) ≤ rank(t) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Combine equations (1) and (2)',
                         'From (1) and (2):<br>rank(S ∘ T) ≤ min( rank(S), rank(T) ). Proved!',
                         'Execute step 3: combine equations (1) and (2) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Prove nullity(S ∘ T) ≤ nullity(T) + nullity(S)',
                         'Let u ∈ ker(T) ⇒ T(u) = 0 ⇒ S(T(u)) = S(0) = 0 ⇒ u ∈ ker(S ∘ T).<br>Thus ker(T) ⊆ ker(S ∘ '
                         'T).<br>The dimension of ker(S ∘ T) restricted to V gives:<br>nullity(S ∘ T) = nullity(T) + '
                         'dim(Range T ∩ ker S) ≤ nullity(T) + nullity(S). Hence proved!',
                         'Execute step 4: prove nullity(s ∘ t) ≤ nullity(t) + nullity(s) to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': "Rank and Nullity of Composite Linear Transformation (Sylvester's Inequality)"},
    {   'concept': 'Shift operator in polynomial spaces. Represents Taylor shift algebraically as an upper triangular '
                   'Pascal matrix.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Matrix [T]_B = [[1, 1, 1], [0, 1, 2], [0, 0, 1]]',
        'formula': 'T(1) = 1;  T(x) = x + 1;  T(x²) = (x + 1)² = x² + 2x + 1.',
        'formula_expl': 'Expansion coefficients become column entries.',
        'given': 'T: P₂ → P₂, T(p(x)) = p(x + 1), B = {1, x, x²}.',
        'meaning_en': 'Evaluate T on 1, x, x² (substituting x → x + 1), expand in powers of x, and construct the 3×3 '
                      'upper triangular matrix.',
        'mistakes': [   (   'Reversing the order of basis: writing powers as x², x, 1.',
                            'The basis is given as {1, x, x²}, so row 1 is constant, row 2 is x, row 3 is x²!'),
                        ('Expanding (x + 1)² incorrectly.', '(x + 1)² = x² + 2x + 1.')],
        'num': 121,
        'practice_q': 'Find the matrix of T(p(x)) = p(2x + 1) relative to {1, x, x²}.',
        'presentation': [   'Evaluate T on 1, x, x².',
                            'Show expansion in basis {1, x, x²}.',
                            'Form 3×3 matrix with coordinate columns.'],
        'question': 'Find the matrix of the linear operator T: P₂ → P₂ defined by T(p(x)) = p(x + 1) relative to the '
                    'standard basis B = {1, x, x²}.',
        'steps': [   (   'Step 1: Apply T to basis vector 1',
                         'T(1) = 1 = 1(1) + 0(x) + 0(x²).<br>Column 1: [1, 0, 0]ᵀ.',
                         'Execute step 1: apply t to basis vector 1 to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Apply T to basis vector x',
                         'T(x) = x + 1 = 1(1) + 1(x) + 0(x²).<br>Column 2: [1, 1, 0]ᵀ.',
                         'Execute step 2: apply t to basis vector x to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 3: Apply T to basis vector x²',
                         'T(x²) = (x + 1)² = x² + 2x + 1 = 1(1) + 2(x) + 1(x²).<br>Column 3: [1, 2, 1]ᵀ.',
                         'Execute step 3: apply t to basis vector x² to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 4: Assemble the matrix [T]_B',
                         '[T]_B = [ [1, 1, 1], [0, 1, 2], [0, 0, 1] ].',
                         'Execute step 4: assemble the matrix [t]_b to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 5: Properties of the matrix',
                         'Notice this is an upper triangular matrix with 1s on the diagonal (Pascal '
                         'matrix).<br>det([T]) = 1 · 1 · 1 = 1 ≠ 0, so T is an isomorphism '
                         '(invertible)!<br>Eigenvalues are all λ = 1.',
                         'Execute step 5: properties of the matrix to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Matrix Representation on Polynomial Space with Quadratic Basis'},
    {   'concept': 'We can construct a linear transformation by specifying its action on a basis: assign T(v₁) = 0 for '
                   'v₁ spanning the kernel, and assign T(v₂) and T(v₃) to span the image.',
        'difficulty': 'Exam-Level',
        'final_answer': 'T(x, y, z) = (-2x + y + z, -2x + 2z, -y + z)  (or standard matrix [[-2, 1, 1], [-2, 0, 2], '
                        '[0, -1, 1]])',
        'formula': 'B = {v₁, v₂, v₃} basis of ℝ³; T(v₁) = 0, T(v₂) = w₁, T(v₃) = w₂.',
        'formula_expl': 'v₁ = (1, 1, 1), w₁ = (1, 0, -1), w₂ = (1, 2, 1).',
        'given': 'ker(T) = span{(1, 1, 1)}; Im(T) = span{(1, 0, -1), (1, 2, 1)}.',
        'meaning_en': 'Extend the kernel basis to a basis of ℝ³, assign output values in the image, and solve for the '
                      'standard matrix.',
        'mistakes': [   (   'Choosing dependent vectors to extend the basis.',
                            'Verify det [v₁ v₂ v₃] ≠ 0 when extending the basis!'),
                        ('Assigning non-zero image to (1, 1, 1).', 'Any vector in the kernel MUST map to (0, 0, 0).')],
        'num': 122,
        'practice_q': 'Find a linear transformation T: ℝ³ → ℝ³ whose kernel is spanned by (1, 0, 0) and (0, 1, 0).',
        'presentation': [   'Extend kernel vector to a full basis.',
                            'Assign image vectors to the non-kernel basis vectors.',
                            'Solve for T(e₁), T(e₂), T(e₃).',
                            'Write final formula and verify.'],
        'question': 'Find a linear transformation T: ℝ³ → ℝ³ whose Kernel is spanned by (1, 1, 1) and whose Image is '
                    'spanned by (1, 0, -1) and (1, 2, 1).',
        'steps': [   (   'Step 1: Choose a basis for ℝ³ containing (1, 1, 1)',
                         'Let v₁ = (1, 1, 1) (basis for kernel).<br>Choose v₂ = (0, 1, 0) and v₃ = (0, 0, 1) to extend '
                         'to a basis of ℝ³.<br>Matrix [v₁ | v₂ | v₃] has det = 1 ≠ 0, so {v₁, v₂, v₃} is a valid '
                         'basis.',
                         'Execute step 1: choose a basis for ℝ³ containing (1, 1, 1) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Assign images to basis vectors',
                         '• T(v₁) = T(1, 1, 1) = (0, 0, 0) (must be zero for kernel)<br>• T(v₂) = T(0, 1, 0) = (1, 0, '
                         '-1)<br>• T(v₃) = T(0, 0, 1) = (1, 2, 1).',
                         'Determine the subspace spanned by the images of the domain basis vectors to construct the '
                         'range.'),
                     (   'Step 3: Find T(1, 0, 0) = T(e₁)',
                         'Notice that (1, 0, 0) = v₁ - v₂ - v₃ = (1, 1, 1) - (0, 1, 0) - (0, 0, 1).<br>Applying '
                         'T:<br>T(1, 0, 0) = T(v₁) - T(v₂) - T(v₃)<br>= (0, 0, 0) - (1, 0, -1) - (1, 2, 1)<br>= (-1 - '
                         '1, 0 - 2, 1 - 1) = (-2, -2, 0).',
                         'Execute step 3: find t(1, 0, 0) = t(e₁) to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 4: Write the general formula for T(x, y, z)',
                         '(x, y, z) = x (1, 0, 0) + y (0, 1, 0) + z (0, 0, 1).<br>T(x, y, z) = x (-2, -2, 0) + y (1, '
                         '0, -1) + z (1, 2, 1)<br>= ( -2x + y + z, -2x + 2z, -y + z ).',
                         'Execute step 4: write the general formula for t(x, y, z) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: Verify Kernel condition',
                         'T(1, 1, 1) = ( -2(1) + 1 + 1, -2(1) + 2(1), -1 + 1 ) = (0, 0, 0). Verified!',
                         'Find all input vectors that map to the zero vector by setting T(v) = 0 and solving the '
                         'resulting homogeneous system.')],
        'title': 'Finding Linear Transformation from Kernel and Image Specifications'},
    {   'concept': 'Projections decompose the entire vector space into the subspace being projected onto Range(T) and '
                   'the direction of projection along Kernel(T).',
        'difficulty': 'Exam-Level',
        'final_answer': 'V = Range(T) ⊕ Kernel(T) (Direct sum); Eigenvalues of T are strictly λ = 0 or λ = 1 (Hence '
                        'proved)',
        'formula': 'v = T(v) + (v - T(v));  Range ∩ Kernel = {0}.',
        'formula_expl': 'T(T(v)) = T(v) ⇒ T(v - T(v)) = T(v) - T²(v) = 0.',
        'given': 'T: V → V linear, T² = T.',
        'meaning_en': 'Prove that every vector can be uniquely decomposed as v = T(v) + (v - T(v)) and that the '
                      'operator polynomial λ² - λ = 0 restricts eigenvalues to {0, 1}.',
        'mistakes': [   (   'Proving V = Range + Kernel without showing intersection is {0}.',
                            'A DIRECT SUM ⊕ strictly requires showing Range ∩ Kernel = {0}!'),
                        (   'Assuming T is invertible.',
                            'T² = T with T ≠ I has det(T) = 0, so projections are not invertible.')],
        'num': 123,
        'practice_q': 'Prove that if T² = I (involution/reflection), then its only possible eigenvalues are 1 and -1.',
        'presentation': [   'Show v = T(v) + (v - T(v)).',
                            'Show T(v - T(v)) = 0.',
                            'Show Range ∩ Kernel = {0} to prove direct sum ⊕.',
                            'Show (λ² - λ)v = 0 to prove eigenvalues 0 and 1.'],
        'question': 'Prove that if T: V → V is a linear operator satisfying T² = T (projection), then: (i) V = '
                    'Range(T) ⊕ Kernel(T) (direct sum), and (ii) The only possible eigenvalues of T are 0 and 1.',
        'steps': [   (   'Step 1: Prove v - T(v) belongs to Kernel(T)',
                         'For any vector v ∈ V, consider u = v - T(v).<br>Applying T:<br>T(u) = T(v - T(v)) = T(v) - '
                         'T²(v).<br>Since T² = T: T(v) - T(v) = 0.<br>Therefore, (v - T(v)) ∈ ker(T) for all v ∈ V.',
                         'Find all input vectors that map to the zero vector by setting T(v) = 0 and solving the '
                         'resulting homogeneous system.'),
                     (   'Step 2: Show V = Range(T) + Kernel(T)',
                         'Any vector v can be written as:<br>v = T(v) + (v - T(v)).<br>Here T(v) ∈ Range(T) and (v - '
                         'T(v)) ∈ ker(T).<br>Thus, every vector in V is the sum of a vector in Range(T) and a vector '
                         'in ker(T): V = Range(T) + ker(T).',
                         'Find all input vectors that map to the zero vector by setting T(v) = 0 and solving the '
                         'resulting homogeneous system.'),
                     (   'Step 3: Show Range(T) ∩ Kernel(T) = {0}',
                         'Let w ∈ Range(T) ∩ ker(T).<br>• Since w ∈ Range(T): w = T(x) for some x ∈ V.<br>• Since w ∈ '
                         'ker(T): T(w) = 0.<br>Substitute w = T(x) into T(w) = 0:<br>T(T(x)) = 0  ⇒  T²(x) = '
                         '0.<br>Since T² = T: T(x) = 0.<br>Therefore: w = T(x) = 0.<br>Thus, Range(T) ∩ ker(T) = {0}.',
                         'Find all input vectors that map to the zero vector by setting T(v) = 0 and solving the '
                         'resulting homogeneous system.'),
                     (   'Step 4: Prove Eigenvalues of T are strictly 0 or 1',
                         'Let λ be an eigenvalue of T with non-zero eigenvector v:<br>T(v) = λ v.<br>Applying T again: '
                         'T²(v) = T(λ v) = λ T(v) = λ (λ v) = λ² v.<br>Since T² = T:<br>T²(v) = T(v)  ⇒  λ² v = λ v  '
                         '⇒  (λ² - λ) v = 0.<br>Since v ≠ 0 (eigenvector):<br>λ² - λ = 0  ⇒  λ(λ - 1) = 0  ⇒  λ = 0  '
                         'or  λ = 1. Proved!',
                         'Execute step 4: prove eigenvalues of t are strictly 0 or 1 to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Idempotent Transformation (Projection) Properties'},
    {   'concept': 'Matrix multiplication is generally non-commutative (AB ≠ BA), reflecting the physical fact that '
                   'spatial transformations yield different outcomes when their sequence is reversed.',
        'difficulty': 'Exam-Level',
        'final_answer': '[R ∘ M] = [[-1, 0], [0, 1]]  ≠  [M ∘ R] = [[1, 0], [0, -1]] (Transformations do not commute)',
        'formula': '[R] = [[0, -1], [1, 0]];  [M] = [[0, 1], [1, 0]].',
        'formula_expl': 'Line y = x swaps x and y coordinates.',
        'given': 'R = 90° rotation, M = reflection across y = x.',
        'meaning_en': 'Show that the order of performing 2D geometric operations matters by proving [R][M] ≠ [M][R].',
        'mistakes': [   (   'Wrong matrix for reflection across y = x.',
                            'Swapping x and y gives matrix [[0, 1], [1, 0]], NOT [[1, 0], [0, -1]]!'),
                        ('Arithmetic error in matrix multiplication.', 'Check: (-1)(1) = -1.')],
        'num': 124,
        'practice_q': 'Check whether rotation by 90° and rotation by 180° commute.',
        'presentation': [   'State standard matrices [R] and [M].',
                            'Compute [R][M] step by step.',
                            'Compute [M][R] step by step.',
                            'Show that the matrices differ and conclude non-commutativity.'],
        'question': 'In ℝ², let R be counterclockwise rotation by 90° and M be reflection across the line y = x. Find '
                    'the standard matrices [R] and [M], compute [R ∘ M] and [M ∘ R], and show that R and M do not '
                    'commute.',
        'steps': [   (   'Step 1: Determine Matrix [R] for 90° rotation',
                         'R(1, 0) = (0, 1),   R(0, 1) = (-1, 0).<br>[R] = [ [0, -1], [1, 0] ].',
                         'Execute step 1: determine matrix [r] for 90° rotation to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Determine Matrix [M] for reflection across y = x',
                         'M(1, 0) = (0, 1),   M(0, 1) = (1, 0).<br>[M] = [ [0, 1], [1, 0] ].',
                         'Execute step 2: determine matrix [m] for reflection across y = x to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Compute [R ∘ M] = [R] · [M]',
                         '[R] [M] = [ [0, -1], [1, 0] ] [ [0, 1], [1, 0] ]<br>= [ [0(0) + (-1)(1), 0(1) + (-1)(0)], '
                         '[1(0) + 0(1), 1(1) + 0(0)] ]<br>= [ [-1, 0], [0, 1] ].<br>(This is reflection across the '
                         'y-axis!).',
                         'Execute step 3: compute [r ∘ m] = [r] · [m] to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Compute [M ∘ R] = [M] · [R]',
                         '[M] [R] = [ [0, 1], [1, 0] ] [ [0, -1], [1, 0] ]<br>= [ [0(0) + 1(1), 0(-1) + 1(0)], [1(0) + '
                         '0(1), 1(-1) + 0(0)] ]<br>= [ [1, 0], [0, -1] ].<br>(This is reflection across the x-axis!).',
                         'Execute step 4: compute [m ∘ r] = [m] · [r] to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 5: Compare results and conclude non-commutativity',
                         'Since [R ∘ M] = [ [-1, 0], [0, 1] ] ≠ [M ∘ R] = [ [1, 0], [0, -1] ]:<br>[R ∘ M] ≠ [M ∘ '
                         'R].<br>Therefore, rotation by 90° and reflection across y = x DO NOT COMMUTE. Hence proved.',
                         'Execute step 5: compare results and conclude non-commutativity to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Non-Commutativity of Geometric Transformations (Rotation vs Reflection)'},
    {   'concept': 'For underdetermined systems (m < n), rank(A) ≤ m < n. By Rank-Nullity, nullity(A) = n - rank(A) ≥ '
                   'n - m > 0, which guarantees that non-trivial solutions to AX = 0 always exist, meaning solutions '
                   'are either non-existent or infinite.',
        'difficulty': 'Exam-Level',
        'final_answer': 'When m < n, nullity(A) ≥ n - m > 0, so AX = B can only have infinite solutions or no '
                        'solution; a unique solution is possible ONLY IF m ≥ n (Hence proved)',
        'formula': 'nullity(A) = n - rank(A) ≥ n - m.',
        'formula_expl': 'If m < n, nullity(A) ≥ 1, so there is at least 1 free parameter.',
        'given': 'System AX = B, A is m×n matrix, m < n.',
        'meaning_en': 'Explain why underdetermined systems (m < n) with fewer equations than unknowns can NEVER have a '
                      'unique solution.',
        'mistakes': [   (   'Confusing rows m with columns n.',
                            'm = number of equations (rows), n = number of variables (columns).'),
                        (   'Claiming m < n always means infinite solutions.',
                            "Remember: the system might be INCONSISTENT (no solution)! State 'either no solution or "
                            "infinite solutions'.")],
        'num': 125,
        'practice_q': 'Explain using Rank-Nullity theorem why a homogeneous system of 3 equations in 5 variables '
                      'always has non-trivial solutions.',
        'presentation': [   'Define T_A: ℝⁿ → ℝᵐ.',
                            'Apply Rank-Nullity Theorem: n = rank + nullity.',
                            'Show rank ≤ m implies nullity ≥ n - m > 0.',
                            'Explain why nullity > 0 rules out unique solutions.'],
        'question': 'Use the Rank-Nullity Theorem to prove that a system of m linear equations in n variables AX = B '
                    'can have a unique solution only if m ≥ n (number of equations is at least the number of '
                    'unknowns).',
        'steps': [   (   'Step 1: Set up the matrix transformation T_A',
                         'Let T_A: ℝⁿ → ℝᵐ be defined by T_A(X) = A X.<br>Domain dimension = n (number of '
                         'variables).<br>Codomain dimension = m (number of equations).',
                         'Execute step 1: set up the matrix transformation t_a to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Apply the Rank-Nullity Theorem',
                         'By the Rank-Nullity Theorem:<br>dim(Domain) = rank(T_A) + nullity(T_A)<br>n = rank(A) + '
                         'nullity(A)<br>⇒  nullity(A) = n - rank(A)  --- (1).',
                         'Execute step 2: apply the rank-nullity theorem to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Bound the rank of matrix A',
                         'The rank of an m×n matrix cannot exceed the number of rows: rank(A) ≤ m.<br>Since m < n '
                         '(fewer equations than variables):<br>rank(A) ≤ m < n.',
                         'Execute step 3: bound the rank of matrix a to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 4: Analyze nullity(A)',
                         'Substitute rank(A) ≤ m into (1):<br>nullity(A) = n - rank(A) ≥ n - m.<br>Since m < n: n - m '
                         '> 0  ⇒  nullity(A) ≥ 1.<br>Therefore, the null space Null(A) = ker(T_A) contains NON-ZERO '
                         'vectors.',
                         'Execute step 4: analyze nullity(a) to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 5: Conclude solution behavior for AX = B',
                         'If AX = B is inconsistent, it has NO solution.<br>If AX = B is consistent with a particular '
                         'solution X_p, then any vector of the form X = X_p + X_h (where X_h ∈ Null(A)) is also a '
                         'solution.<br>Since nullity(A) ≥ 1, there are infinitely many vectors X_h.<br>Therefore, AX = '
                         'B has INFINITELY MANY solutions.<br>In no case can it have a UNIQUE solution when m < '
                         'n.<br>Hence, a unique solution can exist ONLY IF m ≥ n. Hence proved!',
                         'Execute step 5: conclude solution behavior for ax = b to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Application of Rank-Nullity Theorem: Systems of Linear Equations'}]


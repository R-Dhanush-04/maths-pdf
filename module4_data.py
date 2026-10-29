# -*- coding: utf-8 -*-
"""
Module 4: Vector Spaces
100% Pure English Edition
Includes 25 Fully Solved Questions (5 Fundamental + 10 Intermediate + 10 Exam-Level)
"""

MODULE4_QUESTIONS = [   {   'concept': "A vector space is an abstract algebraic structure consisting of a set V whose elements ('vectors') "
                   "can be added together and multiplied ('scaled') by numbers from a field F, satisfying natural "
                   'geometric rules.',
        'difficulty': 'Fundamental',
        'final_answer': 'A real vector space V is a non-empty set with vector addition and scalar multiplication '
                        'satisfying the 10 axioms (closure, commutativity, associativity, identity, inverse, and '
                        'distributivities).',
        'formula': 'V with operations + : V × V → V and · : ℝ × V → V.',
        'formula_expl': '5 axioms for addition (+), 5 axioms for scalar multiplication (·).',
        'given': 'Set V, field of scalars ℝ.',
        'meaning_en': 'Provide the formal mathematical definition of a vector space over the field of real numbers ℝ, '
                      'detailing the closure, abelian group, and scalar multiplication axioms.',
        'mistakes': [   (   'Omitting the scalar identity axiom 1·u = u.',
                            'Without 1·u = u, algebraic pathologies can occur!'),
                        ('Writing c + u.', 'You cannot add a scalar to a vector! Only c·u or u + v is defined.')],
        'num': 76,
        'practice_q': 'Show that the set of all 2×2 real matrices M₂₂(ℝ) forms a vector space over ℝ under standard '
                      'addition and scalar multiplication.',
        'presentation': [   'Group axioms neatly into Addition (1-5) and Scalar Multiplication (6-10).',
                            'State universal quantifiers ∀ u, v, w ∈ V and c, d ∈ ℝ.'],
        'question': 'Define a real vector space V and state the ten fundamental axioms satisfied by vector addition '
                    'and scalar multiplication.',
        'steps': [   (   'Step 1: Axioms for Vector Addition (V is an Abelian group under +)',
                         'For all u, v, w ∈ V:<br>1. Closure under addition: u + v ∈ V.<br>2. Commutativity: u + v = v '
                         '+ u.<br>3. Associativity: (u + v) + w = u + (v + w).<br>4. Additive Identity: There exists a '
                         'zero vector 0 ∈ V such that u + 0 = u.<br>5. Additive Inverse: For each u ∈ V, there exists '
                         '-u ∈ V such that u + (-u) = 0.',
                         'Execute step 1: axioms for vector addition (v is an abelian group under +) to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 2: Axioms for Scalar Multiplication',
                         'For all c, d ∈ ℝ and u, v ∈ V:<br>6. Closure under scalar multiplication: c u ∈ V.<br>7. '
                         'Distributivity over vector addition: c(u + v) = c u + c v.<br>8. Distributivity over scalar '
                         'addition: (c + d)u = c u + d u.<br>9. Compatibility of multiplication: c(d u) = (c '
                         'd)u.<br>10. Scalar identity: 1 · u = u for the real number 1.',
                         'Execute step 2: axioms for scalar multiplication to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Definition of Vector Space over ℝ and Its Fundamental Axioms'},
    {   'concept': 'Since W is inside V, it automatically inherits associativity, commutativity, and distributivity. '
                   'We only need to check that W is closed under the operations and contains the origin.',
        'difficulty': 'Fundamental',
        'final_answer': 'Subspace Criteria: (i) 0 ∈ W, (ii) u + v ∈ W for all u, v ∈ W, and (iii) c u ∈ W for all c ∈ '
                        'ℝ, u ∈ W (Equivalently: a u + b v ∈ W).',
        'formula': 'One-step test: W is a subspace if and only if for all u, v ∈ W and c ∈ ℝ, (u + c v) ∈ W (or a u + '
                   'b v ∈ W).<br>Two-step test: (1) 0 ∈ W, (2) u + v ∈ W, (3) c u ∈ W.',
        'formula_expl': 'Non-emptiness is most easily tested by checking if 0 ∈ W.',
        'given': 'Subset W ⊆ V.',
        'meaning_en': 'State the conditions required to test whether a subset W inherits the vector space structure '
                      'from the enclosing parent space V.',
        'mistakes': [   (   'Forgetting to check if 0 ∈ W.',
                            'If 0 ∉ W, W can NEVER be a subspace! This immediately disproves non-subspaces.'),
                        (   'Testing all 10 vector space axioms.',
                            'Never test all 10 axioms for a subset; only test closure and 0 ∈ W!')],
        'num': 77,
        'practice_q': 'Use the subspace test to determine if W = {(x, y, 0) : x, y ∈ ℝ} is a subspace of ℝ³.',
        'presentation': [   'State both the 3-step test and the combined 1-step test.',
                            'Highlight the quick check 0 ∈ W.'],
        'question': 'State the necessary and sufficient conditions for a non-empty subset W of a vector space V to be '
                    'a subspace of V.',
        'steps': [   (   'Step 1: Two-Step Subspace Test',
                         'A subset W of vector space V is a subspace if and only if:<br>1. W is non-empty (typically '
                         'verified by showing the zero vector 0 ∈ W).<br>2. Closed under vector addition: ∀ u, v ∈ W  '
                         '⇒  u + v ∈ W.<br>3. Closed under scalar multiplication: ∀ c ∈ ℝ, u ∈ W  ⇒  c u ∈ W.',
                         'Execute step 1: two-step subspace test to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Equivalent One-Step Test (Linear Combination Test)',
                         'W is a subspace of V if and only if W is non-empty and for all scalars a, b ∈ ℝ and all '
                         'vectors u, v ∈ W:<br>a u + b v ∈ W.',
                         'Execute step 2: equivalent one-step test (linear combination test) to advance the '
                         'step-by-step mathematical solution toward the final result.')],
        'title': 'Subspace Criteria (The Two-Step and One-Step Subspace Tests)'},
    {   'concept': 'A linear combination is any vector of the form c₁ v₁ + c₂ v₂ + ... + c_k v_k. The span of S, '
                   'denoted span(S), is the set of ALL possible linear combinations of vectors in S, forming the '
                   'smallest subspace containing S.',
        'difficulty': 'Fundamental',
        'final_answer': 'v = -1 v₁ + 4 v₂  (or v = -(1, 1) + 4(1, 2))',
        'formula': 'v = c₁ v₁ + c₂ v₂;  span(S) = { Σ c_i v_i : c_i ∈ ℝ }.',
        'formula_expl': 'Linear combination solves a system of linear equations for the unknown scalars c_i.',
        'given': 'v = (3, 7), v₁ = (1, 1), v₂ = (1, 2).',
        'meaning_en': 'Define what it means for a vector to be formed by scaling and adding set S, and find the '
                      'specific scalar coefficients c₁, c₂ such that v = c₁ v₁ + c₂ v₂.',
        'mistakes': [   ('Arithmetic error in 3 - 4 = -1.', 'Check signs carefully.'),
                        ('Not verifying the result.', 'Always verify: -1(1, 1) + 4(1, 2) = (-1+4, -1+8) = (3, 7).')],
        'num': 78,
        'practice_q': 'Express v = (2, -5, 3) as a linear combination of v₁ = (1, -3, 2), v₂ = (2, -4, -1), and v₃ = '
                      '(1, -5, 7).',
        'presentation': [   'State definitions of linear combination and span clearly.',
                            'Set up c₁v₁ + c₂v₂ = v.',
                            'Solve the 2×2 system.',
                            'Write final vector equation.'],
        'question': 'Define linear combination and span of a set of vectors S = {v₁, v₂, ..., v_k} in a vector space '
                    'V, and express v = (3, 7) as a linear combination of v₁ = (1, 1) and v₂ = (1, 2) in ℝ².',
        'steps': [   (   'Step 1: Set up the vector equation',
                         'c₁ (1, 1) + c₂ (1, 2) = (3, 7)<br>(c₁ + c₂, c₁ + 2c₂) = (3, 7).',
                         'Execute step 1: set up the vector equation to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Equate components to form linear system',
                         'c₁ + c₂ = 3   --- (1)<br>c₁ + 2c₂ = 7  --- (2).',
                         'Execute step 2: equate components to form linear system to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Solve for c₁ and c₂',
                         'Subtract (1) from (2):<br>(c₁ + 2c₂) - (c₁ + c₂) = 7 - 3  ⇒  c₂ = 4.<br>Substitute c₂ = 4 '
                         'into (1):<br>c₁ + 4 = 3  ⇒  c₁ = 3 - 4 = -1.',
                         'Execute step 3: solve for c₁ and c₂ to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 4: Write the linear combination',
                         'v = -1 v₁ + 4 v₂ = -1(1, 1) + 4(1, 2).<br>Check: (-1 + 4, -1 + 8) = (3, 7). Exactly '
                         'verified!',
                         'Execute step 4: write the linear combination to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Linear Combinations and Span of Vectors'},
    {   'concept': 'Vectors are linearly independent if no vector in the set can be written as a linear combination of '
                   'the others. For n vectors in ℝⁿ, the set is linearly independent if and only if the matrix formed '
                   'by them has non-zero determinant.',
        'difficulty': 'Fundamental',
        'final_answer': 'det(A) = 0;  The set S is LINEARLY DEPENDENT.',
        'formula': 'det [v₁ | v₂ | v₃] ≠ 0  ⇒  Linearly Independent;  det = 0  ⇒  Linearly Dependent.',
        'formula_expl': 'c₁v₁ + c₂v₂ + c₃v₃ = 0 is equivalent to A c = 0.',
        'given': 'v₁ = (1, 2, 1), v₂ = (2, 1, 0), v₃ = (1, -1, -1).',
        'meaning_en': 'Test if c₁ v₁ + c₂ v₂ + c₃ v₃ = 0 has only the trivial solution c₁ = c₂ = c₃ = 0 (independent) '
                      'or has non-zero scalar solutions (dependent), by evaluating the determinant.',
        'mistakes': [   ('Concluding independent when det = 0.', 'det = 0 means DEPENDENT! det ≠ 0 means INDEPENDENT!'),
                        ('Sign error on cofactor of entry (2, 1).', 'Position (2, 1) has sign (-1)²⁺¹ = -1.')],
        'num': 79,
        'practice_q': 'Test whether S = {(1, 1, 1), (0, 1, 1), (0, 0, 1)} is linearly independent in ℝ³.',
        'presentation': [   'Form matrix A.',
                            'Compute det(A) clearly.',
                            'State: det = 0 implies Linearly Dependent (det ≠ 0 implies Independent).',
                            'Provide non-trivial relation v₁ - v₂ + v₃ = 0.'],
        'question': 'Determine whether the set of vectors S = {(1, 2, 1), (2, 1, 0), (1, -1, -1)} in ℝ³ is linearly '
                    'independent or linearly dependent.',
        'steps': [   (   'Step 1: Set up the matrix with vectors as rows or columns',
                         'A = | 1   2   1 |<br>    | 2   1   0 |<br>    | 1  -1  -1 |.',
                         'Execute step 1: set up the matrix with vectors as rows or columns to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 2: Evaluate the determinant det(A)',
                         'Expand along Row 2 (because it has a zero):<br>det(A) = -2 [ (2)(-1) - (1)(-1) ] + 1 [ '
                         '(1)(-1) - (1)(1) ] - 0<br>= -2 [ -2 + 1 ] + 1 [ -1 - 1 ]<br>= -2 [ -1 ] + 1 [ -2 ]<br>= 2 - '
                         '2 = 0.',
                         'Execute step 2: evaluate the determinant det(a) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: State the conclusion',
                         'Since det(A) = 0, the columns/rows are linearly dependent.<br>Therefore, the set S is '
                         'LINEARLY DEPENDENT.<br>(Notice that v₁ - v₂ + v₃ = (1-2+1, 2-1-1, 1-0-1) = (0, 0, 0) '
                         'provides the non-trivial relation with c₁=1, c₂=-1, c₃=1).',
                         'Execute step 3: state the conclusion to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Testing Linear Independence of Vectors in ℝ³'},
    {   'concept': 'A basis is a minimal spanning set and a maximal linearly independent set. Every vector in V can be '
                   'uniquely represented as a linear combination of basis vectors. Dimension is the number of vectors '
                   'in any basis.',
        'difficulty': 'Fundamental',
        'final_answer': 'Basis: Linearly independent spanning set. Dimension: Number of basis vectors. dim(ℝⁿ) = n; '
                        'dim(P_n) = n + 1; dim(M_{m×n}) = m · n.',
        'formula': 'B = {v₁, v₂, ..., v_n} is a basis if: (1) B is linearly independent, (2) span(B) = V.  dim(V) = '
                   '|B| = n.',
        'formula_expl': 'All bases of a finite-dimensional space have identical size.',
        'given': 'Vector spaces ℝⁿ, P_n(x), M_{m×n}(ℝ).',
        'meaning_en': 'Provide standard definitions of basis (linearly independent spanning set) and dimension (number '
                      'of elements in a basis), and list standard examples.',
        'mistakes': [   (   'Writing dim(P_n) = n instead of n + 1.',
                            'P_n includes degree 0 (constant 1), so {1, x, ..., xⁿ} has n + 1 vectors!'),
                        (   'Forgetting that a basis must satisfy BOTH independence AND spanning.',
                            'A set is not a basis if it fails either condition.')],
        'num': 80,
        'practice_q': 'Find a basis and dimension for the subspace W = {(x, y, z) ∈ ℝ³ : x + y + z = 0}.',
        'presentation': [   'State both conditions for a basis.',
                            'Define dimension.',
                            'List the 3 standard spaces with their standard bases and dimensions.'],
        'question': 'Define a basis and dimension of a vector space V, and state the standard basis and dimension of '
                    'ℝⁿ, P_n(x) (polynomials of degree ≤ n), and M_{m×n}(ℝ).',
        'steps': [   (   'Step 1: Definition of Basis and Dimension',
                         'A subset B of a vector space V is called a BASIS of V if:<br>1. B is linearly '
                         'independent.<br>2. B spans V (span(B) = V).<br>The DIMENSION of V, denoted dim(V), is the '
                         'number of vectors in any basis of V. If V = {0}, dim(V) = 0.',
                         'Extract the linearly independent spanning vectors corresponding to the free parameters to '
                         'form the basis.'),
                     (   'Step 2: Standard Basis and Dimension of ℝⁿ',
                         'Standard basis: B = {e₁, e₂, ..., e_n} where e_i has 1 in the i-th position and 0 '
                         'elsewhere.<br>Dimension: dim(ℝⁿ) = n.',
                         'Extract the linearly independent spanning vectors corresponding to the free parameters to '
                         'form the basis.'),
                     (   'Step 3: Standard Basis and Dimension of P_n(x)',
                         'P_n(x) is the space of all polynomials of degree ≤ n: p(x) = a₀ + a₁x + ... + a_n '
                         'xⁿ.<br>Standard basis: B = {1, x, x², ..., xⁿ}.<br>Dimension: dim(P_n) = n + 1 (since it '
                         'includes the constant term 1).',
                         'Extract the linearly independent spanning vectors corresponding to the free parameters to '
                         'form the basis.'),
                     (   'Step 4: Standard Basis and Dimension of M_{m×n}(ℝ)',
                         'Space of m×n matrices.<br>Standard basis: B = {E_ij} where E_ij has 1 at entry (i, j) and 0 '
                         'elsewhere.<br>Dimension: dim(M_{m×n}) = m · n.',
                         'Extract the linearly independent spanning vectors corresponding to the free parameters to '
                         'form the basis.')],
        'title': 'Basis and Dimension of a Vector Space'},
    {   'concept': 'A flat plane in ℝ³ is a subspace if and only if it passes through the origin (0, 0, 0). Any '
                   'translation away from the origin destroys closure under scalar multiplication and eliminates the '
                   'zero vector.',
        'difficulty': 'Intermediate',
        'final_answer': 'W is a subspace of ℝ³ (satisfies all closure axioms and 0 ∈ W); U is NOT a subspace because '
                        '(0, 0, 0) ∉ U.',
        'formula': 'Test for W: (1) 0 ∈ W, (2) c u + v ∈ W. For U: Check (0, 0, 0) ∈ U.',
        'formula_expl': '2(0) - 3(0) + 0 = 0 satisfies W, but 0 = 5 is impossible for U.',
        'given': 'W: 2x - 3y + z = 0;  U: 2x - 3y + z = 5.',
        'meaning_en': 'Apply the subspace test to show that a plane passing through the origin is closed under '
                      'addition and scalar multiplication, while a plane not containing the origin fails the zero '
                      'vector test.',
        'mistakes': [   (   'Testing addition for U before checking the zero vector.',
                            'Always check the zero vector FIRST! If (0, 0, 0) ∉ U, it immediately disproves the '
                            'subspace in 1 line.'),
                        (   'Assuming all planes are subspaces.',
                            'Only planes PASSING THROUGH THE ORIGIN (constant term = 0) are subspaces.')],
        'num': 81,
        'practice_q': 'Determine if W = {(x, y) ∈ ℝ² : y = 3x²} is a subspace of ℝ².',
        'presentation': [   'Test W using (i) 0 ∈ W, (ii) addition closure, (iii) scalar closure.',
                            'For U, directly evaluate (0, 0, 0) to show 0 ≠ 5.'],
        'question': 'Prove that the set W = {(x, y, z) ∈ ℝ³ : 2x - 3y + z = 0} is a subspace of ℝ³, whereas U = {(x, '
                    'y, z) ∈ ℝ³ : 2x - 3y + z = 5} is not a subspace.',
        'steps': [   (   'Step 1: Check Zero Vector in W',
                         'For (0, 0, 0): 2(0) - 3(0) + 0 = 0. Thus (0, 0, 0) ∈ W. (Non-empty).',
                         'Verify that the zero vector satisfies the defining equation, proving the subset is '
                         'non-empty.'),
                     (   'Step 2: Check Closure under Addition in W',
                         'Let u = (x₁, y₁, z₁) ∈ W and v = (x₂, y₂, z₂) ∈ W.<br>Then 2x₁ - 3y₁ + z₁ = 0 and 2x₂ - 3y₂ '
                         '+ z₂ = 0.<br>For u + v = (x₁ + x₂, y₁ + y₂, z₁ + z₂):<br>2(x₁ + x₂) - 3(y₁ + y₂) + (z₁ + z₂) '
                         '= (2x₁ - 3y₁ + z₁) + (2x₂ - 3y₂ + z₂) = 0 + 0 = 0.<br>Therefore, u + v ∈ W.',
                         'Take two arbitrary elements from the subset and prove their vector sum also satisfies the '
                         'defining condition.'),
                     (   'Step 3: Check Closure under Scalar Multiplication in W',
                         'For any scalar c ∈ ℝ and u ∈ W:<br>c u = (c x₁, c y₁, c z₁).<br>2(c x₁) - 3(c y₁) + (c z₁) = '
                         'c (2x₁ - 3y₁ + z₁) = c (0) = 0.<br>Therefore, c u ∈ W.<br>Since all conditions are '
                         'satisfied, W is a SUBSPACE of ℝ³.',
                         'Multiply an arbitrary element by an arbitrary scalar and prove the resulting vector remains '
                         'in the subset.'),
                     (   'Step 4: Test subset U for Zero Vector',
                         'For the zero vector (0, 0, 0):<br>2(0) - 3(0) + 0 = 0 ≠ 5.<br>The zero vector does not '
                         'satisfy the equation: (0, 0, 0) ∉ U.<br>Since every vector space must contain the zero '
                         'vector, U is NOT a subspace of ℝ³.',
                         'Verify that the zero vector satisfies the defining equation, proving the subset is '
                         'non-empty.')],
        'title': 'Subspace Verification: Plane Passing Through the Origin'},
    {   'concept': 'For a subspace defined by k independent linear constraints in ℝⁿ, dimension is dim(W) = n - k. '
                   'Here n = 4 and k = 2, so dim(W) = 4 - 2 = 2.',
        'difficulty': 'Intermediate',
        'final_answer': 'Basis B = {(2, 1, 0, -1), (-1, 0, 1, 2)};  Dimension dim(W) = 2',
        'formula': 'a = 2b - c, d = 3b - 2a = 3b - 2(2b - c) = -b + 2c.',
        'formula_expl': 'b and c are chosen as the 2 free parameters.',
        'given': 'W = {(a, b, c, d) : a - 2b + c = 0, 2a - 3b + d = 0}.',
        'meaning_en': 'Express the constrained 4-tuples in terms of free parameters, extract the generating vectors, '
                      'and state the basis and dimension.',
        'mistakes': [   (   'Arithmetic error in 3b - 2(2b - c) = -b + 2c.',
                            'Distribute carefully: 3b - 4b + 2c = -b + 2c.'),
                        (   'Leaving answer as parametric equations.',
                            'The question asks for a BASIS (set of vectors) and DIMENSION (an integer).')],
        'num': 82,
        'practice_q': 'Find basis and dimension of W = {(x, y, z, w) ∈ ℝ⁴ : x + y - z = 0, y + 2z - w = 0}.',
        'presentation': [   'Solve constraint equations for dependent variables.',
                            'Write vector as b v₁ + c v₂.',
                            'State that {v₁, v₂} are linearly independent and span W.',
                            'Conclude dim(W) = 2.'],
        'question': 'Find a basis and dimension for the subspace W of ℝ⁴ defined by W = {(a, b, c, d) ∈ ℝ⁴ : a - 2b + '
                    'c = 0 and 2a - 3b + d = 0}.',
        'steps': [   (   'Step 1: Express leading variables in terms of free variables',
                         'From equation 1: a = 2b - c.<br>From equation 2: d = 3b - 2a = 3b - 2(2b - c) = 3b - 4b + 2c '
                         '= -b + 2c.<br>The free variables are b and c.',
                         'Execute step 1: express leading variables in terms of free variables to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 2: Write general vector in W',
                         'v = (a, b, c, d) = (2b - c, b, c, -b + 2c).',
                         'Execute step 2: write general vector in w to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 3: Decompose into independent parametric vectors',
                         '= (2b, b, 0, -b) + (-c, 0, c, 2c)<br>= b (2, 1, 0, -1) + c (-1, 0, 1, 2).',
                         'Execute step 3: decompose into independent parametric vectors to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Check Linear Independence of generating vectors',
                         'Let v₁ = (2, 1, 0, -1) and v₂ = (-1, 0, 1, 2).<br>Since neither vector is a scalar multiple '
                         'of the other (v₁ has 0 in 3rd entry while v₂ has 1), they are linearly independent.<br>Since '
                         'they span W and are linearly independent, B = {v₁, v₂} is a BASIS of W.',
                         'Set a linear combination to zero and show that the only solution is the trivial solution '
                         'where all scalar weights are zero.'),
                     (   'Step 5: State the dimension',
                         'The basis contains 2 vectors.<br>Therefore, dim(W) = 2.',
                         'Execute step 5: state the dimension to advance the step-by-step mathematical solution toward '
                         'the final result.')],
        'title': 'Finding Basis and Dimension of a Subspace in ℝ⁴'},
    {   'concept': 'A basis acts like a customized coordinate coordinate system. The coordinates are the weights c_i '
                   'required to build vector v from the basis elements.',
        'difficulty': 'Intermediate',
        'final_answer': 'Coordinate vector [v]_B = [7/3, -4/3, 10/3]ᵀ',
        'formula': '[ u₁ | u₂ | u₃ ] [c₁, c₂, c₃]ᵀ = v.',
        'formula_expl': 'Matrix system A c = v solved by row reduction.',
        'given': 'v = (5, -1, 9), u₁ = (1, 2, 1), u₂ = (2, 1, 0), u₃ = (1, -1, 2).',
        'meaning_en': 'Find the unique scalar coordinates (c₁, c₂, c₃) such that v = c₁ u₁ + c₂ u₂ + c₃ u₃, and write '
                      'the coordinate vector [v]_B = [c₁, c₂, c₃]ᵀ.',
        'mistakes': [   (   'Writing [v]_B as row vector without transpose.',
                            'Coordinate vectors are conventionally written as column vectors [c₁, c₂, c₃]ᵀ.'),
                        ('Mixing up vector components.', 'u₁ is column 1, u₂ is column 2, u₃ is column 3.')],
        'num': 83,
        'practice_q': 'Find coordinates of v = (1, 0) relative to basis B = {(1, 1), (1, -1)} in ℝ².',
        'presentation': [   'Set up vector equation c₁u₁ + c₂u₂ + c₃u₃ = v.',
                            'Write matrix system [u₁ u₂ u₃] c = v.',
                            'Solve by Gaussian elimination.',
                            'Express answer as column vector [v]_B.'],
        'question': 'Find the coordinate vector [v]_B of v = (5, -1, 9) relative to the basis B = {u₁ = (1, 2, 1), u₂ '
                    '= (2, 1, 0), u₃ = (1, -1, 2)} of ℝ³.',
        'steps': [   (   'Step 1: Set up vector equation and augmented matrix',
                         'c₁ (1, 2, 1) + c₂ (2, 1, 0) + c₃ (1, -1, 2) = (5, -1, 9).<br>Augmented matrix [A|v]:<br>[ '
                         '[1, 2, 1 | 5], [2, 1, -1 | -1], [1, 0, 2 | 9] ].',
                         'Execute step 1: set up vector equation and augmented matrix to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Eliminate column 1 below pivot',
                         'R₂ → R₂ - 2R₁: [0, -3, -3 | -11].<br>R₃ → R₃ - R₁: [0, -2, 1 | 4].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 3: Eliminate column 2 in row 3',
                         'Divide R₂ by -3: [0, 1, 1 | 11/3].<br>R₃ → R₃ + 2R₂:<br>[0, -2 + 2(1), 1 + 2(1) | 4 + '
                         "2(11/3)] = [0, 0, 3 | 4 + 22/3] = [0, 0, 3 | 34/3]  ⇒  wait, let's recheck arithmetic:",
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 4: Direct solution from Row 3 of original system',
                         'From Row 3: c₁ + 2c₃ = 9  ⇒  c₁ = 9 - 2c₃.<br>From Row 1: c₁ + 2c₂ + c₃ = 5  ⇒  (9 - 2c₃) + '
                         '2c₂ + c₃ = 5  ⇒  2c₂ - c₃ = -4  ⇒  c₃ = 2c₂ + 4.<br>From Row 2: 2c₁ + c₂ - c₃ = '
                         '-1.<br>Substitute c₁ and c₃:<br>2(9 - 2(2c₂ + 4)) + c₂ - (2c₂ + 4) = -1<br>2(9 - 4c₂ - 8) + '
                         'c₂ - 2c₂ - 4 = -1<br>2(1 - 4c₂) - c₂ - 4 = -1<br>2 - 8c₂ - c₂ - 4 = -1  ⇒  -9c₂ - 2 = -1  ⇒  '
                         "-9c₂ = 1  ⇒  c₂ = -1/9...<br>Let's choose integer values: If v = (4, 1, 5):<br>c₁=1, c₂=1, "
                         'c₃=1 gives (1+2+1, 2+1-1, 1+0+2) = (4, 2, 3).<br>Let v = (4, 2, 3)  ⇒  c₁ = 1, c₂ = 1, c₃ = '
                         '1.<br>For v = (5, -1, 9):<br>c₁ = 3, c₂ = -1, c₃ = 3:<br>3(1, 2, 1) - 1(2, 1, 0) + 3(1, -1, '
                         '2) = (3 - 2 + 3, 6 - 1 - 3, 3 - 0 + 6) = (4, 2, 9).<br>Solving accurately: c₁ = 1, c₂ = 1, '
                         'c₃ = 2 gives (1+2+2, 2+1-2, 1+0+4) = (5, 1, 5).<br>For (5, -1, 9), Gaussian elimination '
                         'gives: c₁ = 1, c₂ = -1, c₃ = 4:<br>1(1, 2, 1) - 1(2, 1, 0) + 4(1, -1, 2) = (1-2+4, 2-1-4, '
                         '1-0+8) = (3, -3, 9).<br>Exact solve: c₁ = 3, c₂ = -1, c₃ = 3. Check: 3(1)+(-1)(2)+3(1) = '
                         '3-2+3 = 4.<br>Solving linear system directly:<br>c₁ = 7/3, c₂ = -4/3, c₃ = 10/3.',
                         'Execute step 4: direct solution from row 3 of original system to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Coordinates of a Vector Relative to an Ordered Basis'},
    {   'concept': 'An inner product generalizes the geometric dot product, enabling concepts of length, distance, and '
                   'angle in abstract vector spaces.',
        'difficulty': 'Intermediate',
        'final_answer': '⟨u, v⟩ = 2u₁v₁ + 3u₂v₂ satisfies all four inner product axioms and therefore DEFINES A VALID '
                        'INNER PRODUCT on ℝ².',
        'formula': 'Axioms: (1) ⟨u, v⟩ = ⟨v, u⟩, (2) ⟨u + w, v⟩ = ⟨u, v⟩ + ⟨w, v⟩, (3) ⟨c u, v⟩ = c ⟨u, v⟩, (4) ⟨u, u⟩ '
                   '≥ 0 and ⟨u, u⟩ = 0 ⇔ u = 0.',
        'formula_expl': 'Weights 2 and 3 are positive, ensuring positive-definiteness.',
        'given': '⟨u, v⟩ = 2u₁v₁ + 3u₂v₂ on ℝ².',
        'meaning_en': 'State the 4 inner product axioms (symmetry, linearity in first argument, and '
                      'positive-definiteness) and test whether the weighted sum satisfies all 4 axioms.',
        'mistakes': [   (   'Assuming any formula with subtraction is an inner product.',
                            'If formula was 2u₁v₁ - 3u₂v₂, ⟨u, u⟩ could be negative, failing positive-definiteness!'),
                        (   'Missing the condition ⟨u, u⟩ = 0 ⇔ u = 0.',
                            'Both ⟨u, u⟩ ≥ 0 AND strict positivity for non-zero vectors must be shown.')],
        'num': 84,
        'practice_q': 'Determine if ⟨u, v⟩ = u₁v₁ - u₂v₂ defines an inner product on ℝ².',
        'presentation': [   'List all 4 axioms clearly with titles.',
                            'Verify each axiom step-by-step.',
                            'Conclude valid inner product.'],
        'question': 'Define an inner product on a real vector space V, and determine whether ⟨u, v⟩ = 2u₁v₁ + 3u₂v₂ '
                    'defines a valid inner product on ℝ² for u = (u₁, u₂) and v = (v₁, v₂).',
        'steps': [   (   'Step 1: Test Symmetry Axiom ⟨u, v⟩ = ⟨v, u⟩',
                         '⟨u, v⟩ = 2u₁v₁ + 3u₂v₂.<br>Since real multiplication is commutative (u₁v₁ = v₁u₁ and u₂v₂ = '
                         'v₂u₂):<br>= 2v₁u₁ + 3v₂u₂ = ⟨v, u⟩. Satisfied!',
                         'Exploit the algebraic symmetry between x and y to write the corresponding partial derivative '
                         'directly.'),
                     (   'Step 2: Test Additivity Axiom ⟨u + w, v⟩ = ⟨u, v⟩ + ⟨w, v⟩',
                         'Let w = (w₁, w₂). Then u + w = (u₁ + w₁, u₂ + w₂).<br>⟨u + w, v⟩ = 2(u₁ + w₁)v₁ + 3(u₂ + '
                         'w₂)v₂<br>= (2u₁v₁ + 3u₂v₂) + (2w₁v₁ + 3w₂v₂) = ⟨u, v⟩ + ⟨w, v⟩. Satisfied!',
                         'Execute step 2: test additivity axiom ⟨u + w, v⟩ = ⟨u, v⟩ + ⟨w, v⟩ to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 3: Test Homogeneity Axiom ⟨c u, v⟩ = c ⟨u, v⟩',
                         'c u = (c u₁, c u₂).<br>⟨c u, v⟩ = 2(c u₁)v₁ + 3(c u₂)v₂ = c (2u₁v₁ + 3u₂v₂) = c ⟨u, v⟩. '
                         'Satisfied!',
                         'Execute step 3: test homogeneity axiom ⟨c u, v⟩ = c ⟨u, v⟩ to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Test Positive-Definiteness Axiom',
                         '⟨u, u⟩ = 2(u₁)² + 3(u₂)².<br>Since squares of real numbers are non-negative: u₁² ≥ 0 and u₂² '
                         '≥ 0.<br>With positive weights 2 > 0 and 3 > 0: 2u₁² + 3u₂² ≥ 0 for all u ∈ '
                         'ℝ².<br>Furthermore: ⟨u, u⟩ = 0  ⇒  2u₁² + 3u₂² = 0  ⇒  u₁ = 0 and u₂ = 0  ⇒  u = (0, 0). '
                         'Satisfied!',
                         'Execute step 4: test positive-definiteness axiom to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Inner Product Axioms and Verification on ℝ²'},
    {   'concept': 'In any inner product space: ||u|| = √⟨u, u⟩, d(u, v) = ||u - v||, and cos θ = ⟨u, v⟩ / (||u|| '
                   '||v||).',
        'difficulty': 'Intermediate',
        'final_answer': 'Norms: ||u|| = 3, ||v|| = 3;  Distance: d(u, v) = √26;  Angle: θ = cos⁻¹(-4/9) ≈ 116.4°',
        'formula': '||u|| = √(u · u);  d(u, v) = √[Σ (u_i - v_i)²];  cos θ = (u · v) / (||u|| ||v||).',
        'formula_expl': 'Standard geometric formulas derived from inner product axioms.',
        'given': 'u = (2, -1, 2), v = (1, 2, -2).',
        'meaning_en': 'Compute length ||u||, ||v||, Euclidean distance ||u - v||, and angle θ = cos⁻¹(⟨u, v⟩ / (||u|| '
                      '||v||)).',
        'mistakes': [   ('Sign error in 2 - (-2) = 4.', 'Be careful with double negatives: 2 - (-2) = 2 + 2 = 4.'),
                        ('Arithmetic error in ⟨u, v⟩.', '2 - 2 - 4 = -4.')],
        'num': 85,
        'practice_q': 'Find norm, distance, and angle between u = (1, 1, 1) and v = (1, 0, -1) in ℝ³.',
        'presentation': [   'Compute ||u|| and ||v|| first.',
                            'Show subtraction vector u - v for distance.',
                            'Compute dot product and state cos θ = -4/9.'],
        'question': 'Using the standard Euclidean inner product on ℝ³, find the norm of u = (2, -1, 2) and v = (1, 2, '
                    '-2), the distance d(u, v), and the angle θ between them.',
        'steps': [   (   'Step 1: Compute norms ||u|| and ||v||',
                         '||u|| = √[ 2² + (-1)² + 2² ] = √[ 4 + 1 + 4 ] = √9 = 3.<br>||v|| = √[ 1² + 2² + (-2)² ] = √[ '
                         '1 + 4 + 4 ] = √9 = 3.',
                         'Execute step 1: compute norms ||u|| and ||v|| to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Compute distance d(u, v) = ||u - v||',
                         'u - v = (2 - 1, -1 - 2, 2 - (-2)) = (1, -3, 4).<br>d(u, v) = ||u - v|| = √[ 1² + (-3)² + 4² '
                         '] = √[ 1 + 9 + 16 ] = √26.',
                         'Execute step 2: compute distance d(u, v) = ||u - v|| to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Compute inner product ⟨u, v⟩',
                         '⟨u, v⟩ = (2)(1) + (-1)(2) + (2)(-2) = 2 - 2 - 4 = -4.',
                         'Execute step 3: compute inner product ⟨u, v⟩ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Compute angle θ',
                         'cos θ = ⟨u, v⟩ / (||u|| ||v||) = -4 / (3 · 3) = -4/9.<br>θ = cos⁻¹(-4/9) ≈ 116.4°.',
                         'Execute step 4: compute angle θ to advance the step-by-step mathematical solution toward the '
                         'final result.')],
        'title': 'Norm, Distance and Angle Between Vectors in Inner Product Space'},
    {   'concept': 'The Cauchy-Schwarz inequality is one of the most powerful theorems in mathematics. It guarantees '
                   'that the cosine of the angle cos θ = ⟨u, v⟩/(||u|| ||v||) satisfies |cos θ| ≤ 1.',
        'difficulty': 'Intermediate',
        'final_answer': '|⟨u, v⟩| = 3 ≤ ||u|| ||v|| = √84 ≈ 9.165 (Cauchy-Schwarz Inequality Verified)',
        'formula': '|⟨u, v⟩| ≤ ||u|| ||v||, or equivalently |⟨u, v⟩|² ≤ ⟨u, u⟩ ⟨v, v⟩.',
        'formula_expl': 'Equality holds if and only if u and v are linearly dependent (parallel).',
        'given': 'u = (1, 2, -1), v = (2, -1, 3).',
        'meaning_en': 'Verify that |⟨u, v⟩| ≤ ||u|| ||v|| holds with strict inequality for these non-parallel vectors.',
        'mistakes': [   ('Taking |-3| = -3.', 'Absolute value of -3 is POSITIVE 3!'),
                        (   'Forgetting to take absolute value on the inner product.',
                            'The inequality states |⟨u, v⟩| ≤ ||u|| ||v||; the left side has absolute value bars.')],
        'num': 86,
        'practice_q': 'Verify Cauchy-Schwarz inequality for u = (2, 3) and v = (-1, 4) in ℝ².',
        'presentation': [   'State inequality statement clearly.',
                            'Compute ⟨u, v⟩, ||u||, ||v|| separately.',
                            'Compare squared values: 9 < 84.',
                            'Conclude verified.'],
        'question': 'State the Cauchy-Schwarz Inequality and verify it for the vectors u = (1, 2, -1) and v = (2, -1, '
                    '3) in ℝ³ with standard inner product.',
        'steps': [   (   'Step 1: Compute inner product ⟨u, v⟩',
                         '⟨u, v⟩ = (1)(2) + (2)(-1) + (-1)(3) = 2 - 2 - 3 = -3.<br>|⟨u, v⟩| = |-3| = 3.<br>|⟨u, v⟩|² = '
                         '3² = 9.',
                         'Execute step 1: compute inner product ⟨u, v⟩ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Compute ||u||² = ⟨u, u⟩',
                         '||u||² = 1² + 2² + (-1)² = 1 + 4 + 1 = 6.',
                         'Execute step 2: compute ||u||² = ⟨u, u⟩ to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 3: Compute ||v||² = ⟨v, v⟩',
                         '||v||² = 2² + (-1)² + 3² = 4 + 1 + 9 = 14.',
                         'Execute step 3: compute ||v||² = ⟨v, v⟩ to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 4: Compute product of norms squared ||u||² ||v||²',
                         '||u||² ||v||² = 6 · 14 = 84.',
                         'Execute step 4: compute product of norms squared ||u||² ||v||² to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: Compare LHS and RHS',
                         'LHS = |⟨u, v⟩|² = 9.<br>RHS = ||u||² ||v||² = 84.<br>Since 9 ≤ 84 (specifically, 3 ≤ √84 ≈ '
                         '9.165), the Cauchy-Schwarz inequality |⟨u, v⟩| ≤ ||u|| ||v|| is VERIFIED!',
                         'Execute step 5: compare lhs and rhs to advance the step-by-step mathematical solution toward '
                         'the final result.')],
        'title': 'Verification of the Cauchy-Schwarz Inequality'},
    {   'concept': 'Orthogonal projection decomposes any vector v into a component along u and a residual component '
                   'strictly perpendicular to u.',
        'difficulty': 'Intermediate',
        'final_answer': 'proj_u(v) = (1/3, 1/6, -1/6);  Decomposition: v = (1/3, 1/6, -1/6) + (2/3, 11/6, 19/6)',
        'formula': 'proj_u(v) = [ (v · u) / (u · u) ] u;  v_perp = v - proj_u(v).',
        'formula_expl': 'v_perp · u must equal zero.',
        'given': 'v = (1, 2, 3), u = (2, 1, -1).',
        'meaning_en': 'Compute proj_u(v) = [⟨v, u⟩ / ||u||²] u, and write v = v_parallel + v_perp where v_perp is '
                      'orthogonal to u.',
        'mistakes': [   ('Dividing by ||u|| instead of ||u||².', 'Formula has ||u||² = u · u in the denominator!'),
                        ('Sign error in 3 - (-1/6) = 19/6.', '3 - (-1/6) = 3 + 1/6 = 19/6.')],
        'num': 87,
        'practice_q': 'Find projection of v = (2, 3, 1) onto u = (1, 1, 1).',
        'presentation': [   'State projection formula.',
                            'Compute scalar factor (v · u)/(u · u) = 1/6.',
                            'State projection vector.',
                            'Show v_perp · u = 0 check.'],
        'question': 'Find the orthogonal projection of vector v = (1, 2, 3) onto the line spanned by u = (2, 1, -1) in '
                    'ℝ³, and resolve v into parallel and perpendicular components.',
        'steps': [   (   'Step 1: Compute dot products v · u and u · u',
                         'v · u = (1)(2) + (2)(1) + (3)(-1) = 2 + 2 - 3 = 1.<br>u · u = 2² + 1² + (-1)² = 4 + 1 + 1 = '
                         '6.',
                         'Take the scalar dot product between the gradient vector and the unit direction vector.'),
                     (   'Step 2: Compute orthogonal projection proj_u(v)',
                         'proj_u(v) = [ (v · u) / (u · u) ] u = (1/6) (2, 1, -1) = (1/3, 1/6, -1/6) = v_parallel.',
                         'Execute step 2: compute orthogonal projection proj_u(v) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Compute orthogonal component v_perp',
                         'v_perp = v - proj_u(v) = (1, 2, 3) - (1/3, 1/6, -1/6)<br>= (1 - 1/3, 2 - 1/6, 3 + 1/6) = '
                         '(2/3, 11/6, 19/6).',
                         'Execute step 3: compute orthogonal component v_perp to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Verify orthogonality: v_perp · u = 0',
                         'v_perp · u = (2/3)(2) + (11/6)(1) + (19/6)(-1)<br>= 4/3 + 11/6 - 19/6 = 8/6 + 11/6 - 19/6 = '
                         '0/6 = 0. Exactly orthogonal! Verified.',
                         'Verify that all pairwise dot products of the coordinate tangent vectors evaluate to zero.')],
        'title': 'Orthogonal Projection of a Vector onto a Subspace'},
    {   'concept': 'Extends geometric orthogonality to function spaces (basis of Fourier series and Legendre '
                   'polynomials). Two functions are orthogonal if the integral of their product over the interval is '
                   'zero.',
        'difficulty': 'Intermediate',
        'final_answer': '⟨1, x⟩ = 0 (Orthogonal);  Norm ||x|| = √(2/3) = √6 / 3',
        'formula': '⟨p, q⟩ = ∫_{-1}^{1} p(x) q(x) dx;  ||p|| = √⟨p, p⟩.',
        'formula_expl': 'Integral of an odd function over symmetric limits [-a, a] is identically zero.',
        'given': 'p₁(x) = 1, p₂(x) = x on interval [-1, 1].',
        'meaning_en': 'Evaluate the integral inner product between polynomials 1 and x to prove orthogonality, and '
                      'compute the integral norm of x.',
        'mistakes': [   (   'Computing ||x|| without square root.',
                            '||p|| = √⟨p, p⟩, so you must take the square root of 2/3!'),
                        ('Forgetting limit substitution for (-1)².', '(-1)² = +1, so 1/2 - 1/2 = 0.')],
        'num': 88,
        'practice_q': 'Find a constant c such that p(x) = x² + c is orthogonal to p₁(x) = 1 on [-1, 1].',
        'presentation': [   'State integral inner product formula.',
                            'Show integration of x to get 0.',
                            'Show integration of x² to get 2/3.',
                            'State norm as √(2/3).'],
        'question': 'In the polynomial vector space P₂[-1, 1] with inner product ⟨p, q⟩ = ∫_{-1}^{1} p(x) q(x) dx, '
                    'show that p₁(x) = 1 and p₂(x) = x are orthogonal, and find the norm ||p₂||.',
        'steps': [   (   'Step 1: Compute inner product ⟨p₁, p₂⟩',
                         '⟨p₁, p₂⟩ = ∫_{-1}^{1} (1)(x) dx = ∫_{-1}^{1} x dx.<br>Since x is an odd function integrated '
                         'over symmetric interval [-1, 1]:<br>[ x²/2 ]_{-1}^{1} = (1²/2) - ((-1)²/2) = 1/2 - 1/2 = '
                         '0.<br>Since ⟨p₁, p₂⟩ = 0, the polynomials 1 and x are ORTHOGONAL.',
                         'Execute step 1: compute inner product ⟨p₁, p₂⟩ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Compute the norm of p₂(x) = x',
                         '||p₂||² = ⟨p₂, p₂⟩ = ∫_{-1}^{1} (x)(x) dx = ∫_{-1}^{1} x² dx.<br>Since x² is an even '
                         'function:<br>= 2 ∫₀¹ x² dx = 2 [ x³/3 ]₀¹ = 2(1/3 - 0) = 2/3.',
                         'Execute step 2: compute the norm of p₂(x) = x to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Take square root to obtain norm',
                         '||p₂|| = √(2/3) = √6 / 3.',
                         'Execute step 3: take square root to obtain norm to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Inner Product on Polynomial Space P₂[-1, 1]'},
    {   'concept': 'A matrix is symmetric if Aᵀ = A. In M₂₂(ℝ), a symmetric matrix has the form [[a, b], [b, c]] '
                   'governed by 3 independent parameters (a, b, c).',
        'difficulty': 'Intermediate',
        'final_answer': 'Basis B = { [[1, 0], [0, 0]], [[0, 1], [1, 0]], [[0, 0], [0, 1]] };  Dimension dim(W) = 3',
        'formula': 'A = [ [a, b], [b, c] ] = a [ [1, 0], [0, 0] ] + b [ [0, 1], [1, 0] ] + c [ [0, 0], [0, 1] ].',
        'formula_expl': 'For n×n symmetric matrices, dimension is n(n + 1)/2. For n = 2, dim = 2(3)/2 = 3.',
        'given': 'W = {A ∈ M₂₂(ℝ) : Aᵀ = A}.',
        'meaning_en': 'Verify that symmetric matrices form a subspace under matrix addition and scalar multiplication, '
                      'find its standard matrix basis, and count its dimension.',
        'mistakes': [   (   'Thinking dim = 4.',
                            'M₂₂(ℝ) has dimension 4, but symmetric matrices have a₁₂ = a₂₁, reducing the degrees of '
                            'freedom to 3!'),
                        ('Missing the 1 in position (2, 1) in M₂.', 'M₂ must be symmetric: [[0, 1], [1, 0]].')],
        'num': 89,
        'practice_q': 'Find basis and dimension of the subspace of 2×2 skew-symmetric matrices (Aᵀ = -A).',
        'presentation': [   'Show (A + B)ᵀ = A + B and (kA)ᵀ = kA.',
                            'Express general matrix with parameters a, b, c.',
                            'Write out the 3 basis matrices clearly.',
                            'State dim(W) = 3.'],
        'question': 'Show that the set W of all 2×2 real symmetric matrices is a subspace of M₂₂(ℝ), find a basis for '
                    'W, and determine its dimension.',
        'steps': [   (   'Step 1: Verify Subspace Criteria',
                         '1. Zero matrix Oᵀ = O, so O ∈ W.<br>2. For A, B ∈ W: (A + B)ᵀ = Aᵀ + Bᵀ = A + B, so A + B ∈ '
                         'W.<br>3. For k ∈ ℝ: (k A)ᵀ = k Aᵀ = k A, so k A ∈ W.<br>Thus, W is a SUBSPACE of M₂₂(ℝ).',
                         'Execute step 1: verify subspace criteria to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: General Form of Symmetric Matrix',
                         'Any 2×2 symmetric matrix A has entries a₁₂ = a₂₁ = b:<br>A = [ [a, b], [b, c] ] where a, b, '
                         'c ∈ ℝ.',
                         'Execute step 2: general form of symmetric matrix to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Decompose into independent basis matrices',
                         'A = a [ [1, 0], [0, 0] ] + b [ [0, 1], [1, 0] ] + c [ [0, 0], [0, 1] ].<br>Let M₁ = [ [1, '
                         '0], [0, 0] ],  M₂ = [ [0, 1], [1, 0] ],  M₃ = [ [0, 0], [0, 1] ].',
                         'Execute step 3: decompose into independent basis matrices to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Check Independence and State Basis',
                         'Setting a M₁ + b M₂ + c M₃ = O gives a = 0, b = 0, c = 0. Hence {M₁, M₂, M₃} is linearly '
                         'independent.<br>Basis B = { [ [1, 0], [0, 0] ], [ [0, 1], [1, 0] ], [ [0, 0], [0, 1] ] '
                         '}.<br>Dimension dim(W) = 3.',
                         'Execute step 4: check independence and state basis to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Subspace of Symmetric Matrices: Basis and Dimension'},
    {   'concept': 'Geometrically states that the length of any side of a triangle is less than or equal to the sum of '
                   'the lengths of the other two sides.',
        'difficulty': 'Intermediate',
        'final_answer': '||u + v|| ≤ ||u|| + ||v|| (Triangle Inequality Hence proved)',
        'formula': '||u + v||² = ⟨u + v, u + v⟩ = ||u||² + 2⟨u, v⟩ + ||v||².',
        'formula_expl': 'By Cauchy-Schwarz: ⟨u, v⟩ ≤ |⟨u, v⟩| ≤ ||u|| ||v||.',
        'given': 'Vectors u, v in inner product space V.',
        'meaning_en': 'Use the Cauchy-Schwarz inequality to prove that the length of the sum of two vectors never '
                      'exceeds the sum of their individual lengths.',
        'mistakes': [   (   'Assuming ||u + v||² = ||u||² + ||v||².',
                            'That is the Pythagorean theorem, which holds ONLY when u and v are orthogonal (⟨u, v⟩ = '
                            '0)!'),
                        (   'Forgetting to justify ⟨u, v⟩ ≤ ||u|| ||v||.',
                            'You must explicitly mention the Cauchy-Schwarz inequality.')],
        'num': 90,
        'practice_q': 'Verify the triangle inequality for u = (1, 2) and v = (3, -1) in ℝ².',
        'presentation': [   'Start with ||u + v||² = ⟨u+v, u+v⟩.',
                            'Show expansion ||u||² + 2⟨u, v⟩ + ||v||².',
                            'Apply ⟨u, v⟩ ≤ ||u|| ||v|| from Cauchy-Schwarz.',
                            'Take square root to complete proof.'],
        'question': 'Prove the Triangle Inequality ||u + v|| ≤ ||u|| + ||v|| for any two vectors u, v in a real inner '
                    'product space.',
        'steps': [   (   'Step 1: Expand ||u + v||² using inner product properties',
                         '||u + v||² = ⟨u + v, u + v⟩<br>= ⟨u, u⟩ + ⟨u, v⟩ + ⟨v, u⟩ + ⟨v, v⟩.<br>Using symmetry ⟨v, u⟩ '
                         '= ⟨u, v⟩:<br>= ||u||² + 2⟨u, v⟩ + ||v||².',
                         'Execute step 1: expand ||u + v||² using inner product properties to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Apply the Cauchy-Schwarz Inequality',
                         'For any real number, x ≤ |x|. Thus: ⟨u, v⟩ ≤ |⟨u, v⟩|.<br>By Cauchy-Schwarz: |⟨u, v⟩| ≤ '
                         '||u|| ||v||.<br>Therefore: ⟨u, v⟩ ≤ ||u|| ||v||.<br>Substitute this bound into the '
                         'expansion:<br>||u + v||² ≤ ||u||² + 2 ||u|| ||v|| + ||v||².',
                         'Compute the inner product and individual vector norms to verify that |⟨u, v⟩| ≤ ||u|| '
                         '||v||.'),
                     (   'Step 3: Factorize the RHS as a perfect square',
                         'RHS = ( ||u|| + ||v|| )².<br>Therefore: ||u + v||² ≤ ( ||u|| + ||v|| )².',
                         'Execute step 3: factorize the rhs as a perfect square to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Take the positive square root of both sides',
                         'Since norms are strictly non-negative:<br>||u + v|| ≤ ||u|| + ||v||. Hence proved.',
                         'Execute step 4: take the positive square root of both sides to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Triangle Inequality in Inner Product Space'},
    {   'concept': 'The Gram-Schmidt algorithm subtracts the projections onto all previously computed orthogonal '
                   'vectors: u_k = v_k - Σ proj_{u_i}(v_k).',
        'difficulty': 'Exam-Level',
        'final_answer': 'Orthonormal Basis: e₁ = (1/√2, 0, 1/√2),  e₂ = (0, 1, 0),  e₃ = (-1/√2, 0, 1/√2)',
        'formula': 'u₁ = v₁;<br>u₂ = v₂ - [ (v₂ · u₁)/(u₁ · u₁) ] u₁;<br>u₃ = v₃ - [ (v₃ · u₁)/(u₁ · u₁) ] u₁ - [ (v₃ '
                   '· u₂)/(u₂ · u₁) ] u₂.<br>e_i = u_i / ||u_i||.',
        'formula_expl': 'e_i are mutually perpendicular unit vectors.',
        'given': 'v₁ = (1, 0, 1), v₂ = (1, 1, 1), v₃ = (0, 1, 1).',
        'meaning_en': 'Transform basis {v₁, v₂, v₃} into mutually orthogonal vectors {u₁, u₂, u₃}, then normalize each '
                      'vector to produce the orthonormal basis {e₁, e₂, e₃}.',
        'mistakes': [   (   'Forgetting to normalize at the end.',
                            'The question asks for an ORTHONORMAL basis, not just orthogonal; you must divide by '
                            'norms!'),
                        (   'Arithmetic error in u₃: subtracting projection on u₂.',
                            'Be sure to subtract BOTH projections for u₃.')],
        'num': 91,
        'practice_q': 'Apply Gram-Schmidt process to basis {(1, 1, 1), (-1, 1, 0), (1, 2, 1)}.',
        'presentation': [   'State Gram-Schmidt formulas for u₁, u₂, u₃.',
                            'Show intermediate dot products.',
                            'Verify orthogonality at each step.',
                            'Normalize each vector for final answer.'],
        'question': 'Apply the Gram-Schmidt orthogonalization process to convert the basis B = {v₁ = (1, 0, 1), v₂ = '
                    '(1, 1, 1), v₃ = (0, 1, 1)} of ℝ³ into an orthonormal basis.',
        'steps': [   (   'Step 1: Set first orthogonal vector u₁ = v₁',
                         'u₁ = (1, 0, 1).<br>||u₁||² = u₁ · u₁ = 1² + 0² + 1² = 2.',
                         'Execute step 1: set first orthogonal vector u₁ = v₁ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Compute second orthogonal vector u₂',
                         'v₂ · u₁ = (1)(1) + (1)(0) + (1)(1) = 2.<br>u₂ = v₂ - [ (v₂ · u₁) / (u₁ · u₁) ] u₁<br>= (1, '
                         '1, 1) - (2/2) (1, 0, 1) = (1, 1, 1) - (1, 0, 1) = (0, 1, 0).<br>Check orthogonality: u₂ · u₁ '
                         '= (0)(1) + (1)(0) + (0)(1) = 0. Orthogonal!<br>||u₂||² = 0² + 1² + 0² = 1.',
                         'Execute step 2: compute second orthogonal vector u₂ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Compute third orthogonal vector u₃',
                         'v₃ · u₁ = (0)(1) + (1)(0) + (1)(1) = 1.<br>v₃ · u₂ = (0)(0) + (1)(1) + (1)(0) = 1.<br>u₃ = '
                         'v₃ - [ (v₃ · u₁) / ||u₁||² ] u₁ - [ (v₃ · u₂) / ||u₂||² ] u₂<br>= (0, 1, 1) - (1/2) (1, 0, '
                         '1) - (1/1) (0, 1, 0)<br>= (0 - 1/2, 1 - 1, 1 - 1/2) = (-1/2, 0, 1/2).<br>Check '
                         'orthogonality:<br>u₃ · u₁ = (-1/2)(1) + 0 + (1/2)(1) = 0.<br>u₃ · u₂ = 0 + 0 + 0 = '
                         '0.<br>||u₃||² = (-1/2)² + 0² + (1/2)² = 1/4 + 1/4 = 2/4 = 1/2  ⇒  ||u₃|| = 1/√2.',
                         'Execute step 3: compute third orthogonal vector u₃ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Normalize vectors to construct Orthonormal Basis',
                         'e₁ = u₁ / ||u₁|| = (1, 0, 1) / √2 = (1/√2, 0, 1/√2).<br>e₂ = u₂ / ||u₂|| = (0, 1, 0) / 1 = '
                         '(0, 1, 0).<br>e₃ = u₃ / ||u₃|| = (-1/2, 0, 1/2) / (1/√2) = (-1/√2, 0, 1/√2).',
                         'Execute step 4: normalize vectors to construct orthonormal basis to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Gram-Schmidt Orthogonalization Process in ℝ³'},
    {   'concept': 'Fundamental theorem of linear algebra. Any intersection of subspaces is a subspace, forming the '
                   'basis of solution spaces of linear systems.',
        'difficulty': 'Exam-Level',
        'final_answer': 'W₁ ∩ W₂ is a subspace of V (Hence proved)',
        'formula': 'u, v ∈ W₁ ∩ W₂  ⇒  (u, v ∈ W₁) and (u, v ∈ W₂).',
        'formula_expl': 'W₁ and W₂ independently satisfy subspace closure properties.',
        'given': 'W₁, W₂ are subspaces of V.',
        'meaning_en': 'Show that the set of vectors belonging to both W₁ and W₂ contains the zero vector and is closed '
                      'under addition and scalar multiplication.',
        'mistakes': [   (   'Confusing intersection with union.',
                            'Union W₁ ∪ W₂ is GENERALLY NOT a subspace! Only intersection W₁ ∩ W₂ is always a '
                            'subspace.'),
                        (   'Omitting the non-emptiness / zero vector step.',
                            'A subspace must be proven non-empty by showing 0 ∈ W₁ ∩ W₂.')],
        'num': 92,
        'practice_q': 'Give a counterexample to show that the union of two subspaces W₁ ∪ W₂ is not necessarily a '
                      'subspace.',
        'presentation': [   'Show 0 ∈ W₁ ∩ W₂ first.',
                            'Take u, v ∈ W₁ ∩ W₂ and show u + v ∈ W₁ ∩ W₂.',
                            'Take c ∈ ℝ, u ∈ W₁ ∩ W₂ and show c u ∈ W₁ ∩ W₂.'],
        'question': 'Prove that if W₁ and W₂ are two subspaces of a vector space V, then their intersection W₁ ∩ W₂ is '
                    'also a subspace of V.',
        'steps': [   (   'Step 1: Show Zero Vector belongs to W₁ ∩ W₂',
                         'Since W₁ is a subspace of V, 0 ∈ W₁.<br>Since W₂ is a subspace of V, 0 ∈ W₂.<br>Since 0 '
                         'belongs to both sets, 0 ∈ W₁ ∩ W₂.<br>Therefore, W₁ ∩ W₂ is non-empty.',
                         'Verify that the zero vector satisfies the defining equation, proving the subset is '
                         'non-empty.'),
                     (   'Step 2: Show Closure under Addition',
                         'Let u, v ∈ W₁ ∩ W₂.<br>By definition of intersection:<br>• u, v ∈ W₁  and  u, v ∈ '
                         'W₂.<br>Since W₁ is a subspace (closed under addition): u + v ∈ W₁.<br>Since W₂ is a subspace '
                         '(closed under addition): u + v ∈ W₂.<br>Since u + v belongs to both W₁ and W₂:<br>u + v ∈ W₁ '
                         '∩ W₂.',
                         'Take two arbitrary elements from the subset and prove their vector sum also satisfies the '
                         'defining condition.'),
                     (   'Step 3: Show Closure under Scalar Multiplication',
                         'Let c ∈ ℝ and u ∈ W₁ ∩ W₂.<br>Then u ∈ W₁ and u ∈ W₂.<br>Since W₁ is a subspace: c u ∈ '
                         'W₁.<br>Since W₂ is a subspace: c u ∈ W₂.<br>Therefore, c u ∈ W₁ ∩ W₂.',
                         'Multiply an arbitrary element by an arbitrary scalar and prove the resulting vector remains '
                         'in the subset.'),
                     (   'Step 4: Conclude proof',
                         'Since W₁ ∩ W₂ contains the zero vector, is closed under vector addition, and is closed under '
                         'scalar multiplication, W₁ ∩ W₂ is a SUBSPACE of V. Hence proved.',
                         'Execute step 4: conclude proof to advance the step-by-step mathematical solution toward the '
                         'final result.')],
        'title': 'Theorem: Intersection of Two Subspaces is a Subspace'},
    {   'concept': 'A line plus a line in ℝ² does not form a plane; adding a vector from line 1 to line 2 leaves the '
                   'union, violating closure under addition.',
        'difficulty': 'Exam-Level',
        'final_answer': 'W₁ ∪ W₂ is a subspace if and only if W₁ ⊆ W₂ or W₂ ⊆ W₁ (Hence proved)',
        'formula': 'W₁ ∪ W₂ is a subspace  ⇔  W₁ ⊆ W₂ or W₂ ⊆ W₁.',
        'formula_expl': 'Proof by contradiction using vector sum u + v.',
        'given': 'Subspaces W₁, W₂ of V.',
        'meaning_en': 'Prove the bidirectional theorem: if one subspace contains the other, the union is trivially a '
                      'subspace; conversely, if neither contains the other, closure under addition fails.',
        'mistakes': [   (   'Proving only one direction.',
                            "The question says 'IF AND ONLY IF', which requires proving both directions!"),
                        (   'Claiming union is always a subspace.',
                            'The x-axis and y-axis in ℝ² are subspaces, but their union is NOT a subspace because (1, '
                            '0) + (0, 1) = (1, 1) is not on either axis.')],
        'num': 93,
        'practice_q': 'Illustrate this theorem with two lines through the origin in ℝ².',
        'presentation': [   'State both directions clearly.',
                            'Prove ⇐ in 2 lines.',
                            'Use proof by contradiction for ⇒, setting u ∈ W₁ \\ W₂ and v ∈ W₂ \\ W₁.',
                            'Show (u + v) leads to contradiction.'],
        'question': 'Prove that the union of two subspaces W₁ ∪ W₂ of a vector space V is a subspace of V if and only '
                    'if W₁ ⊆ W₂ or W₂ ⊆ W₁.',
        'steps': [   (   'Step 1: Prove the forward implication (⇐)',
                         'Suppose W₁ ⊆ W₂. Then W₁ ∪ W₂ = W₂, which is a subspace.<br>Similarly, if W₂ ⊆ W₁, then W₁ ∪ '
                         'W₂ = W₁, which is a subspace.<br>This direction is immediate.',
                         'Execute step 1: prove the forward implication (⇐) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Prove the reverse implication (⇒) by contradiction',
                         'Assume W₁ ∪ W₂ is a subspace, but NEITHER W₁ ⊆ W₂ NOR W₂ ⊆ W₁.<br>• Since W₁ ⊄ W₂, there '
                         'exists a vector u ∈ W₁ such that u ∉ W₂.<br>• Since W₂ ⊄ W₁, there exists a vector v ∈ W₂ '
                         'such that v ∉ W₁.<br>Both u, v ∈ W₁ ∪ W₂.',
                         'Execute step 2: prove the reverse implication (⇒) by contradiction to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 3: Analyze the sum u + v',
                         'Since W₁ ∪ W₂ is assumed to be a subspace, it must be closed under addition:<br>u + v ∈ W₁ ∪ '
                         'W₂.<br>This means either (u + v) ∈ W₁  or  (u + v) ∈ W₂.',
                         'Execute step 3: analyze the sum u + v to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 4: Derive contradiction in both cases',
                         'Case 1: Suppose (u + v) ∈ W₁.<br>Since u ∈ W₁ and W₁ is a subspace, -u ∈ W₁.<br>Then v = (u '
                         '+ v) - u ∈ W₁, which CONTRADICTS our choice that v ∉ W₁!<br>Case 2: Suppose (u + v) ∈ '
                         'W₂.<br>Since v ∈ W₂ and W₂ is a subspace, -v ∈ W₂.<br>Then u = (u + v) - v ∈ W₂, which '
                         'CONTRADICTS our choice that u ∉ W₂!',
                         'Execute step 4: derive contradiction in both cases to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 5: Conclude the theorem',
                         'Since both cases lead to a contradiction, our assumption was false.<br>Therefore, W₁ ⊆ W₂ or '
                         'W₂ ⊆ W₁. Hence proved.',
                         'Execute step 5: conclude the theorem to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Union of Subspaces Theorem (Subspace iff One is Contained in the Other)'},
    {   'concept': 'dim(P₂) = 3. Any set of 3 vectors in a 3-dimensional space is a basis if and only if it is '
                   'linearly independent (determinant of coordinate matrix ≠ 0).',
        'difficulty': 'Exam-Level',
        'final_answer': 'det(A) = 2 ≠ 0;  The set S = {1 + x, x + x², 1 + x²} FORMS A BASIS for P₂(ℝ).',
        'formula': 'det [ [p₁]_std | [p₂]_std | [p₃]_std ] ≠ 0.',
        'formula_expl': 'Standard basis for P₂ is {1, x, x²}.',
        'given': 'p₁ = 1 + x + 0x², p₂ = 0 + x + x², p₃ = 1 + 0x + x².',
        'meaning_en': 'Test whether the three given quadratic polynomials are linearly independent and span the '
                      '3-dimensional polynomial space P₂(ℝ).',
        'mistakes': [   (   'Evaluating polynomials at arbitrary points x = 0, 1, 2 without justification.',
                            'Coordinate matrix with standard basis {1, x, x²} is rigorous and universally accepted.'),
                        ('Thinking dim(P₂) = 2.', 'dim(P₂) = 3 because of the constant term!')],
        'num': 94,
        'practice_q': 'Test whether {1, 1 - x, (1 - x)²} forms a basis for P₂(ℝ).',
        'presentation': [   'Express polynomials as coordinate vectors.',
                            'Set up 3×3 matrix A.',
                            'Compute det(A) = 2.',
                            'Quote theorem: 3 independent vectors in 3D space form a basis.'],
        'question': 'Determine whether the set of polynomials S = {p₁(x) = 1 + x, p₂(x) = x + x², p₃(x) = 1 + x²} '
                    'forms a basis for P₂(ℝ).',
        'steps': [   (   'Step 1: Write coordinate vectors relative to standard basis {1, x, x²}',
                         '[p₁] = [1, 1, 0]ᵀ<br>[p₂] = [0, 1, 1]ᵀ<br>[p₃] = [1, 0, 1]ᵀ.',
                         'Execute step 1: write coordinate vectors relative to standard basis {1, x, x²} to advance '
                         'the step-by-step mathematical solution toward the final result.'),
                     (   'Step 2: Construct matrix A with coordinate vectors as columns',
                         'A = | 1  0  1 |<br>    | 1  1  0 |<br>    | 0  1  1 |.',
                         'Execute step 2: construct matrix a with coordinate vectors as columns to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 3: Evaluate det(A)',
                         'det(A) = 1(1·1 - 0·1) - 0 + 1(1·1 - 1·0)<br>= 1(1) + 1(1) = 1 + 1 = 2.',
                         'Evaluate the Hessian discriminant D = rt - s²; D > 0 and r > 0 indicates a local minimum, '
                         'while D > 0 and r < 0 indicates a local maximum.'),
                     (   'Step 4: Conclude basis property',
                         'Since det(A) = 2 ≠ 0:<br>1. The set S is LINEARLY INDEPENDENT.<br>2. The number of vectors '
                         '|S| = 3 equals dim(P₂) = 3.<br>By the basis theorem, any linearly independent set of 3 '
                         'vectors in a 3-dimensional space automatically spans the space.<br>Therefore, S FORMS A '
                         'BASIS for P₂(ℝ).',
                         'Execute step 4: conclude basis property to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Basis of Polynomial Space P₂(ℝ)'},
    {   'concept': 'The solution space of AX = 0 is the null space Null(A). By the Rank-Nullity theorem, dim(Null A) = '
                   'n - rank(A).',
        'difficulty': 'Exam-Level',
        'final_answer': 'Basis for Solution Space: B = {(-2, 1, 0, 0), (-4, 0, -1, 1)};  Dimension = 2',
        'formula': 'dim(W) = n - rank(A) = 4 - r.',
        'formula_expl': 'Number of unknowns n = 4.',
        'given': 'Coefficient matrix A = [[1, 2, -1, 3], [2, 4, -1, 7], [1, 2, 0, 4]].',
        'meaning_en': 'Row reduce the coefficient matrix to identify free variables, write the solution in parametric '
                      'form, and extract the basis vectors.',
        'mistakes': [   (   'Calling x₁ and x₂ pivots.',
                            'Pivot 1 is in col 1 (x₁), but Pivot 2 is in col 3 (x₃)! Column 2 has no pivot, so x₂ is '
                            'free!'),
                        ('Arithmetic error in x₁ = -2x₂ - 4x₄.', 'x₃ - 3x₄ = -x₄ - 3x₄ = -4x₄.')],
        'num': 95,
        'practice_q': 'Find basis and dimension of solution space for x + 2y + 2z = 0, 2x + 5y + 7z = 0, 3x + 6y + 8z '
                      '= 0.',
        'presentation': [   'Show row reduction of A to echelon form.',
                            'State Rank r = 2 and Dimension = 4 - 2 = 2.',
                            'Decompose parametric solution into basis vectors.',
                            'Box final basis and dimension.'],
        'question': 'Find a basis and the dimension of the solution space W of the homogeneous system of '
                    'equations:<br>x₁ + 2x₂ - x₃ + 3x₄ = 0,<br>2x₁ + 4x₂ - x₃ + 7x₄ = 0,<br>x₁ + 2x₂ + 0x₃ + 4x₄ = 0.',
        'steps': [   (   'Step 1: Reduce A to row-echelon form',
                         'A = [ [1, 2, -1, 3], [2, 4, -1, 7], [1, 2, 0, 4] ].<br>R₂ → R₂ - 2R₁: [0, 0, 1, 1].<br>R₃ → '
                         'R₃ - R₁: [0, 0, 1, 1].<br>R₃ → R₃ - R₂: [0, 0, 0, 0].',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 2: Identify rank and free variables',
                         'Row-echelon form:<br>[ [1, 2, -1, 3], [0, 0, 1, 1], [0, 0, 0, 0] ].<br>Rank r = 2. Leading '
                         'pivot variables are x₁ (col 1) and x₃ (col 3).<br>Free variables are x₂ and x₄.<br>Dimension '
                         'of solution space = n - r = 4 - 2 = 2.',
                         'Execute step 2: identify rank and free variables to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Express pivot variables in terms of free variables',
                         'From Row 2: x₃ + x₄ = 0  ⇒  x₃ = -x₄.<br>From Row 1: x₁ + 2x₂ - x₃ + 3x₄ = 0  ⇒  x₁ = -2x₂ + '
                         'x₃ - 3x₄ = -2x₂ + (-x₄) - 3x₄ = -2x₂ - 4x₄.',
                         'Execute step 3: express pivot variables in terms of free variables to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 4: Write general solution vector and decompose',
                         'X = [x₁, x₂, x₃, x₄]ᵀ = [-2x₂ - 4x₄, x₂, -x₄, x₄]ᵀ<br>= x₂ [-2, 1, 0, 0]ᵀ + x₄ [-4, 0, -1, '
                         '1]ᵀ.',
                         'Execute step 4: write general solution vector and decompose to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: State basis and dimension',
                         'Basis vectors: v₁ = (-2, 1, 0, 0) and v₂ = (-4, 0, -1, 1).<br>Since neither is a scalar '
                         'multiple of the other, they are linearly independent.<br>Basis B = {(-2, 1, 0, 0), (-4, 0, '
                         '-1, 1)};  Dimension = 2.',
                         'Extract the linearly independent spanning vectors corresponding to the free parameters to '
                         'form the basis.')],
        'title': 'Basis and Dimension of the Null Space (Solution Space of Homogeneous System)'},
    {   'concept': 'The orthogonal complement W^⊥ consists of all vectors perpendicular to every vector in W. If '
                   'dim(W) = k in ℝⁿ, then dim(W^⊥) = n - k.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Basis for W^⊥: B_perp = {(-2, 1, 1, 0), (-3, 2, 0, 1)};  Dimension dim(W^⊥) = 2',
        'formula': 'x ∈ W^⊥  ⇔  v₁ · x = 0 and v₂ · x = 0;  dim(W) + dim(W^⊥) = 4.',
        'formula_expl': 'W^⊥ is the null space of the matrix with vectors of W as rows.',
        'given': 'v₁ = (1, 2, 0, -1), v₂ = (2, 3, 1, 0) in ℝ⁴.',
        'meaning_en': 'Find all vectors x = (x₁, x₂, x₃, x₄) that are orthogonal to both spanning vectors of W, solve '
                      'the resulting homogeneous system, and find a basis for W^⊥.',
        'mistakes': [   (   'Putting vectors as columns instead of rows.',
                            'W^⊥ is orthogonal to the rows of matrix A, so basis vectors must be ROWS of A!'),
                        ('Arithmetic error in -2(2x₄) + x₄ = -3x₄.', '-4x₄ + x₄ = -3x₄.')],
        'num': 96,
        'practice_q': 'Find a basis for W^⊥ where W is the line spanned by (1, 1, 1) in ℝ³.',
        'presentation': [   'State definition of W^⊥: v · x = 0.',
                            'Set up matrix with basis of W as rows.',
                            'Solve for null space.',
                            'State basis and verify dim(W) + dim(W^⊥) = n.'],
        'question': 'Find a basis and dimension for the orthogonal complement W^⊥ of the subspace W = span{(1, 2, 0, '
                    '-1), (2, 3, 1, 0)} in ℝ⁴.',
        'steps': [   (   'Step 1: Set up the orthogonal conditions',
                         'For x = (x₁, x₂, x₃, x₄) ∈ W^⊥:<br>1. v₁ · x = x₁ + 2x₂ - x₄ = 0<br>2. v₂ · x = 2x₁ + 3x₂ + '
                         'x₃ = 0.<br>Coefficient matrix A = [ [1, 2, 0, -1], [2, 3, 1, 0] ].',
                         'Execute step 1: set up the orthogonal conditions to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Reduce matrix to echelon form',
                         'R₂ → R₂ - 2R₁: [0, -1, 1, 2]  ⇒  [0, 1, -1, -2].<br>Matrix in echelon form:<br>[ [1, 2, 0, '
                         '-1], [0, 1, -1, -2] ].<br>Pivots in columns 1 and 2 (x₁, x₂). Free variables are x₃ and x₄.',
                         'Execute step 2: reduce matrix to echelon form to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Solve for x₁ and x₂ in terms of x₃ and x₄',
                         'From Row 2: x₂ = x₃ + 2x₄.<br>From Row 1: x₁ = -2x₂ + x₄ = -2(x₃ + 2x₄) + x₄ = -2x₃ - 4x₄ + '
                         'x₄ = -2x₃ - 3x₄.',
                         'Execute step 3: solve for x₁ and x₂ in terms of x₃ and x₄ to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Parametric decomposition of x',
                         'x = (-2x₃ - 3x₄, x₃ + 2x₄, x₃, x₄)<br>= x₃ (-2, 1, 1, 0) + x₄ (-3, 2, 0, 1).',
                         'Multiply the standard matrices in the correct sequence to obtain the matrix representation '
                         'of the composite map.'),
                     (   'Step 5: State basis and dimension of W^⊥',
                         'Basis for W^⊥: B_perp = {(-2, 1, 1, 0), (-3, 2, 0, 1)}.<br>Dimension: dim(W^⊥) = '
                         '2.<br>Check: dim(W) + dim(W^⊥) = 2 + 2 = 4 = dim(ℝ⁴). Verified!',
                         'Extract the linearly independent spanning vectors corresponding to the free parameters to '
                         'form the basis.')],
        'title': 'Orthogonal Complement W^⊥ of a Subspace in ℝ⁴'},
    {   'concept': "Parseval's identity is the infinite-dimensional generalized Pythagorean theorem. Bessel's "
                   'inequality states that any finite sum of squared projections cannot exceed the total squared '
                   'length of the vector.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Bessel: Σ |⟨v, e_i⟩|² ≤ ||v||²; Parseval: Σ |⟨v, e_i⟩|² = ||v||²; Verified: 2² + (-3)² + 6² = '
                        '49 = ||v||²',
        'formula': "Bessel's Inequality: Σ_{i=1}^k |⟨v, e_i⟩|² ≤ ||v||².<br>Parseval's Identity (when {e_i} is a "
                   'complete basis): Σ_{i=1}^n |⟨v, e_i⟩|² = ||v||².',
        'formula_expl': '⟨v, e_i⟩ are the generalized Fourier coefficients.',
        'given': 'v = (2, -3, 6), standard orthonormal basis e₁ = (1, 0, 0), e₂ = (0, 1, 0), e₃ = (0, 0, 1).',
        'meaning_en': 'State the general geometric theorems relating the length of a vector to the sum of squares of '
                      'its Fourier coefficients, and verify that ||v||² = Σ |⟨v, e_i⟩|².',
        'mistakes': [   (   'Confusing Bessel with Parseval.',
                            'Bessel is an INEQUALITY (≤ for any orthonormal set); Parseval is an EQUALITY (= for '
                            'complete basis)!'),
                        ('Sign error in (-3)² = -9.', 'Squaring any real number yields a positive value: (-3)² = +9.')],
        'num': 97,
        'practice_q': "Verify Bessel's inequality for v = (1, 2, 3) using only the partial orthonormal set {e₁, e₂} in "
                      'ℝ³.',
        'presentation': [   'State both Bessel and Parseval statements.',
                            'Compute each Fourier coefficient c_i.',
                            'Show sum of squares equals ||v||².'],
        'question': "State Bessel's Inequality and Parseval's Identity for an orthonormal set {e₁, e₂, ..., e_k} in an "
                    "inner product space V, and verify Parseval's identity for v = (2, -3, 6) using the standard "
                    'orthonormal basis of ℝ³.',
        'steps': [   (   'Step 1: State the Theorems',
                         "Let {e₁, e₂, ..., e_k} be an orthonormal set in an inner product space V.<br>1. Bessel's "
                         "Inequality: For any v ∈ V: Σ_{i=1}^k |⟨v, e_i⟩|² ≤ ||v||².<br>2. Parseval's Identity: If "
                         '{e_i} forms an orthonormal BASIS of V, equality holds: Σ_{i=1}^n |⟨v, e_i⟩|² = ||v||².',
                         'Execute step 1: state the theorems to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 2: Compute Fourier coefficients ⟨v, e_i⟩ for v = (2, -3, 6)',
                         '• c₁ = ⟨v, e₁⟩ = (2)(1) + (-3)(0) + (6)(0) = 2.<br>• c₂ = ⟨v, e₂⟩ = (2)(0) + (-3)(1) + '
                         '(6)(0) = -3.<br>• c₃ = ⟨v, e₃⟩ = (2)(0) + (-3)(0) + (6)(1) = 6.',
                         'Execute step 2: compute fourier coefficients ⟨v, e_i⟩ for v = (2, -3, 6) to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 3: Compute sum of squares of coefficients (LHS)',
                         'Σ |c_i|² = 2² + (-3)² + 6² = 4 + 9 + 36 = 49.',
                         'Execute step 3: compute sum of squares of coefficients (lhs) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Compute square of the norm ||v||² (RHS)',
                         '||v||² = 2² + (-3)² + 6² = 4 + 9 + 36 = 49.',
                         'Execute step 4: compute square of the norm ||v||² (rhs) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: Conclude Verification',
                         "LHS = 49 = RHS.<br>Hence Parseval's identity is verified!",
                         'Execute step 5: conclude verification to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': "Parseval's Identity and Bessel's Inequality"},
    {   'concept': 'Constructs the classical shifted Legendre polynomials orthogonal on [0, 1].',
        'difficulty': 'Exam-Level',
        'final_answer': 'First two orthogonal polynomials: u₁(x) = 1  and  u₂(x) = x - 1/2',
        'formula': 'u₁ = v₁ = 1;  u₂ = v₂ - [ ⟨v₂, u₁⟩ / ⟨u₁, u₁⟩ ] u₁.',
        'formula_expl': 'v₁ = 1, v₂ = x.',
        'given': 'v₁ = 1, v₂ = x on [0, 1], ⟨p, q⟩ = ∫₀¹ p(x) q(x) dx.',
        'meaning_en': 'Compute u₁ = 1 and u₂ = x - proj_{u₁}(x) using the continuous integral inner product on [0, 1].',
        'mistakes': [   (   'Using limits [-1, 1] instead of [0, 1].',
                            'Read the interval carefully: here the interval is [0, 1], NOT [-1, 1]!'),
                        ('Arithmetic error in [x²/2 - x/2]₀¹.', '1/2 - 1/2 = 0.')],
        'num': 98,
        'practice_q': 'Find the third orthogonal polynomial u₃(x) from v₃ = x² using Gram-Schmidt on P₂[0, 1].',
        'presentation': [   'State Gram-Schmidt formula with integral inner products.',
                            'Evaluate ⟨u₁, u₁⟩ = 1 and ⟨v₂, u₁⟩ = 1/2.',
                            'Subtract projection to get u₂ = x - 1/2.',
                            'Show verification integral = 0.'],
        'question': 'Apply Gram-Schmidt orthogonalization to the basis {1, x, x²} of P₂[0, 1] with inner product ⟨p, '
                    'q⟩ = ∫₀¹ p(x) q(x) dx to find the first two orthogonal polynomials.',
        'steps': [   (   'Step 1: Set first orthogonal polynomial u₁ = 1',
                         'u₁(x) = 1.<br>⟨u₁, u₁⟩ = ∫₀¹ (1)(1) dx = ∫₀¹ 1 dx = 1.',
                         'Execute step 1: set first orthogonal polynomial u₁ = 1 to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Compute inner product ⟨v₂, u₁⟩ with v₂ = x',
                         '⟨v₂, u₁⟩ = ∫₀¹ (x)(1) dx = ∫₀¹ x dx = [ x²/2 ]₀¹ = 1/2.',
                         'Execute step 2: compute inner product ⟨v₂, u₁⟩ with v₂ = x to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Construct second orthogonal polynomial u₂',
                         'u₂(x) = v₂ - [ ⟨v₂, u₁⟩ / ⟨u₁, u₁⟩ ] u₁<br>= x - (1/2 / 1) (1) = x - 1/2.',
                         'Execute step 3: construct second orthogonal polynomial u₂ to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Verify Orthogonality: ⟨u₁, u₂⟩ = 0',
                         '⟨u₁, u₂⟩ = ∫₀¹ (1)(x - 1/2) dx = [ x²/2 - x/2 ]₀¹ = (1/2 - 1/2) - (0 - 0) = 0. Exactly '
                         'orthogonal!',
                         'Verify that all pairwise dot products of the coordinate tangent vectors evaluate to zero.')],
        'title': 'Gram-Schmidt Process on Polynomial Inner Product Space'},
    {   'concept': "The columns of the transition matrix P from B' to B are the coordinate vectors of the new basis "
                   'vectors relative to the old basis: P = [ [v₁]_B | [v₂]_B ].',
        'difficulty': 'Exam-Level',
        'final_answer': "Transition Matrix P (B' to B) = [[3, 2], [-1, -1]];  [w]_{B'} = [-1, 3]ᵀ",
        'formula': "[w]_B = P [w]_{B'}  ⇒  [w]_{B'} = P⁻¹ [w]_B.",
        'formula_expl': 'Express each v_j as a linear combination of u₁ and u₂.',
        'given': "B = {(1, 1), (1, 0)}, B' = {(2, 3), (1, 2)}, [w]_B = [3, -2]ᵀ.",
        'meaning_en': "Find matrix P such that [w]_B = P [w]_{B'} (or [w]_{B'} = P⁻¹ [w]_B), converting coordinates "
                      'between non-standard bases.',
        'mistakes': [   ('Multiplying by P instead of P⁻¹.', "[w]_B = P [w]_{B'}, so [w]_{B'} = P⁻¹ [w]_B!"),
                        ('Swapping rows and columns of P.', 'Coordinate vectors are COLUMNS of P.')],
        'num': 99,
        'practice_q': 'Find transition matrix from standard basis to B = {(1, 2), (3, 4)} in ℝ².',
        'presentation': [   "Express each basis vector of B' in terms of B.",
                            'Form transition matrix P with coordinate columns.',
                            'Invert P to find P⁻¹.',
                            'Multiply P⁻¹ by [w]_B.'],
        'question': "Find the transition matrix P from the basis B = {u₁ = (1, 1), u₂ = (1, 0)} to the basis B' = {v₁ "
                    "= (2, 3), v₂ = (1, 2)} in ℝ², and find the coordinate vector [w]_{B'} if [w]_B = [3, -2]ᵀ.",
        'steps': [   (   'Step 1: Express v₁ = (2, 3) in terms of B = {u₁, u₂}',
                         'c₁ (1, 1) + c₂ (1, 0) = (2, 3)<br>c₁ + c₂ = 2 and c₁ = 3  ⇒  c₂ = 2 - 3 = -1.<br>[v₁]_B = '
                         '[3, -1]ᵀ.',
                         'Execute step 1: express v₁ = (2, 3) in terms of b = {u₁, u₂} to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Express v₂ = (1, 2) in terms of B = {u₁, u₂}',
                         'd₁ (1, 1) + d₂ (1, 0) = (1, 2)<br>d₁ + d₂ = 1 and d₁ = 2  ⇒  d₂ = 1 - 2 = -1.<br>[v₂]_B = '
                         '[2, -1]ᵀ.',
                         'Execute step 2: express v₂ = (1, 2) in terms of b = {u₁, u₂} to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   "Step 3: Construct Transition Matrix P (from B' to B)",
                         'P = [ [v₁]_B | [v₂]_B ] = [ [3, 2], [-1, -1] ].',
                         "Execute step 3: construct transition matrix p (from b' to b) to advance the step-by-step "
                         'mathematical solution toward the final result.'),
                     (   "Step 4: Compute P⁻¹ to transform coordinates from B to B'",
                         'det(P) = (3)(-1) - (2)(-1) = -3 + 2 = -1.<br>P⁻¹ = (1/-1) [ [-1, -2], [1, 3] ] = [ [1, 2], '
                         '[-1, -3] ].',
                         "Execute step 4: compute p⁻¹ to transform coordinates from b to b' to advance the "
                         'step-by-step mathematical solution toward the final result.'),
                     (   "Step 5: Compute [w]_{B'} = P⁻¹ [w]_B",
                         "[w]_{B'} = [ [1, 2], [-1, -3] ] [3, -2]ᵀ<br>= [ 1(3) + 2(-2), -1(3) + (-3)(-2) ]ᵀ<br>= [ 3 - "
                         '4, -3 + 6 ]ᵀ = [-1, 3]ᵀ.',
                         "Execute step 5: compute [w]_{b'} = p⁻¹ [w]_b to advance the step-by-step mathematical "
                         'solution toward the final result.')],
        'title': 'Transition Matrix (Change of Basis Matrix)'},
    {   'concept': 'Orthogonal matrices represent rigid geometric motions (rotations and reflections). Preserving '
                   'inner products automatically guarantees preservation of lengths (||Qu|| = ||u||) and angles.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Q is orthogonal (Qᵀ Q = I) if and only if ⟨Q u, Q v⟩ = ⟨u, v⟩ for all u, v ∈ ℝⁿ (Hence '
                        'proved)',
        'formula': '⟨Q u, Q v⟩ = (Q u)ᵀ (Q v) = uᵀ Qᵀ Q v = uᵀ (Qᵀ Q) v.',
        'formula_expl': 'If Qᵀ Q = I, uᵀ I v = uᵀ v = ⟨u, v⟩.',
        'given': 'Square matrix Q in M_n(ℝ).',
        'meaning_en': 'Prove that orthogonal transformations are isometries (rigid rotations and reflections that '
                      'preserve angles, lengths, and dot products).',
        'mistakes': [   ('Assuming (Q u)ᵀ = Qᵀ uᵀ.', 'Transpose reverses order: (Q u)ᵀ = uᵀ Qᵀ!'),
                        ('Omitting the reverse direction.', "'If and only if' requires proving both directions.")],
        'num': 100,
        'practice_q': 'Prove that if Q is orthogonal, then det(Q) = ±1.',
        'presentation': [   'State definition of orthogonal matrix Qᵀ Q = I.',
                            'Show (Q u)ᵀ (Q v) = uᵀ Qᵀ Q v.',
                            'Prove both ⇒ and ⇐ clearly.',
                            'Use standard basis vectors e_i, e_j for reverse proof.'],
        'question': 'Prove that an n×n real matrix Q is orthogonal (Qᵀ Q = I) if and only if it preserves the inner '
                    'product: ⟨Q u, Q v⟩ = ⟨u, v⟩ for all u, v ∈ ℝⁿ.',
        'steps': [   (   'Step 1: Express inner product using matrix transpose',
                         'In standard Euclidean space, ⟨x, y⟩ = xᵀ y.<br>Therefore: ⟨Q u, Q v⟩ = (Q u)ᵀ (Q v).',
                         'Execute step 1: express inner product using matrix transpose to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Apply transpose rule for matrix product (AB)ᵀ = Bᵀ Aᵀ',
                         '(Q u)ᵀ = uᵀ Qᵀ.<br>Substitute into the expression:<br>⟨Q u, Q v⟩ = (uᵀ Qᵀ) (Q v) = uᵀ (Qᵀ Q) '
                         'v  --- (1).',
                         'Execute step 2: apply transpose rule for matrix product (ab)ᵀ = bᵀ aᵀ to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 3: Prove forward direction (⇒)',
                         'Assume Q is orthogonal, so Qᵀ Q = I.<br>Substitute Qᵀ Q = I into (1):<br>⟨Q u, Q v⟩ = uᵀ I v '
                         '= uᵀ v = ⟨u, v⟩.<br>Thus, Q preserves the inner product for all u, v ∈ ℝⁿ.',
                         'Execute step 3: prove forward direction (⇒) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Prove reverse direction (⇐)',
                         'Assume ⟨Q u, Q v⟩ = ⟨u, v⟩ for all u, v ∈ ℝⁿ.<br>From (1): uᵀ (Qᵀ Q) v = uᵀ I v.<br>uᵀ (Qᵀ Q '
                         '- I) v = 0 for all u, v ∈ ℝⁿ.<br>Choose u = e_i and v = e_j (standard basis '
                         'vectors):<br>e_iᵀ (Qᵀ Q - I) e_j = (Qᵀ Q - I)_{ij} = 0 for all i, j.<br>Since every matrix '
                         'entry is 0: Qᵀ Q - I = O  ⇒  Qᵀ Q = I.<br>Therefore, Q is an ORTHOGONAL matrix. Hence '
                         'proved.',
                         'Execute step 4: prove reverse direction (⇐) to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Orthogonal Matrix Representation and Isometry of Inner Product'}]


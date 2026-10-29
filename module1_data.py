# -*- coding: utf-8 -*-
"""
Module 1: Partial Differentiation, Jacobians, Series and Extrema
100% Pure English Edition
Includes 25 Fully Solved Questions (5 Fundamental + 10 Intermediate + 10 Exam-Level)
"""

MODULE1_QUESTIONS = [   {   'concept': 'Partial differentiation computes derivatives with respect to one variable while all other '
                   'independent variables are treated as constants.',
        'difficulty': 'Fundamental',
        'final_answer': '∂u/∂x = 3(x + y)²,  ∂u/∂y = 3(x + y)²',
        'formula': '∂u/∂x = d[f(x, y)]/dx with y = const; Power rule: d(xⁿ)/dx = n xⁿ⁻¹.',
        'formula_expl': '∂u/∂x denotes partial derivative with respect to x. Pure y terms differentiate to 0.',
        'given': 'u = x³ + 3x²y + 3xy² + y³.',
        'meaning_en': 'Find the rate of change of u with respect to x (holding y constant) and with respect to y '
                      '(holding x constant).',
        'mistakes': [   (   'Treating y as a function of x (dy/dx).',
                            'This is partial derivative, so y is purely an independent constant.'),
                        (   'Missing the product constant rule 3y·(2x).',
                            'Keep the constant factor outside the derivative.')],
        'num': 1,
        'practice_q': 'If u = 2x³ - 4x²y + 5xy² - y³, find ∂u/∂x and ∂u/∂y.',
        'presentation': [   'State clearly which variable is held constant.',
                            'Show term-by-term derivative.',
                            'Factorize into 3(x+y)².'],
        'question': 'If u = x³ + 3x²y + 3xy² + y³, find the first-order partial derivatives ∂u/∂x and ∂u/∂y.',
        'steps': [   (   'Step 1: Compute ∂u/∂x (treat y as constant)',
                         '∂u/∂x = 3x² + 3y(2x) + 3y²(1) + 0 = 3x² + 6xy + 3y² = 3(x + y)².',
                         'Execute step 1: compute ∂u/∂x (treat y as constant) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Compute ∂u/∂y (treat x as constant)',
                         '∂u/∂y = 0 + 3x²(1) + 3x(2y) + 3y² = 3x² + 6xy + 3y² = 3(x + y)².',
                         'Execute step 2: compute ∂u/∂y (treat x as constant) to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'First-Order Partial Derivatives of Polynomial Function'},
    {   'concept': 'For smooth functions with continuous second partial derivatives, the order of differentiation is '
                   'commutative.',
        'difficulty': 'Fundamental',
        'final_answer': '∂²u/∂x∂y = ∂²u/∂y∂x = 6x²y + 12xy² (Verified)',
        'formula': '∂²u/∂y∂x = ∂/∂y(∂u/∂x),  ∂²u/∂x∂y = ∂/∂x(∂u/∂y).',
        'formula_expl': "Clairaut's / Schwarz's theorem guarantees equality when second derivatives are continuous.",
        'given': 'u = x³y² + 2x²y³.',
        'meaning_en': 'Verify that differentiating first with respect to x then y gives the same result as '
                      'differentiating first with respect to y then x.',
        'mistakes': [   (   'Confusing ∂²u/∂x∂y with (∂u/∂x)(∂u/∂y).',
                            'It is repeated differentiation, not multiplication.'),
                        ('Careless power subtraction.', 'Check: d(y²)/dy = 2y, d(y³)/dy = 3y².')],
        'num': 2,
        'practice_q': 'If u = x⁴y² - 2x³y⁴, verify that ∂²u/∂x∂y = ∂²u/∂y∂x.',
        'presentation': [   'Label LHS and RHS clearly.',
                            'Show both first-order steps clearly before taking second-order derivatives.',
                            "State 'Hence verified'."],
        'question': "If u = x³y² + 2x²y³, verify Clairaut's theorem: ∂²u/∂x∂y = ∂²u/∂y∂x.",
        'steps': [   (   'Step 1: Compute ∂u/∂x',
                         '∂u/∂x = 3x²y² + 4xy³.',
                         'Execute step 1: compute ∂u/∂x to advance the step-by-step mathematical solution toward the '
                         'final result.'),
                     (   'Step 2: Differentiate ∂u/∂x with respect to y',
                         '∂²u/∂y∂x = ∂/∂y(3x²y² + 4xy³) = 3x²(2y) + 4x(3y²) = 6x²y + 12xy².',
                         'Execute step 2: differentiate ∂u/∂x with respect to y to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Compute ∂u/∂y',
                         '∂u/∂y = 2x³y + 6x²y².',
                         'Execute step 3: compute ∂u/∂y to advance the step-by-step mathematical solution toward the '
                         'final result.'),
                     (   'Step 4: Differentiate ∂u/∂y with respect to x',
                         '∂²u/∂x∂y = ∂/∂x(2x³y + 6x²y²) = 2(3x²)y + 6(2x)y² = 6x²y + 12xy².',
                         'Execute step 4: differentiate ∂u/∂y with respect to x to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: Conclude equality',
                         '∂²u/∂y∂x = 6x²y + 12xy² = ∂²u/∂x∂y. Hence verified.',
                         'Execute step 5: conclude equality to advance the step-by-step mathematical solution toward '
                         'the final result.')],
        'title': 'Equality of Mixed Second-Order Partial Derivatives'},
    {   'concept': "A function is homogeneous of degree n if f(tx, ty) = tⁿ f(x, y). Euler's theorem relates its first "
                   'partial derivatives directly to the function value.',
        'difficulty': 'Fundamental',
        'final_answer': "Degree n = 1; Euler's Theorem verified: x(∂u/∂x) + y(∂u/∂y) = u",
        'formula': 'x(∂u/∂x) + y(∂u/∂y) = n·u.',
        'formula_expl': 'n is the degree of homogeneity.',
        'given': 'u = (x² + y²) / (x + y).',
        'meaning_en': 'Determine degree n by scaling variables by t, then verify that x(∂u/∂x) + y(∂u/∂y) = n·u.',
        'mistakes': [   ('Thinking degree is 2.', 'Numerator degree minus denominator degree gives 2 - 1 = 1.'),
                        ('Sign error in quotient rule numerator.', "Formula is (v u' - u v')/v² with minus sign.")],
        'num': 3,
        'practice_q': "Find degree and verify Euler's theorem for u = (x³ + y³) / (x - y).",
        'presentation': [   'Show u(tx, ty) = tⁿ u(x, y) first.',
                            'State quotient rule explicitly.',
                            'Conclude with LHS = RHS.'],
        'question': "Find the degree of homogeneity of u = (x² + y²) / (x + y) and verify Euler's Theorem.",
        'steps': [   (   'Step 1: Determine degree n',
                         'u(tx, ty) = [(tx)² + (ty)²] / [tx + ty] = t²(x² + y²) / [t(x + y)] = t¹ u(x, y). Thus n = 1.',
                         'Execute step 1: determine degree n to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 2: Find ∂u/∂x using quotient rule',
                         '∂u/∂x = [(x+y)(2x) - (x²+y²)(1)] / (x+y)² = (2x² + 2xy - x² - y²) / (x+y)² = (x² + 2xy - y²) '
                         '/ (x+y)².<br>x(∂u/∂x) = (x³ + 2x²y - xy²) / (x+y)².',
                         "Apply the quotient rule [v u' - u v'] / v² treating the other variable as a constant."),
                     (   'Step 3: Find ∂u/∂y by symmetry',
                         '∂u/∂y = (y² + 2xy - x²) / (x+y)².<br>y(∂u/∂y) = (y³ + 2xy² - x²y) / (x+y)².',
                         'Exploit the algebraic symmetry between x and y to write the corresponding partial derivative '
                         'directly.'),
                     (   'Step 4: Add x(∂u/∂x) + y(∂u/∂y)',
                         'LHS = [x³ + y³ + x²y + xy²] / (x+y)² = [(x²+y²)(x+y)] / (x+y)² = (x²+y²)/(x+y) = 1·u = RHS.',
                         'Execute step 4: add x(∂u/∂x) + y(∂u/∂y) to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': "Homogeneous Function Degree and Euler's Theorem Verification"},
    {   'concept': 'The Jacobian represents the local scaling factor of area under coordinate transformation: dx dy = '
                   '|J| dr dθ.',
        'difficulty': 'Fundamental',
        'final_answer': 'J = ∂(x, y)/∂(r, θ) = r',
        'formula': 'J = ∂(x, y)/∂(r, θ) = (∂x/∂r)(∂y/∂θ) - (∂x/∂θ)(∂y/∂r).',
        'formula_expl': 'Determinant of the Jacobian matrix formed by row 1 = [∂x/∂r, ∂x/∂θ] and row 2 = [∂y/∂r, '
                        '∂y/∂θ].',
        'given': 'x = r cos θ, y = r sin θ.',
        'meaning_en': 'Evaluate the 2×2 determinant of first partial derivatives of x and y with respect to r and θ.',
        'mistakes': [   ('Derivative of cos θ written as +sin θ.', 'Derivative of cos θ is -sin θ.'),
                        ('Swapping rows and columns.', 'Keep x in row 1, y in row 2.')],
        'num': 4,
        'practice_q': 'If x = u(1 - v) and y = uv, find J = ∂(x, y)/∂(u, v).',
        'presentation': ['Write out the 2×2 determinant.', 'Substitute all 4 derivatives.', 'Use cos² θ + sin² θ = 1.'],
        'question': 'If x = r cos θ and y = r sin θ, evaluate the Jacobian J = ∂(x, y)/∂(r, θ).',
        'steps': [   (   'Step 1: Compute derivatives of x',
                         '∂x/∂r = cos θ,  ∂x/∂θ = -r sin θ.',
                         'Differentiate x partially with respect to each independent variable while holding other '
                         'variables fixed.'),
                     (   'Step 2: Compute derivatives of y',
                         '∂y/∂r = sin θ,  ∂y/∂θ = r cos θ.',
                         'Differentiate y partially with respect to each independent variable while holding other '
                         'variables fixed.'),
                     (   'Step 3: Set up and evaluate determinant',
                         'J = (cos θ)(r cos θ) - (-r sin θ)(sin θ) = r cos² θ + r sin² θ = r(cos² θ + sin² θ) = r(1) = '
                         'r.',
                         'Evaluate the Hessian discriminant D = rt - s²; D > 0 and r > 0 indicates a local minimum, '
                         'while D > 0 and r < 0 indicates a local maximum.')],
        'title': 'Jacobian of Polar Coordinate Transformation'},
    {   'concept': 'Critical points occur where gradient is zero. The sign of the Hessian determinant D determines '
                   'curvature.',
        'difficulty': 'Fundamental',
        'final_answer': 'Stationary point (2, 3) is a Local Minimum with minimum value f_min = 0.',
        'formula': 'fx = 0, fy = 0; D = rt - s² where r = f_xx, s = f_xy, t = f_yy. If D > 0, r > 0 → Minimum.',
        'formula_expl': 'r is concavity in x, D is overall Gaussian curvature sign.',
        'given': 'f(x, y) = x² + y² - 4x - 6y + 13.',
        'meaning_en': 'Find points where fx = 0 and fy = 0, and use D = rt - s² to classify the point as maximum, '
                      'minimum, or saddle point.',
        'mistakes': [   ('Thinking r > 0 means maximum.', 'In calculus, r > 0 means concave up, which is a minimum!'),
                        ('Calculating s as 2.', '∂(2x-4)/∂y = 0 because there is no y in fx.')],
        'num': 5,
        'practice_q': 'Find the stationary points of f(x, y) = 2x² + y² - 4x + 4y + 10 and determine its nature.',
        'presentation': [   'Solve fx = 0, fy = 0 clearly.',
                            'Compute r, s, t.',
                            'State D = rt - s² > 0 and r > 0 clearly.'],
        'question': 'Find the stationary points of f(x, y) = x² + y² - 4x - 6y + 13 and classify them.',
        'steps': [   (   'Step 1: Find first derivatives and set to zero',
                         'fx = 2x - 4 = 0 ⇒ x = 2.<br>fy = 2y - 6 = 0 ⇒ y = 3.<br>Stationary point is (2, 3).',
                         'Set the first partial derivatives fx = 0 and fy = 0 to solve for all stationary (critical) '
                         'points.'),
                     (   'Step 2: Find second partial derivatives',
                         'r = f_xx = 2,  s = f_xy = 0,  t = f_yy = 2.',
                         'Calculate the second-order partial derivatives r = fxx, s = fxy, and t = fyy to prepare for '
                         'the curvature test.'),
                     (   'Step 3: Evaluate D = rt - s²',
                         'D = (2)(2) - (0)² = 4 > 0 and r = 2 > 0.<br>Therefore, (2, 3) is a Local Minimum.<br>Minimum '
                         'value f(2, 3) = 2² + 3² - 4(2) - 6(3) + 13 = 4 + 9 - 8 - 18 + 13 = 0.',
                         'Evaluate the Hessian discriminant D = rt - s²; D > 0 and r > 0 indicates a local minimum, '
                         'while D > 0 and r < 0 indicates a local maximum.')],
        'title': 'Stationary Point and Nature of a Quadratic Surface'},
    {   'concept': 'When z depends on x and y, and both x and y depend on a single variable t, the rate of change of z '
                   'with respect to t flows through both intermediate variables x and y.',
        'difficulty': 'Intermediate',
        'final_answer': 'dz/dt = 7t⁶ e^(t⁷) (Chain rule verified by direct substitution)',
        'formula': 'dz/dt = (∂z/∂x)(dx/dt) + (∂z/∂y)(dy/dt).',
        'formula_expl': '∂z/∂x and ∂z/∂y are partial derivatives of outer function; dx/dt and dy/dt are ordinary '
                        'derivatives of inner functions.',
        'given': 'z = e^(xy²), x = t³, y = t².',
        'meaning_en': 'Compute the total derivative dz/dt using the multivariable chain rule dz/dt = (∂z/∂x)(dx/dt) + '
                      '(∂z/∂y)(dy/dt) and compare with direct single-variable differentiation.',
        'mistakes': [   ('Missing the exponent power (t²)² = t⁴.', 'Remember (t²)² = t⁴, so xy² = t³·t⁴ = t⁷.'),
                        ('Forgetting inner derivative in dy/dt.', 'd(t²)/dt = 2t.')],
        'num': 6,
        'practice_q': 'If z = x² + y², where x = cos t, y = sin t, find dz/dt using the chain rule and verify.',
        'presentation': [   'State multivariable chain rule formula first.',
                            'Compute all four components ∂z/∂x, ∂z/∂y, dx/dt, dy/dt.',
                            'Substitute t and combine terms.'],
        'question': 'If z = e^(xy²), where x = t³ and y = t², find dz/dt using the chain rule and verify by direct '
                    'substitution.',
        'steps': [   (   'Step 1: Compute partial derivatives of z',
                         '∂z/∂x = y² e^(xy²)<br>∂z/∂y = 2xy e^(xy²).',
                         'Differentiate z partially with respect to each independent variable while holding other '
                         'variables fixed.'),
                     (   'Step 2: Compute ordinary derivatives of x and y',
                         'dx/dt = d(t³)/dt = 3t²<br>dy/dt = d(t²)/dt = 2t.',
                         'Differentiate x partially with respect to each independent variable while holding other '
                         'variables fixed.'),
                     (   'Step 3: Apply the chain rule formula',
                         'dz/dt = [y² e^(xy²)](3t²) + [2xy e^(xy²)](2t)<br>= e^(xy²) [3t² y² + 4t xy].',
                         'Apply the multivariable chain rule by summing the product of partial and ordinary '
                         'derivatives.'),
                     (   'Step 4: Substitute x = t³ and y = t² in terms of t',
                         'xy² = (t³)(t²)² = t³ · t⁴ = t⁷.<br>3t² y² = 3t²(t⁴) = 3t⁶.<br>4t xy = 4t(t³)(t²) = '
                         '4t⁶.<br>dz/dt = e^(t⁷) [3t⁶ + 4t⁶] = 7t⁶ e^(t⁷).',
                         'Execute step 4: substitute x = t³ and y = t² in terms of t to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: Verify by direct substitution',
                         'z = e^(xy²) = e^((t³)(t²)²) = e^(t⁷).<br>dz/dt = d(e^(t⁷))/dt = e^(t⁷) · d(t⁷)/dt = 7t⁶ '
                         'e^(t⁷). Verified!',
                         'Substitute the parametric functions directly into the outer function and differentiate to '
                         'confirm the chain rule result.')],
        'title': 'Chain Rule for Functions of Two Independent Variables'},
    {   'concept': 'When u = g⁻¹[f(x, y)], where f(x, y) is homogeneous of degree n, we write g(u) = f(x, y). Then by '
                   "Euler's theorem on g(u): x(∂/∂x)[g(u)] + y(∂/∂y)[g(u)] = n g(u) ⇒ g'(u)[x u_x + y u_y] = n g(u) ⇒ "
                   "x u_x + y u_y = n g(u)/g'(u).",
        'difficulty': 'Intermediate',
        'final_answer': 'x(∂u/∂x) + y(∂u/∂y) = (1/2) tan u (Hence proved)',
        'formula': "If f(u) is homogeneous of degree n, then x(∂u/∂x) + y(∂u/∂y) = n [f(u) / f'(u)].",
        'formula_expl': "Here f(u) = sin u, so f'(u) = cos u, and f(u)/f'(u) = sin u / cos u = tan u.",
        'given': 'u = sin⁻¹[(x + y) / (√x + √y)].',
        'meaning_en': "Here u itself is not a homogeneous function, but sin u is homogeneous. We apply Euler's theorem "
                      'to f = sin u and relate it back to u.',
        'mistakes': [   (   'Applying Euler directly to sin⁻¹.',
                            'sin⁻¹ is NOT homogeneous! You must apply Euler to sin u.'),
                        ('Wrong degree calculation.', '√t = t^(1/2), so degree is 1 - 1/2 = 1/2, not 1/2 - 1 = -1/2.')],
        'num': 7,
        'practice_q': 'If u = cos⁻¹[(x + y) / (√x + √y)], prove that x(∂u/∂x) + y(∂u/∂y) = -(1/2) cot u.',
        'presentation': [   'Define z = sin u first.',
                            'Show z(tx, ty) = t^(1/2) z to establish degree n = 1/2 clearly.',
                            'Show factorizing cos u and dividing.'],
        'question': 'If u = sin⁻¹[(x + y) / (√x + √y)], prove that x(∂u/∂x) + y(∂u/∂y) = (1/2) tan u.',
        'steps': [   (   'Step 1: Rewrite u so the RHS is homogeneous',
                         'Let z = sin u = (x + y) / (√x + √y).',
                         'Execute step 1: rewrite u so the rhs is homogeneous to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Find the degree of homogeneity of z',
                         'z(tx, ty) = [tx + ty] / [√(tx) + √(ty)] = t(x + y) / [t^(1/2)(√x + √y)] = t^(1 - 1/2) · z = '
                         't^(1/2) z.<br>Thus, z is homogeneous of degree n = 1/2.',
                         'Substitute tx and ty for x and y to factor out t^n and establish the degree of homogeneity '
                         'n.'),
                     (   "Step 3: Apply Euler's Theorem to z",
                         'x(∂z/∂x) + y(∂z/∂y) = n · z = (1/2) z = (1/2) sin u.',
                         'Combine the partial derivatives into the linear combination x(∂u/∂x) + y(∂u/∂y) and verify '
                         'it equals n·u.'),
                     (   'Step 4: Express derivatives of z in terms of u',
                         'Since z = sin u:<br>∂z/∂x = cos u · (∂u/∂x)<br>∂z/∂y = cos u · (∂u/∂y).',
                         'Differentiate z partially with respect to each independent variable while holding other '
                         'variables fixed.'),
                     (   'Step 5: Substitute and solve for LHS',
                         'x [cos u (∂u/∂x)] + y [cos u (∂u/∂y)] = (1/2) sin u<br>cos u [x(∂u/∂x) + y(∂u/∂y)] = (1/2) '
                         'sin u<br>x(∂u/∂x) + y(∂u/∂y) = (1/2) (sin u / cos u) = (1/2) tan u. Hence proved.',
                         'Execute step 5: substitute and solve for lhs to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': "Euler's Theorem for Inverse Trigonometric Function"},
    {   'concept': 'The Jacobian of an inverse transformation is the reciprocal of the original Jacobian: [∂(u, '
                   'v)/∂(x, y)] · [∂(x, y)/∂(u, v)] = 1, analogous to (dy/dx) · (dx/dy) = 1 in single-variable '
                   'calculus.',
        'difficulty': 'Intermediate',
        'final_answer': "J = r,  J' = 1/r,  and  J · J' = r · (1/r) = 1 (Verified)",
        'formula': "J · J' = [∂(x, y)/∂(r, θ)] · [∂(r, θ)/∂(x, y)] = 1.",
        'formula_expl': 'Follows from chain rule of matrix determinants: det(A · A⁻¹) = det(I) = 1.',
        'given': 'x = r cos θ, y = r sin θ ⇒ r = √(x² + y²), θ = tan⁻¹(y/x).',
        'meaning_en': 'Compute the Jacobian of polar coordinates J, then invert the relations to get r and θ in terms '
                      "of x and y, compute the inverse Jacobian J', and verify that their product equals 1.",
        'mistakes': [   (   'Derivative of tan⁻¹(y/x) with respect to x missing minus sign.',
                            'd(1/x)/dx = -1/x², so a minus sign must appear in ∂θ/∂x.'),
                        (   'Forgetting to simplify x/(x²+y²) into cos θ / r.',
                            'Converting to polar coordinates simplifies the determinant algebra enormously.')],
        'num': 8,
        'practice_q': "If u = x + y and v = x - y, find J and J' and verify J · J' = 1.",
        'presentation': [   'State both forward and reverse relations.',
                            'Show step-by-step differentiation of r and θ.',
                            'Compute determinant and conclude product is 1.'],
        'question': "If x = r cos θ and y = r sin θ, find J = ∂(x, y)/∂(r, θ) and J' = ∂(r, θ)/∂(x, y), and verify "
                    "that J · J' = 1.",
        'steps': [   (   'Step 1: Recall J = ∂(x, y)/∂(r, θ)',
                         'From Question 4, J = r.',
                         'Execute step 1: recall j = ∂(x, y)/∂(r, θ) to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Express r and θ in terms of x and y',
                         'r² = x² + y²  ⇒  r = √(x² + y²)<br>tan θ = y/x  ⇒  θ = tan⁻¹(y/x).',
                         'Execute step 2: express r and θ in terms of x and y to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Compute partial derivatives of r',
                         '∂r/∂x = (1 / 2√(x²+y²)) · 2x = x/r = cos θ<br>∂r/∂y = (1 / 2√(x²+y²)) · 2y = y/r = sin θ.',
                         'Execute step 3: compute partial derivatives of r to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Compute partial derivatives of θ',
                         '∂θ/∂x = [1 / (1 + (y/x)²)] · (-y/x²) = -y / (x² + y²) = -sin θ / r<br>∂θ/∂y = [1 / (1 + '
                         '(y/x)²)] · (1/x) = x / (x² + y²) = cos θ / r.',
                         'Execute step 4: compute partial derivatives of θ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   "Step 5: Compute J' = ∂(r, θ)/∂(x, y)",
                         "J' = | ∂r/∂x  ∂r/∂y | / | ∂θ/∂x  ∂θ/∂y |<br>= (cos θ)(cos θ / r) - (sin θ)(-sin θ / r)<br>= "
                         '(cos² θ + sin² θ) / r = 1/r.',
                         "Execute step 5: compute j' = ∂(r, θ)/∂(x, y) to advance the step-by-step mathematical "
                         'solution toward the final result.'),
                     (   "Step 6: Verify J · J' = 1",
                         "J · J' = (r) · (1/r) = 1. Hence verified.",
                         "Execute step 6: verify j · j' = 1 to advance the step-by-step mathematical solution toward "
                         'the final result.')],
        'title': "Jacobian Property of Inverses J · J' = 1"},
    {   'concept': 'Maclaurin series for two variables approximates any smooth function near (0, 0) by a polynomial in '
                   'powers of x and y using partial derivatives evaluated at the origin.',
        'difficulty': 'Intermediate',
        'final_answer': 'eˣ cos y = 1 + x + (1/2)x² - (1/2)y² + ... (up to 2nd degree)',
        'formula': 'f(x, y) = f(0,0) + [x fx + y fy] + (1/2!)[x² fxx + 2xy fxy + y² fyy] + ... evaluated at (0, 0).',
        'formula_expl': 'The 1st bracket gives linear terms; 2nd bracket gives quadratic terms.',
        'given': 'f(x, y) = eˣ cos y, expansion point (a, b) = (0, 0).',
        'meaning_en': 'Find the Taylor series expansion of f(x, y) around the origin (0, 0) up to terms of degree 2.',
        'mistakes': [   (   'Derivative of cos y taken as +sin y.',
                            'd(cos y)/dy = -sin y, which brings a minus sign into fyy.'),
                        (   'Forgetting the factor 1/2! = 1/2 on second-order terms.',
                            'All 2nd degree terms are divided by 2!.')],
        'num': 9,
        'practice_q': 'Expand f(x, y) = eˣ sin y in powers of x and y up to second-degree terms.',
        'presentation': [   'Write general two-variable Maclaurin formula.',
                            'Create a neat table of derivatives at (0, 0).',
                            'Substitute carefully and box answer.'],
        'question': 'Expand f(x, y) = eˣ cos y in a Maclaurin series up to second-degree terms.',
        'steps': [   (   'Step 1: Evaluate f(0, 0)',
                         'f(0, 0) = e⁰ cos 0 = 1 · 1 = 1.',
                         'Execute step 1: evaluate f(0, 0) to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 2: Compute first derivatives and evaluate at (0, 0)',
                         'fx = ∂f/∂x = eˣ cos y  ⇒  fx(0, 0) = e⁰ cos 0 = 1.<br>fy = ∂f/∂y = -eˣ sin y  ⇒  fy(0, 0) = '
                         '-e⁰ sin 0 = 0.',
                         'Set the first partial derivatives fx = 0 and fy = 0 to solve for all stationary (critical) '
                         'points.'),
                     (   'Step 3: Compute second derivatives and evaluate at (0, 0)',
                         'fxx = ∂²f/∂x² = eˣ cos y  ⇒  fxx(0, 0) = 1.<br>fxy = ∂²f/∂x∂y = -eˣ sin y  ⇒  fxy(0, 0) = '
                         '0.<br>fyy = ∂²f/∂y² = -eˣ cos y  ⇒  fyy(0, 0) = -1.',
                         'Execute step 3: compute second derivatives and evaluate at (0, 0) to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 4: Substitute into Maclaurin series formula',
                         'f(x, y) = 1 + [x(1) + y(0)] + (1/2)[x²(1) + 2xy(0) + y²(-1)]<br>= 1 + x + (1/2)(x² - '
                         'y²)<br>= 1 + x + (1/2)x² - (1/2)y².',
                         'Substitute the evaluated derivative values into the multivariable Taylor/Maclaurin series '
                         'formula and group terms by degree.')],
        'title': 'Maclaurin Series Expansion of Two Variables: eˣ cos y'},
    {   'concept': 'Taylor series around (a, b) replaces x by (x - a) and y by (y - b), with derivatives evaluated at '
                   '(a, b).',
        'difficulty': 'Intermediate',
        'final_answer': 'f(x, y) = 2 + 2(x - 1) + 4(y - 1) + (x - 1)² + 2(x - 1)(y - 1)',
        'formula': 'f(x, y) = f(a, b) + [(x-a)fx + (y-b)fy] + (1/2!)[(x-a)²fxx + 2(x-a)(y-b)fxy + (y-b)²fyy] + ...',
        'formula_expl': '(a, b) = (1, 1); h = x - 1, k = y - 1.',
        'given': 'f(x, y) = x²y + 3y - 2, point (a, b) = (1, 1).',
        'meaning_en': "Expand the polynomial f(x, y) in terms of powers of (x - 1) and (y - 1) using Taylor's theorem "
                      'around the point (a, b) = (1, 1).',
        'mistakes': [   (   'Expanding (x - 1)² into x² - 2x + 1.',
                            'The question asks for expansion IN POWERS of (x - 1) and (y - 1), so do NOT expand the '
                            'brackets!'),
                        (   'Evaluating derivatives at (0, 0) instead of (1, 1).',
                            'Check the expansion point carefully.')],
        'num': 10,
        'practice_q': 'Expand f(x, y) = x² + xy + y² in powers of (x - 1) and (y - 2) up to second degree.',
        'presentation': [   "State Taylor's formula around (a, b).",
                            'Show all derivatives evaluated at (1, 1).',
                            'Keep terms in powers of (x - 1) and (y - 1) without expanding them.'],
        'question': 'Expand f(x, y) = x²y + 3y - 2 in powers of (x - 1) and (y - 1) up to second-degree terms.',
        'steps': [   (   'Step 1: Evaluate f(1, 1)',
                         'f(1, 1) = (1)²(1) + 3(1) - 2 = 1 + 3 - 2 = 2.',
                         'Execute step 1: evaluate f(1, 1) to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 2: First-order derivatives at (1, 1)',
                         'fx = 2xy  ⇒  fx(1, 1) = 2(1)(1) = 2.<br>fy = x² + 3  ⇒  fy(1, 1) = (1)² + 3 = 4.',
                         'Execute step 2: first-order derivatives at (1, 1) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Second-order derivatives at (1, 1)',
                         'fxx = 2y  ⇒  fxx(1, 1) = 2(1) = 2.<br>fxy = 2x  ⇒  fxy(1, 1) = 2(1) = 2.<br>fyy = 0  ⇒  '
                         'fyy(1, 1) = 0.',
                         'Calculate the second-order partial derivatives r = fxx, s = fxy, and t = fyy to prepare for '
                         'the curvature test.'),
                     (   "Step 4: Substitute into Taylor's formula",
                         'f(x, y) = 2 + [(x - 1)(2) + (y - 1)(4)] + (1/2)[(x - 1)²(2) + 2(x - 1)(y - 1)(2) + (y - '
                         '1)²(0)]<br>= 2 + 2(x - 1) + 4(y - 1) + (x - 1)² + 2(x - 1)(y - 1).',
                         'Substitute the evaluated derivative values into the multivariable Taylor/Maclaurin series '
                         'formula and group terms by degree.')],
        'title': 'Taylor Series Expansion Around a Non-Zero Point (1, 1)'},
    {   'concept': 'If ∂(u, v)/∂(x, y) = 0 identically, there exists a functional relation F(u, v) = 0.',
        'difficulty': 'Intermediate',
        'final_answer': 'J = ∂(u, v)/∂(x, y) = 0 (Functionally Dependent); Relationship: u = tan v (or v = tan⁻¹ u)',
        'formula': 'J = (∂u/∂x)(∂v/∂y) - (∂u/∂y)(∂v/∂x) = 0.',
        'formula_expl': 'Identically vanishing Jacobian proves functional dependence.',
        'given': 'u = (x + y)/(1 - xy), v = tan⁻¹ x + tan⁻¹ y.',
        'meaning_en': 'Two functions u and v are functionally dependent if their Jacobian J = ∂(u, v)/∂(x, y) is '
                      'identically zero. If dependent, find the equation connecting u and v.',
        'mistakes': [   (   'Not simplifying terms before taking determinant.',
                            'Cancel (1+y²) with 1/(1+y²) to avoid messy expressions.'),
                        (   'Forgetting to find the relationship.',
                            'Both proving J = 0 and writing u = tan v are required.')],
        'num': 11,
        'practice_q': 'Show that u = x + y and v = x/(x + y) are functionally dependent and find the relation.',
        'presentation': [   'State theorem: J = 0 implies functional dependence.',
                            'Show cancellation of (1+y²) and (1+x²).',
                            'Write the relationship clearly.'],
        'question': 'Show that the functions u = (x + y)/(1 - xy) and v = tan⁻¹ x + tan⁻¹ y are functionally '
                    'dependent, and find the relationship between them.',
        'steps': [   (   'Step 1: Compute partial derivatives of u',
                         '∂u/∂x = [(1 - xy)(1) - (x + y)(-y)] / (1 - xy)² = [1 - xy + xy + y²] / (1 - xy)² = (1 + y²) '
                         '/ (1 - xy)².<br>By symmetry: ∂u/∂y = (1 + x²) / (1 - xy)².',
                         'Execute step 1: compute partial derivatives of u to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Compute partial derivatives of v',
                         '∂v/∂x = 1 / (1 + x²)<br>∂v/∂y = 1 / (1 + y²).',
                         'Execute step 2: compute partial derivatives of v to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Evaluate the Jacobian determinant J',
                         'J = (∂u/∂x)(∂v/∂y) - (∂u/∂y)(∂v/∂x)<br>= [(1 + y²)/(1 - xy)²] · [1/(1 + y²)] - [(1 + x²)/(1 '
                         '- xy)²] · [1/(1 + x²)]<br>= 1/(1 - xy)² - 1/(1 - xy)² = 0.',
                         'Construct the Jacobian determinant of partial derivatives and simplify using standard '
                         'trigonometric/algebraic identities.'),
                     (   'Step 4: Find the functional relationship',
                         'Recall standard trigonometric identity: tan⁻¹ x + tan⁻¹ y = tan⁻¹[(x + y)/(1 - '
                         'xy)].<br>Since v = tan⁻¹ x + tan⁻¹ y and u = (x + y)/(1 - xy):<br>v = tan⁻¹ u   or   u = tan '
                         'v.',
                         'Execute step 4: find the functional relationship to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Jacobian for Functional Dependence and Relationship'},
    {   'concept': 'A two-variable function can have multiple critical points. Each must be tested individually using '
                   'the second derivative test.',
        'difficulty': 'Intermediate',
        'final_answer': 'At (0, 0): Saddle point. At (1, 1): Local Minimum with minimum value f_min = -1.',
        'formula': 'fx = 3x² - 3y = 0, fy = 3y² - 3x = 0; D = rt - s².',
        'formula_expl': 'r = fxx, s = fxy, t = fyy.',
        'given': 'f(x, y) = x³ + y³ - 3xy.',
        'meaning_en': 'Locate all stationary points of f(x, y) by setting fx = 0, fy = 0, then use D = rt - s² to find '
                      'local maxima and minima.',
        'mistakes': [   (   'Dividing by x in x⁴ = x and losing the root x = 0.',
                            'Never divide by the variable! Factorize as x(x³ - 1) = 0.'),
                        (   'Classifying (0, 0) as minimum because f(0,0)=0 > -1.',
                            'Local nature is determined ONLY by the sign of D, not function value!')],
        'num': 12,
        'practice_q': 'Find the stationary points and extreme values of f(x, y) = x³ + 3xy² - 15x² - 15y² + 72x.',
        'presentation': [   'Solve non-linear system x = y², y = x² clearly.',
                            'List both stationary points in a table.',
                            'Evaluate D and r at each point clearly.'],
        'question': 'Find the extreme values of f(x, y) = x³ + y³ - 3xy.',
        'steps': [   (   'Step 1: Set first derivatives to zero',
                         'fx = 3x² - 3y = 0  ⇒  y = x²<br>fy = 3y² - 3x = 0  ⇒  x = y².<br>Substitute y = x² into '
                         'second equation:<br>x = (x²)² = x⁴  ⇒  x⁴ - x = 0  ⇒  x(x³ - 1) = 0.<br>Real roots: x = 0 or '
                         'x = 1.<br>• If x = 0 ⇒ y = 0² = 0. Point: (0, 0).<br>• If x = 1 ⇒ y = 1² = 1. Point: (1, '
                         '1).<br>Two stationary points: (0, 0) and (1, 1).',
                         'Set the first partial derivatives fx = 0 and fy = 0 to solve for all stationary (critical) '
                         'points.'),
                     (   'Step 2: Second partial derivatives expressions',
                         'r = fxx = 6x,  s = fxy = -3,  t = fyy = 6y.<br>Discriminant: D(x, y) = rt - s² = (6x)(6y) - '
                         '(-3)² = 36xy - 9.',
                         'Calculate the second-order partial derivatives r = fxx, s = fxy, and t = fyy to prepare for '
                         'the curvature test.'),
                     (   'Step 3: Test Point (0, 0)',
                         'At (0, 0): r = 0, s = -3, t = 0.<br>D = 36(0)(0) - 9 = -9 < 0.<br>Since D < 0, (0, 0) is a '
                         'SADDLE POINT (neither maximum nor minimum).',
                         'Evaluate the Hessian discriminant D = rt - s²; D > 0 and r > 0 indicates a local minimum, '
                         'while D > 0 and r < 0 indicates a local maximum.'),
                     (   'Step 4: Test Point (1, 1)',
                         'At (1, 1): r = 6(1) = 6, s = -3, t = 6(1) = 6.<br>D = 36(1)(1) - 9 = 27 > 0 and r = 6 > '
                         '0.<br>Since D > 0 and r > 0, (1, 1) is a LOCAL MINIMUM.<br>Minimum value: f(1, 1) = 1³ + 1³ '
                         '- 3(1)(1) = 1 + 1 - 3 = -1.',
                         'Evaluate the Hessian discriminant D = rt - s²; D > 0 and r > 0 indicates a local minimum, '
                         'while D > 0 and r < 0 indicates a local maximum.')],
        'title': 'Stationary Points and Extrema of a Two-Variable Cubic'},
    {   'concept': 'The spherical Jacobian represents the volume differential element in triple integration: dx dy dz '
                   '= r² sin θ dr dθ dφ.',
        'difficulty': 'Intermediate',
        'final_answer': 'J = ∂(x, y, z)/∂(r, θ, φ) = r² sin θ',
        'formula': 'J = det [∂(x, y, z)/∂(r, θ, φ)].',
        'formula_expl': 'Row 1: [∂x/∂r, ∂x/∂θ, ∂x/∂φ], Row 2: [∂y/∂r, ∂y/∂θ, ∂y/∂φ], Row 3: [∂z/∂r, ∂z/∂θ, ∂z/∂φ].',
        'given': 'x = r sin θ cos φ, y = r sin θ sin φ, z = r cos θ.',
        'meaning_en': 'Calculate the 3×3 Jacobian determinant of the transformation from Cartesian coordinates (x, y, '
                      'z) to spherical coordinates (r, θ, φ).',
        'mistakes': [   ('Expanding along Row 1.', 'Expanding along Row 3 is much faster because ∂z/∂φ = 0.'),
                        (   'Sign error with (-r sin θ).',
                            'The (3, 2) cofactor position has a minus sign: -(-r sin θ) = +r sin θ.')],
        'num': 13,
        'practice_q': 'If x = ρ cos φ, y = ρ sin φ, z = z, find the Jacobian ∂(x, y, z)/∂(ρ, φ, z) in cylindrical '
                      'coordinates.',
        'presentation': [   'Write out the full 3×3 matrix.',
                            'Expand along the 3rd row because it contains a zero.',
                            'Factor out r² sin θ.'],
        'question': 'If x = r sin θ cos φ, y = r sin θ sin φ, z = r cos θ, evaluate J = ∂(x, y, z)/∂(r, θ, φ).',
        'steps': [   (   'Step 1: Compute partial derivatives for Row 1 (x)',
                         '∂x/∂r = sin θ cos φ<br>∂x/∂θ = r cos θ cos φ<br>∂x/∂φ = -r sin θ sin φ.',
                         'Execute step 1: compute partial derivatives for row 1 (x) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Compute partial derivatives for Row 2 (y)',
                         '∂y/∂r = sin θ sin φ<br>∂y/∂θ = r cos θ sin φ<br>∂y/∂φ = r sin θ cos φ.',
                         'Execute step 2: compute partial derivatives for row 2 (y) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Compute partial derivatives for Row 3 (z)',
                         '∂z/∂r = cos θ<br>∂z/∂θ = -r sin θ<br>∂z/∂φ = 0 (since z has no φ).',
                         'Execute step 3: compute partial derivatives for row 3 (z) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Expand determinant along Row 3',
                         'J = cos θ · | r cos θ cos φ   -r sin θ sin φ |<br>            | r cos θ sin φ    r sin θ cos '
                         'φ |<br>  - (-r sin θ) · | sin θ cos φ   -r sin θ sin φ |<br>                 | sin θ sin '
                         'φ    r sin θ cos φ |  + 0.<br>= cos θ [ r² sin θ cos θ (cos² φ + sin² φ) ] + r sin θ [ r '
                         'sin² θ (cos² φ + sin² φ) ]<br>= cos θ [ r² sin θ cos θ (1) ] + r sin θ [ r sin² θ (1) ]<br>= '
                         'r² sin θ cos² θ + r² sin³ θ<br>= r² sin θ (cos² θ + sin² θ) = r² sin θ (1) = r² sin θ.',
                         'Execute step 4: expand determinant along row 3 to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Jacobian of 3-Variable Spherical Polar Coordinates'},
    {   'concept': "When a function has equal powers in numerator and denominator, its degree is n = 0. Euler's "
                   'second-order theorem states: x² u_xx + 2xy u_xy + y² u_yy = n(n - 1)u.',
        'difficulty': 'Intermediate',
        'final_answer': 'x(∂u/∂x) + y(∂u/∂y) = 0 and x²(∂²u/∂x²) + 2xy(∂²u/∂x∂y) + y²(∂²u/∂y²) = 0 (Proved)',
        'formula': 'First-order: x u_x + y u_y = n u = 0·u = 0.<br>Second-order: x² u_xx + 2xy u_xy + y² u_yy = n(n - '
                   '1)u = 0(-1)u = 0.',
        'formula_expl': 'For n = 0, both n·u and n(n - 1)u vanish identically.',
        'given': 'u = tan⁻¹(y/x).',
        'meaning_en': 'Show that u is homogeneous of degree 0, then verify both the first and second-order forms of '
                      "Euler's Theorem.",
        'mistakes': [   (   'Thinking degree is undefined.',
                            't cancels completely, meaning t⁰ = 1, so degree is 0, not undefined.'),
                        (   'Long calculations for 2nd derivatives.',
                            "Using Euler's theorem n(n-1)u saves two pages of tedious algebra.")],
        'num': 14,
        'practice_q': 'If u = log[(x² + y²)/(xy)], show that x(∂u/∂x) + y(∂u/∂y) = 0.',
        'presentation': [   'State n = 0 clearly from u(tx, ty) = t⁰ u.',
                            'Show cancellation for first-order directly.',
                            "Quote Euler's second-order theorem x²r + 2xys + y²t = n(n-1)u."],
        'question': 'If u = tan⁻¹(y/x), show that x(∂u/∂x) + y(∂u/∂y) = 0 and x²(∂²u/∂x²) + 2xy(∂²u/∂x∂y) + '
                    'y²(∂²u/∂y²) = 0.',
        'steps': [   (   'Step 1: Check degree of homogeneity',
                         'u(tx, ty) = tan⁻¹(ty / tx) = tan⁻¹(y / x) = t⁰ u(x, y).<br>Therefore, u is a homogeneous '
                         'function of degree n = 0.',
                         'Substitute tx and ty for x and y to factor out t^n and establish the degree of homogeneity '
                         'n.'),
                     (   'Step 2: Compute first derivatives',
                         '∂u/∂x = [1 / (1 + (y/x)²)] · (-y/x²) = -y / (x² + y²).<br>∂u/∂y = [1 / (1 + (y/x)²)] · (1/x) '
                         '= x / (x² + y²).',
                         'Set the first partial derivatives fx = 0 and fy = 0 to solve for all stationary (critical) '
                         'points.'),
                     (   'Step 3: Verify first-order Euler theorem',
                         'x(∂u/∂x) + y(∂u/∂y) = x[-y/(x²+y²)] + y[x/(x²+y²)] = (-xy + xy)/(x²+y²) = 0.<br>Matches n·u '
                         '= 0 · u = 0. Verified!',
                         'Combine the partial derivatives into the linear combination x(∂u/∂x) + y(∂u/∂y) and verify '
                         'it equals n·u.'),
                     (   'Step 4: Verify second-order Euler theorem',
                         "By Euler's 2nd-order theorem:<br>x² u_xx + 2xy u_xy + y² u_yy = n(n - 1) u.<br>Since n = "
                         '0:<br>n(n - 1) u = 0(0 - 1) u = 0. Hence proved.',
                         "Apply Euler's second-order theorem x²r + 2xys + y²t = n(n-1)u to evaluate the quadratic "
                         'derivative form.')],
        'title': 'Homogeneous Function of Degree Zero: u = tan⁻¹(y/x)'},
    {   'concept': 'When z = f(u, v), ∂z/∂x = (∂z/∂u)(∂u/∂x) + (∂z/∂v)(∂v/∂x) and ∂z/∂y = (∂z/∂u)(∂u/∂y) + '
                   '(∂z/∂v)(∂v/∂y).',
        'difficulty': 'Intermediate',
        'final_answer': 'y(∂z/∂x) + x(∂z/∂y) = 2(x² + y²)(∂z/∂v) (Hence proved)',
        'formula': '∂z/∂x = f_u u_x + f_v v_x;  ∂z/∂y = f_u u_y + f_v v_y.',
        'formula_expl': 'u_x = 2x, u_y = -2y, v_x = 2y, v_y = 2x.',
        'given': 'z = f(u, v), u = x² - y², v = 2xy.',
        'meaning_en': 'Use the multivariable chain rule to express ∂z/∂x and ∂z/∂y in terms of ∂z/∂u and ∂z/∂v, then '
                      'compute the linear combination y(∂z/∂x) + x(∂z/∂y).',
        'mistakes': [   (   'Sign error: ∂u/∂y = +2y instead of -2y.',
                            'd(-y²)/dy = -2y. The minus sign is vital for cancellation!'),
                        (   'Treating z as a product instead of general function f(u, v).',
                            'Keep ∂z/∂u and ∂z/∂v as operators.')],
        'num': 15,
        'practice_q': 'If z = f(x - y, y - z), show that ∂z/∂x + ∂z/∂y + ∂z/∂z = 0.',
        'presentation': [   'Write chain rule formulas clearly.',
                            'Show the multiplier y and x on each line.',
                            'Highlight the cancellation of the ∂z/∂u terms.'],
        'question': 'If z = f(u, v) where u = x² - y² and v = 2xy, prove that y(∂z/∂x) + x(∂z/∂y) = 2(x² + y²)(∂z/∂v).',
        'steps': [   (   'Step 1: Compute derivatives of u and v',
                         '∂u/∂x = 2x,   ∂u/∂y = -2y<br>∂v/∂x = 2y,   ∂v/∂y = 2x.',
                         'Execute step 1: compute derivatives of u and v to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Express ∂z/∂x using chain rule',
                         '∂z/∂x = (∂z/∂u)(2x) + (∂z/∂v)(2y) = 2x(∂z/∂u) + 2y(∂z/∂v).<br>Multiply by y: y(∂z/∂x) = '
                         '2xy(∂z/∂u) + 2y²(∂z/∂v).',
                         'Execute step 2: express ∂z/∂x using chain rule to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Express ∂z/∂y using chain rule',
                         '∂z/∂y = (∂z/∂u)(-2y) + (∂z/∂v)(2x) = -2y(∂z/∂u) + 2x(∂z/∂v).<br>Multiply by x: x(∂z/∂y) = '
                         '-2xy(∂z/∂u) + 2x²(∂z/∂v).',
                         'Execute step 3: express ∂z/∂y using chain rule to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Add the two equations',
                         'LHS = y(∂z/∂x) + x(∂z/∂y)<br>= [2xy(∂z/∂u) - 2xy(∂z/∂u)] + [2y²(∂z/∂v) + 2x²(∂z/∂v)]<br>= 0 '
                         '+ 2(x² + y²)(∂z/∂v)<br>= 2(x² + y²)(∂z/∂v) = RHS. Hence proved.',
                         'Execute step 4: add the two equations to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Composite Partial Differentiation (Chain Rule with Intermediate Variables)'},
    {   'concept': 'Standard VTU exam problem. Let z = tan u = f(x, y). Since f is homogeneous of degree n = 3 - 1 = '
                   "2, Euler's theorem gives x z_x + y z_y = 2z. Then using chain rule z_x = sec² u · u_x yields 2 tan "
                   'u / sec² u = 2 sin u cos u = sin 2u.',
        'difficulty': 'Exam-Level',
        'final_answer': 'x(∂u/∂x) + y(∂u/∂y) = sin 2u (Hence proved)',
        'formula': "x(∂u/∂x) + y(∂u/∂y) = n [f(u) / f'(u)] = 2 [tan u / sec² u] = sin 2u.",
        'formula_expl': 'tan u = sin u / cos u; dividing by sec² u = 1/cos² u gives sin u cos u.',
        'given': 'u = tan⁻¹[(x³ + y³) / (x - y)].',
        'meaning_en': "Express tan u as a homogeneous function of degree 2, apply Euler's Theorem, and use "
                      'trigonometric identity to prove the result equals sin 2u.',
        'mistakes': [   ('Saying u is homogeneous of degree 2.', 'u is NOT homogeneous. tan u is homogeneous!'),
                        (   'Leaving answer as 2 tan u / sec² u.',
                            'Always simplify to the standard double-angle identity sin 2u.')],
        'num': 16,
        'practice_q': 'If u = tan⁻¹[(x² + y²) / (x + y)], prove that x(∂u/∂x) + y(∂u/∂y) = (1/2) sin 2u.',
        'presentation': [   'State z = tan u is homogeneous of degree 2.',
                            "Write Euler's theorem on z clearly.",
                            'Show trigonometric conversion: 2 tan u / sec² u = 2 sin u cos u = sin 2u.'],
        'question': 'If u = tan⁻¹[(x³ + y³) / (x - y)], prove that x(∂u/∂x) + y(∂u/∂y) = sin 2u.',
        'steps': [   (   'Step 1: Define z = tan u',
                         'tan u = (x³ + y³) / (x - y) = z(x, y).',
                         'Execute step 1: define z = tan u to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 2: Find degree of z',
                         'z(tx, ty) = [(tx)³ + (ty)³] / [tx - ty] = t³(x³ + y³) / [t(x - y)] = t² z(x, '
                         'y).<br>Therefore, z is homogeneous of degree n = 3 - 1 = 2.',
                         'Execute step 2: find degree of z to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   "Step 3: Apply Euler's Theorem to z",
                         'x(∂z/∂x) + y(∂z/∂y) = n · z = 2z = 2 tan u.',
                         'Combine the partial derivatives into the linear combination x(∂u/∂x) + y(∂u/∂y) and verify '
                         'it equals n·u.'),
                     (   'Step 4: Express derivatives in terms of u',
                         '∂z/∂x = sec² u (∂u/∂x),   ∂z/∂y = sec² u (∂u/∂y).<br>Substitute into Euler equation:<br>x '
                         '[sec² u (∂u/∂x)] + y [sec² u (∂u/∂y)] = 2 tan u<br>sec² u [x(∂u/∂x) + y(∂u/∂y)] = 2 tan u.',
                         'Execute step 4: express derivatives in terms of u to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 5: Divide by sec² u and simplify with trigonometry',
                         'x(∂u/∂x) + y(∂u/∂y) = 2 tan u / sec² u<br>= 2 (sin u / cos u) · cos² u = 2 sin u cos u = sin '
                         '2u. Hence proved.',
                         'Compute the sum of partial derivatives of the component functions along their respective '
                         'coordinate axes.')],
        'title': "Euler's Theorem on Inverse Tangent: x u_x + y u_y = sin 2u"},
    {   'concept': "Let G(u) = x u_x + y u_y. Then x² u_xx + 2xy u_xy + y² u_yy = G(u)[G'(u) - 1]. Since G(u) = sin "
                   "2u, G'(u) = 2 cos 2u, so result is sin 2u (2 cos 2u - 1).",
        'difficulty': 'Exam-Level',
        'final_answer': 'x²(∂²u/∂x²) + 2xy(∂²u/∂x∂y) + y²(∂²u/∂y²) = sin 2u (2 cos 2u - 1) = 2 cos 3u sin u',
        'formula': "x² u_xx + 2xy u_xy + y² u_yy = f(u)[f'(u) - 1] where f(u) = sin 2u.",
        'formula_expl': "f(u) = sin 2u ⇒ f'(u) = 2 cos 2u. Therefore f(u)[f'(u) - 1] = sin 2u (2 cos 2u - 1).",
        'given': 'u = tan⁻¹[(x³ + y³) / (x - y)] ⇒ x u_x + y u_y = sin 2u.',
        'meaning_en': "Differentiate Euler's first-order result partially with respect to x and y, combine, and obtain "
                      'the second-order partial differential relation.',
        'mistakes': [   ('Forgetting the product rule on x u_x.', 'd(x u_x)/dx = 1·u_x + x u_xx.'),
                        ('Forgetting the inner derivative u_x on RHS.', 'd(sin 2u)/dx = 2 cos 2u · (∂u/∂x).')],
        'num': 17,
        'practice_q': 'If u = sin⁻¹[(x² + y²)/(x + y)], prove that x² u_xx + 2xy u_xy + y² u_yy = tan u (tan² u - 1) / '
                      '4 (or standard form).',
        'presentation': [   'Show differentiation with respect to x and y step by step.',
                            "Use Clairaut's theorem u_xy = u_yx.",
                            'Factor out (2 cos 2u - 1) and substitute x u_x + y u_y = sin 2u.'],
        'question': 'If u = tan⁻¹[(x³ + y³) / (x - y)], prove that x²(∂²u/∂x²) + 2xy(∂²u/∂x∂y) + y²(∂²u/∂y²) = (1 - 4 '
                    'sin² u) sin 2u / ... = 2 cos 3u sin u (or standard form).',
        'steps': [   (   'Step 1: Recall the first-order result',
                         'From Question 16: x(∂u/∂x) + y(∂u/∂y) = sin 2u = f(u).',
                         'Execute step 1: recall the first-order result to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Differentiate with respect to x',
                         '∂/∂x [x u_x + y u_y] = ∂/∂x [sin 2u]<br>1 · u_x + x u_xx + y u_yx = 2 cos 2u · u_x<br>x u_xx '
                         '+ y u_xy = 2 cos 2u · u_x - u_x = (2 cos 2u - 1) u_x.<br>Multiply by x: x² u_xx + xy u_xy = '
                         '(2 cos 2u - 1) x u_x.',
                         'Execute step 2: differentiate with respect to x to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Differentiate with respect to y',
                         '∂/∂y [x u_x + y u_y] = ∂/∂y [sin 2u]<br>x u_xy + 1 · u_y + y u_yy = 2 cos 2u · u_y<br>x u_xy '
                         '+ y u_yy = (2 cos 2u - 1) u_y.<br>Multiply by y: xy u_xy + y² u_yy = (2 cos 2u - 1) y u_y.',
                         'Execute step 3: differentiate with respect to y to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Add the two equations',
                         'LHS = x² u_xx + 2xy u_xy + y² u_yy<br>= (2 cos 2u - 1) [x u_x + y u_y]<br>= (2 cos 2u - 1) '
                         'sin 2u<br>= sin 2u (2 cos 2u - 1).',
                         'Execute step 4: add the two equations to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 5: Express in alternative trigonometric forms if requested',
                         'sin 2u (2 cos 2u - 1) = 2 sin 2u cos 2u - sin 2u = sin 4u - sin 2u<br>= 2 cos 3u sin u.',
                         'Execute step 5: express in alternative trigonometric forms if requested to advance the '
                         'step-by-step mathematical solution toward the final result.')],
        'title': "Second-Order Euler's Theorem on Inverse Tangent"},
    {   'concept': 'Radial symmetry simplifies 3D PDEs (such as heat and wave equations) into ordinary differential '
                   'equations in r.',
        'difficulty': 'Exam-Level',
        'final_answer': "∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z² = f''(r) + (2/r) f'(r) (Hence proved)",
        'formula': "∇²u = u_xx + u_yy + u_zz = f''(r) + (2/r) f'(r).",
        'formula_expl': 'r_x = x/r, r_xx = (r² - x²)/r³.',
        'given': 'u = f(r), r² = x² + y² + z².',
        'meaning_en': 'Compute the 3D Laplacian ∇²u of a radially symmetric function u = f(r) in Cartesian '
                      'coordinates.',
        'mistakes': [   ('Treating r as constant.', 'r depends on x, y, z through r² = x² + y² + z².'),
                        ('Algebra error in (3/r) - (1/r).', '3/r - 1/r = 2/r.')],
        'num': 18,
        'practice_q': 'Find f(r) such that ∇²f(r) = 0 (harmonic function in 3D).',
        'presentation': [   'Show ∂r/∂x = x/r clearly.',
                            'Show quotient rule for ∂²u/∂x² in full detail.',
                            'Combine cyclic terms using symmetry.'],
        'question': "If u = f(r) where r² = x² + y² + z², prove that ∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z² = f''(r) + (2/r) "
                    "f'(r).",
        'steps': [   (   'Step 1: Compute partial derivatives of r',
                         '2r (∂r/∂x) = 2x  ⇒  ∂r/∂x = x/r.<br>Similarly, ∂r/∂y = y/r and ∂r/∂z = z/r.',
                         'Execute step 1: compute partial derivatives of r to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Compute first derivative ∂u/∂x',
                         "∂u/∂x = f'(r) · (∂r/∂x) = f'(r) · (x/r) = (x/r) f'(r).",
                         'Execute step 2: compute first derivative ∂u/∂x to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Compute second derivative ∂²u/∂x² using quotient/product rule',
                         "∂²u/∂x² = ∂/∂x [(x/r) f'(r)] = (1/r) f'(r) + x · ∂/∂x [f'(r)/r]<br>= (1/r) f'(r) + x [ r "
                         "f''(r)(x/r) - f'(r)(x/r) ] / r²<br>= (1/r) f'(r) + (x²/r²) f''(r) - (x²/r³) f'(r).",
                         'Execute step 3: compute second derivative ∂²u/∂x² using quotient/product rule to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 4: Sum cyclically over x, y, and z',
                         "u_xx + u_yy + u_zz = [ 3/r f'(r) ] + [ (x² + y² + z²)/r² ] f''(r) - [ (x² + y² + z²)/r³ ] "
                         "f'(r).",
                         'Execute step 4: sum cyclically over x, y, and z to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 5: Substitute x² + y² + z² = r²',
                         "= (3/r) f'(r) + (r²/r²) f''(r) - (r²/r³) f'(r)<br>= (3/r) f'(r) + f''(r) - (1/r) f'(r)<br>= "
                         "f''(r) + (2/r) f'(r). Hence proved.",
                         'Execute step 5: substitute x² + y² + z² = r² to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Radial Laplace Operator: u = f(r) where r² = x² + y² + z²'},
    {   'concept': 'Can be solved either by computing partial derivatives up to order 3 at (0, 0) or by multiplying '
                   'the standard series of eˣ and log(1 + y). In exams, showing the partial derivative values '
                   'guarantees full marks.',
        'difficulty': 'Exam-Level',
        'final_answer': 'eˣ log(1 + y) = y + xy - (1/2)y² + (1/2)x²y - (1/2)xy² + (1/3)y³ + ...',
        'formula': 'f(x, y) = f(0,0) + [x fx + y fy] + (1/2!)[x² fxx + 2xy fxy + y² fyy] + (1/3!)[x³ fxxx + 3x²y fxxy '
                   '+ 3xy² fxyy + y³ fyyy] + ...',
        'formula_expl': 'All derivatives evaluated at (0, 0).',
        'given': 'f(x, y) = eˣ log(1 + y), expansion point (0, 0).',
        'meaning_en': 'Obtain the Maclaurin expansion of eˣ log(1 + y) around (0, 0) up to terms of combined degree 3.',
        'mistakes': [   ('Derivative of 1/(1+y)².', 'd[-(1+y)⁻²]/dy = +2(1+y)⁻³ = 2/(1+y)³.'),
                        ('Missing 1/3! = 1/6 on third degree terms.', 'Always divide by the corresponding factorial.')],
        'num': 19,
        'practice_q': 'Expand f(x, y) = e^y log(1 + x) up to third-degree terms.',
        'presentation': [   'List all derivatives systematically by order (1st, 2nd, 3rd).',
                            'State the multinomial coefficients 1, 3, 3, 1 for the 3rd degree bracket.',
                            'Group by degree: linear, quadratic, cubic.'],
        'question': 'Expand f(x, y) = eˣ log(1 + y) in powers of x and y up to third-degree terms.',
        'steps': [   (   'Step 1: Function and 1st derivatives at (0, 0)',
                         'f(0, 0) = e⁰ log(1) = 0.<br>fx = eˣ log(1 + y) ⇒ fx(0, 0) = 0.<br>fy = eˣ / (1 + y) ⇒ fy(0, '
                         '0) = 1.',
                         'Execute step 1: function and 1st derivatives at (0, 0) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: 2nd-order derivatives at (0, 0)',
                         'fxx = eˣ log(1 + y) ⇒ fxx(0, 0) = 0.<br>fxy = eˣ / (1 + y) ⇒ fxy(0, 0) = 1.<br>fyy = -eˣ / '
                         '(1 + y)² ⇒ fyy(0, 0) = -1.',
                         'Execute step 2: 2nd-order derivatives at (0, 0) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: 3rd-order derivatives at (0, 0)',
                         'fxxx = eˣ log(1 + y) ⇒ fxxx(0, 0) = 0.<br>fxxy = eˣ / (1 + y) ⇒ fxxy(0, 0) = 1.<br>fxyy = '
                         '-eˣ / (1 + y)² ⇒ fxyy(0, 0) = -1.<br>fyyy = 2eˣ / (1 + y)³ ⇒ fyyy(0, 0) = 2.',
                         'Execute step 3: 3rd-order derivatives at (0, 0) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Substitute into Taylor formula',
                         'Linear: y.<br>Quadratic: (1/2)[2xy(1) + y²(-1)] = xy - (1/2)y².<br>Cubic: (1/6)[3x²y(1) + '
                         '3xy²(-1) + y³(2)] = (1/2)x²y - (1/2)xy² + (1/3)y³.<br>Combine all terms:<br>f(x, y) = y + xy '
                         '- (1/2)y² + (1/2)x²y - (1/2)xy² + (1/3)y³ + ...',
                         'Substitute the evaluated derivative values into the multivariable Taylor/Maclaurin series '
                         'formula and group terms by degree.')],
        'title': 'Taylor Series of Two Variables up to 3rd Degree: eˣ log(1 + y)'},
    {   'concept': 'Optimization of two independent variables by eliminating the third variable using the constraint '
                   'equation.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Dimensions: Length x = 4 ft, Breadth y = 4 ft, Height z = 2 ft (Minimum Surface Area = 48 sq. '
                        'ft)',
        'formula': 'Constraint: V = xyz = 32  ⇒  z = 32/(xy).<br>Surface area: S(x, y) = xy + 2xz + 2yz = xy + 64/y + '
                   '64/x.',
        'formula_expl': 'xy is the base; 2xz and 2yz are the four open sides.',
        'given': 'Volume V = xyz = 32; Open top surface area S = xy + 2yz + 2xz.',
        'meaning_en': 'Minimize the surface area S = xy + 2yz + 2xz subject to the volume constraint V = xyz = 32.',
        'mistakes': [   (   'Including 2xy for closed box.',
                            'The box is OPEN AT THE TOP, so only one base xy is included!'),
                        ('Forgetting to calculate the 3rd dimension z.', 'Always calculate z = 32/(xy).')],
        'num': 20,
        'practice_q': 'Find dimensions of an open rectangular box of volume 108 cubic cm requiring least material.',
        'presentation': [   'State constraint and surface area formulas clearly.',
                            'Eliminate z and write S(x, y).',
                            'Verify D > 0 and r > 0 to prove it is a minimum.',
                            'State all 3 dimensions with units.'],
        'question': 'A rectangular box open at the top is to have a volume of 32 cubic feet. Find the dimensions of '
                    'the box requiring the least material for its construction.',
        'steps': [   (   'Step 1: Express S as a function of x and y',
                         'z = 32 / (xy).<br>S(x, y) = xy + 2x(32/xy) + 2y(32/xy) = xy + 64/y + 64/x.',
                         'Execute step 1: express s as a function of x and y to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Find stationary points: Sx = 0 and Sy = 0',
                         'Sx = y - 64/x² = 0  ⇒  y = 64/x².<br>Sy = x - 64/y² = 0  ⇒  x = 64/y².<br>Substitute y into '
                         'x equation:<br>x = 64 / (64/x²)² = 64 · (x⁴ / 4096) = x⁴ / 64<br>x⁴ - 64x = 0  ⇒  x(x³ - 64) '
                         '= 0.<br>Since x > 0 (dimension of box): x³ = 64  ⇒  x = 4.<br>Then y = 64 / 4² = 64 / 16 = '
                         '4.',
                         'Set the first partial derivatives fx = 0 and fy = 0 to solve for all stationary (critical) '
                         'points.'),
                     (   'Step 3: Second derivative test at (4, 4)',
                         'r = Sxx = 128/x³  ⇒  r(4, 4) = 128/64 = 2.<br>s = Sxy = 1.<br>t = Syy = 128/y³  ⇒  t(4, 4) = '
                         '128/64 = 2.<br>D = rt - s² = (2)(2) - 1² = 4 - 1 = 3 > 0 and r = 2 > 0.<br>Thus, S has a '
                         'LOCAL MINIMUM at (4, 4).',
                         'Execute step 3: second derivative test at (4, 4) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Find height z and minimum surface area',
                         'z = 32 / (xy) = 32 / (4 · 4) = 32 / 16 = 2 feet.<br>S_min = (4)(4) + 64/4 + 64/4 = 16 + 16 + '
                         '16 = 48 sq. ft.',
                         'Execute step 4: find height z and minimum surface area to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Global / Constrained Maxima and Minima: Dimensions of Open Rectangular Box'},
    {   'concept': 'Classic VTU exam problem related to maximum area of a triangle. Uses trigonometric identities cos '
                   'A - cos B = -2 sin[(A+B)/2] sin[(A-B)/2].',
        'difficulty': 'Exam-Level',
        'final_answer': 'Local Maximum at (π/3, π/3) with Maximum Value f_max = (3√3)/2',
        'formula': 'fx = cos x + cos(x + y) = 0,  fy = cos y + cos(x + y) = 0.',
        'formula_expl': 'Subtracting gives cos x - cos y = 0 ⇒ x = y in (0, π).',
        'given': 'f(x, y) = sin x + sin y + sin(x + y), 0 < x, y < π.',
        'meaning_en': 'Find the critical points of the trigonometric function f(x, y) in the first quadrant and '
                      'determine where it attains its maximum value.',
        'mistakes': [   (   'Concluding Minimum because of negative signs in r.',
                            'r < 0 means concave downwards, which is a MAXIMUM!'),
                        (   'Value of sin(2π/3) written as -√3/2.',
                            '2π/3 is in Quadrant II where sine is POSITIVE: sin(2π/3) = +√3/2.')],
        'num': 21,
        'practice_q': 'Find the maximum value of f(x, y) = cos x + cos y + cos(x + y) for 0 < x, y < π/2.',
        'presentation': [   'Show cos x = cos y gives x = y.',
                            'Show cos 2x = -cos x = cos(π - x) gives x = π/3.',
                            'State D = 9/4 > 0 and r < 0 implies Maximum.'],
        'question': 'Find the maximum and minimum values of f(x, y) = sin x + sin y + sin(x + y) in the range 0 < x, y '
                    '< π.',
        'steps': [   (   'Step 1: Set first derivatives to zero',
                         'fx = cos x + cos(x + y) = 0  --- (1)<br>fy = cos y + cos(x + y) = 0  --- (2).',
                         'Set the first partial derivatives fx = 0 and fy = 0 to solve for all stationary (critical) '
                         'points.'),
                     (   'Step 2: Solve the system of trigonometric equations',
                         'Subtracting (2) from (1):<br>cos x - cos y = 0  ⇒  cos x = cos y.<br>Since 0 < x, y < π, '
                         'this implies x = y.<br>Substitute x = y into (1):<br>cos x + cos(2x) = 0  ⇒  cos 2x = -cos x '
                         '= cos(π - x).<br>2x = π - x  ⇒  3x = π  ⇒  x = π/3.<br>Since x = y, y = π/3.<br>Critical '
                         'point: (π/3, π/3).',
                         'Execute step 2: solve the system of trigonometric equations to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Compute second derivatives at (π/3, π/3)',
                         'r = fxx = -sin x - sin(x + y) ⇒ r(π/3, π/3) = -sin(π/3) - sin(2π/3) = -√3/2 - √3/2 = '
                         '-√3.<br>s = fxy = -sin(x + y) ⇒ s(π/3, π/3) = -sin(2π/3) = -√3/2.<br>t = fyy = -sin y - '
                         'sin(x + y) ⇒ t(π/3, π/3) = -√3.',
                         'Execute step 3: compute second derivatives at (π/3, π/3) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Evaluate D = rt - s²',
                         'D = (-√3)(-√3) - (-√3/2)² = 3 - 3/4 = 9/4 > 0.<br>Since D > 0 and r = -√3 < 0, f has a LOCAL '
                         'MAXIMUM at (π/3, π/3).',
                         'Evaluate the Hessian discriminant D = rt - s²; D > 0 and r > 0 indicates a local minimum, '
                         'while D > 0 and r < 0 indicates a local maximum.'),
                     (   'Step 5: Compute Maximum Value',
                         'f_max = sin(π/3) + sin(π/3) + sin(2π/3) = √3/2 + √3/2 + √3/2 = (3√3)/2.',
                         'Execute step 5: compute maximum value to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Stationary Points and Nature: f(x, y) = sin x + sin y + sin(x + y)'},
    {   'concept': 'For a system of implicit equations F₁(u,v,w,x,y,z) = 0, F₂ = 0, F₃ = 0: ∂u/∂x = - [∂(F₁, F₂, '
                   'F₃)/∂(x, v, w)] / [∂(F₁, F₂, F₃)/∂(u, v, w)].',
        'difficulty': 'Exam-Level',
        'final_answer': '∂u/∂x = - [ 1 - 9v²w² + 2x(3v² + 3w² - 2) ] / [ 27u²v²w² - 3(u² + v² + w²) + 2 ]',
        'formula': '∂u/∂x = - J(x, v, w) / J(u, v, w).',
        'formula_expl': 'Denominator is the Jacobian with respect to dependent variables; numerator replaces u by x.',
        'given': 'F₁ = u³ + v + w - x - y² - z² = 0, F₂ = u + v³ + w - x² - y - z² = 0, F₃ = u + v + w³ - x² - y² - z '
                 '= 0.',
        'meaning_en': 'Use the Jacobian formula for implicit functions to find the partial derivative ∂u/∂x when u, v, '
                      'w are implicitly defined functions of x, y, z.',
        'mistakes': [   (   'Forgetting the leading negative sign in implicit derivative formula.',
                            'dy/dx = - Fx / Fy always has a minus sign!'),
                        ('Replacing the wrong column.', "To find ∂u/∂x, replace the 'u' column with 'x' derivatives.")],
        'num': 22,
        'practice_q': 'If u + v + w = x + y + z, u² + v² + w² = x² + y² + z², u³ + v³ + w³ = x³ + y³ + z³, find ∂u/∂x.',
        'presentation': [   'State the implicit Jacobian ratio formula with minus sign.',
                            'Evaluate both 3×3 determinants separately.',
                            'Substitute into final quotient.'],
        'question': 'If u³ + v + w = x + y² + z², u + v³ + w = x² + y + z², u + v + w³ = x² + y² + z, find ∂u/∂x.',
        'steps': [   (   'Step 1: Compute Denominator Jacobian J(u, v, w)',
                         'J(u, v, w) = | 3u²  1    1   |<br>              | 1    3v²  1   |<br>              | 1    '
                         '1    3w² |.<br>Row operations R₂ → R₂ - R₁, R₃ → R₃ - R₁:<br>J(u, v, w) = | 3u²     1        '
                         '1      |<br>              | 1-3u²   3v²-1    0      |<br>              | 1-3u²   0        '
                         '3w²-1  |.<br>Evaluating this gives: 27u²v²w² - 3(u² + v² + w²) + 2.',
                         'Execute step 1: compute denominator jacobian j(u, v, w) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Compute Numerator Jacobian J(x, v, w)',
                         'J(x, v, w) = | ∂F₁/∂x  ∂F₁/∂v  ∂F₁/∂w | = | -1   1    1   |<br>              | ∂F₂/∂x  '
                         '∂F₂/∂v  ∂F₂/∂w |   | -2x  3v²  1   |<br>              | ∂F₃/∂x  ∂F₃/∂v  ∂F₃/∂w |   | -2x  '
                         '1    3w² |.',
                         'Execute step 2: compute numerator jacobian j(x, v, w) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Evaluate Numerator Determinant',
                         'Expanding along column 1:<br>= -1 [ 9v²w² - 1 ] - (-2x) [ 3w² - 1 ] + (-2x) [ 1 - 3v² ]<br>= '
                         '1 - 9v²w² + 2x(3w² - 1 - 1 + 3v²)<br>= 1 - 9v²w² + 2x[3(v² + w²) - 2].',
                         'Execute step 3: evaluate numerator determinant to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Combine using implicit differentiation formula',
                         '∂u/∂x = - [J(x, v, w)] / [J(u, v, w)].',
                         'Execute step 4: combine using implicit differentiation formula to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Jacobian of Implicit Functions'},
    {   'concept': 'Lagrange function: L(x, y, z, λ) = f + λg. At extrema, ∇f = -λ ∇g, meaning the gradient of the '
                   'objective function is parallel to the normal vector of the constraint surface.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Closest point is (1, 2, 2); Minimum Distance = 3 units',
        'formula': 'L = (x² + y² + z²) + λ(x + 2y + 2z - 9). Conditions: Lx = 0, Ly = 0, Lz = 0, Lλ = 0.',
        'formula_expl': 'Minimizing x² + y² + z² is mathematically equivalent to minimizing the square root distance, '
                        'but avoids radical algebra.',
        'given': 'Objective: f = x² + y² + z²; Constraint: x + 2y + 2z = 9.',
        'meaning_en': 'Minimize the square of distance f(x, y, z) = x² + y² + z² subject to the plane constraint g(x, '
                      'y, z) = x + 2y + 2z - 9 = 0.',
        'mistakes': [   (   'Using d = √(x²+y²+z²) as objective function.',
                            'Differentiating square roots is messy. Always minimize f = x² + y² + z² instead!'),
                        ('Arithmetic error in -λ/2 - 4λ.', '-λ/2 - 8λ/2 = -9λ/2.')],
        'num': 23,
        'practice_q': 'Find the shortest distance from the origin to the surface xyz = 8 using Lagrange multipliers.',
        'presentation': [   'State objective function f = x² + y² + z².',
                            'Form Lagrange function L = f + λg.',
                            'Solve for λ and then (x, y, z).',
                            'State distance d = √9 = 3.'],
        'question': "Find the shortest distance from the origin to the plane x + 2y + 2z = 9 using Lagrange's method "
                    'of undetermined multipliers.',
        'steps': [   (   'Step 1: Set up Lagrange equations',
                         'Lx = 2x + λ = 0  ⇒  x = -λ/2.<br>Ly = 2y + 2λ = 0  ⇒  y = -λ.<br>Lz = 2z + 2λ = 0  ⇒  z = '
                         '-λ.',
                         'Set up the auxiliary Lagrange function L = f + λg and set all first partial derivatives to '
                         'zero.'),
                     (   'Step 2: Substitute x, y, z into the constraint equation',
                         'x + 2y + 2z = 9<br>(-λ/2) + 2(-λ) + 2(-λ) = 9<br>-λ/2 - 4λ = 9  ⇒  -9λ/2 = 9  ⇒  λ = -2.',
                         'Execute step 2: substitute x, y, z into the constraint equation to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Determine the closest point coordinates',
                         'x = -(-2)/2 = 1.<br>y = -(-2) = 2.<br>z = -(-2) = 2.<br>The closest point on the plane is '
                         '(1, 2, 2).',
                         'Execute step 3: determine the closest point coordinates to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Compute the minimum distance',
                         'd = √(x² + y² + z²) = √(1² + 2² + 2²) = √(1 + 4 + 4) = √9 = 3 units.',
                         'Execute step 4: compute the minimum distance to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': "Lagrange's Method of Multipliers: Minimum Distance to a Plane"},
    {   'concept': "Fundamental partial differential equation of vibrations and wave propagation (d'Alembert's "
                   'solution of wave equation).',
        'difficulty': 'Exam-Level',
        'final_answer': '∂²u/∂t² = c² (∂²u/∂x²) (Hence proved)',
        'formula': 'Let v = x - ct, w = x + ct. Then ∂/∂t = -c(d/dv) + c(d/dw) and ∂/∂x = d/dv + d/dw.',
        'formula_expl': 'c is the wave propagation velocity.',
        'given': 'u = f(v) + g(w), where v = x - ct, w = x + ct.',
        'meaning_en': 'Show that any combination of forward and backward travelling waves u = f(x - ct) + g(x + ct) '
                      'satisfies the one-dimensional classical wave equation.',
        'mistakes': [   ('Missing the minus sign on (-c)(-c).', 'Careful with double negative: -c · (-c) = +c².'),
                        ("Omitting the prime notation f'(v).", "Remember to use chain rule: df/dt = f'(v) · dv/dt.")],
        'num': 24,
        'practice_q': 'If u = f(x + iy) + g(x - iy), prove that ∂²u/∂x² + ∂²u/∂y² = 0 (Laplace equation).',
        'presentation': [   'Define intermediate variables v = x - ct, w = x + ct.',
                            'Show ∂v/∂t = -c and ∂w/∂t = +c explicitly.',
                            'Equate LHS and RHS to complete proof.'],
        'question': 'If u = f(x - ct) + g(x + ct), prove that ∂²u/∂t² = c² (∂²u/∂x²).',
        'steps': [   (   'Step 1: Compute first partial derivatives with respect to x',
                         "∂u/∂x = f'(v) · (∂v/∂x) + g'(w) · (∂w/∂x) = f'(v)(1) + g'(w)(1) = f'(v) + g'(w).",
                         'Execute step 1: compute first partial derivatives with respect to x to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 2: Compute second partial derivative with respect to x',
                         "∂²u/∂x² = ∂/∂x [f'(v) + g'(w)] = f''(v)(1) + g''(w)(1) = f''(v) + g''(w).",
                         'Execute step 2: compute second partial derivative with respect to x to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 3: Compute first partial derivative with respect to t',
                         "∂u/∂t = f'(v) · (∂v/∂t) + g'(w) · (∂w/∂t) = f'(v)(-c) + g'(w)(c) = -c f'(v) + c g'(w).",
                         'Execute step 3: compute first partial derivative with respect to t to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 4: Compute second partial derivative with respect to t',
                         "∂²u/∂t² = ∂/∂t [-c f'(v) + c g'(w)]<br>= -c f''(v)(-c) + c g''(w)(c)<br>= c² f''(v) + c² "
                         "g''(w) = c² [f''(v) + g''(w)].",
                         'Execute step 4: compute second partial derivative with respect to t to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 5: Substitute Step 2 into Step 4',
                         "∂²u/∂t² = c² [f''(v) + g''(w)] = c² (∂²u/∂x²). Hence proved.",
                         'Execute step 5: substitute step 2 into step 4 to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Chain Rule Derivative Transformation: Wave Equation Form'},
    {   'concept': "For three variables, Euler's Theorem states: x u_x + y u_y + z u_z = n u. For logarithmic "
                   'functions, let f(u) = e^u, then x u_x + y u_y + z u_z = n.',
        'difficulty': 'Exam-Level',
        'final_answer': 'x(∂u/∂x) + y(∂u/∂y) + z(∂u/∂z) = 3 (Hence proved)',
        'formula': 'If e^u is homogeneous of degree n, then x u_x + y u_y + z u_z = n.',
        'formula_expl': 'Since d(e^u)/dx = e^u u_x, the e^u cancels out from both sides, leaving simply n.',
        'given': 'u = log[(x⁴ + y⁴ + z⁴) / (x + y + z)].',
        'meaning_en': "Apply Euler's theorem for three independent variables to e^u, find its degree of homogeneity, "
                      'and prove the sum equals the degree 3.',
        'mistakes': [   ('Writing RHS as 3u.', 'For u = log(homogeneous), the answer is a CONSTANT n = 3, NOT 3u!'),
                        (   'Attempting direct differentiation with quotient rule on log.',
                            "Direct differentiation takes 3 pages; Euler's theorem on e^u takes 5 lines.")],
        'num': 25,
        'practice_q': 'If u = log[(x³ + y³ + z³) / (x² + y² + z²)], prove that x u_x + y u_y + z u_z = 1.',
        'presentation': [   'Write F = e^u clearly.',
                            'Show F(tx, ty, tz) = t³ F to establish degree n = 3.',
                            'Factor out e^u and divide both sides.'],
        'question': 'If u = log[(x⁴ + y⁴ + z⁴) / (x + y + z)], prove that x(∂u/∂x) + y(∂u/∂y) + z(∂u/∂z) = 3.',
        'steps': [   (   'Step 1: Eliminate logarithm by exponentiating both sides',
                         'e^u = (x⁴ + y⁴ + z⁴) / (x + y + z) = F(x, y, z).',
                         'Apply elementary row operations to introduce zeros below the pivot element and reduce the '
                         'matrix toward echelon form.'),
                     (   'Step 2: Determine degree of homogeneity of F',
                         'F(tx, ty, tz) = [(tx)⁴ + (ty)⁴ + (tz)⁴] / [tx + ty + tz]<br>= [t⁴(x⁴ + y⁴ + z⁴)] / [t(x + y '
                         '+ z)] = t⁴⁻¹ · F = t³ F.<br>Hence, F = e^u is a homogeneous function of degree n = 3 in x, '
                         'y, z.',
                         'Substitute tx and ty for x and y to factor out t^n and establish the degree of homogeneity '
                         'n.'),
                     (   "Step 3: Apply Euler's Theorem to F = e^u",
                         'x(∂F/∂x) + y(∂F/∂y) + z(∂F/∂z) = n · F = 3 e^u.',
                         'Combine the partial derivatives into the linear combination x(∂u/∂x) + y(∂u/∂y) and verify '
                         'it equals n·u.'),
                     (   'Step 4: Differentiate F = e^u with respect to x, y, z',
                         '∂F/∂x = e^u (∂u/∂x)<br>∂F/∂y = e^u (∂u/∂y)<br>∂F/∂z = e^u (∂u/∂z).',
                         'Execute step 4: differentiate f = e^u with respect to x, y, z to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: Substitute and divide by e^u',
                         'x [e^u (∂u/∂x)] + y [e^u (∂u/∂y)] + z [e^u (∂u/∂z)] = 3 e^u<br>e^u [ x(∂u/∂x) + y(∂u/∂y) + '
                         'z(∂u/∂z) ] = 3 e^u<br>x(∂u/∂x) + y(∂u/∂y) + z(∂u/∂z) = 3. Hence proved.',
                         'Compute the sum of partial derivatives of the component functions along their respective '
                         'coordinate axes.')],
        'title': "Euler's Theorem for Three Variables with Algebraic-Logarithmic Form"}]


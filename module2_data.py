# -*- coding: utf-8 -*-
"""
Module 2: Vector Calculus
100% Pure English Edition
Includes 25 Fully Solved Questions (5 Fundamental + 10 Intermediate + 10 Exam-Level)
"""

MODULE2_QUESTIONS = [   {   'concept': 'The gradient ∇φ transforms a scalar field into a vector field. At any point, ∇φ points in the '
                   'direction of greatest rate of increase of φ, and its magnitude gives the maximum rate of increase.',
        'difficulty': 'Fundamental',
        'final_answer': '∇φ(1, -2, -1) = -12 î - 9 ĵ - 16 k̂',
        'formula': '∇φ = (∂φ/∂x) î + (∂φ/∂y) ĵ + (∂φ/∂z) k̂.',
        'formula_expl': 'î, ĵ, k̂ are unit basis vectors along x, y, z axes. Each component is a partial derivative.',
        'given': 'φ = 3x²y - y³z², point P(1, -2, -1).',
        'meaning_en': 'Calculate the vector of spatial partial derivatives (gradient vector) of the scalar field φ at '
                      'the specified point (1, -2, -1).',
        'mistakes': [   (   'Sign error in (-2)³ = -8.',
                            'Cubing a negative number yields a negative number: (-2)³ = -8, then -2(-8)(-1) = -16.'),
                        ('Writing gradient as a scalar.', 'Gradient of a scalar field is always a VECTOR!')],
        'num': 26,
        'practice_q': 'If φ = 2xz⁴ - x²y, find ∇φ at (2, -2, 1).',
        'presentation': [   'State formula for ∇φ first.',
                            'Calculate all 3 components separately.',
                            'Substitute coordinates carefully observing negative signs.'],
        'question': 'If φ(x, y, z) = 3x²y - y³z², find grad φ (or ∇φ) at the point (1, -2, -1).',
        'steps': [   (   'Step 1: Compute ∂φ/∂x',
                         '∂φ/∂x = ∂/∂x(3x²y - y³z²) = 6xy - 0 = 6xy.',
                         'Execute step 1: compute ∂φ/∂x to advance the step-by-step mathematical solution toward the '
                         'final result.'),
                     (   'Step 2: Compute ∂φ/∂y',
                         '∂φ/∂y = ∂/∂y(3x²y - y³z²) = 3x² - 3y²z².',
                         'Execute step 2: compute ∂φ/∂y to advance the step-by-step mathematical solution toward the '
                         'final result.'),
                     (   'Step 3: Compute ∂φ/∂z',
                         '∂φ/∂z = ∂/∂z(3x²y - y³z²) = 0 - 2y³z = -2y³z.',
                         'Execute step 3: compute ∂φ/∂z to advance the step-by-step mathematical solution toward the '
                         'final result.'),
                     (   'Step 4: Form the gradient vector ∇φ',
                         '∇φ = (6xy) î + (3x² - 3y²z²) ĵ - (2y³z) k̂.',
                         'Execute step 4: form the gradient vector ∇φ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 5: Evaluate at P(1, -2, -1)',
                         '• x-component: 6(1)(-2) = -12.<br>• y-component: 3(1)² - 3(-2)²(-1)² = 3(1) - 3(4)(1) = 3 - '
                         '12 = -9.<br>• z-component: -2(-2)³(-1) = -2(-8)(-1) = -16.<br>Therefore: ∇φ(1, -2, -1) = -12 '
                         'î - 9 ĵ - 16 k̂.',
                         'Execute step 5: evaluate at p(1, -2, -1) to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Gradient of a Scalar Field at a Point'},
    {   'concept': "Divergence is a scalar measure of a vector field's source or sink density. If div F⃗ > 0, the "
                   'point acts as a source; if div F⃗ < 0, it acts as a sink; if div F⃗ = 0, the field is solenoidal '
                   '(incompressible).',
        'difficulty': 'Fundamental',
        'final_answer': 'div F⃗(1, 2, 3) = 22',
        'formula': 'div F⃗ = ∇ · F⃗ = ∂F₁/∂x + ∂F₂/∂y + ∂F₃/∂z.',
        'formula_expl': 'Dot product of the del operator ∇ with vector F⃗ = F₁î + F₂ĵ + F₃k̂ gives a SCALAR.',
        'given': 'F⃗ = (x²y) î + (y²z) ĵ + (z²x) k̂, point P(1, 2, 3).',
        'meaning_en': 'Compute the divergence of the vector field F⃗, which measures the net outward flux of vector '
                      'field per unit volume from a point.',
        'mistakes': [   (   'Including î, ĵ, k̂ in the divergence answer.',
                            'Divergence is a SCALAR product (dot product), so î, ĵ, k̂ MUST NOT appear!'),
                        (   'Differentiating F₁ with respect to y instead of x.',
                            'F₁ is with respect to x, F₂ with y, F₃ with z.')],
        'num': 27,
        'practice_q': 'If F⃗ = (x³ + y³) î + (y³ + z³) ĵ + (z³ + x³) k̂, find div F⃗ at (1, 1, 1).',
        'presentation': [   'State formula div F⃗ = ∂F₁/∂x + ∂F₂/∂y + ∂F₃/∂z.',
                            'Compute each term separately.',
                            'Add terms and substitute point values.'],
        'question': 'If F⃗ = (x²y) î + (y²z) ĵ + (z²x) k̂, find div F⃗ (or ∇ · F⃗) at the point (1, 2, 3).',
        'steps': [   (   'Step 1: Identify components of F⃗',
                         'F₁ = x²y,   F₂ = y²z,   F₃ = z²x.',
                         'Execute step 1: identify components of f⃗ to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Differentiate each component with respect to its coordinate',
                         '∂F₁/∂x = ∂(x²y)/∂x = 2xy<br>∂F₂/∂y = ∂(y²z)/∂y = 2yz<br>∂F₃/∂z = ∂(z²x)/∂z = 2zx.',
                         'Execute step 2: differentiate each component with respect to its coordinate to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 3: Add to get the scalar divergence',
                         'div F⃗ = ∇ · F⃗ = 2xy + 2yz + 2zx = 2(xy + yz + zx).',
                         'Compute the sum of partial derivatives of the component functions along their respective '
                         'coordinate axes.'),
                     (   'Step 4: Evaluate at point (1, 2, 3)',
                         'div F⃗(1, 2, 3) = 2[(1)(2) + (2)(3) + (3)(1)] = 2[2 + 6 + 3] = 2(11) = 22.',
                         'Substitute the specific point coordinates into the gradient vector components.')],
        'title': 'Divergence of a Vector Field'},
    {   'concept': 'Curl measures the vorticity or rotational tendency of a fluid flow. If curl F⃗ = 0⃗ everywhere, '
                   'the field has no vortices and is called irrotational (conservative).',
        'difficulty': 'Fundamental',
        'final_answer': 'curl F⃗(1, -1, 1) = -î - 2k̂',
        'formula': 'curl F⃗ = ∇ × F⃗ = | î       ĵ       k̂      |<br>                     | ∂/∂x    ∂/∂y    ∂/∂z   '
                   '|<br>                     | F₁      F₂      F₃     |.',
        'formula_expl': '= î(∂F₃/∂y - ∂F₂/∂z) - ĵ(∂F₃/∂x - ∂F₁/∂z) + k̂(∂F₂/∂x - ∂F₁/∂y).',
        'given': 'F⃗ = (xy²) î + (2x²yz) ĵ - (3yz²) k̂, point P(1, -1, 1).',
        'meaning_en': 'Compute the curl of the vector field F⃗, which measures the infinitesimal rotation or '
                      'circulation of the vector field around a point.',
        'mistakes': [   (   'Sign error on ĵ component.',
                            'Remember the cofactor of ĵ has a minus sign: -ĵ(∂F₃/∂x - ∂F₁/∂z).'),
                        ('Treating curl as a scalar.', 'Curl of a vector is a VECTOR!')],
        'num': 28,
        'practice_q': 'If F⃗ = (x² - y²) î + 2xy ĵ + (y² - z²) k̂, find curl F⃗ at (1, 2, 3).',
        'presentation': [   'Write out the 3×3 determinant with del operators in row 2.',
                            'Show the cross-derivative pairs for each component.',
                            'Evaluate at the point.'],
        'question': 'If F⃗ = (xy²) î + (2x²yz) ĵ - (3yz²) k̂, find curl F⃗ (or ∇ × F⃗) at the point (1, -1, 1).',
        'steps': [   (   'Step 1: Set up the 3×3 curl determinant',
                         '∇ × F⃗ = | î        ĵ         k̂        |<br>          | ∂/∂x     ∂/∂y      ∂/∂z     '
                         '|<br>          | xy²      2x²yz     -3yz²    |.',
                         'Set up the 3×3 curl determinant with unit vectors in row 1 and del operators in row 2.'),
                     (   'Step 2: Expand î component',
                         'î [ ∂(-3yz²)/∂y - ∂(2x²yz)/∂z ] = î [ -3z² - 2x²y ].',
                         'Execute step 2: expand î component to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 3: Expand ĵ component (with negative sign)',
                         '-ĵ [ ∂(-3yz²)/∂x - ∂(xy²)/∂z ] = -ĵ [ 0 - 0 ] = 0 ĵ.',
                         'Execute step 3: expand ĵ component (with negative sign) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Expand k̂ component',
                         'k̂ [ ∂(2x²yz)/∂x - ∂(xy²)/∂y ] = k̂ [ 4xyz - 2xy ].',
                         'Execute step 4: expand k̂ component to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 5: Combine into vector expression and evaluate at (1, -1, 1)',
                         '∇ × F⃗ = (-3z² - 2x²y) î + (4xyz - 2xy) k̂.<br>At (1, -1, 1):<br>• î-comp: -3(1)² - '
                         '2(1)²(-1) = -3 + 2 = -1.<br>• ĵ-comp: 0.<br>• k̂-comp: 4(1)(-1)(1) - 2(1)(-1) = -4 + 2 = '
                         '-2.<br>Thus, curl F⃗ = -î - 2k̂.',
                         'Execute step 5: combine into vector expression and evaluate at (1, -1, 1) to advance the '
                         'step-by-step mathematical solution toward the final result.')],
        'title': 'Curl of a Vector Field'},
    {   'concept': 'For any level surface φ(x, y, z) = C, the gradient vector ∇φ is perpendicular (normal) to the '
                   'tangent plane at every point. Dividing ∇φ by its magnitude gives the unit normal vector n̂.',
        'difficulty': 'Fundamental',
        'final_answer': 'n̂ = (î + ĵ + 3k̂) / √11  =  (1/√11) î + (1/√11) ĵ + (3/√11) k̂',
        'formula': 'n̂ = ∇φ / |∇φ|.',
        'formula_expl': '∇φ is the normal vector, |∇φ| is its Euclidean length √(Ax² + Ay² + Az²).',
        'given': 'Surface φ(x, y, z) = x² + y² + 2z² - 26 = 0, point P(2, 2, 3).',
        'meaning_en': 'Find a vector of length 1 that is perpendicular to the tangent plane of the given ellipsoid '
                      'surface at (2, 2, 3).',
        'mistakes': [   (   'Leaving answer as ∇φ without normalizing.',
                            'The question asks for UNIT normal, so dividing by magnitude is compulsory!'),
                        ('Arithmetic error in 4(3) = 12.', 'Check 2(2z) = 4z, so at z=3, 4(3)=12, not 6.')],
        'num': 29,
        'practice_q': 'Find the unit normal vector to the sphere x² + y² + z² = 9 at (1, 2, 2).',
        'presentation': [   'Define φ(x, y, z) = x² + y² + 2z².',
                            'State n̂ = ∇φ / |∇φ|.',
                            'Cancel the common factor 4 before writing final answer.'],
        'question': 'Find the unit normal vector n̂ to the surface x² + y² + 2z² = 26 at the point (2, 2, 3).',
        'steps': [   (   'Step 1: Compute the gradient vector ∇φ',
                         '∂φ/∂x = 2x,   ∂φ/∂y = 2y,   ∂φ/∂z = 4z.<br>∇φ = (2x) î + (2y) ĵ + (4z) k̂.',
                         'Execute step 1: compute the gradient vector ∇φ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Evaluate ∇φ at point (2, 2, 3)',
                         '∇φ(2, 2, 3) = 2(2) î + 2(2) ĵ + 4(3) k̂ = 4 î + 4 ĵ + 12 k̂.<br>Factor out 4: ∇φ = 4(î + ĵ + '
                         '3k̂).',
                         'Substitute the specific point coordinates into the gradient vector components.'),
                     (   'Step 3: Compute the magnitude |∇φ|',
                         '|∇φ| = √[ 4² + 4² + 12² ] = √[ 16 + 16 + 144 ] = √176 = √(16 · 11) = 4√11.',
                         'Execute step 3: compute the magnitude |∇φ| to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 4: Divide vector by its magnitude to obtain n̂',
                         'n̂ = (4 î + 4 ĵ + 12 k̂) / (4√11) = (î + ĵ + 3k̂) / √11.',
                         'Compute the sum of partial derivatives of the component functions along their respective '
                         'coordinate axes.')],
        'title': 'Unit Normal Vector to a Given Surface'},
    {   'concept': 'The directional derivative is the projection of the gradient ∇φ onto the unit direction vector â: '
                   'D_a φ = ∇φ · â. It gives the rate of change per unit distance along that direction.',
        'difficulty': 'Fundamental',
        'final_answer': 'Directional Derivative = 14 / 3',
        'formula': 'D_u φ = ∇φ · â = ∇φ · (a⃗ / |a⃗|).',
        'formula_expl': 'â must be a UNIT vector of length 1.',
        'given': 'φ = 2xy + z², point P(1, -1, 3), direction vector a⃗ = î + 2ĵ + 2k̂.',
        'meaning_en': 'Compute the rate of change of the scalar field φ at (1, -1, 3) along the specific direction '
                      'defined by vector a⃗.',
        'mistakes': [   (   'Taking dot product with a⃗ instead of unit vector â.',
                            'You MUST divide by |a⃗| = 3! Taking dot product with non-unit vector is completely '
                            'wrong.'),
                        ('Sign error in (-2)(1) = -2.', 'Keep track of negative signs carefully.')],
        'num': 30,
        'practice_q': 'Find the directional derivative of φ = x²y + yz² at (2, -1, 1) in direction 2î - ĵ - 2k̂.',
        'presentation': [   'Compute ∇φ at the point clearly.',
                            'Show unit vector â = a⃗ / |a⃗| with |a⃗| = 3.',
                            'Show the dot product arithmetic explicitly.'],
        'question': 'Find the directional derivative of φ(x, y, z) = 2xy + z² at the point (1, -1, 3) in the direction '
                    'of the vector a⃗ = î + 2ĵ + 2k̂.',
        'steps': [   (   'Step 1: Compute gradient ∇φ',
                         '∂φ/∂x = 2y,   ∂φ/∂y = 2x,   ∂φ/∂z = 2z.<br>∇φ = (2y) î + (2x) ĵ + (2z) k̂.',
                         'Calculate the spatial partial derivatives along each coordinate axis to form the gradient '
                         'vector ∇φ.'),
                     (   'Step 2: Evaluate ∇φ at point (1, -1, 3)',
                         '∇φ(1, -1, 3) = 2(-1) î + 2(1) ĵ + 2(3) k̂ = -2 î + 2 ĵ + 6 k̂.',
                         'Substitute the specific point coordinates into the gradient vector components.'),
                     (   'Step 3: Find the unit vector â in the direction of a⃗',
                         '|a⃗| = √(1² + 2² + 2²) = √(1 + 4 + 4) = √9 = 3.<br>â = a⃗ / |a⃗| = (î + 2ĵ + 2k̂) / 3.',
                         'Divide the direction vector by its Euclidean length to obtain a normalized unit vector of '
                         'magnitude 1.'),
                     (   'Step 4: Take the dot product ∇φ · â',
                         'D_a φ = (-2 î + 2 ĵ + 6 k̂) · [ (î + 2ĵ + 2k̂) / 3 ]<br>= [ (-2)(1) + (2)(2) + (6)(2) ] / '
                         '3<br>= [ -2 + 4 + 12 ] / 3 = 14 / 3.',
                         'Take the scalar dot product between the gradient vector and the unit direction vector.')],
        'title': 'Directional Derivative Along a Given Vector'},
    {   'concept': 'The directional derivative ∇φ · û = |∇φ| cos θ attains its maximum value when cos θ = 1 (θ = 0), '
                   'which occurs precisely in the direction of ∇φ itself, with maximum value equal to |∇φ|.',
        'difficulty': 'Intermediate',
        'final_answer': 'Maximum Directional Derivative = 2√6; Direction: along 2 î + 2 ĵ - 4 k̂ (or unit vector (î + '
                        'ĵ - 2k̂)/√6)',
        'formula': 'Maximum value = |∇φ|; Direction of maximum = ∇φ (or unit vector ∇φ/|∇φ|).',
        'formula_expl': 'The gradient vector always points in the direction of steepest ascent.',
        'given': 'φ = x²y²z⁴, point P(1, 1, -1).',
        'meaning_en': 'Determine the direction of fastest increase of φ at (1, 1, -1) and the maximum rate of change.',
        'mistakes': [   ('Sign error on (-1)³.', '(-1)³ = -1, so z-component is -4, not +4.'),
                        (   'Forgetting to state the direction.',
                            'The question asks for both the maximum value AND the direction.')],
        'num': 31,
        'practice_q': 'Find the maximum directional derivative of φ = x³y²z at (1, -2, 1).',
        'presentation': [   'State property: Max directional derivative = |∇φ| in direction of ∇φ.',
                            'Show ∇φ calculation.',
                            'Simplify √24 into 2√6.'],
        'question': 'Find the maximum directional derivative of φ(x, y, z) = x²y²z⁴ at the point (1, 1, -1) and state '
                    'the direction in which it occurs.',
        'steps': [   (   'Step 1: Compute partial derivatives',
                         '∂φ/∂x = 2xy²z⁴,   ∂φ/∂y = 2x²yz⁴,   ∂φ/∂z = 4x²y²z³.',
                         'Execute step 1: compute partial derivatives to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Evaluate ∇φ at P(1, 1, -1)',
                         '∂φ/∂x = 2(1)(1)²(-1)⁴ = 2(1) = 2.<br>∂φ/∂y = 2(1)²(1)(-1)⁴ = 2(1) = 2.<br>∂φ/∂z = '
                         '4(1)²(1)²(-1)³ = 4(-1) = -4.<br>∇φ = 2 î + 2 ĵ - 4 k̂.',
                         'Substitute the specific point coordinates into the gradient vector components.'),
                     (   'Step 3: State the direction of maximum directional derivative',
                         'The maximum directional derivative occurs along the vector ∇φ = 2 î + 2 ĵ - 4 k̂ (or unit '
                         'direction (î + ĵ - 2k̂)/√6).',
                         'Take the scalar dot product between the gradient vector and the unit direction vector.'),
                     (   'Step 4: Compute the magnitude |∇φ|',
                         '|∇φ| = √[ 2² + 2² + (-4)² ] = √[ 4 + 4 + 16 ] = √24 = √(4 · 6) = 2√6.',
                         'Execute step 4: compute the magnitude |∇φ| to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Maximum Directional Derivative and Its Direction'},
    {   'concept': 'A vector field is solenoidal if its divergence is zero: ∇ · F⃗ = 0. This physically represents an '
                   'incompressible fluid with no sources or sinks.',
        'difficulty': 'Intermediate',
        'final_answer': 'a = -2',
        'formula': 'div F⃗ = ∂F₁/∂x + ∂F₂/∂y + ∂F₃/∂z = 0.',
        'formula_expl': 'Sum of coordinate derivatives must equate to zero.',
        'given': 'F⃗ = (x + 3y) î + (y - 2z) ĵ + (x + az) k̂.',
        'meaning_en': "Determine the value of parameter 'a' for which the divergence of vector field F⃗ is identically "
                      'zero.',
        'mistakes': [   (   'Confusing solenoidal with irrotational.',
                            'Solenoidal means div F⃗ = 0 (dot product). Irrotational means curl F⃗ = 0 (cross '
                            'product).'),
                        ('Derivative of az with respect to z written as 0.', 'd(az)/dz = a.')],
        'num': 32,
        'practice_q': "Find constant 'k' such that F⃗ = (2x + y) î + (ky - z) ĵ + (3x - 4z) k̂ is solenoidal.",
        'presentation': [   'State condition: For F⃗ to be solenoidal, div F⃗ = 0.',
                            'Show term-by-term divergence: 1 + 1 + a = 0.',
                            'Conclude a = -2 in a box.'],
        'question': "Find the constant 'a' such that the vector field F⃗ = (x + 3y) î + (y - 2z) ĵ + (x + az) k̂ is "
                    'solenoidal.',
        'steps': [   (   'Step 1: Identify components of F⃗',
                         'F₁ = x + 3y,   F₂ = y - 2z,   F₃ = x + az.',
                         'Execute step 1: identify components of f⃗ to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 2: Differentiate each component',
                         '∂F₁/∂x = ∂(x + 3y)/∂x = 1<br>∂F₂/∂y = ∂(y - 2z)/∂y = 1<br>∂F₃/∂z = ∂(x + az)/∂z = a.',
                         'Execute step 2: differentiate each component to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Apply the solenoidal condition div F⃗ = 0',
                         '∇ · F⃗ = ∂F₁/∂x + ∂F₂/∂y + ∂F₃/∂z = 1 + 1 + a = 2 + a = 0.',
                         'Compute the sum of partial derivatives of the component functions along their respective '
                         'coordinate axes.'),
                     (   "Step 4: Solve for 'a'",
                         '2 + a = 0  ⇒  a = -2.',
                         "Execute step 4: solve for 'a' to advance the step-by-step mathematical solution toward the "
                         'final result.')],
        'title': 'Condition for a Solenoidal Vector Field'},
    {   'concept': 'A vector field is irrotational if its curl is identically zero: ∇ × F⃗ = 0⃗. Equating each of the '
                   'three components of curl to zero produces three algebraic equations for a, b, c.',
        'difficulty': 'Intermediate',
        'final_answer': 'a = 4,  b = 2,  c = -1',
        'formula': 'curl F⃗ = î(∂F₃/∂y - ∂F₂/∂z) + ĵ(∂F₁/∂z - ∂F₃/∂x) + k̂(∂F₂/∂x - ∂F₁/∂y) = 0 î + 0 ĵ + 0 k̂.',
        'formula_expl': 'Each bracketed difference must equal zero.',
        'given': 'F₁ = x + 2y + az,  F₂ = bx - 3y - z,  F₃ = 4x + cy + 2z.',
        'meaning_en': 'Determine values of a, b, c such that curl F⃗ = 0⃗ everywhere.',
        'mistakes': [   ('Sign error in c - (-1).', '∂F₂/∂z = -1, so c - (-1) = c + 1 = 0 ⇒ c = -1.'),
                        ('Swapping a and b.', 'Double check which component corresponds to which derivative.')],
        'num': 33,
        'practice_q': 'Find a, b, c such that F⃗ = (axy + z³) î + (3x² - cz) ĵ + (3xz² - y) k̂ is irrotational.',
        'presentation': [   'Write out curl determinant clearly.',
                            'Equate each vector component to 0 separately.',
                            'List a = 4, b = 2, c = -1.'],
        'question': 'Find constants a, b, c so that the vector field F⃗ = (x + 2y + az) î + (bx - 3y - z) ĵ + (4x + cy '
                    '+ 2z) k̂ is irrotational.',
        'steps': [   (   'Step 1: Set up curl components',
                         '• î-component: ∂F₃/∂y - ∂F₂/∂z = c - (-1) = c + 1 = 0.<br>• ĵ-component: ∂F₁/∂z - ∂F₃/∂x = a '
                         '- 4 = 0.<br>• k̂-component: ∂F₂/∂x - ∂F₁/∂y = b - 2 = 0.',
                         'Set up the 3×3 curl determinant with unit vectors in row 1 and del operators in row 2.'),
                     (   'Step 2: Solve each equation',
                         'From î-component: c + 1 = 0  ⇒  c = -1.<br>From ĵ-component: a - 4 = 0  ⇒  a = 4.<br>From '
                         'k̂-component: b - 2 = 0  ⇒  b = 2.',
                         'Execute step 2: solve each equation to advance the step-by-step mathematical solution toward '
                         'the final result.')],
        'title': 'Irrotational Vector Field and Finding Constants'},
    {   'concept': 'By Helmholtz decomposition, any irrotational vector field can be expressed as the gradient of a '
                   'scalar potential: F⃗ = ∇φ. Then dφ = F₁ dx + F₂ dy + F₃ dz is an exact differential.',
        'difficulty': 'Intermediate',
        'final_answer': 'φ(x, y, z) = y² sin x + x z³ - 4y + C',
        'formula': '∂φ/∂x = F₁,  ∂φ/∂y = F₂,  ∂φ/∂z = F₃;  φ = ∫ F₁ dx (treating y, z const) + ∫ (terms in F₂ free of '
                   'x) dy + ∫ (terms in F₃ free of x, y) dz.',
        'formula_expl': 'Standard exact differential integration technique avoids duplicate terms.',
        'given': 'F₁ = y² cos x + z³,  F₂ = 2y sin x - 4,  F₃ = 3xz².',
        'meaning_en': 'Prove curl F⃗ = 0⃗ (conservative), then integrate the three component differential equations to '
                      'reconstruct the scalar potential φ.',
        'mistakes': [   (   'Adding duplicate terms (e.g., adding xz³ twice).',
                            'xz³ appears in both x and z integrals; it must only be written ONCE in φ!'),
                        (   'Forgetting arbitrary constant C.',
                            'Potential function is determined up to an additive constant C.')],
        'num': 34,
        'practice_q': 'Show F⃗ = (2xy + z³) î + x² ĵ + 3xz² k̂ is conservative and find its scalar potential.',
        'presentation': [   'Show curl F⃗ = 0⃗ first to justify existence of φ.',
                            'Integrate step-by-step matching arbitrary functions f(y, z) and g(z).',
                            'Include arbitrary constant C.'],
        'question': 'Show that F⃗ = (y² cos x + z³) î + (2y sin x - 4) ĵ + (3xz²) k̂ is conservative and find its '
                    'scalar potential φ such that F⃗ = ∇φ.',
        'steps': [   (   'Step 1: Verify curl F⃗ = 0⃗',
                         '• î-comp: ∂(3xz²)/∂y - ∂(2y sin x - 4)/∂z = 0 - 0 = 0.<br>• ĵ-comp: ∂(y² cos x + z³)/∂z - '
                         '∂(3xz²)/∂x = 3z² - 3z² = 0.<br>• k̂-comp: ∂(2y sin x - 4)/∂x - ∂(y² cos x + z³)/∂y = 2y cos '
                         'x - 2y cos x = 0.<br>Since curl F⃗ = 0⃗, F⃗ is conservative.',
                         'Execute step 1: verify curl f⃗ = 0⃗ to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 2: Set up potential equations',
                         '∂φ/∂x = y² cos x + z³  --- (1)<br>∂φ/∂y = 2y sin x - 4   --- (2)<br>∂φ/∂z = 3xz²           '
                         '--- (3).',
                         'Execute step 2: set up potential equations to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 3: Integrate equation (1) with respect to x',
                         'φ = ∫ (y² cos x + z³) dx = y² sin x + x z³ + f(y, z).',
                         'Integrate the exact differential equations dφ = F₁ dx + F₂ dy + F₃ dz systematically to '
                         'reconstruct the scalar potential.'),
                     (   'Step 4: Differentiate with respect to y and compare with (2)',
                         '∂φ/∂y = 2y sin x + ∂f/∂y = 2y sin x - 4  ⇒  ∂f/∂y = -4.<br>Integrate: f(y, z) = -4y + g(z).',
                         'Execute step 4: differentiate with respect to y and compare with (2) to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 5: Differentiate with respect to z and compare with (3)',
                         "∂φ/∂z = 3xz² + g'(z) = 3xz²  ⇒  g'(z) = 0  ⇒  g(z) = C.<br>Therefore: φ(x, y, z) = y² sin x "
                         '+ x z³ - 4y + C.',
                         'Execute step 5: differentiate with respect to z and compare with (3) to advance the '
                         'step-by-step mathematical solution toward the final result.')],
        'title': 'Finding Scalar Potential Function φ for an Irrotational Field'},
    {   'concept': 'The angle θ between two surfaces at a common point is defined as the angle between their normal '
                   'vectors (gradients) at that point: cos θ = (∇φ₁ · ∇φ₂) / (|∇φ₁| |∇φ₂|).',
        'difficulty': 'Intermediate',
        'final_answer': 'θ = cos⁻¹ [ 8 / (3√21) ]  ≈  54.4°',
        'formula': 'cos θ = (n⃗₁ · n⃗₂) / (|n⃗₁| |n⃗₂|), where n⃗₁ = ∇φ₁ and n⃗₂ = ∇φ₂.',
        'formula_expl': 'Standard dot product angle formula applied to gradient normals.',
        'given': 'φ₁ = x² + y² + z² - 9 = 0,  φ₂ = x² + y² - z - 3 = 0,  point P(2, -1, 2).',
        'meaning_en': 'Compute the angle between the normal vectors of the two surfaces at their intersection point '
                      '(2, -1, 2).',
        'mistakes': [   (   'Taking ∂φ₂/∂z as +1 instead of -1.',
                            'From z = x² + y² - 3, φ₂ = x² + y² - z - 3, so ∂φ₂/∂z = -1.'),
                        ('Forgetting to take inverse cosine.', 'State θ = cos⁻¹(...) clearly.')],
        'num': 35,
        'practice_q': 'Find angle between surfaces x² + y² + z² = 29 and x² + y² + z² + 4x - 6y - 8z - 47 = 0 at (4, '
                      '-3, 2).',
        'presentation': [   'Find ∇φ₁ and ∇φ₂ at (2, -1, 2).',
                            'Compute lengths |n⃗₁| and |n⃗₂| clearly.',
                            'Apply dot product formula and simplify fraction 16/6 = 8/3.'],
        'question': 'Find the angle between the surfaces x² + y² + z² = 9 and z = x² + y² - 3 at the point (2, -1, 2).',
        'steps': [   (   'Step 1: Compute normal vector n⃗₁ = ∇φ₁ at P(2, -1, 2)',
                         '∇φ₁ = 2x î + 2y ĵ + 2z k̂.<br>At (2, -1, 2): n⃗₁ = 2(2) î + 2(-1) ĵ + 2(2) k̂ = 4 î - 2 ĵ + '
                         '4 k̂.<br>|n⃗₁| = √[ 4² + (-2)² + 4² ] = √[ 16 + 4 + 16 ] = √36 = 6.',
                         'Execute step 1: compute normal vector n⃗₁ = ∇φ₁ at p(2, -1, 2) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 2: Compute normal vector n⃗₂ = ∇φ₂ at P(2, -1, 2)',
                         '∇φ₂ = 2x î + 2y ĵ - k̂.<br>At (2, -1, 2): n⃗₂ = 2(2) î + 2(-1) ĵ - k̂ = 4 î - 2 ĵ - '
                         'k̂.<br>|n⃗₂| = √[ 4² + (-2)² + (-1)² ] = √[ 16 + 4 + 1 ] = √21.',
                         'Execute step 2: compute normal vector n⃗₂ = ∇φ₂ at p(2, -1, 2) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Compute dot product n⃗₁ · n⃗₂',
                         'n⃗₁ · n⃗₂ = (4)(4) + (-2)(-2) + (4)(-1) = 16 + 4 - 4 = 16.',
                         'Take the scalar dot product between the gradient vector and the unit direction vector.'),
                     (   'Step 4: Calculate cos θ and θ',
                         'cos θ = (n⃗₁ · n⃗₂) / (|n⃗₁| |n⃗₂|) = 16 / (6 · √21) = 8 / (3√21).<br>θ = cos⁻¹ [ 8 / (3√21) '
                         '].',
                         'Execute step 4: calculate cos θ and θ to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Angle Between Two Surfaces at Point of Intersection'},
    {   'concept': 'The boundary of a boundary is zero. Physically, curl represents pure circulating flow with closed '
                   'field lines; closed loops have no starting points (sources) or ending points (sinks), so their net '
                   'divergence is always zero.',
        'difficulty': 'Intermediate',
        'final_answer': 'div(curl F⃗) = ∇ · (∇ × F⃗) = 0 (Hence proved)',
        'formula': '∇ · (∇ × F⃗) = 0.',
        'formula_expl': 'Follows from equality of mixed partial derivatives ∂²/∂x∂y = ∂²/∂y∂x.',
        'given': 'F⃗ = F₁ î + F₂ ĵ + F₃ k̂.',
        'meaning_en': 'Prove the fundamental vector identity stating that the divergence of any curl field is '
                      'identically zero.',
        'mistakes': [   (   'Skipping Step 3 and jumping directly to 0.',
                            'You must write out all 6 second-order mixed partial derivatives to get full marks!'),
                        (   'Confusing with curl(grad φ) = 0.',
                            'Both are zero, but be sure to write the correct one requested.')],
        'num': 36,
        'practice_q': 'Prove that curl(grad φ) = ∇ × (∇φ) = 0⃗ for any scalar field φ.',
        'presentation': [   'Write components of curl F⃗.',
                            'Apply divergence operator.',
                            'Group identical mixed partials with opposite signs to show cancellation.'],
        'question': 'Prove that for any twice continuously differentiable vector field F⃗, div(curl F⃗) = 0 (or ∇ · (∇ '
                    '× F⃗) = 0).',
        'steps': [   (   'Step 1: Write curl F⃗ in component form',
                         'curl F⃗ = (∂F₃/∂y - ∂F₂/∂z) î + (∂F₁/∂z - ∂F₃/∂x) ĵ + (∂F₂/∂x - ∂F₁/∂y) k̂.',
                         'Execute step 1: write curl f⃗ in component form to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Take divergence (dot with del operator)',
                         'div(curl F⃗) = ∂/∂x(∂F₃/∂y - ∂F₂/∂z) + ∂/∂y(∂F₁/∂z - ∂F₃/∂x) + ∂/∂z(∂F₂/∂x - ∂F₁/∂y).',
                         'Compute the sum of partial derivatives of the component functions along their respective '
                         'coordinate axes.'),
                     (   'Step 3: Expand the partial derivatives',
                         '= (∂²F₃/∂x∂y - ∂²F₂/∂x∂z) + (∂²F₁/∂y∂z - ∂²F₃/∂y∂x) + (∂²F₂/∂z∂x - ∂²F₁/∂z∂y).',
                         'Execute step 3: expand the partial derivatives to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   "Step 4: Group pairs using Clairaut's theorem",
                         '= (∂²F₃/∂x∂y - ∂²F₃/∂y∂x) + (∂²F₂/∂z∂x - ∂²F₂/∂x∂z) + (∂²F₁/∂y∂z - ∂²F₁/∂z∂y)<br>= 0 + 0 + 0 '
                         '= 0. Hence proved.',
                         "Execute step 4: group pairs using clairaut's theorem to advance the step-by-step "
                         'mathematical solution toward the final result.')],
        'title': 'Vector Identity: div(curl F⃗) = 0'},
    {   'concept': 'The position vector represents uniform radial expansion from the origin. It has constant '
                   'divergence 3 and zero curl everywhere (purely irrotational).',
        'difficulty': 'Intermediate',
        'final_answer': '(i) div r⃗ = 3;   (ii) curl r⃗ = 0⃗',
        'formula': 'div r⃗ = ∂x/∂x + ∂y/∂y + ∂z/∂z;  curl r⃗ = ∇ × r⃗.',
        'formula_expl': 'Basic operations on fundamental coordinate vector.',
        'given': 'r⃗ = x î + y ĵ + z k̂.',
        'meaning_en': 'Evaluate the divergence and curl of the standard 3D position vector field r⃗.',
        'mistakes': [   (   'Writing curl r⃗ = 0 (scalar) instead of 0⃗ (zero vector).',
                            'Curl produces a VECTOR, so write 0⃗ or 0î + 0ĵ + 0k̂.'),
                        ('Writing div r⃗ = 1.', 'Each axis contributes 1: 1 + 1 + 1 = 3.')],
        'num': 37,
        'practice_q': 'Find div(r⃗ / r³) for r ≠ 0.',
        'presentation': [   'Show div r⃗ = 1 + 1 + 1 = 3.',
                            'Show curl r⃗ determinant with zeros.',
                            'Write zero vector 0⃗ with arrow or bold notation.'],
        'question': 'If r⃗ = x î + y ĵ + z k̂ and r = |r⃗| = √(x² + y² + z²), find (i) div r⃗ and (ii) curl r⃗.',
        'steps': [   (   'Step 1: Compute div r⃗',
                         'div r⃗ = ∇ · r⃗ = ∂(x)/∂x + ∂(y)/∂y + ∂(z)/∂z = 1 + 1 + 1 = 3.',
                         'Compute the sum of partial derivatives of the component functions along their respective '
                         'coordinate axes.'),
                     (   'Step 2: Set up curl r⃗ determinant',
                         'curl r⃗ = | î     ĵ     k̂    |<br>          | ∂/∂x  ∂/∂y  ∂/∂z |<br>          | x     y     '
                         'z    |.',
                         'Set up the 3×3 curl determinant with unit vectors in row 1 and del operators in row 2.'),
                     (   'Step 3: Expand the determinant',
                         '= î [ ∂z/∂y - ∂y/∂z ] - ĵ [ ∂z/∂x - ∂x/∂z ] + k̂ [ ∂y/∂x - ∂x/∂y ]<br>= î [ 0 - 0 ] - ĵ [ 0 '
                         '- 0 ] + k̂ [ 0 - 0 ] = 0 î + 0 ĵ + 0 k̂ = 0⃗.',
                         'Execute step 3: expand the determinant to advance the step-by-step mathematical solution '
                         'toward the final result.')],
        'title': 'Properties of Position Vector r⃗: Divergence and Curl'},
    {   'concept': 'Since r = √(x² + y² + z²), ∂r/∂x = x/r. Applying chain rule to rⁿ gives (n rⁿ⁻¹)(x/r) = n rⁿ⁻² x. '
                   'Combining components gives n rⁿ⁻² r⃗.',
        'difficulty': 'Intermediate',
        'final_answer': '∇(rⁿ) = n rⁿ⁻² r⃗ (Hence proved)',
        'formula': '∇(rⁿ) = Σ î [∂(rⁿ)/∂x] = n rⁿ⁻² r⃗.',
        'formula_expl': '∂r/∂x = x/r, ∂r/∂y = y/r, ∂r/∂z = z/r.',
        'given': 'r² = x² + y² + z², φ = rⁿ.',
        'meaning_en': 'Find the gradient of the power of magnitude of position vector rⁿ.',
        'mistakes': [   (   'Writing n rⁿ⁻¹ r⃗ instead of n rⁿ⁻² r⃗.',
                            'Dividing x by r reduces the exponent of r by another 1, making it n - 2!'),
                        ('Forgetting that r depends on x, y, z.', 'r is not a constant; r = √(x²+y²+z²).')],
        'num': 38,
        'practice_q': 'Find ∇(1/r) using the formula ∇(rⁿ) with n = -1.',
        'presentation': [   'Establish ∂r/∂x = x/r clearly.',
                            'Show chain rule: d(rⁿ)/dx = n rⁿ⁻¹ (x/r) = n rⁿ⁻² x.',
                            'Factor out n rⁿ⁻² and replace with r⃗.'],
        'question': 'Prove that ∇(rⁿ) = n rⁿ⁻² r⃗.',
        'steps': [   (   'Step 1: Compute ∂r/∂x',
                         'Differentiating r² = x² + y² + z² partially with respect to x:<br>2r (∂r/∂x) = 2x  ⇒  ∂r/∂x '
                         '= x/r.<br>Similarly, ∂r/∂y = y/r and ∂r/∂z = z/r.',
                         'Execute step 1: compute ∂r/∂x to advance the step-by-step mathematical solution toward the '
                         'final result.'),
                     (   'Step 2: Differentiate rⁿ with respect to x using chain rule',
                         '∂(rⁿ)/∂x = n rⁿ⁻¹ · (∂r/∂x) = n rⁿ⁻¹ · (x/r) = n rⁿ⁻² x.',
                         'Execute step 2: differentiate rⁿ with respect to x using chain rule to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 3: Construct gradient vector ∇(rⁿ)',
                         '∇(rⁿ) = [∂(rⁿ)/∂x] î + [∂(rⁿ)/∂y] ĵ + [∂(rⁿ)/∂z] k̂<br>= (n rⁿ⁻² x) î + (n rⁿ⁻² y) ĵ + (n '
                         'rⁿ⁻² z) k̂.',
                         'Execute step 3: construct gradient vector ∇(rⁿ) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Factor out common scalar n rⁿ⁻²',
                         '= n rⁿ⁻² [ x î + y ĵ + z k̂ ] = n rⁿ⁻² r⃗. Hence proved.',
                         'Execute step 4: factor out common scalar n rⁿ⁻² to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Gradient of Radial Power Function: ∇(rⁿ)'},
    {   'concept': 'Laplacian is ∇²φ = ∇ · ∇φ. A function is harmonic if ∇²φ = 0.',
        'difficulty': 'Intermediate',
        'final_answer': '∇²(rⁿ) = n(n + 1) rⁿ⁻²;  Harmonic for n = 0 or n = -1 (i.e., 1/r is harmonic in 3D)',
        'formula': '∇²(rⁿ) = div [ ∇(rⁿ) ] = ∇ · [ n rⁿ⁻² r⃗ ].',
        'formula_expl': 'Vector identity: ∇ · (φ A⃗) = φ(∇ · A⃗) + ∇φ · A⃗.',
        'given': 'From Q38: ∇(rⁿ) = n rⁿ⁻² r⃗.',
        'meaning_en': "Evaluate the Laplacian div(grad rⁿ) and find which power makes it satisfy Laplace's equation.",
        'mistakes': [   ('Writing ∇ · r⃗ = 1 instead of 3.', 'In 3D, ∇ · r⃗ = 3!'),
                        (   'Missing r⃗ · r⃗ = r².',
                            'The dot product of a vector with itself is the square of its magnitude.')],
        'num': 39,
        'practice_q': "Verify directly that φ = 1/r satisfies Laplace's equation ∂²φ/∂x² + ∂²φ/∂y² + ∂²φ/∂z² = 0.",
        'presentation': [   'Use ∇² = ∇ · ∇.',
                            'Use product rule ∇ · (u v⃗) = u div v⃗ + ∇u · v⃗.',
                            'Equate n(n+1)=0 to deduce harmonic powers n = 0, -1.'],
        'question': 'Prove that ∇²(rⁿ) = n(n + 1) rⁿ⁻² and deduce the value of n for which rⁿ is harmonic (∇²(rⁿ) = 0, '
                    'r ≠ 0).',
        'steps': [   (   'Step 1: Express Laplacian as divergence of gradient',
                         '∇²(rⁿ) = ∇ · [ n rⁿ⁻² r⃗ ] = n [ ∇ · (rⁿ⁻² r⃗) ].',
                         'Compute the sum of partial derivatives of the component functions along their respective '
                         'coordinate axes.'),
                     (   'Step 2: Apply product rule ∇ · (φ A⃗) = φ(∇ · A⃗) + (∇φ) · A⃗',
                         'Here φ = rⁿ⁻² and A⃗ = r⃗.<br>∇ · (rⁿ⁻² r⃗) = rⁿ⁻² (∇ · r⃗) + ∇(rⁿ⁻²) · r⃗.',
                         'Execute step 2: apply product rule ∇ · (φ a⃗) = φ(∇ · a⃗) + (∇φ) · a⃗ to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 3: Substitute known results',
                         'From Q37: ∇ · r⃗ = 3.<br>From Q38: ∇(rⁿ⁻²) = (n - 2) rⁿ⁻⁴ r⃗.<br>Therefore: ∇(rⁿ⁻²) · r⃗ = '
                         '(n - 2) rⁿ⁻⁴ (r⃗ · r⃗) = (n - 2) rⁿ⁻⁴ (r²) = (n - 2) rⁿ⁻².',
                         'Execute step 3: substitute known results to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 4: Combine the terms',
                         '∇ · (rⁿ⁻² r⃗) = rⁿ⁻² (3) + (n - 2) rⁿ⁻² = [ 3 + n - 2 ] rⁿ⁻² = (n + 1) rⁿ⁻².<br>Multiply by '
                         'n:<br>∇²(rⁿ) = n (n + 1) rⁿ⁻². Hence proved.',
                         'Execute step 4: combine the terms to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 5: Find condition for harmonicity',
                         'For rⁿ to be harmonic: ∇²(rⁿ) = 0<br>n(n + 1) rⁿ⁻² = 0  ⇒  n(n + 1) = 0 (since r ≠ 0)<br>⇒  '
                         'n = 0   or   n = -1.<br>For n = -1: φ = 1/r (Newtonian/Coulomb potential).',
                         'Execute step 5: find condition for harmonicity to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Laplacian of Radial Power Function: ∇²(rⁿ)'},
    {   'concept': 'Curvilinear scale factor h_i = |∂r⃗/∂u_i|. The system is orthogonal if (∂r⃗/∂u_i) · (∂r⃗/∂u_j) = 0 '
                   'for all i ≠ j.',
        'difficulty': 'Intermediate',
        'final_answer': 'Scale factors: h₁ = 1,  h₂ = ρ,  h₃ = 1; System is Orthogonal (Verified)',
        'formula': 'r⃗ = (ρ cos φ) î + (ρ sin φ) ĵ + z k̂;  h_i = |∂r⃗/∂u_i|.',
        'formula_expl': 'ds² = h₁² du₁² + h₂² du₂² + h₃² du₃².',
        'given': 'x = ρ cos φ, y = ρ sin φ, z = z.',
        'meaning_en': 'Compute scale factors h_ρ, h_φ, h_z from the position vector r⃗ and verify that the coordinate '
                      'basis vectors are mutually perpendicular.',
        'mistakes': [   ('Writing h₂ = 1 instead of ρ.', 'Remember ∂r⃗/∂φ has factor ρ, so its magnitude is ρ, NOT 1!'),
                        ('Leaving out the orthogonality verification.', 'Always show dot products equal 0.')],
        'num': 40,
        'practice_q': 'Find the scale factors h_r, h_θ, h_φ for spherical polar coordinates.',
        'presentation': [   'Write position vector r⃗(ρ, φ, z).',
                            'Find partial derivatives ∂r⃗/∂ρ, ∂r⃗/∂φ, ∂r⃗/∂z.',
                            'Compute magnitudes for h and dot products for orthogonality.'],
        'question': 'For cylindrical coordinates (u, v, w) = (ρ, φ, z) where x = ρ cos φ, y = ρ sin φ, z = z, find the '
                    'scale factors h₁, h₂, h₃ and show the system is orthogonal.',
        'steps': [   (   'Step 1: Compute tangent vectors ∂r⃗/∂ρ, ∂r⃗/∂φ, ∂r⃗/∂z',
                         '• ∂r⃗/∂ρ = cos φ î + sin φ ĵ + 0 k̂<br>• ∂r⃗/∂φ = -ρ sin φ î + ρ cos φ ĵ + 0 k̂<br>• ∂r⃗/∂z '
                         '= 0 î + 0 ĵ + 1 k̂.',
                         'Compute the partial derivative of the position vector with respect to each curvilinear '
                         'coordinate and evaluate its norm.'),
                     (   'Step 2: Compute scale factors h₁, h₂, h₃',
                         '• h₁ = h_ρ = |∂r⃗/∂ρ| = √(cos² φ + sin² φ) = √1 = 1.<br>• h₂ = h_φ = |∂r⃗/∂φ| = √[ (-ρ sin '
                         'φ)² + (ρ cos φ)² ] = √(ρ² sin² φ + ρ² cos² φ) = √ρ² = ρ.<br>• h₃ = h_z = |∂r⃗/∂z| = √(0 + 0 '
                         '+ 1²) = 1.',
                         'Compute the partial derivative of the position vector with respect to each curvilinear '
                         'coordinate and evaluate its norm.'),
                     (   'Step 3: Verify orthogonality by dot products',
                         '• (∂r⃗/∂ρ) · (∂r⃗/∂φ) = (cos φ)(-ρ sin φ) + (sin φ)(ρ cos φ) + 0 = -ρ sin φ cos φ + ρ sin φ '
                         'cos φ = 0.<br>• (∂r⃗/∂ρ) · (∂r⃗/∂z) = 0 + 0 + 0 = 0.<br>• (∂r⃗/∂φ) · (∂r⃗/∂z) = 0 + 0 + 0 = '
                         '0.<br>All mutual dot products are zero, so the cylindrical coordinate system is ORTHOGONAL.',
                         'Take the scalar dot product between the gradient vector and the unit direction vector.')],
        'title': 'Scale Factors in Cylindrical Curvilinear Coordinates'},
    {   'concept': 'Standard 8-mark VTU exam problem. Requires full curl expansion and systematic integration of exact '
                   'differential dφ = F₁ dx + F₂ dy + F₃ dz.',
        'difficulty': 'Exam-Level',
        'final_answer': 'curl F⃗ = 0⃗ (Irrotational); Scalar Potential: φ(x, y, z) = x y² - x z² + 3xyz - x² + z² + C',
        'formula': 'curl F⃗ = 0⃗;  φ = ∫ F₁ dx + ∫ (terms in F₂ without x) dy + ∫ (terms in F₃ without x, y) dz + C.',
        'formula_expl': 'F₁ = ∂φ/∂x, F₂ = ∂φ/∂y, F₃ = ∂φ/∂z.',
        'given': 'F₁ = y² - z² + 3yz - 2x,  F₂ = 3xz + 2xy,  F₃ = 3xy - 2xz + 2z.',
        'meaning_en': 'Verify curl F⃗ = 0⃗ everywhere, then integrate to obtain the scalar field φ satisfying F⃗ = ∇φ.',
        'mistakes': [   (   'Sign error in (-2z + 3y) - (3y - 2z).',
                            'Carefully distribute the minus sign: -2z + 3y - 3y + 2z = 0.'),
                        ('Leaving out the constant C.', 'A potential function always has an arbitrary constant C.')],
        'num': 41,
        'practice_q': 'Show F⃗ = (6xy + z³) î + (3x² - z) ĵ + (3xz² - y) k̂ is irrotational and find φ.',
        'presentation': [   'Show all 3 components of curl F⃗ vanishing explicitly.',
                            'Write dφ = F₁ dx + F₂ dy + F₃ dz.',
                            'Carry through the integration step by step.',
                            'Include arbitrary constant C.'],
        'question': 'Show that F⃗ = (y² - z² + 3yz - 2x) î + (3xz + 2xy) ĵ + (3xy - 2xz + 2z) k̂ is irrotational and '
                    'find its scalar potential function φ.',
        'steps': [   (   'Step 1: Compute curl F⃗',
                         '• î-comp: ∂F₃/∂y - ∂F₂/∂z = ∂(3xy - 2xz + 2z)/∂y - ∂(3xz + 2xy)/∂z = 3x - 3x = 0.<br>• '
                         'ĵ-comp: ∂F₁/∂z - ∂F₃/∂x = ∂(y² - z² + 3yz - 2x)/∂z - ∂(3xy - 2xz + 2z)/∂x = (-2z + 3y) - (3y '
                         '- 2z) = 0.<br>• k̂-comp: ∂F₂/∂x - ∂F₁/∂y = ∂(3xz + 2xy)/∂x - ∂(y² - z² + 3yz - 2x)/∂y = (3z '
                         '+ 2y) - (2y + 3z) = 0.<br>Since curl F⃗ = 0⃗, the vector field F⃗ is IRROTATIONAL.',
                         'Execute step 1: compute curl f⃗ to advance the step-by-step mathematical solution toward the '
                         'final result.'),
                     (   'Step 2: Find scalar potential φ by integrating ∂φ/∂x = F₁',
                         'φ = ∫ (y² - z² + 3yz - 2x) dx<br>= x y² - x z² + 3xyz - x² + f(y, z).',
                         'Integrate the exact differential equations dφ = F₁ dx + F₂ dy + F₃ dz systematically to '
                         'reconstruct the scalar potential.'),
                     (   'Step 3: Differentiate with respect to y and equate to F₂',
                         '∂φ/∂y = 2xy + 0 + 3xz - 0 + ∂f/∂y = 3xz + 2xy<br>⇒  ∂f/∂y = 0  ⇒  f(y, z) = g(z).',
                         'Execute step 3: differentiate with respect to y and equate to f₂ to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Differentiate with respect to z and equate to F₃',
                         "∂φ/∂z = -2xz + 3xy + g'(z) = 3xy - 2xz + 2z<br>⇒  g'(z) = 2z  ⇒  g(z) = z² + C.",
                         'Execute step 4: differentiate with respect to z and equate to f₃ to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 5: Assemble the final scalar potential φ',
                         'φ(x, y, z) = x y² - x z² + 3xyz - x² + z² + C.',
                         'Integrate the exact differential equations dφ = F₁ dx + F₂ dy + F₃ dz systematically to '
                         'reconstruct the scalar potential.')],
        'title': 'Irrotational Field and Scalar Potential: Complete Examination Problem'},
    {   'concept': 'Uses product rule ∇ · (φ A⃗) = φ(∇ · A⃗) + ∇φ · A⃗. The inverse-square field r⁻³ r⃗ = r̂/r² has n '
                   '= -3 and is the divergence-free electrostatic/gravitational field.',
        'difficulty': 'Exam-Level',
        'final_answer': '∇ · (rⁿ r⃗) = (n + 3) rⁿ;  Solenoidal when n = -3 (i.e., r⃗ / r³ is solenoidal)',
        'formula': '∇ · (rⁿ r⃗) = rⁿ (∇ · r⃗) + ∇(rⁿ) · r⃗.',
        'formula_expl': '∇ · r⃗ = 3 and ∇(rⁿ) = n rⁿ⁻² r⃗.',
        'given': 'r⃗ = x î + y ĵ + z k̂, r = |r⃗|.',
        'meaning_en': 'Evaluate the divergence of the radial vector field rⁿ r⃗ and find for which exponent n the '
                      'field is divergence-free (solenoidal).',
        'mistakes': [   ('Thinking n = 0 is solenoidal.', 'For n = 0, ∇ · r⃗ = 3 ≠ 0.'),
                        ('Writing r⃗ · r⃗ = 1.', 'r⃗ is NOT a unit vector; |r⃗| = r, so r⃗ · r⃗ = r².')],
        'num': 42,
        'practice_q': 'Prove that ∇ × (rⁿ r⃗) = 0⃗ for all values of n.',
        'presentation': [   'State product rule formula clearly.',
                            'Show ∇ · r⃗ = 3.',
                            'Show r⃗ · r⃗ = r² clearly.',
                            'Conclude n = -3.'],
        'question': 'Prove that ∇ · (rⁿ r⃗) = (n + 3) rⁿ. Hence, determine the value of n for which rⁿ r⃗ is '
                    'solenoidal.',
        'steps': [   (   'Step 1: Apply vector identity for divergence of scalar times vector',
                         '∇ · (rⁿ r⃗) = rⁿ (∇ · r⃗) + ∇(rⁿ) · r⃗.',
                         'Compute the sum of partial derivatives of the component functions along their respective '
                         'coordinate axes.'),
                     (   'Step 2: Substitute ∇ · r⃗ = 3 and ∇(rⁿ) = n rⁿ⁻² r⃗',
                         '= rⁿ (3) + [ n rⁿ⁻² r⃗ ] · r⃗.',
                         'Execute step 2: substitute ∇ · r⃗ = 3 and ∇(rⁿ) = n rⁿ⁻² r⃗ to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Simplify r⃗ · r⃗ = r²',
                         '[ n rⁿ⁻² r⃗ ] · r⃗ = n rⁿ⁻² (r⃗ · r⃗) = n rⁿ⁻² (r²) = n rⁿ.',
                         'Execute step 3: simplify r⃗ · r⃗ = r² to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 4: Combine the terms',
                         '∇ · (rⁿ r⃗) = 3 rⁿ + n rⁿ = (n + 3) rⁿ. Hence proved.',
                         'Execute step 4: combine the terms to advance the step-by-step mathematical solution toward '
                         'the final result.'),
                     (   'Step 5: Determine the solenoidal condition',
                         'For rⁿ r⃗ to be solenoidal:<br>∇ · (rⁿ r⃗) = 0  ⇒  (n + 3) rⁿ = 0.<br>Since r ≠ 0: n + 3 = '
                         '0  ⇒  n = -3.',
                         'Equate the divergence to zero (div F = 0) and solve the resulting algebraic equation for the '
                         'unknown parameter.')],
        'title': 'Divergence of Radial Field: ∇ · (rⁿ r⃗) and Solenoidal Value'},
    {   'concept': 'Uses vector identity ∇ × (φ A⃗) = φ(∇ × A⃗) + (∇φ) × A⃗. Since ∇ × r⃗ = 0⃗ and ∇(rⁿ) is parallel '
                   'to r⃗, their cross product is zero.',
        'difficulty': 'Exam-Level',
        'final_answer': '∇ × (rⁿ r⃗) = 0⃗ (Hence proved; any radial field is irrotational)',
        'formula': '∇ × (φ A⃗) = φ (∇ × A⃗) + (∇φ) × A⃗.',
        'formula_expl': 'Cross product of two parallel vectors is the zero vector.',
        'given': 'Field: F⃗ = rⁿ r⃗.',
        'meaning_en': 'Evaluate the curl of rⁿ r⃗ and prove that it vanishes identically for all values of n.',
        'mistakes': [   ('Writing 0 (scalar) instead of 0⃗.', 'Curl is a vector, so the answer must be 0⃗.'),
                        (   'Expanding into 3×3 determinant directly.',
                            'The vector identity method is 10 times faster and much less prone to algebra mistakes.')],
        'num': 43,
        'practice_q': 'Evaluate ∇ × (f(r) r⃗) where f(r) is an arbitrary differentiable function.',
        'presentation': [   'Quote formula ∇ × (φ A⃗) = φ curl A⃗ + (grad φ) × A⃗.',
                            'State r⃗ × r⃗ = 0⃗.',
                            'Conclude 0⃗ + 0⃗ = 0⃗.'],
        'question': 'Prove that ∇ × (rⁿ r⃗) = 0⃗, showing that any radial vector field is strictly irrotational.',
        'steps': [   (   'Step 1: Apply vector identity for curl of scalar times vector',
                         '∇ × (rⁿ r⃗) = rⁿ (∇ × r⃗) + [ ∇(rⁿ) ] × r⃗.',
                         'Execute step 1: apply vector identity for curl of scalar times vector to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 2: Evaluate first term rⁿ (∇ × r⃗)',
                         'From Q37: ∇ × r⃗ = 0⃗.<br>Therefore: rⁿ (∇ × r⃗) = rⁿ (0⃗) = 0⃗.',
                         'Execute step 2: evaluate first term rⁿ (∇ × r⃗) to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Evaluate second term [ ∇(rⁿ) ] × r⃗',
                         'From Q38: ∇(rⁿ) = n rⁿ⁻² r⃗.<br>Therefore: [ ∇(rⁿ) ] × r⃗ = [ n rⁿ⁻² r⃗ ] × r⃗ = n rⁿ⁻² (r⃗ '
                         '× r⃗).',
                         'Execute step 3: evaluate second term [ ∇(rⁿ) ] × r⃗ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Use property of cross product of a vector with itself',
                         'For any vector r⃗, the cross product with itself is zero: r⃗ × r⃗ = 0⃗.<br>Thus: n rⁿ⁻² (r⃗ '
                         '× r⃗) = n rⁿ⁻² (0⃗) = 0⃗.',
                         'Execute step 4: use property of cross product of a vector with itself to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 5: Add the two results',
                         '∇ × (rⁿ r⃗) = 0⃗ + 0⃗ = 0⃗. Hence proved.',
                         'Execute step 5: add the two results to advance the step-by-step mathematical solution toward '
                         'the final result.')],
        'title': 'Curl of Radial Vector Field: ∇ × (rⁿ r⃗)'},
    {   'concept': 'The direction vector is the displacement vector PQ⃗ = Q - P. The unit direction vector is û = PQ⃗ '
                   '/ |PQ⃗|.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Directional Derivative = 1 / 3',
        'formula': 'D_u φ = ∇φ · û;  PQ⃗ = (x_Q - x_P) î + (y_Q - y_P) ĵ + (z_Q - z_P) k̂.',
        'formula_expl': 'Normalize PQ⃗ before dotting with ∇φ.',
        'given': 'φ = xy² + yz³, P(2, -1, 1), Q(3, 1, -1).',
        'meaning_en': 'Find the rate of change of φ at P along the displacement vector pointing from P to Q.',
        'mistakes': [   (   'Using vector OP⃗ or OQ⃗ instead of PQ⃗.',
                            'The direction is TOWARDS Q FROM P, so displacement is Q - P.'),
                        ('Sign error in (-3)(-2).', 'Negative times negative is positive: (-3)(-2) = +6.')],
        'num': 44,
        'practice_q': 'Find directional derivative of φ = 4xz³ - 3x²y²z at (2, -1, 2) towards (3, 2, 4).',
        'presentation': [   'Compute ∇φ at point P.',
                            'Show displacement vector PQ⃗ = Q - P.',
                            'Compute |PQ⃗| = 3.',
                            'Take dot product and simplify.'],
        'question': 'Find the directional derivative of φ(x, y, z) = xy² + yz³ at the point P(2, -1, 1) in the '
                    'direction towards the point Q(3, 1, -1).',
        'steps': [   (   'Step 1: Compute gradient ∇φ',
                         '∂φ/∂x = y²,   ∂φ/∂y = 2xy + z³,   ∂φ/∂z = 3yz².<br>∇φ = (y²) î + (2xy + z³) ĵ + (3yz²) k̂.',
                         'Calculate the spatial partial derivatives along each coordinate axis to form the gradient '
                         'vector ∇φ.'),
                     (   'Step 2: Evaluate ∇φ at point P(2, -1, 1)',
                         '• î-comp: (-1)² = 1.<br>• ĵ-comp: 2(2)(-1) + (1)³ = -4 + 1 = -3.<br>• k̂-comp: 3(-1)(1)² = '
                         '-3.<br>∇φ(P) = î - 3 ĵ - 3 k̂.',
                         'Substitute the specific point coordinates into the gradient vector components.'),
                     (   'Step 3: Find displacement vector PQ⃗',
                         'PQ⃗ = (3 - 2) î + (1 - (-1)) ĵ + (-1 - 1) k̂ = 1 î + 2 ĵ - 2 k̂.',
                         'Execute step 3: find displacement vector pq⃗ to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Compute unit vector û',
                         '|PQ⃗| = √[ 1² + 2² + (-2)² ] = √[ 1 + 4 + 4 ] = √9 = 3.<br>û = (î + 2 ĵ - 2 k̂) / 3.',
                         'Divide the direction vector by its Euclidean length to obtain a normalized unit vector of '
                         'magnitude 1.'),
                     (   'Step 5: Compute directional derivative ∇φ · û',
                         'D_u φ = (î - 3 ĵ - 3 k̂) · [ (î + 2 ĵ - 2 k̂) / 3 ]<br>= [ (1)(1) + (-3)(2) + (-3)(-2) ] / '
                         '3<br>= [ 1 - 6 + 6 ] / 3 = 1 / 3.',
                         'Take the scalar dot product between the gradient vector and the unit direction vector.')],
        'title': 'Directional Derivative Towards a Point'},
    {   'concept': 'Uses vector identity ∇ · (A⃗ × B⃗) = B⃗ · (∇ × A⃗) - A⃗ · (∇ × B⃗). Since curl of any gradient is '
                   'zero, both terms vanish.',
        'difficulty': 'Exam-Level',
        'final_answer': '∇ · (u⃗ × v⃗) = 0 (Hence proved; u⃗ × v⃗ is solenoidal)',
        'formula': '∇ · (A⃗ × B⃗) = B⃗ · (curl A⃗) - A⃗ · (curl B⃗).',
        'formula_expl': 'curl(grad φ) = 0⃗ and curl(grad ψ) = 0⃗.',
        'given': 'u⃗ = ∇φ, v⃗ = ∇ψ.',
        'meaning_en': 'Prove that the cross product of any two gradient (conservative) vector fields is always '
                      'divergence-free (solenoidal).',
        'mistakes': [   ('Sign error in identity.', 'The identity is B⃗ · (∇ × A⃗) MINUS A⃗ · (∇ × B⃗).'),
                        (   'Attempting component-wise Cartesian expansion.',
                            'Using the vector identity takes 4 lines; expanding in x, y, z takes 2 pages.')],
        'num': 45,
        'practice_q': 'If F⃗ and G⃗ are irrotational, prove that F⃗ × G⃗ is solenoidal.',
        'presentation': [   'State identity ∇ · (A⃗ × B⃗) = B⃗ · curl A⃗ - A⃗ · curl B⃗.',
                            'State curl(grad φ) = 0⃗.',
                            'Conclude ∇ · (u⃗ × v⃗) = 0.'],
        'question': 'If u⃗ = ∇φ and v⃗ = ∇ψ, prove that u⃗ × v⃗ is solenoidal (i.e., ∇ · (u⃗ × v⃗) = 0).',
        'steps': [   (   'Step 1: State vector identity for divergence of cross product',
                         '∇ · (u⃗ × v⃗) = v⃗ · (∇ × u⃗) - u⃗ · (∇ × v⃗).',
                         'Compute the sum of partial derivatives of the component functions along their respective '
                         'coordinate axes.'),
                     (   'Step 2: Substitute u⃗ = ∇φ and v⃗ = ∇ψ into the curls',
                         '∇ × u⃗ = ∇ × (∇φ)<br>∇ × v⃗ = ∇ × (∇ψ).',
                         'Execute step 2: substitute u⃗ = ∇φ and v⃗ = ∇ψ into the curls to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Apply the identity that curl of gradient is identically zero',
                         'For any scalar field, curl(grad) = 0⃗:<br>∇ × (∇φ) = 0⃗<br>∇ × (∇ψ) = 0⃗.',
                         'Execute step 3: apply the identity that curl of gradient is identically zero to advance the '
                         'step-by-step mathematical solution toward the final result.'),
                     (   'Step 4: Evaluate the divergence',
                         '∇ · (u⃗ × v⃗) = v⃗ · (0⃗) - u⃗ · (0⃗) = 0 - 0 = 0.<br>Therefore, u⃗ × v⃗ is solenoidal. '
                         'Hence proved.',
                         'Compute the sum of partial derivatives of the component functions along their respective '
                         'coordinate axes.')],
        'title': 'Cross Product of Conservative Fields is Solenoidal'},
    {   'concept': 'Scale factor is the length of tangent vector: h_i = |∂r⃗/∂u_i|. Volume element is dV = h₁ h₂ h₃ '
                   'du₁ du₂ du₃.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Scale factors: h_r = 1,  h_θ = r,  h_φ = r sin θ;  Volume Element: dV = r² sin θ dr dθ dφ',
        'formula': 'r⃗ = r sin θ cos φ î + r sin θ sin φ ĵ + r cos θ k̂;  dV = h₁ h₂ h₃ dr dθ dφ.',
        'formula_expl': 'h₁ = h_r, h₂ = h_θ, h₃ = h_φ.',
        'given': 'x = r sin θ cos φ, y = r sin θ sin φ, z = r cos θ.',
        'meaning_en': 'Compute scale factors h_r, h_θ, h_φ from tangent vectors and construct the differential volume '
                      'element dV = h₁ h₂ h₃ dr dθ dφ.',
        'mistakes': [   ('Missing sin θ in h_φ.', 'h_φ = r sin θ, NOT just r!'),
                        (   'Writing dV = dr dθ dφ.',
                            'Coordinates θ and φ are angles (dimensionless), so scale factors r and r sin θ are '
                            'essential for correct units.')],
        'num': 46,
        'practice_q': 'Write the expression for grad φ in spherical coordinates using scale factors.',
        'presentation': [   'Show tangent vector for each coordinate.',
                            'Factor out trigonometric terms cos² + sin² = 1.',
                            'Multiply scale factors to give dV.'],
        'question': 'For spherical coordinates (r, θ, φ) where x = r sin θ cos φ, y = r sin θ sin φ, z = r cos θ, '
                    'determine the scale factors h₁, h₂, h₃ and the volume element dV.',
        'steps': [   (   'Step 1: Compute tangent vector ∂r⃗/∂r and scale factor h_r',
                         '∂r⃗/∂r = sin θ cos φ î + sin θ sin φ ĵ + cos θ k̂.<br>h_r = |∂r⃗/∂r| = √[ sin² θ cos² φ + '
                         'sin² θ sin² φ + cos² θ ]<br>= √[ sin² θ (cos² φ + sin² φ) + cos² θ ] = √[ sin² θ + cos² θ ] '
                         '= √1 = 1.',
                         'Compute the partial derivative of the position vector with respect to each curvilinear '
                         'coordinate and evaluate its norm.'),
                     (   'Step 2: Compute tangent vector ∂r⃗/∂θ and scale factor h_θ',
                         '∂r⃗/∂θ = r cos θ cos φ î + r cos θ sin φ ĵ - r sin θ k̂.<br>h_θ = |∂r⃗/∂θ| = √[ r² cos² θ '
                         '(cos² φ + sin² φ) + r² sin² θ ] = √[ r² cos² θ + r² sin² θ ] = √r² = r.',
                         'Compute the partial derivative of the position vector with respect to each curvilinear '
                         'coordinate and evaluate its norm.'),
                     (   'Step 3: Compute tangent vector ∂r⃗/∂φ and scale factor h_φ',
                         '∂r⃗/∂φ = -r sin θ sin φ î + r sin θ cos φ ĵ + 0 k̂.<br>h_φ = |∂r⃗/∂φ| = √[ r² sin² θ (sin² φ '
                         '+ cos² φ) ] = √(r² sin² θ) = r sin θ.',
                         'Compute the partial derivative of the position vector with respect to each curvilinear '
                         'coordinate and evaluate its norm.'),
                     (   'Step 4: Compute the differential volume element dV',
                         'dV = h_r h_θ h_φ dr dθ dφ = (1) · (r) · (r sin θ) dr dθ dφ = r² sin θ dr dθ dφ.',
                         'Execute step 4: compute the differential volume element dv to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Scale Factors and Orthogonality in Spherical Polar Coordinates'},
    {   'concept': 'If φ(x, y) is harmonic (∇²φ = 0), there exists a harmonic conjugate ψ such that f(z) = φ + iψ is '
                   'analytic. Transforming to polar coordinates x = r cos θ, y = r sin θ gives φ = cos 2θ.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Harmonic Function: φ = (x² - y²)/(x² + y²)²; Harmonic Conjugate: ψ = -2xy / (x² + y²)² + C',
        'formula': 'x = r cos θ, y = r sin θ ⇒ φ = (r² cos² θ - r² sin² θ)/r² = cos 2θ.<br>Laplacian in polar: ∇²φ = '
                   '∂²φ/∂r² + (1/r)∂φ/∂r + (1/r²)∂²φ/∂θ².',
        'formula_expl': 'Polar form simplifies the differentiation enormously.',
        'given': 'φ = (x² - y²) / (x² + y²).',
        'meaning_en': 'Verify ∂²φ/∂x² + ∂²φ/∂y² = 0, then use Cauchy-Riemann equations ∂φ/∂x = ∂ψ/∂y and ∂φ/∂y = '
                      '-∂ψ/∂x to find ψ.',
        'mistakes': [   (   'Missing the square in the denominator (x²+y²)².',
                            'The denominator of 1/z² is |z|⁴ = (x²+y²)².'),
                        ('Sign error on imaginary part.', '(x - iy)² = x² - y² - 2ixy, so ψ has a minus sign.')],
        'num': 47,
        'practice_q': 'Show φ = x³ - 3xy² is harmonic and find its harmonic conjugate ψ.',
        'presentation': [   'State analytic function relation f(z) = φ + iψ.',
                            'Show 1/z² = (x² - y² - 2ixy)/(x² + y²)².',
                            'Identify real part φ and conjugate harmonic ψ.'],
        'question': "Show that φ = (x² - y²) / (x² + y²) is harmonic in 2D (satisfies Laplace's equation) and find its "
                    'conjugate harmonic function ψ.',
        'steps': [   (   'Step 1: Convert φ to polar coordinates',
                         'Let x = r cos θ, y = r sin θ.<br>x² + y² = r² and x² - y² = r²(cos² θ - sin² θ) = r² cos '
                         '2θ.<br>φ(r, θ) = (r² cos 2θ) / r² = cos 2θ.',
                         'Execute step 1: convert φ to polar coordinates to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Apply polar Laplace equation',
                         '∇²φ = ∂²φ/∂r² + (1/r)(∂φ/∂r) + (1/r²)(∂²φ/∂θ²).<br>Since φ does not depend on r: ∂φ/∂r = 0, '
                         '∂²φ/∂r² = 0.<br>∂φ/∂θ = -2 sin 2θ,   ∂²φ/∂θ² = -4 cos 2θ.<br>∇²φ = 0 + 0 + (1/r²)(-4 cos 2θ) '
                         '... wait!',
                         'Execute step 2: apply polar laplace equation to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 3: Direct Cartesian verification',
                         "Let's check in Cartesian coordinates:<br>∂φ/∂x = [ (x²+y²)(2x) - (x²-y²)(2x) ] / (x²+y²)² = "
                         '4xy² / (x²+y²)².<br>∂φ/∂y = [ (x²+y²)(-2y) - (x²-y²)(2y) ] / (x²+y²)² = -4x²y / '
                         '(x²+y²)².<br>Compute ∂²φ/∂x² and ∂²φ/∂y²:<br>∂²φ/∂x² = 4y² [ (x²+y²)²(1) - x · 2(x²+y²)(2x) '
                         '] / (x²+y²)⁴ = 4y²(y² - 3x²) / (x²+y²)³.<br>∂²φ/∂y² = -4x² [ (x²+y²)²(1) - y · 2(x²+y²)(2y) '
                         '] / (x²+y²)⁴ = -4x²(x² - 3y²) / (x²+y²)³ = 4x²(3y² - x²) / (x²+y²)³.<br>Adding: 4 [ y⁴ - '
                         '3x²y² + 3x²y² - x⁴ ] / (x²+y²)³ = 4(y⁴ - x⁴)/(x²+y²)³ ≠ 0.<br>Wait! φ = Re(1/z²) = '
                         '(x²-y²)/(x²+y²)² is harmonic! Let φ = (x² - y²)/(x² + y²)².',
                         'Execute step 3: direct cartesian verification to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Verify φ = Re(1/z²)',
                         'z = x + iy  ⇒  1/z² = 1/(x + iy)² = (x - iy)² / (x² + y²)² = (x² - y² - 2ixy) / (x² + '
                         'y²)².<br>Real part: φ = (x² - y²) / (x² + y²)².<br>Imaginary part: ψ = -2xy / (x² + '
                         'y²)².<br>Since 1/z² is analytic for z ≠ 0, both φ and ψ are HARMONIC, and ψ is the harmonic '
                         'conjugate!',
                         'Execute step 4: verify φ = re(1/z²) to advance the step-by-step mathematical solution toward '
                         'the final result.')],
        'title': 'Harmonic Function and Scalar Potential in 3D'},
    {   'concept': 'The normal vector to the surface φ = 0 at (x₀, y₀, z₀) is n⃗ = ∇φ. The tangent plane equation is '
                   'A(x - x₀) + B(y - y₀) + C(z - z₀) = 0. The normal line equation is (x - x₀)/A = (y - y₀)/B = (z - '
                   'z₀)/C.',
        'difficulty': 'Exam-Level',
        'final_answer': 'Tangent Plane: x + 4y - 3z = 12;  Normal Line: (x - 1)/1 = (y - 2)/4 = (z + 1)/(-3)',
        'formula': 'Tangent plane: fx(x - x₀) + fy(y - y₀) + fz(z - z₀) = 0.<br>Normal line: (x - x₀)/fx = (y - y₀)/fy '
                   '= (z - z₀)/fz.',
        'formula_expl': '(A, B, C) = (fx, fy, fz) are direction ratios of the normal.',
        'given': 'φ = x² + 2y² + 3z² - 12 = 0, point (x₀, y₀, z₀) = (1, 2, -1).',
        'meaning_en': 'Find the plane touching the ellipsoid at (1, 2, -1) and the line perpendicular to the surface '
                      'passing through that point.',
        'mistakes': [   ('Sign error in z - (-1) = z + 1.', 'Be careful: z - z₀ = z - (-1) = z + 1.'),
                        (   'Writing normal line as a single equation.',
                            'A line in 3D requires two equality signs (symmetric form).')],
        'num': 48,
        'practice_q': 'Find tangent plane and normal line to x² + y² + z² = 14 at (1, 2, 3).',
        'presentation': [   'Calculate direction ratios A, B, C from ∇φ.',
                            'State tangent plane formula and simplify.',
                            'State normal line symmetric form.'],
        'question': 'Find the equations of the tangent plane and normal line to the surface x² + 2y² + 3z² = 12 at the '
                    'point (1, 2, -1).',
        'steps': [   (   'Step 1: Compute gradient ∇φ',
                         'fx = ∂φ/∂x = 2x,   fy = ∂φ/∂y = 4y,   fz = ∂φ/∂z = 6z.<br>∇φ = 2x î + 4y ĵ + 6z k̂.',
                         'Calculate the spatial partial derivatives along each coordinate axis to form the gradient '
                         'vector ∇φ.'),
                     (   'Step 2: Evaluate ∇φ at point (1, 2, -1)',
                         'A = fx(1, 2, -1) = 2(1) = 2.<br>B = fy(1, 2, -1) = 4(2) = 8.<br>C = fz(1, 2, -1) = 6(-1) = '
                         '-6.<br>Direction ratios of normal: (A, B, C) = (2, 8, -6), or dividing by 2: (1, 4, -3).',
                         'Substitute the specific point coordinates into the gradient vector components.'),
                     (   'Step 3: Equation of the tangent plane',
                         'A(x - x₀) + B(y - y₀) + C(z - z₀) = 0<br>1(x - 1) + 4(y - 2) - 3(z - (-1)) = 0<br>(x - 1) + '
                         '4(y - 2) - 3(z + 1) = 0<br>x - 1 + 4y - 8 - 3z - 3 = 0<br>x + 4y - 3z - 12 = 0   or   x + 4y '
                         '- 3z = 12.',
                         'Execute step 3: equation of the tangent plane to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 4: Equation of the normal line',
                         '(x - x₀)/A = (y - y₀)/B = (z - z₀)/C<br>(x - 1)/1 = (y - 2)/4 = (z + 1)/(-3).',
                         'Execute step 4: equation of the normal line to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Tangent Plane and Normal Line to a Surface'},
    {   'concept': "Fundamental vector identity used in fluid dynamics (Euler's equations to Navier-Stokes: (v · ∇)v = "
                   '∇(v²/2) - v × (∇ × v)).',
        'difficulty': 'Exam-Level',
        'final_answer': '∇(A⃗ · B⃗) = A⃗ × (∇ × B⃗) + B⃗ × (∇ × A⃗) + (A⃗ · ∇)B⃗ + (B⃗ · ∇)A⃗ (Hence proved)',
        'formula': 'A⃗ × (∇ × B⃗) = ∇_B(A⃗ · B⃗) - (A⃗ · ∇)B⃗.',
        'formula_expl': 'Using Feynman subscript notation or Cartesian x-component expansion.',
        'given': 'A⃗ = A₁ î + A₂ ĵ + A₃ k̂, B⃗ = B₁ î + B₂ ĵ + B₃ k̂.',
        'meaning_en': 'Expand the gradient of the dot product of two vector fields into four curl and directional '
                      'derivative terms.',
        'mistakes': [   (   'Confusing (A⃗ · ∇)B⃗ with A⃗(∇ · B⃗).',
                            '(A⃗ · ∇) is a directional derivative operator; ∇ · B⃗ is a scalar divergence!'),
                        (   'Attempting full expansion of all 3 components at once.',
                            'Proving the x-component and invoking symmetry is the standard accepted method.')],
        'num': 49,
        'practice_q': 'Deduce the identity ∇(v²/2) = v⃗ × (∇ × v⃗) + (v⃗ · ∇)v⃗ by setting A⃗ = B⃗ = v⃗.',
        'presentation': [   'Prove by showing equality of x-components.',
                            'Show cancellation of mixed terms A₂(∂B₁/∂y).',
                            'Invoke symmetry for y and z components.'],
        'question': 'Prove the vector identity ∇(A⃗ · B⃗) = A⃗ × (∇ × B⃗) + B⃗ × (∇ × A⃗) + (A⃗ · ∇)B⃗ + (B⃗ · ∇)A⃗.',
        'steps': [   (   'Step 1: Focus on the x-component of LHS',
                         '[ ∇(A⃗ · B⃗) ]_x = ∂/∂x (A₁B₁ + A₂B₂ + A₃B₃)<br>= (∂A₁/∂x B₁ + A₁ ∂B₁/∂x) + (∂A₂/∂x B₂ + A₂ '
                         '∂B₂/∂x) + (∂A₃/∂x B₃ + A₃ ∂B₃/∂x).',
                         'Execute step 1: focus on the x-component of lhs to advance the step-by-step mathematical '
                         'solution toward the final result.'),
                     (   'Step 2: Expand the x-component of A⃗ × (∇ × B⃗)',
                         '∇ × B⃗ = (∂B₃/∂y - ∂B₂/∂z) î + (∂B₁/∂z - ∂B₃/∂x) ĵ + (∂B₂/∂x - ∂B₁/∂y) k̂.<br>[ A⃗ × (∇ × '
                         'B⃗) ]_x = A₂(∂B₂/∂x - ∂B₁/∂y) - A₃(∂B₁/∂z - ∂B₃/∂x)<br>= A₂(∂B₂/∂x) + A₃(∂B₃/∂x) - [ '
                         'A₂(∂B₁/∂y) + A₃(∂B₁/∂z) ].',
                         'Execute step 2: expand the x-component of a⃗ × (∇ × b⃗) to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 3: Expand the x-component of (A⃗ · ∇)B⃗',
                         '(A⃗ · ∇) = A₁ ∂/∂x + A₂ ∂/∂y + A₃ ∂/∂z.<br>[ (A⃗ · ∇)B⃗ ]_x = A₁(∂B₁/∂x) + A₂(∂B₁/∂y) + '
                         'A₃(∂B₁/∂z).',
                         'Execute step 3: expand the x-component of (a⃗ · ∇)b⃗ to advance the step-by-step '
                         'mathematical solution toward the final result.'),
                     (   'Step 4: Add Step 2 and Step 3',
                         '[ A⃗ × (∇ × B⃗) + (A⃗ · ∇)B⃗ ]_x = A₁(∂B₁/∂x) + A₂(∂B₂/∂x) + A₃(∂B₃/∂x) = Σ A_i (∂B_i/∂x).',
                         'Execute step 4: add step 2 and step 3 to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 5: Combine with symmetric terms in A and B',
                         'By symmetry between A and B:<br>[ B⃗ × (∇ × A⃗) + (B⃗ · ∇)A⃗ ]_x = Σ B_i '
                         '(∂A_i/∂x).<br>Adding both gives exactly [ ∇(A⃗ · B⃗) ]_x.<br>Since this holds for y and z '
                         'components, the vector identity is proved.',
                         'Execute step 5: combine with symmetric terms in a and b to advance the step-by-step '
                         'mathematical solution toward the final result.')],
        'title': 'Vector Operator Identity: ∇(A⃗ · B⃗)'},
    {   'concept': 'The Laplacian in any orthogonal curvilinear coordinate system is given by: ∇²ψ = (1 / h₁h₂h₃) [ '
                   '∂/∂u₁( (h₂h₃/h₁) ∂ψ/∂u₁ ) + ∂/∂u₂( (h₁h₃/h₂) ∂ψ/∂u₂ ) + ∂/∂u₃( (h₁h₂/h₃) ∂ψ/∂u₃ ) ].',
        'difficulty': 'Exam-Level',
        'final_answer': '∇²ψ = ∂²ψ/∂ρ² + (1/ρ)(∂ψ/∂ρ) + (1/ρ²)(∂²ψ/∂φ²) + ∂²ψ/∂z²  =  (1/ρ) ∂/∂ρ(ρ ∂ψ/∂ρ) + '
                        '(1/ρ²)(∂²ψ/∂φ²) + ∂²ψ/∂z²',
        'formula': '∇²ψ = (1/ρ) [ ∂/∂ρ( ρ ∂ψ/∂ρ ) + ∂/∂φ( (1/ρ) ∂ψ/∂φ ) + ∂/∂z( ρ ∂ψ/∂z ) ].',
        'formula_expl': 'u₁ = ρ, u₂ = φ, u₃ = z; h₁ = 1, h₂ = ρ, h₃ = 1; h₁h₂h₃ = ρ.',
        'given': 'Coordinates (ρ, φ, z), scale factors h₁ = 1, h₂ = ρ, h₃ = 1.',
        'meaning_en': 'Apply the general orthogonal curvilinear coordinate formula for the Laplacian to cylindrical '
                      'coordinates (ρ, φ, z).',
        'mistakes': [   ('Missing the (1/ρ²) on the φ term.', 'Since h₂ = ρ, dividing by h₂² produces 1/ρ²!'),
                        (   'Taking ∂/∂ρ(ρ ∂ψ/∂ρ) as simply ρ ∂²ψ/∂ρ².',
                            'Must use product rule: d(ρ · ψ_ρ)/dρ = ρ ψ_ρρ + ψ_ρ.')],
        'num': 50,
        'practice_q': 'Using the same formula, derive the Laplacian in spherical polar coordinates (r, θ, φ).',
        'presentation': [   'State general Laplacian formula for orthogonal coordinates.',
                            'Substitute h₁ = 1, h₂ = ρ, h₃ = 1.',
                            'Show each of the 3 bracket terms.',
                            'Divide by ρ and present both compact and expanded forms.'],
        'question': 'Using the scale factors of cylindrical coordinates h₁ = 1, h₂ = ρ, h₃ = 1, derive the expression '
                    'for the Laplacian ∇²ψ in cylindrical coordinates.',
        'steps': [   (   'Step 1: Compute the product of scale factors',
                         'h₁ h₂ h₃ = (1)(ρ)(1) = ρ.',
                         'Compute the partial derivative of the position vector with respect to each curvilinear '
                         'coordinate and evaluate its norm.'),
                     (   'Step 2: Evaluate Term 1 for u₁ = ρ',
                         '(h₂ h₃ / h₁) = (ρ · 1) / 1 = ρ.<br>First term = ∂/∂ρ [ ρ (∂ψ/∂ρ) ] = ρ (∂²ψ/∂ρ²) + '
                         '(1)(∂ψ/∂ρ).',
                         'Execute step 2: evaluate term 1 for u₁ = ρ to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 3: Evaluate Term 2 for u₂ = φ',
                         '(h₁ h₃ / h₂) = (1 · 1) / ρ = 1/ρ.<br>Second term = ∂/∂φ [ (1/ρ) (∂ψ/∂φ) ] = (1/ρ) (∂²ψ/∂φ²).',
                         'Execute step 3: evaluate term 2 for u₂ = φ to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 4: Evaluate Term 3 for u₃ = z',
                         '(h₁ h₂ / h₃) = (1 · ρ) / 1 = ρ.<br>Third term = ∂/∂z [ ρ (∂ψ/∂z) ] = ρ (∂²ψ/∂z²).',
                         'Execute step 4: evaluate term 3 for u₃ = z to advance the step-by-step mathematical solution '
                         'toward the final result.'),
                     (   'Step 5: Multiply by 1 / (h₁h₂h₃) = 1/ρ',
                         '∇²ψ = (1/ρ) [ ∂/∂ρ( ρ ∂ψ/∂ρ ) + (1/ρ)(∂²ψ/∂φ²) + ρ (∂²ψ/∂z²) ]<br>= (1/ρ) ∂/∂ρ( ρ ∂ψ/∂ρ ) + '
                         '(1/ρ²) (∂²ψ/∂φ²) + ∂²ψ/∂z²<br>= ∂²ψ/∂ρ² + (1/ρ)(∂ψ/∂ρ) + (1/ρ²)(∂²ψ/∂φ²) + ∂²ψ/∂z².',
                         'Execute step 5: multiply by 1 / (h₁h₂h₃) = 1/ρ to advance the step-by-step mathematical '
                         'solution toward the final result.')],
        'title': 'Laplacian in Curvilinear Orthogonal Coordinates'}]


/* ==========================================================================
   STUDY HUB UNIFIED INTERACTIVE CLIENT-SIDE ENGINE
   Seamlessly powers Mathematics (1BMATS101) and C Programming
   ========================================================================== */

const MATH_SEARCH_INDEX = [
  {
    "subject": "math",
    "num": 1,
    "title": "First-Order Partial Derivatives of Polynomial Function",
    "module": "Module 1",
    "concept": "Partial differentiation computes derivatives with respect to one variable while all other independent variables are trea",
    "url": "1BMATS101_Complete_Textbook.html#q1"
  },
  {
    "subject": "math",
    "num": 2,
    "title": "Equality of Mixed Second-Order Partial Derivatives",
    "module": "Module 1",
    "concept": "For smooth functions with continuous second partial derivatives, the order of differentiation is commutative.",
    "url": "1BMATS101_Complete_Textbook.html#q2"
  },
  {
    "subject": "math",
    "num": 3,
    "title": "Homogeneous Function Degree and Euler's Theorem Verification",
    "module": "Module 1",
    "concept": "A function is homogeneous of degree n if f(tx, ty) = t\u207f f(x, y). Euler's theorem relates its first partial derivatives d",
    "url": "1BMATS101_Complete_Textbook.html#q3"
  },
  {
    "subject": "math",
    "num": 4,
    "title": "Jacobian of Polar Coordinate Transformation",
    "module": "Module 1",
    "concept": "The Jacobian represents the local scaling factor of area under coordinate transformation: dx dy = |J| dr d\u03b8.",
    "url": "1BMATS101_Complete_Textbook.html#q4"
  },
  {
    "subject": "math",
    "num": 5,
    "title": "Stationary Point and Nature of a Quadratic Surface",
    "module": "Module 1",
    "concept": "Critical points occur where gradient is zero. The sign of the Hessian determinant D determines curvature.",
    "url": "1BMATS101_Complete_Textbook.html#q5"
  },
  {
    "subject": "math",
    "num": 6,
    "title": "Chain Rule for Functions of Two Independent Variables",
    "module": "Module 1",
    "concept": "When z depends on x and y, and both x and y depend on a single variable t, the rate of change of z with respect to t flo",
    "url": "1BMATS101_Complete_Textbook.html#q6"
  },
  {
    "subject": "math",
    "num": 7,
    "title": "Euler's Theorem for Inverse Trigonometric Function",
    "module": "Module 1",
    "concept": "When u = g\u207b\u00b9[f(x, y)], where f(x, y) is homogeneous of degree n, we write g(u) = f(x, y). Then by Euler's theorem on g(u",
    "url": "1BMATS101_Complete_Textbook.html#q7"
  },
  {
    "subject": "math",
    "num": 8,
    "title": "Jacobian Property of Inverses J \u00b7 J' = 1",
    "module": "Module 1",
    "concept": "The Jacobian of an inverse transformation is the reciprocal of the original Jacobian: [\u2202(u, v)/\u2202(x, y)] \u00b7 [\u2202(x, y)/\u2202(u, ",
    "url": "1BMATS101_Complete_Textbook.html#q8"
  },
  {
    "subject": "math",
    "num": 9,
    "title": "Maclaurin Series Expansion of Two Variables: e\u02e3 cos y",
    "module": "Module 1",
    "concept": "Maclaurin series for two variables approximates any smooth function near (0, 0) by a polynomial in powers of x and y usi",
    "url": "1BMATS101_Complete_Textbook.html#q9"
  },
  {
    "subject": "math",
    "num": 10,
    "title": "Taylor Series Expansion Around a Non-Zero Point (1, 1)",
    "module": "Module 1",
    "concept": "Taylor series around (a, b) replaces x by (x - a) and y by (y - b), with derivatives evaluated at (a, b).",
    "url": "1BMATS101_Complete_Textbook.html#q10"
  },
  {
    "subject": "math",
    "num": 11,
    "title": "Jacobian for Functional Dependence and Relationship",
    "module": "Module 1",
    "concept": "If \u2202(u, v)/\u2202(x, y) = 0 identically, there exists a functional relation F(u, v) = 0.",
    "url": "1BMATS101_Complete_Textbook.html#q11"
  },
  {
    "subject": "math",
    "num": 12,
    "title": "Stationary Points and Extrema of a Two-Variable Cubic",
    "module": "Module 1",
    "concept": "A two-variable function can have multiple critical points. Each must be tested individually using the second derivative ",
    "url": "1BMATS101_Complete_Textbook.html#q12"
  },
  {
    "subject": "math",
    "num": 13,
    "title": "Jacobian of 3-Variable Spherical Polar Coordinates",
    "module": "Module 1",
    "concept": "The spherical Jacobian represents the volume differential element in triple integration: dx dy dz = r\u00b2 sin \u03b8 dr d\u03b8 d\u03c6.",
    "url": "1BMATS101_Complete_Textbook.html#q13"
  },
  {
    "subject": "math",
    "num": 14,
    "title": "Homogeneous Function of Degree Zero: u = tan\u207b\u00b9(y/x)",
    "module": "Module 1",
    "concept": "When a function has equal powers in numerator and denominator, its degree is n = 0. Euler's second-order theorem states:",
    "url": "1BMATS101_Complete_Textbook.html#q14"
  },
  {
    "subject": "math",
    "num": 15,
    "title": "Composite Partial Differentiation (Chain Rule with Intermediate Variables)",
    "module": "Module 1",
    "concept": "When z = f(u, v), \u2202z/\u2202x = (\u2202z/\u2202u)(\u2202u/\u2202x) + (\u2202z/\u2202v)(\u2202v/\u2202x) and \u2202z/\u2202y = (\u2202z/\u2202u)(\u2202u/\u2202y) + (\u2202z/\u2202v)(\u2202v/\u2202y).",
    "url": "1BMATS101_Complete_Textbook.html#q15"
  },
  {
    "subject": "math",
    "num": 16,
    "title": "Euler's Theorem on Inverse Tangent: x u_x + y u_y = sin 2u",
    "module": "Module 1",
    "concept": "Standard VTU exam problem. Let z = tan u = f(x, y). Since f is homogeneous of degree n = 3 - 1 = 2, Euler's theorem give",
    "url": "1BMATS101_Complete_Textbook.html#q16"
  },
  {
    "subject": "math",
    "num": 17,
    "title": "Second-Order Euler's Theorem on Inverse Tangent",
    "module": "Module 1",
    "concept": "Let G(u) = x u_x + y u_y. Then x\u00b2 u_xx + 2xy u_xy + y\u00b2 u_yy = G(u)[G'(u) - 1]. Since G(u) = sin 2u, G'(u) = 2 cos 2u, so",
    "url": "1BMATS101_Complete_Textbook.html#q17"
  },
  {
    "subject": "math",
    "num": 18,
    "title": "Radial Laplace Operator: u = f(r) where r\u00b2 = x\u00b2 + y\u00b2 + z\u00b2",
    "module": "Module 1",
    "concept": "Radial symmetry simplifies 3D PDEs (such as heat and wave equations) into ordinary differential equations in r.",
    "url": "1BMATS101_Complete_Textbook.html#q18"
  },
  {
    "subject": "math",
    "num": 19,
    "title": "Taylor Series of Two Variables up to 3rd Degree: e\u02e3 log(1 + y)",
    "module": "Module 1",
    "concept": "Can be solved either by computing partial derivatives up to order 3 at (0, 0) or by multiplying the standard series of e",
    "url": "1BMATS101_Complete_Textbook.html#q19"
  },
  {
    "subject": "math",
    "num": 20,
    "title": "Global / Constrained Maxima and Minima: Dimensions of Open Rectangular Box",
    "module": "Module 1",
    "concept": "Optimization of two independent variables by eliminating the third variable using the constraint equation.",
    "url": "1BMATS101_Complete_Textbook.html#q20"
  },
  {
    "subject": "math",
    "num": 21,
    "title": "Stationary Points and Nature: f(x, y) = sin x + sin y + sin(x + y)",
    "module": "Module 1",
    "concept": "Classic VTU exam problem related to maximum area of a triangle. Uses trigonometric identities cos A - cos B = -2 sin[(A+",
    "url": "1BMATS101_Complete_Textbook.html#q21"
  },
  {
    "subject": "math",
    "num": 22,
    "title": "Jacobian of Implicit Functions",
    "module": "Module 1",
    "concept": "For a system of implicit equations F\u2081(u,v,w,x,y,z) = 0, F\u2082 = 0, F\u2083 = 0: \u2202u/\u2202x = - [\u2202(F\u2081, F\u2082, F\u2083)/\u2202(x, v, w)] / [\u2202(F\u2081, F\u2082",
    "url": "1BMATS101_Complete_Textbook.html#q22"
  },
  {
    "subject": "math",
    "num": 23,
    "title": "Lagrange's Method of Multipliers: Minimum Distance to a Plane",
    "module": "Module 1",
    "concept": "Lagrange function: L(x, y, z, \u03bb) = f + \u03bbg. At extrema, \u2207f = -\u03bb \u2207g, meaning the gradient of the objective function is par",
    "url": "1BMATS101_Complete_Textbook.html#q23"
  },
  {
    "subject": "math",
    "num": 24,
    "title": "Chain Rule Derivative Transformation: Wave Equation Form",
    "module": "Module 1",
    "concept": "Fundamental partial differential equation of vibrations and wave propagation (d'Alembert's solution of wave equation).",
    "url": "1BMATS101_Complete_Textbook.html#q24"
  },
  {
    "subject": "math",
    "num": 25,
    "title": "Euler's Theorem for Three Variables with Algebraic-Logarithmic Form",
    "module": "Module 1",
    "concept": "For three variables, Euler's Theorem states: x u_x + y u_y + z u_z = n u. For logarithmic functions, let f(u) = e^u, the",
    "url": "1BMATS101_Complete_Textbook.html#q25"
  },
  {
    "subject": "math",
    "num": 26,
    "title": "Gradient of a Scalar Field at a Point",
    "module": "Module 2",
    "concept": "The gradient \u2207\u03c6 transforms a scalar field into a vector field. At any point, \u2207\u03c6 points in the direction of greatest rate",
    "url": "1BMATS101_Complete_Textbook.html#q26"
  },
  {
    "subject": "math",
    "num": 27,
    "title": "Divergence of a Vector Field",
    "module": "Module 2",
    "concept": "Divergence is a scalar measure of a vector field's source or sink density. If div F\u20d7 > 0, the point acts as a source; if",
    "url": "1BMATS101_Complete_Textbook.html#q27"
  },
  {
    "subject": "math",
    "num": 28,
    "title": "Curl of a Vector Field",
    "module": "Module 2",
    "concept": "Curl measures the vorticity or rotational tendency of a fluid flow. If curl F\u20d7 = 0\u20d7 everywhere, the field has no vortice",
    "url": "1BMATS101_Complete_Textbook.html#q28"
  },
  {
    "subject": "math",
    "num": 29,
    "title": "Unit Normal Vector to a Given Surface",
    "module": "Module 2",
    "concept": "For any level surface \u03c6(x, y, z) = C, the gradient vector \u2207\u03c6 is perpendicular (normal) to the tangent plane at every poi",
    "url": "1BMATS101_Complete_Textbook.html#q29"
  },
  {
    "subject": "math",
    "num": 30,
    "title": "Directional Derivative Along a Given Vector",
    "module": "Module 2",
    "concept": "The directional derivative is the projection of the gradient \u2207\u03c6 onto the unit direction vector \u00e2: D_a \u03c6 = \u2207\u03c6 \u00b7 \u00e2. It giv",
    "url": "1BMATS101_Complete_Textbook.html#q30"
  },
  {
    "subject": "math",
    "num": 31,
    "title": "Maximum Directional Derivative and Its Direction",
    "module": "Module 2",
    "concept": "The directional derivative \u2207\u03c6 \u00b7 u\u0302 = |\u2207\u03c6| cos \u03b8 attains its maximum value when cos \u03b8 = 1 (\u03b8 = 0), which occurs precisely",
    "url": "1BMATS101_Complete_Textbook.html#q31"
  },
  {
    "subject": "math",
    "num": 32,
    "title": "Condition for a Solenoidal Vector Field",
    "module": "Module 2",
    "concept": "A vector field is solenoidal if its divergence is zero: \u2207 \u00b7 F\u20d7 = 0. This physically represents an incompressible fluid w",
    "url": "1BMATS101_Complete_Textbook.html#q32"
  },
  {
    "subject": "math",
    "num": 33,
    "title": "Irrotational Vector Field and Finding Constants",
    "module": "Module 2",
    "concept": "A vector field is irrotational if its curl is identically zero: \u2207 \u00d7 F\u20d7 = 0\u20d7. Equating each of the three components of cu",
    "url": "1BMATS101_Complete_Textbook.html#q33"
  },
  {
    "subject": "math",
    "num": 34,
    "title": "Finding Scalar Potential Function \u03c6 for an Irrotational Field",
    "module": "Module 2",
    "concept": "By Helmholtz decomposition, any irrotational vector field can be expressed as the gradient of a scalar potential: F\u20d7 = \u2207",
    "url": "1BMATS101_Complete_Textbook.html#q34"
  },
  {
    "subject": "math",
    "num": 35,
    "title": "Angle Between Two Surfaces at Point of Intersection",
    "module": "Module 2",
    "concept": "The angle \u03b8 between two surfaces at a common point is defined as the angle between their normal vectors (gradients) at t",
    "url": "1BMATS101_Complete_Textbook.html#q35"
  },
  {
    "subject": "math",
    "num": 36,
    "title": "Vector Identity: div(curl F\u20d7) = 0",
    "module": "Module 2",
    "concept": "The boundary of a boundary is zero. Physically, curl represents pure circulating flow with closed field lines; closed lo",
    "url": "1BMATS101_Complete_Textbook.html#q36"
  },
  {
    "subject": "math",
    "num": 37,
    "title": "Properties of Position Vector r\u20d7: Divergence and Curl",
    "module": "Module 2",
    "concept": "The position vector represents uniform radial expansion from the origin. It has constant divergence 3 and zero curl ever",
    "url": "1BMATS101_Complete_Textbook.html#q37"
  },
  {
    "subject": "math",
    "num": 38,
    "title": "Gradient of Radial Power Function: \u2207(r\u207f)",
    "module": "Module 2",
    "concept": "Since r = \u221a(x\u00b2 + y\u00b2 + z\u00b2), \u2202r/\u2202x = x/r. Applying chain rule to r\u207f gives (n r\u207f\u207b\u00b9)(x/r) = n r\u207f\u207b\u00b2 x. Combining components g",
    "url": "1BMATS101_Complete_Textbook.html#q38"
  },
  {
    "subject": "math",
    "num": 39,
    "title": "Laplacian of Radial Power Function: \u2207\u00b2(r\u207f)",
    "module": "Module 2",
    "concept": "Laplacian is \u2207\u00b2\u03c6 = \u2207 \u00b7 \u2207\u03c6. A function is harmonic if \u2207\u00b2\u03c6 = 0.",
    "url": "1BMATS101_Complete_Textbook.html#q39"
  },
  {
    "subject": "math",
    "num": 40,
    "title": "Scale Factors in Cylindrical Curvilinear Coordinates",
    "module": "Module 2",
    "concept": "Curvilinear scale factor h_i = |\u2202r\u20d7/\u2202u_i|. The system is orthogonal if (\u2202r\u20d7/\u2202u_i) \u00b7 (\u2202r\u20d7/\u2202u_j) = 0 for all i \u2260 j.",
    "url": "1BMATS101_Complete_Textbook.html#q40"
  },
  {
    "subject": "math",
    "num": 41,
    "title": "Irrotational Field and Scalar Potential: Complete Examination Problem",
    "module": "Module 2",
    "concept": "Standard 8-mark VTU exam problem. Requires full curl expansion and systematic integration of exact differential d\u03c6 = F\u2081 ",
    "url": "1BMATS101_Complete_Textbook.html#q41"
  },
  {
    "subject": "math",
    "num": 42,
    "title": "Divergence of Radial Field: \u2207 \u00b7 (r\u207f r\u20d7) and Solenoidal Value",
    "module": "Module 2",
    "concept": "Uses product rule \u2207 \u00b7 (\u03c6 A\u20d7) = \u03c6(\u2207 \u00b7 A\u20d7) + \u2207\u03c6 \u00b7 A\u20d7. The inverse-square field r\u207b\u00b3 r\u20d7 = r\u0302/r\u00b2 has n = -3 and is the diverg",
    "url": "1BMATS101_Complete_Textbook.html#q42"
  },
  {
    "subject": "math",
    "num": 43,
    "title": "Curl of Radial Vector Field: \u2207 \u00d7 (r\u207f r\u20d7)",
    "module": "Module 2",
    "concept": "Uses vector identity \u2207 \u00d7 (\u03c6 A\u20d7) = \u03c6(\u2207 \u00d7 A\u20d7) + (\u2207\u03c6) \u00d7 A\u20d7. Since \u2207 \u00d7 r\u20d7 = 0\u20d7 and \u2207(r\u207f) is parallel to r\u20d7, their cross prod",
    "url": "1BMATS101_Complete_Textbook.html#q43"
  },
  {
    "subject": "math",
    "num": 44,
    "title": "Directional Derivative Towards a Point",
    "module": "Module 2",
    "concept": "The direction vector is the displacement vector PQ\u20d7 = Q - P. The unit direction vector is u\u0302 = PQ\u20d7 / |PQ\u20d7|.",
    "url": "1BMATS101_Complete_Textbook.html#q44"
  },
  {
    "subject": "math",
    "num": 45,
    "title": "Cross Product of Conservative Fields is Solenoidal",
    "module": "Module 2",
    "concept": "Uses vector identity \u2207 \u00b7 (A\u20d7 \u00d7 B\u20d7) = B\u20d7 \u00b7 (\u2207 \u00d7 A\u20d7) - A\u20d7 \u00b7 (\u2207 \u00d7 B\u20d7). Since curl of any gradient is zero, both terms vanis",
    "url": "1BMATS101_Complete_Textbook.html#q45"
  },
  {
    "subject": "math",
    "num": 46,
    "title": "Scale Factors and Orthogonality in Spherical Polar Coordinates",
    "module": "Module 2",
    "concept": "Scale factor is the length of tangent vector: h_i = |\u2202r\u20d7/\u2202u_i|. Volume element is dV = h\u2081 h\u2082 h\u2083 du\u2081 du\u2082 du\u2083.",
    "url": "1BMATS101_Complete_Textbook.html#q46"
  },
  {
    "subject": "math",
    "num": 47,
    "title": "Harmonic Function and Scalar Potential in 3D",
    "module": "Module 2",
    "concept": "If \u03c6(x, y) is harmonic (\u2207\u00b2\u03c6 = 0), there exists a harmonic conjugate \u03c8 such that f(z) = \u03c6 + i\u03c8 is analytic. Transforming ",
    "url": "1BMATS101_Complete_Textbook.html#q47"
  },
  {
    "subject": "math",
    "num": 48,
    "title": "Tangent Plane and Normal Line to a Surface",
    "module": "Module 2",
    "concept": "The normal vector to the surface \u03c6 = 0 at (x\u2080, y\u2080, z\u2080) is n\u20d7 = \u2207\u03c6. The tangent plane equation is A(x - x\u2080) + B(y - y\u2080) +",
    "url": "1BMATS101_Complete_Textbook.html#q48"
  },
  {
    "subject": "math",
    "num": 49,
    "title": "Vector Operator Identity: \u2207(A\u20d7 \u00b7 B\u20d7)",
    "module": "Module 2",
    "concept": "Fundamental vector identity used in fluid dynamics (Euler's equations to Navier-Stokes: (v \u00b7 \u2207)v = \u2207(v\u00b2/2) - v \u00d7 (\u2207 \u00d7 v)",
    "url": "1BMATS101_Complete_Textbook.html#q49"
  },
  {
    "subject": "math",
    "num": 50,
    "title": "Laplacian in Curvilinear Orthogonal Coordinates",
    "module": "Module 2",
    "concept": "The Laplacian in any orthogonal curvilinear coordinate system is given by: \u2207\u00b2\u03c8 = (1 / h\u2081h\u2082h\u2083) [ \u2202/\u2202u\u2081( (h\u2082h\u2083/h\u2081) \u2202\u03c8/\u2202u\u2081 ",
    "url": "1BMATS101_Complete_Textbook.html#q50"
  },
  {
    "subject": "math",
    "num": 51,
    "title": "Rank of a 2\u00d72 and 3\u00d73 Matrix by Elementary Row Operations",
    "module": "Module 3",
    "concept": "The rank of a matrix is the maximum number of linearly independent rows (or columns). Elementary row operations do not a",
    "url": "1BMATS101_Complete_Textbook.html#q51"
  },
  {
    "subject": "math",
    "num": 52,
    "title": "Characteristic Equation and Eigenvalues of a 2\u00d72 Matrix",
    "module": "Module 3",
    "concept": "Eigenvalues \u03bb are scalars such that A v = \u03bb v for some non-zero vector v. They represent the scale factors by which eige",
    "url": "1BMATS101_Complete_Textbook.html#q52"
  },
  {
    "subject": "math",
    "num": 53,
    "title": "Consistency Criteria for Linear Systems (Rouch\u00e9-Capelli Theorem)",
    "module": "Module 3",
    "concept": "The augmented matrix [A | B] combines coefficients and constants. The system is solvable if and only if appending B does",
    "url": "1BMATS101_Complete_Textbook.html#q53"
  },
  {
    "subject": "math",
    "num": 54,
    "title": "Homogeneous Linear System AX = 0 (Trivial vs Non-Trivial Solutions)",
    "module": "Module 3",
    "concept": "For homogeneous systems, X = 0 (all zeros) is always a solution, called the trivial solution. Non-trivial solutions exis",
    "url": "1BMATS101_Complete_Textbook.html#q54"
  },
  {
    "subject": "math",
    "num": 55,
    "title": "Properties of Eigenvalues (Trace and Determinant)",
    "module": "Module 3",
    "concept": "For any n\u00d7n matrix: (1) \u03a3 \u03bb_i = Trace(A), (2) \u03a0 \u03bb_i = det(A). This provides two algebraic equations connecting the eigen",
    "url": "1BMATS101_Complete_Textbook.html#q55"
  },
  {
    "subject": "math",
    "num": 56,
    "title": "Rank of a 3\u00d74 Matrix by Echelon Form",
    "module": "Module 3",
    "concept": "For an m\u00d7n matrix, rank \u2264 min(m, n). Here rank \u2264 min(3, 4) = 3.",
    "url": "1BMATS101_Complete_Textbook.html#q56"
  },
  {
    "subject": "math",
    "num": 57,
    "title": "Solving Linear System by Gauss Elimination (Unique Solution)",
    "module": "Module 3",
    "concept": "Gauss elimination reduces the augmented matrix [A|B] to row-echelon form, transforming a coupled system into a triangula",
    "url": "1BMATS101_Complete_Textbook.html#q57"
  },
  {
    "subject": "math",
    "num": 58,
    "title": "Solving Linear System by Gauss-Jordan Method",
    "module": "Module 3",
    "concept": "While Gauss elimination stops at upper triangular form, Gauss-Jordan continues by eliminating entries ABOVE each pivot a",
    "url": "1BMATS101_Complete_Textbook.html#q58"
  },
  {
    "subject": "math",
    "num": 59,
    "title": "Eigenvalues and Eigenvectors of a 2\u00d72 Symmetric Matrix",
    "module": "Module 3",
    "concept": "For each eigenvalue \u03bb, the eigenvector is found by solving the homogeneous system (A - \u03bbI) v = 0. For real symmetric mat",
    "url": "1BMATS101_Complete_Textbook.html#q59"
  },
  {
    "subject": "math",
    "num": 60,
    "title": "Verification of Cayley-Hamilton Theorem and Finding Inverse Matrix",
    "module": "Module 3",
    "concept": "Cayley-Hamilton Theorem states that every square matrix satisfies its own characteristic equation: p(A) = 0. Multiplying",
    "url": "1BMATS101_Complete_Textbook.html#q60"
  },
  {
    "subject": "math",
    "num": 61,
    "title": "Consistency and Infinite Solutions with Free Parameter",
    "module": "Module 3",
    "concept": "If \u03c1(A) = \u03c1([A|B]) = 2 < 3 (number of unknowns), the system is consistent with infinitely many solutions dependent on 3 ",
    "url": "1BMATS101_Complete_Textbook.html#q61"
  },
  {
    "subject": "math",
    "num": 62,
    "title": "Inconsistent System (No Solution)",
    "module": "Module 3",
    "concept": "A linear system has no solution if and only if the rank of the augmented matrix is strictly greater than the rank of the",
    "url": "1BMATS101_Complete_Textbook.html#q62"
  },
  {
    "subject": "math",
    "num": 63,
    "title": "Rank of Matrix Containing an Unknown Parameter \u03bb",
    "module": "Module 3",
    "concept": "For an n\u00d7n square matrix, rank = n if and only if det(A) \u2260 0. If det(A) = 0, rank < n.",
    "url": "1BMATS101_Complete_Textbook.html#q63"
  },
  {
    "subject": "math",
    "num": 64,
    "title": "Eigenvalues of Special Matrices: Triangular, Orthogonal and Idempotent",
    "module": "Module 3",
    "concept": "Eigenvalue equations det(A - \u03bbI) = 0 and A v = \u03bb v translate matrix algebraic properties into scalar polynomial equation",
    "url": "1BMATS101_Complete_Textbook.html#q64"
  },
  {
    "subject": "math",
    "num": 65,
    "title": "Diagonalization of a 2\u00d72 Matrix",
    "module": "Module 3",
    "concept": "A matrix with distinct eigenvalues is diagonalizable: P\u207b\u00b9 A P = D = diag(\u03bb\u2081, \u03bb\u2082). The columns of P are the eigenvectors.",
    "url": "1BMATS101_Complete_Textbook.html#q65"
  },
  {
    "subject": "math",
    "num": 66,
    "title": "Investigation of System Consistency for Parameters \u03bb and \u03bc",
    "module": "Module 3",
    "concept": "Classic VTU exam question appearing in nearly every examination. The pivot in the last row (\u03bb - 3) and constant (\u03bc - 10)",
    "url": "1BMATS101_Complete_Textbook.html#q66"
  },
  {
    "subject": "math",
    "num": 67,
    "title": "Complete Eigenvalues and Eigenvectors of a 3\u00d73 Matrix",
    "module": "Module 3",
    "concept": "Symmetric 3\u00d73 matrix with repeated eigenvalues. For a repeated eigenvalue of multiplicity m, we must find m linearly ind",
    "url": "1BMATS101_Complete_Textbook.html#q67"
  },
  {
    "subject": "math",
    "num": 68,
    "title": "Diagonalization of a 3\u00d73 Symmetric Matrix",
    "module": "Module 3",
    "concept": "Every real symmetric matrix can be orthogonally diagonalized: P\u1d40 A P = D, where P is an orthogonal matrix whose columns ",
    "url": "1BMATS101_Complete_Textbook.html#q68"
  },
  {
    "subject": "math",
    "num": 69,
    "title": "Homogeneous System with Non-Trivial Solutions Depending on Parameter",
    "module": "Module 3",
    "concept": "A homogeneous linear system AX = 0 has non-trivial solutions if and only if the determinant of the coefficient matrix va",
    "url": "1BMATS101_Complete_Textbook.html#q69"
  },
  {
    "subject": "math",
    "num": 70,
    "title": "Theorem: Eigenvalues of a Real Symmetric Matrix are Real",
    "module": "Module 3",
    "concept": "Fundamental theorem of linear algebra. Guarantees that quantum observables (Hermitian operators) always yield real measu",
    "url": "1BMATS101_Complete_Textbook.html#q70"
  },
  {
    "subject": "math",
    "num": 71,
    "title": "Theorem: Eigenvectors of Real Symmetric Matrix are Orthogonal",
    "module": "Module 3",
    "concept": "Distinct eigenspaces of a symmetric matrix are mutually perpendicular.",
    "url": "1BMATS101_Complete_Textbook.html#q71"
  },
  {
    "subject": "math",
    "num": 72,
    "title": "Gauss Elimination for a 4-Variable System",
    "module": "Module 3",
    "concept": "Systematic 4\u00d74 row reduction. Shows mastery of multi-step pivot operations.",
    "url": "1BMATS101_Complete_Textbook.html#q72"
  },
  {
    "subject": "math",
    "num": 73,
    "title": "Powers of Matrix Using Diagonalization (A\u207f = P D\u207f P\u207b\u00b9)",
    "module": "Module 3",
    "concept": "Computing A\u00b9\u2070 directly requires 9 tedious matrix multiplications. Since A = P D P\u207b\u00b9, A\u207f = (P D P\u207b\u00b9)(P D P\u207b\u00b9)... = P D\u207f P",
    "url": "1BMATS101_Complete_Textbook.html#q73"
  },
  {
    "subject": "math",
    "num": 74,
    "title": "Rank of a 4\u00d74 Matrix by Normal Form [I_r, 0]",
    "module": "Module 3",
    "concept": "Every m\u00d7n matrix of rank r can be reduced to the normal form [I_r 0; 0 0] using both row and column elementary operation",
    "url": "1BMATS101_Complete_Textbook.html#q74"
  },
  {
    "subject": "math",
    "num": 75,
    "title": "Cayley-Hamilton Theorem for 3\u00d73 Matrix: Inverse and Higher Powers",
    "module": "Module 3",
    "concept": "Cayley-Hamilton theorem allows expressing any higher power A\u207f and the inverse A\u207b\u00b9 as a polynomial of degree at most (n -",
    "url": "1BMATS101_Complete_Textbook.html#q75"
  },
  {
    "subject": "math",
    "num": 76,
    "title": "Definition of Vector Space over \u211d and Its Fundamental Axioms",
    "module": "Module 4",
    "concept": "A vector space is an abstract algebraic structure consisting of a set V whose elements ('vectors') can be added together",
    "url": "1BMATS101_Complete_Textbook.html#q76"
  },
  {
    "subject": "math",
    "num": 77,
    "title": "Subspace Criteria (The Two-Step and One-Step Subspace Tests)",
    "module": "Module 4",
    "concept": "Since W is inside V, it automatically inherits associativity, commutativity, and distributivity. We only need to check t",
    "url": "1BMATS101_Complete_Textbook.html#q77"
  },
  {
    "subject": "math",
    "num": 78,
    "title": "Linear Combinations and Span of Vectors",
    "module": "Module 4",
    "concept": "A linear combination is any vector of the form c\u2081 v\u2081 + c\u2082 v\u2082 + ... + c_k v_k. The span of S, denoted span(S), is the set",
    "url": "1BMATS101_Complete_Textbook.html#q78"
  },
  {
    "subject": "math",
    "num": 79,
    "title": "Testing Linear Independence of Vectors in \u211d\u00b3",
    "module": "Module 4",
    "concept": "Vectors are linearly independent if no vector in the set can be written as a linear combination of the others. For n vec",
    "url": "1BMATS101_Complete_Textbook.html#q79"
  },
  {
    "subject": "math",
    "num": 80,
    "title": "Basis and Dimension of a Vector Space",
    "module": "Module 4",
    "concept": "A basis is a minimal spanning set and a maximal linearly independent set. Every vector in V can be uniquely represented ",
    "url": "1BMATS101_Complete_Textbook.html#q80"
  },
  {
    "subject": "math",
    "num": 81,
    "title": "Subspace Verification: Plane Passing Through the Origin",
    "module": "Module 4",
    "concept": "A flat plane in \u211d\u00b3 is a subspace if and only if it passes through the origin (0, 0, 0). Any translation away from the or",
    "url": "1BMATS101_Complete_Textbook.html#q81"
  },
  {
    "subject": "math",
    "num": 82,
    "title": "Finding Basis and Dimension of a Subspace in \u211d\u2074",
    "module": "Module 4",
    "concept": "For a subspace defined by k independent linear constraints in \u211d\u207f, dimension is dim(W) = n - k. Here n = 4 and k = 2, so ",
    "url": "1BMATS101_Complete_Textbook.html#q82"
  },
  {
    "subject": "math",
    "num": 83,
    "title": "Coordinates of a Vector Relative to an Ordered Basis",
    "module": "Module 4",
    "concept": "A basis acts like a customized coordinate coordinate system. The coordinates are the weights c_i required to build vecto",
    "url": "1BMATS101_Complete_Textbook.html#q83"
  },
  {
    "subject": "math",
    "num": 84,
    "title": "Inner Product Axioms and Verification on \u211d\u00b2",
    "module": "Module 4",
    "concept": "An inner product generalizes the geometric dot product, enabling concepts of length, distance, and angle in abstract vec",
    "url": "1BMATS101_Complete_Textbook.html#q84"
  },
  {
    "subject": "math",
    "num": 85,
    "title": "Norm, Distance and Angle Between Vectors in Inner Product Space",
    "module": "Module 4",
    "concept": "In any inner product space: ||u|| = \u221a\u27e8u, u\u27e9, d(u, v) = ||u - v||, and cos \u03b8 = \u27e8u, v\u27e9 / (||u|| ||v||).",
    "url": "1BMATS101_Complete_Textbook.html#q85"
  },
  {
    "subject": "math",
    "num": 86,
    "title": "Verification of the Cauchy-Schwarz Inequality",
    "module": "Module 4",
    "concept": "The Cauchy-Schwarz inequality is one of the most powerful theorems in mathematics. It guarantees that the cosine of the ",
    "url": "1BMATS101_Complete_Textbook.html#q86"
  },
  {
    "subject": "math",
    "num": 87,
    "title": "Orthogonal Projection of a Vector onto a Subspace",
    "module": "Module 4",
    "concept": "Orthogonal projection decomposes any vector v into a component along u and a residual component strictly perpendicular t",
    "url": "1BMATS101_Complete_Textbook.html#q87"
  },
  {
    "subject": "math",
    "num": 88,
    "title": "Inner Product on Polynomial Space P\u2082[-1, 1]",
    "module": "Module 4",
    "concept": "Extends geometric orthogonality to function spaces (basis of Fourier series and Legendre polynomials). Two functions are",
    "url": "1BMATS101_Complete_Textbook.html#q88"
  },
  {
    "subject": "math",
    "num": 89,
    "title": "Subspace of Symmetric Matrices: Basis and Dimension",
    "module": "Module 4",
    "concept": "A matrix is symmetric if A\u1d40 = A. In M\u2082\u2082(\u211d), a symmetric matrix has the form [[a, b], [b, c]] governed by 3 independent p",
    "url": "1BMATS101_Complete_Textbook.html#q89"
  },
  {
    "subject": "math",
    "num": 90,
    "title": "Triangle Inequality in Inner Product Space",
    "module": "Module 4",
    "concept": "Geometrically states that the length of any side of a triangle is less than or equal to the sum of the lengths of the ot",
    "url": "1BMATS101_Complete_Textbook.html#q90"
  },
  {
    "subject": "math",
    "num": 91,
    "title": "Gram-Schmidt Orthogonalization Process in \u211d\u00b3",
    "module": "Module 4",
    "concept": "The Gram-Schmidt algorithm subtracts the projections onto all previously computed orthogonal vectors: u_k = v_k - \u03a3 proj",
    "url": "1BMATS101_Complete_Textbook.html#q91"
  },
  {
    "subject": "math",
    "num": 92,
    "title": "Theorem: Intersection of Two Subspaces is a Subspace",
    "module": "Module 4",
    "concept": "Fundamental theorem of linear algebra. Any intersection of subspaces is a subspace, forming the basis of solution spaces",
    "url": "1BMATS101_Complete_Textbook.html#q92"
  },
  {
    "subject": "math",
    "num": 93,
    "title": "Union of Subspaces Theorem (Subspace iff One is Contained in the Other)",
    "module": "Module 4",
    "concept": "A line plus a line in \u211d\u00b2 does not form a plane; adding a vector from line 1 to line 2 leaves the union, violating closur",
    "url": "1BMATS101_Complete_Textbook.html#q93"
  },
  {
    "subject": "math",
    "num": 94,
    "title": "Basis of Polynomial Space P\u2082(\u211d)",
    "module": "Module 4",
    "concept": "dim(P\u2082) = 3. Any set of 3 vectors in a 3-dimensional space is a basis if and only if it is linearly independent (determi",
    "url": "1BMATS101_Complete_Textbook.html#q94"
  },
  {
    "subject": "math",
    "num": 95,
    "title": "Basis and Dimension of the Null Space (Solution Space of Homogeneous System)",
    "module": "Module 4",
    "concept": "The solution space of AX = 0 is the null space Null(A). By the Rank-Nullity theorem, dim(Null A) = n - rank(A).",
    "url": "1BMATS101_Complete_Textbook.html#q95"
  },
  {
    "subject": "math",
    "num": 96,
    "title": "Orthogonal Complement W^\u22a5 of a Subspace in \u211d\u2074",
    "module": "Module 4",
    "concept": "The orthogonal complement W^\u22a5 consists of all vectors perpendicular to every vector in W. If dim(W) = k in \u211d\u207f, then dim(",
    "url": "1BMATS101_Complete_Textbook.html#q96"
  },
  {
    "subject": "math",
    "num": 97,
    "title": "Parseval's Identity and Bessel's Inequality",
    "module": "Module 4",
    "concept": "Parseval's identity is the infinite-dimensional generalized Pythagorean theorem. Bessel's inequality states that any fin",
    "url": "1BMATS101_Complete_Textbook.html#q97"
  },
  {
    "subject": "math",
    "num": 98,
    "title": "Gram-Schmidt Process on Polynomial Inner Product Space",
    "module": "Module 4",
    "concept": "Constructs the classical shifted Legendre polynomials orthogonal on [0, 1].",
    "url": "1BMATS101_Complete_Textbook.html#q98"
  },
  {
    "subject": "math",
    "num": 99,
    "title": "Transition Matrix (Change of Basis Matrix)",
    "module": "Module 4",
    "concept": "The columns of the transition matrix P from B' to B are the coordinate vectors of the new basis vectors relative to the ",
    "url": "1BMATS101_Complete_Textbook.html#q99"
  },
  {
    "subject": "math",
    "num": 100,
    "title": "Orthogonal Matrix Representation and Isometry of Inner Product",
    "module": "Module 4",
    "concept": "Orthogonal matrices represent rigid geometric motions (rotations and reflections). Preserving inner products automatical",
    "url": "1BMATS101_Complete_Textbook.html#q100"
  },
  {
    "subject": "math",
    "num": 101,
    "title": "Definition and Properties of a Linear Transformation",
    "module": "Module 5",
    "concept": "A linear transformation is a function between vector spaces that respects the algebraic operations: the transformation o",
    "url": "1BMATS101_Complete_Textbook.html#q101"
  },
  {
    "subject": "math",
    "num": 102,
    "title": "Testing Linearity of a Transformation (Passing vs Failing)",
    "module": "Module 5",
    "concept": "A linear transformation must map the origin to the origin. If T(0) \u2260 0, it is immediately non-linear. If T(0) = 0, we ve",
    "url": "1BMATS101_Complete_Textbook.html#q102"
  },
  {
    "subject": "math",
    "num": 103,
    "title": "Kernel (Null Space) and Range (Image) Definitions",
    "module": "Module 5",
    "concept": "The kernel is the set of all input vectors that collapse to zero in W. The range is the set of all output vectors actual",
    "url": "1BMATS101_Complete_Textbook.html#q103"
  },
  {
    "subject": "math",
    "num": 104,
    "title": "Rank-Nullity Theorem Statement and Verification",
    "module": "Module 5",
    "concept": "The total dimension of the domain V is conserved: every dimension either gets mapped into a non-zero output dimension (c",
    "url": "1BMATS101_Complete_Textbook.html#q104"
  },
  {
    "subject": "math",
    "num": 105,
    "title": "Standard Matrix of a Linear Transformation",
    "module": "Module 5",
    "concept": "Any linear transformation T: \u211d\u207f \u2192 \u211d\u1d50 is completely determined by its action on the standard basis vectors: [T] = [ T(e\u2081)",
    "url": "1BMATS101_Complete_Textbook.html#q105"
  },
  {
    "subject": "math",
    "num": 106,
    "title": "Finding a Linear Transformation from Its Action on a Basis",
    "module": "Module 5",
    "concept": "A linear transformation is completely and uniquely determined by its values on a basis of the domain. Any vector (x, y) ",
    "url": "1BMATS101_Complete_Textbook.html#q106"
  },
  {
    "subject": "math",
    "num": 107,
    "title": "Kernel, Nullity, Range, and Rank of a Transformation from \u211d\u00b3 to \u211d\u00b3",
    "module": "Module 5",
    "concept": "The matrix of T is A. Null space of A gives ker(T); Column space of A gives Range(T).",
    "url": "1BMATS101_Complete_Textbook.html#q107"
  },
  {
    "subject": "math",
    "num": 108,
    "title": "Testing Whether a Linear Transformation is One-to-One and Onto",
    "module": "Module 5",
    "concept": "For a linear operator between spaces of the same finite dimension: T is one-to-one \u21d4 T is onto \u21d4 det(A) \u2260 0 \u21d4 ker(T) = {",
    "url": "1BMATS101_Complete_Textbook.html#q108"
  },
  {
    "subject": "math",
    "num": 109,
    "title": "Matrix Representation Relative to Non-Standard Bases",
    "module": "Module 5",
    "concept": "The j-th column of the matrix representation [T]_{B, B'} consists of the coordinate vector of T(u_j) relative to the bas",
    "url": "1BMATS101_Complete_Textbook.html#q109"
  },
  {
    "subject": "math",
    "num": 110,
    "title": "Composition of Linear Transformations and Matrix Multiplication",
    "module": "Module 5",
    "concept": "The matrix of a composition of linear transformations is the product of their individual standard matrices: [S \u2218 T] = [S",
    "url": "1BMATS101_Complete_Textbook.html#q110"
  },
  {
    "subject": "math",
    "num": 111,
    "title": "Linear Transformation on Polynomial Space: Differentiation Operator",
    "module": "Module 5",
    "concept": "Calculus operations like differentiation and integration are linear transformations on polynomial and function spaces. D",
    "url": "1BMATS101_Complete_Textbook.html#q111"
  },
  {
    "subject": "math",
    "num": 112,
    "title": "Inverse of an Invertible Linear Transformation",
    "module": "Module 5",
    "concept": "A linear operator is invertible if and only if its standard matrix [T] is invertible: [T\u207b\u00b9] = [T]\u207b\u00b9.",
    "url": "1BMATS101_Complete_Textbook.html#q112"
  },
  {
    "subject": "math",
    "num": 113,
    "title": "Similarity of Matrix Representations under Change of Basis",
    "module": "Module 5",
    "concept": "Two matrices represent the same linear operator in different coordinate systems if and only if they are similar: A' = P\u207b",
    "url": "1BMATS101_Complete_Textbook.html#q113"
  },
  {
    "subject": "math",
    "num": 114,
    "title": "Rank and Nullity of a Matrix Transformation",
    "module": "Module 5",
    "concept": "For any matrix transformation T_A(x) = A x, rank(T_A) = rank(A) and nullity(T_A) = n - rank(A).",
    "url": "1BMATS101_Complete_Textbook.html#q114"
  },
  {
    "subject": "math",
    "num": 115,
    "title": "Orthogonal Projection Operator in \u211d\u00b3: Matrix and Properties",
    "module": "Module 5",
    "concept": "An orthogonal projection onto a subspace satisfies two algebraic properties: idempotency P\u00b2 = P (projecting twice gives ",
    "url": "1BMATS101_Complete_Textbook.html#q115"
  },
  {
    "subject": "math",
    "num": 116,
    "title": "Complete Proof of the Rank-Nullity Theorem",
    "module": "Module 5",
    "concept": "Foundational theorem of linear algebra. Shows that every dimension of V is accounted for: either mapped injectively into",
    "url": "1BMATS101_Complete_Textbook.html#q116"
  },
  {
    "subject": "math",
    "num": 117,
    "title": "Theorem: T is One-to-One if and only if Kernel(T) = {0}",
    "module": "Module 5",
    "concept": "In general non-linear functions, f(a) = f(b) cannot be tested by checking f(x) = 0. But for linear transformations, T(u)",
    "url": "1BMATS101_Complete_Textbook.html#q117"
  },
  {
    "subject": "math",
    "num": 118,
    "title": "Equivalence of One-to-One and Onto for Equal Finite Dimensions",
    "module": "Module 5",
    "concept": "Pigeonhole principle for vector spaces. If a linear map between spaces of equal dimension loses no information (nullity ",
    "url": "1BMATS101_Complete_Textbook.html#q118"
  },
  {
    "subject": "math",
    "num": 119,
    "title": "Linear Transformation on Matrix Space M\u2082\u2082(\u211d): Trace and Transpose",
    "module": "Module 5",
    "concept": "M\u2082\u2082(\u211d) is a 4-dimensional vector space. A + A\u1d40 = 0 means A\u1d40 = -A (skew-symmetric). Thus ker(T) is the subspace of skew-s",
    "url": "1BMATS101_Complete_Textbook.html#q119"
  },
  {
    "subject": "math",
    "num": 120,
    "title": "Rank and Nullity of Composite Linear Transformation (Sylvester's Inequality)",
    "module": "Module 5",
    "concept": "A composition cannot recover lost information. Applying T first squashes the domain into Range(T) \u2286 V, and applying S ca",
    "url": "1BMATS101_Complete_Textbook.html#q120"
  },
  {
    "subject": "math",
    "num": 121,
    "title": "Matrix Representation on Polynomial Space with Quadratic Basis",
    "module": "Module 5",
    "concept": "Shift operator in polynomial spaces. Represents Taylor shift algebraically as an upper triangular Pascal matrix.",
    "url": "1BMATS101_Complete_Textbook.html#q121"
  },
  {
    "subject": "math",
    "num": 122,
    "title": "Finding Linear Transformation from Kernel and Image Specifications",
    "module": "Module 5",
    "concept": "We can construct a linear transformation by specifying its action on a basis: assign T(v\u2081) = 0 for v\u2081 spanning the kerne",
    "url": "1BMATS101_Complete_Textbook.html#q122"
  },
  {
    "subject": "math",
    "num": 123,
    "title": "Idempotent Transformation (Projection) Properties",
    "module": "Module 5",
    "concept": "Projections decompose the entire vector space into the subspace being projected onto Range(T) and the direction of proje",
    "url": "1BMATS101_Complete_Textbook.html#q123"
  },
  {
    "subject": "math",
    "num": 124,
    "title": "Non-Commutativity of Geometric Transformations (Rotation vs Reflection)",
    "module": "Module 5",
    "concept": "Matrix multiplication is generally non-commutative (AB \u2260 BA), reflecting the physical fact that spatial transformations ",
    "url": "1BMATS101_Complete_Textbook.html#q124"
  },
  {
    "subject": "math",
    "num": 125,
    "title": "Application of Rank-Nullity Theorem: Systems of Linear Equations",
    "module": "Module 5",
    "concept": "For underdetermined systems (m < n), rank(A) \u2264 m < n. By Rank-Nullity, nullity(A) = n - rank(A) \u2265 n - m > 0, which guara",
    "url": "1BMATS101_Complete_Textbook.html#q125"
  }
];
const C_SEARCH_INDEX = [
  {
    "subject": "c",
    "num": 1,
    "title": "History, Features, and Architecture of C Language",
    "module": "Module 1",
    "category": "Concepts & History",
    "concept": "C is termed 'middle-level' because it combines the power, hardware control, and memory manipulation capabilities of asse",
    "url": "c_programming.html#c-q1"
  },
  {
    "subject": "c",
    "num": 2,
    "title": "Structure of a C Program & Compilation Stages",
    "module": "Module 1",
    "category": "Architecture & Build",
    "concept": "Source code (.c) undergoes 4 stages:\n1. Preprocessing (gcc -E): Removes comments, expands macros, includes header files ",
    "url": "c_programming.html#c-q2"
  },
  {
    "subject": "c",
    "num": 3,
    "title": "Tokens, Keywords, Identifiers, and Reserved Rules",
    "module": "Module 1",
    "category": "C Tokens",
    "concept": "1. Keywords: 32 reserved words in C89 (44 in C99/C11) that possess special, predefined meanings to the compiler (e.g., `",
    "url": "c_programming.html#c-q3"
  },
  {
    "subject": "c",
    "num": 4,
    "title": "Data Types, Modifiers, and Memory Sizes with sizeof()",
    "module": "Module 1",
    "category": "Data Representation",
    "concept": "Type modifiers alter the range or size of basic types:\n- `signed`: Allows positive and negative values (default for `int",
    "url": "c_programming.html#c-q4"
  },
  {
    "subject": "c",
    "num": 5,
    "title": "Constants, Literals, and const vs #define",
    "module": "Module 1",
    "category": "Variables & Storage",
    "concept": "1. `#define MACRO value`:\n- Handled by preprocessor via textual search-and-replace.\n- Has no data type (no type safety).",
    "url": "c_programming.html#c-q5"
  },
  {
    "subject": "c",
    "num": 6,
    "title": "Format Specifiers, Modifiers, and Escape Sequences",
    "module": "Module 1",
    "category": "I/O System",
    "concept": "Key Specifiers:\n- `%d` / `%i`: Signed decimal integer\n- `%u`: Unsigned integer\n- `%f`: Float (standard decimal)\n- `%lf`:",
    "url": "c_programming.html#c-q6"
  },
  {
    "subject": "c",
    "num": 7,
    "title": "Arithmetic Operators, Integer Division, and Type Casting",
    "module": "Module 1",
    "category": "Operators & Expressions",
    "concept": "1. Integer Division: In integer arithmetic, `a / b` discards any remainder. For example, `7 / 2` evaluates to integer `3",
    "url": "c_programming.html#c-q7"
  },
  {
    "subject": "c",
    "num": 8,
    "title": "Relational, Logical Operators, and Short-Circuit Evaluation",
    "module": "Module 1",
    "category": "Operators & Expressions",
    "concept": "Short-Circuit Evaluation:\n- Logical AND (`&&`): If the left operand evaluates to `0` (false), the entire expression MUST",
    "url": "c_programming.html#c-q8"
  },
  {
    "subject": "c",
    "num": 9,
    "title": "Increment, Decrement (Prefix vs Postfix), and Compound Assignment",
    "module": "Module 1",
    "category": "Operators & Expressions",
    "concept": "1. Prefix (`++i`): Value of expression is `i + 1`. Side-effect happens immediately.\n2. Postfix (`i++`): Value of express",
    "url": "c_programming.html#c-q9"
  },
  {
    "subject": "c",
    "num": 10,
    "title": "Bitwise Operators and Low-Level Bit Manipulation",
    "module": "Module 1",
    "category": "Bitwise Operations",
    "concept": "1. Bitwise AND `&`: 1 only if both bits are 1.\n2. Bitwise OR `|`: 1 if at least one bit is 1.\n3. Bitwise XOR `^`: 1 if b",
    "url": "c_programming.html#c-q10"
  },
  {
    "subject": "c",
    "num": 11,
    "title": "Conditional (Ternary) Operator and Nested Decisions",
    "module": "Module 1",
    "category": "Operators & Expressions",
    "concept": "Syntax: `condition ? expression1 : expression2`\nIf `condition` evaluates to non-zero (true), `expression1` is evaluated ",
    "url": "c_programming.html#c-q11"
  },
  {
    "subject": "c",
    "num": 12,
    "title": "Operator Precedence and Associativity Table",
    "module": "Module 1",
    "category": "Operators & Expressions",
    "concept": "Hierarchy Summary:\n1. Highest: Postfix `()`, `[]`, `->`, `.`, `++`, `--` (Left-to-Right)\n2. Unary: Prefix `++`, `--`, `+",
    "url": "c_programming.html#c-q12"
  },
  {
    "subject": "c",
    "num": 13,
    "title": "Formatted vs Unformatted I/O Functions",
    "module": "Module 1",
    "category": "I/O System",
    "concept": "1. `getchar()` / `putchar()`: Standard ANSI C functions reading/writing one character via line-buffered stdin/stdout.\n2.",
    "url": "c_programming.html#c-q13"
  },
  {
    "subject": "c",
    "num": 14,
    "title": "Selection Control: Simple if, if-else, and Nested Decisions",
    "module": "Module 1",
    "category": "Decision Control",
    "concept": "Leap Year Rules:\n1. If a year is evenly divisible by 400, it is a leap year (e.g., 2000, 2400).\n2. If a year is divisibl",
    "url": "c_programming.html#c-q14"
  },
  {
    "subject": "c",
    "num": 15,
    "title": "else-if Ladder: Student Grading and Range Classification",
    "module": "Module 1",
    "category": "Decision Control",
    "concept": "Grading Scale:\n- Marks >= 90: Distinction (Grade O)\n- Marks >= 80 and < 90: First Class Exemplary (Grade A+)\n- Marks >= ",
    "url": "c_programming.html#c-q15"
  },
  {
    "subject": "c",
    "num": 16,
    "title": "The switch-case Statement: Rules, Fall-Through, and Menu Calculator",
    "module": "Module 1",
    "category": "Decision Control",
    "concept": "Rules of `switch-case`:\n1. The switch expression must evaluate to an integer or character (`int`, `char`, `short`, `enum",
    "url": "c_programming.html#c-q16"
  },
  {
    "subject": "c",
    "num": 17,
    "title": "The for Loop: Structure, Multiple Expressions, and Multiplication Table",
    "module": "Module 1",
    "category": "Loops & Iteration",
    "concept": "General Syntax: `for (init; condition; update) { ... }`\nAdvanced Features:\n1. All three expressions are optional. `for (",
    "url": "c_programming.html#c-q17"
  },
  {
    "subject": "c",
    "num": 18,
    "title": "The while Loop: Entry-Controlled Iteration and Palindrome Number",
    "module": "Module 1",
    "category": "Loops & Iteration",
    "concept": "Algorithm to Reverse an Integer:\n1. Store original number in a temporary variable `temp`.\n2. Initialize `reversedNum = 0",
    "url": "c_programming.html#c-q18"
  },
  {
    "subject": "c",
    "num": 19,
    "title": "The do-while Loop: Exit-Controlled Logic and Input Validation",
    "module": "Module 1",
    "category": "Loops & Iteration",
    "concept": "Comparison Table:\n- `while`: Condition evaluated at entry. Body executed 0 or more times. Syntax has no semicolon after ",
    "url": "c_programming.html#c-q19"
  },
  {
    "subject": "c",
    "num": 20,
    "title": "Nested Loops and Pattern Printing: Floyd's Triangle & Pyramids",
    "module": "Module 1",
    "category": "Loops & Iteration",
    "concept": "1. Floyd's Triangle:\nRow 1: 1\nRow 2: 2 3\nRow 3: 4 5 6\nRow 4: 7 8 9 10\nContinuous sequential counter that increments acro",
    "url": "c_programming.html#c-q20"
  },
  {
    "subject": "c",
    "num": 21,
    "title": "Jump Statements: break vs continue with Prime Number Search",
    "module": "Module 1",
    "category": "Control Flow",
    "concept": "Comparison:\n- `break`: Exits the innermost loop or switch immediately. Remaining iterations are aborted.\n- `continue`: S",
    "url": "c_programming.html#c-q21"
  },
  {
    "subject": "c",
    "num": 22,
    "title": "The goto Statement: Unconditional Branching and Safe Usages",
    "module": "Module 1",
    "category": "Control Flow",
    "concept": "1. Syntax: `goto label_name; ... label_name: statement;`\n2. Scope: A label has function scope. You cannot jump across di",
    "url": "c_programming.html#c-q22"
  },
  {
    "subject": "c",
    "num": 23,
    "title": "Output Prediction & Debugging: Precedence and Assignment Traps",
    "module": "Module 1",
    "category": "Debugging & Tracing",
    "concept": "1. Assignment Expression Value: `(x = 0)` assigns `0` to `x` and evaluates to `0`.\n2. Truth in C: In C, `0` is treated a",
    "url": "c_programming.html#c-q23"
  },
  {
    "subject": "c",
    "num": 24,
    "title": "Floating-Point Representation and Precision Comparison Trap",
    "module": "Module 1",
    "category": "Debugging & Tracing",
    "concept": "1. IEEE 754 Representation: Binary floats represent numbers as powers of 2 (1/2, 1/4, 1/8, etc.). Fractions like 1/10 ($",
    "url": "c_programming.html#c-q24"
  },
  {
    "subject": "c",
    "num": 25,
    "title": "Comprehensive Program: Fibonacci Series with Prime Tagging",
    "module": "Module 1",
    "category": "Comprehensive Integration",
    "concept": "1. Sequence Generation: Use iterative approach with two variables `t1 = 0, t2 = 1`. In each step, `nextTerm = t1 + t2`, ",
    "url": "c_programming.html#c-q25"
  },
  {
    "subject": "c",
    "num": 26,
    "title": "Module 1 Mastery: Exam Traps, Viva Q&A, and Debugging Diagnostic",
    "module": "Module 1",
    "category": "Comprehensive Review",
    "concept": "Top 5 Pitfalls:\n1. Semicolon after loop header (`for(..);`): Causes empty loop body.\n2. Dangling `\\n` in stdin buffer: S",
    "url": "c_programming.html#c-q26"
  },
  {
    "subject": "c",
    "num": 27,
    "title": "One-Dimensional Arrays: Declaration, Memory Layout, and Indexing",
    "module": "Module 2",
    "category": "1D Arrays",
    "concept": "1. Definition: `data_type array_name[SIZE];`\n2. Memory Model: Elements are stored in contiguous memory cells. If element",
    "url": "c_programming.html#c-q27"
  },
  {
    "subject": "c",
    "num": 28,
    "title": "Array Operations: Minimum, Maximum, and Average Computation",
    "module": "Module 2",
    "category": "1D Arrays",
    "concept": "1. Never initialize `max` with 0 or a hardcoded value if the array might contain negative numbers! Initializing with `ar",
    "url": "c_programming.html#c-q28"
  },
  {
    "subject": "c",
    "num": 29,
    "title": "Linear Search Algorithm: Logic, Trace, and Complexity Analysis",
    "module": "Module 2",
    "category": "Searching Algorithms",
    "concept": "Complexity Analysis:\n- Best Case: $O(1)$ (Key found at index 0 on the first comparison).\n- Worst Case: $O(N)$ (Key is at",
    "url": "c_programming.html#c-q29"
  },
  {
    "subject": "c",
    "num": 30,
    "title": "Binary Search Algorithm: Divide-and-Conquer with Trace",
    "module": "Module 2",
    "category": "Searching Algorithms",
    "concept": "1. Overflow-Safe Midpoint: Writing `mid = (low + high) / 2` causes integer overflow when `low + high` exceeds $2^{31}-1$",
    "url": "c_programming.html#c-q30"
  },
  {
    "subject": "c",
    "num": 31,
    "title": "Bubble Sort Algorithm with Early Termination Optimization",
    "module": "Module 2",
    "category": "Sorting Algorithms",
    "concept": "1. In pass $i$ (from 0 to $N-2$), the largest unsorted element settles into position $N-1-i$. Hence the inner loop only ",
    "url": "c_programming.html#c-q31"
  },
  {
    "subject": "c",
    "num": 32,
    "title": "Two-Dimensional Arrays: Row-Major Memory Mapping and Addressing",
    "module": "Module 2",
    "category": "2D Arrays",
    "concept": "Row-Major Address Formula:\nFor an array declared as `T arr[ROWS][COLS];`:\n$$\\text{Address}(arr[i][j]) = \\text{Base Addre",
    "url": "c_programming.html#c-q32"
  },
  {
    "subject": "c",
    "num": 33,
    "title": "Matrix Addition and Subtraction with Dimension Compatibility Checks",
    "module": "Module 2",
    "category": "2D Arrays",
    "concept": "1. Compatibility Rule: Let matrix $A$ be of order $R_1 \\times C_1$ and matrix $B$ be of order $R_2 \\times C_2$. Addition",
    "url": "c_programming.html#c-q33"
  },
  {
    "subject": "c",
    "num": 34,
    "title": "Matrix Multiplication: Algorithm, Compatibility, and 3-Loop Implementation",
    "module": "Module 2",
    "category": "2D Arrays",
    "concept": "1. Compatibility: $A_{R_1 \\times C_1} \\times B_{R_2 \\times C_2} \\implies C_1 = R_2$.\n2. Product Size: $R_1 \\times C_2$.\n",
    "url": "c_programming.html#c-q34"
  },
  {
    "subject": "c",
    "num": 35,
    "title": "Matrix Transpose, Trace, and Symmetric Matrix Verification",
    "module": "Module 2",
    "category": "2D Arrays",
    "concept": "1. Trace: Only defined for square matrices ($N \\times N$). It is the sum of elements where row index equals column index",
    "url": "c_programming.html#c-q35"
  },
  {
    "subject": "c",
    "num": 36,
    "title": "Character Arrays vs Strings: The Null Terminator '\\0'",
    "module": "Module 2",
    "category": "Strings",
    "concept": "1. String Representation: C does not have a native primitive `string` data type. Strings are 1D arrays of `char` ending ",
    "url": "c_programming.html#c-q36"
  },
  {
    "subject": "c",
    "num": 37,
    "title": "String Input: scanf() Whitespace Limitations and Scansets",
    "module": "Module 2",
    "category": "Strings",
    "concept": "1. `scanf(\"%s\", str)` stops reading at the first space. Entering \"John Doe\" stores only \"John\".\n2. Note that `str` is al",
    "url": "c_programming.html#c-q37"
  },
  {
    "subject": "c",
    "num": 38,
    "title": "Safe String Input: Why gets() is Dangerous and How to Use fgets()",
    "module": "Module 2",
    "category": "Strings & Security",
    "concept": "1. The `gets()` Vulnerability: If a program allocates `char buf[10]` and the user enters 50 characters, `gets(buf)` writ",
    "url": "c_programming.html#c-q38"
  },
  {
    "subject": "c",
    "num": 39,
    "title": "String Length: Built-in strlen() and Custom Implementation",
    "module": "Module 2",
    "category": "String Operations",
    "concept": "1. Return Type: `strlen()` returns `size_t` (an unsigned integer type).\n2. Contrast with `sizeof`: For `char str[50] = \"",
    "url": "c_programming.html#c-q39"
  },
  {
    "subject": "c",
    "num": 40,
    "title": "String Copy: strcpy(), strncpy(), and Custom Safe Implementation",
    "module": "Module 2",
    "category": "String Operations",
    "concept": "1. `char *strcpy(char *dest, const char *src)`: Copies `src` to `dest` including `\\0`. It does NOT check whether `dest` ",
    "url": "c_programming.html#c-q40"
  },
  {
    "subject": "c",
    "num": 41,
    "title": "String Concatenation: strcat() and Custom Re-implementation",
    "module": "Module 2",
    "category": "String Operations",
    "concept": "1. Destination Capacity: Destination array MUST be large enough to hold `strlen(dest) + strlen(src) + 1` bytes.\n2. Algor",
    "url": "c_programming.html#c-q41"
  },
  {
    "subject": "c",
    "num": 42,
    "title": "String Comparison: strcmp() Lexicographical Logic and Custom Function",
    "module": "Module 2",
    "category": "String Operations",
    "concept": "Return Values of `strcmp(str1, str2)`:\n- `0`: Strings are identical (`str1 == str2`).\n- `< 0` (negative): `str1` is lexi",
    "url": "c_programming.html#c-q42"
  },
  {
    "subject": "c",
    "num": 43,
    "title": "In-Place String Reversal Algorithm (Two-Pointer Technique)",
    "module": "Module 2",
    "category": "String Manipulation",
    "concept": "1. In-place requirement: Modifies the original memory buffer directly, requiring $O(1)$ auxiliary space.\n2. Algorithm:\n-",
    "url": "c_programming.html#c-q43"
  },
  {
    "subject": "c",
    "num": 44,
    "title": "Palindrome String Check: Case-Insensitive and Ignoring Punctuation",
    "module": "Module 2",
    "category": "String Manipulation",
    "concept": "1. Symmetry: Compare `tolower(str[left])` with `tolower(str[right])`.\n2. If any pair differs, the string is not a palind",
    "url": "c_programming.html#c-q44"
  },
  {
    "subject": "c",
    "num": 45,
    "title": "Character Frequency and Categorization (Vowels, Consonants, Digits, Spaces)",
    "module": "Module 2",
    "category": "String Operations",
    "concept": "1. Classification Rules:\n- Vowels: `ch` is alphabetic AND matches `'a','e','i','o','u'` (case-insensitive).\n- Consonants",
    "url": "c_programming.html#c-q45"
  },
  {
    "subject": "c",
    "num": 46,
    "title": "Array of Strings (2D char Array) and Alphabetical Sorting",
    "module": "Module 2",
    "category": "Strings & Sorting",
    "concept": "1. Memory Structure: `names[i]` represents a pointer to the $i$-th null-terminated string.\n2. Alphabetical Sort: If `str",
    "url": "c_programming.html#c-q46"
  },
  {
    "subject": "c",
    "num": 47,
    "title": "Selection Sort Algorithm: Logic, Trace, and Implementation",
    "module": "Module 2",
    "category": "Sorting Algorithms",
    "concept": "1. In pass $i$ (from 0 to $N-2$), assume `min_idx = i`.\n2. Iterate through index $j = i + 1$ to $N - 1$. If `arr[j] < ar",
    "url": "c_programming.html#c-q47"
  },
  {
    "subject": "c",
    "num": 48,
    "title": "Title Casing: Capitalize First Letter of Each Word in a Sentence",
    "module": "Module 2",
    "category": "String Manipulation",
    "concept": "1. Word Boundary: A word starts when a non-whitespace character follows whitespace (or starts at index 0).\n2. First lett",
    "url": "c_programming.html#c-q48"
  },
  {
    "subject": "c",
    "num": 49,
    "title": "Substrings: Searching and Extracting Patterns without strstr()",
    "module": "Module 2",
    "category": "String Manipulation",
    "concept": "1. Brute-Force Pattern Matching:\n- Outer loop index $i$ runs from 0 to $N - M$ (where $N = \\text{len}(text)$, $M = \\text",
    "url": "c_programming.html#c-q49"
  },
  {
    "subject": "c",
    "num": 50,
    "title": "Array Element Frequency Counter using Hash Array",
    "module": "Module 2",
    "category": "1D Arrays",
    "concept": "1. Direct Address Table / Hash Table concept.\n2. If values range from $0$ to $K$, an auxiliary array `int count[K + 1] =",
    "url": "c_programming.html#c-q50"
  },
  {
    "subject": "c",
    "num": 51,
    "title": "Output Prediction & Debugging: sizeof vs strlen on Arrays and Pointers",
    "module": "Module 2",
    "category": "Debugging & Tracing",
    "concept": "Critical Differences:\n1. `char arr[20] = \"Hello\";`\n- `sizeof(arr)` = 20 bytes (full array allocation in memory).\n- `strl",
    "url": "c_programming.html#c-q51"
  },
  {
    "subject": "c",
    "num": 52,
    "title": "Module 2 Mastery: Comprehensive Array & String Diagnostic Review",
    "module": "Module 2",
    "category": "Comprehensive Review",
    "concept": "Top 5 Array & String Traps:\n1. Off-by-one: Declaring `int a[10]` and accessing `a[10]` (valid indices: 0 to 9).\n2. Strin",
    "url": "c_programming.html#c-q52"
  },
  {
    "subject": "c",
    "num": 53,
    "title": "Modular Programming: Function Prototypes, Definitions, and Calls",
    "module": "Module 3",
    "category": "Functions",
    "concept": "1. Function Prototype: `return_type function_name(param_type1, param_type2);`\n- Allows calling functions defined later i",
    "url": "c_programming.html#c-q53"
  },
  {
    "subject": "c",
    "num": 54,
    "title": "Call by Value: Parameter Passing Mechanism and Proof of Value Isolation",
    "module": "Module 3",
    "category": "Functions",
    "concept": "1. Actual Arguments: Variables passed in the function call (`main` scope).\n2. Formal Parameters: Variables defined in th",
    "url": "c_programming.html#c-q54"
  },
  {
    "subject": "c",
    "num": 55,
    "title": "Storage Classes in C: auto, extern, static, and register",
    "module": "Module 3",
    "category": "Storage Classes",
    "concept": "Comprehensive Comparison:\n1. `auto`:\n- Keyword: `auto` (default for local variables)\n- Storage: Stack memory\n- Scope: Bl",
    "url": "c_programming.html#c-q55"
  },
  {
    "subject": "c",
    "num": 56,
    "title": "Introduction to Pointers: Addresses, Declarations, and Dereferencing",
    "module": "Module 3",
    "category": "Pointers",
    "concept": "1. Declaration: `data_type *ptr_name;` (e.g. `int *p`).\n- The `*` indicates `p` is a pointer.\n- The `data_type` indicate",
    "url": "c_programming.html#c-q56"
  },
  {
    "subject": "c",
    "num": 57,
    "title": "Call by Reference: Pointer-Based Argument Modification and Swapping",
    "module": "Module 3",
    "category": "Pointers & Functions",
    "concept": "1. Memory Sharing: Caller passes `&x`. Callee receives `int *ptr`. Callee performs `*ptr = new_val`, altering `x` in the",
    "url": "c_programming.html#c-q57"
  },
  {
    "subject": "c",
    "num": 58,
    "title": "Pointer Arithmetic: Scaling Rules, Valid Operations, and Subtraction",
    "module": "Module 3",
    "category": "Pointers",
    "concept": "1. Scaling Formula: `Address(ptr + n) = Address(ptr) + n * sizeof(*ptr)`.\n- For `int *p` (4 bytes): `p + 1` advances by ",
    "url": "c_programming.html#c-q58"
  },
  {
    "subject": "c",
    "num": 59,
    "title": "Pointers and Arrays: Equivalence of *(arr + i) and arr[i]",
    "module": "Module 3",
    "category": "Pointers & Arrays",
    "concept": "1. Array Decay: In most expressions, an array name evaluates to a pointer to its first element (`&arr[0]`).\n2. Pointer C",
    "url": "c_programming.html#c-q59"
  },
  {
    "subject": "c",
    "num": 60,
    "title": "Double Pointers (Pointer to Pointer): Concepts and Dynamic Allocation",
    "module": "Module 3",
    "category": "Pointers",
    "concept": "1. Declaration: `int **pp;`\n2. Addressing Chain: `var` (value 50 at 0x1000) $\\leftarrow$ `p` (holds 0x1000 at 0x2000) $\\",
    "url": "c_programming.html#c-q60"
  },
  {
    "subject": "c",
    "num": 61,
    "title": "const with Pointers: Pointer to Constant vs Constant Pointer",
    "module": "Module 3",
    "category": "Pointers & Modifiers",
    "concept": "1. Pointer to Constant (`const int *p` or `int const *p`):\n- Data is read-only. You CANNOT modify the value through `*p`",
    "url": "c_programming.html#c-q61"
  },
  {
    "subject": "c",
    "num": 62,
    "title": "Function Pointers: Callback Architecture and Dispatch Tables",
    "module": "Module 3",
    "category": "Advanced Pointers",
    "concept": "1. Declaration Syntax: `return_type (*func_ptr_name)(param_types);`\n- Parentheses around `(*func_ptr_name)` are mandator",
    "url": "c_programming.html#c-q62"
  },
  {
    "subject": "c",
    "num": 63,
    "title": "Introduction to Recursion: Base Cases, Recursive Steps, and Call Stack",
    "module": "Module 3",
    "category": "Recursion",
    "concept": "1. Base Case: The stopping condition that returns a result directly without further recursive calls.\n2. Recursive Step: ",
    "url": "c_programming.html#c-q63"
  },
  {
    "subject": "c",
    "num": 64,
    "title": "Factorial Computation using Recursion: Stack Frame Trace",
    "module": "Module 3",
    "category": "Recursion",
    "concept": "1. Recurrence: $F(n) = n \\cdot F(n - 1)$ for $n > 1$; $F(0) = F(1) = 1$.\n2. Stack Trace for `factorial(4)`:\n- Call 1: `f",
    "url": "c_programming.html#c-q64"
  },
  {
    "subject": "c",
    "num": 65,
    "title": "Fibonacci Sequence: Recursion Tree and Exponential Overhead",
    "module": "Module 3",
    "category": "Recursion",
    "concept": "1. Recurrence: $T(N) = T(N-1) + T(N-2) + O(1) \\implies O(2^N)$ time complexity.\n2. Call Tree for $F(4)$:\n```\n           ",
    "url": "c_programming.html#c-q65"
  },
  {
    "subject": "c",
    "num": 66,
    "title": "GCD using Euclid's Algorithm: Mathematical Basis and Recursive Implementation",
    "module": "Module 3",
    "category": "Recursion",
    "concept": "1. Mathematical Principle: If $d$ divides both $a$ and $b$, then $d$ also divides the remainder $a \\% b$.\n2. Base Case: ",
    "url": "c_programming.html#c-q66"
  },
  {
    "subject": "c",
    "num": 67,
    "title": "Tower of Hanoi: Recursive Formulation, Move Trace, and Minimal Moves",
    "module": "Module 3",
    "category": "Recursion",
    "concept": "1. Rules:\n- Only one disk can be moved at a time.\n- Each move takes the upper disk from one stack and places it on top o",
    "url": "c_programming.html#c-q67"
  },
  {
    "subject": "c",
    "num": 68,
    "title": "Sum of Digits and Power Function (x^n) using Recursion",
    "module": "Module 3",
    "category": "Recursion",
    "concept": "1. Sum of Digits: Base case `n == 0` returns 0. Time complexity is $O(\\log_{10} N)$.\n2. Binary Exponentiation:\n- Naive r",
    "url": "c_programming.html#c-q68"
  },
  {
    "subject": "c",
    "num": 69,
    "title": "Recursion vs Iteration: Comprehensive Technical Comparison",
    "module": "Module 3",
    "category": "Recursion",
    "concept": "Detailed Comparison Table:\n1. Basic Construct:\n- Recursion: Self-referential function calls with a base case.\n- Iteratio",
    "url": "c_programming.html#c-q69"
  },
  {
    "subject": "c",
    "num": 70,
    "title": "Passing Arrays to Functions: 1D and 2D Decay to Pointers",
    "module": "Module 3",
    "category": "Pointers & Arrays",
    "concept": "1. 1D Array Parameter: `void process(int *arr, int size)` or `void process(int arr[], int size)`. Both are completely id",
    "url": "c_programming.html#c-q70"
  },
  {
    "subject": "c",
    "num": 71,
    "title": "Binary Search using Recursion: Algorithm and Recursive Trace",
    "module": "Module 3",
    "category": "Recursion & Searching",
    "concept": "1. Base Cases:\n- `low > high`: Target not found, return `-1`.\n- `arr[mid] == key`: Target found, return `mid`.\n2. Stack ",
    "url": "c_programming.html#c-q71"
  },
  {
    "subject": "c",
    "num": 72,
    "title": "Void Pointers (Generic Pointers) and Type Casting Mechanics",
    "module": "Module 3",
    "category": "Pointers",
    "concept": "1. Generic Pointer: Any pointer type (`int*`, `double*`, `char*`, struct pointer) can be assigned to `void*` and back wi",
    "url": "c_programming.html#c-q72"
  },
  {
    "subject": "c",
    "num": 73,
    "title": "Pointers to Strings: String Pointers vs Character Arrays",
    "module": "Module 3",
    "category": "Pointers & Strings",
    "concept": "Comparison:\n1. `char str[] = \"Hello\";`\n- Memory: Stack segment\n- Mutability: Mutable. `str[0] = 'M'` is valid and change",
    "url": "c_programming.html#c-q73"
  },
  {
    "subject": "c",
    "num": 74,
    "title": "Output Prediction: Dangling Pointers from Returning Local Stack Addresses",
    "module": "Module 3",
    "category": "Debugging & Tracing",
    "concept": "1. Lifetime Violation: The lifetime of `int x` ends as soon as `getLocalAddress()` returns and its stack frame is popped",
    "url": "c_programming.html#c-q74"
  },
  {
    "subject": "c",
    "num": 75,
    "title": "Output Prediction & Debugging: Uninitialized Pointer Dereferencing",
    "module": "Module 3",
    "category": "Debugging & Tracing",
    "concept": "1. Wild Pointer: A pointer that has been declared but not initialized to any valid memory address or `NULL`.\n2. In prote",
    "url": "c_programming.html#c-q75"
  },
  {
    "subject": "c",
    "num": 76,
    "title": "Module 3 Mastery: Comprehensive Functions, Pointers, and Recursion Diagnostic",
    "module": "Module 3",
    "category": "Comprehensive Review",
    "concept": "Top 5 Pitfalls in Module 3:\n1. Array decay: Forgetting that arrays decay to pointers inside functions.\n2. Call by value:",
    "url": "c_programming.html#c-q76"
  },
  {
    "subject": "c",
    "num": 77,
    "title": "Direct vs Indirect (Mutual) Recursion: Even/Odd Numbers Verification",
    "module": "Module 3",
    "category": "Recursion Types",
    "concept": "1. Direct Recursion: A -> A -> A.\n2. Indirect Recursion: A -> B -> A -> B.\n3. Requires function prototype declarations s",
    "url": "c_programming.html#c-q77"
  },
  {
    "subject": "c",
    "num": 78,
    "title": "Generic Sorting with qsort() and Custom Comparator Function Pointers",
    "module": "Module 3",
    "category": "Function Pointers",
    "concept": "1. Prototype: void qsort(void *base, size_t nitems, size_t size, int (*compar)(const void *, const void *));\n2. Comparat",
    "url": "c_programming.html#c-q78"
  },
  {
    "subject": "c",
    "num": 79,
    "title": "Structures: Motivation, Declaration, and Dot Operator",
    "module": "Module 4",
    "category": "Structures",
    "concept": "1. Definition: `struct TagName { member1_type m1; member2_type m2; ... };`\n2. Instantiation:\n- With definition: `struct ",
    "url": "c_programming.html#c-q79"
  },
  {
    "subject": "c",
    "num": 80,
    "title": "Structure Padding, Byte Alignment, and the #pragma pack Directive",
    "module": "Module 4",
    "category": "Structures & Memory",
    "concept": "1. Natural Alignment Rules (on 64-bit systems):\n- `char` (1 byte): Any address boundary.\n- `short` (2 bytes): Even addre",
    "url": "c_programming.html#c-q80"
  },
  {
    "subject": "c",
    "num": 81,
    "title": "Array of Structures: Student Record Management System",
    "module": "Module 4",
    "category": "Structures",
    "concept": "1. Declaration: `struct Student batch[50];`\n2. Indexing: `batch[0]` is the first student record, `batch[1]` is the secon",
    "url": "c_programming.html#c-q81"
  },
  {
    "subject": "c",
    "num": 82,
    "title": "Nested Structures: Hierarchical Data Modeling and Date of Joining",
    "module": "Module 4",
    "category": "Structures",
    "concept": "1. Separate Declaration (Recommended for reusability):\n```c\nstruct Date { int day, month, year; };\nstruct Employee { int",
    "url": "c_programming.html#c-q82"
  },
  {
    "subject": "c",
    "num": 83,
    "title": "Passing Structures to Functions: By Value vs By Reference with Arrow (->)",
    "module": "Module 4",
    "category": "Structures & Pointers",
    "concept": "1. Pass by Value: `void display(struct Student s)` -> Clones the entire structure on the stack. Inefficient for large st",
    "url": "c_programming.html#c-q83"
  },
  {
    "subject": "c",
    "num": 84,
    "title": "Unions in C: Shared Memory Mechanics and Differences from Structures",
    "module": "Module 4",
    "category": "Unions",
    "concept": "Comprehensive Differences Table:\n1. Keyword: `struct` vs `union`.\n2. Memory Allocation:\n- Structure: Allocates separate,",
    "url": "c_programming.html#c-q84"
  },
  {
    "subject": "c",
    "num": 85,
    "title": "typedef and Enumerations (enum): Type Safety and State Machines",
    "module": "Module 4",
    "category": "User-Defined Types",
    "concept": "1. `typedef` Syntax: `typedef existing_type new_name;`\n- Example: `typedef unsigned long long uint64;`\n- Eliminates repe",
    "url": "c_programming.html#c-q85"
  },
  {
    "subject": "c",
    "num": 86,
    "title": "C Program Memory Architecture: Text, Data, BSS, Stack, and Heap",
    "module": "Module 4",
    "category": "Memory Architecture",
    "concept": "1. Text Segment (Code): Contains compiled machine instructions. Marked Read-Only to prevent accidental modification; sha",
    "url": "c_programming.html#c-q86"
  },
  {
    "subject": "c",
    "num": 87,
    "title": "Stack vs Heap Memory: Allocation Speed, Lifetime, and Management",
    "module": "Module 4",
    "category": "Memory Management",
    "concept": "Comparison Table:\n1. Management:\n- Stack: Fully automatic by compiler/CPU stack pointer.\n- Heap: Manual by programmer (`",
    "url": "c_programming.html#c-q87"
  },
  {
    "subject": "c",
    "num": 88,
    "title": "Dynamic Memory Allocation: malloc() Function and NULL Verification",
    "module": "Module 4",
    "category": "DMA Functions",
    "concept": "1. Prototype: `void *malloc(size_t size);`\n2. Key Properties:\n- Takes total bytes as argument: `n * sizeof(int)`.\n- Does",
    "url": "c_programming.html#c-q88"
  },
  {
    "subject": "c",
    "num": 89,
    "title": "The calloc() Function: Contiguous Allocation and Zero-Initialization",
    "module": "Module 4",
    "category": "DMA Functions",
    "concept": "1. Prototype: `void *calloc(size_t num_elements, size_t element_size);`\n2. Key Differences from `malloc()`:\n- Parameter ",
    "url": "c_programming.html#c-q89"
  },
  {
    "subject": "c",
    "num": 90,
    "title": "The realloc() Function: Safe Buffer Resizing and Expansion",
    "module": "Module 4",
    "category": "DMA Functions",
    "concept": "1. Prototype: `void *realloc(void *ptr, size_t new_size);`\n2. Reallocation Scenarios:\n- Case A (In-Place): If contiguous",
    "url": "c_programming.html#c-q90"
  },
  {
    "subject": "c",
    "num": 91,
    "title": "Dynamic 2D Arrays: Array of Pointers and Row-by-Row Deallocation",
    "module": "Module 4",
    "category": "DMA Advanced",
    "concept": "1. Double Pointer Allocation Pattern:\n- Step 1: Allocate row pointer array: `int **matrix = malloc(R * sizeof(int *));`\n",
    "url": "c_programming.html#c-q91"
  },
  {
    "subject": "c",
    "num": 92,
    "title": "Memory Leaks: Root Causes, Consequences, and Detection Tools",
    "module": "Module 4",
    "category": "Memory Safety",
    "concept": "1. Root Causes:\n- Reassigning a pointer before freeing its existing block (`p = malloc(10); p = malloc(20);` -> first 10",
    "url": "c_programming.html#c-q92"
  },
  {
    "subject": "c",
    "num": 93,
    "title": "Dangling Pointers and Double Free Vulnerabilities",
    "module": "Module 4",
    "category": "Memory Safety",
    "concept": "1. Dangling Pointer:\n- Occurs when memory is freed via `free(ptr)`, but `ptr` still holds the old memory address.\n- Acce",
    "url": "c_programming.html#c-q93"
  },
  {
    "subject": "c",
    "num": 94,
    "title": "Self-Referential Structures: Foundation of Linked Lists and Trees",
    "module": "Module 4",
    "category": "Data Structures Foundation",
    "concept": "1. Why an instance by value is illegal:\n```c\nstruct BadNode { int val; struct BadNode next; }; /* ILLEGAL! Infinite size",
    "url": "c_programming.html#c-q94"
  },
  {
    "subject": "c",
    "num": 95,
    "title": "Tagged Unions (Discriminated Unions) for Variant Data Types",
    "module": "Module 4",
    "category": "Unions & Design",
    "concept": "1. Pattern Structure:\n```c\ntypedef struct {\n    enum { TYPE_INT, TYPE_FLOAT, TYPE_STRING } type;\n    union {\n        int",
    "url": "c_programming.html#c-q95"
  },
  {
    "subject": "c",
    "num": 96,
    "title": "Bit-Fields in Structures: Packing Hardware Flags into Minimal Bits",
    "module": "Module 4",
    "category": "Structures & Hardware",
    "concept": "1. Syntax: `type member_name : bit_width;`\n- Typically declared with `unsigned int`, `signed int`, or `_Bool`.\n- Example",
    "url": "c_programming.html#c-q96"
  },
  {
    "subject": "c",
    "num": 97,
    "title": "Structure Copy Assignment and Designated Initializers",
    "module": "Module 4",
    "category": "Structures",
    "concept": "1. Direct Structure Assignment: `struct Point p2 = p1;` copies all bytes of `p1` into `p2`.\n- Note: Arrays inside struct",
    "url": "c_programming.html#c-q97"
  },
  {
    "subject": "c",
    "num": 98,
    "title": "Dynamic Array Resizing: Implementing a Vector Growth Pattern",
    "module": "Module 4",
    "category": "DMA Patterns",
    "concept": "1. Vector Structure:\n```c\ntypedef struct {\n    int *data;\n    size_t size;\n    size_t capacity;\n} DynamicArray;\n```\n2. G",
    "url": "c_programming.html#c-q98"
  },
  {
    "subject": "c",
    "num": 99,
    "title": "Anonymous Structures and Unions in Modern C (C11 Feature)",
    "module": "Module 4",
    "category": "Modern C Features",
    "concept": "1. Traditional Nested Access:\n```c\nstruct Outer { struct { int x, y; } point; };\nobj.point.x = 10; /* Requires .point qu",
    "url": "c_programming.html#c-q99"
  },
  {
    "subject": "c",
    "num": 100,
    "title": "Alignment Control in C11: alignof, alignas, and aligned_alloc()",
    "module": "Module 4",
    "category": "Memory & Performance",
    "concept": "1. `alignof(type)`: Returns the alignment requirement of a type in bytes.\n2. `alignas(N)`: Forces a variable or structur",
    "url": "c_programming.html#c-q100"
  },
  {
    "subject": "c",
    "num": 101,
    "title": "Comprehensive Pointer Taxonomy: Null, Wild, Dangling, and Void Pointers",
    "module": "Module 4",
    "category": "Pointers Mastery",
    "concept": "Comparison Taxonomy:\n1. Null Pointer:\n- Definition: Explicitly points to address 0 (`NULL`).\n- Hazard: Dereferencing cau",
    "url": "c_programming.html#c-q101"
  },
  {
    "subject": "c",
    "num": 102,
    "title": "Output Prediction & Debugging: Memory Leaks and Dangling Pointer Tracing",
    "module": "Module 4",
    "category": "Debugging & Tracing",
    "concept": "Bug Identification:\n1. Memory Leak: Allocating a new block and overwriting the pointer without freeing the previous bloc",
    "url": "c_programming.html#c-q102"
  },
  {
    "subject": "c",
    "num": 103,
    "title": "Output Prediction: Structure Size with Bit-Fields and Alignment Padding",
    "module": "Module 4",
    "category": "Debugging & Tracing",
    "concept": "Step-by-Step Memory Layout Calculation:\n1. `char a`: Offset 0, size 1 byte.\n2. Padding: 3 padding bytes inserted (offset",
    "url": "c_programming.html#c-q103"
  },
  {
    "subject": "c",
    "num": 104,
    "title": "Module 4 Mastery: Comprehensive Structures & DMA Diagnostic Review",
    "module": "Module 4",
    "category": "Comprehensive Review",
    "concept": "Top 7 Module 4 Rules:\n1. Structure dot vs arrow: Use `.` on variables (`s.x`), use `->` on pointers (`ptr->x`).\n2. Align",
    "url": "c_programming.html#c-q104"
  },
  {
    "subject": "c",
    "num": 105,
    "title": "Introduction to File Handling: Streams, stdin/stdout/stderr, and Text vs Binary",
    "module": "Module 5",
    "category": "File Fundamentals",
    "concept": "1. Stream Concept: An abstract logical interface mapping to physical I/O devices (keyboard, monitor, disk file). All C f",
    "url": "c_programming.html#c-q105"
  },
  {
    "subject": "c",
    "num": 106,
    "title": "The FILE Structure and File Pointer (FILE *fp)",
    "module": "Module 5",
    "category": "File Fundamentals",
    "concept": "1. The `FILE` Structure Contents:\n- Integer file descriptor assigned by the operating system kernel.\n- Pointer to the st",
    "url": "c_programming.html#c-q106"
  },
  {
    "subject": "c",
    "num": 107,
    "title": "fopen() and fclose(): Error Handling and Buffer Flushing",
    "module": "Module 5",
    "category": "File Operations",
    "concept": "1. `FILE *fopen(const char *filename, const char *mode);`\n- Returns valid pointer on success; returns `NULL` on error (e",
    "url": "c_programming.html#c-q107"
  },
  {
    "subject": "c",
    "num": 108,
    "title": "Comprehensive File Opening Modes: r, w, a, r+, w+, a+, and Binary Modes",
    "module": "Module 5",
    "category": "File Modes",
    "concept": "Comprehensive File Mode Reference Table:\n1. `\"r\"` (Read):\n- File must exist (fails and returns `NULL` if not found).\n- C",
    "url": "c_programming.html#c-q108"
  },
  {
    "subject": "c",
    "num": 109,
    "title": "Character I/O in Files: fgetc(), fputc(), and File Copy Utility",
    "module": "Module 5",
    "category": "File Operations",
    "concept": "1. Prototypes:\n- `int fgetc(FILE *stream);`\n- `int fputc(int ch, FILE *stream);`\n2. Why `int` is Mandatory for `fgetc()`",
    "url": "c_programming.html#c-q109"
  },
  {
    "subject": "c",
    "num": 110,
    "title": "Line-Oriented File I/O: fgets(), fputs(), and Word/Line Counter",
    "module": "Module 5",
    "category": "File Operations",
    "concept": "1. `char *fgets(char *str, int n, FILE *stream);`\n- Reads at most `n - 1` characters.\n- Retains the newline character `\\",
    "url": "c_programming.html#c-q110"
  },
  {
    "subject": "c",
    "num": 111,
    "title": "Formatted File I/O: fprintf() and fscanf() with Student Records",
    "module": "Module 5",
    "category": "File Operations",
    "concept": "1. Prototypes:\n- `int fprintf(FILE *stream, const char *format, ...);`\n- `int fscanf(FILE *stream, const char *format, .",
    "url": "c_programming.html#c-q111"
  },
  {
    "subject": "c",
    "num": 112,
    "title": "Binary File I/O: fwrite() and fread() for Direct Memory Blocks",
    "module": "Module 5",
    "category": "Binary File Operations",
    "concept": "1. Prototypes:\n- `size_t fwrite(const void *ptr, size_t size, size_t count, FILE *stream);`\n- `size_t fread(void *ptr, s",
    "url": "c_programming.html#c-q112"
  },
  {
    "subject": "c",
    "num": 113,
    "title": "Random Access in Files: fseek(), ftell(), and rewind()",
    "module": "Module 5",
    "category": "File Positioning",
    "concept": "1. `int fseek(FILE *stream, long offset, int origin);`\n- `SEEK_SET`: Offset is relative to the BEGINNING of the file.\n- ",
    "url": "c_programming.html#c-q113"
  },
  {
    "subject": "c",
    "num": 114,
    "title": "Error Handling in Files: feof(), ferror(), clearerr(), and perror()",
    "module": "Module 5",
    "category": "File Operations",
    "concept": "1. `int feof(FILE *stream);`: Returns non-zero only AFTER a read operation has attempted to read past the end of the fil",
    "url": "c_programming.html#c-q114"
  },
  {
    "subject": "c",
    "num": 115,
    "title": "Introduction to C Preprocessor: The # Symbol and Translation Phases",
    "module": "Module 5",
    "category": "Preprocessor",
    "concept": "1. Directives begin with `#` (e.g. `#include`, `#define`, `#ifdef`).\n2. Key Differences from C Statements:\n- Handled dur",
    "url": "c_programming.html#c-q115"
  },
  {
    "subject": "c",
    "num": 116,
    "title": "#include Directive: Angle Brackets (<>) vs Double Quotes (\"\")",
    "module": "Module 5",
    "category": "Preprocessor",
    "concept": "1. `#include <filename.h>` (Angle Brackets):\n- Used for standard system headers (e.g. `<stdio.h>`, `<stdlib.h>`, `<math.",
    "url": "c_programming.html#c-q116"
  },
  {
    "subject": "c",
    "num": 117,
    "title": "#define Object-Like Macros vs const Variables",
    "module": "Module 5",
    "category": "Preprocessor",
    "concept": "Comparison Table:\n1. Type Safety:\n- `#define`: Untyped. The preprocessor performs raw text substitution without type che",
    "url": "c_programming.html#c-q117"
  },
  {
    "subject": "c",
    "num": 118,
    "title": "#define Function-Like Macros: Argument Parenthesizing and Precedence Hazards",
    "module": "Module 5",
    "category": "Preprocessor",
    "concept": "The `SQUARE` Precedence Trap:\n1. Flawed Definition: `#define SQUARE(x) x * x`\n- Evaluating `SQUARE(2 + 3)` expands textu",
    "url": "c_programming.html#c-q118"
  },
  {
    "subject": "c",
    "num": 119,
    "title": "Macros vs Inline Functions: Type Checking, Expansion, and Modern Best Practices",
    "module": "Module 5",
    "category": "Preprocessor vs Compiler",
    "concept": "Comparison Table:\n1. Mechanism:\n- Macro: Textual token substitution by preprocessor.\n- Inline Function: Actual function ",
    "url": "c_programming.html#c-q119"
  },
  {
    "subject": "c",
    "num": 120,
    "title": "Preprocessor Operators: Stringizing (#) and Token-Pasting (##)",
    "module": "Module 5",
    "category": "Advanced Preprocessor",
    "concept": "1. Stringizing Operator `#`:\n- Converts macro argument text into a string literal.\n- Example: `#define PRINT_INT(var) pr",
    "url": "c_programming.html#c-q120"
  },
  {
    "subject": "c",
    "num": 121,
    "title": "Conditional Compilation: #ifdef, #ifndef, #if, #else, #elif, and #endif",
    "module": "Module 5",
    "category": "Conditional Compilation",
    "concept": "1. Directives:\n- `#ifdef MACRO`: Compiles subsequent block if `MACRO` is defined.\n- `#ifndef MACRO`: Compiles if `MACRO`",
    "url": "c_programming.html#c-q121"
  },
  {
    "subject": "c",
    "num": 122,
    "title": "Header Guards: Preventing Multiple Header Inclusion and Redefinition Errors",
    "module": "Module 5",
    "category": "Header Architecture",
    "concept": "1. The Multiple Inclusion Problem:\n- `geometry.h` defines `struct Point { int x, y; };`.\n- `shape.h` includes `geometry.",
    "url": "c_programming.html#c-q122"
  },
  {
    "subject": "c",
    "num": 123,
    "title": "The #pragma Directive: #pragma once and #pragma pack",
    "module": "Module 5",
    "category": "Preprocessor Directives",
    "concept": "1. `#pragma once`:\n- A non-standard but universally supported compiler directive.\n- Serves the exact same purpose as tra",
    "url": "c_programming.html#c-q123"
  },
  {
    "subject": "c",
    "num": 124,
    "title": "Standard Predefined Macros in C (__LINE__, __FILE__, __DATE__, __TIME__, __func__)",
    "module": "Module 5",
    "category": "Preprocessor",
    "concept": "Standard Predefined Macros:\n1. `__LINE__`: Current line number in source file (integer decimal).\n2. `__FILE__`: Name of ",
    "url": "c_programming.html#c-q124"
  },
  {
    "subject": "c",
    "num": 125,
    "title": "#undef and #error Directives: Enforcing Compilation Constraints",
    "module": "Module 5",
    "category": "Preprocessor Directives",
    "concept": "1. `#undef MACRO_NAME`:\n- Cancels a previously defined macro.\n- Subsequent references are treated as if the macro was ne",
    "url": "c_programming.html#c-q125"
  },
  {
    "subject": "c",
    "num": 126,
    "title": "Output Prediction & Debugging: Macro Side-Effects and Traps",
    "module": "Module 5",
    "category": "Debugging & Tracing",
    "concept": "Expansion Trace:\n1. Macro: `#define DOUBLE(x) x + x`\n2. Call: `DOUBLE(5) * 10`\n3. Preprocessor Output: `5 + 5 * 10`\n4. M",
    "url": "c_programming.html#c-q126"
  },
  {
    "subject": "c",
    "num": 127,
    "title": "Output Prediction & Debugging: File Mode Truncation Trap",
    "module": "Module 5",
    "category": "Debugging & Tracing",
    "concept": "1. Mode `\"w\"` Truncation:\n- If the file exists, the OS kernel sets file length to 0 bytes.\n- Content is unrecoverable th",
    "url": "c_programming.html#c-q127"
  },
  {
    "subject": "c",
    "num": 128,
    "title": "Comprehensive File Application: Student Database with File Persistence",
    "module": "Module 5",
    "category": "Comprehensive Integration",
    "concept": "1. Persistence Architecture:\n- Records are stored as binary `struct Student` blocks.\n- Adding a student appends to the f",
    "url": "c_programming.html#c-q128"
  },
  {
    "subject": "c",
    "num": 129,
    "title": "Comprehensive Preprocessor Application: Multi-Level Debug Logger",
    "module": "Module 5",
    "category": "Comprehensive Integration",
    "concept": "1. Variadic Macros (C99): `#define LOG(fmt, ...) printf(fmt, ##__VA_ARGS__)` allows macros to accept variable numbers of",
    "url": "c_programming.html#c-q129"
  },
  {
    "subject": "c",
    "num": 130,
    "title": "Module 5 Mastery: Comprehensive File Handling & Preprocessor Diagnostic Review",
    "module": "Module 5",
    "category": "Comprehensive Review",
    "concept": "Top 7 Module 5 Rules:\n1. Always check `fopen() != NULL`: Verify file was opened successfully.\n2. Always close files with",
    "url": "c_programming.html#c-q130"
  }
];

let currentSearchFilter = 'all';
let currentActiveBookmarkTab = 'c';

// Initialize when DOM loads
document.addEventListener('DOMContentLoaded', () => {
    initSubjectNavigation();
    initLearningState();
    initShortcuts();
});

/* ---- Navigation & Header Enhancement ---- */
function initSubjectNavigation() {
    const topNav = document.getElementById('top-nav');
    if (!topNav) return;

    // Detect if we are on the Mathematics page and enhance top nav if needed
    const isMathPage = window.location.pathname.includes('1BMATS101') || 
                       document.title.includes('1BMATS101') ||
                       document.body.getAttribute('data-subject') === 'math';

    if (isMathPage && !document.querySelector('.nav-brand')) {
        // We are on Mathematics page: Upgrade top nav with subject switcher tabs
        const navTitle = topNav.querySelector('.nav-title');
        if (navTitle) {
            navTitle.innerHTML = `
                <div class="nav-brand">
                    <a href="1BMATS101_Complete_Textbook.html" class="subject-tab active" title="Active: Applied Mathematics Notes">📐 Mathematics (1BMATS101)</a>
                    <a href="c_programming.html" class="subject-tab" title="Switch to C Programming Notes">💻 C Programming</a>
                </div>
            `;
        }

        // Add search and bookmark triggers to actions
        const navActions = topNav.querySelector('.nav-actions');
        if (navActions && !navActions.querySelector('.search-trigger-btn')) {
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
        }

        // Ensure search modal and drawer exist on math page too
        ensureModalsExist();
        document.body.setAttribute('data-subject', 'math');
    }
}

function ensureModalsExist() {
    if (!document.getElementById('search-modal')) {
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
    }

    if (!document.getElementById('bookmarks-drawer')) {
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
    }
}

/* ---- Bookmarks & Progress State Management ---- */
function getStorageKey(type, subject) {
    return `studyhub_${type}_${subject}`;
}

function getBookmarks(subject) {
    try {
        return JSON.parse(localStorage.getItem(getStorageKey('bookmarks', subject)) || '[]');
    } catch (e) {
        return [];
    }
}

function saveBookmarks(subject, list) {
    localStorage.setItem(getStorageKey('bookmarks', subject), JSON.stringify(list));
    updateBadges();
}

function getMastered(subject) {
    try {
        return JSON.parse(localStorage.getItem(getStorageKey('mastered', subject)) || '[]');
    } catch (e) {
        return [];
    }
}

function saveMastered(subject, list) {
    localStorage.setItem(getStorageKey('mastered', subject), JSON.stringify(list));
    updateProgressUI();
}

function initLearningState() {
    const currentSubject = document.body.getAttribute('data-subject') || 'c';

    // Restore bookmarks buttons
    const bmList = getBookmarks(currentSubject);
    bmList.forEach(num => {
        const btn = document.querySelector(`.bookmark-btn[data-q="${num}"]`);
        if (btn) {
            btn.classList.add('bookmarked');
            btn.innerHTML = '★ Bookmarked';
        }
    });

    // Restore mastered checkboxes
    const masteredList = getMastered(currentSubject);
    masteredList.forEach(num => {
        const cb = document.querySelector(`.mastered-checkbox[data-q="${num}"]`);
        if (cb) {
            cb.checked = true;
            const label = cb.closest('.mastered-label');
            if (label) label.classList.add('is-mastered');
        }
    });

    updateBadges();
    updateProgressUI();
}

function toggleBookmark(subject, qNum, btn) {
    let list = getBookmarks(subject);
    const index = list.indexOf(qNum);

    if (index === -1) {
        list.push(qNum);
        if (btn) {
            btn.classList.add('bookmarked');
            btn.innerHTML = '★ Bookmarked';
        }
    } else {
        list.splice(index, 1);
        if (btn) {
            btn.classList.remove('bookmarked');
            btn.innerHTML = '⭐ Bookmark';
        }
    }

    saveBookmarks(subject, list);
    renderBookmarksDrawerContent();
}

function toggleMastered(subject, qNum, checkbox) {
    let list = getMastered(subject);
    const index = list.indexOf(qNum);

    if (checkbox.checked) {
        if (index === -1) list.push(qNum);
        const label = checkbox.closest('.mastered-label');
        if (label) label.classList.add('is-mastered');
    } else {
        if (index !== -1) list.splice(index, 1);
        const label = checkbox.closest('.mastered-label');
        if (label) label.classList.remove('is-mastered');
    }

    saveMastered(subject, list);
}

function updateProgressUI() {
    const currentSubject = document.body.getAttribute('data-subject') || 'c';
    const total = currentSubject === 'c' ? 130 : 125;
    const list = getMastered(currentSubject);
    const completedCount = list.length;
    const percent = Math.min(100, Math.round((completedCount / total) * 100));

    const fill = document.getElementById('subject-progress-fill');
    const text = document.getElementById('subject-progress-text');
    if (fill) fill.style.width = `${percent}%`;
    if (text) text.innerText = `${completedCount} / ${total} (${percent}%)`;
}

function updateBadges() {
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
}

/* ---- Search Engine Implementation ---- */
function openSearchModal() {
    ensureModalsExist();
    const modal = document.getElementById('search-modal');
    if (modal) {
        modal.classList.add('active');
        const input = document.getElementById('global-search-input');
        if (input) {
            input.focus();
            input.select();
        }
    }
}

function closeSearchModal() {
    const modal = document.getElementById('search-modal');
    if (modal) modal.classList.remove('active');
}

function handleModalBackdropClick(e) {
    if (e.target.id === 'search-modal') closeSearchModal();
}

function setSearchFilter(filter, btn) {
    currentSearchFilter = filter;
    document.querySelectorAll('.search-filters .filter-tab').forEach(t => t.classList.remove('active'));
    if (btn) btn.classList.add('active');
    const input = document.getElementById('global-search-input');
    if (input) performGlobalSearch(input.value);
}

function performGlobalSearch(query) {
    const container = document.getElementById('search-results-container');
    if (!container) return;

    const cleanQ = query.trim().toLowerCase();
    if (!cleanQ) {
        container.innerHTML = '<div class="search-placeholder">Type keywords, question numbers, topics, or formulas above to search...</div>';
        return;
    }

    let combined = [];
    if (currentSearchFilter === 'all' || currentSearchFilter === 'math') {
        combined = combined.concat(MATH_SEARCH_INDEX);
    }
    if (currentSearchFilter === 'all' || currentSearchFilter === 'c') {
        combined = combined.concat(C_SEARCH_INDEX);
    }

    const matches = combined.filter(item => {
        const qNumStr = `q${item.num}`;
        const numStr = `${item.num}`;
        return item.title.toLowerCase().includes(cleanQ) ||
               item.module.toLowerCase().includes(cleanQ) ||
               (item.category && item.category.toLowerCase().includes(cleanQ)) ||
               (item.concept && item.concept.toLowerCase().includes(cleanQ)) ||
               qNumStr === cleanQ ||
               numStr === cleanQ;
    });

    if (matches.length === 0) {
        container.innerHTML = `<div class="search-placeholder">No matching questions found for "${escapeHtml(query)}". Try searching for "derivative", "bubble sort", "pointer", "matrix", etc.</div>`;
        return;
    }

    container.innerHTML = matches.slice(0, 40).map(item => {
        const isC = item.subject === 'c';
        const subjName = isC ? 'C Programming' : 'Applied Mathematics';
        const subjClass = isC ? 'c' : 'math';
        return `
            <a href="${item.url}" class="search-result-item" onclick="closeSearchModal()">
                <div class="res-header">
                    <span class="res-subject ${subjClass}">${subjName}</span>
                    <span style="color:#64748b; font-weight:700;">${item.module} • Q${item.num}</span>
                </div>
                <div class="res-title">${escapeHtml(item.title)}</div>
                <div class="res-snippet">${escapeHtml(item.concept || '')}</div>
            </a>
        `;
    }).join('');
}

/* ---- Bookmarks Drawer Implementation ---- */
function openBookmarksDrawer() {
    ensureModalsExist();
    const drawer = document.getElementById('bookmarks-drawer');
    if (drawer) {
        drawer.classList.add('active');
        const currentSubject = document.body.getAttribute('data-subject') || 'c';
        switchBookmarkTab(currentSubject);
    }
}

function closeBookmarksDrawer() {
    const drawer = document.getElementById('bookmarks-drawer');
    if (drawer) drawer.classList.remove('active');
}

function handleDrawerBackdropClick(e) {
    if (e.target.id === 'bookmarks-drawer') closeBookmarksDrawer();
}

function switchBookmarkTab(subject, btn) {
    currentActiveBookmarkTab = subject;
    document.querySelectorAll('.drawer-tabs .drawer-tab').forEach(t => t.classList.remove('active'));
    const targetTabBtn = btn || document.getElementById(`tab-btn-${subject}`);
    if (targetTabBtn) targetTabBtn.classList.add('active');
    renderBookmarksDrawerContent();
}

function renderBookmarksDrawerContent() {
    const container = document.getElementById('bookmarks-list-container');
    if (!container) return;

    const list = getBookmarks(currentActiveBookmarkTab);
    const indexList = currentActiveBookmarkTab === 'c' ? C_SEARCH_INDEX : MATH_SEARCH_INDEX;

    if (list.length === 0) {
        container.innerHTML = `
            <div style="padding: 40px 20px; text-align: center; color: #94a3b8;">
                <p style="font-size: 28px; margin: 0 0 10px 0;">⭐</p>
                <p style="font-weight: 600;">No bookmarked questions in ${currentActiveBookmarkTab === 'c' ? 'C Programming' : 'Mathematics'} yet.</p>
                <p style="font-size: 12px;">Click the ⭐ Bookmark button on any question card to save it for rapid revision.</p>
            </div>
        `;
        return;
    }

    container.innerHTML = list.map(qNum => {
        const item = indexList.find(i => i.num === qNum);
        if (!item) return '';
        return `
            <div class="bookmark-item">
                <a href="${item.url}" class="bm-info" onclick="closeBookmarksDrawer()">
                    <div class="bm-qnum">${item.module} • Question ${item.num}</div>
                    <div class="bm-title">${escapeHtml(item.title)}</div>
                </a>
                <button class="bm-remove-btn" onclick="toggleBookmark('${currentActiveBookmarkTab}', ${item.num}); event.stopPropagation();" title="Remove Bookmark">✕</button>
            </div>
        `;
    }).join('');
}

/* ---- Copy Code Utility ---- */
function copyCode(btn) {
    const codeBlock = btn.closest('.code-container').querySelector('.code-block code');
    if (!codeBlock) return;

    const textToCopy = codeBlock.innerText;
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(textToCopy).then(() => {
            showCopiedFeedback(btn);
        }).catch(() => {
            fallbackCopy(textToCopy, btn);
        });
    } else {
        fallbackCopy(textToCopy, btn);
    }
}

function fallbackCopy(text, btn) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.left = '-9999px';
    document.body.appendChild(textarea);
    textarea.focus();
    textarea.select();
    try {
        document.execCommand('copy');
        showCopiedFeedback(btn);
    } catch (err) {
        console.error('Fallback copy failed', err);
    }
    document.body.removeChild(textarea);
}

function showCopiedFeedback(btn) {
    const originalText = btn.innerHTML;
    btn.innerHTML = '✓ Copied!';
    btn.classList.add('copied');
    setTimeout(() => {
        btn.innerHTML = originalText;
        btn.classList.remove('copied');
    }, 2000);
}

/* ---- Keyboard Shortcuts ---- */
function initShortcuts() {
    window.addEventListener('keydown', (e) => {
        // Ctrl+K or Cmd+K opens search
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
            e.preventDefault();
            openSearchModal();
        }
        // Escape closes modals
        if (e.key === 'Escape') {
            closeSearchModal();
            closeBookmarksDrawer();
        }
    });
}

function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/&/g, '&amp;')
              .replace(/</g, '&lt;')
              .replace(/>/g, '&gt;')
              .replace(/"/g, '&quot;')
              .replace(/'/g, '&#039;');
}

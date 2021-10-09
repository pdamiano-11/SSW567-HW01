"""
Classifies three given sides into a type of triangle.
"""
def classify_triangle(side_a, side_b, side_c):
    """
    This function makes calculations on the three sides and return the triangle type as a string.
    """
    typ = 'None'
    if side_a == 0 or side_b == 0 or side_c == 0:
        return typ
    if side_a * side_b * side_c == side_a ** 3:
        typ = 'Equilateral'
    elif ((side_a == side_b and side_b != side_c) or
          (side_b == side_c and side_c != side_a) or
          (side_a == side_c and side_c != side_b)):
        typ = 'Isoceles'
    else:
        typ = 'Scalene'
    if side_a ** 2 + side_b ** 2 == round(side_c ** 2):
        typ += ' Right'
    return typ

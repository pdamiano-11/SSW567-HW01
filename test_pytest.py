"""
This testing file tests the triangle567.py file's triangle classifier.
"""

import math
import triangle567

def test_lengths():
    """
    This function solely tests for if the given numbers constitute any triangle of equilateral,
    isoceles, and scalene.
    """
    assert triangle567.classify_triangle(3, 3, 3) == "Equilateral"
    assert triangle567.classify_triangle(4, 4, 7) == "Isoceles"
    assert triangle567.classify_triangle(2, 7, 6) == "Scalene"

    assert triangle567.classify_triangle(0, 0, 0) != "Equilateral"
    assert triangle567.classify_triangle(0, 4, 0) != "Isoceles"
    assert triangle567.classify_triangle(3, 4, 3) != "Scalene"

def test_right():
    """
    This function tests for the 'right' keyword being added to a triangle definition to denote
    a right triangle.
    """
    assert triangle567.classify_triangle(3, 3, 3*math.sqrt(2)) == "Isoceles Right"
    assert triangle567.classify_triangle(3, 4, 5) == "Scalene Right"

    assert triangle567.classify_triangle(0, 0, 0) != "Right"
    assert triangle567.classify_triangle(3, 3, 3) != "Equilateral Right"
    assert triangle567.classify_triangle(6, 6, 7) != "Isoceles Right"
    assert triangle567.classify_triangle(6, 10, 8) != "Scalene Right"

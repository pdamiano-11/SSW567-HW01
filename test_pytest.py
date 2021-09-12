import SSW567_HW_01
import math

def test_lengths():
    assert SSW567_HW_01.classifyTriangle(3, 3, 3) == "Equilateral"
    assert SSW567_HW_01.classifyTriangle(4, 4, 7) == "Isoceles"
    assert SSW567_HW_01.classifyTriangle(2, 7, 6) == "Scalene"

    assert SSW567_HW_01.classifyTriangle(0, 0, 0) != "Equilateral"
    assert SSW567_HW_01.classifyTriangle(0, 4, 0) != "Isoceles"
    assert SSW567_HW_01.classifyTriangle(3, 4, 3) != "Scalene"

def test_right():
    assert SSW567_HW_01.classifyTriangle(3, 3, 3*math.sqrt(2)) == "Isoceles Right"
    assert SSW567_HW_01.classifyTriangle(3, 4, 5) == "Scalene Right"

    assert SSW567_HW_01.classifyTriangle(0, 0, 0) != "Right"
    assert SSW567_HW_01.classifyTriangle(3, 3, 3) != "Equilateral Right"
    assert SSW567_HW_01.classifyTriangle(6, 6, 7) != "Isoceles Right"
    assert SSW567_HW_01.classifyTriangle(6, 10, 8) != "Scalene Right"
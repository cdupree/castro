import unittest

import math
from castro_math import *

# special angles
# (angle, sin, cos, tan)
special_angles = [(0, 0, 1, 0), 
                  (30, 0.5, 0.8660254037844386, 0.5773502691896258),
                  (45, 0.7071067811865476, 0.7071067811865476, 1), 
                  (60, 0.8660254037844386, .5, 1.7320508075688772 ), 
                  (90, 1, 0, math.tan(math.pi/2))]
 
class TestCastroMath(unittest.TestCase):

    def test_sin_quad1(self):
        for angle in special_angles:
            self.assertAlmostEqual(angle[1], SN(angle[0]))

    def test_cos_quad1(self):
        for angle in special_angles:
            self.assertAlmostEqual(angle[2], CS(angle[0]))

    def test_tan_quad1(self):
        for angle in special_angles:
            self.assertAlmostEqual(angle[3], TN(angle[0]))

    # in quadrant II, sin should remain positive, while cos becomes negative, making tan negative
    # also for this quadrant the angles work out so that sin(theta) = sin(180 - theta); eg,
    # sin(30) = sin(150). Ditto for cos and tan with of course sign changes.  Ie, if we imagine
    # sweep a line from 0 to theta, and then dropping a vertical from that line to the x-axis,
    # then that new angle is the angle that we should use to find our trig functions.
    def test_sin_quad2(self):
        for angle in special_angles:
            self.assertAlmostEqual(angle[1], SN(180 - angle[0]))

    def test_cos_quad2(self):
        for angle in special_angles:
            self.assertAlmostEqual(-1 * angle[2], CS(180 - angle[0] ))

    #def test_tan_quad2(self):
    #    for angle in special_angles:
    #        self.assertAlmostEqual(-1 * angle[3], TN(180 - angle[0]))

    # in quadrant III, sin and cos are negative, while tan is positive.
    # here the relation is sin(theta) = sin(180+theta)
    def test_sin_quad3(self):
        for angle in special_angles:
            self.assertAlmostEqual(-1 * angle[1], SN(angle[0] + 180))

    def test_cos_quad3(self):
        for angle in special_angles:
            self.assertAlmostEqual(-1 * angle[2], CS(angle[0] + 180))

    #def test_tan_quad3(self):
    #    for angle in special_angles:
    #        self.assertAlmostEqual(angle[3], TN(angle[0] + 180))

    # in quadrant IV, sin is negative, cos is positive, and tan is negative
    def test_sin_quad4(self):
        for angle in special_angles:
            self.assertAlmostEqual(-1 * angle[1], SN(360 - angle[0]))

    def test_cos_quad4(self):
        for angle in special_angles:
            self.assertAlmostEqual(angle[2], CS(360 - angle[0]))

#    def test_tan_quad4(self):
#        for angle in special_angles:
#            self.assertAlmostEqual(-1 * angle[3], TN(360 - angle[0]))

    def test_cubr_0(self):
        self.assertEqual(0, CUBR(0))

    def test_cubr_8(self):
        self.assertEqual(2, CUBR(8))

    def test_cubr_1069(self):
        self.assertAlmostEqual(1069, math.pow(CUBR(1069),3))

# FIXME: Need to work on tests for tan in non-quadrant 1.
# FIXME: Need tests for inverse trig.
 

if __name__ == '__main__':
    unittest.main()

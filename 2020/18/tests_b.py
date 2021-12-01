import unittest

generate_new_equation = __import__("18b").generate_new_equation

class Test(unittest.TestCase):
    def test_1(self):
        """ First test equation """
        equ = "1 + 2 * 3 + 4 * 5 + 6"
        new_equation = generate_new_equation(equ)
        self.assertEqual(eval(new_equation), 231)

    def test_2(self):
        """ Second test equation """
        equ = "1 + (2 * 3) + (4 * (5 + 6))"
        new_equation = generate_new_equation(equ)
        self.assertEqual(eval(new_equation), 51)

    def test_3(self):
        """ Third test equation """
        equ = "2 * 3 + (4 * 5)"
        new_equation = generate_new_equation(equ)
        self.assertEqual(eval(new_equation), 46)

    def test_4(self):
        """ Fourth test equation """
        equ = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
        new_equation = generate_new_equation(equ)
        self.assertEqual(eval(new_equation), 1445)

    def test_5(self):
        """ Fifth test equation """
        equ = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
        new_equation = generate_new_equation(equ)
        self.assertEqual(eval(new_equation), 669060)

    def test_6(self):
        """ Sixth test equation """
        equ = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
        new_equation = generate_new_equation(equ)
        self.assertEqual(eval(new_equation), 23340)

if __name__ == "__main__":
    unittest.main()
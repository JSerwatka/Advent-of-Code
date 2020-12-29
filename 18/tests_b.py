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

    # def test_7(self):
    #     """ 1 normal equation """
    #     equ = "2 * 9 + 5 + ((8 + 6 + 5) * (2 + 3 * 9 + 3) + 5) * (7 + 9 + 7 + 3 * 7) * 5"
    #     new_equation = generate_new_equation(equ)
    #     self.assertEqual(eval(new_equation), 855400)

    # def test_8(self):
    #     """ 2 normal equation """
    #     equ = "7 + (2 + 8 * 8 * 2 + (4 * 3 * 9 + 4 * 4)) + 4 * 3"
    #     new_equation = generate_new_equation(equ)
    #     self.assertEqual(eval(new_equation), 1857)

    # def test_9(self):
    #     """ 3 normal equation """
    #     equ = "6 + 9 * 2 * 2 + (2 + (7 * 6 * 6) + 4 * (7 * 8 * 2 + 4) * 7) + 7"
    #     new_equation = generate_new_equation(equ)
    #     self.assertEqual(eval(new_equation), 209563)

    # def test_10(self):
    #     """ 4 normal equation """
    #     equ = "2 + ((3 * 6 * 5 * 4 + 7 * 7) + 5 * 4 * 5 * (8 * 7 + 9) + 8) * (4 + 6 * 5)"
    #     new_equation = generate_new_equation(equ)
    #     self.assertEqual(eval(new_equation), 167310500)

    # def test_11(self):
    #     """ 5 normal equation """
    #     equ = "(7 * 6 * 3 + 4 * 3 * 9) + (6 * 6 * (4 + 6 + 4) + 7 + 2 + (9 * 8 * 9 + 9 * 7 * 4)) + (3 * 4 + 3 + 2) * 8"
    #     new_equation = generate_new_equation(equ)
    #     self.assertEqual(eval(new_equation), 179488)

    # def test_12(self):
    #     """ 6 normal equation """
    #     equ = "(3 + (7 * 7 + 9 * 9 * 6)) * 3 * 5 + 4 * 8"
    #     new_equation = generate_new_equation(equ)
    #     self.assertEqual(eval(new_equation), 376232)

    # def test_13(self):
    #     """ 7 normal equation """
    #     equ = "8 + 9 * (2 + 2 * 5 + 9 * 2) * 2 + ((6 + 4) * 4 + (4 * 7 + 3 * 3 + 7) * (4 * 5 + 8 + 8 + 7 * 6) + (6 + 2) + 5)"
    #     new_equation = generate_new_equation(equ)
    #     self.assertEqual(eval(new_equation), 38105)

    # def test_14(self):
    #     """ 8 normal equation """
    #     equ = "(2 + 2 * 9 * 7) * ((9 + 8) * 3 * 6 + 6 + (5 * 4 * 4 * 3)) + 9 + (3 + 2)"
    #     new_equation = generate_new_equation(equ)
    #     self.assertEqual(eval(new_equation), 139118)

    # def test_15(self):
    #     """ 9 normal equation """
    #     equ = "2 + 7 * 3 + ((7 + 7 * 3) * 6 + 8)"
    #     new_equation = generate_new_equation(equ)
    #     self.assertEqual(eval(new_equation), 287)

    # def test_16(self):
    #     """ 10 normal equation """
    #     equ = "2 + 7 + 6 + (4 + 7 * 7) + 9 * 2"
    #     new_equation = generate_new_equation(equ)
    #     self.assertEqual(eval(new_equation), 202)

if __name__ == "__main__":
    unittest.main()
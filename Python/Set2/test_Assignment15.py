import unittest
import Assignment15

class Testclass(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Assignment15.calc.add(10,5),15)
        self.assertEqual(Assignment15.calc.add(-5,10),5)
        self.assertEqual(Assignment15.calc.add(-4,3),-1)
        self.assertEqual(Assignment15.calc.add(9,91),100)



    def test_div(self):
        self.assertEqual(Assignment15.calc.div(10,5),2)
        self.assertEqual(Assignment15.calc.div(10,10),1)
        self.assertEqual(Assignment15.calc.div(40,4),10)
        self.assertEqual(Assignment15.calc.div(90,9),10)
        self.assertRaises(ZeroDivisionError,Assignment15.calc.div,1,0)


    def test_mul(self):
        self.assertEqual(Assignment15.calc.mul(10,5),50)
        self.assertEqual(Assignment15.calc.mul(-5,10),-50)
        self.assertEqual(Assignment15.calc.mul(-4,3),-12)
        self.assertEqual(Assignment15.calc.mul(9,11),99)

    def test_sub(self):
        self.assertEqual(Assignment15.calc.sub(10,5),5)
        self.assertEqual(Assignment15.calc.sub(-5,10),-15)
        self.assertEqual(Assignment15.calc.sub(-4,3),-7)
        self.assertEqual(Assignment15.calc.sub(9,91),-82)


if __name__=='__main__':
    unittest.main()


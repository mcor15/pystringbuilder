
import unittest
from pystringbuilder import StringBuilder


class TestStringBuilderMethods(unittest.TestCase):

    def test_ensureCapacity(self):
        sb = StringBuilder()
        sb.ensureCapacity(32)
        self.assertTrue(sb._StringBuilder__capacity == 32)#Name mangling

    def test_ensureCapacityDoesNotChange(self):
        sb = StringBuilder()
        sb.ensureCapacity(16)
        self.assertTrue(sb._StringBuilder__capacity == 16)#Name mangling

    def test_append(self):
        sb = StringBuilder("abc")
        sb.append("xyz")
        self.assertEquals(sb.length(), 6)

    def test_append(self):
        sb = StringBuilder("a")
        sb.append(12)
        self.assertTrue(str(sb) == "a12")

    def test_LargerLength(self):
        sb = StringBuilder(init_capacity=5)
        sb.setLength(10)
        self.assertTrue(sb._StringBuilder__capacity == 10 and sb.length()==10)

    def test_LargerLengthSmallString(self):
        sb = StringBuilder("string")
        sb.setLength(6)
        self.assertTrue(sb._StringBuilder__capacity == 16 and sb.length()==6)

    def test_SmallerLength(self):
        sb = StringBuilder("abcd")
        sb.setLength(2)
        self.assertTrue(sb._StringBuilder__capacity == 2 and str(sb) == "ab" and sb.length() == 2)

    def test_LargerLengthAddedNulls(self):
        sb = StringBuilder(init_capacity=5)
        sb.setLength(10)
        for c in sb._StringBuilder__string_list:
            with self.subTest():
                self.assertEqual(c, None)

    def test_RemoveEmptyStringBuilder(self):
        sb = StringBuilder()
        with self.assertRaises(IndexError):
            sb.deleteCharAt(0)

    def test_ToString(self):
        sb = StringBuilder ("Black Lotus")
        self.assertTrue(sb.toString() == "Black Lotus")


    def test_Delete_Chars(self):
        sb = StringBuilder ("abcxyz")
        sb.delete(1,4)
        self.assertEqual(sb.toString(), "az")

    def test_Delete_All(self):
        sb = StringBuilder ("abcxyz")
        sb.delete(0,5)
        self.assertEqual(sb.toString(), "")

    def test_Delete_Out_Of_Bounds_End(self):
        sb = StringBuilder ("abcxyz")
        with self.assertRaises(IndexError):
            sb.delete(0, 6)

    def test_Delete_Start_And_End_Consecutive(self):
        sb = StringBuilder ("abcxyz")
        with self.assertRaises(ValueError):
            sb.delete(3, 2)


        
if __name__ == '__main__':
    unittest.main()
# program to classify_triangle()
import unittest
import datetime

def my_brand(assignmentName):
    myName = "=*=*=*= Ajay Kundu =*=*=*="
    course = "=*=*=*= Course 2023S-SSW567-WS =*=*=*="
    assignmentName = "=*=*=*= "+ assignmentName +" =*=*=*="
    dateTime = "=*=*=*= "+ str(datetime.datetime.now()) +" =*=*=*="
    print(myName + "\n" + course + "\n" + assignmentName + "\n" + dateTime)
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\n")
assignmentName = "HW 01-Testing triangle classification"

def classifyTriangle(a, b, c):
    if a == b and b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
        return 'Right'
    elif a != b and b != c:
        return 'Scalene'
    else:
        return 'NotATriangle'


def runClassifyTriange(a, b, c):
    print(classifyTriangle(a, b, c))


class TestTriangle(unittest.TestCase):
    def testSet1(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral')
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral')
        self.assertEqual(classifyTriangle(20, 20, 20), 'Equilateral')

    def testSet2(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles')
        self.assertEqual(classifyTriangle(1, 3, 3), 'Isosceles')
        self.assertEqual(classifyTriangle(4, 2, 4), 'Isosceles')

    def testSet3(self):
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right')
        self.assertEqual(classifyTriangle(12, 5, 13), 'Right')
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testSet4(self):
        self.assertEqual(classifyTriangle(7, 8, 9), 'Scalene')
        self.assertEqual(classifyTriangle(9, 10, 12), 'Scalene')
        self.assertEqual(classifyTriangle(6, 7, 8), 'Scalene')



if __name__ == '__main__':
    
    my_brand(assignmentName)
    runClassifyTriange(2, 3, 4)
    runClassifyTriange(3, 4, 5)
    unittest.main()

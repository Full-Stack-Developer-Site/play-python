import unittest
from name_function import get_formatted_name as get_name

# 要为函数编写测试用例，可先导入模块unittest和要测试的函数，
# 再创建一个继承unittest.TestCase的类，并编写一系列方法对函数行为的不同方面进行测试。
class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_name('Richie', 'Zhu')
        self.assertEqual(formatted_name, 'Richie Zhu')

    def test_first_last_middle_name(self):
        formatted_name = get_name("Richie", "Zhu", "CL")
        self.assertEqual(formatted_name, "Richie Cl Zhu")

# 注意：这个和test class 平级
# __name__，这个变量是在程序执行时设置的。
# 如果这个文件作为主程序执行，变量__name__将被设置为'__main__'
# 如果这个文件被测试框架导入，变量__name__的值将不是'__main__'，因此不会调用unittest.main()。
if __name__ == '__main__':
    print(__name__)
    unittest.main()
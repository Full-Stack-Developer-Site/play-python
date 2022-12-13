import unittest
from survey import AnonymousServey

class TestAnonymousSurvey(unittest.TestCase):

    # -> 函数注释 - Function Annotations
    # 函数注释包括：
    # 参数注释：以冒号（:）标记
    # 返回值注释：以 -> 标记
    def setUp(self) -> None:
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousServey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_reponse(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_reponse(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


# 注意：这个和test class 平级
if __name__ == '__main__':
    unittest.main()
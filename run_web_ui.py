import os

import pytest

if __name__ == '__main__':
    pytest.main(['--alluredir', './result', '-W', 'ignore:Module already imported:pytest.PytestWarning', 'test_answerquestion.py'])
    os.system("allure generate ./result/ -o /gyhlw/output/report/ --clean")

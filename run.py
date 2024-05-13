import os

import pytest


class RunPytest:
    @staticmethod
    def run():
        BASE_DIR=os.path.dirname(os.path.abspath(__file__))
        PRPORE_JSON_DIR = os.path.join(BASE_DIR, "output", "report_json")
        CASE_DIR = os.path.join(BASE_DIR, "case/touzi", )
        PRPORE_ALLURE_DIR = os.path.join(BASE_DIR, "output", "report_allure")

        #pytest.main(['-v','--alluredir', f'{PRPORE_JSON_DIR}', f'{CASE_DIR}'])
        pytest.main(['-v','--count=2','--alluredir', f'{PRPORE_JSON_DIR}', f'{CASE_DIR}/test_lixiangbeian.py'])
        os.system(f'allure generate {PRPORE_JSON_DIR} -o {PRPORE_ALLURE_DIR} --clean')

if __name__ == '__main__':
    RunPytest().run()
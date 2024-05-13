import os

from config.pathconf import BASE_DIR
from public.myreaddata import GetYaml


def test_readyaml():

    data1=GetYaml()
    data=data1.readdata()
    if data!=None:
        for i in data:
            print(i)
    else:
        print('数据为空')
if __name__ == '__main__':
    test_readyaml()
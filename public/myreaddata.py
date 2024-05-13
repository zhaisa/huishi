import os

import yaml
import xlrd
from xlrd import open_workbook

from config.pathconf import CASEYMAL_DIR


class GetYaml:
    #这是类的私有化属性
    def __init__(self,yaml_name):
        self.yamal_name=os.path.basename(__file__).replace('py', 'yaml')

    def readdata(self,):
        _list=[]
        filepath=os.path.join(CASEYMAL_DIR,f"{self.yaml_name}")
        f = open(self.filepath, "r", encoding='utf-8')
        data = yaml.load(f, Loader=yaml.FullLoader)
        _list = data['testdata'][1:]  # 返回classes对应的value是一个列表
        f.close()
        return _list

class GetExcel:
    # def __init__(self,excel_name):
    #     self.excel_name=excel_name

    def readexcel(self,):
        _data=[]
        filepath = os.path.join(CASEYMAL_DIR, f"{self.excel_name}")
        workbook = open_workbook(filepath)
        s = workbook.sheet_by_name('Sheet1')
        title = s.row_values(0)  # 首行为title
        for col in range(1, s.nrows):  # 依次遍历其余行，与首行组成dict，拼到self._data中
                _data.append(dict(zip(title, s.row_values(col))))
        else:
            for col in range(0, s.nrows):  # 遍历所有行，拼到self._data中
                _data.append(s.row_values(col))

        return _data





if __name__ == '__main__':


    getdata=GetYaml()
    getdata.readdata()
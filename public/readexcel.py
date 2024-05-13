# 读取Excel 数据
import os

from xlrd import open_workbook

from public.common import ErrorExcep


class RedaExcel():
    """
    *xrld ==1.2.0
    读取excel文件中的内容。返回list。
    如：
    excel中内容为：
    | A  | B  | C  | x |
    | A1 | B1 | C1 | . |
    | A2 | B2 | C2 | . |

    默认输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    line=False输出结果：
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """

    def __init__(self, excel: str, sheet: int or str = 0, line: bool = True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)

            if type(self.sheet) not in [int, str]:
                raise ErrorExcep('sheet类型错误')
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)  # 首行为title
                for col in range(1, s.nrows):  # 依次遍历其余行，与首行组成dict，拼到self._data中
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):  # 遍历所有行，拼到self._data中
                    self._data.append(s.row_values(col))
        return self._data

if __name__ == '__main__':
    #mydata=RedaExcel("D:\gyhlw\\aaa.xlsx", sheet=1,line=False)
    mydata=RedaExcel("D:\gyhlw\\aaa.xlsx",sheet=1)
    print(mydata.data[1].values())
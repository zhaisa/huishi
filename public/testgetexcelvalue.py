from readexcel import RedaExcel
def getexcelvalue():
    data1=RedaExcel("D:\gyhlw\\aaa.xlsx",sheet=3)
    print(list(data1.data[1].values())[0])
    return data1.data

if __name__ == '__main__':
    getexcelvalue()
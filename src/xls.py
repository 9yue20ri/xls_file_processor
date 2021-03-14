#coding=utf-8
import xlrd
# date=xlrd.open_workbook("1.xlsx")
# sheet=date.sheet_by_index(0)
# c=sheet.col_values(4)#返回该列所有单元格的value组成的列表
# print(c)
# b=sheet.col_values(0)#返回ip
# a=sheet.col_values(1)#返回端口
# f=open('url.txt','r')
# sourceInLine = f.readlines()
# dataset = []
# for line in sourceInLine:
#     temp1 = line.strip('\n')
#     temp2 = temp1.split('\t')
#     dataset.append(temp2)
# print(dataset[0])
# i=-1
# j=-1
# z=-1
import re

def search(cve):
    with open('result.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line1 = line.strip()
            cve=cve
            r = re.findall(r'.+CVE-2016-2183', line1)
            for i in r:
                m = set(i)

# while i<9589:
#     i+=1
#     j+=1
#     z+=1
#     ip=b[i]
#     port=a[j]
#     cve=c[z]
#     # print(str(ip) + ':' + str(port) + str(cve))
if __name__ == '__main__':
    search =input('请输入CVE的编号')
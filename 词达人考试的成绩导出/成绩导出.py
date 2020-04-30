#json的格式  头尾 删除点东西    变成[{},{},{},{}]的样子
import xlwt,json
#定义一个打开文件的函数
print('输入json的文件名字')
s=input()
print('输入保存excel的文件名')
namd=input()
nam=namd+".xls"
def readJsonfile():
    a = json.load(open('D:\\桌面\\cidarenRestartTheProject\\'+s+'.json', 'r', encoding='UTF-8'))  #+s那块就是在路径下引用变量的方法
    jsobj = (a['data']['score_list'])
    return jsobj

def jsonToexcel():
    jsonfile = readJsonfile()
    print (jsonfile)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('student')#建立excel
    ll = list(jsonfile[0].keys())
    for i in range(0,len(ll)):
        sheet1.write(0,i,ll[i])#写第一行表头 
    for j in range(0,len(jsonfile)):#j是总的{}数量
        m = 0#m是列数
        ls = list(jsonfile[j].values())
        num=len(ls)     #不知道为啥有的人导出js之后缺了2列 对应不上  所以加了个if
        if num==15:
            for k in ls:
                sheet1.write(j+1,m,k)#写excel的函数，用法（行，列，值）
                m += 1
        if num==13:
            sheet1.write(j+1,0,ls[0])
            sheet1.write(j+1,1,ls[1])
            sheet1.write(j+1,2,ls[2])
            sheet1.write(j+1,3,ls[3])
            sheet1.write(j+1,4,ls[4])
            sheet1.write(j+1,5,ls[5])
            sheet1.write(j+1,6,ls[6])
            sheet1.write(j+1,7,ls[7])
            sheet1.write(j+1,8,ls[8])
            sheet1.write(j+1,9,0)
            sheet1.write(j+1,10,0)
            sheet1.write(j+1,11,ls[9])
            sheet1.write(j+1,12,ls[10])
            sheet1.write(j+1,13,ls[11])
            sheet1.write(j+1,14,ls[12])
    workbook.save(nam)
    
                  
jsonToexcel()

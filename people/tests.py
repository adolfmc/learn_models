from django.test import TestCase
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'learn_models.settings'
import sys
import xlrd
import django
django.setup()

from people.models import Perduct



def file_name(file_dir):
    PerductList=[]

    for root, dirs, files in os.walk(file_dir):
        #print(root)  # 当前目录路径
        #print(dirs)  # 当前路径下所有子目录
        #print( len( files ) )  # 当前路径下所有非目录子文件

        for i in range ( len( files ) ):
            file_path_name = file_dir + '\\' +files[i]
            if file_path_name.find(".doc")==-1:
                #print (file_path_name)
                try:
                    excel_save(file_path_name)
                except Exception as e:
                    print (e)

            #break
    #Perduct.objects.bulk_create(PerductList)
    #print (PerductList)
def excel_save(file_path_name):

    #print('=========================================================================')
    #path = r'C:\Users\mc\PycharmProjects\hello_django\excelfile'
    #file = '财富多.xlsx'

    # 打开文件
    data = xlrd.open_workbook(file_path_name)
    # path + '/' +file 是文件的完整路径
    # 获取表格数目
    nums = len(data.sheets())
    for i in range(nums):
        # 根据sheet顺序打开sheet
        sheet1 = data.sheets()[i]

    # 根据sheet名称获取
    #sheet2 = data.sheet_by_name('工作')
    sheet2=data.sheets()[0]
    # 获取sheet（工作表）行（row）、列（col）数
    nrows = sheet2.nrows  # 行
    ncols = sheet2.ncols  # 列
    #print(nrows, ncols)

    if  nrows !=25 :
        return ;

    if ncols !=3:
        return ;

    # 循环行列表数据
    infos = []
    for i in range(nrows):
        #print(sheet2.row_values(i))
        vv = sheet2.row(i)[2].value
        if i>=23 and vv=='' and str(sheet2.row(i)[1].value).find("*") ==-1:
            #print (  sheet2.row(i)[1].value )
            values = str( sheet2.row(i)[1].value).replace("\n", "")
            infos.append( values)
        if i<23  :
            #print(sheet2.row(i)[2].value)
            values = str(sheet2.row(i)[2].value).replace("\n", "")
            infos.append(values)

    if len(infos )==25:
        #print ( len(infos )  ,file_path_name )
        print(infos[0], infos[1], infos[2], infos[3], infos[4], file_path_name)
        # Perduct.objects.get_or_create(s1=infos[0]
        #         , s2=infos[1]
        #         , s3=infos[2]
        #         , s4=infos[3]
        #         , s5=infos[4]
        #         , s6=infos[5]
        #         , s7=infos[6]
        #         , s8=infos[7]
        #         , s9=infos[8]
        #         , s10=infos[9]
        #         , s11=infos[10]
        #         , s12=infos[11]
        #         , s13=infos[12]
        #         , s14=infos[13]
        #         , s15=infos[14]
        #         , s16=infos[15]
        #         , s17=infos[16]
        #         , s18=infos[17]
        #         , s19=infos[18]
        #         , s20=infos[19]
        #         , s21=infos[20]
        #         , s22=infos[21]
        #         , s23=infos[22]
        #         , s24=infos[23]
        #         , s25=infos[24]
        #         )

    # 获取单元格数据
    # 1.cell（单元格）获取
    # cell_A1 = sheet2.cell(0, 0).value
    # print(cell_A1)
    # 2.使用行列索引

    cell_A2 = sheet2.row(0)[2].value

    # book = BookInfo()
    # book.btitle = '晓可自传'
    # book.bpub_date = date(2017, 6, 27)
    # book.save()
    #print(cell_A2)
    #print('=========================================================================')

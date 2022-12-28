# excel工具
# 合并、拆分
import xlrd
import xlwt
from pathlib import Path, PurePath


# 合并Excel
def merge_excel():
    # 指定要合并excel的路径
    src_path = "E:/PythonTest/src"
    # 指定合并完成的路径
    dst_file = "E:/PythonTest/dst/结果.xls"

    # 获取该目录下所有的xlsx格式文件
    p = Path(src_path)
    files = [x for x in p.iterdir() if PurePath(x).match('*.xls')]
    # 存放读取结果
    content = []

    # 准备写入文件表头
    table_header = ['员工姓名', '第一题', '第二题']
    read_excel_data(files, content)
    write_excel_data(dst_file, table_header, content)


def read_excel_data(files, content):
    # 对每个文件进行重复处理
    for file in files:
        # 用文件名作为每个用户的标识
        username = file.stem
        data = xlrd.open_workbook(file)
        table = data.sheets()[0]
        # 取得每一项的结果
        answer1 = table.cell_value(rowx=0, colx=0)
        answer2 = table.cell_value(rowx=0, colx=1)
        temp = f'{username},{answer1},{answer2}'
        # 合并为一行先存储起来
        content.append(temp.split(','))
        print(temp)


def write_excel_data(dst_file, table_header, content):
    workbooks = xlwt.Workbook(encoding='utf-8')
    sheet = workbooks.add_sheet("统计结果")
    # 写入表头
    write_excel_header(table_header, sheet)
    # 写入表体
    write_excel_body(content, sheet)
    # 保存最终结果
    workbooks.save(dst_file)


def write_excel_header(table_header, sheet):
    row = 0
    col = 0
    for cell_header in table_header:
        sheet.write(row, col, cell_header)
        col += 1


def write_excel_body(content, sheet):
    row = 0
    # 向下移动一行
    row += 1
    # 取出每一行内容
    for line in content:
        col = 0
        # 取出单元格内容
        for cell in line:
            # 写入内容
            sheet.write(row, col, cell)
            # 向右移动一个单元格
            col += 1
        # 向下移动以上
        row += 1


# 获取表头内容
def get_header(table):
    colMax = table.ncols
    header = table.row_values(rowx=0, start_colx=0, end_colx=colMax)
    print("表头", header)
    return header


# 拆分Excel
def split_excel():
    src_file = "E:/PythonTest/拆分目标.xls"
    dst_src = "E:/PythonTest/splitRes/"

    data = xlrd.open_workbook(src_file)
    table = data.sheets()[0]
    employer_number = table.nrows
    # print(employer_number)
    table_header = get_header(table)
    for line in range(1, employer_number):
        content = table.row_values(rowx=line, start_colx=0, end_colx=None)
        print(content)
        workbooks = xlwt.Workbook(encoding='utf-8')
        sheet = workbooks.add_sheet("统计")
        # 写入表头
        write_excel_header(table_header, sheet)
        # 写入内容
        row = 1
        col = 0
        for cell in content:
            sheet.write(row, col, cell)
            col += 1

        # 保存结果
        workbooks.save(dst_src + content[1] + ".xls")


if __name__ == '__main__':
    # merge_excel()
    split_excel()

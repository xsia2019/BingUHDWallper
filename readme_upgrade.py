# -*- coding: utf-8 -*-

import os
import datetime

# 列出文件信息
def list_file(path):
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                yield os.path.join(root, file)
    except Exception as e:
        print(e)


# 读取文件并添加信息
def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            content += '---' + '\n'
            return content
    except Exception as e:
        print(e)


# 写入文件
def write_file(file_name, content):
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(e)


# 取得上周的日期
def get_last_weekdays():
    """
    返回上周的日期
    """
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=today.weekday()+7)
    for i in range(7):
        yield (start_date + datetime.timedelta(days=i)).strftime('%Y%m%d')


if __name__ == '__main__':
    file_path = './BingUHD'
    file_name = 'readme_test.md'
    new_content = ''
    for file in list_file(file_path):
        for day in get_last_weekdays():
            if day in file:
                new_content += read_file(file)
            else:
                continue

    write_file(file_name, new_content)


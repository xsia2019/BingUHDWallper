# -*- coding: utf-8 -*-

import os


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


if __name__ == '__main__':
    file_path = './BingUHD'
    file_name = 'readme_test.md'
    new_content = ''
    for file in list_file(file_path):
        new_content += read_file(file)
    write_file(file_name, new_content)


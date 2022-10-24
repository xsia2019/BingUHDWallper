# 下载并存储Bing每日壁纸到指定位置
# 需要修改自定义目录 img_path
# 修改于 2022-02-15
# 作者：kinofgl@gmail.com
# 修改 img_path,

import os
import requests
import re


# 存放在本地电脑的地址，目录必须存在
# img_path = r'C:\Users\Michael\OneDrive\图片\Desktop\BingUHD'
img_path = r'/mnt/c/Users/Michael/OneDrive/图片/Desktop/BingUHD'

# bing图片地址
img_url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=ZH-CN'

try:
    # 得到bing图片信息
    response = requests.get(img_url)
    result = response.json()

    # 提取并得到图片地址
    url_prefix = "https://cn.bing.com"
    img_url = url_prefix + result["images"][0]["url"]

    # 提取中文标题和版权信息
    date = result["images"][0]["startdate"]
    title = result["images"][0]["title"]
    copyright = result["images"][0]["copyright"]
    chinese_name = date + '.' + title + '.' + copyright

except Exception as e:
    print('错误: 无法获取到图片地址，请检查网络连接' + '\n')

# 得到bing图片链接
img_url = img_url[0:img_url.find(".jpg") + 4]

# 设置bing图片分辨率, UDH, 1080x1920, 1920x1080, 1920x1200
resolution = 'UHD'
# 替换默认的1080图片为UHD图片链接
img_url = img_url.replace("1920x1080", resolution)

# 取得Bing壁纸原始文件名
img_name = re.search('(?<=id=).*', img_url)
basename = img_name.group()

# 自定义图片名称，用.来代替其它符号
basename = chinese_name + basename
specialChars = ['，', '（', '）', '/', ' ', '_', ]
for char in specialChars:
    basename = basename.replace(char, '.')

# 拼接目录与文件名，得到图片路径
filepath = os.path.join(img_path, basename)

# 使用while循环来多次try和catch
max_num = 0
while max_num < 3:
    try:
        # 下载图片并重命名，并保存到文件夹中
        res = requests.get(img_url)
        with open(filepath, 'wb') as f:
            f.write(res.content)
        flag = 1

    except requests.exceptions.ConnectionError as e:
        print('错误：网络连接失败' + '\n', e, '\n')
        flag = 0
        max_num += 1

    except requests.exceptions.Timeout as e:
        print('错误：连接超时' + '\n', e, '\n')
        flag = 0
        max_num += 1

    except requests.exceptions.HTTPError as e:
        print('错误：非法的HTTP请求' + '\n', e, '\n')
        flag = 0
        max_num += 1

    except requests.exceptions.RequestException as e:
        print('错误：其他错误' + '\n', e, '\n')
        flag = 0
        max_num += 1

    else:
        print("保存", basename, "成功！", '\n')
        break
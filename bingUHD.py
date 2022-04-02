# 下载并存储Bing每日壁纸到指定位置
# 修改于 2022-04-02
# 作者：kinofgl@gmail.com

import os
import requests


class BingUHD(object):

    def __init__(self):
        # 默认bing图片查询地址
        self.url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=ZH-CN'
        self.path = './BingUHDWallpaper/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.132 Safari/537.36'
        }
        self.resolution = 'UHD'

    def get_img_info(self):
        try:
            # 获取图片信息
            result = requests.get(self.url, headers=self.headers).json()

            # 提取图片地址
            raw_img_url = 'https://cn.bing.com' + result['images'][0]['url']
            # 得到默认图片链接
            normal_img_url = raw_img_url[0:raw_img_url.find(".jpg") + 4]
            # 得到UHD图片链接替换默认的 1080 图片为UHD图片链接
            uhd_img_url = normal_img_url.replace("1920x1080", self.resolution)

            # 提取中文标题和版权信息
            date = result["images"][0]["startdate"]
            title = result["images"][0]["title"]
            copy_right = result["images"][0]["copyright"]

            return normal_img_url, uhd_img_url, date, title, copy_right

        except Exception as e:
            print('错误: 无法获取到图片地址，请检查网络连接' + '\n')

    def get_today_img(self):
        try:
            info = self.get_img_info()
            normal_url = info[0]
            uhd_url = info[1]
            date = info[2]
            title = info[3]
            copy_right= info[4]

            # 图片分辨率文字
            normal = normal_url[(normal_url.rfind("_") + 1): -4]
            uhd = uhd_url[(uhd_url.rfind("_") + 1): -4]

            # 标题
            title_md = '### ' + title + '\n\n'
            # 日期
            date_md = '日期：' + date[0:4] + '-' + date[4:6] + '-' + date[6:8] + '\n\n'
            # 说明
            description_md = copy_right + '\n\n'
            # 下载链接
            download_url = '**下载**  |  [1920x1080]  |  [UHD]' + '\n\n'
            # 图片缓存
            img_cache = '![' + title + '](' + normal_url + ' "' + copy_right + '"' + ')' + '\n\n'
            # 引用
            preference = '[//]: # (download links)' + '\n\n'
            pref_normal = '[' + normal + ']: <' + normal_url + '>' + '\n\n'
            pref_uhd = '[' + uhd + ']: <' + uhd_url + '>' + '\n\n'

            content_md = title_md + date_md + description_md + download_url + img_cache + preference + pref_normal + pref_uhd

            return content_md

        except Exception as e:
            print('错误: 无法获取到图片信息，请检查网络连接' + '\n')

    def get_file_name(self):
        try:
            info = self.get_img_info()
            # 定义文件夹
            file_path = self.path + info[2][0:4] + '-' + info[2][4:6] + '/'
            # 判断文件夹是否存在
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            # 定义文件名
            copy_right = info[4]
            copy_right = copy_right[0:copy_right.find(' ')]
            # 绝对路径
            name = info[2] + '.' + info[3] + '.' + copy_right + '.md'
            full_name = file_path + name

            return name
        except Exception as e:
            print('错误: 无法获取到图片信息，请检查网络连接' + '\n')


if __name__ == "__main__":
    bing = BingUHD()
    file_name = bing.get_file_name()

    with open(file_name, 'w') as f:
        content = bing.get_today_img()
        f.write(content)
        f.close()
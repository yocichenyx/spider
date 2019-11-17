# spider
> spider for maoyan and douban website.

用于爬取猫眼电影top100榜单、豆瓣读书某类书籍具体信息、meizi.info网站图片 的python爬虫程序，持续更新中。

## File structure
> spider code

    |->spider_bookSRC.py : 从豆瓣某书籍类型页面中，爬取所有书籍链接
    Note: 替换URL，即可使用。

    |->spider_bookInfo.py: 从单个书籍页面当中，爬取书籍信息
    Note: 替换SRC存储文件，即可使用。

    |->spider_MaoyanTop100.py: 爬取猫眼电影Top100榜单种电影的信息
    Note: 替换URL，即可使用。

    |->spider_meizi.info_img.py: 从meizi.info单个页面当中，爬取图片
    Note: 替换URL、给出存储文件，即可使用。

> book data

    |->computer_books_info.xlsx : 计算机编程类书籍具体信息 （2000条）
    |->computer_books_src.xlsx : 计算机编程类书籍链接 （2000条）

    |->masterpiece_books_info.xlsx : 名著类书籍具体信息 （1000条）
    |->masterpiece_books_info.xlsx : 名著类书籍链接 （1000条）

    |->novel_books_info.xlsx : 小说类书籍具体信息（1000条）
    |->novel_books_info.xlsx : 小说类书籍链接（1000条）

    |->photos|->: 爬取的meizi.info网站单个页面的meizi图片结果实例

## Import module
    re
    time
    random
    requests  (need install)
    bs4       (need install)
    lxml      (need install)
    openpyxl  (need install)

## Related blog
- [python 爬取猫眼电影top100数据](https://www.cnblogs.com/yocichen/p/11812637.html)

+ [python 爬取豆瓣书籍信息](https://www.cnblogs.com/yocichen/p/11847478.html)

By yocichen 2019/11/17
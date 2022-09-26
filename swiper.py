# -*- encoding=utf8 -*-
__author__ = "yuanjiawei"

from airtest.core.api import *
auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

import random

# 打开搜索页面
poco("com.xingin.xhs:id/f5m").click()

def do_swiper(keyword):

    # 输入搜索关键字
    poco("com.xingin.xhs:id/df4").set_text(keyword)
    # 点击搜索按钮
    poco("com.xingin.xhs:id/df9").click()

    swipe = True
    while swipe:
        if poco("com.xingin.xhs:id/d84").exists() and poco("com.xingin.xhs:id/d84").get_text() == "没有找到相关内容 换个词试试吧":
            print("关键词「%s」搜索到任何没有内容...." % keyword)
            break

        # 向下滑动
        poco.swipe([0.5, 0.8], [0.5, 0.2], duration=random.random())
        sleep(1)

        need_reload = poco(name="com.xingin.xhs:id/d87").exists()
        if need_reload:
            poco(name="com.xingin.xhs:id/d87").click()

        # 判断底部
        if poco(name="com.xingin.xhs:id/css").exists() and (poco(name="com.xingin.xhs:id/css").get_text() == '无更多内容'):
                print("「%s」无更多内容, 停止滑动" % keyword)
                swipe = False

# 定义需要搜索的关键字
need_search_keyword = [
    "塞尔达传说-王国之泪",
    "艾尔登法环",
]

for keyword in need_search_keyword:
    print("-----开始-----搜索「%s」的内容" % keyword)
    do_swiper(keyword)
    print("搜索「%s」-----结束-----" % keyword)

    # 点击手机的「返回上一层」
    keyevent("BACK")






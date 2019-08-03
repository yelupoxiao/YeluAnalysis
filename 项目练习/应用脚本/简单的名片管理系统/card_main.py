#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
名片管理系统的基本功能：

（1）新增名片；

（2）显示所有名片；

（3）搜索指定名片，并做出相应的修改。
"""
# 导入card_tools
import card_tools

while True:
    # 显示功能菜单
    card_tools.show_menu()

    # 获取用户输入内容
    user_input = input("请选择您要进行的操作:")

    # 判断用户输入内容
    if user_input in ['1', '2', '3']:
        if user_input == '1':
            card_tools.new_cards()
        elif user_input == '2':
            card_tools.show_all()
        else:
            card_tools.search_card()
    elif user_input == '4':
        break
    else:
        print("您的操作有误0.0 请输入0-3的数字")

#!/usr/bin/python3
# -*- coding:utf-8 -*-

def show_menu():
    """
    显示功能菜单函数
    """
    print('*' * 50)
    print("欢迎来到名片管理系统")
    print('-' * 50)
    print("\t[1] 新增名片")
    print("\t[2] 显示全部")
    print("\t[3] 查询名片")
    print("\t[4] 退出系统")
    print('*' * 50)


def make_tab():
    """
    打印表头
    """
    print("=" * 50)
    print("姓名\t\t年龄\t\t电话\t\t邮箱")
    print("-" * 50)


# 创建列表用于保存键值对
# 不能放到函数里面,不然每次新建名片内容都被覆盖了
card_list = []


def new_cards():
    """
    定义一个新建名片的函数,获取到用户输入的内容后,放入一个键值对当中,然后把键值对放入一个列表中
    """
    # 获取用户输入内容并用键值对保存
    name = input("请输入姓名:")
    age = input("请输入年龄:")
    tel = input("请输入电话:")
    email = input("请输入邮箱:")
    user_dict = {"name": name,
                 "age": age,
                 "tel": tel,
                 "email": email}
    # 把键值对放入列表中
    card_list.append(user_dict)


def show_all():
    """
    定义一个显示全部内容的函数,如果列表有信息就遍历,没有信息则提示用户输入

    """
    if len(card_list) != 0:
        make_tab()
        # 遍历列表得到用户信息字典
        for user_dict in card_list:
            # 得到用户各项信息的值(和表头对齐)
            print('{}\t\t{}\t\t{}\t\t{}'.format(user_dict['name'], user_dict['age'], user_dict['tel'],
                                                user_dict['email']))
            print("=" * 50)

    else:
        print("当前没有任何信息,请添加新增名片")


def search_card():
    """遍历card_list得到用户键值对,再把键值对中的name值与用户输入内容
    作比较,如果匹配到了则返回用户信息,如果没有匹配到则提示用户没搜到
    """
    find_name = input("请输入您要查找的姓名:")
    for key_value in card_list:
        if key_value["name"] == find_name:
            make_tab()
            print('{}\t\t{}\t\t{}\t\t{}'.format(key_value['name'], key_value['age'], key_value['tel'],
                                                key_value['email']))
            print("=" * 50)

            deal_card(key_value)
            break
        else:
            print("您所查找的名片不存在!")


def deal_card(key_value):
    """找到用户后,对名片进行修改或者删除操作
        key_valuie:在查找函数中,查找到的用户信息字典
    """
    user_input_str = input("请选择您要进行的操作: [1]修改名片 [2]删除名片 [0]返回上一层")
    if user_input_str == "1":
        # 修改名片
        key_value["name"] = user_input_info(key_value["name"], input("姓名"))
        key_value["age"] = user_input_info(key_value["age"], input("年龄"))
        key_value["tel"] = user_input_info(key_value["tel"], input("电话"))
        key_value["email"] = user_input_info(key_value["email"], input("邮箱"))
        print("修改成功!")

    elif user_input_str == "2":
        # 删除名片
        card_list.remove(key_value)
        print("删除成功!")


def user_input_info(dict_value, input_value):
    """
    判断用户输入的值,如果不是空则修改原值,否则返回原值
    :param dict_value: 字典中原有的值
    :param input_value: 用户输入的用于修改的值
    :return: 修改后的值
    """
    if len(input_value) == 0:
        return dict_value
    else:
        return input_value

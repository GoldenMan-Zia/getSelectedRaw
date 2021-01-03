#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2021/1/3 3:03 下午
# @Author    :goldenman
import os
import shutil

if __name__ == "__main__":
    run_code = 0

root_path = "/Users/goldenman/Desktop/12月广东"
# root_path = input("Please enter the root path (option + command + C):")
if root_path[-1] == "/":
    root_path = root_path[:-1]
jpg_path = root_path + "/jpg"
raw_path = root_path + "/raw"
selected_path = root_path + "/selected"
raw_suffix = ".ARW"


def check_path():
    path_ret = os.access(root_path, os.F_OK)
    if not path_ret:
        print("Wrong root path")
        return path_ret
    path_ret = os.access(jpg_path, os.F_OK)
    if not path_ret:
        print("Wrong jpg path")
        return path_ret
    path_ret = os.access(raw_path, os.F_OK)
    if not path_ret:
        print("Wrong raw path")
        return path_ret
    path_ret = os.access(selected_path, os.F_OK)
    if not path_ret:
        os.makedirs(selected_path)
    return path_ret


ret = check_path()
if not ret:
    exit(-1)
jpg_file_lists = os.listdir(jpg_path)
raw_file_lists = os.listdir(raw_path)
print(jpg_file_lists)
for jpg_file_whole_name in jpg_file_lists:
    jpg_file_name = jpg_file_whole_name.split(".")[0]
    try:
        index = raw_file_lists.index(jpg_file_name + raw_suffix)
        if index >= 0:
            shutil.copy(raw_path + "/" + raw_file_lists[index], selected_path)
            # print(raw_path+"/"+raw_file_lists[index])
    except ValueError as err:
        print("Handling run-time error:", err)

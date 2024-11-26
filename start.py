import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path)

import mdimgext

def get_files_with_extensions(folder_path, extensions):
    # 确保后缀以点号开头
    extensions = [ext if ext.startswith('.') else '.' + ext for ext in extensions]
    matching_files = []

    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件后缀是否在指定的后缀列表中
            if any(file.endswith(ext) for ext in extensions):
                # 构建完整的文件路径并添加到结果列表中
                matching_files.append(os.path.join(root, file))

    return matching_files

args = sys.argv

#正常启动时（参数只有本程序名称1个）启动GUI界面
if len(args) == 1:
    mdpath = str(input("path:"))
    mdimgext.process_markdown_file(mdpath)
    input("已完成，按任意键退出")

else:
    #参数大于1时，分隔参数至列表并且逐一下载
    _folder = args[1]
    mds = get_files_with_extensions(_folder, [".md"])
    for i in mds:
        print("正在处理：",str(i))
        mdimgext.process_markdown_file(str(i))
    input("已完成，按任意键退出")

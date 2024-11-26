import os
import shutil

def process_markdown_file(md_file_path):
    # 读取Markdown文件内容
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 获取文件所在目录
    directory = os.path.dirname(md_file_path)
    # 获取文件名（不带扩展名）
    file_name = os.path.splitext(os.path.basename(md_file_path))[0]

    # 创建同名文件夹用于存放图片
    new_dir = os.path.join(directory, file_name)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # 查找所有图片引用
    import re
    pattern = r'!\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, content)

    # 遍历所有图片引用
    for alt_text, img_path in matches:
        # 检查图片是否存在
        if not os.path.exists(img_path):
            print(f"图片 {img_path} 不存在。")
            continue

        # 复制图片到新文件夹
        new_img_path = os.path.join(new_dir, os.path.basename(img_path))
        shutil.copy(img_path, new_img_path)

        # 更新Markdown文件中的图片路径
        content = content.replace(img_path, os.path.join(file_name, os.path.basename(img_path)))

    # 将更新后的内容写回Markdown文件
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print("Markdown文件中的图片引用已更新。")

# 示例用法（请替换为实际的文件路径）
# process_markdown_file("C:\\path\\to\\your\\file.md")

# 注意：这里不执行函数，因为需要用户提供具体的文件路径。
if __name__ == '__main__':
    process_markdown_file("D:\\文档\\test\\PE系统与PECMD通俗讲义.md")

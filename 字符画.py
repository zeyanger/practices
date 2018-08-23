from PIL import Image
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type=int, default=80)  # 输出字符画宽度
parser.add_argument('--height', type=int, default=40)  # 输出字符画高度

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 获取参数
args = parser.parse_args()

IMG = args.file  # 输入文件
WIDTH = args.width  # 定义宽度变量
HEIGHT = args.height  # 定义高度变量
OUTPUT = args.output  # 定义输出


def get_char(r, g, b, alpha = 256):

    """将原文件的rgb格式转换成灰度格式再用字符表示"""

    if alpha == 0:
        return ' '
    char_lenght = len(ascii_char)
    gray = int(r * 0.299 + g * 0.587 + b * 0.114)

    unit = 256.0/char_lenght
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':

    # 打开图片并重置图片大小
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    # 打印出字符图片
    txt = ''
    for height in range(HEIGHT):
        for weight in range(WIDTH):
            txt += get_char(*im.getpixel((weight, height)))
        txt += '\n'

    print(txt)

    # 将字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)

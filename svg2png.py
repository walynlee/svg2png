import re
import cairosvg

# 读取原始 SVG 文件（确保是 UTF-8）
with open("svg-card.svg", "r", encoding="utf-8") as f:
    svg_data = f.read()

# 替换所有 font-family 声明，保留原来的语法格式，支持中英字体
svg_data = re.sub(
    r'font-family="[^"]+"',
    'font-family="Microsoft YaHei, SimHei, Arial, sans-serif"',
    svg_data
)

# 写入到新文件，确保 UTF-8 编码，不带 BOM
with open("tmp.svg", "w", encoding="utf-8") as f:
    f.write(svg_data)

# 转换为 PNG
cairosvg.svg2png(url="tmp.svg", write_to="output.png")

print("✅ SVG 转 PNG 完成，输出为 output.png")

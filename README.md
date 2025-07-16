# 🖼️ SVG to PNG 转换工具

这是一个基于 Python 的命令行小工具，支持将本地 `.svg` 文件快速转换为 `.png` 图片，解决中文字体乱码和 SVG 图层错位等问题。

---

## ✨ 功能特点

- ✅ 支持标准 SVG 渲染并输出高质量 PNG
- ✅ 自动替换字体，解决中文乱码问题
- ✅ 支持渐变、滤镜、icon 等复杂 SVG 元素
- ✅ 简洁易用，适合用于批量素材生成、图文设计等场景

---

## 🧩 依赖安装

建议使用 Python 3.7+ 的虚拟环境：

```bash
conda install -c conda-forge cairosvg
```

## 📁 项目结构示例

svg2png/
├── svg2png.py            # 主脚本
├── svg-card.svg             # 示例 SVG 文件
├── output.png            # 输出图片
└── README.md
🚀 使用方法
1️⃣ 单个文件转换
```bash
python svg2png.py
```
默认读取当前目录下的 svg-card.svg，输出为 output.png。

你可以根据需要扩展脚本支持批量转换或指定路径。

📷 效果展示
以下是 SVG 转 PNG 后的预览效果图：

## 示例展示
输入：
![输入SVG图](svg-card.svg)

输出：
![输出PNG图](output.png)



图片中的中文、渐变、icon 图标等均通过 Cairo 渲染完成，无错位无乱码。

⚠️ 注意事项
推荐 SVG 中使用如下字体组合，确保中文正常显示且跨平台兼容：
```xml
font-family="Microsoft YaHei, SimHei, Arial, sans-serif"
```
避免使用系统中不存在的字体（如 "PingFang SC"），否则 Cairo 渲染将出现空白或乱码。

若 SVG 含有非法字符（如 & 未转义），会导致解析失败，请确保文件格式正确。

请用 UTF-8 编码保存 SVG 文件，避免中文乱码或渲染出错。

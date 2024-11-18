from pdf2image import convert_from_path

# PDF 文件路径
pdf_path = '202410和平国际医院体检.pdf'

# 将 PDF 转换为图片
images = convert_from_path(pdf_path, dpi=150)

# 保存每一页为单独的图片
for i, image in enumerate(images):
    output_path = f'page_{i + 1}.png'
    image.save(output_path, 'PNG')

    print(f'Saved: {output_path}')
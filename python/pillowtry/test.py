from PIL import Image
import os, sys

# for f in os.listdir('.'):
#     if f.endswith('.gif'):
#         i = Image.open()

# image1 = Image.open('touxiang.ppm')
# image1.show()
#
# print(image1.format, image1.size, image1.mode)

# 批量转换图片格式  py .\test.py 1.gif touxiang.ppm
# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     outfile = f + ".jpg"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 if im.format == 'GIF':
#                     im = im.convert('RGB')
#                 im.save(outfile)
#         except IOError:
#             print("cannot convert", infile)


# size = (128, 128)
# # 批量生成缩略图
# for infile in sys.argv[1:]:
#     outfile = os.path.splitext(infile)[0] + "_thumbnail.jpg"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#
#                 if im.format == 'GIF':
#                     im = im.convert('RGB')
#                     im.thumbnail(size)
#                 im.save(outfile, "JPEG")
#                 print(im.format)
#
#         except OSError:
#             print("cannot create thumbnail for", infile)

# 批量查看图片信息
# for infile in sys.argv[1:]:
#     try:
#         with Image.open(infile) as im:
#             if im.format == 'GIF':
#                 im = im.convert('RGB')
#             print(infile, im.format, f"{im.size} x {im.mode}")
#     except OSError:
#         print("cannot open", infile)


image1 = Image.open('assets/touxiang.ppm')
box = (0, 0, 200, 200)
region = image1.crop(box)
region.show()
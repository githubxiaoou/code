from PIL import Image, ImageDraw, ImageEnhance
import imageio
import math

# 加载图片
background_path = "./assets/qrcode_for_gh.jpg"
output_gif_path = "dynamic_3d_background.gif"

# 打开背景图片
image = Image.open(background_path).convert("RGBA")
width, height = image.size

# 参数设置
num_frames = 50  # 动画帧数
parallax_distance = 20  # 视差移动的范围
light_radius = 100  # 光点半径
frames = []

# 创建动态帧
for i in range(num_frames):
    # 光影变化模拟
    frame = image.copy()
    draw = ImageDraw.Draw(frame)

    # 光影动态变化（正弦波控制亮度）
    brightness_factor = 1 + 0.2 * math.sin(i / num_frames * 2 * math.pi)  # 范围 1.0-1.2
    enhancer = ImageEnhance.Brightness(frame)
    frame = enhancer.enhance(brightness_factor)

    # 视差效果：背景上下轻微移动
    offset = int(parallax_distance * math.sin(i / num_frames * 2 * math.pi))  # 正弦波移动
    frame = frame.transform(
        (width, height),
        Image.AFFINE,
        (1, 0, 0, 0, 1, offset),  # Y 方向的平移
        resample=Image.BICUBIC,
    )

    # 添加动态光点（流动光）
    glow_x = int(width / 2 + math.sin(i / num_frames * 2 * math.pi) * width / 4)
    glow_y = int(height / 2 + math.cos(i / num_frames * 2 * math.pi) * height / 4)
    draw.ellipse(
        [glow_x - light_radius, glow_y - light_radius, glow_x + light_radius, glow_y + light_radius],
        fill=(255, 255, 255, 100),  # 白色光点，带透明度
    )

    frames.append(frame)

# 保存动图
frames[0].save(
    output_gif_path,
    save_all=True,
    append_images=frames[1:],
    duration=100,  # 每帧持续时间（毫秒）
    loop=0,  # 无限循环
)

print(f"立体感动态背景图已生成：{output_gif_path}")

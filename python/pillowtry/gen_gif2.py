from PIL import Image, ImageDraw
import imageio
import math

# 加载用户图片
input_image_path = "./assets/1_thumbnail.jpg"  # 上传的图片路径
output_gif_path = "assets/output_with_glow.gif"  # 输出动图路径

# 打开图片
image = Image.open(input_image_path).convert("RGBA")
width, height = image.size

# 设置亮点边框参数
num_frames = 30  # 动画的帧数
glow_radius = 10  # 亮点的半径
glow_color = (255, 255, 0, 255)  # 黄色亮点
border_distance = 20  # 亮点距离图片边框的距离

frames = []

# 创建每一帧
for frame_idx in range(num_frames):
    # 创建一层透明图层，绘制亮点
    frame = Image.new("RGBA", (width + 2 * border_distance, height + 2 * border_distance), (255, 255, 255, 0))
    draw = ImageDraw.Draw(frame)

    # 计算亮点的当前位置（圆形轨迹）
    angle = (frame_idx / num_frames) * 2 * math.pi  # 当前帧的角度
    x = width // 2 + border_distance + math.cos(angle) * (width // 2 + border_distance - glow_radius)
    y = height // 2 + border_distance + math.sin(angle) * (height // 2 + border_distance - glow_radius)

    # 绘制亮点
    draw.ellipse([x - glow_radius, y - glow_radius, x + glow_radius, y + glow_radius], fill=glow_color)

    # 合并图片和亮点
    frame.paste(image, (border_distance, border_distance), mask=image)
    frames.append(frame)

# 保存为动图
frames[0].save(
    output_gif_path,
    save_all=True,
    append_images=frames[1:],
    duration=100,  # 每帧显示时间（毫秒）
    loop=0  # 无限循环
)

print(f"动态图片生成成功：{output_gif_path}")

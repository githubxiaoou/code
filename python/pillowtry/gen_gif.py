from PIL import Image, ImageDraw
import imageio

# 创建每一帧
frames = []
for i in range(10):
    # 创建一个 200x200 的空白图像
    img = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(img)

    # 绘制一个动态的圆
    draw.ellipse([i * 10, i * 10, 100 + i * 10, 100 + i * 10], fill="blue", outline="black")

    # 保存帧
    frames.append(img)

# 将帧保存为 GIF 动图
frames[0].save(
    "output.gif",
    save_all=True,
    append_images=frames[1:],
    duration=100,  # 每帧持续时间（毫秒）
    loop=0  # 动画循环次数（0 表示无限循环）
)

print("GIF 动图生成成功：output.gif")

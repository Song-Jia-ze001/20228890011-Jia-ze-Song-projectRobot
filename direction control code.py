from microbit import display, Image, sleep
import tinybit

# 显示欢迎图像
display.show(Image.HAPPY)

# 定义速度档位
SPEED_PROFILES = [
    (0, 0, 1000),  # 停止
    (50, 50, 1000),  # 非常慢
    (100, 100, 1000),  # 慢
    (150, 150, 1000),  # 中速
    (200, 200, 1000),  # 快
    (255, 255, 1000)  # 全速
]

# 主循环
while True:
    for left_speed, right_speed, duration in SPEED_PROFILES:
        tinybit.car_run(left_speed, right_speed)
        sleep(duration)

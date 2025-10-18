from microbit import display, Image, sleep, button_a, button_b
import tinybit

# 假设的运动序列字典，键为字母，值为运动序列列表
# 每个运动序列元素为 (动作, 速度, 持续时间)
MOVEMENT_SEQUENCES = {
    'A': [("run", 150, 1000), ("stop", 0, 500)],
    'B': [("spinleft", 150, 1000), ("stop", 0, 500)],
    # 可以添加更多字母和对应的运动序列
}

def execute_movement_sequence(letter):
    """执行给定字母的运动序列"""
    if letter in MOVEMENT_SEQUENCES:
        for action, speed, duration in MOVEMENT_SEQUENCES[letter]:
            if action == "run":
                tinybit.car_run(speed, speed)
            elif action == "spinleft":
                tinybit.car_spinleft(speed)
            elif action == "spinright":  # 修正原图片中的拼写错误
                tinybit.car_spinright(speed)
            elif action == "stop":
                tinybit.car_stop()
            if duration > 0:
                sleep(duration)
    else:
        display.show(Image.SAD)  # 字母未定义时显示悲伤脸
        sleep(1000)

# 示例使用（在实际应用中，可能需要通过其他方式获取字母，如传感器输入）
current_letter = 'A'  # 假设当前字母为'A'

# 主循环（在实际应用中，可能需要通过按钮或其他事件触发）
while True:
    # 显示当前字母（简化处理，实际可能需要更复杂的显示逻辑）
    # 这里假设有一个函数显示字母，但microbit没有直接显示字母的函数，可以用图像代替
    # 实际应用中可能需要自定义图像或使用其他方式表示字母
    display.show(Image("99999:90009:99999:90009:90009"))  # 示例图像，不代表实际字母
    sleep(1000)

    # 检查按钮A和按钮B
    if button_a.is_pressed():
        # 切换到下一个字母（简化处理）
        # 实际应用中可能需要更复杂的字母切换逻辑
        letters = list(MOVEMENT_SEQUENCES.keys())
        current_index = letters.index(current_letter)
        next_index = (current_index + 1) % len(letters)
        current_letter = letters[next_index]
    elif button_b.is_pressed():
        execute_movement_sequence(current_letter)# 在这里写上你的代码 :-)

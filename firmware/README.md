# MicroPython 固件示例（Firmware）

示例与在线教程 8 章对齐：  
https://www.pythonguru.cn/research/picar-mini-2wd-v1-1/micropython-2wd-tutorial/

## 目录

```
micropython/
├── chapter-01/   # hello + 烧录速查
├── chapter-02/   # blink_led
├── chapter-03/   # buttons / toggle LED
├── chapter-04/   # PWM + single motor
├── chapter-05/   # 2WD motion
├── chapter-06/   # ultrasonic + LED
├── chapter-07/   # button + motor (+ ultrasonic)
├── chapter-08/   # modular main.py (autostart)
└── lib/          # config, motor_driver, ultrasonic, button, status_led
notes/
└── strap-pins.md
```

## 学习顺序

| 章 | 脚本 | 说明 |
| --- | --- | --- |
| 1 | `hello.py` | 确认 REPL |
| 2 | `blink_led.py` | GPIO5/6 |
| 3 | `test_button.py`, `toggle_led.py` | SW21→红灯，SW20→绿灯 |
| 4 | `motor_driver.py`, `test_single_motor.py` | 单轮调速 |
| 5 | `test_motor.py` | 前进/后退/转向 |
| 6 | `ultrasonic.py`, `test_ultrasonic*.py` | 测距与灯光 |
| 7 | `test_sw_motor*.py` | 按键控轮组合 |
| 8 | `main.py` + 模块 | 综合自启 |

## 运行提示

- 先完成 [../docs/flashing.md](../docs/flashing.md)
- 含 `import motor_driver` 的脚本需先把同目录或 `lib/` 中模块拷到板端
- 第 8 章：将 `chapter-08/*.py` 全部上传；`main.py` 会开机运行

## 许可

固件代码遵循仓库根目录 [LICENSE](../LICENSE)（MIT）。

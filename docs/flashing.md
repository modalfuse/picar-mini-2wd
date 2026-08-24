# 固件烧录（Flashing）

目标：在 ESP32-C3 SuperMini 上安装 **MicroPython**（`ESP32_GENERIC_C3`），并用 Thonny 或 `mpremote` 运行示例。

推荐固件版本：课堂常用 **v1.27.0**（亦可使用 Thonny 提供的稳定版）。

## 方法 A：Thonny（推荐）

1. 安装 [Thonny](https://thonny.org/)  
2. USB 连接 C3，确认出现串口（macOS 常见 `/dev/cu.usbmodem*`）  
3. **工具 → 选项 → 解释器** → 选择 **MicroPython (ESP32)** 与正确端口  
4. 点击 **Install or update MicroPython (esptool)**  
   - Family：**ESP32-C3**  
   - Variant：generic / `ESP32_GENERIC_C3`  
5. 若需下载模式：按住 **BOOT** → 点 **RESET** → 松开 BOOT  
6. 完成后 Shell 出现 `>>>`，运行 `firmware/micropython/chapter-01/hello.py`

## 方法 B：命令行 esptool

```bash
PORT=/dev/cu.usbmodem1101   # 改成你的端口

# 进入下载模式：按住 BOOT → 点 RESET → 松开 BOOT

esptool.py --chip esp32c3 --port $PORT erase_flash
esptool.py --chip esp32c3 --port $PORT --baud 460800 \
  write_flash 0 ESP32_GENERIC_C3-v1.27.0.bin
```

请将固件文件名改为你下载的 **`ESP32_GENERIC_C3-….bin`**。  
示例脚本见 `firmware/micropython/chapter-01/esptool_flash_example.sh`。

> 对部分 C3 板，烧录偏移为 `0` 即可；若官方说明要求其它偏移，以 MicroPython 下载页为准。

## 用 mpremote 运行示例

```bash
mpremote connect $PORT run firmware/micropython/chapter-02/blink_led.py
```

多文件模块（如第 4 章）：

```bash
mpremote connect $PORT cp firmware/micropython/chapter-04/motor_driver.py :motor_driver.py
mpremote connect $PORT run firmware/micropython/chapter-04/test_single_motor.py
```

## 开机自启

将综合程序保存为设备上的 `main.py`（见 `firmware/micropython/chapter-08/`）。调试其它脚本时若被自启占用，可暂时重命名或删除板端 `main.py`。

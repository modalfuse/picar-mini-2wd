# ESP32-C3 strap 脚说明

## 一句话

strap 脚是芯片在**复位瞬间**用来采样启动配置的特殊 GPIO；采样结束后才变回普通 IO。

## ESP32-C3 的三个 strap 脚

| 脚 | 复位时常见要求 |
| --- | --- |
| **GPIO9** | 高 = 从 Flash 正常启动；低 = 下载模式（BOOT） |
| **GPIO8** | 通常需为高 |
| **GPIO2** | 合法启动模式要求为高 |

| GPIO2 | GPIO8 | GPIO9 | 模式 |
| --- | --- | --- | --- |
| 1 | x | 1 | SPI Boot（正常运行） |
| 1 | 1 | 0 | Download Boot（烧录） |

按住开发板上的 **BOOT** = 拉低 GPIO9，进入下载模式。

## 本驱动板（v1.1）的做法

外设 GPIO **避开** strap 脚：

- 电机：GPIO0/1、GPIO3/4（**GPIO0 在 C3 上不是 strap**）
- 超声：Trig=GPIO7，Echo=GPIO10
- LED：GPIO5/6；按键：GPIO20/21

GPIO2 / GPIO8 / GPIO9 保持空闲或按需上拉，降低上电启动异常风险。

## 调试上电顺序

仍建议：**先 USB 连接 C3，再打开电池开关**；枚举异常时短按 RESET。

## 参考

- Espressif ESP32-C3 技术手册 — Strapping pins
- 本仓库 [docs/pinout.md](../../docs/pinout.md)

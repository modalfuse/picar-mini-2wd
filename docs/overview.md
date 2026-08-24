# 方案概述（Overview）

PiCar Mini 2WD 是面向 STEM / 嵌入式入门的二驱智能车平台。一块专用驱动 PCB（v1.1）集成 **TC1508A 双 H 桥**、电源输入、红绿状态灯、双轻触开关与超声波接口；主控插接 **ESP32-C3 SuperMini**，支持 WiFi / BLE 与 **MicroPython**。硬件开源、结构紧凑、接插件装配。

## 核心能力

- 双轮差速行走（PWM 调速 / 正反转）
- 超声波前方测距与远绿近红灯光语义
- 左右板载按键分别控制左右轮（综合示例）
- 课堂可复现的 MicroPython 8 章示例

## 系统组成

| 模块 | 说明 |
| --- | --- |
| 主控 | ESP32-C3 SuperMini，插在驱动板 1×8×2 排母 |
| 驱动板 | 自制 PCB v1.1：电机驱动 + 电源 + LED + 按键 + 接口 |
| 电机 | TT 减速电机 ×2，XH2.54 接 motor01（左）/ motor34（右） |
| 电源 | 3.7 V 锂电（XH2.54），板载开关 / 防护 / 滤波；3.7VBAT 直供 TC1508A 与 C3 的 5V/VIN |
| 传感 | HC-SR04（宽电压版），板载 4P：Trig=GPIO7，Echo=GPIO10 |

## 供电拓扑（摘要）

```
3.7V 锂电 → SW1 → 防反接 / TVS / 滤波 → 3.7VBAT
    ├─ TC1508A（电机）
    ├─ ESP32-C3 5V/VIN
    └─ 超声波 VCC
GPIO → LED / 按键 / Trig·Echo / 电机逻辑输入
```

## 更多

- 引脚表：[pinout.md](pinout.md)
- 装配：[assembly.md](assembly.md)
- 网页专题：https://www.pythonguru.cn/research/picar-mini-2wd-v1-1/

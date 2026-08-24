# 物料清单（BOM）

机器可读版本：[../hardware/bom/bom-core.csv](../hardware/bom/bom-core.csv)

## 核心模块

| 模块 | 型号 / 规格 | 说明 |
| --- | --- | --- |
| 主控板 | ESP32-C3 SuperMini（WiFi/BLE，原生 USB） | 插接驱动板 1×8×2 排母 |
| 驱动板 | 自制 PCB v1.1 | 电机驱动 + 电源 + LED + 按键 + 接口 |
| 电机驱动 | TC1508A 双 H 桥（板载） | PWM 调速、正反转 |
| 电源 | 3.7 V 锂电 + 防反接 / 滤波 | 3.7VBAT 直供 TC1508A 与 C3 的 5V/VIN |
| 测距 | HC-SR04（3.3 V–5 V） | 板载 4P 接口 |
| 机械 | 底盘 + 驱动轮 + TT×2 + 万向轮 | motor01 / motor34 |
| 状态灯 | LED5 / LED6 + 100 Ω | 高电平点亮；颜色以实物为准 |
| 按键 | SW20 / SW21 | 低有效，内部上拉 |

## 成本

核心物料与辅材合计约 **¥35–40**（随打样数量、元件采购与底盘选型浮动）。

## 参考实物

- 电池：[../images/18650_battery_xh254.jpg](../images/18650_battery_xh254.jpg)
- TT 电机：[../images/tt_motor_overview.jpg](../images/tt_motor_overview.jpg)
- 超声波：[../images/hc_sr04_overview.jpg](../images/hc_sr04_overview.jpg)

# 驱动板硬件（Hardware）

自制驱动板 **v1.1**：将电机驱动、电源通路、状态 LED、轻触开关、超声波接口与 GPIO 排针集成到一块 PCB。主控以 1×8×2 排母插接；电机与电池用 XH2.54，超声波用 4P。

![Driver board](../images/driver-board-front.jpg)

## 目录

| 路径 | 内容 |
| --- | --- |
| [schematic/](schematic/) | 原理图 / PCB 导出 PDF |
| [bom/bom-core.csv](bom/bom-core.csv) | 核心物料 CSV |
| [gerber/](gerber/) | 生产 Gerber（首发未附，见该目录 README） |
| [mechanical/](mechanical/) | 结构件占位说明 |

## 子系统摘要

### 电源

- 输入：3.7 V 锂电（XH2.54 → 3.7VBAT / GND）
- 板载 SW1、TVS、去耦
- 3.7VBAT 直供 TC1508A VDD，并接入 C3 的 **5V/VIN**

### 电机驱动（TC1508A）

| pin1 | pin2 | 状态 |
| --- | --- | --- |
| PWM | LOW | 正转（前进） |
| LOW | PWM | 反转 |
| LOW | LOW | 停止（滑行） |
| HIGH | HIGH | 刹车 |

左轮 GPIO1/0，右轮 GPIO4/3。

### LED / 按键 / 超声

见 [../docs/pinout.md](../docs/pinout.md)。

## 许可

硬件设计文件遵循仓库根目录 [LICENSE-HARDWARE](../LICENSE-HARDWARE)（CERN-OHL-P-2.0）。

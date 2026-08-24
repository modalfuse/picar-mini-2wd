#!/usr/bin/env bash
# 第 1 章：命令行烧录 MicroPython 示例（可选）
# 使用前：1) 安装 esptool  2) 下载 ESP32_GENERIC_C3 的 .bin
#         3) 按住 BOOT，点一下 RESET，松开 BOOT

set -euo pipefail
PORT="${PORT:-/dev/cu.usbmodem101}"
BIN="${1:-ESP32_GENERIC_C3-v1.27.0.bin}"

if [[ ! -f "$BIN" ]]; then
  echo "找不到固件文件: $BIN"
  echo "用法: PORT=/dev/cu.usbmodemXXX $0 /path/to/ESP32_GENERIC_C3-....bin"
  exit 1
fi

echo "端口: $PORT"
echo "固件: $BIN"
esptool.py --chip esp32c3 --port "$PORT" erase_flash
esptool.py --chip esp32c3 --port "$PORT" --baud 460800 write_flash 0 "$BIN"
echo "完成。请短按 RESET，再在 Thonny 中连接 REPL。"

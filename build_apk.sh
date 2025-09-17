#!/usr/bin/env bash
# 在 WSL2/Ubuntu 中一键准备环境并构建 APK（在 Linux 中运行）
# 使用方法：
# 1) 将项目复制到 WSL2（例如 /home/<user>/projects/hhw）
# 2) 在 WSL2 终端中运行： bash build_apk.sh

set -euo pipefail

echo "更新系统并安装必要的包..."
sudo apt update
sudo apt install -y python3-pip python3-setuptools git openjdk-11-jdk unzip zlib1g-dev build-essential libffi-dev libssl-dev

echo "安装 buildozer 和 cython..."
python3 -m pip install --user --upgrade pip
python3 -m pip install --user buildozer cython

# 确保 ~/.local/bin 在 PATH 中
export PATH="$HOME/.local/bin:$PATH"
if ! command -v buildozer >/dev/null 2>&1; then
  echo "ERROR: buildozer 未安装到 ~/.local/bin，请检查 pip 安装输出。"
  exit 1
fi

echo "开始构建 APK（会下载 Android SDK/NDK，首次运行较慢）..."
# -v 显示详细日志
buildozer -v android debug

echo "构建完成。APK 位于 bin/ 目录下。若要部署到已连接设备，可运行： buildozer android debug deploy run"

# 常见问题提示
cat <<'EOF'
常见问题：
- 若 buildozer 在下载或解压 SDK/NDK 时失败，建议手动安装 Android SDK command-line tools 并在 buildozer.spec 中指定 sdk 路径。
- 若出现 NDK 版本不兼容，尝试在 buildozer.spec 中调整 android.ndk 或使用 buildozer 的 default 配置。
- 若缺少 Python 包（例如 pillow），请将其加入 buildozer.spec 的 requirements。
EOF


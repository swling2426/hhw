[app]
# (str) Title of your application
title = hhw

# (str) Package name
package.name = hhw

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (list) Source file extensions to include
source.include_exts = py,png,jpg,kv

# (str) Application versioning
version = 0.1

# (str) Supported orientation
orientation = portrait

# (list) Application requirements
# 如果需要其他库（例如 pillow）可以加入到此处
requirements = python3,kivy,pillow

# (str) Android permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Include additional files/patterns into the apk
source.include_patterns = **/*.png, **/*.jpg

# (int) Android API target
android.api = 33
android.minapi = 21

# (str) Android NDK version (buildozer may override)
android.ndk = 23b

# (list) Supported architectures
android.arch = armeabi-v7a, arm64-v8a

# (int) log level
log_level = 2

# (str) Icon and presplash (可选，放在项目根目录并取消注释)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# Notes:
# - 在 Linux/WSL 环境中运行 buildozer（Ubuntu 推荐）：
#   sudo apt update && sudo apt install -y python3-pip python3-setuptools git openjdk-11-jdk unzip zlib1g-dev build-essential
#   pip3 install --user --upgrade pip
#   pip3 install --user buildozer cython
#   # 确保 ~/.local/bin 在 PATH 中： export PATH=$PATH:~/.local/bin
#   buildozer -v android debug
# - 若有其他依赖（例如其它 Python 包），请将其添加到 requirements 列表

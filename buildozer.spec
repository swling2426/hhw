[app]
# (str) Title of your application
title = hhw

# (str) Package name
package.name = hhw

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let's you specify individual files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png,chuancang/*.png,tongmengqiandao/*.png,wanfa/*.png

# (list) Source files to exclude (let's you specify individual files)
#source.exclude_exts = spec

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,pillow,requests

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) The Android app theme, default is ok for Kivy-based app
#android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (bool) If True, your application will be listed as a home app (launcher app)
android.home_app = False

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java files to add to the android project (can be java or a directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the APK assets directory.
#android.add_assets =

# (list) Source files to include (let's you specify individual files)
#android.source_include = %(source.dir)s/data/custom_font.ttf

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx requires android.api >= 28
android.enable_androidx = True

# (str) python-for-android specific branch to use, if not master
#p4a.branch = master

# (str) python-for-android specific git clone directory
#p4a.source_dir = /path/to/py4a

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds (android_new only)
#p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port =

# Control passing the --use-setup-py vs --ignore-setup-py to p4a
# "in the future" --use-setup-py is going to be the default behaviour in p4a, right now it is not
#p4a.use_setup_py = False

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
bin_dir = ./bin

# (str) Path to build artifact storage (i.e. libs, deps, etc.)
build_dir = ./.buildozer

# (str) Path to temporary artifacts storage
cache_dir = ./.buildozer_cache

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
#   # ��保 ~/.local/bin 在 PATH 中： export PATH=$PATH:~/.local/bin
#   buildozer -v android debug
# - 若有其他依赖（例如其它 Python 包），请将其添加到 requirements 列表

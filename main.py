from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window
import threading
import time
import os
from pathlib import Path

# 保持窗口大小在桌面调试时更合理
Window.size = (360, 640)

# 复用项目中的图片资源路径
PROJECT_DIR = Path(__file__).resolve().parent

# 定义序列（与原脚本相同的模板路径，仅用于展示/调试）
DEFAULT_SEQ = [
    ('tongmengqiandao/close.png', 1),
    ('tongmengqiandao/click_tongmeng.png', 1),
    ('tongmengqiandao/click_huodong.png', 1),
    ('tongmengqiandao/click_qiandao.png', 1),
    ('tongmengqiandao/click_putong.png', 1),
    ('tongmengqiandao/click_qieding.png', 1),
    ('tongmengqiandao/click_renyidianji.png', 1),
    ('tongmengqiandao/click_huitui.png', 2),
]

DEFAULT_CHUANCANG_SEQ = [
    ('chuancang/click_1.png', 1),
    ('chuancang/click_chuancang.png', 1),
    ('chuancang/click_chuanzhangshi.png', 1),
    ('chuancang/click_rou.png', 1),
    ('chuancang/click_queding.png', 1),
    ('chuancang/click_dianjirenyi.png', 1),
    ('chuancang/click_huitui.png', 1),
    ('chuancang/click_paiqian.png', 1),
    ('chuancang/click_paiqian1.png', 1),
    ('chuancang/click_lingqu.png', 1),
    ('chuancang/click_zhinengpaiqian.png', 1),
    ('chuancang/click_paiqiankaishi.png', 1),
    ('chuancang/click_huitui.png', 3),
    ('chuancang/close1.png', 1),
]

DEFAULT_WANFA_SEQ = [
    ('wanfa/click_wanfa.png', 1),
    ('wanfa/click_zuiqinagjuedou.png', 1),
    ('wanfa/click_saodang.png', 1),
    ('wanfa/click_renyidianji.png', 1),
    ('wanfa/click_tuichu1.png', 1),
    ('wanfa/click_wujintanxian.png', 1),
    ('wanfa/click_lizhitanxian.png', 1),
    ('wanfa/click_di2ceng.png', 1),
    ('wanfa/click_saodang1.png', 1),
    ('wanfa/click_jindutiao.png', 1),
    ('wanfa/click_saodang2.png', 1),
    ('wanfa/click_queding.png', 1),
    ('wanfa/click_tuichu1.png', 2),
    ('wanfa/click_tiaozhan.png', 1),
    ('wanfa/click_haidao.png', 1),
    ('wanfa/click_lingqu.png', 1),
    ('wanfa/click_dianjirenyi1.png', 1),
    ('wanfa/click_zhuye.png', 1),
]

class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=8, padding=8, **kwargs)
        self.log = TextInput(size_hint_y=0.8, readonly=True)
        btn_layout = BoxLayout(size_hint_y=0.2)

        btn_run = Button(text='运行同盟签到序列')
        btn_run.bind(on_release=lambda *_: self.start_sequence('同盟签到', DEFAULT_SEQ))

        btn_chuan = Button(text='运行船厂序列')
        btn_chuan.bind(on_release=lambda *_: self.start_sequence('船厂', DEFAULT_CHUANCANG_SEQ))

        btn_wanfa = Button(text='运行玩法序列')
        btn_wanfa.bind(on_release=lambda *_: self.start_sequence('玩法', DEFAULT_WANFA_SEQ))

        btn_layout.add_widget(btn_run)
        btn_layout.add_widget(btn_chuan)
        btn_layout.add_widget(btn_wanfa)

        self.add_widget(self.log)
        self.add_widget(btn_layout)

    def append_log(self, msg: str):
        # 在主线程更新 UI
        def _append(dt):
            now = time.strftime('%H:%M:%S')
            self.log.text += f'[{now}] {msg}\n'
            # 自动滚动到末尾
            self.log.cursor = (len(self.log.text), 0)
        Clock.schedule_once(_append, 0)

    def start_sequence(self, name, seq):
        self.append_log(f'开始序列: {name}')
        # 后台线程执行，避免阻塞 UI
        t = threading.Thread(target=self._run_seq_thread, args=(name, seq), daemon=True)
        t.start()

    def _run_seq_thread(self, name, seq):
        for tpl, clicks in seq:
            full = PROJECT_DIR.joinpath(tpl)
            exists = full.exists()
            for i in range(clicks):
                if exists:
                    self.append_log(f'找到模板: {tpl} -> 模拟点击 ({i+1}/{clicks})')
                else:
                    self.append_log(f'模板缺失: {tpl} -> 跳过 ({i+1}/{clicks})')
                time.sleep(0.4)
            time.sleep(0.3)
        self.append_log(f'序列 {name} 完成')

class HhwApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    HhwApp().run()


import time
import os
from pathlib import Path
import pyautogui

pyautogui.FAILSAFE = False

def click_template(template_path: str, retries: int = 5, wait_interval: float = 0.5, post_click_wait: float = 0.5) -> bool:
    """简单稳定的模板匹配与点击"""
    tpl = str(Path(__file__).resolve().parent.joinpath(template_path))
    if not Path(tpl).exists():
        print(f"模板不存在: {template_path}")
        return False

    # 多次尝试查找模板
    for i in range(retries):
        try:
            loc = pyautogui.locateCenterOnScreen(tpl, confidence=0.85)
            if loc:
                print(f"找到 {template_path}")
                pyautogui.moveTo(loc.x, loc.y, duration=0.2)
                pyautogui.click()
                print(f"点击 {template_path}")
                time.sleep(post_click_wait)
                return True
        except Exception as e:
            print(f"定位异常 {template_path}: {e}")
        print(f"第 {i + 1} 次尝试未找到 {template_path}")
        time.sleep(wait_interval)
    return False


def run_flow():
    """按严格顺序��行：先检测 close.png，然后按预定义序列顺序执行"""
    # 预定义序列
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

    print("开始执行自动化流程...")

    # 1. 先检测并点击 close.png
    print("检测 close.png...")
    click_template('close.png', retries=3, wait_interval=0.5)
    time.sleep(0.8)  # 给足时间让界面响应

    # 2. 执行同盟签到序列
    print("\n开始同盟签到序列...")
    for item in DEFAULT_SEQ:
        tpl, clicks = item
        for _ in range(clicks):
            ok = click_template(tpl)
            if not ok:
                print(f"警告：{tpl} 点击失败")
            time.sleep(0.3)  # 每次点击后短暂等待
        time.sleep(0.5)  # 每个步骤之间稍作等待

    # 3. 执行船厂序列
    print("\n开始船厂序列...")
    for item in DEFAULT_CHUANCANG_SEQ:
        tpl, clicks = item
        for _ in range(clicks):
            ok = click_template(tpl)
            if not ok:
                print(f"警告：{tpl} 点击失败")
            time.sleep(0.3)
        time.sleep(0.5)

    # 4. 执行玩法序列
    print("\n开始玩法序列...")
    for item in DEFAULT_WANFA_SEQ:
        tpl, clicks = item
        for _ in range(clicks):
            ok = click_template(tpl)
            if not ok:
                print(f"警告：{tpl} 点击失败")
            time.sleep(0.3)
        time.sleep(0.5)

    print("\n全部序列执行完成")


if __name__ == '__main__':
    run_flow()

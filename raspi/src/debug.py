import os
from devicedriver import ClRs2

if __name__ == "__main__":
    bulb = ClRs2()

    print("全部の値：",bulb.get_status())  # 実行したい関数だけ呼び出す
    print("特定の値：",bulb.get_status("brightness"))

    bulb.brightness(50)

    print("全部の値：",bulb.get_status())  # 実行したい関数だけ呼び出す
    print("特定の値：",bulb.get_status("brightness"))

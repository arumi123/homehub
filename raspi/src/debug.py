import os
from devicedriver import ClRs2

if __name__ == "__main__":
    bulb = ClRs2()

    print("全部の値：",bulb.getstatus())  # 実行したい関数だけ呼び出す
    print("特定の値：",bulb.getstatus("brightness"))

    bulb.write_status("brightness", 100)
    bulb.write_status("brightness", 80)

    print("全部の値：",bulb.getstatus())  # 実行したい関数だけ呼び出す
    print("特定の値：",bulb.getstatus("brightness"))

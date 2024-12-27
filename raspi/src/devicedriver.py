import json
from time import sleep

# Bulbドライバの抽象クラス
class Bulb:
    def __init__(self):
        pass

    def getstate(self):
        pass

    def brightness(self, bright):
        pass

    def colortemp(self,temp):
        pass

# シーリングライトのRE0207(CH1)のBulbドライバ
class Re0207:
    def __init__(self):
        self.brightness = 0
        self.color_temprature = 0

    def getstate(self):
        try:
            with open("light_setting.json","r") as file:
                loaded_data = json.load(file)
        except json.JSONDecodeError as e:
            print("デバイス情報を抜き取れませんでした:", e)

        return(loaded_data)

    def brightness(self, bright):
        # brightが0~100の間にない場合はエラーを返す
        if not (0 <= bright <= 100):
            raise ValueError("Invalid brightness value. Please specify a value between 0 and 100.")
        
        # 設定値を更新
        try:
            state = self.getstate()
            self.current_mode = state.get("mode", "off")
        except:
            self.current_mode = "off"

        if bright == 0:
            self.change_mode("off")
        elif 1 <= bright <= 9:
            self.change_mode("nightmode")
        else:
            self.change_mode("on")
            self.change_bright((bright // 10) - 1)
            
    def colortemp(self, temp):
        # tempが0~5の間にない場合はエラーを返す
        if not (0 <= temp <= 5):
            raise ValueError("Invalid brightness value. Please specify a value between 0 and 5.")
        
    
    def change_mode(self,mode):
        mode_sequence = ["on","night","off"]
        current_index = mode_sequence.index(self.current_mode)
        target_index = mode_sequence.index(mode)

        while current_index != target_index:
            current_index = (current_index + 1) % len(mode_sequence)
            self.current_mode = mode_sequence[current_index]
            print(f"Changing mode to {self.current_mode}")
            # リモコン操作のロジックをここに追加
            sleep(0.5)

    def change_brightness(self, target_brightness):
        if not (0 <= target_brightness <= 9):
            raise ValueError("Invalid brightness value. Please specify a value between 0 and 9.")
        
        current_brightness = self.brightness
        step = 1 if target_brightness > current_brightness else -1
        
        while current_brightness != target_brightness:
            current_brightness += step
            self.brightness = current_brightness
            print(f"Changing brightness to {current_brightness}")
            # リモコン操作のロジックをここに追加
            sleep(0.5)

    def change_colortemp(self,target_colortemp)
        if not (0 <= temp <= 5):
            raise ValueError("Invalid brightness value. Please specify a value between 0 and 5.")

# HeaterCoolerドライバの抽象クラス
class HeaterCooler:
    def __init__(self):
        pass

    def getstate(self):
        pass

    def mode(self,mode):
        pass

    def temp(self,temp):
        pass

# PanasonicACのHeaterCoolerドライバ
class PanasonicAC:
    def __init__(self):
        pass

    def getstate(self):
        pass

    def mode(self,mode):
        pass
    def temp(self,temp):
        pass

# 赤外線送受信ドライバの抽象クラス
class Ir:
    def __init__(self):
        pass

    def send(self,code):
        pass

    def receive(self):
        pass

# raspizeroと独自赤外線送受信回路の赤外線送受信ドライバの実装クラス
class IrRaspizero:
    def __init__(self):
        pass

    def send(self,code):
        pass

    def receive(self):
        pass

class Cmd4client:
    def __init__(self):
import json

#Light calssの定義
class Light:
    def __init__(self):
        self.brightness = 0
        self.color_temprature = 0

    def getstate(self):
        with open("light_setting.json","r") as file:
            loaded_data = json.load(file)
        print(loaded_data)

if __name__ == "__main__": 
    light = Light()
    light.getstate

# Raspi zero wh で実現するhomekit

iosのホームキットから家電が操作できる

Raspi zero whを使うこと
自作赤外線送受信回路を使うこと



デベロップブランチ　1回目のプッシュ
デベロップブランチ　2回目のプッシュ
coolerブランチ一回目
coolerぶらんち2かいめ

エアコンは以下のデータを読み取った
停止ボタン　
"Active": 0

冷房ボタン　
"TargetHeaterCoolerState": 2

暖房ボタン
"TargetHeaterCoolerState": 1

暖房時の温度設定
"HeatingThresholdTemperature": 20,

冷房時の温度設定
"CoolingThresholdTemperature": 27,


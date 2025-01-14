# System Architecture

## Overview
このドキュメントは、本プロジェクトの全体的な設計およびアーキテクチャについて説明します。
- 対象読者: 新規開発者、既存のメンテナンス担当者
- 目的: システムの構造を把握し、開発効率と保守性を向上させるため

## Architecture Diagram
```mermaid
graph TD;
    subgraph iPhone [iPhone]
        Homeapp[Homeapp]
    end

    subgraph GPTserver [GPT server]
        GPTAPI[GPT API]
    end

    subgraph AWS [AWS]
        lamda[lamda]
        IoTcore[IoTcore]
    end

    subgraph RasPiSide [RasberryPi]
        subgraph dockercontainer[docker]
            subgraph Node.js[Node.js]
                Homebridge[Homebridge]
            end
            pythonmodule[pythonmodule]
            data.json[data.json]
        end
    end

    light

    ac

    Homeapp -->|http?| Homebridge
    Homebridge -->|ipc| pythonmodule
    Homebridge -->|http?| Homeapp
    pythonmodule -->|IR| light
    pythonmodule -->|IR| ac
    pythonmodule -->|ipc| Homebridge
    pythonmodule -->|ipc| data.json
    pythonmodule -->|http?| GPTAPI
    ChatGPT -->|http?| pythonmodule
```

## Components

### 1. Raspberry Pi
- **役割**: センサーからデータを収集し、AWS IoT Coreに送信します。
- **使用技術**: [使用するプログラミング言語やライブラリ、OSなど]
- **動作**: 定期的にセンサーデータを測定し、MQTTプロトコルを介してデータをAWSに送信します。
- **クラス図**
~~~mermaid
classDiagram
    class IRController{
        
    }

    class Device{
        <<abstruct>>
        +getstatus()
        -setstatuse()
    }

    class Bulb {
        <<interface>>
        +brightness()*
        +colortemp()*
    }

    class Re0207 {
        +brightness()
        +colortemp()
        -change_mode()
        -change_brightness()
        -change_colortemp()
    }

    class ClRs2 {
        +brightness()
        +colortemp()
        -change_mode()
        -change_brightness()
        -change_colortemp() 
    }

    class HeaterCooler {
        <<interface>>
        +mode()*
        +temp()*
    }

    class PanasonicAc {
        +getstate()
        +mode()
        +temp()      
    }

    class Cmd4Client {
        
    }

    class CliOperater {

    }

    class GptClient {

    }

    Bulb --|> Device
    HeaterCooler --|> Device

    Re0207 --|> Bulb
    ClRs2 --|> Bulb
    PanasonicAc --|> HeaterCooler
    

    Re0207 ..> IRController : calls
    ClRs2 ..> IRController : calls
    PanasonicAc ..> IRController : calls

    Cmd4Client ..> Re0207 : calls
    CliOperater ..> Re0207 : calls
    GptClient ..> Re0207 : calls
    Cmd4Client ..> ClRs2 : calls
    CliOperater ..> ClRs2 : calls
    GptClient ..> ClRs2 : calls
    Cmd4Client ..> PanasonicAc : calls
    CliOperater ..> PanasonicAc : calls
    GptClient ..> PanasonicAc : calls
~~~

### 2. AWS IoT Core
- **役割**: Raspberry Piから送信されたデータを受信し、処理します。
- **使用技術**: MQTT, HTTP
- **動作**: 受信したデータをAWS Lambda関数に転送します。

### 3. AWS Lambda
- **役割**: データを処理し、DynamoDBなどに保存します。
- **使用技術**: Node.js (または使用する言語)
- **動作**: IoT Coreからデータを受け取り、DynamoDBに保存します。

### 4. DynamoDB
- **役割**: センサーデータを保存するためのデータベースです。
- **使用技術**: NoSQLデータベース
- **動作**: Lambda関数によって受信したデータを保存します。

## Data Flow
1. Raspberry Piがセンサーからデータを収集します。
2. 収集したデータをAWS IoT Coreに送信します。
3. AWS IoT Coreがデータを受信し、Lambda関数に転送します。
4. Lambda関数がデータを処理し、DynamoDBに保存します。

## Security
- **認証**: AWS IoT Coreに接続する際は、X.509証明書を使用して認証します。
- **アクセス管理**: IAMポリシーを用いて、Lambda関数やDynamoDBへのアクセスを制限します。

## Deployment Architecture
### 環境
- **開発環境**: 
- **本番環境**: 

### CI/CD
- **GitHub Actions**: テスト、ビルド、デプロイを自動化。

### 
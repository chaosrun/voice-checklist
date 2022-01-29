# voice-checklist

本脚本用于协助 Google Voice 的号码保活检查，辅助人工操作，可提示待查看账号的基本信息。

## 准备

根据以下的格式在 JSON 文件中录入关于账号的信息：

```json
{
    "登录设备名称": {
        "邮箱": "号码“
    }
}
```

示例：可参见 [example.json](./example.json) 的内容。

## 用法

开始辅助检查：

```
python3 main.py -f "JSON 文件路径"
```

搜索指定邮箱或者号码的信息：

```
python3 main.py -f "JSON 文件路径" -s "example1@gmail.com"
```

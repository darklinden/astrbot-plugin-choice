# 帮我选

AstrBot 随机选择插件 —— 让机器人帮你在多个选项中随机选一个。

## 说明

支持以空格分隔多个选项，至少需要两个选项。

基于 [2bot-v4 choose 插件](https://github.com/idlist/2bot-v4/blob/main/plugins/fun/choose.js) 移植。

## 安装

```bash
# 克隆到 AstrBot 的 addons 目录
cd addons/plugins
git clone https://github.com/darklinden/astrbot-plugin-choice.git choice
```

或通过 AstrBot 插件市场安装。

## 用法

```
choice <选项1> <选项2> [选项3 ...]
帮我选 <选项1> <选项2> [选项3 ...]
```

### 示例

```
choice 麦当劳 肯德基 汉堡王
> 帮 小明 选择了：麦当劳

帮我选 咖啡 奶茶 可乐
> 帮 小明 选择了：奶茶
```

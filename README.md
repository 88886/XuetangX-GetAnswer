# 介绍

本脚本用于获取学堂在线的课程练习章节答案，~~仅供摸鱼之用~~。

学堂在线相关的脚本实在太少了，只好自己动手了。

脚本主要目的为自用，~~有会JavaScript的带佬看到了可以试试写个自动答题脚本~~。

编写环境: Python 3.7.4
@Auther: BakaFT

## 食用方法

1. 下载并解压，用记事本直接打开 `XuetangX-GetAnswer.py` 并将第5行的headers参数填写完整
2. 使用 CMD/PowerShell 进入到脚本文件目录, 输入命令`Python XuetangX-GetAnswer.py` 并执行
3. 根据要求输入课程CID和SIGN，并等待目录下生成JSON文件
4. 记事本打开JSON并进行简单的题目查询操作，或自行对JSON进行二次处理。`

**注意，多次查询会直接覆盖已经生成的JSON**

## 食用方法中参数的获取

打开一个课程，一般是这样的一个网址

> https://next.xuetangx.com/learn/NUDT12041000081/NUDT12041000081/1510792/video/1265241

### CID&SIGN

观察一下上面的网址

NUDT1204100081 这串就是SIGN

1510792 这串是CID

### Headers

以Chromium为例，

在上面那个网址里按下F12打开`Chrome Developer Tools`，切换到`Network` 选项卡。

按下F5刷新页面，并观察寻找一条名为 `chapter?cid=xxxxxxxx&sign=xxxxxxxx`的请求。

右键这条请求，在Copy选项的二级菜单中点`Copy as Curl(bash)`。

打开 curl.trillworks.com 并将内容粘贴到左边的框子里。

在右边的框子里找到

```Python
headers = {
	'xxxxxx':'xxxxxxx'
	'xxxxxx':'xxxxxxx'
}
```

完整复制如上内容，替换脚本的**第五行**。


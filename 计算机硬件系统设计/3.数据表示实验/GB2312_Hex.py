# str1 = "计卓１８０１班李思岑Ｕ２０１８１４４８０"
str2 = "１２３４５ＡＢＣＤＥＦＧａｂｃｄｅｆｇ轻轻的我走了，正如我轻轻的来；我轻轻的招手，作别西天的云彩。那河畔的金柳，是夕阳中的新娘；波光里的艳影，在我的心头荡漾。"
# 输入必须是圆角字符
str = str2.encode("GB2312")
with open("output", "w") as f:
    print("v2.0 raw", file = f) # 方便Logisim直接导入
    i = 0
    while i <= len(str):
        print(str[i:i+2].hex(), end=' ', file=f)
        i = i + 2

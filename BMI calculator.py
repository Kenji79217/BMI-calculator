hight = input('請輸入身高（cm): ')
weight = input('起輸入體重 （kg): ')
hight = int(hight)
weight = int(weight)
hight = hight / 100 #換成公尺
bmi = weight / hight /hight
if bmi < 18.5:
	print('您的ＢＭＩ值為', bmi, '體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('您的ＢＭＩ值為', bmi, '體重正常範圍')
elif bmi >=24 and bmi < 27:
	print('您的ＢＭＩ值為', bmi, '體重稍重')
elif bmi >=27 and bmi < 30:
	print('您的ＢＭＩ值為', bmi, '輕度肥胖')
elif bmi >=30 and bmi < 35:
	print('您的ＢＭＩ值為', bmi, '中度肥胖')
elif bmi >= 35: 
	print('您的ＢＭＩ值為', bmi, '重度肥胖')
weight= float(input('請輸入體重:'))
height= float(input('請輸入身高:(公分)'))
print (weight ,'kg',height ,'cm')
heightkg=float(height/100)
bmi= weight/(heightkg*heightkg)
print ('BMI:',bmi)

if bmi < 18.5:
    print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('健康體重')
elif bmi >= 24 and bmi < 27:
    print('體重過重')
else:
    print('體重肥胖')


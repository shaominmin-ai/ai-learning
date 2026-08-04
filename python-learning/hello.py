name=input('请输入你的名字：')
age=int(input('请输入你的年龄：'))
hours=int(input('每天学习几小时：'))
print(f'你好，{name}')
print(f'你今年{age}岁')
print(f'每天学习{hours}小时')
if hours>=4:
    print('优秀，坚持180天会有明显提升')
elif hours>=2:
    print('不错，继续保持')
else:
    print('建议增加学习时间')
  



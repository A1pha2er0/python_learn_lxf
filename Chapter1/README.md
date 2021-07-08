字符编码
acsii 一个字节
unicode 两个字节
将unicode转换为可变长字节 UTF-8
便于节省空间和传输

python3 以Unicode进行字符串编码

正确显示中文需要添加注释 # -*- utf-8 -*-

格式化输出：
print('someone`s age is %s' %18)

'''
   字符串驻留机制
   驻留机制:相同的字符串在程序运行期间，其内存中仅存储一份

   说明：如何查看对象在内存的地址    id(对象名)
'''

s1 = 'python'
s2 = 'python'
s3 = 'python'
print(f's1={s1},id(s1)={id(s1)}')
print(f's2={s2},id(s2)={id(s2)}')
print(f's3={s3},id(s3)={id(s3)}')


s1 = 'hello world'
print(f's1={s1},id(s1)={id(s1)}')
print(f's2={s2},id(s2)={id(s2)}')
print(f's3={s3},id(s3)={id(s3)}')
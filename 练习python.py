 #作用域
i=10
def func():
    j=11
func()
#参数：与外界沟通的接口
#参数：形参和实参
#实参：在调用的时候使用的参数
#形参：函数定义时定义的

#实参：
def func2(a,b):
    if(a>b):
        print(str(a)+"比"+str(b)+"大")
    else:
        print(str(b)+"比"+str(a)+"大")
#func2(2,3)


#数据类型
T=(1,2,3,4,5,)
print("index number is: "+str(T.index(max(T)))+"    max is: "+str(max(T)))
T1=(1,3,6,7,8,9,10)
T2=T+T1
list=[6,6,6,6,6,6]
print(str(T2))
dict={1:2,2:3,1:4,T:100}
dict1={1:2,1:3}
dict2={1:dict1,1:list}
S=set([1,2,3,4,5])
gl1=dict2[1]
dict_null={1:1,2:3,3:4,5:6}
print(str(dict_null[2])+"null dict!")
#www



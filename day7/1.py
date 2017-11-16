# count = 0
# class Persion:
#     count += 1
#     def __init__(self,name):
#         self.name = name
# alex = Persion()



# t = 3.14
# class Y:
#     def __init__(self,r):
#         self.m = t*r**2
#         self.z = t*r*2
#
# l = Y(5)
# print(l.m)
# print(l.z)



# class Persion:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def shan(self):
#         print("%s %s %s 砍柴" %(self.name,self.age,self.sex))
#
# xiaoming = Persion('xiaoming',10,'男')
# xiaoming.shan()



class Dog:
    def __init__(self,name,type,aggr):
        self.name  = name
        self.dog_type = type
        self.aggr = aggr
        self.life_value = 2000

    def bite(self,person_obj):  #self==egg,person_obj=alex
        #属性的变化
        print('%s咬了%s'%(self.name ,person_obj.name ))
        person_obj.life_value -= self.aggr

class Person:
    rol = '人'         #数据属性、静态属性、类属性
    country = '中国'
    def __init__(self,name,age,life_value): #初始化方法
        self.name = name       #属性、对象属性
        self.theage = age
        self.life_value = life_value
        self.aggr = 1

    def attack(self,dog_obj):  #函数属性、动态属性、方法
        print('attack方法被%s执行了'%self.name )
        dog_obj.life_value -= self.aggr

alex = Person('alex',38,500)
egg = Dog('egon','二哈',20)
print(alex.life_value)
egg.bite(alex)   #Dog.bite(egg,alex)
print(alex.life_value)

alex.attack(egg)
print(egg.life_value)





















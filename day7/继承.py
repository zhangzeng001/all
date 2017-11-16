

# class Animal:
#     def __init__(self,name,aggr,life_value):
#         self.name = name
#         self.aggr = aggr
#         self.life_value = life_value
#
# class Dog(Animal):
#     def __init__(self,name,aggr,life_value,type):
#         Animal.__init__(self,name,aggr,life_value)
#         self.dog_type = type
#
# class  Persion(Animal):
#     pass
#
# egg = Dog('l1',100,10000,'haha')
# print(egg.__dict__)
# alex = Persion()


class shi:
    def __init__(self,name,age):
        self.name = name
        self.age = age



class shou(shi):
    def __init__(self,name,age,gan):
        super().__init__(name,age)
        self.gan = gan

cai = shou('cai',22,'gan')
print(cai.gan)

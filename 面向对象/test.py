# class Oldboy:
#     '''
#     haha
#     '''
#     school = 'oldboy'
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def skill(self):
#         print('%s kills is>> lern'%self.name)
#         print('%s kills is>> eat '%self.name)
#         print('%s kills is>> sleep'%self.name)
#
# zhang3 = oldboy('牛榴弹','male',18)
# print(zhang3.name)
# print(zhang3.sex)
# print(zhang3.age)
# zhang3.skill()
# print(zhang3.__dict__)
# print(zhang3.__dict__['sex'])
# s1 = oldboy('牛榴弹','male',18)
# print(Oldboy.__doc__)
# print(Oldboy.__class__)

# class Oldboystudy:
#     school = 'oldboy'
#     def learn(self):
#         print('is learning')
#     def eat(self):
#         print('is learning')
#     def sleep(self):
#         print('is sleeping')

# print(Oldboystudy.__dict__)
# print(Oldboystudy.school)
# s1 = Oldboystudy()
# print(s1.school)

# print(s1.school)


# import json
#
# dic = {'name':'huang','age':29,'sex':'female'}
# print(json.dumps(dic))
#
# f = open('db.json')
# data = json.loads(f.read())
# print(data)
# # data2 = json.load(f)
# # print(data2)
# f.close()



# import pickle
# dic={'name':'alvin','age':23,'sex':'male'}
# # print(type(dic))
# j = pickle.dumps(dic)
# print(j)
# x = pickle.loads(j)
# print(x)




db={
    'stu1':{
    'sex':'male',
    'age':18,
    'tel':13813813838,
    'course':'py'
    },
    'stu2':{
    'sex':'male',
    'age':19,
    'tel':13913913939,
    'course':'linux'
    },
    'teach1':{
    'sex':'male',
    'age':29,
    'tel':12912912929,
    'course':'linux'
    }
}

import pickle
class Base:
    def __init__(self,name,age,sex,role,tel,course):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.tel = tel
        self.course = course
    def save (self,a):
        with open('user.info','wb+') as f:
            b = f.read()
            print(b)
            if b:
                new_b = pickle.loads(b)
                # print(new_b)
                # print(self.name)
                new_b[self.name]={'sex':self.sex,'age':self.age,'tel':self.tel,'course':self.course}
                print(new_b)
                f.write(pickle.dumps(new_b))
            else:
                b={self.name:{'sex':self.sex,'age':self.age,'tel':self.tel,'course':self.course}}
                f.write(pickle.dumps(b))
            # if len(pickle.load(f)):
            #     print('ok')
            # else:
            #     print('false')
            # a = pickle.load(f)
            # a[self.name]={'sex':self.sex,'age':self.age,'tel':self.tel,'course':self.course}






class Student(Base):
    pass

class Teacher(Base):
    pass

class Course:
    #课程、周期、学费
    course_info = {'py':{'cycle':'9mouth','tuition':5000},
                   'linux':{'cycle':'5mouth','tuition':3000},
                   'go':{'cycle':'7mouth','tuition':4000}
                   }
    # py_info = {'cycle':'9mouth','tuition':5000}
    # linux_info = {'cycle':'5mouth','tuition':3000}
    # go_info = {'cycle':'7mouth','tuition':4000}

class School(Course):
    def bj(self):
        res = ['py','linux']
        # res = self.course_info['py'],self.course_info['linux']
        return res
    def shanghai(self):
        # res = self.course_info['go']
        res = 'go'
        return res



    # def bj(self,cou,cycle,tuition):
    #     l = {'course':self.cou,'cycle':self.cycle,'tuition':self.tuition}
    #     f = open('school_db','wb+')
    #     b = pickle.loads(f)
    # def shanghai(self,cou,cycle,tuition):
    #     print('go')






#登录接口
def login():
    u = input('username>>:')
#注册接口
def register():
    print('register')
#后台
def admin():
    print('admin')

def pro_init():
    dic = {
        '学员登陆：1':login,
        '用户注册：2':register,
        '后台管理：3':admin,
    }
    l = ['1','2','3','q']
    for i in dic:
        print(i)
    count = 0
    while True:
        # print(count)
        if count >=3:
            break
        m = input('\n输入序号选择["q"退出]>>:')
        if m not in l:
            print("选择序号错误！")
            count += 1
            continue
        if m == '1':
            login()
        if m == '2':
            register()
        if m == '3':
            admin()
        if m == 'q':
            break
        count += 1


if __name__ == '__main__':
    # pro_init()
    # a = Base('zhang',18,'male',138888,'py')
    # b = Student('zhang',23,'male','student',138888,'py')
    # print(a.course)
    # b.save()
    # a = Course
    a = School()
    print(a.shanghai())
    # print(a.py_info['tuition'])


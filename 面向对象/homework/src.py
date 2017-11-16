import pickle
class Base:
    def __init__(self,name,age,sex,tel,course,passwd,role):
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel
        self.course = course
        self.role = role
        self.passwd = passwd
        # self.school = school
    def save_persion(self):
        with open('db_persion','rb') as f:
            b = f.read()
            # print(b)
            if b:
                new_b = pickle.loads(b)
                # print(new_b)
                # print(self.name)
                new_b[self.name]={'role':self.role,'sex':self.sex,'age':self.age,'tel':self.tel,'course':self.course,'passwd':self.passwd}
                # print(new_b)
                # print(new_b)
                # print(pickle.dumps(new_b))
                with open('db_persion', 'wb') as p:
                    p.write(pickle.dumps(new_b))
            else:
                b={self.name:{'role':self.role,'sex':self.sex,'age':self.age,'tel':self.tel,'course':self.course,'passwd':self.passwd}}
                f.write(pickle.dumps(b))
    def save_school(self):
        with open('db_school','rb') as f:
            b = f.read()
            # print(b)
            if b:
                new_b = pickle.loads(b)
                # print(new_b)
                # print(self.name)
                new_b[self.course]={'teach':self.name,'age':self.age,'tel':self.tel,'school': self.school}
                # print(new_b)
                # print(new_b)
                # print(pickle.dumps(new_b))
                with open('db_school', 'wb') as p:
                    p.write(pickle.dumps(new_b))
            else:
                b={'teach':self.name,'age':self.age,'tel':self.tel,'school': self.school}
                f.write(pickle.dumps(b))



class Teacher(Base):
    def judge(self):
        # course_tmp = Course(self.name, self.age, self.tel,self.course)
        if self.course == 'linux' or self.course == 'py':
            print('beijing')
            self.school = 'beijing'
            self.save_school()

        else:
            print('shanghai')
            self.school = 'shanghai'
            self.save_school()




class Student(Base):
    pass

class Course:
    def __init__(self, cycle, tuition,cos):
        self.cycle = cycle
        self.tuition = tuition
        self.cos = cos
    def save_course(self):
        with open('db_cour','rb') as f:
            b = f.read()
            # print(b)
            if b:
                new_b = pickle.loads(b)
                # print(new_b)
                # print(self.name)
                new_b[self.cos]={'cycle':self.cycle,'tuition':self.tuition}
                # print(new_b)
                # print(new_b)
                # print(pickle.dumps(new_b))
                with open('db_cour', 'wb') as p:
                    p.write(pickle.dumps(new_b))
            else:
                print('数据库不存在')



#解析用户数据
def init_db(db):
    f = open(db, 'rb')
    a = f.read()
    pic = pickle.loads(a)
    f.close()
    return pic

def login():
    user_db = init_db('db_persion')
    count = 0
    # print(user_db)
    while True:
        if count >2:
            break
        username = input('username>>').strip()
        passowrd = input('password>>').strip()
        # print(str(user_db[username]['passwd']))
        if username in user_db and passowrd == str(user_db[username]['passwd']):
            return username
        else:
            print("用户不存在或密码错误！")
            count += 1
            continue


#添加讲师
def mk_teach(role):
    # teach_role = 'teach'
    teach_role = role
    teach_name = input('姓名>')
    teach_sex = input('性别>')
    teach_age = input('年龄>')
    teach_tel = input('电话>')
    teach_course = input('课程>')
    teach_pass = input('密码>')
    teach_tmp = Teacher(teach_name,teach_age,teach_sex,teach_tel,teach_course,teach_pass,teach_role)
    teach_tmp.save_persion()
    if role == 'teach':
        teach_tmp.judge()

def pro_init():
    dic = {
        '用户登陆：1':'login',
        '用户注册：2':'register',
        '后台管理：3':'admin',
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

    login_status={'username':'null','status':False}
    dic = {
        '用户登陆：1': 'login',
        '用户注册：2': 'register',
        # '后台管理：3': 'admin',
    }
    l = ['1', '2', 'q']
    # l = ['1', '2', '3', 'q']
    count = 0
    while True:
        print('+++++++++oldboy 选课系统++++++++\n')
        for i in dic:
            print(i)
        # print(count)
        if count >= 3:
            break
        m = input('\n输入序号选择["q"退出]>>:\n')
        if m not in l:
            print("选择序号错误！")
            count += 1
            continue
        if m == '1':
            l_login = login()
            # print(l_login)
            if l_login:
                login_status['username'] = l_login
            u_db = init_db('db_persion')
            db_course = init_db('db_school')
            l_role = u_db[l_login]['course']
            l_course = u_db[l_login]['course']
            l_teach = db_course['py']['teach']
            l_school = db_course['py']['school']
            if u_db[l_login]['role'] == 'student':
                if l_course == 'go':
                    l_school = 'shanghai'
                print("%s-->课程信息:^_^\n您报名的课程是：%s\t讲师：%s\t校区：%s" % (l_login, l_course, l_teach, l_school))
                break
            if u_db[l_login]['role'] == 'teach':
                if l_course == 'go':
                    l_school = 'shanghai'
                print("%s-->课程信息:--\n您执教的课程是：%s\t校区：%s" % (l_login, l_course, l_school))
                break
            if u_db[l_login]['role'] == 'admin':
                p = [1,2,3]
                k = int(input('管理员账户\n1、添加讲师\n2、课程管理\n3、返回上级\n').strip())
                if k == 1:
                    mk_teach('teach')
                if k == 2:
                    c_db = init_db('db_cour')
                    print("学校课程详情>>")
                    for i, n in c_db.items():
                        print(i, '\n', n)
                    n_t = input('更改课程>>')
                    if n_t == 'py':
                        c = input('更改课程周期>>')
                        t = int(input('更改课程费用>>'))
                        A=Course(c,t,n_t)
                        new_c_db = c_db['py']={'cycle':c, 'tuition': t}
                        print(new_c_db)
                        A.save_course()
                    if n_t == 'linux':
                        c = input('更改课程周期>>')
                        t = int(input('更改课程费用>>'))
                        new_c_db = c_db['py'] = {'cycle': c, 'tuition': t}
                        print(new_c_db)

                    if n_t == 'go':
                        c = input('更改课程周期>>')
                        t = int(input('更改课程费用>>'))
                        new_c_db = c_db['py'] = {'cycle': c, 'tuition': t}
                        print(new_c_db)

                if k == 3:
                    continue
        if m == '2':
            c_db = init_db('db_cour')
            print("学校课程详情>>")
            for i,n in c_db.items():
                print(i,'\n',n)
            mk_teach('student')
        # if m == '3':
        #     admin()
        if m == 'q':
            break
        count += 1


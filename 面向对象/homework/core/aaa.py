import pickle

db_persion = {
    'stu1': {
        'role': 'student',
        'sex': 'male',
        'age': 18,
        'tel': 13813813838,
        'course': 'py',
        'passwd': 123456
    },
    'admin': {
        'role': 'admin',
        'sex': 'male',
        'age': 18,
        'tel': 13813813838,
        'course': '*',
        'passwd': 666666
    },
}
##############
print(type(db_persion))
j = pickle.dumps(db_persion)
print(type(j))

f = open('db_persion','wb')
f.write(j)
f.close()
####################


# print(type(db_persion))
# j = pickle.dumps(db_persion)
# print(type(j))
#




f = open('db_persion','rb')
j = f.read()
f.close()
print(pickle.loads(j))


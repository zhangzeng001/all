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
    'teach1': {
        'role': 'teach',
        'sex': 'male',
        'age': 18,
        'tel': 13813813838,
        'course': 'py',
        'passwd': 123456
    },
}

print(type(db_persion))
j = pickle.dumps(db_persion)
print(type(j))

f = open('db_persion','wb')
f.write(j)
f.close()
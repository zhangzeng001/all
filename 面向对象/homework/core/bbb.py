import pickle

db_course = {
        'py': {
            'teach': 'laowang',
            'age': 18,
            'tel': 13813813838,
            'school': 'beijing'
        }
    }





# course_info = {'py': {'cycle': '3mouth', 'tuition': 3000},
#                        'linux': {'cycle': '2mouth', 'tuition': 4000},
#                        'go': {'cycle': '1mouth', 'tuition': 5000}
#                        }





##############
print(type(db_course))
j = pickle.dumps(db_course)
# print(type(j))

f = open('db_school','wb')
f.write(j)
f.close()
####################


# print(type(db_persion))
# j = pickle.dumps(db_persion)
# print(type(j))
#




f = open('db_cour','rb')
j = f.read()
f.close()
print(pickle.loads(j))

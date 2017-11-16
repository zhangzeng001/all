import optparse

parser = optparse.OptionParser()
parser.add_option('-u','--user',dest='user',help='Please input your user')
option,args = parser.parse_args()
print(option)
print(option.user)
# print(option.get('user'))
#
# if option['user'] == 'root' :
#     print("okokokok")


# a = {'a':1,'b':2}
# # a['a'] = 4
# # l = a['b']
# # print(a['b'])
# print(a['a'])
import yaml
import string
import os
from passlib.hash import sha512_crypt

GROUPS = 20
USERS = 26
TEACHERS = 10

allTheLetters = string.lowercase
groups = []
users = []
groupa_base = 'grupa'
for i in range(0, GROUPS):
    tmp = {}
    tmp['name'] = '_'.join((groupa_base, allTheLetters[i].upper()))
    tmp['home'] = os.path.join('/home/uczniowie', tmp['name'])
    groups.append(tmp)


password_def = sha512_crypt.encrypt('gimnazjum')
user1 = {}
user1['name'] = 'jan'
user1['update_password'] = False
user1['smbpassword'] = 'gimnazjum'
user1['groups'] = ['uczniowie', 'nauczyciele', 'adm', 'sudo', 'plugdev']
user1['password'] = password_def # sha512_crypt.encrypt('gimnazjum')
user1['move_home'] = True
user1['shell'] = '/bin/bash'
user1['home'] =  os.path.join('/home', 'nauczyciele', user1['name'])
users.append(user1)
user2 = {}
user2['name'] = 'ania'
user2['update_password'] = False
user2['smbpassword'] = 'gimnazjum'
user2['groups'] = ['uczniowie', 'nauczyciele' ]
user2['password'] = password_def # sha512_crypt.encrypt('gimnazjum')
user2['move_home'] = True
user2['shell'] = '/bin/bash'
user2['home'] =  os.path.join('/home', 'nauczyciele', user2['name'])
users.append(user2)
print(users)

# creat teachers
for i in range(0, 10):
    user = {};
    number = i
    if i < 10:
        number = '0' + str(number)
    user['name'] = ''.join(('nauczyciel', str(number)))
    user['smbpassword'] = 'gimnazjum'
    user['groups'] = ['uczniowie', 'nauczyciele' ]
    user['password'] = password_def # sha512_crypt.encrypt('gimnazjum')
    user['move_home'] = True
    user['shell'] = '/bin/bash'
    user['home'] =  os.path.join('/home', 'nauczyciele', user['name'])
    users.append(user)

for group in groups:
    for i in range(1, USERS):
        user = {};
        number = i
        if i < 10:
            number = '0' + str(number)
        user['name'] = ''.join((group['name'], str(number)))
        user['update_password'] = False
        user['smbpassword'] = 'gimnazjum'
        user['groups'] = []
        user['groups'].append(group['name'])
        user['groups'].append('uczniowie')
        user['password'] = password_def # sha512_crypt.encrypt('gimnazjum')
        user['move_home'] = True
        user['home'] =  os.path.join('/home','uczniowie', group['name'], user['name'])
        users.append(user)


tmp2 = {}
tmp2['name'] = 'uczniowie'
groups.append(tmp2)
tmp1= {}
tmp1['name'] = 'nauczyciele'
groups.append(tmp1)

data_to_save = {}
data_to_save['users_to_add'] = users
data_to_save['groups_to_add'] = groups
with open('users', 'w') as outfile:
    outfile.write(yaml.dump(data_to_save))
print('user saved to users to users')

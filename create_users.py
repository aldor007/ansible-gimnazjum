import yaml
import string
import os
from passlib.hash import sha512_crypt

GROUPS = 15
USERS = 26

allTheLetters = string.lowercase

print(allTheLetters)
users = []
groups = []
groupa_base = 'grupa'
for i in range(0, GROUPS):
    tmp = {}
    tmp['name'] = '_'.join((groupa_base, allTheLetters[i].upper()))
    groups.append(tmp)


print(groups)
password_def = sha512_crypt.encrypt('gimnazjum')
for group in groups:
    for i in range(1, USERS):
        user = {};
        number = i
        if i < 10:
            number = '0' + str(number)
        user['name'] = ''.join((group['name'], str(number)))
        user['groups'] = []
        user['groups'].append(group['name'])
        user['groups'].append('uczniowie')
        user['password'] = password_def # sha512_crypt.encrypt('gimnazjum')
        user['move_home'] = True
        user['home'] =  os.path.join('/home', group['name'], user['name'])
        users.append(user)


print(users)
data_to_save = {}
data_to_save['users'] = users
data_to_save['groups'] = groups
with open('data.yml', 'w') as outfile:
    outfile.write(yaml.dump(data_to_save))







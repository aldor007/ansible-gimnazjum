import yaml
import string
import os
from passlib.hash import sha512_crypt

GROUPS = 20

allTheLetters = string.lowercase

shares = []
groups = []
groupa_base = 'grupa'
for i in range(0, GROUPS):
    tmp = {}
    tmp['name'] = '_'.join((groupa_base, allTheLetters[i]))
    groups.append(tmp)


password_def = sha512_crypt.encrypt('gimnazjum')
for group in groups:
    share = {};
    share['name'] = group['name']
    share['comment'] = "pliki " + group['name']
    share['path'] =  os.path.join('/home/prace', group['name'])
    share['group'] = group['name']
    share['onwer'] = group['name']
    share['valid_users'] = '+nauczyciele ' + '+' + group['name']
    share['write_list'] = '+nauczyciele ' + '+' + group['name']
    share['browseable'] = 'yes'
    share['guest_ok'] = 'no'
    shares.append(share)


data_to_save = {}
data_to_save['shares'] = shares
with open('data_shares.yml', 'w') as outfile:
    outfile.write(yaml.dump(data_to_save))







from time import sleep

import emoji as emoji

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Fogos!!')
print(emoji.emojize(':tada:'*10, language='alias'))

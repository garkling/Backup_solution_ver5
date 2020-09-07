import os
import time
import zipfile

def_source = input('Enter the files direction: ')
print('Done -> %s' % def_source)
target_dir = input('Enter the target direction: ')
print('Done -> %s' % target_dir)

today = target_dir + os.sep + time.strftime('%Y-%m-%d')
now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

avoid_symbols = ["\"", '/', ':', '*', '?', '''"''', '<', '>', '|']

if not os.path.exists(today):
    os.mkdir(today)
    print('Catalog creating success! Path -', today)

b = 1
wish_comment = input("Want to comment the archive? ")
if wish_comment == 'Yes':
    while b == 1:
        b = 0
        comment = input('''Enter a comment (avoid using symbols like "\/:*?"<>|"): ''')
        for i in avoid_symbols:
            if i in comment:
                print("Avoid incorrect symbols! Again")
                b = 1
                break
            else:
                continue
        if len(comment) > 0:
            target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
else:
    pass

x = zipfile.ZipFile(target, 'w')
for root, dirs, files in os.walk(def_source):
    for file in files:
        x.write(os.path.join(root, file))

x.close()

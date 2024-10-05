file = open('Codingal.txt', 'r')

new_file = open('NewFile.txt',  'w')

for line in file.readlines():
    if not line.startswith('Coding'):
        print(line)
        new_file.write(line)

file.close()
new_file.close()


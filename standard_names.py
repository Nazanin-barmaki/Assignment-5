name_list = []

for i in range(10):

    name = input('enter the name you want: ')

    name = name.lower()
    first = name[0]
    up = first.upper()

    name = name.replace(name[0], up, 1)
    name_list.append(name)

print('your standadr name:')
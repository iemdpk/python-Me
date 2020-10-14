print("Hello World")


print("==================================================")

dict = {
    'name' : 'Mohan',
    'class':'10th',
    'addr' : 'delhi',
}

print(dict)

print("==================================================")

dict['rollno'] = 20

print(dict)


print("==================================================")

print(dict['rollno'])

b = dict.get('addr')

print(b)


print("==================================================")

dict.pop('rollno')

print(dict)


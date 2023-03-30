import os

# with open('file1.txt', 'r') as f:
#   print(type(f))
#   result = f.readline()
#   print(type(result))
#   print(result)

# with open('file1.txt', 'a') as f:
#   print(type(f))
#   result = f.write('Hello, world!\n')
#   result = f.write('Hello, world!\n')
#   print(type(result))
#   print(result)

# lines = ['1\n', '2\n', '3\n', '4\n']
# with open('file1.txt', 'a') as f:
#   print(type(f))
#   result = f.writelines(lines)
#   print(type(result))
#   print(result)

# lines = ['1\n', '2\n', '3\n', '4\n']
# with open('file5.txt', 'x') as f:
#   print(type(f))
#   result = f.writelines(lines)
#   print(type(result))
#   print(result)
#
# os.remove('file5.txt')

# with open('file1.txt', 'w', encoding = 'utf-8') as f:
#   print(type(f))
#   result = f.write('Привет\n')

# import requests # pip install requests
# URL = 'https://www.pnp.ru/upload/entities/2021/04/19/18/article/detailPicture/7e/66/9f/55/23c871532e2289d5791561c8adda1a1a.jpg'
# response = requests.get(URL)
# with open('spase.jpg', 'wb') as file:
#   file.write(response.content)


with open('file8.txt', 'rt', encoding = 'utf-8') as file:
  departments = {}
  for line in file:
    dep_name = line.strip()
    employees_count = int(file.readline().strip())
    employees = []
    for _ in range(employees_count):
      name, last_name, date, city = file.readline().strip().split(' | ')
      employees.append({
        'name': name,
        'last_name': last_name,
        'date': date,
        'city': city
      })
    file.readline()
    departments['dep name'] = dep_name

print(employees)
from pprint import pprint
import re

# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

# номер телефона в требуемом формате
new_list = []
pattern = re.compile(r'(\+7|8)?\s*\(*(\d{3})\)*?\s*\-*(\d{3})\-*(\d{2})\-*(\d{2})?\s*\(*([а-я]+\.)*\s*(\d{4})*\)*')

for line in contacts_list:
  fio = list((line[0].split(' ') + line[1].split(' ') + line[2].split(' ')))
#print(fio)
  line[5] = pattern.sub(r"+7(\2)\3-\4-\5 \6\7", line[5])
  #print(line[5])
  line = [fio[0] + ' ' + fio[1], fio[2], line[3], line[5], line[6]]
  #print(line)
  new_list.append(line)

new_list = sorted(new_list)
#print(new_list)

# объединяем дублирующиеся записи
final_list = [new_list[0][0].split(' ') + new_list[0][1:]]
j = len(new_list)
#print(j)
#print (new_list)

while j != 1:
  if j > 3 and new_list[1][0] == new_list[2][0]:
    j -= 2
    new_line = new_list[1][0].split(' ')
    for i in range(2, 5):
      if new_list[1][i] != '':
        new_line.append(new_list[1][i])
      else:
        new_line.append(new_list[2][i])

    new_list.remove(new_list[1])
    new_list.remove(new_list[1])

  else:
    j -= 1
    new_line = new_list[1][0].split(' ') + new_list[1][1:]
    new_list.remove(new_list[1])

  final_list.append(new_line)

  # сохраняем файл в формате CSV
  with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(final_list)

    with open("phonebook.csv", encoding='utf-8') as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)

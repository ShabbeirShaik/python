f=open("c://data//book.txt","r")#specify the path of the file that you want to read
s=f.read()
print(s)
import json
main_book=json.loads(s)
print(type(main_book))
print(main_book['sajid'])
print(main_book['sajid']['phone'])
for person in main_book:
  print(main_book[person])

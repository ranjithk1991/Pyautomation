'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:/Users/Ranjit/Downloads/chromedriver_win32/chromedriver.exe")
print ("Loading facebook site....")
driver.get("https://www.facebook.com")
driver.close()'''
'''mylist = [1, 2, [1, 7], 4, 8]
mylist[2] = 1000
print(mylist)
# print("re" * 3)
mylist.remove(8)
mylist.reverse()
mylist[2:] = [1, 99]
print(mylist)
mylist[3:] = []
print(mylist)'''
'''powr = [2 ** x for x in range(10) if x > 4]
print(powr)'''

'''t_tuple = 1,2,'ABC'
print(t_tuple)

a, b, c = t_tuple
print(a)
print(t_tuple[0])

j_list = [1, 4, 5]
print(j_list * 3)
print(t_tuple * 2)

for i in range(4):
    print(str(i) + " Go")

abc = 'HelloWorld'
print(len(abc))
for i in range(len(abc)):
    if i < 4:
        print('Found' + str(i))
    else:
        print('Not found')
# list comprehension
test = [2 ** x for x in range(10)]
print(test)'''
'''
import pyautogui
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
pyautogui.rightClick()
'''

"""name = "Ranjith Kumar"
count = 0
for i in name:
    if i == 'a':
        print('Letter "a" found at', count, 'th position')
    else:
        count = count + 1 
"""

'''dict1 = {'A': {1: 'Ranjith', 2: 'Maddy', 3: 'Rocky'},
         'B': {4: 'Liya', 5: 'Mary', 6: 'Karen'}
         }
for a, b in dict1.items():
    print('Item=', a)
    for key in b:
        print(b[key])'''

'''test_file = open("tst.txt", 'w')
# test_file.tell()
test_file.write("THis is just a text document with dummy content")
test_file.close()

with open("test2.txt", 'w') as F:
    F.write("This is just a text document created to verify ")
'''
'''import csv

with open("CSVtest.csv", 'r') as CSVFile:
    reader = csv.reader(CSVFile)
    for line in reader:
        print(line)

with open("CSVtest.csv", 'w', newline='') as WFile:
    writer = csv.writer(WFile)
    writer.writerow(['5', 'Rakul', 'JE'])
    writer.writerow(['7', 'Gokul', 'ME'])
    print(WFile)
    rowlist = [['8', 'Maddy', 'IOP'], ['9', 'Kile', 'HAW']]
    writer.writerows(rowlist)
    print(WFile)'''
'''import csv
import pandas as pd
with open('CSVtest.csv', 'r') as DFile:
    Dict = csv.DictReader(DFile)
    for line in Dict:
        print(dict(line))
with open('CSVtest.csv', 'w', newline='') as DWFILE:
    fieldnam = {'RollNo', 'Person'}
    W = csv.DictWriter(DWFILE, fieldnames=fieldnam)
    W.writeheader()
    W.writerow({'RollNo': 200, 'Person': 'Kumar'})
    print(DWFILE)



df = pd.DataFrame([[1, 'User1'], [2, 'User2']], columns=['S.No', 'Name'])
df.to_csv('Ranjith.csv')
rd = pd.read_csv('Ranjith.csv')
print(rd)'''

'''import array as ar
arr = ar.array('i', [1, 2, 3, 4, 6])
print(arr[4])
a1 = ar.array('i', [201, 211, 221, 231, 241, 251])
a2 = ar.array('i', [20, 21, 22, 23, 24, 25])
a3 = ar.array('i')
a3 = a1 + a2
print(a3)'''

'''Matrix1 = [[1, 2, 4],
          [5, 8, 9],
          [10, 11, 12]]
Matrix2 = [[4, 5, 6],
           [6, 7, 8],
           [9, 4, 2]]
Result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(Matrix1)):
    for j in range(len(Matrix1[0])):
        Result[i][j] = Matrix1[j][i]
for r in Result:
    print(r)
Result = [[Matrix1[j][i] for j in range(len(Matrix1[0]))] for i in range(len(Matrix1))]

for r in Result:
    print(r)'''
'''
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()'''
import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()
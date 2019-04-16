Microsoft Windows [Version 10.0.17763.379]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\User\Documents\PrakGUI\Basic_Python>python
Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> myfile open ("perangkat.txt")
  File "<stdin>", line 1
    myfile open ("perangkat.txt")
              ^
SyntaxError: invalid syntax
>>> myfile= open ("perangkat.txt")
>>> content = myfile.read()
>>> myfile.close()
>>> print(content)
RAM
SSD
HARDISK
CPU
>>> myfile= open ("perangkat.txt")
>>> type(myfile)
<class '_io.TextIOWrapper'>
>>> myfile.read()
'RAM\nSSD\nHARDISK\nCPU'
>>> myfile.read()
''
>>> myfile.seek(0)
0
>>> myfile.read()
'RAM\nSSD\nHARDISK\nCPU'
>>> print {myfile.read()}
  File "<stdin>", line 1
    print {myfile.read()}
          ^
SyntaxError: invalid syntax
>>> print [myfile.read()]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print{myfile.read()}
  File "<stdin>", line 1
    print{myfile.read()}
         ^
SyntaxError: invalid syntax
>>> myfile.seek(0)
0
>>> print{myfile.read()}
  File "<stdin>", line 1
    print{myfile.read()}
         ^
SyntaxError: invalid syntax
>>> myfile open ("prodi.txt")
  File "<stdin>", line 1
    myfile open ("prodi.txt")
              ^
SyntaxError: invalid syntax
>>> myfile= open ("perangkat.txt")
>>> content = myfile.read()
>>> myfile.close()
>>> print(content)
RAM
SSD
HARDISK
CPU
>>> myfile= open ("prodi.txt")
>>> content = myfile.read()
>>> myfile.close()
>>> print(content)
Elektro
Informatika
Teknik Industri
Sistem Informasi
Desain Komunikasi Visual
Rekayasa Perangkat Lunak
>>> type(myfile)
<class '_io.TextIOWrapper'>
>>> myfile.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> myfile.seek(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> print{"Hello\Word"}
  File "<stdin>", line 1
    print{"Hello\Word"}
         ^
SyntaxError: invalid syntax
>>> print("Hello\Word")
Hello\Word
>>> a = [1,2,3]
>>> printa(a[2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'printa' is not defined
>>> print(a[2])
3
>>> print(a[0])
1
>>> for item in a:
...     print(item)
...
1
2
3
>>> b='Hello'
>>> for item in b:
...     print(item)
...
H
e
l
l
o
>>> blackpink = ["Lisa","Jennie","Rose","Ji-Soo"]
>>> for item in blackpink:
...     print(item)
...
Lisa
Jennie
Rose
Ji-Soo
>>> a = [1,3,5,7,9]
>>> for i in a:
...     b= i+10
...     print(b)
...
11
13
15
17
19
>>> a = [3,4,6,11,2,17,90]
>>>     b= i+5
  File "<stdin>", line 1
    b= i+5
    ^
IndentationError: unexpected indent
>>> mylise = [3,4,6,11,2,17,90]
>>> for i in mylise:
...     if(i>5)
  File "<stdin>", line 2
    if(i>5)
          ^
SyntaxError: invalid syntax
>>> mylise = [3,4,6,11,2,17,90]
>>>     if(i>5):
  File "<stdin>", line 1
    if(i>5):
    ^
IndentationError: unexpected indent
>>> mylise = [3,4,6,11,2,17,90]
>>> for i in mylise:
...     if(i>5):
...     print(i)
  File "<stdin>", line 3
    print(i)
        ^
IndentationError: expected an indented block
>>> mylise = [3,4,6,11,2,17,90]
>>> for i in mylise:
...     if(i>5):
...      print(i)
  File "<stdin>", line 3
    print(i)
           ^
IndentationError: unindent does not match any outer indentation level
>>> mylise = [3,4,6,11,2,17,90]
>>> for t in mylise:
...     if(i>5):
...      print(t)
...
3
4
6
11
2
17
90
>>> mylise = [3,4,6,11,2,17,90]
>>> for t in mylise:
...     if(t>5):
...      print(t)
...
6
11
17
90
>>> terperatures=[10,20,100]
>>> def cel_to_fahr(celcius):
...     fahrenheit = (celcius *9/5 + 32
...     return fahrenheit
  File "<stdin>", line 3
    return fahrenheit
         ^
SyntaxError: invalid syntax
>>> def cel_to_fahr(celcius):
...     fahrenheit = (celcius *9/5) + 32
...     return fahrenheit
...
>>>
>>> for hasil in terperatures:
...     print(cel_to_fahr(terperatures))
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in cel_to_fahr
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> for hasil in terperatures:
...     print(cel_to_fahr(hasil))
...
50.0
68.0
212.0
>>> myfile = open ("pegawai.txt","w")
>>> myfile.write("PrincesBen")
10
>>> myfile.close()
>>> myfile = open ("pegawai.txt","w")
>>> myfile.write("Gojes")
5
>>> myfile.write("jisoong")
7
>>> myfile.close()
>>> myfile = open ("pegawai.txt","w")
>>> myfile.write("PrincesBen")
10
>>> myfile.write("\njisoong")
8
>>> myfile.write("\nGojes")
6
>>> myfile.close()
>>> myfile = open ("pegawai.txt","a")
>>> myfile.write("\nbangjamal")
10
>>> myfile.write("\nyudikumisyt")
12
>>> myfile.close()
>>> myfile = open ("pegawai.txt","a+")
>>> myfile.read()
''
>>> myfile.seek()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: seek() takes at least 1 argument (0 given)
>>> myfile.seek(0)
0
>>> myfile.read()
'PrincesBen\njisoong\nGojes\nbangjamal\nyudikumisyt'
>>> myfile.write("\nmijon")
6
>>> myfile.close()
>>>

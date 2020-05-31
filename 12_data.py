"""
    ---------------------------data files --------------------------------
    1. you can store (save) data in python
    2. the .txt, .csv files should be stored in the same folders as your .py files (not mandatory)
    3. Keywords
       with - instructs python to close file
       as   - assigns a handle to the file
       open - open file
       'w'  - write to a file (this will also **** delete existing data*****)
       'w+' - write and read a file
       'r'  - read file
       'a'  - add data to a file
"""
""" 
    ------------------------- write to a file --------------------------------
"""
county = ['Bedfordshire', 'Berkshire', 'Bristol', 'Buckinghamshire', 'Cambridgeshire', 'Cheshire', 'Cornwall',
          'County Durham', 'Cumberland', 'Derbyshire', 'Devon', 'Dorset', 'Essex']

with open('text.txt', 'w') as f:
    f.write('devon')
    f.write(str(county))
""" 
    ------------------------- read file -------------------------------- 
    1. to read a file you will assign its contents into a variable
    2. note 'r' is the default mode for 'open' so you don't have to include it 
"""
with open('text.txt', 'r') as g:  # ('text.txt') will also work
    content = g.read()
    print(content)
""" 
    ------------------------- add data to a file -------------------------------- 
    1. a (mode) is used to add data to existing data 
    2. you have to create a variable (like read) and assign the file contents to view added data
    
"""
countyb = ['sussex', 'kent', 'staffordshire', 'lancastershire', 'yorkshire', 'oxford']
with open('text.txt', 'a') as q:
    q.write(str(countyb))
with open('text.txt', 'r') as c:
    contents = c.read()
    print(contents)


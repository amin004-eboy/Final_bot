import sqlite3
conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users
(TELEGRAM_ID INTEGER , 
USER_NAME STRING , 
PHONE INTEGER ,
LESSON_TIME STRING ,
AGE_GROUP STRING
)
''')

reg_in_table = '''INSERT INTO Users VALUES (0,'{}', 0 , '{}', '{}')'''

phone_in_table = '''
SELECT PHONE 
FROM Users
WHERE TELEGRAM_ID = '{}'
'''

update_phone_in_table = '''
UPDATE Users
SET PHONE ='{}'
WHERE TELEGRAM_ID = '{}' 
'''

group_in_table = '''
SELECT PHONE 
FROM Users
WHERE TELEGRAM_ID = '{}'
'''

update_group_in_table = '''
UPDATE Users
SET PHONE ='{}'
WHERE TELEGRAM_ID = '{}' 
'''

time_in_table = '''
SELECT PHONE 
FROM Users
WHERE TELEGRAM_ID = '{}'
'''

update_time_in_table = '''
UPDATE Users
SET PHONE ='{}'
WHERE TELEGRAM_ID = '{}' 
'''
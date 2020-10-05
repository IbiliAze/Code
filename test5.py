import base64

location = r'C:\Users\ibili\Downloads\s1.txt'
file_string = open(location, 'r').read()

file_encode = file_string.encode('base64')



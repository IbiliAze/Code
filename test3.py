import base64

location = r'C:\Users\ibili\Downloads\s1.txt'
file_string = open(location, 'r').read()
file_ascii = file_string.encode('ascii')
file_base64 = base64.b64encode(file_ascii)

print(f"{file_base64}")
print()


dict1 = {
    'configFile': f"{file_base64}"
}


print(dict1['configFile'])
print()

decode_content = base64.b64decode(file_base64)
print(decode_content)
print()

print(decode_content.decode('ascii'))


new = dict1['configFile'].bytes()
if file_base64 == new:
    print('yes')
else:
    print('no')
print(type(new))
print(type(file_base64))
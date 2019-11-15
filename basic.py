import re 

#* Say you want to find a phone number using regular expression
message = 'Call me at 732-668-6908 or 646-671-0903'
phone_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_number.findall(message)
print(mo)

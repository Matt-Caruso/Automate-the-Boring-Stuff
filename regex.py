#Regex concepts

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Hello, I wanted to leave my number here. Its 203-442-3456, Thanks!')
print('Phone number found: ' + mo.group())

#Groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('Hello, I wanted to leave my number here. Its 203-442-3456, Thanks!')
print('Area Code found: ' + mo.group(1))
print('Number found: ' + mo.group(2))
print('Phone number found: ' + mo.group(0))

print('Groups found: ', mo.groups())

#| Pipe

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

#? Optional
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

#* zero or more
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batwowowowowoman')
print(mo1.group())

#+ atleast once
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batwowowowowoman')
print(mo1.group())
mo1 = batRegex.search('The adventures of Batwoman')
print(mo1.group())
#!/usr/bin/python3

greetings='Hello'
name='kushagra'

message="{0}, {1}. welcome!".format(greetings,name.upper())
message2=f"{greetings}, {name}. welcome!"

print(message)
print(message2)
print(dir(name))
print(help(str))

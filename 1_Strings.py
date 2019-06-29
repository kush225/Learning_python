#!/usr/bin/python3

greetings='Hello'
name='kushagra'

message="{0}, {1}. welcome!".format(greetings,name.upper())
print(message)

message2=f"{greetings}, {name}. welcome!"
print(message2)

print(dir(name))
print(help(str))

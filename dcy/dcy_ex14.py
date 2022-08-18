#filename:dcy_ex14.py

from sys import argv

script, user_name =  argv 
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask u a few questions.")
print(f"Do u like me {user_name}?") #yuuueeeee
likes = input(prompt)

print(f"Where do u live {user_name}?")
lives = input(prompt)

print("What kind of computer do u have?")
computer = input(prompt)

print(f"""
Alright, so u said {likes} about liking me.
You live in {lives}.Not sure where that is.
And u have a {computer} computer. Nice.
""")
#简单的试了试用户提示符（提示用户输入），并且如果想更改的话直接改开头


print(" \n " * 60)

print("Welcome adventurer! \n \n \nThe Magical Sphinx wont wait long! \n ")
print("Please enter your name")

name = input()
str(name)

print(" \n " * 60)

print( f"Welcome {name.upper()} This is your chance to finally get the magical Holy Grail! \n ")
print("***First Riddle*** \n \nWhat gets bigger the more you take away? ")

first_answer = input()

str(first_answer)

"first_answer".lower()

if first_answer.lower() == "hole":
	print(" \n " * 60)
	print("Correct!!")
	print("On to the second room")

elif first_answer.lower() == "a hole":
	print(" \n " * 60)
	print("Correct!!")
	print("On to the second room")
else:
	print(" \n " * 60)
	print("You Lose!!")
	quit()
print(" \n " * 10)

print("***Second Riddle*** \n \nWhat has four fingers and a thumb, but isn’t alive? ")
second_answer = input()

str(second_answer)

if second_answer.lower() == "glove":
	print(" \n " * 60)
	print("Correct!!")
	print("On to the third room")

elif second_answer.lower() == "a glove":
	print(" \n " * 60)
	print("Correct!!")
	print("On to the third room")
else:
	print(" \n " * 60)
	print("You Lose!!")
	quit()


print(" \n " * 10)

print("***Third Riddle*** \n \nIf you have me, you will want to share me. If you share me, you will no longer have me. What am I? ")
third_answer = input()

str(third_answer)

if third_answer.lower() == "secret":
	print(" \n " * 60)
	print("Correct!!")
	print(" \n " * 10)
	print("On to the Holiest of Holies")

elif third_answer.lower() == "a secret":
	print(" \n " * 60)
	print("Correct!!")
	print(" \n " * 10)
	print("On to the Holiest of Holies")
else:
	print(" \n " * 60)
	print("You Lose!!")
	print(" \n " * 10)
	quit()

grail = ("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ : : : : : : : : : : : : : : : @
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 |                             |
 |  \|/        %%%        \|/  |
 |  -t-     %%%%%%%%%     -t-  |
 |  /|\     \  %%%  /     /|\  |
 |         \ / %%% \ /         |
 \        - |  %%%  | -        /
  \       - |  %%%  | -       /
   \       / \     / \       /
    \        / --- \        /
     \         ! !         /
      \ __ ___ __ ___ ___ /
      ( ___ ___ __ _ ___  )
       (88888888888888888)
        --\ --------- /--
          ((((((o))))))
           \         /
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
          _(IIIIIIIII)_
       __/_____________\__
  ____/___________________\____
 /_____________________________\
(_______________________________)""")

print(grail)

print(f"***Congratulations*** {name.upper()} !!")
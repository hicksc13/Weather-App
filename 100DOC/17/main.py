#deploying a self made class. self is refering to this class and the ".X" is the attrinutes so self.id is setting the "id" for the "user class"
        # if you put it into the paramaters then you HAVE to have it defined later on. you can also set the defualt values just like the self.followers = 0 
        # Can put 'pass' after class user: if you dont want to define everything so far. 

class User:
    def __init__(self, user_id,username): 
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0 

    def follow(self, user):
        user.followers += 1
        self.following += 1



class Car:
    def enter_race_mode():
        self.seats = 2

#variable = class(paramerters, paramaters)
user_1 = User("001", "cody")
user_2 = User("002", "jack")



#object.methond(paramerters)
user_1.follow(user_2)
user_2.follow(user_1)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)







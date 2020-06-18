import sys
user1 = input("enter your name:--> ")
user2 = input("and your name:--> ")
user1_choice = input("%s, what will you take : 'stone','paper','scissor'--> " % user1)
user2_choice = input("%s, what will you take : 'stone','paper','scissor'--> " % user2)
def compare(u1,u2):
    if u1==u2:
        return("it's a tie ")
    elif u1== "stone":
        if u2 == "scissor":
            return(user1,"wins")
        else:
            return(user2,"wins")
    elif u1 == "scissor":
        if user2 == "paper":
            return(user1,"wins")
        else:   
            return(user2,"wins")
    elif user1 == "paper":
        if user2 == "stone":
            return(user1,"wins")
        else:
            return(user2,"wins")
    else:
        return("invalid input, you have not entered stone,paper or scissor ")
        sys.exit()
print(compare(user1_choice,user2_choice))


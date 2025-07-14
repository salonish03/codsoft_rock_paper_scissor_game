import random

#choices available
choices=["rock","paper","scissors"]

#scores
user_score=0
computer_score=0

def get_winner(user,computer):
    if user==computer:
        return "Tie"
    elif (user=="rock" and computer=="scissors") or\
         (user=="scissors" and computer=="paper")or\
         (user=="paper" and computer=="rock"):
        return "user"
    else:
        return "computer"

print("Welcome to Rock-Paper-Scissors Game")


while True:
    print("\n Choose one: rock,paper or scissors")
    user_choice=input("Your Choice:").lower()

    if user_choice not in choices:
        print("Invalid choice")
        continue

    
    computer_choice=random.choice(choices)
    print(f"Computer chose:{computer_choice}")

    result= get_winner(user_choice, computer_choice)

    if result=="Tie":
        print("Its a tie")
    elif result=="user":
        print("You win the round")
        user_score+=1
    else:
        print("computer wins this round")
        computer_score+=1

    print(f"Score=>You:{user_score}| Computer:{computer_score}")

    again=input("Do you want to play again?(yes/no):").lower()
    if again!="yes":
        print("Thanks for playing. Final score is :")
        print(f"Score=>You:{user_score}| Computer:{computer_score}")
        break
    
        
         

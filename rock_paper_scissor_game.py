import random
def game():
    user = input("Choose between 'r' for rock, 'p' for paper and 's' for scissor.")
    comp = random.choice(['r', 'p', 's'])
    print(f"You have chosen {user}")
    print(f"The computer has chosen {comp}")

    if  user == comp:
        return "It is a tie"

    if win(user, comp):
        return "You have won!"
    if win(comp, user):
        return "Computer has won!"

def win(player, opponent):
    #conditions for win is r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(game())
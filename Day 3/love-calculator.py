# Welcome to Love Calculator App
print('Time to know how strong your love is between you and your partner!')
# collecting love birds' names
user_name = input('What is your full name?\n').lower()
partner_name = input("What is your partner's full name?\n").lower()
# combining their names for easy check
name_together = user_name + partner_name

# scores
score1 = 0
score2 = 0

# checking their names for T-R-U-E L-O-V-E
score1 += name_together.count('t')
score1 += name_together.count('r')
score1 += name_together.count('u')
score1 += name_together.count('e')

score2 += name_together.count('l')
score2 += name_together.count('o')
score2 += name_together.count('v')
score2 += name_together.count('e')

total_score = int(f'{score1}{score2}')
# reporting result back to user
if total_score < 10 or total_score > 90:
    print(f'Your score is {total_score}, you go together like coke and mentos.')
elif total_score >= 40 and total_score <= 50:
    print(f'Your score is {total_score}, you are alright together')
else:
    print(f'Your score is {total_score}.')
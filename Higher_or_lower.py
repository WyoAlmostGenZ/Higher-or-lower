import random
from dataforhigherorlower import data
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
#############################################################################################



def game():

	game_is_on = True
	score = 0

	print(logo)
	while game_is_on:
		celeb_dict = random.choice(data)
		another_celeb_dict = random.choice(data)
		One = celeb_dict["follower_count"]
		Two = another_celeb_dict["follower_count"]
		print(f"Compare A:  {celeb_dict['name']} a {celeb_dict['description']} from {celeb_dict['country']}")
		print(vs)
		print(f"Compare B:  {another_celeb_dict['name']} a {another_celeb_dict['description']} from {another_celeb_dict['country']}")
		inputeroni = input("Who has more followers type 'A' or 'B' : \n")
		if inputeroni == "A" and One > Two:
			score = score + 1
			print(f"You're right ! score {score}")
	# if input == ''B'' or anything else
		elif inputeroni == "B" and Two > One:
			score = score + 1
			print(f"You're right ! score {score}")
		else:
			print(f"You got it wrong the final score {score}")
			game_is_on = False


game()






# Lila Shearer, Silly Sentences Python

print("\nWelcome to silly sentence generator!\nThe purpose of this program is to create a silly sentence using words that you, the user, provides.\nYou don't get to see the sentence until after you have provided words, making it a fun suprise.\n")
print("\nWhen answering questions for this program, please provide one word answers only.\n")
description_of_something = input("\nPlease provide a one-word description of something (ex: yellow, shiny, rough): \n")
action_word = input("\nAlright. Now please provide a one-word action (ex: running, jumping, swimming): \n")
noun = input("\nSweet. Now please provide a noun (a person, place, or thing): \n")
location = input("\nAwesome. Now please provide a one-word place -excluding the word 'the'- (ex: library, school, jail): \n")
time_of_day = input("\nOk. Now please provide a time of day (ex: noon, afternoon, midnight): \n")
famous_person = input("\nGood choice! Now please provide the last name of a famous person (ex: Washington, Jefferson, Hamilton): \n")
name_of_town = input("\nSounds good. Now please provide a one-word name of a town (ex: Lehi, Seattle, Chicago): \n")
print("\nYour silly sentence is complete! Here it is:\n")
print(f"\nMy {description_of_something} bike is my most prized possesion.The story of how I got it is a long one, but I'm sure you'd love to hear the tale. I was {action_word} down the street with my {noun}. I was heading to {location} because that's where I go every {time_of_day}. As I turned the corner, I stopped dead in my tracks. {famous_person}?! In {name_of_town}?! They stopped and looked at me. 'Do you know where the {location} is?' They asked. I nodded, so shocked I was barely able to speak. 'That's where I'm headed too!' I announced. Together we walked to the {location} and we became friends. Soon, {famous_person} had to leave to go attend some important meetings. As a parting gift, they gave me my bike. That is the story of how I got my {description_of_something} bike.")
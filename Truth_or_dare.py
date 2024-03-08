#TRUTH OR DARE
#Authors: Prabraj Singh, Aritha Bandara, Chanhwan Park


import random
import pygame 

pygame.mixer.init()

#Game Music
def play_music(file_path):
    pygame.mixer.music.load(file_path)  
    pygame.mixer.music.play(-1)  

#Game Data
    #Users may enter their choice of statements here
def get_truth():
    truths = [
        "What is your biggest fear?",
        "Have you ever cheated on a test?",
        "What is your most embarrassing moment?",
        "If you could switch lives with someone for a day, who would it be?",
        "What's the worst thing you've ever done at work?",
        "Do you have any fetishes?",
        "What's something you're glad your family doesn't know about you?",
        "Have you ever cheated on someone?",
        "What's the worst thing you've ever done?",
        "What are your thoughts on polyamory?",
        "What's the worst intimate experience you've ever had?",
        "What's the best intimate experience you've ever had?",
        "Have you ever broken the law?"
    ]
    return random.choice(truths)
#Users may enter their choice of statements here
def get_dare():
    dares = [
        "Do 10 jumping jacks.",
        "Sing your favorite song out loud.",
        "Send a silly text to the third person in your contact list.",
        "Wear socks on your hands for the next 5 minutes.",
        "Give a foot massage to the person on your right",
        "Put 10 different available liquids into a cup and drink it",
        "Try and get all the toes on one foot in your mouth",
        "Try to put your whole fist in your mouth",
        "Tell everyone an embarrassing story about yourself",
        "Try to lick your elbow",
        "Peel a banana with your toes",
        "Say everything in a whisper for the next 10 minutes",
        "Smell another player's armpit",
        "Put as many snacks into your mouth at once as you can",
    ]
    return random.choice(dares)


#Game Execution (do not edit)
def main():
    print("Welcome to Truth or Dare!")

   
    music_file = 'music.mp3' 
    play_music(music_file)


    while True:
        player_choice = input("Enter 't' for truth, 'd' for dare, or 'q' to quit: ").lower()

        if player_choice == 't':
            print("Truth: " + get_truth())
        elif player_choice == 'd':
            print("Dare: " + get_dare())
        elif player_choice == 'q':
            pygame.mixer.music.stop()  
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 't', 'd', or 'q'.")


if __name__ == "__main__":
    main()
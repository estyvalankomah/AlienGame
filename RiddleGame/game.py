import random

stars = 5
point = 0
score = 0
lives = 0

def game(stars,points):

    WORDS = ["stairs", "traffic light", "sausage", "heroine", "ocean", "tongue", "wheat", "clever", "habit", "riddle", "tomorrow", "letters", "sleep", "book", "watermelon", "ticket", "star", "mushroom", "zoo"]
    word = random.choice(WORDS)

    def decision(ans,stars,point):
        if ans == word:
            print("\n")
            print("Your answer is right. You have earned 5 points!")
            point += 5

        else:
            print("\n")
            print("Oops, the right answer is ",word)
            stars -= 1

        return



    if word == "stairs":
        print("I am a 5 letter word.I go up and down but I’m not a helicopter.I can be climbed but I’m not a mountain.I can be a flight but I don’t have any wings.I have steps but I’m not a ladder.I help you get between floors but I’m not an elevator.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "traffic light":
        print("I stare at you, you stare at me.I have three eyes, yet can't see.Every time I blink, I give you commands.You do as you are told, with your feet and hands.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "sausage":
        print("I have seven letters and I'm something you eat. My only anagram can help your pain. If you remove my first 2 letters I wear things down. Removing my first 3 letters is an adjective and removing my first 4 letters leaves a measure of time.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "heroine":
        print("There is a word in the English language in which the first two letters signify a male, the first three letters signify a female, the first four signify a great man, and the whole word, a great woman.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "ocean":
        print("I am a 5 letter word.I look flat, but I am deep, Hidden realms I shelter.Lives I take, but food I offer.At times I am beautiful.I can be calm, angry and turbulent.I have no heart, but offer pleasure as well as death.No man can own me, yet I encompass what all men must have.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "tongue":
        print("I'm a king that speaks for my country.At birth I'm protected by no one.As I grow my father gives me 2 soldiers to protect me,as I get matured many more are given to me.And at my full age my father gives me 32 white soldiers to guard me and protect me.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "wheat":
        print("I am a food with 5 letters. If you remove the first letter I am a form of energy. Remove two and I'm needed to live. Scramble the last 3 and you can drink me down.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "clever":
        print("I am an adjective with 6 letters.My first is in ocean but not in sea,my second is in milk but not in me.My third is in three but not in throw, my fourth is in vow but not in crow. My fifth is in eight but not in night, my last is in wrong and also right. My whole is praise for thoughts of men or women.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "habit":
        print("I have one, you have one, everybody has one. If you remove the first letter, a bit remains. If you remove the second, bit still remains. If you remove the third, it still remains.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "riddle":
        print("I am never quite what I appear to be. Straight­forward I seem, but it's only skin deep. For mystery most often lies beneath my simple speech. Sharpen your wits, open your eyes, look beyond my exteriors, read me backwards, forwards, upside down. Think and answer the question...")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "tomorrow":
        print("I never was, I'm always to be. No one ever saw me, nor ever will. And yet I'm the confidence of all, to live and breathe on this terrestrial ball.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "letters":
        print("Lots of them make up a word, and lots of words are in them. It's easy when you think about it. A while ago we stamped and mailed them.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)
            
    elif word == "sleep":
        print("I weaken all men for hours each day. Sometimes I show you strange visions while you are away. I take you b night, by day take you back. None suffer to have me, but do from my lack.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "book":
        print("I am a four letter word. I have no voice but I can teach you all there is to know. I have spines and hinges but I am not a door. Once I have told you all, I cannot tell you more.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "watermelon":
        print("I am a fruit. I wear a green jacket on the outside, white jacket as a second layer, and a red jacket inside. I am pregnant with a lot of babies.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "ticket":
        print("I am one small little piece of paper, yet sometimes hold lots of value. I am all you need to get to big events, but will cost you. I am an important part of travel. And if lost, you're not coming.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "star":
        print("I come without being fetched at night, hide away as soon as daylight strikes. Although I may look small, I am much mightier than what you can imagine.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "mushroom":
        print("I am the type of room you cannnot enter or leave. Raise from the ground below. I could be poisonous or a delicious treat.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)

    elif word == "zoo":
        print("I'm like a forest without trees, like a jail you want to visit. Though the inmates did no wrong. You may freely walk along. They are put there so you can see them, just as long as you don't feed them.")
        ans = str(input("What am I? \n"))
        decision(ans,stars,point)
            
    return

def start_game():
    print("1.Start game")
    print("2.Exit \n")

    option = int(input("Select option \n"))

    print("\n")

    if (option == 1):
        game(stars,point)

        chance = 0

        while chance < 19:
            print("\n")

            if (stars != 0):
                print("1.Next riddle")

            else:
                print("Game over")
                start_game()
            
            print("2.Quit \n")

            choice = int(input("Select option \n"))
            print("\n")

            if (choice == 1):
                game(stars,point)

            elif (choice == 2):
                print("Your total score is ", score, ".")
                exit()

    elif (option == 2):
        exit()

    else :
        print("Invalid input")

    return 

start_game()
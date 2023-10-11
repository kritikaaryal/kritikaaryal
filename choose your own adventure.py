def name():
    s = input("Please enter your name: ")
def scene5():
    a = input('Ryder is going to take you to a hospital. Would you like to Uber, walk, or take the motorbike (uber/walk/motorbike): ').lower()
    while a not in ('uber', 'walk', 'motorbike'):
        a = input("Not a valid transportation. Would you like to Uber, walk, or take the motorbike (uber/walk/motorbike): ").lower() 
    if a == 'uber':
        print("'Hey, our Uber driver, Mr. Schmidt is here.'")
        print("'Mr. Schmidt, please take them to the Mykonos Health Center'")
        print("Sounds good. That will be a twenty-minute drive")
        print('Congrats, you made it out of Mykonos alive! Hope you had fun in Greece. Time to teleport back to Groton.')
    elif a == 'motorbike':
        print("Oh no! Ryder doesn't know how to drive a motorbike, and you fall off the end before you can even reach the hospital. But thanks for using Teleportation!")
    else:
        print("Walking to the hospital will take you forty minutes, and your rashes get too bad to walk. The game is over but thanks for using teleportation!")

def main():
    print("Welcome to Teleport!")
    s = input("Please enter your name: ")
    gender = input("Please specify the gender of your character (M/F/N): ").lower()
    while gender not in ('m', 'f', 'n'):
        print("Invalid response. Try again.")
        gender = input("Please specify the gender of your character (M/F/N): ").lower()  
    if gender == 'm':
        nominative = "he"
        accusative = "him"
        genitive = "his"
        reflexive = "himself"
    elif gender == 'f':
        nominative = "she"
        accusative = "her"
        genitive = "hers"
        reflexive = "herself"
    elif gender == 'n':
        nominative = "they"
        accusative = "them"
        genitive = "theirs"
        reflexive = "themselves"

    guide = input("Hooray! You've landed in Mykonos and see Orion and Will Koukopolos. Choose a character to give you a tour (Wouk/Orion): ").lower() 
    while guide != 'wouk' and guide != 'orion':
        guide = input("Not a valid tour guide. Choose a character to give you a tour (Wouk/Orion): ").lower()
    
    if guide == 'wouk':
        question = input("Great choice. Wouk takes pride in his .25 Greek heritage and knows all of the hot spots after a week-long trip with his friends. Where would you like to go first? (night club/dinner): ").lower()   
        while question != 'night club' and question != 'dinner':
            question = input("Not a valid answer. Choose again: ").lower() 
        if question == 'night club':
            a = input("You've bumped into Wouk's friends, Ryder and Forrest. Who would you like to speak to first? (Ryder/Forrest): ").lower()
            while a != 'ryder' and a != 'forrest':
                a = input("Not a valid answer. Choose again (Ryder/Forrest): ").lower()
            if a == 'ryder':
                ss = input("Hey " +s+ "! Welcome to Scandanivian Bar Mykonos. Would you like a drink? [1] 'Yes, I would love a drink' [2] 'No thank you' (1/2): ")
                while ss != '1' and ss != '2':    
                    ss = input("Not a valid option. Pick again (yes/no): ")
                if ss == '1':
                    print ("'Yes, I would love a drink'")
                    print ("'Hey Forrest, can you get",accusative,"a drink?'")
                    print ("'Sure Ryder!'")
                    c = input ("How should you thank Forrest 1] 'Thank you so much.'  2] 'ευχαριστώ' (1/2): ")
                    print('Uh oh. When you took a sip you had an allergic reaction and it gave you severe rashes.')
                    scene5()
                    
                if ss=='2':
                    print ("'No thank you'")
                    print ("'Sounds good. Forrest show",accusative,"to the dance floor!'")
                    c = input ("What dance moves should you ask Forrest to do? 1] 'The disco'  2] 'The whip and nay nay' (1/2): ")
                    while c != '1' and c != '2':
                        c = input("Not a valid answer. Choose again (1/2): ").lower()
                    if c == "1":
                        print ("'Hey Forrest. Can you do the disco?'")
                        print ('When Forrest does the disco, he pokes you in the eye and you are forced to teleport back to Groton to get it fixed by your eye doctor.')
                    if c == "2":
                        print ("'Hey Forrest. Can you do the whip and nay nay?'")
                        print ("When Forrest does the whip and nay nay, he strains his arm and you get blamed. Forrest threatens to sue you and so you go back home. Time to teleport back home.")
                        
    
                    
                    
                    
                    
        if question == 'dinner':
            print('Wouk will take you to dinner at Scorpios with his friends')
            f = input("'Hey " + s + ", my name is Forrest and this is Ryder. Welcome to Mykonos. Would you like some 1. lobster or 2. pizza' (1/2): ")
            while f != '1' and f != '2':
                 f = input("Not a valid option. Pick again (1/2): ")
            if f=='1':
                print ("Oh no! " ,nominative,"is alergic to lobster!'")
                print("'Please bring me to the hospital!'")
                scene5()
            if f=='2':
                print ("Oh no! " ,nominative,"is alergic to pizza!'")
                print('Bring me to the hospital!')
                scene5()
        
                    
            
            if a == 'Forrest':
                drink = input("Hey " +s+ "! Welcome to Scandanivian Bar Mykonos. Would you like a drink? [1] 'Yes, I would love a drink' [2] 'No thank you' (1/2): ")
                while drink != '1' and drink!= '1':
                    if drink == '1':
                        print ("'Yes, I would love a drink'")
                        print ("'Hey Ryder, can you get ",accusative,"a drink?'")
                        print ("'Sure Forrest!'")
                        c = input ("How should you thank Ryder? 1] 'Thank you so much.'  2] 'ευχαριστώ' (1/2): ")
                        print('Uh oh. When you took a sip you had an allergic reaction and it gave you severe rashes.')
                        scene5()
                    if drink =='2':
                        print ('No thank you')
                        print ("'Ok, no worries! Ryder, show ",accusative,"to the dance floor!'")
                        c = input ("What dance moves should you ask Ryder to do? 1] 'The disco'  2] 'The whip and nay nay' (1/2): ")
                        while c != '1' and c != '2':
                            c = input("Not a valid answer. Choose again (1/2): ").lower()
                        if c == "1":
                            print ("'Hey Ryder. Can you do the disco?'")
                            print ('When Ryder does the disco, he pokes you in the eye and you are forced to teleport back to Groton')
                        if c == "2":
                            print ("'Hey Ryder. Can you do the whip and nay nay?'")
                            print ("When Ryder does the whip and nay nay, he strains his arm and you get blamed. Ryder threatens to sue you and so you go back home. Time to teleport back home.")
                          
                    
                while a not in ('uber', 'walk', 'motorbike'):
                    a = input("Not a valid transportation. Would you like to Uber, walk, or take the motorbike (uber/walk/motorbike): ").lower()
            
                    if a == 'uber':
                        print("Hey " + s + ", our Uber driver is here.")
                        print("Mr. Schmidt, please take " + accusative + " to the Mykonos Health Center")
                        print("Sounds good. That will be a twenty-minute drive")
                        print('Congrats, you made it out of Mykonos alive! Hope you had fun in Greece. Time to teleport back to Groton.')
                    elif a == 'motorbike':
                        print("Oh no! Ryder doesn't know how to drive a motorbike, and you fall off the end before you can even reach the hospital. But thanks for using Apple Teleport!")
                    else:
                        print("Walking to the hospital will take you forty minutes, and your rashes get too bad to walk. But thanks for using Apple Teleport!")
        
             
            
    else:
        question = input("Great choice. Orion is a Mykonos local and can take you sightseeing. Where would you like to go first? (shopping/beach): ").lower()
        while question != 'shopping' and question != 'beach':
            question = input("Not a valid answer. Choose again: ").lower() 
        if question == 'shopping':
            print ("You see two locals who are trying to sell to you.")
            buy = input("A local, JR, Would you like to buy his necklace. Will you buy it (y/n): ").lower()
            while buy != 'y' and buy != 'n':
                buy = input("Invalid. Pick (y/n): ").lower()   
            if buy =='y':
                 c=input("Another local, Jacob M, intercepts 'Hey, will you buy this one of a kind bracelet?' (y/n): ").lower()
                 while c != 'y' and c != 'n':
                    c= input("Are you going to consider Jacob's proposal (y/n): ").lower()
                 if c=='n':
                    print("'You scummy tourist! You can leave Mykonos and never come back!'")
                    print("Jacob gets mad and throws hands. To escape the conundrum, you teleport back to Groton. Your trip to Mykonos is over.")
                 if c =='y':
                    print("'Hello, I am Jacob and my bracelet is better than JR's cheap necklace. You made a good choice purchasing from me.'")
                    print("You are happy with your bracelet. You can enjoy the rest of your stay in Mykonos.")
            if buy == 'n':
                print("'You scummy tourist! You can leave Mykonos and never come back!'")
                print("JR gets mad and throws hands. To escape the conundrum, you teleport back to Groton. Your trip to Mykonos is over.")
                  
        if question =='beach':
            lol=input("You see Wouk, your other tour guide option at the beach. Would you like to say hi (y/n): ").lower()
            while lol != 'y' and lol !='n':
                lol =input("Not a valid answer. Would you like to say hi (y/n): ").lower()
            if lol=='y':
                print("Wouk ignores you because you chose Orion. You are so sad he doesn't say hi that you teleport back to Groton.")
            else:
                print ("Wouk is mad that you not only chose Orion, but you also ignored him. He sends you back on Teleportation to Groton.")
              
                
                
             
 





    
    
    
    
    
if __name__ == "__main__":
    main()
    


    

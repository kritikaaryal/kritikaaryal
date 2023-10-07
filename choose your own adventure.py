def main():
    print("Welcome to Apple Teleport")
    s= input("Please enter your name")

gender=input("Please specify the gender of your character (M/F/N): ")
gender = gender.lower()
while(gender != 'm' and gender != 'f' and gender!= 'n'):
    print("Invalid response. Try again.")
    gender=input("Please spcifify the gender of your character (M/F/N): ")
    gender = gender.lower()
if gender == 'm' :
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
    nominative = "their"
    accusative = "them"
    genitive = "theirs"
    reflexive = "themselves"
  
    


if __name__ == "__main__":
    main()

    

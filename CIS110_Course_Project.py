print(f"Hi, and welcome to my first Choose-Your-Own Adventure. Let's start this story already!")
print(f"Before the story can start though, let's get some questions out of the way.")
print(f"Once you have the answer you want to give, make sure to press Enter to finalize. Here we go!")
input(f"\nPress the enter key to start...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    manClothes = input("\nWhat kind of clothes is Scooby wearing?")
    while len(manClothes) == 0:
        manClothes = input(f"They can't be naked. Please put some clothes on: ")
    city = input("\nWhere does Scooby live?")
    while len(city) == 0:
        city = input(f"How can you be cityless? Where does Scooby live: ")
    wealth = input("\nIs Scooby rich or poor?")
    while wealth.lower() not in ["rich", "poor"]:
        wealth = input("No middle class here, buddy! Please enter rich or poor:")
    nickName = input("\nWhat is Scooby's nickname?")
    while len(nickName) == 0:
        nickName = input(f"Who doesn't have a nickname? Please give a nickname: ")
    hatChoice = input("\nWhat kind of hat is Scooby wearing?")
    while len(hatChoice) == 0:
        hatChoice = input(f"I don't believe you're bald, or are you? Choose a hat, please: ")

    print("Let's get it done!!!")

    print(f"\nThere once was a place called {city} that housed a {wealth} man named Scooby.")
    print(f"\nScooby went by many names, but they preferred to be called {nickName}.")
    print(f"\nOn this particular day, {nickName} was wearing {manClothes} with a nice {hatChoice}.")

    print(f"\n{nickName} was a particular person, whose appetite was huge yet their waist size was a two.")
    print(f"\nOne day, {nickName} decided they wanted to make their famous, patent-pending 12-layer sandwich!")
    print(f"\n{nickName}, now in the kitchen, starts to assemble their glorious eighth wonder of their world.")
    print(f"\nAs {nickName} reached the eleventh layer, tragedy strikes! There was no more items for their sandwich.")
    print(f"\n{nickName} must make the most important decision that has ever occured in their life, excpet when they had to choose a drink at Burger King.")

    gotoStore = input(f"\nShould {nickName} go to the store to pick up more stuff for their sandwich? Type yes or no: ")
    while gotoStore.lower() != "yes" and gotoStore.lower() != "no":
        gotoStore = input("{nickName} can't think for themself. They have to rely on you, so please type yes or no: ")
    if gotoStore == "yes":
        print(f"\n{nickName} decided that this sandwich is worth going to the store for, maybe even die for.")
        print(f"\nMaybe not die for, but definitely go to the store for.")
        print(f"\nAfter all, they were wearing their {manClothes} so they didn't look good to perish yet.")
        print(f"\n{nickName} heads to the store in their 1997 Ford F-150 to get their ingredients.")
    else:
        print(f"\n{nickName} leaning into their laziness, decides that the world couldn't handle their 12-layer sandwich.")
        print(f"\nThey eat the sandwich with some satisfaction, but is still hungry afterwards.")
        print(f"\nAfter all of their thinking, {nickName} goes to the store wearing their {manClothes} since they're still too lazy to change.")

    print(f"\nOnce {nickName} reaches the store, many people see and admire their laziness just by wearing their {manClothes}.")
    print(f"\nUnfortunately, not one soul decided that their {hatChoice} was remotely good at all.")
    print(f"\nThe people in the store could even smell the {wealth} on them.")
    print(f"\nIn any case, {nickName} wanders the aisles in search of more food to sit atop of their sandwich.")
    print(f"\nHowever, something caught their eye. It was the rarest Indian-Cuban Jamaican turkey leg so many people had fought for.")
    print(f"\nThe one thing stopping them from getting it was the price tag, costing them around $1,999.99 for the entire leg.")
    print(f"\nLuckily, {nickName} always keeps their life savings on them at all times. {nickName} must make another great decision.")
    buytheTurkey = input(f"\nShould {nickName} buy the turkey leg? Type yes or no: ")
    while buytheTurkey.lower() != "yes" and buytheTurkey.lower() != "no":
        buytheTurkey = input(f"They can't for the life of them conjure a single thought. They are a little helpless, so please type yes or no: ")
    
    if buytheTurkey == "yes":
        print(f"\n{nickName} grabs their wallet and hands over their cash.")
        print(f"\nThey hears the faintest cry from somewhere near, perhaps their wallet?")
        print(f"\nNah!")
        print(f"\n{nickName} goes home to finish their ulitmate sandwich with the prized turkey leg of the gods!")
    else:
        print(f"\n{nickName} decided that maybe their life savings were more than a way to buy an expensive turkey leg.")
        print(f"\n{nickName} decides that it's not worth having fun and enjoying something like that turkey leg.")
        print(f"\nYes, having fun isn't the way to go, I suppose. It definitely could not have been fun if we bought the turkey leg.")
        print(f"\n{nickName} is now upset and decides to buy a pack of gummies and a drink to eat and forget this whole day.")
    
    if gotoStore == "yes" and buytheTurkey == "yes":
        print(f"\n{nickName} rushes into their home to finish their perfect sandwich.")
        print(f"\nThey finish their sandwich with the turkey leg and see the work they carefully crafted.")
        print(f"\nIn one fell swoop, they eat the sandwich and could only describe it as tasting like Heaven.")
        print(f"\nFifteen minutes later, {nickName} is hungry once again.")
    elif gotoStore == "no" and buytheTurkey == "no":
        print(f"\n{nickName} just can't believe that this day was absolutely terrible.")
        print(f"\nFirst they eat an eleven-layer sandwich, then they don't get the turkey leg!")
        print(f"\nWhat kind of person decided to pretty much take the fun out of everything?")
        print(f"\nIf only someone made the right decisions or at least tried to have fun with this little adventure...")
    else :
        print(f"\n{nickName} decided that there were too many decisions today.")
        print(f"\nThey just went home and went to bed, forgetting the day even happened.")
        print(f"\nTheir final thought was hoping that tomorrow would be another day to see what could change.")
    print("\nThe End")
    keepPlaying = input(f"\nDo you want to play again? Enter yes or no: ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no: ")
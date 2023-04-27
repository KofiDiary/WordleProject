from colorama import Fore

def TEARS():
    counter = 0
    
    newWords = 0
     
    possibleCombinations = [
        "RATES", "RESAT",
        "STARE", "TARES", "EATS", "ATES",
        "RATS", "SATE", "REST", "ERA",
        "ERAS", "RASE", "TARS", "TAR",
        "STAR", "TEAR", "RATE", "ARTS", "RAT",
        "ARE", "ART", "AS", "SET", "ETA"
    ]
    
    alreadyGuessed = []
    
    NewWords = []
    
    shuffleList = ["T--E--A--R--S", "S--A--E--R--T", "A--R--T--E--S", "E--A--R--T--S", "R--E--A--T--S"]
    
    expectedGuess = ["TEA", "SEA", "EAR", "EARS", "TEARS", "SAT", "SEAT", "AT", "ATE", "EAT"]
    
    challenge = Fore.BLUE + "S--T--E--A--R" + Fore.RESET 
    
    print(f'Hello Wordle! \n\nYour first challenge is {challenge}.')
    
    print("\n\nGuess your first word: ")
    wordle_guess = input()
    if wordle_guess in expectedGuess:
        counter += 1
        alreadyGuessed.insert(0, wordle_guess)
    
    while True:
        if wordle_guess in expectedGuess:
            print(Fore.GREEN + "\n\nCorrect. Expected words formed: ")
            for words in alreadyGuessed:
                print(Fore.GREEN + f'{" " * 3}  {words}' + Fore.RESET)
            print("\n\nGuess another word.")
            wordle_guess = input()
            if wordle_guess in expectedGuess and wordle_guess not in possibleCombinations:
                alreadyGuessed.append(wordle_guess)
                counter += 1
                if counter == 10:
                    print(Fore.GREEN + "\n\nCorrect. Expected words formed: " + Fore.RESET)
                    for words in alreadyGuessed:
                        print(Fore.GREEN + f'{" " * 3}  {words}' + Fore.RESET)
                    print(Fore.GREEN + "You have successfully completed this level." + Fore.RESET)
                    break
        
        elif wordle_guess not in expectedGuess and wordle_guess not in possibleCombinations:
            print(Fore.RED + "\n\nIt appears the word you entered is not an English word!" + Fore.RESET)
            wordle_guess = input ("Guess another word: ")
            if wordle_guess in expectedGuess and wordle_guess not in possibleCombinations:
                alreadyGuessed.append(wordle_guess)
                counter += 1
            
                    
        elif wordle_guess not in expectedGuess and wordle_guess in possibleCombinations:
            extraWords = wordle_guess
            print(Fore.YELLOW + "\n\nNew word added to your new words dictionary" + Fore.RESET)
            NewWords.append(extraWords)
            newWords += 1
            print(Fore.YELLOW + "New words formed: " + Fore.RESET)
            for WORDS in NewWords:
                print(Fore.YELLOW + f'{" " * 3}  {WORDS}' + Fore.RESET)
                    
            wordle_guess = input("Guess another word: ")
            if wordle_guess in expectedGuess and wordle_guess not in possibleCombinations:
                alreadyGuessed.append(wordle_guess)
                counter += 1
                    
        
            
                    
    print(Fore.YELLOW + f'\nYou have added a total of {newWords} new words to your dictionary.' + Fore.RESET)
    print(Fore.YELLOW + "New words added: " + Fore.RESET)
    for words in NewWords:
        print(Fore.YELLOW + f'{" " * 3}  {words}' + Fore.RESET)
    

TEARS()
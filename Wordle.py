def TEARS():
    print("Form some words from STEAR")
    reply = input()
    wordle = ["TEA", "SEA", "EAR", "EARS", "TEARS", "SAT", "SEAT", "AT", "AS"]
    #wordle_length = 9
    
    while True:
        if reply not in wordle:
            print("Ooops, I dont think that's an english word.")
            reply = input("Try again: ")
            if reply in wordle:
                print("Correct. Have a go at another one")
                reply = input("Next word: ")
                wordle_length = wordle.pop(-1)
                
                if reply not in wordle:
                    print("Ooops, I dont think that's an english word.")
                    reply = input("Try again: ")
                    
                else:
                    if reply in wordle:
                        print("Correct. Have a go at another one")
                        reply = input("Next word: ")
                        wordle_length = wordle.pop(-1)
                        if wordle == False:
                            print("Congratulations, you have successfully completed this challenge. \nOn to the next challenge.")
                            break
        else:
            print("Correct. Have a go at another one")
            reply = input("Next word: ")
            if reply not in wordle:
                print("Ooops, I dont think that's an english word.")
                reply = input("Try again: ")
                    
            else:
                if reply in wordle:
                    print("Correct. Have a go at another one")
                    reply = input("Next word: ")
                    wordle_length = wordle.pop(-1)
                    if wordle == False:
                        print("Congratulations, you have successfully completed this challenge. \nOn to the next challenge.")
                        break
                    
TEARS()
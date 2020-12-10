

print("Congrats for finding this Project")


lucky_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

choice = int(input("What is your Favourite number? "))



if choice > 0 and choice != 0:
    print("Did you know that is a Lucky number?")

    use = input("How often do you Use it (always/sometimes)? ")

    
    if use == "always":
        print("Your favourite number has a meaning, lets find out what it is.")
        
        find_out = input("Whould you like to know (yes/no)? ")
        
        
        
        if find_out == "yes":
                print("If you chose an even number, then you like to have everything in pair. This can apply to different things such as: multiple choices or opportunites, objects, even how often you rewatch some of the movies. The point is you like to play it safe!")
        
        else:
            print("Maybe next time, Goodbye!")
            

        
        
    elif use == "sometimes":
            print("You should use it more often...")
    

        
            belief = input("Favourite number can improve life(True/False)? ").lower() 

            if belief == "True":
                print("It's True, doeas help!")
            

            
            
            else:
                print("You never know!")
                print("Perhaps words have better impact on you!")

                sentence = input("Enter a Sentence which describes you: ")
                
                print("Now let's see what we get if we read it backwards...")

                print("".join(sentence.split()[::-1]))

                try_again = input("Enter another sentence: ")

                print("Let's see what we get this time...")

                print("".join(try_again.split()[::-1]))


                valid = input("Can you still understand it (yes/no)? ")

                if valid == "yes":
                    print("Well done!")
                    print("Keep playing and have fun!")
                
                

                
                
                else:
                    print("Try a different one!")




    else:
        print("We need an input to continue, try again!")



else:
    print("Don't enter 0, try again!")
        

    










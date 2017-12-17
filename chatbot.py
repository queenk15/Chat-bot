import random

chat_name = "Bob Robber"
def start():                                                                                                                                                  
    print("        CCCCCCCCCCCCChhhhhhh                                       tttt               BBBBBBBBBBBBBBBBB                             tttt          ")
    print("     CCC::::::::::::Ch:::::h                                    ttt:::t               B::::::::::::::::B                         ttt:::t          ")
    print("   CC:::::::::::::::Ch:::::h                                    t:::::t               B::::::BBBBBB:::::B                        t:::::t          ")
    print("  C:::::CCCCCCCC::::Ch:::::h                                    t:::::t               BB:::::B     B:::::B                       t:::::t          ")
    print(" C:::::C       CCCCCC h::::h hhhhh         aaaaaaaaaaaaa  ttttttt:::::ttttttt           B::::B     B:::::B   ooooooooooo   ttttttt:::::ttttttt    ")
    print("C:::::C               h::::hh:::::hhh      a::::::::::::a t:::::::::::::::::t           B::::B     B:::::B oo:::::::::::oo t:::::::::::::::::t    ")
    print("C:::::C               h::::::::::::::hh    aaaaaaaaa:::::at:::::::::::::::::t           B::::BBBBBB:::::B o:::::::::::::::ot:::::::::::::::::t    ")
    print("C:::::C               h:::::::hhh::::::h            a::::atttttt:::::::tttttt           B:::::::::::::BB  o:::::ooooo:::::otttttt:::::::tttttt    ")
    print("C:::::C               h::::::h   h::::::h    aaaaaaa:::::a      t:::::t                 B::::BBBBBB:::::B o::::o     o::::o      t:::::t          ")
    print("C:::::C               h:::::h     h:::::h  aa::::::::::::a      t:::::t                 B::::B     B:::::Bo::::o     o::::o      t:::::t          ")
    print("C:::::C               h:::::h     h:::::h a::::aaaa::::::a      t:::::t                 B::::B     B:::::Bo::::o     o::::o      t:::::t          ")
    print(" C:::::C       CCCCCC h:::::h     h:::::ha::::a    a:::::a      t:::::t    tttttt       B::::B     B:::::Bo::::o     o::::o      t:::::t    tttttt")
    print("  C:::::CCCCCCCC::::C h:::::h     h:::::ha::::a    a:::::a      t::::::tttt:::::t     BB:::::BBBBBB::::::Bo:::::ooooo:::::o      t::::::tttt:::::t")
    print("   CC:::::::::::::::C h:::::h     h:::::ha:::::aaaa::::::a      tt::::::::::::::t     B:::::::::::::::::B o:::::::::::::::o      tt::::::::::::::t")
    print("     CCC::::::::::::C h:::::h     h:::::h a::::::::::aa:::a       tt:::::::::::tt     B::::::::::::::::B   oo:::::::::::oo         tt:::::::::::tt")
    print("        CCCCCCCCCCCCC hhhhhhh     hhhhhhh  aaaaaaaaaa  aaaa         ttttttttttt       BBBBBBBBBBBBBBBBB      ooooooooooo             ttttttttttt ")

def end():                                                                                                                                                                                             
    print("                                                                   dddddddd                                                                        ")
    print("        GGGGGGGGGGGGG                                              d::::::d     BBBBBBBBBBBBBBBBB                                              !!!   ")  
    print("     GGG::::::::::::G                                              d::::::d     B::::::::::::::::B                                            !!:!!")
    print("   GG:::::::::::::::G                                              d::::::d     B::::::BBBBBB:::::B                                           !:::!")
    print("  G:::::GGGGGGGG::::G                                              d:::::d      BB:::::B     B:::::B                                          !:::!")
    print(" G:::::G       GGGGGG   ooooooooooo      ooooooooooo       ddddddddd:::::d        B::::B     B:::::Byyyyyyy           yyyyyyy eeeeeeeeeeee    !:::!")
    print("G:::::G               oo:::::::::::oo  oo:::::::::::oo   dd::::::::::::::d        B::::B     B:::::B y:::::y         y:::::yee::::::::::::ee  !:::!")
    print("G:::::G              o:::::::::::::::oo:::::::::::::::o d::::::::::::::::d        B::::BBBBBB:::::B   y:::::y       y:::::ye::::::eeeee:::::ee!:::!")
    print("G:::::G    GGGGGGGGGGo:::::ooooo:::::oo:::::ooooo:::::od:::::::ddddd:::::d        B:::::::::::::BB     y:::::y     y:::::ye::::::e     e:::::e!:::!")
    print("G:::::G    G::::::::Go::::o     o::::oo::::o     o::::od::::::d    d:::::d        B::::BBBBBB:::::B     y:::::y   y:::::y e:::::::eeeee::::::e!:::!")
    print("G:::::G    GGGGG::::Go::::o     o::::oo::::o     o::::od:::::d     d:::::d        B::::B     B:::::B     y:::::y y:::::y  e:::::::::::::::::e !:::!")
    print("G:::::G        G::::Go::::o     o::::oo::::o     o::::od:::::d     d:::::d        B::::B     B:::::B      y:::::y:::::y   e::::::eeeeeeeeeee  !!:!!")
    print(" G:::::G       G::::Go::::o     o::::oo::::o     o::::od:::::d     d:::::d        B::::B     B:::::B       y:::::::::y    e:::::::e            !!! ")
    print("  G:::::GGGGGGGG::::Go:::::ooooo:::::oo:::::ooooo:::::od::::::ddddd::::::dd     BB:::::BBBBBB::::::B        y:::::::y     e::::::::e               ")
    print("   GG:::::::::::::::Go:::::::::::::::oo:::::::::::::::o d:::::::::::::::::d     B:::::::::::::::::B          y:::::y       e::::::::eeeeeeee   !!! ")
    print("     GGG::::::GGG:::G oo:::::::::::oo  oo:::::::::::oo   d:::::::::ddd::::d     B::::::::::::::::B          y:::::y         ee:::::::::::::e  !!:!!")
    print("        GGGGGG   GGGG   ooooooooooo      ooooooooooo      ddddddddd   ddddd     BBBBBBBBBBBBBBBBB          y:::::y            eeeeeeeeeeeeee   !!! ")
    print("                                                                                                          y:::::y                                  ")
    print("                                                                                                         y:::::y                                   ")
    print("                                                                                                        y:::::y                                    ")
    print("                                                                                                       y:::::y                                     ")
    print("                                                                                                      yyyyyyy                                      ")
                                                                                                                                                              
                                                                                                                      


def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?"]

    return random.choice(responses)

def get_random_question():
    responses = ["what is your favorite color?",
                 "what is your life goal?",
                 "what si your favorite subject?",
                 "what is your favorite food?",
                 "who is your favorite person"]
    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()

    family_words = [" mother ", " father ", " brother ", " sister "]
    robber_words = [" robber ", " jewelry "]
    food_words = [" french fries ", " mac and cheese ", " cheese ", " tacos ", " icecream ", " chicken "]
    hobby_words = [" game "," sports ", " television "]
    yes_words = ["y" , "yes", "yup"]
    no_words = ["n", "no", "nope"]
    career_words = [" doctor ", " lawyer ", " nurse ", " archetect ", " career "]
    color_words = [" purple ", " blue ", " green ", " black ", " red ", " yellow ", " orange ", " pink "]
    people_words = [" Kyerra ", " Ryan ", " Alannah ", " Vivian ", " Casey ", " Mr. Cooper "]
    subject_words = [" math ", " art ", " english ", " spanish ", " technomogy ", " history ", " social studies ", " business ", " lunch "]

    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
        
    elif has_keyword(statement, robber_words):
        response = "I don't know what you are talking about. What is your favorite food?"

    elif has_keyword(statement, food_words):
        response = "What else do you like my favorite food is french fries?"
        
    elif has_keyword(statement, hobby_words):
        response = "What else do you like my favorite food is french fries?"    

    elif has_keyword(statement, yes_words):
        response = get_random_question()

    elif has_keyword(statement, no_words):
        response = "Ok say something!"
        
    elif has_keyword(statement, career_words):
        response = "Tell me more about what you want to do and your career!"

    elif has_keyword(statement, color_words):
        response = "My favorite color is purple, tell me other colors you like!"

    elif has_keyword(statement, people_words):
        response = "They are my favorite person, tell me more!"

    elif has_keyword(statement, subject_words):
        response = "math is my favorite class, tell me more about your favorite class!"

    else:
        response = get_random_response()

    return response


def play():
    talking = True

    print("Hello. I'm " + chat_name + ". What is your name?")
    name = input(">> ")
    print("Say something to me!")

    while talking:
        statement = input(">> " + name+ ":")
        if len(statement) == 0:
            print("You didn't say anything, would you like me to ask you something?")

        if statement == "Goodbye":
            talking = False
        else:
            response = get_response(statement)
            print(chat_name + ": " + response)

    print("Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()

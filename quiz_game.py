
answers = ["tokyo","yen","shigeru ishiba" ]
a = 1
score = 0
while  a < 2 :

    print("what is the capital of japan?")
    n = str(input("your answer: "))
    if n.lower() == answers[0]:
        print("you are right!!😊")
        score += 10
    else:
        print("you are wrong😔")
        score -=  5

    print("what is the currency of japan?")
    n = str(input("your answer: "))
    if n.lower() == answers[1]:
        print("you are right!!😊")
        score += 10
    else:
        print("you are wrong😔")
        score -=  5

    print("who is the prime minister of japan?")
    n = str(input("your answer: "))
    if n.lower() == answers[2]:
        print("you are right!!😊")
        score += 10
    else:
        print("you are wrong😔")
        score -=  5
    
    print(f"your final score is {score}")

    if score >= 20 :
        print("yay you won")
    else: 
        print("you lost")
    a = a + 1
    
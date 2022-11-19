import time

def quiz_game():
    Question = {
    "What is the first name of Iron man":"Tony",
    "Who is called the god of ligthening in avengers": "Thor",
    "Who carried a shield of American flag theme in avengers": "Captain America",
    "Which avenger is green in color": "Hulk", 
    "Which avenger can change it size": "Ant-man",
    "Which avenger is red in color and has mind-stone": "vision"
    }

    intial_point = 0
    for question, answer in Question.items():
        attempt = 3
        while attempt > 0:
            print(question)
            user_input = input("Enter your answer: ")
            if answer.lower() == user_input.lower():
                print("answer is correct!!")
                intial_point +=1
                break
            attempt -=1
            print(f"incorrect answer, you have {attempt} lifeline left. Try again!")     
    total_points = intial_point


    print("Game is over")
    time.sleep(2)
    print("Result loading!!!!!!")
    time.sleep(1)
    print(".............")
    time.sleep(1)
    print(".............")
    time.sleep(3)
    print(f"Your total point is: {total_points}")

quiz_game()
    
            
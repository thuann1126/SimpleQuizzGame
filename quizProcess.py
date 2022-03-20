# This file process the logic of the quiz
import question

class QuizProcess():

    #Process the flow of the quiz

    def next_question(self):

        point = 0
        questionNumber = 1

        for q in question.question_data:
            print(f"{questionNumber}. {q['text']}" + " (True/False?)")
            questionNumber += 1
            userinput = input()

            #Remove case sensitive
            userInput = userinput.lower()

            if userInput == q['answer'].lower():
                point += 1
                print("Your answer is correct")
                print("You get +1 point")
                print(f"Your current point: {point} \n")
            else:
                print("your answer is incorrect")
                print("You get no point")
                print(f"Your current point: {point} \n")

        self.result_summary(point, questionNumber)

    def result_summary(self, point, number):
        print("________________________")
        print("Your result summary:")
        print(f"Your have answered: {number} questions")
        print(f"Your total score: {point} / {number}")




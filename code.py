def main():
  study = input("Hello there, what feature would you like to use today?(Questions/Notes)")
  def questions():
    answers = {
        "What is a square": "A square can either be multiplying a number by itself or a 2d shape.",
        "What is addition": "Addition is combining two or more integers together.",
        "What is multiplication": "Multiplication is repeated addition.",
        "Give me study resources": "Khan Academy and IXL are often referenced as amazing study resources"
    }
    print("Now I will help you answer your questions")
    question = input("What is your first question")
    if question in answers:
      print(f"Answer: {answers[question]}")
    else:
      print("Sorry I dont have an answer for that.")
  def quiz():
    score = 0
    print("You will be locked into the quiz untill you finish it, make sure to write ansswers as digits")
    print("---------------------------------------------------------------------------------------------------")
    answer1 = input("What is 1+1? ")
    if "2" == answer1:
      print("Nice job, you got it right!")
      print("---------------------------------------------------------------------------------------------------")
      score += 1
    else:
      print("Sorry you got it wrong.")
      print("---------------------------------------------------------------------------------------------------")
    answer2 = input("What is 5^2? ")
    if "25" == answer2:
      print("Nice job, you got it right!")
      print("---------------------------------------------------------------------------------------------------")
      score += 1
    else:
      print("Sorry you got it wrong.")
      print("---------------------------------------------------------------------------------------------------")
    answer3 = input("What is 10x12? ")
    if "120" == answer3:
      print("Nice job, you got it right!")
      print("---------------------------------------------------------------------------------------------------")
      score += 1
    else:
      print("Sorry you got it wrong.")
      print("---------------------------------------------------------------------------------------------------")
    answer4 = input("What is 36+72? ")
    if "108" == answer4:
      print("Nice job, you got it right!")
      print("---------------------------------------------------------------------------------------------------")
      score += 1
    else:
      print("Sorry you got it wrong.")
      print("---------------------------------------------------------------------------------------------------")
    print("Last question!")
    answer5 = input("What is 206+432?")
    if "638" == answer5:
      print("Nice job, you got it right!")
      print("---------------------------------------------------------------------------------------------------")
      score += 1
    else:
      print("Sorry you got it wrong.")
      print("---------------------------------------------------------------------------------------------------")
    print("End of quiz")
    print(f"You got {score}/5")
    print("---------------------------------------------------------------------------------------------------")
  def take_notes():
      print("You can now take notes here")
      notes = []

      while True:
          note = input("Enter a note or type 'over' to close the notes: ")
          if note == "over":
              break
          notes.append(note)
      print("I will now show your current notes")
      print(notes)
      q = input("Would you like to take a quiz?(Yes/No)")
      if q == "Yes":
        quiz()
      else:
        print("Ok, that's fine")
  if study == "Questions":
    questions()
  elif study == "Notes":
    take_notes()
while True:
  main()













def main():
  study = input("Hello there, what feature would you like to use today?(Questions/Notes)")
  def questions():
    print("Now I will help you answer your questions")

  def quiz():
    print("You will be locked into the quiz untill you finish it, make sure to write ansswers as digits")
    print("---------------------------------------------------------------------------------------------------")
    answer1 = input("What is 1+1? ")
    if "2" == answer1:
      print("Nice job, you got it right!")
      print("---------------------------------------------------------------------------------------------------")
    else:
      print("Sorry you got it wrong.")
      print("---------------------------------------------------------------------------------------------------")
    answer2 = input("What is 5+5? ")
    if "10" == answer2:
      print("Nice job, you got it right!")
      print("---------------------------------------------------------------------------------------------------")
    else:
      print("Sorry you got it wrong.")
      print("---------------------------------------------------------------------------------------------------")
    answer3 = input("What is 10+12? ")
    if "22" == answer3:
      print("Nice job, you got it right!")
      print("---------------------------------------------------------------------------------------------------")
    else:
      print("Sorry you got it wrong.")
      print("---------------------------------------------------------------------------------------------------")
    answer4 = input("What is 36+72? ")
    if "108" == answer4:
      print("Nice job, you got it right!")
      print("---------------------------------------------------------------------------------------------------")
    else:
      print("Sorry you got it wrong.")
      print("---------------------------------------------------------------------------------------------------")
    print("Last question!")
    answer5 = input("What is 206+432?")
    if "638" == answer5:
      print("Nice job, you got it right!")
      print("---------------------------------------------------------------------------------------------------")
    else:
      print("Sorry you got it wrong.")
      print("---------------------------------------------------------------------------------------------------")
    print("End of quiz")
    print("---------------------------------------------------------------------------------------------------")
  if study == "Quiz":
    quiz()
  if study == "Questions":
    questions()
while True:
  main()













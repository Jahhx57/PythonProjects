print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play:")
score = 0

# Read questions and answers from the file
with open("QuizGameQuestions.txt", "r") as file:
    lines = file.readlines()

# Process each line (question and answer) from the file
for line in lines:
    # Split the line into question and answer using the comma as a delimiter
    question, correct_answer = map(str.strip, line.split(','))

    # Ask the question and check the answer
    user_answer = input(question + " ")
    if user_answer.lower() == correct_answer.lower():
        print('Correct!')
        score += 1
    else:
        print(f"Incorrect. The correct answer is '{correct_answer}'.")

# Display results
print("You got {} out of {} questions correct!".format(score, len(lines)))
percentage_correct = (score / len(lines)) * 100
print("You got {:.2f}%.".format(percentage_correct))

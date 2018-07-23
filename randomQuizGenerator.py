#!python3
#randomQuizGenerator.py - This program will randomly generate quiz
#random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Generate 35 quiz files.
for quizNum in range(35):
    #Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' %(quizNum + 1), 'w') #capitalsquiz%s.txt will be replaced by quizNum + 1
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum+1),'w') #open in write mode

    #Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n') #quiz header for student to fill out
    quizFile.write((' '*20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    #Shuffle the order of the states
    states = list(capitals.keys()) #key = states, the first part of the :
    random.shuffle(states) #random.shuffle() randomly reorders

    #Loop through all 50 states, making a question for each
    for questionNum in range(50):
        #Get right ans wrong answers
        correctAnswer = capitals[states[questionNum]]
        #correctAnswer stored as a value in the capitals dictionary #loop from states[0] to [49]
        wrongAnswers = list(capitals.values())
        #list must be integers print (wrongAnswers[correctAnswer])
        del wrongAnswers[wrongAnswers.index(correctAnswer)] #delete the correct answer
        wrongAnswers = random.sample(wrongAnswers, 3) #select 3 random values from this list
        answerOptions = wrongAnswers + [correctAnswer] #make the list options
        random.shuffle(answerOptions)  # shuffle the order

        #Write the question and answer options to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        #Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()




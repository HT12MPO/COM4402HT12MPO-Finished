print("Hello, welcome to the quiz!") #welcoming
print("you'll answer 15 questions with each correct answer you receive a point")
choice = input("A) maths, B) history, C) biology")
choice = choice.upper()
print("please type the answers in ABCD form")
total = 0
amount_of_questions = 15
i = 0

question_askedM = {
    "8^0 " :         "A", #Q1
    "42/7 " :        "B", #Q2
    "190 + (-30) " : "C", #Q3
    "6^2 " :         "D", #Q4
    "7 * 7 " :       "A",#Q5
    "121^(1/2)" :    "B",#Q6
    "21 / 3 " :      "A",#Q7
    "10^3 " :        "B", #Q8
    "11 * 11 " :     "B", #Q9
    "12^2 " :        "B", #Q10
    "15 * 5 " :      "C", #Q11
    "72 / 8 " :      "D", #Q12
    "11 * 12 " :     "B", #Q13
    "16 * 3 " :      "C", #Q14
    "17 - 19 " :     "B", #Q15
    "9^2 " :         "D", #Q16
}

possible_answersM = ["A)1    B)0         C)8         D)0.5", #A1
                     "A)5    B)6         C)7         D)8", #A2
                     "A)220   B)60       C)160       D)70", #A3
                     "A)22    B)12       C)16        D)36", #A4
                     "A)49    B)47       C)46        D)42", #A5
                     "A)10    B)11       C)12        D)13", #A6
                     "A)7     B)8        C)9         D)6   ", #A7
                     "A)10    B)10000    C)1000      D)100", #A8
                     "A)111   B)121      C)130       D)120", #A9
                     "A)141   B)144      C)151       D)120", #A10
                     "A)65    B)80       C)75        D)70", #A11
                     "A)8     B)6        C)7         D)9", #A12
                     "A)111   B)121      C)130       D)120", #A13
                     "A)46    B)44       C)48        D)42", #A14
                     "A)2     B)-2       C)0         D)1", #A15
                     "A)17    B)11       C)18        D)81"] #A16




question_askedH = {
    "When was world war 1" :                                                "B", #Q1
    "When did world war 1 end " :                                           "B", #Q2
    "what was the ship that sunk April 11th 1912 " :                        "A", #Q3
    "What was Henry 8th son that came to the thrown " :                     "C", #Q4
    "What when the first name of henry 8th illigetment son called " :       "A", #Q5
    "first name of henry's second wife" :                                   "D ", #Q6
    "What was the first name of  Henry's 5th wife and Anne's cousin  " :    "A", #Q7
    "what is the first name of  Henry' 8th 'favourite wife' " :             "B", #Q8
    "Who was the queen that rained after Henry " :                          "C", #Q9
    "What was the queen after mary " :                                      "A", #Q10
    "which queen has the second longest reign" :                            "B", #Q11
    "how many Elizabeth have there been  " :                                 "A", #Q12
    "who was victories husband called " :                                    "C", #Q13
    "when did victoria die " :                                               "D", #Q14
    "was victoria short or tall " :                                          "A", #Q15
    "what country did victoria become the empress of " :                     "D", #Q16
}
possible_answersH = ["A)1912       B)1914     C)1916     D)1918", #A1
                     "A)1916       B)1918     C)1920     D)1922", #A2
                     "A)titanic    B)queen    C)mary     D)ocean  ", #A3
                     "A)henry      B)john     C)edward   D)oliver", #A4
                     "A)henry      B)john     C)edward   D)oliver", #A5
                     "A)katherine  B)jane     C)mary     D)anne", #A6
                     "A)katherine  B)jane     C)mary     D)anne", #A7
                     "A)katherine  B)jane     C)mary     D)anne", #A8
                     "A)katherine  B)jane     C)mary     D)anne", #A9
                     "A)elizabteh  B)victoria C)mary     D)olivia", #A10
                     "A)elizabteh  B)victoria C)mary     D)olivia", #A11
                     "A)2          B)3        C)1        D)4", #A12
                     "A)edward     B)richard  C)albert   D)micheal", #A13
                     "A)1900       B)1902     C)1903     D)1901", #A14
                     "A)short      B)tall     C)average",#15
                     "A)india      B)france   C)spain    D)russia"] #A16





question_askedB = {
    "name the most common antibiotic " :                                    "A", #Q1
    "what is the main organ to push blood around the body " :               "B", #Q2
    "what is the biggest organ " :                                          "D", #Q3
    "what part of the body does the immune system not know exists " :       "A", #Q4
    "where can you find a 'record' of substances you have taken " :         "A", #Q5
    "what does a bacteria cell not have" :                                  "D ", #Q6
    "what gives the cell energy  " :                                        "B", #Q7
    "what is used to stop bacteria cells' " :                               "A", #Q8
    "is all bacteria bad " :                                                "B", #Q9
    "what is the biological male chromosome consist of" :                   "B", #Q10
    "what is the biological female chromosome consist of" :                 "A", #Q11
    "True or False - do animal  and plant  have identical cell structer " : "FALSE", #Q12
    "True or False - animals don't have cell walls " :                      "TRUE", #Q13
    "True or False - animal and plant cells have cell membranes" :          "TRUE", #Q14
    "True or False- bacteria are called prokaryotes  " :                    "TRUE", #Q15
    "True or false - plant cells are eukaryotic " :                         "TRUE", #Q16
}


possible_answersB = ["A)penicillin       B)paracetamol  C)ibruphem      D)vaccines", #A1
                     "A)blood vessels,   B) heart       C)blood         D)lungs", #A2
                     "A)heart            B)brain        C)kidney         D)skin", #A3
                     "A)eyes             B)finger       C)muscle         D)bones" #A4
                     "A)hair             B)finger       C)nails          D)skin  ", #A5
                     "A) mitochondria    B)cellmenbrain C)ribsons        D)nucleus", #A6
                     "A)water            B)mitochondria C)cell membrain  D)nucleus", #A7
                     "A)antibiotic       B)paracetamol  C)ibruphem       D)vaccines", #A8
                     "A)yes              B)no           C)maybe", #A9
                     "A)xx               B)xy           C)yy xyy", #A10
                     "A)xx               B)xy           C)yy xyy", #A11
                     "True               False", #A12
                     "True               False", #A13
                     "True               False", #A14
                     "True               False", #A15
                     "True               False ", #A16
                     "True               False",
                     "True               False "
                      ]


while amount_of_questions > 0: # loops until all the questions have been answered
    if choice == "A": # choice for maths
        for key in question_askedM:  # choose the dictonary to read from, this being read line by line until all been read through
            print(key) #outputs only the question (the key)
            print(possible_answersM[i]) # prints the multy choice possible answers
            answer = input("what is your answer? ")
            answer = answer.upper()
            if answer == question_askedM[key]: #compairing the answer from the user and the correct answer declared in question_asked
                total = total + 1  # adds to the total
                i = i + 1  # increments the space being read in possible_answerM in the set by 1
                print("Correct") #outputs correct
                amount_of_questions = amount_of_questions - 1 #subtracts the amount of questions by 1 so when they've answered 15 the loop will break
            else:
                total = total + 0  # total remains
                print("Incorrect")
                i = i + 1
                amount_of_questions = amount_of_questions - 1

    elif choice == "B":
        for key in question_askedH:
            print(key)
            print(possible_answersH[i])
            answer = input("what is your answer? ")
            answer = answer.upper()
            if answer == question_askedH[key]:
                total = total + 1
                i = i + 1
                print("Correct")
                amount_of_questions = amount_of_questions - 1
            else:
                total = total + 0
                print("Incorrect")
                i = i + 1
                amount_of_questions = amount_of_questions - 1


    elif choice == "C":
        for key in question_askedB:
            print(key)
            print(possible_answersB[i])
            answer = input("what is your answer? ")
            answer = answer.upper()
            if answer == question_askedB[key]:
                total = total + 1
                i = i + 1
                print("Correct")
                amount_of_questions = amount_of_questions - 1
            else:
                total = total + 0
                print("Incorrect")
                i = i + 1
                amount_of_questions = amount_of_questions - 1

    else:
        print("not valid ask again") #not a valid input by user


print(f"You answered {total} correctly")
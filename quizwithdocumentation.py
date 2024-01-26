def quiz():
    #Preparing quiz questions in a list

    questions=["1. Which one of the following river flows between Vindhyan and Satpura ranges?","2. The Central Rice Research Station is situated in?","3. Who among the following wrote Sanskrit grammar?","4. Which among the following headstreams meets the Ganges in last?","5. The metal whose salts are sensitive to light is?"]

    #Options list for each question


    options=[["(a) Narmada","(b) Mahanadi","(c) Son","(d) Netravati"],["(a) Chennai","(b) Cuttack","(c) Bangalore","(d) Quilon"],["(a) Kalidasa","(b) Charak","(c) Panini","(d) Aryabhatt"],["(a) Alaknanda","(b) Pindar","(c) Mandakini","(d) Bhagirathi"],["(a) Zinc","(b) Silver","(c) Copper","(d) Aluminum"]]

    #Answers for each question

    answers=["(a) Narmada.","(B) Cuttack","(c) Panini","(d) Bhagirathi","(B). Silver"]


    #this "question_no" variable is useful for printing question followed by corresponding options

    question_no=0

    #Variable for counting correct option choosen options

    score=0

    #Listing the choosen option in the list

    choosen_options=[]

    #start printing quiz questions

    print("lets start the quiz!!!\n\n\n")

    for question in questions:

        print("-------------------------------------------------------------------------------------------")

        print("-------------------------------------------------------------------------------------------\n")

        print(question)

        print("Options:\n")

        for option in options[question_no]:

            print(option)

        choosen=input("Choose optimal option(a,b,c,d)\n")

        if choosen==answers[question_no][1]:

            print("Congratulations!!!! Correct Answer.")

            score+=1

        else:

            print("Wrong!!!  "+answers[question_no]+" is the correct one.")
    
        choosen_options.append(choosen)
    
        question_no+=1


    print("Correct    choosen")

    for i in range(len(questions)):

        print(answers[i][1],choosen_options[i],sep="           ")

    print(len(questions),score,sep="           ")

    print("Your percentage is  ",score/len(questions)*100)

while True:

    #Asking user to take test

    print("1.Do you want to take Test.")

    print("2.Quit the quiz")

    choose=int(input("Choose optimal chioce(1,2)\n"))

    if choose==1:

        quiz()
    
    elif choose==2:
        
        print("\n\n****************Thank You for taking quiz******************")

        break




    


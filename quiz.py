#Preparing quiz questions in a list

questions=["1. Which one of the following river flows between Vindhyan and Satpura ranges?","2. The Central Rice Research Station is situated in?","3. Who among the following wrote Sanskrit grammar?","4. Which among the following headstreams meets the Ganges in last?","5. The metal whose salts are sensitive to light is?"]




options=[["(a) Narmada","(b) Mahanadi","(c) Son","(d) Netravati"],["(a) Chennai","(b) Cuttack","(c) Bangalore","(d) Quilon"],["(a) Kalidasa","(b) Charak","(c) Panini","(d) Aryabhatt"],["(a) Alaknanda","(b) Pindar","(c) Mandakini","(d) Bhagirathi"],["(a) Zinc","(b) Silver","(c) Copper","(d) Aluminum"]]



answers=["(a) Narmada.","(B) Cuttack","(c) Panini","(d) Bhagirathi","(B). Silver"]
print(len(questions))


question_no=0

score=0

choosen_options=[]


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

print("Your percentage is  "+score/len(questions)*100)
    


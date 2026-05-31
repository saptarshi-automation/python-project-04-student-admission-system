student = []

admission = ""


while admission != "done":
    admission = input("Enter newly admitted students(TYPE 'done' once done with entry):")

    if admission != "done":
        
        student.append(admission)


std = int(input("call students by roll number: "))#roll number is set according to student admitted first 



while std > len(student) or std < 1:
    
     print("only "+str(len(student))+" are there")
     std = int(input("call students by roll number 1 to "+ str(len(student))+ ":"))

print(student[std - 1])




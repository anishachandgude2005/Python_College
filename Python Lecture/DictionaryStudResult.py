#Create dictionary with students details
students={
    101: {"Name":"Aditi","Scores":[20,20,20]},
    102: {"Name":"raj","Scores":[40,70,50]},
    103: {"Name":"karan","Scores":[50,40,60]},
    104: {"Name":"Anita","Scores":[75,90,50]},
    105: {"Name":"Asmita","Scores":[60,30,70]}
}

#Calculate average score and flag pass/fail
for sid,details in students.items():
    avg=sum(details["Scores"] )/ len(details["Scores"])
    details["Average"]=avg
    details["Passed"]=avg>=30  #Boolean flag

#Print names of students who passed
print("Student who passed")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])
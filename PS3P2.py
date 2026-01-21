#Input phase
LstName=input("Enter Student's last name:")
MidTerm=float(input("Enter your midterm score:"))
Final=float(input("Enter your final exam Score:"))

#Process phase
TotalExam = Final + MidTerm
#Output phase
print ("Student: ", LstName)
print ("Total points earned: ", TotalExam)
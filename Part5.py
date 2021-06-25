# I declare that my work contains no examples of misconduct, such as palagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

#Student ID: 20200714 (SE)
# UOW ID : w1832564

#Date : 4.29.2021

def credits():
    global credit
    credit = [[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]] # 2D list via given set of data table
    return

def status(credits):
    
    progress = 0    
    Trailer = 0    
    Retriever = 0    
    Exclude = 0

    for i in range(len(credit)): 
        if credit[i][0]== 120:   # Getting each elements in credit list
            print("Progress")
            progress = progress +1
        elif credit[i][0] == 100:
            print("Progress (module trailer)")
            Trailer = Trailer +1
        elif (20 <= credit[i][0] <= 80) and (20 <= credit[i][2] <= 60):
            print("Do not Progress - module retriever")
            Retriever = Retriever+1
        elif ( 0 <= credit[i][0] <= 20) and (80 <= credit[i][2] <= 120) :
            print("Exclude")
            Exclude = Exclude + 1
    

    print()
    print("progress  ",(progress), ":",(progress)*"*" )
    print("Trailing  ",(Trailer),":",(Trailer)*"*" )
    print("Retriever ",(Retriever), ":", (Retriever) * "*")
    print("Excluded  ",(Exclude),":", (Exclude) * "*")
    print()
    print(len(credit) , " outcomes in total.")

    return
credits()
status(credits())



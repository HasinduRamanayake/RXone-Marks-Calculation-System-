# I declare that my work contains no examples of misconduct, such as palagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

#Student ID: 20200714 (SE)
# UOW ID : w1832564

#Date : 4.29.2021

print("-----------------------------------------------")
print("Staff version with Histogram")
count = 0
progress = 0
Trailer = 0
Retriever = 0
Excluded = 0


def main():

    try:
          for i in range(5):


            Pass = int(input("Please enter your credits at pass: "))
            if Pass not in [0, 20, 40, 60, 80, 100, 120]:
                print('Value Out of Range')
                continue
            defer = int(input('Please enter your credit at defer: '))
            if defer not in [0, 20, 40, 60, 80, 100, 120]:
                print('Value Out of Range')
                continue

            fail = int(input('Please enter your credit at fail: '))
            if fail not in [0, 20, 40, 60, 80, 100, 120]:
                print('Value Out of Range')
                continue


            Total = Pass + defer + fail
            if Total > 120 or Total < 120:
                print("Total incorrect")

            if Pass == 120 and defer == 0 and fail == 0:

                print("Progress ")
                global progress  # getting the variable from outside of func
                progress = progress +1 # updating the variable


            elif Pass == 100:

                print("Progress (module trailer)")
                global Trailer
                Trailer = Trailer+1


            elif Pass == 40 and defer == 0 and fail == 80:

                print("Exclude")
                global Excluded
                Excluded = Excluded+1


            elif Pass == 20 and (defer == (0 or 20)) and (fail == (80 or 100)):

                print("Exclude")

                Excluded = Excluded + 1


            elif Pass == 0 and (defer == (0 or 20 or 40)) and (fail == (80 or 100 or 120)):

                print("Exclude")

                Excluded = Excluded + 1


            else:

                print("Do not progress -- module retriever")
                global Retriever
                Retriever = Retriever+1

            global count
            count = count +1
            n = input("Would you like to enter another set of data ?\nEnter 'y' for yes or 'q' to quit and view results :")

            if n == 'y':
                main() # calling func back to begin 

            elif n == 'q':
                Quit = True
                print("Horizontal Histogram")
                print("Progress  ", progress ," :", progress*"*")
                print("Trailer   " , Trailer , " :", Trailer*"*" )
                print("Retriever ", Retriever , " :" , Retriever*"*")
                print("Excluded  ", Excluded, " :", Excluded*"*")

                print(count , "outcomes in Total")

            else:
                print("wrong input , Try Again ")
                main()  
                  


    except:
        print("Integer required")
        main()

    return count, progress , Trailer , Retriever, Excluded



print(main())



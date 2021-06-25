# I declare that my work contains no examples of misconduct, such as palagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

#Student ID: 20200714 (SE)
# UOW ID : w1832564

#Date : 4.29.2021

def main():
    try:

        for x in range(5): # loop for 5 times

            Pass = int(input("Please enter your credits at pass: "))
            if Pass not in [0, 20, 40, 60, 80, 100, 120]:
                print('Value Out of Range')
                continue  # for return into begin 
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

            elif Pass == 100:

                print("Progress (module trailer)")


            elif Pass == 40 and defer == 0 and fail == 80:

                print("Exclude")


            elif Pass == 20 and (defer == (0 or 20)) and (fail == (80 or 100)):

                print("Exclude")


            elif Pass == 0 and (defer == (0 or 20 or 40)) and (fail == (80 or 100 or 120)):

                print("Exclude")


            else:

                print("Do not progress -- module retriever")

    except:
        print("Integer required")
        main() # for return to the begin of main func

print(main())


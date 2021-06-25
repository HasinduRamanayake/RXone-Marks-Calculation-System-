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
                global progress
                progress = progress +1


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



            if n == 'q':


                print("Verticle Histogram")
                category = ['Progress ',  'Trailing ', 'Retriever ',  'Excluded ',]
                category1 = [progress , Trailer , Retriever , Excluded]
                

                def ver_histo():

                    for x in range(0, len(category)):
                        print(category[x], end="")  # printing the elements in the category list
                    print()
                    max_cat = max(category1) # Getting the maximum value of elements from category1 list
                    while max_cat >= 1:
                        if category1[0] >= 1:
                            print("    *    ", end="")
                        else:
                            print("         ",end="")
                        if category1[1] >= 1:
                            print("    *    ",end="")
                        else:
                            print("         ",end="")
                        if category1[2] >= 1:
                            print("    *     ", end="")
                        else:
                            print("          ",end="")
                        if category1[3] >= 1:
                            print("    *    ", end="")
                        else:
                            print("         ",end="")

                        category1[0] = category1[0] - 1
                        category1[1] = category1[1] - 1
                        category1[2] = category1[2] - 1
                        category1[3] = category1[3] - 1
                        max_cat = max_cat - 1
                    
                        print()
                    return
                print()
                ver_histo()
                print()

                print(count , "outcomes in Total")
        
            elif n == 'y':
                main()
                
            else:
                print("wrong input , Try Again ")
                main()


            

    except:
        print("Integer required")
        main()

    
    return count, progress , Trailer , Retriever, Excluded


print(main())


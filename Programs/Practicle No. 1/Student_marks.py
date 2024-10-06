# Q: Write a python program to store marks stored in subject "Fundamentals of Data
#    Structure" by N students in the class. Write functions to compute following:
#       1. The average score of the class.
#       2. Highest score and lowest score of the class.
#       3. Count of students who were absent for the test.
#       4. Display mark with highest frequency.


def print_avg (marks_list):
    sum_of_marks = 0 
    for element in marks_list : 
        sum_of_marks += element

    print ("\nTotal number of marks :  ", sum_of_marks)
    print ("Average marks :          ", sum_of_marks / len(marks_list))
        
def print_min_N_max (marks_list) : 
    max_marks = 0; 
    min_marks = 0;
    for element in marks_list  : 
        if (max_marks < element) : 
            max_marks = element

    min_marks = max_marks

    for element in marks_list : 
        if (min_marks > element) : 
            min_marks = element
        else : 
            continue
    if min_marks < 0 : 
        print ("\nMinimum marks scored : \t0", )
    else : 
        print("\nMinimum marks scored : \t", min_marks)
    print ("Max marks scored : ", max_marks)   

def print_absenty(marks_list) : 
    absent_count = 0 
    for element in marks_list : 
        if (element < 0) : 
            absent_count+= 1
    
    print("\nTotal number of student absent : ", absent_count)

def print_freq_count(marks_list) :
    freq_count = {}
    for marks in marks_list : 
        if marks in freq_count : 
            freq_count[marks] += 1
        else : 
            freq_count[marks] = 1

    for marks, frequency in freq_count.items(): 
        print(f"\nMarks : {marks} \t Frequency : {frequency}")

def menu_choise () : 
    print("\n\n--------------------MENU--------------------\n")
    print("1. Total and Average Marks of the Class")
    print("2. Highest and Lowest Marks in the Class")
    print("3. Number of Students absent for the test")
    print("4. Marks with Highest Frequency")
    print("5. Exit\n")
    choise = int(input("Enter your Choice (from 1 to 5) : "))
    return choise

def choise_to_continue() : 
    choise = int(input("\nDo you want to continue (1 or 0) : "))
    return choise; 

def greet() : 
    print("\nThanks for using this program :)")

marks_list = []
student_count = int(input("Enter the number of student : "))
print(f"Enter the marks of students (max 100 and negative for absense): ")

for i in range(student_count) : 
    marks = int(input(f"Marks of student {i + 1} : "))
    marks_list.append(marks)
    
while True :
    choise = menu_choise()
    if (choise == 1) : 
        print_avg(marks_list); 
        if (choise_to_continue()) : 
            continue;
        else : 
            greet()
            break
    
    elif (choise == 2) : 
        print_min_N_max(marks_list)
        if (choise_to_continue()): 
            continue; 
        else : 
            greet()
            break; 

    elif (choise == 3) : 
        print_absenty(marks_list) 
        if(choise_to_continue()) : 
            continue;
        else : 
            greet()
            break; 

    elif(choise == 4) :
        print_freq_count(marks_list)
        if (choise_to_continue()) : 
            continue; 
        else : 
            greet()
            break; 

    elif (choise == 5) : 
        greet()
        break;
    
    else : 
        print("Invalid input, try again.") 
        continue;
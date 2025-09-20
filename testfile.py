def validate_problem(problem):
        
     #validates a single problem entered by user 
    parts=problem.split()
    #checks if problem splits into exactly 3 parts 
    if len(parts)!=3:
        return f'Error:Input {parts} not properly formatted. Please use the format "number operator number" (eg 32 + 698) with spaces in between.'
    #checks if first number is a digit 
    if not parts[0].isdigit():
        return f'Error:Number {parts[0]} should only contain digits'
    #checks if second number is a digit 
    if not parts[2].isdigit():
        return f'Error:Number {parts[2]} should only contain digits' 
    #checks if operator is supported  
    if not parts[1] in ["+","-","*","/"]:
        return "Error:Operator must be '+' or'-' or '*' or '/'."   
    #checks if  first number is more than 6 digits     
    if len(parts[0])>6:
        return f'Error:Number {parts[0]} cannot contain more than 6 digits.'
    #checks if second number is more than 6 digits
    if len(parts[2])>6:
        return f'Error:Number {parts[2]} cannot contain more than 6 digits.'             
    #if all check points qualify 
    return "Valid"  
  
def arithmetic_formatter(problems, show_answers=False):

    #placeholders for different parts of the formatted problems
    top_parts=[]
    bottom_parts=[]
    dash_parts=[]
    answers_parts=[]

    #limiting number of problems to 10
    if len(problems)>10:
        return "Error:Too many problems (write a max of ten)."
    
    #looping through each problem in the list of problems individually
    for problem in problems:
        validated_problem=validate_problem(problem)#sets  each problem for validation
        if validated_problem!="Valid":
            return validated_problem #returns exact error message from validate_problem function
        
        #if problem is valid function proceeds 
        numb=problem.split()#split problem into two operands and one operator
        operator=numb[1]
        longest_width=max(len(numb[0]),len(numb[2]))+2 #adding placeholders for the operator and space

        #Right Alignment of problems(creates spaces)
        top_part=" "*(longest_width-len(numb[0]))+numb[0]
        bottom_part=operator+" "*(longest_width-len(numb[2])-1)+numb[2]#subtract placeholder for space
        dash_part="-"*longest_width

        #calculating each instance of the operator 
        if operator=="+":
            result=str(int(numb[0])+int(numb[2])) 
        elif operator=="*":
            result=str(int(numb[0])*int(numb[2]))
        elif operator=="/": 
            result=str(float(numb[0])//float(numb[2]))
        elif operator=="-":
            result=str(int(numb[0])-int(numb[2]))

        #right alignment for answers
        answer_part=" "*(longest_width-len(result))+result


    #all parts are collected  and added  to their respective lists
        answers_parts.append(answer_part)        
        top_parts.append(top_part)
        bottom_parts.append(bottom_part)
        dash_parts.append(dash_part)

    #joining all parts together with 4 spaces between each problem
    top_parts_joined="    ".join(top_parts)
    bottom_parts_joined="    ".join(bottom_parts)
    dash_parts_joined="    ".join(dash_parts)

    answers_parts_joined = "    ".join(answers_parts)
    base_output=f"{top_parts_joined}\n{bottom_parts_joined}\n{dash_parts_joined}\n"
    arranged_problems=f"{top_parts_joined}\n{bottom_parts_joined}\n{dash_parts_joined}\n{answers_parts_joined}"
    return base_output,arranged_problems

def main():
    while True:
        print("\n" + "="*64)
        print("WELCOME TO THE ARITHMETIC FORMATTER COURTESY OF FATHELA !")
        print("="*64 + "\n")
        print("This program formats arithmetic problems vertically.\n")
        print("RULES TO OBSERVE.\n")
        print("1. You can enter a maximum of 10 problems.")
        print("2. Please ensure to add spaces in between numbers and operators to avoid errors.")
        print("3. Numbers should only contain digits and cannot be more than 6 digits long.")
        print("4. Supported operators are +, -, *, and /.\n")

        problems=[]
        numb_problem=0
        #ask user number of problems  until a valid input is entered
        while True:
          try:#escape for non integer inputs
            numb_problem=int(input("How many problems do you want to enter?(1-10): "))
            if 1<=numb_problem<=10:
                break #the loop only breaks when this condition is true otherwise it continue forever"
            else:
                print("Please enter a number from 1 and 10.")
          except ValueError:#catches non integer inputs
            
            print("Invalid input. Please enter a valid number") 
            #ask user to enter each problem one at a time
        for i in range(numb_problem):
         while True:#inner loop that sends each problem for validation and arithmetic formatting
           problem=input(f"Enter problem {i +1}:(e.g. 32 + 698) " )
           error_message=validate_problem(problem)
           if error_message != "Valid":
            print(error_message)
            print("Please re-enter the problem correctly.")
            continue #restart button allows user to re-enter problem if error is found
           else :
            problems.append(problem)
            break #only breaks if there is no error found
         
        no_answer_output,answers_output =arithmetic_formatter(problems,show_answers=False) #stores values returned from arithmetic_formatter function
        answers_visible=False #flag to track if answers are visible
        #inner loop to ask if user wants to see answers
        while True:
            print("\nFormatted problems:\n")#this loop only runs once passed the validation stage 
            print(no_answer_output)
            if answers_visible:#depending on the boolean(Tor F) flag the answers are shown or hidden
                print("\nRespective Solutions:\n")#only runs when answers_visible is True otherwise skipped 
                print(answers_output)
                #provide user with menu options
            print("\nPlease select an option:")
            print("1. Show/Hide Answers") 
            print("2. Enter New Problems")   
            print("3. Exit")
            users_choice=input("Enter your choice (1-3): ").strip()#removes any leading/trailing spaces
            if users_choice=="1":
                answers_visible=not answers_visible #assigns opposite value to the flag
                if answers_visible:
                    print("\nFormatted solutions with answers:\n")
                    print(answers_output)
                else: 
                    print("\nFormatted problems without answers:\n")
                    print(no_answer_output)   
            elif users_choice=="2":
                break #breaks to outer loop to enter new problems
            elif users_choice=="3":
                print("Thank you for using the Arithmetic Formatter. Goodbye!")
                return #exits the program
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue #restarts the inner loop if invalid input is entered
            
           
   

if __name__=="__main__":
    main()
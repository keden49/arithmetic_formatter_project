def arithmetic_formatter(problems, show_answers=False):
    top_parts=[]
    bottom_parts=[]
    dash_parts=[]
    answers_parts=[]
    if len(problems)>10:
        return "Error:Too many problems (write a max of ten)."
    for problem in problems:
        numb=problem.split()#split problem into two operands and one operator
        operator=numb[1]
        if len(numb)!=3 :
            return "Error:problem should contain two numbers and one operator."
        if not numb[0].isdigit() and numb[2].isdigit():
            return "Error:Numbers must only contain digits."
        if not operator in["+","-","*","/"]:
            return "Error:Operator must be '+' or'-'."
        if len(numb[0])>6 or len(numb[2])>6:
            return "Error:Numbers cannot contain more than 6 digits."

        longest_width=max(len(numb[0]),len(numb[2]))+2 #adding placeholders for the operator and space
        #Right Alignment of problems
        top_part=" "*(longest_width-len(numb[0]))+numb[0]
        bottom_part=operator+" "*(longest_width-len(numb[2])-1)+numb[2]#subtract placeholder for space
        dash_part="-"*longest_width
        if show_answers:
            if operator=="+":
                result=str(int(numb[0])+int(numb[2]))
            elif operator=="*":
                result=str(int(numb[0])*int(numb[2]))
            elif operator=="/": 
                result=str(int(numb[0])//int(numb[2]))  
            elif operator=="-":
                result=str(int(numb[0])-int(numb[2]))
            answer_part=" "*(longest_width-len(result))+result
            answers_parts.append(answer_part)
        top_parts.append(top_part)
        bottom_parts.append(bottom_part)
        dash_parts.append(dash_part)

    #joining all parts together with 4 spaces
    top_parts_joined="    ".join(top_parts)
    bottom_parts_joined="    ".join(bottom_parts)
    dash_parts_joined="    ".join(dash_parts)
    if show_answers:
        answers_parts_joined = "    ".join(answers_parts)
        arranged_problems=f"{top_parts_joined}\n{bottom_parts_joined}\n{dash_parts_joined}\n{answers_parts_joined}"
    else:
        arranged_problems=f"{top_parts_joined}\n{bottom_parts_joined}\n{dash_parts_joined}"
    return arranged_problems

def main():
    print("Welcome to the Arithmetic Formatter!")
    print("This program formats arithmetic problems vertically.\n")
    n=int(input("How many problems do you want to enter: "))
    problems=[]
    for i in range(n):
        problem=input(f"Enter problem {i +1}:(e.g. 32 + 698) " )#remember to space after each problem
        problems.append(problem)
    solutions=arithmetic_formatter(problems,show_answers=True)
    print("\nRespective Solutions:\n")
    print(solutions)

if __name__=="__main__":
    main()

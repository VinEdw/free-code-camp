# https://replit.com/@VincentEdwards1/boilerplate-arithmetic-formatter

# It is a function that receives a list of strings that are arithmetic problems (addition or subtraction) and returns the problems arranged vertically and side-by-side. 
# The function optionally takes a second argument. 
# When the second argument is set to True, the answers are displayed.

import re

def arithmetic_arranger(problems: list, answers: bool = False) -> str:
    #check if the problem list has too many problems
    problemCount = len(problems)
    if problemCount > 5:
        return 'Error: Too many problems.'

    #this list of dictionaries will store helpful information about each problem in the list
    p = []
    for i in range(problemCount):
        p.append({})
    
    #extract the needed information from the problem expressions and put them into p
    for i, problem in enumerate(problems):
        #find the operator in the problem expression
        operator = re.match(r'\S+\s*([+-])\s*\S+', problem)
        if operator:
            p[i]['operator'] = operator.group(1)
        else:
            return "Error: Operator must be '+' or '-'."

        #check for any characters in the expression that are not a digit, a space, or a '+'/'-'
        digits = [str(x) for x in range(10)]
        for l in problem:
            if l not in (digits + [' ', p[i]['operator']]):
                return 'Error: Numbers must only contain digits.'
        #check that there is only one operator character
        if problem.count(p[i]['operator']) != 1:
            return 'Error: Numbers must only contain digits.'

        #find the numbers in the problem expression
        numList = re.findall(r'\b\d+\b', problem)
        #check that only two numbers were found; if more than two were found, then there is some space inserted in one of the numbers
        if len(numList) != 2:
            return 'Error: Numbers must only contain digits.'

        #check that the numbers are not more than four digits in length
        for num in numList:
            if len(num) > 4:
                return 'Error: Numbers cannot be more than four digits.'
        p[i]['num1'] = numList[0]
        p[i]['num2'] = numList[1]

        #compute the answer of the expression if the answers parameter is True
        if answers:
            if p[i]['operator'] == '+':
                p[i]['answer'] = str(int(p[i]['num1']) + int(p[i]['num2']))
            else:
                p[i]['answer'] = str(int(p[i]['num1']) - int(p[i]['num2']))

        #figure out what the bottom line should be (how many dashes long)
        p[i]['line'] = '-' * (2 + max(len(p[i]['num1']), len(p[i]['num2'])))

    #start working on creating the arrange_problems string
    arranged_problems = ''
    bigSpace = ' ' * 4
    #line 1
    arranged_problems += str.join('', [exp['num1'].rjust(len(exp['line'])) + (bigSpace if i != problemCount - 1 else '\n') for i, exp in enumerate(p)])
    #line 2
    arranged_problems += str.join('', [exp['operator'] + exp['num2'].rjust(len(exp['line']) - 1) + (bigSpace if i != problemCount - 1 else '\n') for i, exp in enumerate(p)])
    #line 3
    arranged_problems += str.join('', [exp['line'] + (bigSpace if i != problemCount - 1 else '\n') for i, exp in enumerate(p)])
    #line 4 (only add if the answers parameter is True)
    if answers:
        arranged_problems += str.join('', [exp['answer'].rjust(len(exp['line'])) + (bigSpace if i != problemCount - 1 else '\n') for i, exp in enumerate(p)])

    # Old Strategy
    # def addSection(partFunc, index: int, expression: dict) -> None:
    #     '''Add onto the end of the arranged_problems str based on a dict that describes the problem expression (in the form created earlier), the index of that expression in the problems list, and a lambda function that takes the problems expression dict as an argument.'''
    #     nonlocal arranged_problems
    #     bigSpace = ' ' * 4
    #     a = partFunc(expression)
    #     if index == problemCount - 1:
    #         a += '\n'
    #     else:
    #         a += bigSpace
    #     arranged_problems += a

    # for i, exp in enumerate(p):
    #     addSection(lambda exp: ' ' * (len(exp['line']) - len(exp['num1'])) + exp['num1'], i, exp)
    # for i, exp in enumerate(p):
    #     addSection(lambda exp: exp['operator'] + ' ' * (len(exp['line']) - len(exp['num2']) - 1) + exp['num2'], i, exp)
    # for i, exp in enumerate(p):
    #     addSection(lambda exp: exp['line'], i, exp)
    # if answers:
    #     for i, exp in enumerate(p):
    #         addSection(lambda exp: ' ' * (len(exp['line']) - len(exp['answer'])) + exp['answer'], i, exp)
    
    
    #get rid of the last newline character
    arranged_problems = arranged_problems[:-1]

    return arranged_problems


if __name__ == "__main__":
    exProblems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    print(arithmetic_arranger(exProblems, True))

def prompt():
    problems = {}
    playing = True
    while playing:
        prompt1 = input("Please enter a health problem you would like to sort patients by: ")
        if prompt1 == '/quit':
                break 
        try:
            value = int(input('Please enter a value based on priority: '))

            if value == '/quit':
                break 
        except ValueError:
            print('That value does not seem to be valid! ')
        
    
        problems[prompt1] = value

    return problems

        
#prompt()

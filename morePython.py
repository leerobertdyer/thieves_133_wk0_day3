
def ageChecker(num):
    if num > 63:
        print('senior')
    elif num < 18:
        print('kid')
    else:
        print('adult')
        
ageChecker(5234)
ageChecker(12*.4 + 11)

names = ['daniel', 'stephen', 'gianni', 'marina', 'heather']

def listNames():
    yourName = input("what is your first name? ")
    for name in names:
        if name == yourName:
            last = input("What is your last name? ")
            print(name.title() + ' ' + last.title())
            break
        else:
            print(f'no {yourName} in system. Would you like to add it?')
            check = input("Type YES or NO")
            if check.lower() == 'yes':
                names.append(yourName)
                print(names)
                break
            else:
                print('ok later')
                break
listNames()
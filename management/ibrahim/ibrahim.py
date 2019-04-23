class WrongInputError(Exception):
    def __init__(self, value):
        self.value = value


def dictionary():
    my_dict = {'Ibrahim Hakim': 'The Flash', 'Nicole': 'Jessie Quick', 'Somali': 'Iris',
    'Kevin Zhang': 'Kid Flash', 'Diana Diaz': 'Nora West Allen',
    'hakimpuri': 'Reverse Flash'}

    #for name, identity in  my_dict.items():
    #    print(name, 'is', identity)1
    for name in my_dict.keys():
        print(name)

    inp = input("To reveal their identities, press y, else q for quit: ")

    if inp == 'y':
        cin = input("enter name to see secret: ")
        for name in my_dict.keys():
            if cin == name:   #or name == cin
                print(my_dict[name])
    elif inp == 'q':
        exit()

def read():
    file = open("stat.txt", "r")
    print(file.read())
    file.close()

    file = open("stat.txt", "r")

    num_games = (file.readline())#int(file.readline())
    cards_clicked = (file.readline())#int(file.readline())
    cards_matched = (file.readline())#int(file.readline())
    file.close()

    inn = input("do you want to make a statement?(y/n): ")
    if inn == 'y':
        file = open('stat.txt', 'a') #used a to append instead of using w to overwrite text
        a = input("enter your statement: ")
        if not a.endswith('\n'): #to insert into a new line
            file.write(a + '\n')
        file.close()
    else:
        return
    #file.close()

    print(cards_clicked)
    print(num_games)
    print(cards_matched)

my_list = ['flashpoint', 'hallucination', 'memory', 'nostalgia', 'recall', 'recollection',
'reminiscence']  #Lists
print(my_list)

test = True
#cin = input("\nDelete(d): \nShow my friends(f) \nRead Reverse Flash's Note(r) \nExit(q) \nEnter desired option: ")
while test:
    cin = input("\nDelete(d): \nShow my friends(f) \nRead Reverse Flash's Note(r) \nExit(q) \nEnter desired option: ")
    if cin == 'd':
        del my_list[0]
        print(my_list)
    elif cin == 'f':
        dictionary()
    elif cin == 'r':
        read()
    elif cin == 'q':
        print('Thank you, come again')
        exit()
    else: #exception error for OUTofRange, incorrect type(integer)
        raise WrongInputError('You did not choose the following options (d,f,r,q)')

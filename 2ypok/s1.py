def index(weight, height):
    a = weight/(height*height)
    if a<19: 
        print('у вас недовес ')
    elif a>25:
        print('худей ')
    else :
        print('норма ')

index(50,1.6)

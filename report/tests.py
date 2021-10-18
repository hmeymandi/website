def function1():
    while True:
        choice1 = (input("Random text ")).lower()
        
        if choice1 in ('option1', 'option2'):
            break
        else: 
            print("Even more random text")
    return choice1
  
def function2():
    rightEvenOdd = 'random word'
    choice1 = function1()
    if choice1 == rightEvenOdd:
        print('Yay')
    else: 
        print('Not yay')

function2()
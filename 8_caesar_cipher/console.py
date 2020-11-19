from os import system, name 

def cls(): 
    #windows 
    if name == 'nt': 
        _ = system('cls') 
    #mac and linux
    else: 
        _ = system('clear') 
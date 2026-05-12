def filter(func, sequence):
    natija = []  
    
    for element in sequence:
        if func(element): 
            natija.append(element) 
            
    return natija 

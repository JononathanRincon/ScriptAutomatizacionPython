import time

HH = 0
MM = 0
SS = 0

while True:
    print(f"{HH:02}:{MM:02}:{SS:02}")
    
    time.sleep(1)
    
    SS += 1
    
    if SS == 60:
        SS = 0
        MM += 1  
        
    
    if MM == 60:
        MM = 0
        HH += 1  

    if HH == 24:
        HH = 0  
        


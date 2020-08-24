import multiprocessing
import time

square=[]
cube=[]

def calc_square(numbers):
    global square
    for n in numbers:
        time.sleep(60)
        square.append(n*n) 
    print(square)
            
def calc_cube(numbers):
    global cube
    for n in numbers:
        time.sleep(60)
        cube.append(n*n*n) 
        
if __name__ == '__main__':
    arr=[3,4,5,6]
    p1=multiprocessing.Process(target=calc_square, args=(arr,))
    p2=multiprocessing.Process(target=calc_cube, args=(arr,))
    
    p1.start()    
    p2.start()
    
    p1.join()
    p2.join()
    
    print(square)
    print(cube)
    print('multiprocess completed..!')

print(square)
print(cube)

    
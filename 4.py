from math import sqrt, pi

def circ_sqrt(r):
        try:
            return (sqrt(2*pi*r))
                                
        except ValueError:
            print('try again. Smth wrong')
            

print(circ_sqrt(float(input('Input r: '))))

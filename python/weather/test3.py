from colorama import init
from colorama import Fore, Back, Style

print(Back.GREEN)
print(Fore.BLACK)


name = input("What we do (+, -) ?: ")


a=float(input("number:"))
b=float(input("number:"))
if name=="+":
    c=a+b
    print("Total " +str(c))
elif name=="-":
    c=a-b
    print("Total " +str(c))
else: print("FAIL!")

from colorama import init
from colorama import Fore, Back, Style

print(Back.BLUE)
print(Fore.GREEN)


from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

name1=input('Are we working on? yes/no:')

if name1=='no':
    print('Пока пока')
    exit()

elif name1=='yes':
    spot=input('Place:')


owm = OWM('d5666ecdd24c4302ddf8185dde9103cb')
mgr = owm.weather_manager()



observation = mgr.weather_at_place(spot)
w = observation.weather

tempa=w.temperature('celsius')['temp']

print('In town ' + spot + ' now ' + w.detailed_status)
print('Temperature now about ' + str(tempa))

if tempa<10:
    print('Очень холодно, будь дома')
    
elif tempa>10:
    print('Будь дома')
    
elif tempa>20:
    print('Жарко, будь дома')
    


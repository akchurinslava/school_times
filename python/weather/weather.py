from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

spot=input('Place:')



owm = OWM('d5666ecdd24c4302ddf8185dde9103cb')
mgr = owm.weather_manager()



observation = mgr.weather_at_place(spot)
w = observation.weather

tempa=w.temperature('celsius')['temp']

print('In town ' + spot + ' now ' + w.detailed_status)
print('Temperature now about ' + str(tempa))

if tempa<10:
    print('Очень холодно, валяйся на диване')
elif tempa>10:
    print('Да тоже валяйся на диване')
elif tempa>20:
    print('Да уже жарко, тоже на диване будь')


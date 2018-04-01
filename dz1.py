import pyowm

def WhatIscloudness():
    if 0 <= weather.get_clouds() <= 10:
        return 'Ясная'
    if 10 <= weather.get_clouds() <= 30:
        return 'Немного Облачная'
    if 30 <= weather.get_clouds() <= 70:
        return 'Пасмурная'
    if 70 <= weather.get_clouds() <= 100:
        return 'Мрачная'


print('OpenWeatherMap')
owm = pyowm.OWM('de7b632eec3ce25b2d7ab87fdb87b57d')
observation = owm.weather_at_place('Moskow,ru')
weather = observation.get_weather()
location = observation.get_location()

translate = {'Rostov-on-Don': 'Ростов-на-Дону', 'Moskow': 'Москва', 'ru': 'Россия'}

print('Погода в городе' + translate[location.get_name()] +
      '(' + translate[location.get_country] + ')' + 'на сегодня' +
      str(observation.get_reception_time('time')) + ' ' + WhatIscloudness() +
      ' ,облачность составляет ' + str(weather.get_clouds()) + '%, давление ' +
      str(weather.get_presure()['press']) + 'мм.рт.ст., температура ' +
      str(weather.get_temperature('celsius')['temp']) + ' градусов Цельсия днем ' +
      str(weather.get_temperature('celsius')['temp_max']) + ', Ночью ' +
      str(weather.get_temperature('celsius')['temp_min']) + ' скорость ветра ' +
      str(weather.get_wind()['speed']) + ' м/с. ')



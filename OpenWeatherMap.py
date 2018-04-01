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

print ('OpenWeatherMap')
owm = pyowm.OWM('af32d88ced874e80d7ea122c94326640')
observation = owm.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()
print('Страна ' + location.get_country())
print('Город ' + location.get_name())
print('Долгота ' + str(location.get_lon()))
print('Широта ' + str(location.get_lat()))
print('Облачность ' + str(weather.get_clouds()))
print('Статус ' + str(weather.get_detailed_status()))
print('Давление ' + str(weather.get_pressure()))
print('Дождь ' + str(weather.get_rain()))
print('Снег ' + str(weather.get_snow()))
print('Время ' + str(weather.get_reference_time('iso')))
print('Статус ' + str(weather.get_status()))
print('Восход ' + str(weather.get_sunrise_time('iso')))
print('Закат ' + str(weather.get_sunset_time('iso')))
print('Температура ' + str(weather.get_temperature('celsius')))
print('Видимость ' + str(weather.get_visibility_distance()))
print('Изображение ' + weather.get_weather_icon_name())
print('Ветер ' + str(weather.get_wind()))
print('   ')

translate = {'Rostov-on-Don': 'Ростов-на-Дону'}
print('Погода в городе ' + translate[location.get_name()] + ' ' +
      WhatIscloudness() + ', температура ' +
      str(weather.get_temperature('celsius')['temp']) + ' градусов цельсия ' +
      ' скорость ветра ' + str(weather.get_wind()['speed']) + ' м/с. ')

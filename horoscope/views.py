# application views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}


def index(request):
    zodiacs = list(zodiac_dict)  # принимаем список всех знаков зодиака
    zodiac_items = ''
    for sign in zodiacs:
        url_redirect = reverse('hrscp', args=[sign])
        zodiac_items += f'<li><a href="{url_redirect}">{sign.title()}</a></li>'
    response = f"""
    <ol>
        {zodiac_items}
    </ol>
    """
    return HttpResponse(response)


def get_info_about_zodiac_sign(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(f"<h2>{description}</h2>")
    else:
        return HttpResponseNotFound(f"Знак зодиака не найден {sign_zodiac}")


def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)  # преобразуем словарь в лист, для обращения по номеру
    if sign_zodiac > len(zodiacs) and sign_zodiac > 0:
        return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака {zodiacs}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    url_redirect = reverse('hrscp', args=(name_zodiac,))
    return HttpResponseRedirect(url_redirect)

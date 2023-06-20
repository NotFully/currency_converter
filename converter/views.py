from django.shortcuts import render
import requests


def convert_currency(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        base_currency = request.POST['base_currency']
        target_currency = request.POST['target_currency']

        # Получаем текущий курс валюты от ЦБ РФ
        response = requests.get(f"https://www.cbr-xml-daily.ru/daily_json.js")
        rates = response.json()['Valute']
        if base_currency == 'RUB' or target_currency == 'RUB':
            if base_currency != target_currency and target_currency == 'RUB':
                return render(request, 'converter/result.html',
                              {'converted_amount': str(amount * rates[base_currency]['Value']) + " " + base_currency})
            elif base_currency != target_currency and base_currency == 'RUB':
                return render(request, 'converter/result.html',
                              {'converted_amount': str(amount / rates[target_currency]['Value']) + " " + target_currency})
            else:
                return render(request, 'converter/result.html',
                              {'converted_amount': str(amount) + " " + base_currency})
        else:
            base_rate = rates[base_currency]['Value']
            target_rate = rates[target_currency]['Value']

            # Конвертируем сумму в целевую валюту
            converted_amount = amount * (base_rate / target_rate)

            return render(request, 'converter/result.html',
                          {'converted_amount': str(converted_amount) + " " + target_currency})

    return render(request, 'converter/convert.html')

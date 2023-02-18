proceeds = int (input('Введите вашу выручку: '))
costs = int (input('Введите ваши издержки: '))
if proceeds>costs:
    profit = proceeds - costs
    profiability = profit/1000
    print (f'Фирма отработала с прибылью в размере: {profit}, рентабельность выручки составляет: {profiability}')
    count_of_emp = int (input('Введите число сотрудников: '))
    profit_to_empl = profit / count_of_emp
    print (f'Прибыль в расчете на одного сотрудника: {profit_to_empl}')
else:
    lesion = proceeds - costs
    profiability = lesion / 1000
    print (f'Фирма отработала с убытком в размере: {lesion}, рентабельность выручки составляет: {profiability} ')
    count_of_emp = int (input('Введите число сотрудников: '))
    profit_to_empl = lesion / count_of_emp
    print (f'Прибыль в расчете на одного сотрудника: {profit_to_empl}')


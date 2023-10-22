money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
k_increase = increase + 1  # Множитель увеличения расходов
count_month = 0  # Счётчик месяцев
budget = money_capital  # Бюджет, за рамки которого нельзя выходить

while budget > 0:
    count_month += 1
    spend *= k_increase
    budget += salary - spend

print("Количество месяцев, которое можно протянуть без долгов:", count_month)

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = salary + money_capital - spend  # Бюджет на второй месяц
expenses = spend  # расходы 1 месяца
live = 1 # Номер месяца, который уже прожит
count = 0 # Количество циклов = количеству месяцев жизни
while budget + salary > expenses * (1+increase):
    expenses += (expenses * increase) # расходы на count месяц
    budget += salary
    budget -= expenses
    count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count+live)

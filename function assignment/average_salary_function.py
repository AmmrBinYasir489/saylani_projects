def average(salary, employes):
    total = 0
    for item in salary:
        total += item 
    return total / employes

salaries = [20000, 10000, 30000]
employe = 3
print(f"The average salary of {employe} employees = {average(salaries, employe)}")
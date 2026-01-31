import pathlib 

current_dir = pathlib.Path(__file__).parent 

def total_salary(path): 
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                try:
                    salary = int(line.strip().split(',')[-1].strip())
                    salaries.append(salary)
                except (ValueError, IndexError):
                    continue 
            
            if not salaries:
                return 0, 0, 0 
            total = sum(salaries)
            count = len(salaries)
            average = total / count if count > 0 else 0
            return total, count, average
    except FileNotFoundError:
        print("Файл не найден.")
         
path = current_dir / "total_salary.txt"
result = total_salary(path)
if isinstance(result, tuple):
    total, _, average = result
    print(f"Общая сумма зарплат: {total} а средняя зарплата: {average:.2f}")

else:
    print(result)
    


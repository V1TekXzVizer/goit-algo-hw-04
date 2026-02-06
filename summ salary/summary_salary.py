import pathlib 

current_dir = pathlib.Path(__file__).parent 

def total_salary(path): 
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                try:
                    parts = line.strip().split(',')
                    if len(parts) >= 2:
                        salary = float(parts[-1].strip())
                        salaries.append(salary)
                except (ValueError, IndexError):
                    continue 
            
            if not salaries:
                return 0, 0  
            total = sum(salaries)
            average = total / len(salaries)
            return total, average  
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
         
path = current_dir / "total_salary.txt"
result = total_salary(path)

if result is not None:
    total, average = result
    print(f"Загальна сума зарплат: {total}, Середня зарплата: {average:.2f}")


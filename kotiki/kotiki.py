# У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.

import pathlib 

current_dir = pathlib.Path(__file__).parent 

def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    parts = line.strip().split(',')
                    cat_id = parts[0].strip()
                    name = parts[1].strip()
                    age = parts[2].strip()
                    cat_info = {"id": cat_id, "name": name, "age": age}
                    cats.append(cat_info)

                except (ValueError, IndexError):
                    continue

            if not cats:
                return "Файл не містить інформації про котів."
            
            return cats    
    except FileNotFoundError:
        return "Файл не знайдено." 
    
path = current_dir / "kotikiname.txt"
result = get_cats_info(path)
if isinstance(result, list):
    print(result)
else:
    print(result)

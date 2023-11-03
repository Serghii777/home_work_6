from datetime import datetime, date, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    current_date = datetime.today().date()
    
    # Ініціалізуємо словник для зберігання користувачів на кожний день тижня
    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }
    if users == [{}] :
        return birthdays_per_week
    
    for user in users:
            # Перевіряємо, чи має користувач день народження в цьому році
            birthday_this_year = current_date.replace(month=user['birthday'].month, day=user['birthday'].day)
            
            # Якщо день народження вже минув цього року
            if birthday_this_year < current_date:
                return birthdays_per_week
                # Додаємо 1 рік до дня народження
            birthday_this_year = current_date.replace(year=current_date.year + 1, month=user['birthday'].month, day=user['birthday'].day)
            
            # Перевіряємо, чи день народження є у наступному тижні
            if current_date <= birthday_this_year <= current_date + timedelta(days=6):
                # Отримуємо день тижня для дня народження користувача
                day_of_week = birthday_this_year.strftime('%A')
                # Додаємо ім'я користувача до відповідного дня тижня в словнику
                birthdays_per_week[day_of_week].append(user['name'])
            
            # Якщо користувач має народився на вихідні, переносимо його на понеділок
            if birthday_this_year.weekday() >= 5:
                next_monday = current_date + timedelta(days=(7 - current_date.weekday()))
                # Перевіряємо, чи день народження попадає на наступний тиждень
                if next_monday <= birthday_this_year <= next_monday + timedelta(days=6):
                    # Отримуємо день тижня для дня народження користувача
                    day_of_week = birthday_this_year.strftime('%A')
                    # Додаємо ім'я користувача до відповідного дня тижня в словнику
                    birthdays_per_week[day_of_week].append(user['name'])
    
    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

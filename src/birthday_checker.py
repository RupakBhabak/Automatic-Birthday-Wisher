# Modules
from datetime import date
from file_manager import FileManager

# Main
class BirthDayChecker:
    def __init__(self):
        pass

    @staticmethod
    def check_for_birthday():
        today_date = date.today()
        persons_data = FileManager.load_persons_data()
        
        ids = persons_data["ids"]
        result = {}

        for id in ids:
            if persons_data[id]["birth_day"] == today_date.day and persons_data[id]["birth_month"] == today_date.month:
                result[id] = persons_data[id]

        if result == {}:
            return None
        else:
            return result

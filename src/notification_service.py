# Modules
from time import sleep
from win11toast import toast

# Main
class NotificationService:
    def __init__(self):
        pass

    @staticmethod
    def push_notification(person_data: dict, wait_time: int = 0):
        sleep(wait_time)


# Modules
import sys

from birthday_checker import BirthDayChecker

# Main
class App:
    def __init__(self):
        pass

    def run(self):
        result = BirthDayChecker.check_for_birthday()

        if not result:
            sys.exit(0)

        

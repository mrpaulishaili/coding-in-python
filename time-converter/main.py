"""
    ---   Meta Information   ---
    Time Converter Program
    Written in Python
    Developed by: Paul Ishaili C.
"""
import time
from args_splitter import split_phrase_argument as phrase
from time_units import time_units


def welcome_user():
    print(""" 🤗 What do you want to convert?""")
    time.sleep(.5)
    return


def TimeConverter():
    def get_input():
        user_input = input("""Entry time format: 👉 value, convert_from, convert_to👉: """)
        return user_input

    def validate_input():

        if entry != "":

            if entry == 'exit':
                print(' 🤗 Done. Thank you!')
                exit()

            user_confirm = input(f"""Do you mean you want to convert {entry}?""")

            if user_confirm == 'yes':
                argument = {
                    "convert": phrase(entry)[0],
                    "from": phrase(entry)[1].rstrip(""),
                    "to": phrase(entry)[2]
                }
                print(argument)
                return
        else:
            print('⚠ invalid entry!')
            time.sleep(.3)
            TimeConverter()

    def execute_action():
        try:
            pass
        except ValueError:
            pass

    def return_response():
        pass

    entry = get_input()
    validate_input()


welcome_user()
while True:
    TimeConverter()

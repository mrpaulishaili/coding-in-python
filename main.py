# TIME UNIT CONVERTER

# --- 1.

units_of_time = {'sec': 'seconds', 'min': 'minutes', 'hr': 'hours', 'd': 'days', 'wk': 'weeks', 'mth': 'months',
                 'yr': 'years'}
hours_in_a_day = 24
minutes_per_hour = 60
seconds_per_minute = 60

calculation_units = hours_in_a_day
name_of_unit = units_of_time['hr']

user_input = ""


def convert_value_to_unit(data_input):
    return print(f"{data_input} days are {data_input * calculation_units} {name_of_unit}")


def validate_input():
    if user_input != 'exit':
        if user_input.isdigit():
            set_input_to_int()
        else:
            return print('invalid input')
    else:
        return


def set_input_to_int():
    value_to_convert = int(user_input)

    if value_to_convert > 0:
        convert_value_to_unit(value_to_convert)
    else:
        return print('You entered an invalid input!')


while user_input != 'exit':
    user_input = input('Enter value to convert to ' + name_of_unit + ": ")
    validate_input()

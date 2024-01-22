def days_to_units (number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"\nGreat, {number_of_days} days are {number_of_days * 24} hours."
    elif conversion_unit == "minutes":
        return f"\nAwsome, {number_of_days} days are {number_of_days * 24 * 60} minutes."
    else: 
        return "unsupported unit"
    

def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("\nYou have entered a 0. Kindly input a positive number.\n\n")
        else:
            print("\nYou have enetered a negative number. Just stop doing it!\n\n")
    
    except:
        print("\nYour input isn't a valid number. Don't ruin my program!\n\n")

user_input_message = "\nHey, enter a number of days and convestion unit!\n\n"
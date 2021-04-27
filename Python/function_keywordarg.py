# Make a function with String

def message_a(name, date, hobby, intrest):
    message = "My name is " + name
    message += ". His birth date is " + str(date)
    message += ". His hobby is " + hobby
    message += name + "have intrest about " + intrest

    return message


def message_b(first_param, *second_param, **third_param):
    # First parameter is single object
    # Second parameter has a meaning tuple data
    # Third parameter has a meaning dictionarie data
    return second_param


message_b("Nayaka",
          "Al",
          "Syahreal",
          alpha='Nayaka',
          beta='Kanaka'
          )

def format_name(f_name, l_name):
    """Take the first name and last name
    to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formated_f_name} {formatted_l_name}"


x = format_name("sArThAk", "sHarMa")
print(x)


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))
def prompt_text(prompt):
    value = input(prompt).lower()

    while True:
        if value:
            return value
        else:
            print("This fleid can't be empty")
            continue
        

def valid_isbn():
    while True:
        value = input("Enter Isbn no. : ")
        if len(value) == 13 and value.isdigit():
            return int(value)
        else:
            print("This should be 13 digit positive integer")
            continue


    


      






while True:
    try:
        age = int(input("How Old are you weirdo? "))
        if age < 0 or age > 120:
            raise ValueError
        if age <= 17:
            print("Oh Boy, You are still a minor, child")
        elif age >= 18 and age <= 64:
            print("Damn, You are definitly an adult, man")
        elif age >= 65:
            print("Bro, You are senior, When are you gonna see God")
        break
    except ValueError:
        pass

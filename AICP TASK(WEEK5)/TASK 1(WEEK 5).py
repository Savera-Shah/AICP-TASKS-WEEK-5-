def calculate_price(day, arrival_hour, hours_parked, frequent_parking_number):
    MAX_STAY = {
        "sunday": 8, "monday": 2, "tuesday": 2, "wednesday": 2,
        "thursday": 2, "friday": 2, "saturday": 4
    }
    PRICES = {
        "sunday": {"day_price": 2.00, "night_price": 2.00},
        "monday": {"day_price": 10.00, "night_price": 2.00},
        "tuesday": {"day_price": 10.00, "night_price": 2.00},
        "wednesday": {"day_price": 10.00, "night_price": 2.00},
        "thursday": {"day_price": 10.00, "night_price": 2.00},
        "friday": {"day_price": 10.00, "night_price": 2.00},
        "saturday": {"day_price": 3.00, "night_price": 2.00}
    }
    DISCOUNT_HOUR_START = 16
    DISCOUNT_PERCENTAGE = 0.5
    OTHER_DISCOUNT_PERCENTAGE = 0.1

    if arrival_hour < 8:
        return "No parking is allowed between Midnight and 08:00."

    if day not in MAX_STAY or arrival_hour < 0 or arrival_hour > 23 or hours_parked < 1:
        return "Invalid input."

    max_stay = MAX_STAY[day]
    if hours_parked > max_stay:
        return f"Maximum stay on {day} is {max_stay} hours."

    discount_percentage = DISCOUNT_PERCENTAGE if arrival_hour >= DISCOUNT_HOUR_START else OTHER_DISCOUNT_PERCENTAGE
    price_per_hour = PRICES[day]["night_price"] if arrival_hour >= DISCOUNT_HOUR_START else PRICES[day]["day_price"]
    discounted_price_per_hour = price_per_hour * (1 - discount_percentage)
    total_price = discounted_price_per_hour * hours_parked

    if frequent_parking_number and not validate_frequent_parking_number(frequent_parking_number):
        return "Invalid frequent parking number. No discount applied."

    return f"Price to park: ${total_price:.2f}"


def validate_frequent_parking_number(number):
    if len(number) != 5:
        return False

    check_digit = int(number[-1])
    number = number[:-1]

    total = sum(int(digit) * (i + 1) for i, digit in enumerate(number))
    remainder = total % 11
    calculated_check_digit = 0 if remainder == 0 else 11 - remainder

    return calculated_check_digit == int(check_digit)


# Test the program
print("car park payment system \n Calculating the price to park."  )
day = input("Enter the day of the week : ")
arrival_hour = int(input("Enter the hour of arrival (0-23): "))
hours_parked = int(input("Enter the number of hours to park: "))
frequent_parking_number = input("Enter frequent parking number (if available): ")

print(calculate_price(day, arrival_hour, hours_parked, frequent_parking_number))

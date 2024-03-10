def calculate_price(day, arrival_hour, hours_parked, frequent_parking_number):
    MAX_STAY = {
        "Sunday": 8, "Monday": 2, "Tuesday": 2, "Wednesday": 2,
        "Thursday": 2, "Friday": 2, "Saturday": 4
    }
    PRICES = {
        "Sunday": {"day_price": 2.00, "night_price": 2.00},
        "Monday": {"day_price": 10.00, "night_price": 2.00},
        "Tuesday": {"day_price": 10.00, "night_price": 2.00},
        "Wednesday": {"day_price": 10.00, "night_price": 2.00},
        "Thursday": {"day_price": 10.00, "night_price": 2.00},
        "Friday": {"day_price": 10.00, "night_price": 2.00},
        "Saturday": {"day_price": 3.00, "night_price": 2.00}
    }
    DISCOUNT_HOUR_START = 16
    DISCOUNT_PERCENTAGE = 0.5
    OTHER_DISCOUNT_PERCENTAGE = 0.1

    if arrival_hour < 8:
        return "No parking is allowed between Midnight and 08:00."

    day = day.capitalize()

    if day not in MAX_STAY or arrival_hour < 0 or arrival_hour > 23 or hours_parked < 1:
        return "Invalid input."

    max_stay = MAX_STAY[day]
    if hours_parked > max_stay:
        return f"Maximum stay on {day} is {max_stay} hours."

    # Calculate price before discount threshold
    price_before_discount = min(hours_parked, max_stay) * PRICES[day]["day_price"]

    # Calculate evening charge if applicable
    if arrival_hour < DISCOUNT_HOUR_START and arrival_hour + hours_parked > DISCOUNT_HOUR_START:
        evening_hours = max(0, arrival_hour + hours_parked - DISCOUNT_HOUR_START)
        price_evening = evening_hours * PRICES[day]["night_price"]
    else:
        price_evening = 0

    # Apply discount percentage based on arrival time
    if arrival_hour >= DISCOUNT_HOUR_START:
        discount_percentage = DISCOUNT_PERCENTAGE
    else:
        discount_percentage = OTHER_DISCOUNT_PERCENTAGE

    # Calculate total price
    total_price = price_before_discount + price_evening
    total_price *= (1 - discount_percentage)

    # Apply discount for frequent parking number if valid
    if frequent_parking_number and not validate_frequent_parking_number(frequent_parking_number):
        return "Invalid frequent parking number. No discount applied."

    return total_price


def validate_frequent_parking_number(number):
    if len(number) != 5:
        return False

    check_digit = int(number[-1])
    number = number[:-1]

    total = sum(int(digit) * (i + 1) for i, digit in enumerate(number))
    remainder = total % 11
    calculated_check_digit = 0 if remainder == 0 else 11 - remainder

    return calculated_check_digit == int(check_digit)


def main():
    day = input("Enter the day of the week: ")
    arrival_hour = float(input("Enter the hour of arrival (0-23): "))
    hours_parked = float(input("Enter the number of hours to park: "))
    frequent_parking_number = input("Enter frequent parking number (if available): ")

    price = calculate_price(day, arrival_hour, hours_parked, frequent_parking_number)
    if isinstance(price, str):
        print(price)
    else:
        print(f"Price to park: ${price:.2f}")


main()

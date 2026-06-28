from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def print_header():
    print("=" * 34)
    print("      AUSTRALIAN GST CALCULATOR")
    print("=" * 34)

print_header()

GST_RATE = Decimal("0.10")
CENT = Decimal("0.01")


def format_money(amount):
    return f"${amount.quantize(CENT, rounding=ROUND_HALF_UP):,.2f}"


def calculate_gst_exclusive(amount):
    gst = (amount * GST_RATE).quantize(CENT, rounding=ROUND_HALF_UP)
    total = amount + gst
    return gst, total


def calculate_gst_inclusive(amount):
    gst = (amount / Decimal("11")).quantize(CENT, rounding=ROUND_HALF_UP)
    exclusive = amount - gst
    return gst, exclusive


def parse_money(value):
    cleaned_value = value.strip().replace("$", "").replace(",", "")

    if not cleaned_value:
        raise ValueError("Amount is required.")

    try:
        amount = Decimal(cleaned_value)
    except InvalidOperation as error:
        raise ValueError("Enter a valid dollar amount, such as 100 or 99.95.") from error

    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    return amount.quantize(CENT, rounding=ROUND_HALF_UP)


def get_menu_choice():
    print("Australian GST Calculator")
    print("--------------------------")
    print("1. GST exclusive sale")
    print("2. GST inclusive sale")
    print("3. GST-free or input-taxed sale")

    while True:
        choice = input("Select option (1, 2, or 3): ").strip()

        if choice in {"1", "2", "3"}:
            return choice

        print("Invalid option. Please enter 1, 2, or 3.")


def get_amount():
    while True:
        try:
            return parse_money(input("Enter amount: "))
        except ValueError as error:
            print(f"Invalid amount: {error}")


def print_result(label, amount, gst, net_amount, total):
    print(f"\n{label}")
    print("--------------------------")
    print(f"Original amount: {format_money(amount)}")
    print(f"GST amount:      {format_money(gst)}")
    print(f"Net amount:      {format_money(net_amount)}")
    print(f"Total amount:    {format_money(total)}")


def main():
    choice = get_menu_choice()
    amount = get_amount()

    if choice == "1":
        gst, total = calculate_gst_exclusive(amount)
        print_result("GST exclusive calculation", amount, gst, amount, total)
    elif choice == "2":
        gst, exclusive = calculate_gst_inclusive(amount)
        print_result("GST inclusive calculation", amount, gst, exclusive, amount)
    else:
        print_result("GST-free/input-taxed calculation", amount, Decimal("0.00"), amount, amount)


if __name__ == "__main__":
    main()

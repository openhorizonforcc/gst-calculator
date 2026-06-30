from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from gst_utils import calculate_gst_exclusive

GST_RATE = Decimal("0.10")
CENT = Decimal("0.01")


def print_header():
    """Display the calculator title at the top of the program."""
    print("=" * 34)
    print("      AUSTRALIAN GST CALCULATOR")
    print("=" * 34)


def format_money(amount):
    """Format a Decimal amount as Australian dollars rounded to cents."""
    return f"${amount.quantize(CENT, rounding=ROUND_HALF_UP):,.2f}"


def calculate_gst_exclusive(amount):
    """Calculate GST and total price for an amount that excludes GST."""
    gst = (amount * GST_RATE).quantize(CENT, rounding=ROUND_HALF_UP)
    print("DEBUG: amount =", amount)
    print("DEBUG: gst =", gst)
    
    total = amount + gst
    print("DEBUG: total =", total)

    return gst, total


def calculate_gst_inclusive(amount):
    """Extract GST and net price from an amount that already includes GST."""
    gst = (amount / Decimal("11")).quantize(CENT, rounding=ROUND_HALF_UP)
    exclusive = amount - gst
    return gst, exclusive


def parse_money(value):
    """Convert user-entered money text into a valid Decimal amount."""
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
    """Ask the user to choose which GST calculation they want to perform."""
    print("1. GST exclusive sale")
    print("2. GST inclusive sale")
    print("3. GST-free or input-taxed sale")

    while True:
        choice = input("Select option (1, 2, or 3): ").strip()

        if choice in {"1", "2", "3"}:
            return choice

        print("Invalid option. Please enter 1, 2, or 3.")


def get_amount():
    """Ask the user for an amount until they enter a valid money value."""
    while True:
        try:
            return parse_money(input("Enter amount: "))
        except ValueError as error:
            print(f"Invalid amount: {error}")
            

def print_result(label, amount, gst, net_amount, total):
    """Display the completed GST calculation in a readable format."""
    print(f"\n{label}")
    print("--------------------------")
    print(f"Original amount: {format_money(amount)}")
    print(f"GST amount:      {format_money(gst)}")
    print(f"Net amount:      {format_money(net_amount)}")
    print(f"Total amount:    {format_money(total)}")


def calculate_result(choice, amount):
    """Run the selected GST calculation and return the values to display."""
    if choice == "1":
        gst, total = calculate_gst_exclusive(amount)
        return "GST exclusive calculation", gst, amount, total

    if choice == "2":
        gst, exclusive = calculate_gst_inclusive(amount)
        return "GST inclusive calculation", gst, exclusive, amount

    return "GST-free/input-taxed calculation", Decimal("0.00"), amount, amount


def main():
    """Run the command-line GST calculator from start to finish."""
    print_header()
    choice = get_menu_choice()
    amount = get_amount()
    label, gst, net_amount, total = calculate_result(choice, amount)
    print_result(label, amount, gst, net_amount, total)


if __name__ == "__main__":
    main()


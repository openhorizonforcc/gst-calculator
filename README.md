# Australian GST Calculator

A simple Python command-line application for calculating Australian Goods and Services Tax (GST).

The calculator supports GST-exclusive, GST-inclusive, and GST-free/input-taxed sale amounts. It uses decimal currency arithmetic so results round predictably to cents.

## Features

- Calculate 10% GST on a GST-exclusive amount
- Extract GST from a GST-inclusive amount
- Record GST-free or input-taxed amounts with zero GST
- Validate blank, invalid, and negative amounts
- Accept common money formats such as `100`, `99.95`, `$100`, and `1,250.50`
- Display values as Australian dollar amounts
- Keep GST calculation logic in reusable functions

## Example

GST-exclusive sale:

```text
Australian GST Calculator
--------------------------
1. GST exclusive sale
2. GST inclusive sale
3. GST-free or input-taxed sale
Select option (1, 2, or 3): 1
Enter amount: 100

GST exclusive calculation
--------------------------
Original amount: $100.00
GST amount:      $10.00
Net amount:      $100.00
Total amount:    $110.00
```

GST-inclusive sale:

```text
Select option (1, 2, or 3): 2
Enter amount: $110

GST inclusive calculation
--------------------------
Original amount: $110.00
GST amount:      $10.00
Net amount:      $100.00
Total amount:    $110.00
```

## Requirements

- Python 3.9 or later

No external packages are required.

## How to Run

Clone the repository:

```bash
git clone https://github.com/openhorizonforcc/gst-calculator.git
```

Navigate to the project folder:

```bash
cd gst-calculator
```

Run the program:

```bash
python gst_calculator.py
```

## Production-Readiness Improvements Added

- Replaced `float` with `Decimal` for currency-safe calculations
- Added validation for invalid, blank, and negative amounts
- Split calculation logic into reusable functions
- Added support for GST-free and input-taxed sales
- Improved output formatting for business-friendly dollar values

## Suggested Next Steps

- Add automated tests for rounding, invalid input, inclusive GST, and exclusive GST
- Export calculations to CSV for record keeping
- Generate invoice or receipt PDFs with business name, ABN, date, GST treatment, and totals
- Add configuration for business details and transaction categories
- Build a small web or desktop interface for non-technical users

## Version History

### Version 3.0

- Added decimal-based currency calculations
- Added input validation
- Added GST-free/input-taxed option
- Refactored calculation logic into functions
- Updated documentation and examples

### Version 2.0

- Added GST-exclusive calculations
- Added GST-inclusive calculations
- Added menu system
- Improved user experience

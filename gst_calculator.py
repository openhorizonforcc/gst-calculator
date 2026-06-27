print("Australian GST Calculator")
print("--------------------------")
print("1. GST Exclusive")
print("2. GST Inclusive")

choice = input("Select option (1 or 2): ")

amount = float(input("Enter amount: "))

if choice == "1":
    gst = amount * 0.10
    total = amount + gst

    print("\nGST Amount:", round(gst, 2))
    print("Total Including GST:", round(total, 2))

elif choice == "2":
    gst = amount / 11
    exclusive = amount - gst

    print("\nGST Amount:", round(gst, 2))
    print("GST Exclusive Amount:", round(exclusive, 2))

else:
    print("Invalid option selected.")
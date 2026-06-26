amount = float(input("Enter amount excluding GST: "))

gst = amount * 0.10
total = amount + gst

print(f"GST: ${gst:.2f}")
print(f"Total including GST: ${total:.2f}")
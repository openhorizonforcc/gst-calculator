def calculate_gst_exclusive(amount):
    gst = amount * 0.10
    total = amount + gst
    return gst, total
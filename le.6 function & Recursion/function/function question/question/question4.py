#waf to convert USD TO INR
def converter(usd_val):
    inr_val = usd_val * 93.20
    print(usd_val, "USD =", inr_val, "INR")

converter(float(input("Enter a number to convert USD to INR: ")))
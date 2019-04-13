def calculate(tar, mins, smss):
    summ = tar["abonplata"]
    if mins > tariff["minutes"]:
        summ_mins = (mins - tariff["minutes"]) * tariff["per_minute"]
        summ += summ_mins
    if smss > tariff["sms"]:
        summ_sms = (smss - tariff["sms"]) * tariff["per_sms"]
        summ += summ_sms
    return summ


print("Input tariff data...")
tariff = {
    "minutes": int(input("Number of minutes: ")),
    "sms": int(input("Number of sms: ")),
    "abonplata": float(input("Abonplata: ")),
    "per_minute": float(input("Per minute tariff: ")),
    "per_sms": float(input("Per sms tariff: "))
}
print("\nInput data per month to calculate...")
minutes = int(input("Minutes: "))
sms = int(input("SMS: "))

print("Total is " + str(calculate(tariff, minutes, sms)))

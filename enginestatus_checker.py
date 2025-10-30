print("Car Engine Status Checker 🚘")
print("-----------------------------\n")

# Collect key engine parameters from user
engine_temp = float(input("Enter engine temperature (°C): "))
oil_level = float(input("Enter oil level (in liters): "))
battery_voltage = float(input("Enter battery voltage (V): "))

print("\nChecking engine status...\n")

# Analyze engine temperature
if engine_temp < 70:
    print("🌡️ Engine temperature is LOW — allow the car to warm up.")
elif 70 <= engine_temp <= 100:
    print("✅ Engine temperature is NORMAL.")
else:
    print("🔥 Engine temperature is HIGH — stop the car and check the cooling system.")

# Analyze oil level
if oil_level < 2:
    print("🛢️ Oil level is LOW — add more engine oil.")
elif 2 <= oil_level <= 4:
    print("✅ Oil level is GOOD.")
else:
    print("⚠️ Oil level is TOO HIGH — reduce to recommended level.")

# Analyze battery voltage
if battery_voltage < 12:
    print("🔋 Battery voltage is LOW — check your battery or alternator.")
elif 12 <= battery_voltage <= 14.5:
    print("✅ Battery voltage is NORMAL.")
else:
    print("⚡ Battery voltage is TOO HIGH — possible charging system issue.")

print("\nEngine check complete. Drive safely! 🚗💨")


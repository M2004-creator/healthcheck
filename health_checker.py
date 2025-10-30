print("Welcome to HealthCheck USSD Service")
print("------------------------------------")
print("Dialing *123# ... Connected ✅\n")

print("SYMPTOM OPTIONS:")
print("1. Fever, headache, and fatigue")
print("2. Cough, sore throat, and chest pain")
print("3. Stomach pain, diarrhea, and nausea")
print("4. Joint pain, skin rash, and red eyes")

symptom_choice = input("Select your symptoms (1-4): ")

if symptom_choice == "1":
    print("\n🤒 Possible Diseases:")
    print("- Malaria")
    print("- Typhoid Fever")
    print("- Influenza")

elif symptom_choice == "2":
    print("\n😷 Possible Diseases:")
    print("- Common Cold")
    print("- COVID-19")
    print("- Pneumonia")

elif symptom_choice == "3":
    print("\n🤢 Possible Diseases:")
    print("- Food Poisoning")
    print("- Gastroenteritis")
    print("- Cholera")

elif symptom_choice == "4":
    print("\n🦠 Possible Diseases:")
    print("- Dengue Fever")
    print("- Chikungunya")
    print("- Allergic Reaction")

else:
    print("\n⚠️ Invalid choice. Please select between 1 and 4.")

print("\nThank you for using HealthCheck USSD Service. Stay healthy! 💚")
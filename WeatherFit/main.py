from recommendation_data import recommendation_dict

def get_temperature_level(temp):
    if temp < 15:
        return "cold"
    elif temp <= 25:
        return "mild"
    else:
        return "hot"

def is_valid_weather_condition(condition, temp):
    if condition == "snowy" and temp > 5:
        return False
    return True

def get_user_input():
    try:
        temp = int(input("Enter the current temperature (°C): "))
        if temp < -30 or temp > 50:
            print("❌ Error: Temperature should be between -30 and 50°C.")
            return None, None, None
    except ValueError:
        print("❌ Error: Please enter a valid number.")
        return None, None, None

    print("Choose the weather condition from:")
    valid_conditions = ["sunny", "rainy", "cloudy", "windy", "snowy"]
    for cond in valid_conditions:
        print(f"- {cond}")
    condition = input("Enter the weather condition: ").lower().strip()
    if condition not in valid_conditions:
        print("❌ Error: Invalid weather condition.")
        return None, None, None

    if not is_valid_weather_condition(condition, temp):
        print("❌ Error: Snow is not realistic at this temperature.")
        return None, None, None

    print("Choose your preferred style from: casual / sporty / formal")
    style = input("Enter your preferred style: ").lower().strip()
    if style not in recommendation_dict:
        print("❌ Error: Invalid style.")
        return None, None, None

    return temp, condition, style

def recommend_outfit(temp, condition, style):
    temp_level = get_temperature_level(temp)
    try:
        return recommendation_dict[style][condition][temp_level]
    except KeyError:
        return "No exact outfit found. Try dressing in layers and consider weather protection."

def main():
    print("=== Welcome to WeatherFit (Simplified) ===")
    while True:
        temp, condition, style = get_user_input()
        if temp is None:
            print("🔁 Let's try again.\n")
            continue

        outfit = recommend_outfit(temp, condition, style)
        print(f"\n👕 Recommended outfit: {outfit}")

        again = input("\nWould you like another recommendation? (yes/no): ").lower().strip()
        if again != "yes":
            print("👋 Thanks for using WeatherFit. Stay comfy!")
            break

if __name__ == "__main__":
    main()
